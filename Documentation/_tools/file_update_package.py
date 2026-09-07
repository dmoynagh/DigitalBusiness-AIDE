#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file update package - deploy a package of updated documents into the tree.

WHAT IT DOES
    Takes a FileUpdatePackage - a zip file produced by a Chat or Cowork
    session, carrying updated documentation files and a manifest describing
    them - and deploys those files into the master tree.

        find the newest package in the drop folder
        validate it: a zip, with a manifest, naming files it actually contains
        show the package's instructions to the user and wait, if it has any
        for each file: move the document it replaces into _superseded,
                       then write the new one
        run the binder builder
        move the package into _superseded
        report what happened, and hold the window open until it is read

WHAT IT DOES NOT DO
    It does not merge, patch or edit. A package carries whole files and this
    tool places them. It does not decide what should be in a package, and it
    does not resolve versions beyond moving the single file each manifest entry
    names - general supersession is version cleanup's job.

    It never overwrites. A file already sitting where a package wants to write,
    and not named as the one being replaced, is reported as a CONFLICT and left
    exactly where it is.

HOW IT IS RUN
    Live by default. Pass --dry-run to see the report without changing
    anything. It reads its settings from a JSON file sitting beside this
    script, so it can simply be double-clicked on Windows.

    The completion summary is the point of the run, not an afterthought: it is
    the user's confirmation that the deploy did what they expected, and the
    window stays open until they have read it.

DESIGN NOTE
    This is one tool that does one thing, and a sibling to version cleanup and
    the binder builder. The path logic, settings loader, plan/apply split and
    report shape below are deliberately the same as theirs, copied rather than
    imported: there is no shared module, no plugin system and no base class
    between them.

Python 3.8 or newer. Standard library only.
"""

import argparse
import datetime
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
# Path(__file__) is this script's own file. .resolve() turns it into a full,
# unambiguous path, and .parent gives the folder holding it. Everything the
# tool reads or writes hangs off this folder rather than off the "current
# working directory", because the working directory depends on *how* the script
# was launched (double-click, terminal, scheduler) and is therefore unreliable.
# It also means each copy of the tool uses its own settings and its own log.
SCRIPT_DIR = Path(__file__).resolve().parent

SETTINGS_FILENAME = "file_update_package_settings.json"
SUPERSEDED_FOLDER_NAME = "_superseded"

# The manifest sits at the root of the package and is the package's statement
# of what it contains. A zip without one is not a FileUpdatePackage.
MANIFEST_NAME = "_manifest.json"

PACKAGE_SUFFIX = ".zip"

# Spots "C:" or "D:" at the start of a path, so a Windows path in a settings
# file being run on Mac or Linux fails loudly rather than being mistaken for a
# relative pattern that then silently never matches anything. Also used on
# manifest paths, where a drive letter is never legitimate.
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

# How long the binder builder is given before the deploy stops waiting for it.
# The trigger is best-effort: a binder builder that hangs must not hang the
# report of a deploy that has already happened.
BINDER_TIMEOUT_SECONDS = 600

# Folder names this corpus has settled on. The check that uses them does not
# rename anything - it only says, in the completion summary, that a folder is
# one character away from a convention. The known offender is the misspelled
# "_superceded" at the documentation root, which is deliberately left alone: it
# is underscore-prefixed, so every tool skips it, and reconciling it is a human
# act rather than a tool's.
CONVENTION_FOLDER_NAMES = (
    "_superseded",
    "_fileupdatepackages",
    "_binder",
    "_tools",
    "_config",
    "_rebuild",
)

# difflib's similarity ratio, 0.0 to 1.0. At 0.85 a one-character misspelling of
# a convention name is caught and an unrelated folder is not. The check is
# advisory - it never changes what the tool does or what it exits with - but a
# summary that cries wolf stops being read, so it is paired with the underscore
# rule below rather than being loosened.
NAMING_SIMILARITY = 0.85

# The settings file is shipped with the tool, but if someone deletes it - or
# copies just the .py file to a new location - we write this back out rather
# than failing. Keeping the defaults as *text* (not as a Python dictionary that
# gets dumped to JSON) means the file we create is byte-for-byte the file we
# ship, comments and ordering included.
#
# JSON has no comment syntax, so the explanatory lines are carried as ordinary
# keys beginning with "_comment". The loader ignores them. That keeps the file
# valid JSON, readable by any editor and parseable by the standard library.
DEFAULT_SETTINGS_JSON = """{
  "_comment": "Settings for the file update package deployer. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_documentation_root": "The root of the document tree packages are deployed into. Manifest paths are measured from here. A relative path is resolved against the folder this script lives in, so \\"..\\" means the parent folder - which is what an instance sitting in _tools wants. Give a full path such as \\"C:/Users/you/Documents\\" to point somewhere else. Forward slashes are safe on Windows. This setting cannot use \\"~/\\", because \\"~/\\" means \\"measured from the documentation root\\" and this is the setting that defines it.",
  "documentation_root": "..",

  "_comment_paths": "The three settings below accept three kinds of path. ABSOLUTE - \\"C:/Docs/_fileupdatepackages\\". ROOT-ANCHORED - \\"~/_fileupdatepackages\\" - measured from the documentation root above. RELATIVE - \\"_fileupdatepackages\\" - measured from the folder this script lives in. Note that ~ means the documentation root here, never your home folder.",

  "_comment_drop_folder": "Where packages are put to be deployed. The newest unprocessed .zip in this folder is the one that gets processed; the rest wait. Processed packages are moved into a _superseded subfolder of it.",
  "drop_folder": "~/_fileupdatepackages",

  "_comment_binder_builder": "The binder builder script to run after a deploy. Point this at the running instance, not at the master copy, so it uses that instance's settings. Set it to \\"\\" to skip the trigger entirely.",
  "binder_builder": "~/_tools/binder_builder.py",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder.",
  "log_file": "file_update_package.log"
}
"""


# ---------------------------------------------------------------------------
# Small record types
# ---------------------------------------------------------------------------
# A dataclass is Python shorthand for "a class that just holds these fields".
# The lines below generate the constructor for us. Used here instead of loose
# tuples so that report code can say event.kind rather than event[0].

@dataclass
class Event:
    """One line of the report: something that happened, or failed to."""
    kind: str      # see REPORT_KINDS
    folder: Path   # the folder it concerns
    detail: str    # human-readable description


# The vocabulary, in the order a summary line lists it. The paired live and dry
# run words are the same shape the sibling tools use for MOVED/WOULD MOVE and
# INCLUDED/WOULD INCLUDE. CONFLICT and ERROR carry their meanings exactly.
REPORT_KINDS = (
    "DEPLOYED",        # an updated file written over its predecessor's place
    "WOULD DEPLOY",    # dry run equivalent
    "CREATED",         # a file that did not exist before
    "WOULD CREATE",
    "SUPERSEDED",      # the document a manifest entry replaces, moved aside
    "WOULD SUPERSEDE",
    "CONFLICT",        # a destination is taken, or a supersession is ambiguous
    "SKIPPED",         # nothing to do, or a package left waiting its turn
    "INVALID",         # not a package, or a manifest that cannot be trusted
    "BINDER",          # the binder builder was triggered, and what it said
    "PROCESSED",       # the package itself, moved into _superseded
    "WOULD PROCESS",
    "ERROR",           # filesystem refusal, or a failed binder builder run
)


@dataclass
class ManifestEntry:
    """One file a package asks to be deployed."""
    path: str          # as written in the manifest, forward slashes
    action: str        # "create" or "update"
    replaces: str      # filename of the document being superseded, or ""
    relative: Path     # the same path, validated and turned into a Path


@dataclass
class Manifest:
    """A package's statement of what it contains."""
    description: str = ""
    user_instructions: str = ""
    entries: list = field(default_factory=list)


