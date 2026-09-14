"""File update package deployer — apply a package of updated documents."""

name = "fup"
label = "FUP"
description = "Apply update packages"

import argparse
import datetime
import difflib
import json
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MANIFEST_NAME = "_manifest.json"
PACKAGE_SUFFIX = ".zip"
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

CONVENTION_FOLDER_NAMES = (
    "_fileupdatepackages",
    "_binder",
    "_aide",
    "_rebuild",
)

NAMING_SIMILARITY = 0.85

REPORT_KINDS = (
    "REPLACED",
    "WOULD REPLACE",
    "CREATED",
    "WOULD CREATE",
    "MOVED",
    "WOULD MOVE",
    "DELETED",
    "WOULD DELETE",
    "CONFLICT",
    "SKIPPED",
    "INVALID",
    "BINDER",
    "PROCESSED",
    "WOULD PROCESS",
    "ERROR",
)


# ---------------------------------------------------------------------------
# Record types
# ---------------------------------------------------------------------------

@dataclass
class Event:
    kind: str
    folder: Path
    detail: str


@dataclass
class ManifestEntry:
    path: str          # as written in the manifest
    action: str        # "create", "replace", or "move"
    replaces: str      # filename being replaced, or ""
    relative: Path     # validated path for create/replace
    old_path: Path     # for move: source path relative to root
    new_path: Path     # for move: destination path relative to root


@dataclass
class Manifest:
    description: str = ""
    user_instructions: str = ""
    entries: list = field(default_factory=list)


@dataclass
class Outcome:
    package: Path = None
    package_line: str = ""
    description: str = ""
    instructions: str = "none in this package"
    binder: str = "not triggered"
    package_state: str = "left in the drop folder"
    entry_count: int = 0
    naming: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Path forms
# ---------------------------------------------------------------------------

def tidy_setting_text(value, label):
    text = str(value).strip().replace("\\", "/")
    if not text:
        raise ValueError(
            'Setting "{}" contains an empty path.'.format(label))
    return text


def resolve_path(text, label, base, root=None):
    if text.startswith("~"):
        anchor = root if root is not None else base
        if anchor is None:
            raise ValueError(
                'Setting "{}" cannot use "~/", because no root is defined.'
                .format(label))
        if not text.startswith("~/"):
            raise ValueError(
                'Setting "{}": "~" means the root folder, so it has to be '
                'written as "~/something".'.format(label))
        return (anchor / text[2:]).resolve()
    path = Path(text)
    if not path.is_absolute():
        if WINDOWS_DRIVE.match(text):
            raise ValueError(
                'Setting "{}" is "{}", which looks like a Windows path, but '
                "this is not Windows.".format(label, text))
        path = base / path
    return path.resolve()


def normalise(path):
    return Path(os.path.normcase(str(path)))


def is_inside(path, folder):
    try:
        normalise(path).relative_to(normalise(folder))
        return True
    except ValueError:
        return False


def relative_to(path, root):
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


# ---------------------------------------------------------------------------
# Finding the package
# ---------------------------------------------------------------------------

def find_packages(drop_folder):
    if not drop_folder.is_dir():
        return []
    packages = []
    for entry in sorted(drop_folder.iterdir()):
        if not entry.is_file():
            continue
        if entry.suffix.lower() != PACKAGE_SUFFIX:
            continue
        try:
            modified = entry.stat().st_mtime
        except OSError:
            modified = 0.0
        packages.append((modified, os.path.normcase(entry.name), entry))
    packages.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [entry for _modified, _name, entry in packages]


def describe_package(path):
    try:
        stat = path.stat()
    except OSError:
        return path.name
    when = datetime.datetime.fromtimestamp(stat.st_mtime)
    return "{}  ({}, {:,} bytes)".format(
        path.name, when.strftime("%Y-%m-%d %H:%M"), stat.st_size)