@dataclass
class Outcome:
    """
    The facts the completion summary states that the event list cannot.

    Counts are derived from the events, so they are not held here. What is held
    is everything the summary must say about the run as a whole: which package,
    whether the user saw its instructions, what the binder builder did, and
    whether the package was filed away afterwards.
    """
    package: Path = None
    package_line: str = ""      # name, date and size, taken before it moves
    description: str = ""
    instructions: str = "none in this package"
    binder: str = "not triggered"
    package_state: str = "left in the drop folder"
    entry_count: int = 0        # files the manifest asked for
    naming: list = field(default_factory=list)   # (relative path, expected)


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

def load_settings(settings_path):
    """
    Read the settings file, creating it from the shipped defaults if missing.

    Returns a plain dictionary. Raises ValueError with a readable message if
    the file exists but is not valid JSON - a mistyped settings file should
    stop the run with an explanation, not with a stack trace.
    """
    if not settings_path.exists():
        print("No settings file found. Creating one with default values:")
        print("  {}".format(settings_path))
        print("Check the paths in it, then run the tool again.")
        print("")
        settings_path.write_text(DEFAULT_SETTINGS_JSON, encoding="utf-8")

    text = settings_path.read_text(encoding="utf-8")
    try:
        settings = json.loads(text)
    except json.JSONDecodeError as error:
        # The exception carries the line and column of the problem, which is
        # the single most useful thing to show someone fixing the file.
        raise ValueError(
            "The settings file is not valid JSON.\n"
            "  file: {}\n"
            "  problem: {} (line {}, column {})\n"
            "Common causes: a missing comma, a trailing comma after the last "
            "item, or a single backslash inside a path (write \\\\ or use /)."
            .format(settings_path, error.msg, error.lineno, error.colno)
        )

    if not isinstance(settings, dict):
        raise ValueError(
            "The settings file must contain a JSON object (a {{ ... }} block), "
            "but it contains {}.".format(type(settings).__name__)
        )

    return settings