# ---------------------------------------------------------------------------
# Manifest reading and validation
# ---------------------------------------------------------------------------

def safe_relative_path(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("the path is empty")
    tidied = text.strip().replace("\\", "/")
    while tidied.startswith("./"):
        tidied = tidied[2:]
    if tidied.startswith("/") or Path(tidied).is_absolute():
        raise ValueError('"{}" is an absolute path'.format(text))
    if WINDOWS_DRIVE.match(tidied):
        raise ValueError('"{}" names a drive'.format(text))
    segments = [part for part in tidied.split("/") if part and part != "."]
    if not segments:
        raise ValueError('"{}" does not name a file'.format(text))
    if ".." in segments:
        raise ValueError(
            '"{}" contains "..", which would write outside the documentation '
            "root".format(text))
    if tidied.endswith("/"):
        raise ValueError('"{}" names a folder, not a file'.format(text))
    return Path(*segments)


def read_manifest(archive, names):
    problems = []

    if MANIFEST_NAME not in names:
        return None, ["the package contains no {}".format(MANIFEST_NAME)]

    try:
        raw = archive.read(MANIFEST_NAME).decode("utf-8-sig")
    except (KeyError, OSError, zipfile.BadZipFile) as error:
        return None, ["{} could not be read: {}".format(MANIFEST_NAME, error)]
    except UnicodeDecodeError:
        return None, ["{} is not UTF-8 text".format(MANIFEST_NAME)]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        return None, [
            "{} is not valid JSON: {} (line {}, column {})"
            .format(MANIFEST_NAME, error.msg, error.lineno, error.colno)]

    if not isinstance(data, dict):
        return None, [
            "{} must contain a JSON object, but it contains {}"
            .format(MANIFEST_NAME, type(data).__name__)]

    manifest = Manifest(
        description=str(data.get("description", "")).strip(),
        user_instructions=str(data.get("user_instructions", "")).strip(),
    )

    listed = data.get("files")
    if not isinstance(listed, list) or not listed:
        return None, [
            '{} has no "files" list, or it is empty'.format(MANIFEST_NAME)]

    seen = {}
    for position, item in enumerate(listed, start=1):
        where = "files entry {}".format(position)
        if not isinstance(item, dict):
            problems.append("{} is not an object".format(where))
            continue

        action = str(item.get("action", "")).strip().lower()
        # Accept "update" as backward-compatible synonym for "replace"
        if action == "update":
            action = "replace"
        if action not in ("create", "replace", "move"):
            problems.append(
                '{} ({}): action is "{}", but it must be "create", "replace" '
                'or "move"'.format(
                    where, item.get("path", item.get("old_path", "")),
                    item.get("action", "")))
            continue

        if action == "move":
            # Move entries have old_path and new_path, no zip member
            try:
                old_relative = safe_relative_path(
                    item.get("old_path", ""))
            except ValueError as error:
                problems.append("{} old_path: {}".format(where, error))
                continue
            try:
                new_relative = safe_relative_path(
                    item.get("new_path", ""))
            except ValueError as error:
                problems.append("{} new_path: {}".format(where, error))
                continue

            old_key = os.path.normcase(str(old_relative))
            new_key = os.path.normcase(str(new_relative))
            if old_key in seen:
                problems.append(
                    "{}: old_path already referenced (entries {} and {})"
                    .format(where, seen[old_key], position))
                continue
            if new_key in seen:
                problems.append(
                    "{}: new_path already referenced (entries {} and {})"
                    .format(where, seen[new_key], position))
                continue
            seen[old_key] = position
            seen[new_key] = position

            manifest.entries.append(ManifestEntry(
                path="", action=action, replaces="",
                relative=None,
                old_path=old_relative, new_path=new_relative))
            continue

        # create or replace: requires a file in the zip
        try:
            relative = safe_relative_path(item.get("path", ""))
        except ValueError as error:
            problems.append("{}: {}".format(where, error))
            continue

        path = str(item.get("path", "")).strip().replace("\\", "/")

        replaces = str(item.get("replaces", "") or "").strip()
        if replaces and action != "replace":
            problems.append(
                '{} ({}): "replaces" is only meaningful on a replace'
                .format(where, path))
            continue
        if replaces and ("/" in replaces or "\\" in replaces):
            problems.append(
                '{} ({}): "replaces" is a filename, not a path - "{}" '
                "contains a folder separator".format(where, path, replaces))
            continue

        if path not in names:
            problems.append(
                '{}: the package does not contain "{}"'.format(where, path))
            continue

        key = os.path.normcase(str(relative))
        if key in seen:
            problems.append(
                '{} ({}): the same path is listed twice (entries {} and {})'
                .format(where, path, seen[key], position))
            continue
        seen[key] = position

        manifest.entries.append(ManifestEntry(
            path=path, action=action, replaces=replaces,
            relative=relative,
            old_path=None, new_path=None))

    if not manifest.entries and not problems:
        problems.append('{} lists no usable files'.format(MANIFEST_NAME))

    return manifest, problems


# ---------------------------------------------------------------------------
# User instructions gate
# ---------------------------------------------------------------------------

def acknowledge_instructions(instructions, dry_run):
    print("")
    print("=" * 72)
    print("INSTRUCTIONS FROM THIS PACKAGE")
    print("-" * 72)
    for line in instructions.splitlines() or [instructions]:
        print(line)
    print("=" * 72)

    if dry_run:
        print("(dry run - a live run would wait for you here)")
        return "present, shown; not gated in a dry run"

    if not sys.stdin or not sys.stdin.isatty():
        print("(no interactive console - continuing without acknowledgement)")
        return "present, shown; NOT acknowledged - no interactive console"

    try:
        input("\nPress Enter to continue with the deploy, "
              "or Ctrl+C to stop... ")
    except EOFError:
        return "present, shown; not acknowledged - console closed"
    return "present, shown and acknowledged"


# ---------------------------------------------------------------------------
# Deploying
# ---------------------------------------------------------------------------

def find_replaced_file(documentation_root, target, replaces):
    wanted = os.path.normcase(replaces)
    beside = target.parent / replaces
    if beside.is_file():
        return [beside]
    found = []
    for dirpath, dirnames, filenames in os.walk(documentation_root):
        dirnames[:] = sorted(dirnames)
        for filename in filenames:
            if os.path.normcase(filename) == wanted:
                found.append(Path(dirpath) / filename)
    return found


def delete_replaced(path, dry_run):
    """Delete the document being replaced from the working tree."""
    folder = path.parent
    if dry_run:
        return Event("WOULD DELETE", folder, path.name)
    try:
        path.unlink()
        return Event("DELETED", folder, path.name)
    except OSError as error:
        return Event("ERROR", folder,
                     "{} could not be deleted: {}".format(path.name, error))


def write_member(archive, member, target):
    data = archive.read(member)
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(data)
    return len(data)


def deploy_entry(archive, entry, documentation_root, dry_run):
    """Deploy one manifest entry. Returns (events, affected_paths)."""
    events = []
    affected = []

    if entry.action == "move":
        return deploy_move(entry, documentation_root, dry_run)

    target = (documentation_root / entry.relative).resolve()
    folder = target.parent

    if not is_inside(target, documentation_root):
        return [Event(
            "CONFLICT", documentation_root,
            "{}: resolves outside the documentation root and was not deployed"
            .format(entry.path))], []

    occupied = target.exists()

    if entry.action == "replace":
        wanted = entry.replaces or target.name
        matches = find_replaced_file(documentation_root, target, wanted)

        if len(matches) == 1:
            previous = matches[0]
            event = delete_replaced(previous, dry_run)
            events.append(event)
            cleared = event.kind in ("DELETED", "WOULD DELETE")

            if cleared:
                affected.append(previous)

            if normalise(previous) == normalise(target):
                if not cleared:
                    events.append(Event(
                        "CONFLICT", folder,
                        "{}: not deployed - {} could not be removed"
                        .format(entry.path, previous.name)))
                    return events, affected
                occupied = False
        elif not matches:
            events.append(Event(
                "SKIPPED", folder,
                '{}: nothing replaced - "{}" is not in the documentation '
                "tree".format(entry.path, wanted)))
        else:
            events.append(Event(
                "CONFLICT", folder,
                '{}: "{}" was found in {} places and none were removed ({})'
                .format(entry.path, wanted, len(matches),
                        ", ".join(relative_to(match, documentation_root)
                                  for match in matches))))

    if occupied:
        events.append(Event(
            "CONFLICT", folder,
            "{}: not deployed - a file already exists there and the package "
            "did not name it as replaced".format(entry.path)))
        return events, affected

    kind, would = (("CREATED", "WOULD CREATE") if entry.action == "create"
                   else ("REPLACED", "WOULD REPLACE"))
    if dry_run:
        events.append(Event(
            would, folder,
            "{}  ({:,} bytes)".format(entry.path,
                                       archive.getinfo(entry.path).file_size)))
        return events, affected

    try:
        written = write_member(archive, entry.path, target)
        affected.append(target)
        events.append(Event(kind, folder,
                            "{}  ({:,} bytes)".format(entry.path, written)))
    except (OSError, zipfile.BadZipFile, KeyError) as error:
        events.append(Event("ERROR", folder,
                            "{} could not be written: {}"
                            .format(entry.path, error)))
    return events, affected


def deploy_move(entry, documentation_root, dry_run):
    """Execute a move action. Returns (events, affected_paths)."""
    events = []
    affected = []

    old_target = (documentation_root / entry.old_path).resolve()
    new_target = (documentation_root / entry.new_path).resolve()

    if not is_inside(old_target, documentation_root):
        return [Event(
            "CONFLICT", documentation_root,
            "move: old_path resolves outside the documentation root"
        )], []
    if not is_inside(new_target, documentation_root):
        return [Event(
            "CONFLICT", documentation_root,
            "move: new_path resolves outside the documentation root"
        )], []

    old_folder = old_target.parent
    new_folder = new_target.parent

    if not old_target.is_file():
        events.append(Event(
            "CONFLICT", old_folder,
            "move: {} does not exist".format(
                relative_to(old_target, documentation_root))))
        return events, []

    if new_target.exists():
        events.append(Event(
            "CONFLICT", new_folder,
            "move: {} already exists".format(
                relative_to(new_target, documentation_root))))
        return events, []

    if dry_run:
        events.append(Event(
            "WOULD MOVE", old_folder,
            "{} -> {}".format(
                relative_to(old_target, documentation_root),
                relative_to(new_target, documentation_root))))
        return events, []

    try:
        new_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_target), str(new_target))
        affected.append(old_target)
        affected.append(new_target)
        events.append(Event(
            "MOVED", old_folder,
            "{} -> {}".format(
                relative_to(old_target, documentation_root),
                relative_to(new_target, documentation_root))))
    except OSError as error:
        events.append(Event(
            "ERROR", old_folder,
            "move failed: {}".format(error)))

    return events, affected


# ---------------------------------------------------------------------------
# Binder trigger
# ---------------------------------------------------------------------------

def trigger_binder(context, dry_run):
    """Run the binder builder. Returns (Event, summary phrase)."""
    if dry_run:
        return (Event("BINDER", context.project_root,
                      "would trigger binder rebuild"),
                "would be triggered (dry run)")

    try:
        from aide.utilities import binder as binder_module
        from aide.cli import Context

        binder_ctx = Context(
            context.all_settings.get("binder", {}),
            context.project_root,
            all_settings=context.all_settings)

        binder_module.run(binder_ctx)

        return (Event("BINDER", context.project_root,
                      "binder rebuild triggered"),
                "triggered")
    except Exception as error:
        return (Event("ERROR", context.project_root,
                      "binder builder failed: {}".format(error)),
                "FAILED - {}".format(error))


# ---------------------------------------------------------------------------
# Folder naming check
# ---------------------------------------------------------------------------

def check_folder_naming(documentation_root):
    findings = []
    for dirpath, dirnames, _filenames in os.walk(documentation_root):
        for folder_name in sorted(dirnames):
            lowered = folder_name.lower()
            if not lowered.startswith("_"):
                continue
            if lowered in CONVENTION_FOLDER_NAMES:
                continue
            close = difflib.get_close_matches(
                lowered, CONVENTION_FOLDER_NAMES, n=1,
                cutoff=NAMING_SIMILARITY)
            if close:
                folder = Path(dirpath) / folder_name
                findings.append(
                    (relative_to(folder, documentation_root), close[0]))
    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def count_kinds(events):
    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1
    return counts