# ---------------------------------------------------------------------------
# Path forms
# ---------------------------------------------------------------------------
# The same three spellings the sibling tools accept:
#
#   absolute        "C:/Docs/_fileupdatepackages"   one exact folder
#   root-anchored   "~/_fileupdatepackages"         measured from the root
#   relative        "_fileupdatepackages"           measured from the script
#
# This tool has no include or exclude lists, so there is nowhere for the
# folder-relative *pattern* form to apply: every setting here names one place,
# and the relative spelling is therefore resolved against the script folder,
# exactly as `root`, `output` and `log_file` are in the other two tools.
#
# Note that "~" does NOT mean the home folder here. Python's expanduser is
# deliberately never called on these settings, so "~/" always means the
# documentation root and can never quietly resolve to C:\\Users\\someone.

def tidy_setting_text(value, label):
    """Trim a settings value and normalise its separators to forward slashes."""
    text = str(value).strip().replace("\\", "/")
    if not text:
        raise ValueError('Setting "{}" contains an empty path.'.format(label))
    return text


def resolve_one_folder(text, label, root=None):
    """
    Resolve a settings value that names ONE place: absolute, "~/" measured from
    the documentation root, or relative to the script's own folder.
    """
    if text.startswith("~"):
        if root is None:
            raise ValueError(
                'Setting "{}" cannot use "~/", because "~/" means "measured '
                'from the documentation root" and this setting is what defines '
                'that root. Use a full path, or a path relative to the script '
                'folder - ".." is the folder above this script, which is what '
                'an instance sitting in a _tools folder wants.'.format(label)
            )
        if not text.startswith("~/"):
            raise ValueError(
                'Setting "{}": "~" means the documentation root, so it has to '
                'be written as "~/something".'.format(label)
            )
        return (root / text[2:]).resolve()

    path = Path(text)
    if not path.is_absolute():
        if WINDOWS_DRIVE.match(text):
            raise ValueError(
                'Setting "{}" is "{}", which looks like a Windows path, but '
                "this is not Windows.".format(label, text)
            )
        # resolve() also removes any ".." segments, so two spellings of the
        # same folder compare equal later on.
        path = SCRIPT_DIR / path
    return path.resolve()


def normalise(path):
    """
    Case-fold a path the way the local filesystem does.

    os.path.normcase lowercases on Windows, where FOO and foo are the same
    folder, and changes nothing on Mac or Linux. Comparing paths through it
    avoids both false misses on Windows and false matches elsewhere.
    """
    return Path(os.path.normcase(str(path)))


def is_inside(path, folder):
    """True if `path` is `folder` itself, or anywhere beneath it."""
    try:
        normalise(path).relative_to(normalise(folder))
        return True
    except ValueError:
        # relative_to raises when path is not under folder. Catching that is
        # the standard pathlib way of asking this question.
        return False


def relative_to(path, root):
    """Show a path relative to the root when possible - shorter to read."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


# ---------------------------------------------------------------------------
# Finding the package
# ---------------------------------------------------------------------------

def find_packages(drop_folder):
    """
    Every unprocessed package in the drop folder, newest first.

    Only the top level is looked at, which is what keeps processed packages -
    which live in the _superseded subfolder - from being found again. The sort
    is by modification time, with the name as a tie-breaker so that two files
    written in the same second still come out in a stable order.
    """
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
    """A short "when and how big" line for the report header."""
    try:
        stat = path.stat()
    except OSError:
        return path.name
    when = datetime.datetime.fromtimestamp(stat.st_mtime)
    return "{}  ({}, {:,} bytes)".format(
        path.name, when.strftime("%Y-%m-%d %H:%M"), stat.st_size)


# ---------------------------------------------------------------------------
# Reading and validating the manifest
# ---------------------------------------------------------------------------
# Validation is a gate, not a filter. A package either deploys as a whole or is
# rejected as a whole: a manifest naming a file the zip does not contain is a
# package built wrongly, and deploying the half of it that happens to be
# present would leave the tree in a state nobody designed.
#
# The one thing checked with real suspicion is the shape of each path. A zip is
# an untrusted input, and a member path containing ".." or a drive letter would
# write outside the documentation root - the "zip slip" mistake. Every path is
# therefore checked before it is used, and the resolved destination is checked
# again to be inside the root.

def safe_relative_path(text):
    """
    Turn a manifest path into a relative Path, or raise ValueError.

    Refused: an empty path, an absolute one, a drive letter, and any ".."
    segment. A manifest path is always measured from the documentation root and
    always points downwards.
    """
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
            "root".format(text)
        )
    if tidied.endswith("/"):
        raise ValueError('"{}" names a folder, not a file'.format(text))

    return Path(*segments)


def read_manifest(archive, names):
    """
    Read and check the manifest. Returns (manifest, problems).

    `problems` is a list of readable strings. If it is not empty the package is
    INVALID and nothing at all is deployed from it.
    """
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
            .format(MANIFEST_NAME, error.msg, error.lineno, error.colno)
        ]

    if not isinstance(data, dict):
        return None, [
            "{} must contain a JSON object, but it contains {}"
            .format(MANIFEST_NAME, type(data).__name__)
        ]

    manifest = Manifest(
        description=str(data.get("description", "")).strip(),
        user_instructions=str(data.get("user_instructions", "")).strip(),
    )

    listed = data.get("files")
    if not isinstance(listed, list) or not listed:
        return None, [
            '{} has no "files" list, or it is empty'.format(MANIFEST_NAME)
        ]

    seen = {}
    for position, item in enumerate(listed, start=1):
        where = "files entry {}".format(position)
        if not isinstance(item, dict):
            problems.append("{} is not an object".format(where))
            continue

        try:
            relative = safe_relative_path(item.get("path", ""))
        except ValueError as error:
            problems.append("{}: {}".format(where, error))
            continue

        path = str(item.get("path", "")).strip().replace("\\", "/")
        action = str(item.get("action", "")).strip().lower()
        if action not in ("create", "update"):
            problems.append(
                '{} ({}): action is "{}", but it must be "create" or "update"'
                .format(where, path, item.get("action", ""))
            )
            continue

        replaces = str(item.get("replaces", "") or "").strip()
        if replaces and action != "update":
            problems.append(
                '{} ({}): "replaces" is only meaningful on an update'
                .format(where, path)
            )
            continue
        if replaces and ("/" in replaces or "\\" in replaces):
            problems.append(
                '{} ({}): "replaces" is a filename, not a path - "{}" contains '
                "a folder separator".format(where, path, replaces)
            )
            continue

        # The archive must actually contain what the manifest promises.
        if path not in names:
            problems.append(
                "{}: the package does not contain \"{}\"".format(where, path))
            continue

        # Two entries writing the same destination is a package built wrongly:
        # whichever ran second would hit its own predecessor as a CONFLICT.
        key = os.path.normcase(str(relative))
        if key in seen:
            problems.append(
                '{} ({}): the same path is listed twice (entries {} and {})'
                .format(where, path, seen[key], position)
            )
            continue
        seen[key] = position

        manifest.entries.append(ManifestEntry(
            path=path, action=action, replaces=replaces, relative=relative,
        ))

    if not manifest.entries and not problems:
        problems.append('{} lists no usable files'.format(MANIFEST_NAME))

    return manifest, problems


# ---------------------------------------------------------------------------
# The user instructions gate
# ---------------------------------------------------------------------------

def acknowledge_instructions(instructions, dry_run):
    """
    Show the package's instructions and wait for the user to acknowledge them.

    Deliberately placed BEFORE any file is written, so that stopping here -
    with Ctrl+C - stops a deploy that has not started rather than one that is
    half done.

    Returns a phrase for the completion summary. The wait is skipped when there
    is no interactive console, for the same reason the exit pause is: a run
    triggered by another tool must not block forever on a keypress nobody is
    there to press.
    """
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
    """
    Find the document a manifest entry supersedes. Returns a list of matches.

    Looked for beside the new file first, which is where a superseded version
    almost always is - v7 and v8 of one document live in the same folder. Only
    if it is not there is the rest of the tree searched, and _superseded
    folders are skipped throughout: a file already filed away is not a
    candidate for being filed away again.

    A list is returned rather than one path because "found in three places" is
    a real answer, and one this tool must not resolve by guessing.
    """
    wanted = os.path.normcase(replaces)

    beside = target.parent / replaces
    if beside.is_file():
        return [beside]

    found = []
    for dirpath, dirnames, filenames in os.walk(documentation_root):
        # dirnames[:] = ... replaces the contents of the existing list rather
        # than rebinding the name. os.walk only notices the former.
        dirnames[:] = sorted(
            name for name in dirnames
            if os.path.normcase(name) != SUPERSEDED_FOLDER_NAME
        )
        for filename in filenames:
            if os.path.normcase(filename) == wanted:
                found.append(Path(dirpath) / filename)
    return found


def supersede(path, dry_run):
    """
    Move one document into _superseded beside it. Returns an Event.

    Nothing is ever overwritten: a taken destination is a CONFLICT and the file
    stays where it is. This is the same shape, and the same guarantee, as the
    binder builder's supersession of its own previous output.
    """
    folder = path.parent
    destination = folder / SUPERSEDED_FOLDER_NAME / path.name

    if dry_run:
        return Event("WOULD SUPERSEDE", folder,
                     "{} -> {}/".format(path.name, SUPERSEDED_FOLDER_NAME))

    if destination.exists():
        return Event(
            "CONFLICT", folder,
            "{} left in place: {}/{} already exists"
            .format(path.name, SUPERSEDED_FOLDER_NAME, path.name)
        )

    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        # A last existence check immediately before the move: the destination
        # could have appeared since, and shutil.move would silently overwrite
        # it on Linux and macOS.
        if destination.exists():
            return Event(
                "CONFLICT", folder,
                "{} left in place: {}/{} appeared during the run"
                .format(path.name, SUPERSEDED_FOLDER_NAME, path.name)
            )
        shutil.move(str(path), str(destination))
        return Event("SUPERSEDED", folder,
                     "{} -> {}/".format(path.name, SUPERSEDED_FOLDER_NAME))
    except OSError as error:
        return Event("ERROR", folder,
                     "{} could not be superseded: {}".format(path.name, error))


def write_member(archive, member, target):
    """
    Write one file out of the package.

    Binary mode throughout: the bytes in the package are the bytes on disk,
    with no encoding assumption and no line-ending translation. zipfile's own
    extract() is deliberately not used, because it derives the destination from
    the member name - and the destination here has already been validated.
    """
    data = archive.read(member)
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(data)
    return len(data)


def deploy_entry(archive, entry, documentation_root, dry_run):
    """
    Deploy one manifest entry. Returns a list of Events, in the order they
    happened: the supersession first, then the write.

    The two questions are asked in this order deliberately. An update whose
    predecessor sits at the same path can only be written after that
    predecessor has been moved aside, and the never-overwrite check that
    follows is then a genuine test rather than a formality.
    """
    events = []
    target = (documentation_root / entry.relative).resolve()
    folder = target.parent

    # Belt and braces after safe_relative_path: the resolved destination must
    # still be inside the documentation root. A symbolic link in the tree could
    # otherwise carry a well-formed relative path somewhere else entirely.
    if not is_inside(target, documentation_root):
        return [Event(
            "CONFLICT", documentation_root,
            "{}: resolves outside the documentation root and was not deployed"
            .format(entry.path)
        )]

    # Does anything stand between this entry and its destination? Normally the
    # answer is simply "is something already there", but an update whose
    # predecessor sits at the destination itself clears its own way.
    occupied = target.exists()

    if entry.action == "update":
        # No "replaces" named means the entry updates the file at its own path,
        # which is the file that then has to be moved aside.
        wanted = entry.replaces or target.name
        matches = find_replaced_file(documentation_root, target, wanted)

        if len(matches) == 1:
            previous = matches[0]
            event = supersede(previous, dry_run)
            events.append(event)
            cleared = event.kind in ("SUPERSEDED", "WOULD SUPERSEDE")

            if normalise(previous) == normalise(target):
                # The document being replaced IS the destination. In a live run
                # it has just been moved; in a dry run it has not, but it would
                # have been, and reporting a conflict against a file the run
                # itself would have moved would make the dry run a liar.
                if not cleared:
                    events.append(Event(
                        "CONFLICT", folder,
                        "{}: not deployed - {} could not be moved out of the "
                        "way".format(entry.path, previous.name)
                    ))
                    return events
                occupied = False
        elif not matches:
            events.append(Event(
                "SKIPPED", folder,
                "{}: nothing superseded - \"{}\" is not in the documentation "
                "tree".format(entry.path, wanted)
            ))
        else:
            events.append(Event(
                "CONFLICT", folder,
                "{}: \"{}\" was found in {} places and none were moved ({})"
                .format(entry.path, wanted, len(matches),
                        ", ".join(relative_to(match, documentation_root)
                                  for match in matches))
            ))

    # Never overwrite. By this point an update's predecessor has been moved out
    # of the way, so anything still sitting at the destination is a file this
    # package did not account for.
    if occupied:
        events.append(Event(
            "CONFLICT", folder,
            "{}: not deployed - a file already exists there and the package "
            "did not name it as superseded".format(entry.path)
        ))
        return events

    # The live word and its dry-run twin, kept as a pair rather than derived
    # from one another: "WOULD " + "DEPLOYED" would read "WOULD DEPLOYED".
    kind, would = (("CREATED", "WOULD CREATE") if entry.action == "create"
                   else ("DEPLOYED", "WOULD DEPLOY"))
    if dry_run:
        events.append(Event(
            would, folder,
            "{}  ({:,} bytes)".format(entry.path,
                                      archive.getinfo(entry.path).file_size)
        ))
        return events

    try:
        written = write_member(archive, entry.path, target)
        events.append(Event(kind, folder,
                            "{}  ({:,} bytes)".format(entry.path, written)))
    except (OSError, zipfile.BadZipFile, KeyError) as error:
        events.append(Event("ERROR", folder,
                            "{} could not be written: {}"
                            .format(entry.path, error)))
    return events


# ---------------------------------------------------------------------------
# The binder builder trigger
# ---------------------------------------------------------------------------

def trigger_binder_builder(script_path, dry_run):
    """
    Run the binder builder. Returns (Event, summary phrase).

    Best-effort by design: the deploy has already happened by the time this
    runs, and a binder that could not be rebuilt does not undo it. A failure
    here is reported as an ERROR against the binder step and the deploy still
    stands.

    The binder builder decides for itself whether a rebuild is needed - it
    compares the tree against the manifest of the current binder - so this is
    an unconditional call, made after every deploy.

    stdin is closed rather than inherited, which is what stops the binder
    builder pausing for a keypress at the end of its own run: it skips that
    pause when it has no interactive console.
    """
    folder = script_path.parent

    if dry_run:
        return (Event("BINDER", folder,
                      "would run {}".format(script_path.name)),
                "would be triggered (dry run)")

    if not script_path.is_file():
        return (Event("ERROR", folder,
                      "binder builder not run: {} does not exist"
                      .format(script_path)),
                "NOT triggered - {} does not exist".format(script_path))

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(folder),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=BINDER_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return (Event("ERROR", folder,
                      "binder builder did not finish within {} seconds"
                      .format(BINDER_TIMEOUT_SECONDS)),
                "FAILED - did not finish within {} seconds"
                .format(BINDER_TIMEOUT_SECONDS))
    except OSError as error:
        return (Event("ERROR", folder,
                      "binder builder could not be started: {}".format(error)),
                "FAILED - could not be started: {}".format(error))

    output = result.stdout.decode("utf-8", errors="replace")
    # The binder builder's own summary line is the one thing worth carrying up
    # into this report. Its full report is in its own log, which the line that
    # follows points at.
    outcome = ""
    for line in output.splitlines():
        if line.startswith("Result:"):
            outcome = line[len("Result:"):].strip()
    if not outcome:
        outcome = "no result line in its output"

    if result.returncode != 0:
        return (Event("ERROR", folder,
                      "binder builder exited {}: {}"
                      .format(result.returncode, outcome)),
                "ran and FAILED (exit {}) - {}"
                .format(result.returncode, outcome))

    return (Event("BINDER", folder, "binder builder run: {}".format(outcome)),
            "triggered - {}".format(outcome))


# ---------------------------------------------------------------------------
# Folder naming check
# ---------------------------------------------------------------------------
# Advisory only. It reports, it never renames, and it never changes the exit
# code. A misspelled underscore folder is skipped by every tool in this family
# for the same reason a correctly spelled one is, so it does no damage - but it
# silently splits a convention in two, and the only way that gets noticed is if
# something says so.

def check_folder_naming(documentation_root):
    """
    Find folders whose names are near-misses of a convention name.

    Returns a list of (path relative to the root, the name it probably meant).

    Only folders whose names begin with an underscore are considered, which is
    the class every convention name belongs to.
    """
    findings = []
    for dirpath, dirnames, _filenames in os.walk(documentation_root):
        for name in sorted(dirnames):
            lowered = name.lower()
            # Only underscore folders are candidates. Every convention name is
            # one, and the restriction is what keeps an ordinary folder out of
            # the summary: "file-update-package", the master folder of this very
            # tool, scores 0.86 against "_fileupdatepackages" on similarity
            # alone and is obviously not a misspelling of it.
            if not lowered.startswith("_"):
                continue
            if lowered in CONVENTION_FOLDER_NAMES:
                continue
            close = difflib.get_close_matches(
                lowered, CONVENTION_FOLDER_NAMES, n=1,
                cutoff=NAMING_SIMILARITY)
            if close:
                folder = Path(dirpath) / name
                findings.append(
                    (relative_to(folder, documentation_root), close[0]))
    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def count_kinds(events):
    """How many of each kind of event, for the summary line and the totals."""
    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1
    return counts


def build_completion_summary(events, outcome, dry_run):
    """
    The block that holds the window open, as a list of lines.

    This is the primary output of the tool. Someone who reads nothing else
    should be able to tell from these lines whether the deploy did what they
    expected, and if it did not, which file was involved and why.
    """
    counts = count_kinds(events)
    deployed = counts.get("DEPLOYED", 0) + counts.get("WOULD DEPLOY", 0)
    created = counts.get("CREATED", 0) + counts.get("WOULD CREATE", 0)
    superseded = counts.get("SUPERSEDED", 0) + counts.get("WOULD SUPERSEDE", 0)
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

    lines.append(row("files updated:", deployed))
    lines.append(row("files created:", created))
    lines.append(row("files superseded:", superseded))

    lines.append(row("conflicts:", len(conflicts)))
    for event in conflicts:
        lines.append("    - {}".format(event.detail))

    lines.append(row("errors:", len(errors)))
    for event in errors:
        lines.append("    - {}".format(event.detail))

    # A rejected package is not an error in the tool - nothing was attempted
    # and nothing failed - so it is counted separately from one, and the row
    # only appears when there is something to say.
    if invalid:
        lines.append(row("package rejected:",
                         "nothing in it was deployed"))
        for event in invalid:
            lines.append("    - {}".format(event.detail))

    lines.append(row("user instructions:", outcome.instructions))
    lines.append(row("binder builder:", outcome.binder))
    lines.append(row("the package is now:", outcome.package_state))

    # The naming check speaks here and nowhere else. It is advisory: it names
    # what it found and leaves the decision to a person.
    if outcome.naming:
        lines.append(row("folder naming:",
                         "{} folder(s) close to a convention name but not "
                         "matching it".format(len(outcome.naming))))
        for found, expected in outcome.naming:
            lines.append("    - {}  (expected \"{}\")".format(found, expected))
    else:
        lines.append(row("folder naming:", "no misspelled folders found"))

    lines.append("-" * 72)

    # The final status line. Note that conflicts count as errors here: the
    # deploy did not do everything the package asked for, and saying otherwise
    # on the one line most likely to be read alone would be a lie of omission.
    # Did every file the manifest asked for actually land?
    complete = (outcome.entry_count > 0
                and deployed + created == outcome.entry_count
                and not conflicts)

    if errors or conflicts or invalid:
        if deployed + created == 0:
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


def build_report(settings_path, documentation_root, drop_folder, dry_run,
                 events, outcome):
    """
    Build the run report as a list of lines.

    One function produces both the on-screen report and the log entry, so the
    two can never drift apart.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing changed)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("file update package   {}   {}".format(timestamp, mode))
    lines.append("documentation root: {}".format(documentation_root))
    lines.append("settings:           {}".format(settings_path))
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
        # Events are reported in the order they happened rather than sorted:
        # a deploy is a sequence, and a supersession followed by the write that
        # depended on it reads as one story. The folder heading still changes
        # as the run moves through the tree.
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
    """
    Append one entry to the log. The log is never rewritten or trimmed.

    Failing to write the log must not lose the report that is already on
    screen, so a problem here is reported and swallowed.
    """
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        # "a" is append mode: the file is created if absent, and writes always
        # go to the end. newline="\n" leaves line endings to us, so the log
        # looks the same on every platform.
        with open(log_path, "a", encoding="utf-8", newline="\n") as log_file:
            log_file.write("\n".join(lines))
            log_file.write("\n\n")
        return True
    except OSError as error:
        print("WARNING: could not write the log file {}: {}"
              .format(log_path, error))
        return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def pause_before_exit():
    """
    Hold the console open so a double-clicked run can be read.

    Skipped when there is no interactive console attached - otherwise a
    scheduled or piped run would hang forever waiting for a keypress.
    """
    if not sys.stdin or not sys.stdin.isatty():
        return
    try:
        input("\nPress Enter to close...")
    except (EOFError, KeyboardInterrupt):
        pass