def build_completion_summary(events, outcome, dry_run):
    counts = count_kinds(events)
    replaced = counts.get("REPLACED", 0) + counts.get("WOULD REPLACE", 0)
    created = counts.get("CREATED", 0) + counts.get("WOULD CREATE", 0)
    moved = counts.get("MOVED", 0) + counts.get("WOULD MOVE", 0)
    deleted = counts.get("DELETED", 0) + counts.get("WOULD DELETE", 0)
    conflicts = [event for event in events if event.kind == "CONFLICT"]
    errors = [event for event in events if event.kind == "ERROR"]
    invalid = [event for event in events if event.kind == "INVALID"]

    def row(label, value):
        return "  {:<22}{}".format(label, value)

    lines = []
    lines.append("=" * 72)
    lines.append("COMPLETION SUMMARY{}".format(
        "   (DRY RUN - nothing was changed)" if dry_run else ""))
    lines.append("-" * 72)

    if outcome.package is None:
        lines.append(row("package:", "none - nothing to deploy"))
    else:
        lines.append(row("package:", outcome.package.name))
        if outcome.description:
            lines.append(row("", outcome.description))

    lines.append(row("files replaced:", replaced))
    lines.append(row("files created:", created))
    lines.append(row("files moved:", moved))
    lines.append(row("files deleted:", deleted))

    lines.append(row("conflicts:", len(conflicts)))
    for event in conflicts:
        lines.append("    - {}".format(event.detail))

    lines.append(row("errors:", len(errors)))
    for event in errors:
        lines.append("    - {}".format(event.detail))

    if invalid:
        lines.append(row("package rejected:",
                         "nothing in it was deployed"))
        for event in invalid:
            lines.append("    - {}".format(event.detail))

    lines.append(row("user instructions:", outcome.instructions))
    lines.append(row("binder builder:", outcome.binder))
    lines.append(row("the package is now:", outcome.package_state))

    if outcome.naming:
        lines.append(row("folder naming:",
                         "{} folder(s) close to a convention name but not "
                         "matching it".format(len(outcome.naming))))
        for found, expected in outcome.naming:
            lines.append("    - {}  (expected \"{}\")".format(found, expected))
    else:
        lines.append(row("folder naming:", "no misspelled folders found"))

    lines.append("-" * 72)

    complete = (outcome.entry_count > 0
                and replaced + created + moved == outcome.entry_count
                and not conflicts)

    if errors or conflicts or invalid:
        if replaced + created + moved == 0:
            status = "FAILED - nothing was deployed"
        elif complete:
            status = ("COMPLETED WITH ERRORS - every file was deployed, but a "
                      "later step failed")
        else:
            status = "COMPLETED WITH ERRORS - the deploy is incomplete"
    elif outcome.package is None:
        status = "COMPLETED SUCCESSFULLY - there was nothing to do"
    elif dry_run:
        status = "COMPLETED SUCCESSFULLY - dry run, nothing was changed"
    else:
        status = "COMPLETED SUCCESSFULLY"

    lines.append(status)
    lines.append("=" * 72)
    return lines