def run(dry_run):
    """The whole job. Returns an exit code: 0 for success, 1 for a problem."""
    settings_path = SCRIPT_DIR / SETTINGS_FILENAME

    try:
        settings = load_settings(settings_path)

        # The documentation root is resolved first, because "~/" in the other
        # settings is measured from it.
        documentation_root = resolve_one_folder(
            tidy_setting_text(settings.get("documentation_root", ".."),
                              "documentation_root"),
            "documentation_root",
        )
        drop_folder = resolve_one_folder(
            tidy_setting_text(settings.get("drop_folder",
                                           "~/_fileupdatepackages"),
                              "drop_folder"),
            "drop_folder", root=documentation_root,
        )
        binder_setting = str(settings.get("binder_builder",
                                          "~/_tools/binder_builder.py")).strip()
        binder_path = None
        if binder_setting:
            binder_path = resolve_one_folder(
                tidy_setting_text(binder_setting, "binder_builder"),
                "binder_builder", root=documentation_root,
            )
        log_path = resolve_one_folder(
            tidy_setting_text(settings.get("log_file",
                                           "file_update_package.log"),
                              "log_file"),
            "log_file", root=documentation_root,
        )
    except ValueError as error:
        print("SETTINGS PROBLEM")
        print(error)
        return 1

    if not documentation_root.is_dir():
        print("SETTINGS PROBLEM")
        print('The "documentation_root" setting does not point at a folder '
              "that exists:")
        print("  {}".format(documentation_root))
        print("  (from settings file {})".format(settings_path))
        return 1

    events = []
    outcome = Outcome()
    # The naming check runs on every run, package or no package. It is the one
    # thing here that reports on the tree rather than on the deploy, and a run
    # that found nothing to deploy is as good a moment to mention it as any.
    outcome.naming = check_folder_naming(documentation_root)

    packages = find_packages(drop_folder)

    if not packages:
        events.append(Event(
            "SKIPPED", drop_folder,
            "no packages found in {}".format(
                drop_folder if drop_folder.is_dir()
                else "{} (the folder does not exist)".format(drop_folder))
        ))
        return finish(events, outcome, settings_path, documentation_root,
                      drop_folder, dry_run, log_path)

    package = packages[0]
    outcome.package = package
    # Described now, while it is still where it was found: by the time the
    # report is built the package may have been moved into _superseded.
    outcome.package_line = describe_package(package)
    # Only the newest is processed. Batching packages would mean deciding what
    # to do when the third of five conflicts, and the answer to that is a
    # person looking at the report - so the rest simply wait their turn.
    for waiting in packages[1:]:
        events.append(Event(
            "SKIPPED", drop_folder,
            "{}: waiting - only the newest package is processed in a run"
            .format(waiting.name)
        ))

    # --- validate ---------------------------------------------------------
    if not zipfile.is_zipfile(package):
        events.append(Event("INVALID", drop_folder,
                            "{} is not a zip file".format(package.name)))
        return finish(events, outcome, settings_path, documentation_root,
                      drop_folder, dry_run, log_path)

    try:
        archive = zipfile.ZipFile(package)
    except (zipfile.BadZipFile, OSError) as error:
        events.append(Event("INVALID", drop_folder,
                            "{} could not be opened: {}"
                            .format(package.name, error)))
        return finish(events, outcome, settings_path, documentation_root,
                      drop_folder, dry_run, log_path)

    with archive:
        names = set(archive.namelist())
        manifest, problems = read_manifest(archive, names)

        if problems:
            # Validation is a gate: a package that is wrong in one place is not
            # deployed in the places it happens to be right.
            for problem in problems:
                events.append(Event(
                    "INVALID", drop_folder,
                    "{}: {}".format(package.name, problem)))
            return finish(events, outcome, settings_path, documentation_root,
                          drop_folder, dry_run, log_path)

        outcome.description = manifest.description
        outcome.entry_count = len(manifest.entries)

        # --- the gate -----------------------------------------------------
        if manifest.user_instructions:
            outcome.instructions = acknowledge_instructions(
                manifest.user_instructions, dry_run)

        # --- deploy -------------------------------------------------------
        for entry in manifest.entries:
            events.extend(deploy_entry(archive, entry, documentation_root,
                                       dry_run))

    counts = count_kinds(events)
    wrote_something = any(counts.get(kind) for kind in
                          ("DEPLOYED", "WOULD DEPLOY",
                           "CREATED", "WOULD CREATE"))
    incomplete = bool(counts.get("CONFLICT") or counts.get("ERROR"))

    # --- the binder builder ----------------------------------------------
    if binder_path is None:
        outcome.binder = "not triggered - no binder_builder set in settings"
    elif not wrote_something:
        outcome.binder = "not triggered - no files were deployed"
    else:
        event, phrase = trigger_binder_builder(binder_path, dry_run)
        events.append(event)
        outcome.binder = phrase

    # --- file the package away -------------------------------------------
    # A partial deploy leaves the package in the drop folder. Whoever sorts the
    # conflict out needs the package still to hand, and a package filed under
    # _superseded reads as one that was fully applied.
    if incomplete:
        outcome.package_state = ("left in the drop folder - the deploy was "
                                 "not complete")
    elif not wrote_something:
        outcome.package_state = "left in the drop folder - nothing was deployed"
    else:
        event = supersede(package, dry_run)
        if event.kind in ("SUPERSEDED", "WOULD SUPERSEDE"):
            event = Event(
                "WOULD PROCESS" if dry_run else "PROCESSED", drop_folder,
                "{} -> {}/".format(package.name, SUPERSEDED_FOLDER_NAME))
            outcome.package_state = "{}moved to {}/".format(
                "would be " if dry_run else "", SUPERSEDED_FOLDER_NAME)
        else:
            outcome.package_state = ("left in the drop folder - it could not "
                                     "be moved")
        events.append(event)

    return finish(events, outcome, settings_path, documentation_root,
                  drop_folder, dry_run, log_path)


def finish(events, outcome, settings_path, documentation_root, drop_folder,
           dry_run, log_path):
    """
    Report, log, and return the exit code.

    Every path out of run() comes through here, so a run that stopped at
    validation produces the same shaped report - and the same completion
    summary - as one that deployed twenty files.
    """
    lines = build_report(settings_path, documentation_root, drop_folder,
                         dry_run, events, outcome)
    print("\n".join(lines))

    # Dry runs are logged too, clearly marked, so the log is a complete record
    # of every time the tool was pointed at the tree.
    append_to_log(log_path, lines)
    print("\nLog: {}".format(log_path))

    # Exit code follows the sibling tools: 0 unless something refused. Note the
    # consequence, which is stated in the design document: a CONFLICT and an
    # INVALID package both exit 0, because nothing failed - the tool did
    # exactly what it should with what it was given. The completion summary is
    # where a person reads that, and it says FAILED in plain words.
    return 1 if any(event.kind == "ERROR" for event in events) else 0


def main():
    parser = argparse.ArgumentParser(
        description="Deploy a FileUpdatePackage into the documentation tree. "
                    "Reads its settings from {} beside the script."
                    .format(SETTINGS_FILENAME)
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",  # present = True, absent = False
        help="report what would be deployed without changing anything",
    )
    args = parser.parse_args()

    try:
        exit_code = run(args.dry_run)
    except KeyboardInterrupt:
        print("\nInterrupted.")
        exit_code = 1

    pause_before_exit()
    return exit_code


# When Python runs a file directly, it sets __name__ to "__main__". This guard
# is the conventional way to say "only do this when run, not when imported".
if __name__ == "__main__":
    sys.exit(main())