def build_report(documentation_root, drop_folder, dry_run, events, outcome):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing changed)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("file update package   {}   {}".format(timestamp, mode))
    lines.append("documentation root: {}".format(documentation_root))
    lines.append("drop folder:        {}".format(drop_folder))
    if outcome.package is not None:
        lines.append("package:            {}".format(outcome.package_line))
        if outcome.description:
            lines.append("description:        {}".format(outcome.description))
    lines.append("-" * 72)

    if not events:
        lines.append("Nothing happened, which should not be possible - please "
                     "report this.")
    else:
        current_folder = None
        for event in events:
            if event.folder != current_folder:
                current_folder = event.folder
                lines.append("")
                lines.append("[{}]".format(
                    relative_to(event.folder, documentation_root)))
            lines.append("  {:<17} {}".format(event.kind, event.detail))

    counts = count_kinds(events)
    summary = ", ".join(
        "{} {}".format(counts[kind], kind.lower())
        for kind in REPORT_KINDS if kind in counts
    ) or "nothing to do"

    lines.append("")
    lines.append("-" * 72)
    lines.append("Result: {}".format(summary))
    lines.extend(build_completion_summary(events, outcome, dry_run))
    return lines


def append_to_log(log_path, lines):
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "a", encoding="utf-8", newline="\n") as log_file:
            log_file.write("\n".join(lines))
            log_file.write("\n\n")
    except OSError as error:
        print("WARNING: could not write the log file {}: {}".format(
            log_path, error))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def finish(events, outcome, documentation_root, drop_folder,
           dry_run, log_path):
    report_lines = build_report(documentation_root, drop_folder,
                                dry_run, events, outcome)
    print("\n".join(report_lines))
    append_to_log(log_path, report_lines)
    print("\nLog: {}".format(log_path))
    return 1 if any(event.kind == "ERROR" for event in events) else 0


def run(context):
    project_root = context.project_root
    settings = context.settings

    if project_root is None:
        print("No project root found (no _aide/ directory). "
              "Run aide from inside a project.")
        return

    parser = argparse.ArgumentParser(prog="aide fup", add_help=False)
    parser.add_argument("--dry-run", action="store_true")
    args, _unknown = parser.parse_known_args(context.argv)
    dry_run = args.dry_run

    documentation_root = project_root

    try:
        drop_setting = settings.get("drop_folder", "~/_fileupdatepackages")
        drop_folder = resolve_path(
            tidy_setting_text(drop_setting, "drop_folder"),
            "drop_folder", project_root, root=documentation_root)

        log_setting = settings.get("log_file",
                                   "~/_aide/file_update_package.log")
        log_path = resolve_path(
            tidy_setting_text(log_setting, "log_file"),
            "log_file", project_root, root=documentation_root)
    except ValueError as error:
        print("SETTINGS PROBLEM")
        print(error)
        return

    if not documentation_root.is_dir():
        print("SETTINGS PROBLEM")
        print("The documentation root does not exist:")
        print("  {}".format(documentation_root))
        return

    events = []
    outcome = Outcome()
    outcome.naming = check_folder_naming(documentation_root)

    packages = find_packages(drop_folder)

    if not packages:
        events.append(Event(
            "SKIPPED", drop_folder,
            "no packages found in {}".format(
                drop_folder if drop_folder.is_dir()
                else "{} (the folder does not exist)".format(drop_folder))))
        finish(events, outcome, documentation_root, drop_folder,
               dry_run, log_path)
        return

    package = packages[0]
    outcome.package = package
    outcome.package_line = describe_package(package)
    for waiting in packages[1:]:
        events.append(Event(
            "SKIPPED", drop_folder,
            "{}: waiting - only the newest package is processed in a run"
            .format(waiting.name)))

    # --- validate ---------------------------------------------------------
    if not zipfile.is_zipfile(package):
        events.append(Event("INVALID", drop_folder,
                            "{} is not a zip file".format(package.name)))
        finish(events, outcome, documentation_root, drop_folder,
               dry_run, log_path)
        return

    try:
        archive = zipfile.ZipFile(package)
    except (zipfile.BadZipFile, OSError) as error:
        events.append(Event("INVALID", drop_folder,
                            "{} could not be opened: {}"
                            .format(package.name, error)))
        finish(events, outcome, documentation_root, drop_folder,
               dry_run, log_path)
        return

    all_affected = []

    with archive:
        zip_names = set(archive.namelist())
        manifest, problems = read_manifest(archive, zip_names)

        if problems:
            for problem in problems:
                events.append(Event(
                    "INVALID", drop_folder,
                    "{}: {}".format(package.name, problem)))
            finish(events, outcome, documentation_root, drop_folder,
                   dry_run, log_path)
            return

        outcome.description = manifest.description
        outcome.entry_count = len(manifest.entries)

        # --- the gate -----------------------------------------------------
        if manifest.user_instructions:
            outcome.instructions = acknowledge_instructions(
                manifest.user_instructions, dry_run)

        # --- deploy -------------------------------------------------------
        for entry in manifest.entries:
            entry_events, affected = deploy_entry(
                archive, entry, documentation_root, dry_run)
            events.extend(entry_events)
            all_affected.extend(affected)

    counts = count_kinds(events)
    wrote_something = any(counts.get(kind) for kind in
                          ("REPLACED", "WOULD REPLACE",
                           "CREATED", "WOULD CREATE",
                           "MOVED", "WOULD MOVE"))
    incomplete = bool(counts.get("CONFLICT") or counts.get("ERROR"))

    # --- file the package away (delete) -----------------------------------
    if incomplete:
        outcome.package_state = ("left in the drop folder - the deploy was "
                                 "not complete")
    elif not wrote_something:
        outcome.package_state = "left in the drop folder - nothing was deployed"
    else:
        if dry_run:
            events.append(Event("WOULD PROCESS", drop_folder,
                                "{} would be deleted".format(package.name)))
            outcome.package_state = "would be deleted (dry run)"
        else:
            try:
                package.unlink()
                all_affected.append(package)
                events.append(Event("PROCESSED", drop_folder,
                                    "{} deleted".format(package.name)))
                outcome.package_state = "deleted"
            except OSError as error:
                events.append(Event("ERROR", drop_folder,
                                    "{} could not be deleted: {}"
                                    .format(package.name, error)))
                outcome.package_state = ("left in the drop folder - it could "
                                         "not be deleted")

    # --- git commit -------------------------------------------------------
    if all_affected and not dry_run:
        replaced_count = counts.get("REPLACED", 0)
        created_count = counts.get("CREATED", 0)
        moved_count = counts.get("MOVED", 0)
        parts = []
        if replaced_count:
            parts.append("{} replaced".format(replaced_count))
        if created_count:
            parts.append("{} created".format(created_count))
        if moved_count:
            parts.append("{} moved".format(moved_count))
        summary = ", ".join(parts) if parts else "applied"

        context.git_commit(
            "fup: applied {} ({})".format(package.stem, summary),
            all_affected)

    # --- the binder builder -----------------------------------------------
    do_trigger = settings.get("trigger_binder", True)
    if not do_trigger:
        outcome.binder = "not triggered - disabled in settings"
    elif not wrote_something:
        outcome.binder = "not triggered - no files were deployed"
    else:
        event, phrase = trigger_binder(context, dry_run)
        events.append(event)
        outcome.binder = phrase

    finish(events, outcome, documentation_root, drop_folder,
           dry_run, log_path)
