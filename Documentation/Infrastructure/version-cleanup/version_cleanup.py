#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
version cleanup - move superseded document versions out of the live tree.

WHAT IT DOES
    Walks a folder tree. In each folder it looks for files whose names are
    identical apart from a "_v<number>" suffix just before the extension.
    The highest number stays where it is; every lower version is moved into a
    "_superseded" subfolder of the folder it came from.

        Foo_v8.md + Foo_v9.md   ->  Foo_v8.md moves, Foo_v9.md stays
        Foo.md    + Foo_v1.md   ->  Foo.md moves (no suffix counts as v0)
        Foo_v3.md alone         ->  nothing happens

    Grouping is always within a single folder. The walk is recursive, but
    Foo_v8.md in one folder is never compared with Foo_v9.md in another.

HOW IT IS RUN
    Live by default. Pass --dry-run to see the report without changing
    anything. It reads its settings from a JSON file sitting beside this
    script, so it can simply be double-clicked on Windows.

DESIGN NOTE
    This is one tool that does one thing. Sibling tools (binder assembly is
    next) will be separate scripts run in sequence, so there is deliberately no
    plugin system, no action registry and no shared base class here.

Python 3.8 or newer. Standard library only.
"""

import argparse
import datetime
import json
import os
import re
import shutil
import sys
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

SETTINGS_FILENAME = "version_cleanup_settings.json"
SUPERSEDED_FOLDER_NAME = "_superseded"

# The matching rule, as a regular expression, applied to a filename with its
# extension already stripped off:
#   ^          start of the name
#   (?P<base>.+)   one or more characters, captured as "base" - the document
#                  identity. ".+" rather than ".*" so a file literally named
#                  "_v1.md" is not read as an empty document name.
#   _[vV]      the literal separator; upper or lower case v is accepted
#   (?P<number>\d+)  one or more digits, captured as "number"
#   $          end of the name - the suffix must be the last thing before the
#              extension, so "Foo_v2_draft.md" is deliberately not a match.
VERSION_SUFFIX = re.compile(r"^(?P<base>.+)_[vV](?P<number>\d+)$")

# Spots "C:" or "D:" at the start of a settings path, so a Windows path in a
# settings file being run on Mac or Linux fails loudly rather than being
# mistaken for a relative pattern that then silently never matches anything.
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

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
  "_comment": "Settings for the version cleanup tool. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_root": "The folder to tidy, including everything beneath it. A relative path is resolved against the folder this script lives in, so \\"..\\" means the parent folder. Give a full path such as \\"C:/Users/you/Documents\\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \\"C:/Docs/_binder\\" - names one exact folder. ROOT-ANCHORED - \\"~/_binder\\" - names one exact folder, measured from the root above. RELATIVE - \\"_binder\\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_include": "Folders whose names start with an underscore are skipped by default. List any that should be processed anyway. Example: [\\"_binder\\"] processes every _binder folder in the tree; [\\"~/_binder\\"] processes only the one at the top.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \\"_superseded\\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder.",
  "log_file": "version_cleanup.log"
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
    kind: str      # MOVED / WOULD MOVE / CONFLICT / AMBIGUOUS / ERROR
    folder: Path   # the folder it happened in
    detail: str    # human-readable description


@dataclass
class PlannedMove:
    """One file that should move, and where it should move to."""
    source: Path
    destination: Path
    reason: str    # e.g. "v7 superseded by v9"


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
        print("Review it, then run the tool again if the defaults are wrong.")
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
# Three spellings are accepted, because the tree needs two different kinds of
# statement: "this exact folder" and "any folder shaped like this".
#
#   absolute        "C:/Docs/_binder"   one exact folder
#   root-anchored   "~/_binder"         one exact folder, measured from root
#   relative        "_binder"           a PATTERN: every folder whose path
#                                       ends with those segments
#
# The relative form is the interesting one. It is not resolved once at startup;
# it is a shape the walk tests every folder against, so a single "_binder"
# entry covers a _binder subfolder wherever one turns up in the tree. Several
# segments work too: "_binder/current" matches any .../_binder/current.
#
# Note that "~" does NOT mean the home folder here. Python's expanduser is
# deliberately never called on these settings, so "~/" always means the root of
# the tree being tidied and can never quietly resolve to C:\Users\someone.

def tidy_setting_text(value, label):
    """Trim a settings value and normalise its separators to forward slashes."""
    text = str(value).strip().replace("\\", "/")
    if not text:
        raise ValueError('Setting "{}" contains an empty path.'.format(label))
    return text


def resolve_one_folder(text, label, root=None):
    """
    Resolve a settings value that names ONE place: absolute, "~/" measured from
    the root, or relative to the script's own folder.

    Used for the root and the log file. Include and exclude go through
    parse_scope_entry instead, because they also accept patterns.
    """
    if text.startswith("~"):
        if root is None:
            raise ValueError(
                'Setting "{}" cannot use "~/", because "~/" means "measured '
                'from the root" and this setting is what defines the root. '
                'Use a full path, or a path relative to the script folder.'
                .format(label)
            )
        if not text.startswith("~/"):
            raise ValueError(
                'Setting "{}": "~" means the root folder, so it has to be '
                'written as "~/something".'.format(label)
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


def parse_scope_entry(text, label, root):
    """
    Classify one include or exclude entry.

    Returns ("folder", Path) for the absolute and "~/" forms, or
    ("pattern", (segments...)) for the relative form.
    """
    if text.startswith("~"):
        return ("folder", resolve_one_folder(text, label, root))

    path = Path(text)
    if path.is_absolute():
        return ("folder", path.resolve())
    if WINDOWS_DRIVE.match(text):
        raise ValueError(
            'Setting "{}" contains "{}", which looks like a Windows path, but '
            "this is not Windows.".format(label, text)
        )

    # Anything else is a pattern. Splitting on "/" and dropping empty pieces
    # tolerates a stray leading or trailing slash.
    segments = tuple(part for part in text.split("/") if part)
    if not segments or "." in segments:
        raise ValueError(
            'Setting "{}" contains "{}", which does not name anything.'
            .format(label, text)
        )
    if ".." in segments:
        raise ValueError(
            'Setting "{}" contains "{}". A relative entry is a pattern tested '
            'against every folder in the tree, so ".." has no meaning in one. '
            'Write "~/..." to anchor at the root, or give a full path.'
            .format(label, text)
        )
    return ("pattern", segments)


def normalise(path):
    """
    Case-fold a path the way the local filesystem does.

    os.path.normcase lowercases on Windows, where FOO and foo are the same
    folder, and changes nothing on Mac or Linux. Comparing paths through it
    avoids both false misses on Windows and false matches elsewhere.
    """
    return Path(os.path.normcase(str(path)))


# ---------------------------------------------------------------------------
# Folder scope
# ---------------------------------------------------------------------------

def is_inside(path, folder):
    """True if `path` is `folder` itself, or anywhere beneath it."""
    try:
        normalise(path).relative_to(normalise(folder))
        return True
    except ValueError:
        # relative_to raises when path is not under folder. Catching that is
        # the standard pathlib way of asking this question.
        return False


@dataclass
class Scope:
    """
    Everything the walk needs in order to decide which folders are in play.

    Entries arrive already sorted into exact folders and patterns, so the walk
    itself stays readable: it asks questions, it does not parse settings.
    """
    root: Path
    include_folders: list = field(default_factory=list)
    include_patterns: list = field(default_factory=list)
    exclude_folders: list = field(default_factory=list)
    exclude_patterns: list = field(default_factory=list)
    include_text: list = field(default_factory=list)   # as typed, for the report
    exclude_text: list = field(default_factory=list)

    def parts_below_root(self, path):
        """The folder's path as case-folded segments measured from the root."""
        try:
            relative = path.relative_to(self.root)
        except ValueError:
            return None
        return tuple(os.path.normcase(part) for part in relative.parts)

    def matches_pattern(self, path, patterns):
        """
        True if the folder's path ENDS WITH one of the patterns.

        This trailing-segment test is what makes "_binder" mean "any _binder
        folder, wherever it appears". Because the comparison is made against
        the path measured from the root, a pattern can never reach above the
        root, and the root itself is never matched: it has no segments to
        compare.
        """
        parts = self.parts_below_root(path)
        if parts is None:
            return False
        for pattern in patterns:
            length = len(pattern)
            if length > len(parts):
                continue
            wanted = tuple(os.path.normcase(part) for part in pattern)
            if parts[-length:] == wanted:
                return True
        return False

    def leads_to_include_pattern(self, path):
        """
        True if something deeper down could still match a multi-segment
        include pattern.

        For "_binder/current", a folder ending in "_binder" is not itself
        included, but the walk has to pass through it to reach "current".
        Testing every *proper* prefix of every pattern is exactly that
        lookahead. Single-segment patterns have no proper prefix and contribute
        nothing here, which is right: they match the folder itself or not at
        all.
        """
        parts = self.parts_below_root(path)
        if parts is None:
            return False
        for pattern in self.include_patterns:
            for length in range(1, len(pattern)):
                if length > len(parts):
                    continue
                wanted = tuple(os.path.normcase(part)
                               for part in pattern[:length])
                if parts[-length:] == wanted:
                    return True
        return False

    def is_excluded(self, path):
        """Excluded folders, and everything inside them, are never touched."""
        if any(is_inside(path, folder) for folder in self.exclude_folders):
            return True
        return self.matches_pattern(path, self.exclude_patterns)

    def is_included(self, path):
        """True if this exact folder was named, or it matches a pattern."""
        if any(normalise(path) == normalise(folder)
               for folder in self.include_folders):
            return True
        return self.matches_pattern(path, self.include_patterns)

    def should_descend(self, path):
        """
        Should the walk go *into* this folder?

        Note the difference between descending and processing. An underscore
        folder that is not itself included may still need to be walked through,
        because something deeper down is on the include list. It is traversed,
        but its own files are left alone.
        """
        if self.is_excluded(path):
            return False
        if not path.name.startswith("_"):
            return True
        if self.is_included(path):
            return True
        # Is this folder on the way to an exactly-named include?
        if any(is_inside(folder, path) for folder in self.include_folders):
            return True
        return self.leads_to_include_pattern(path)

    def should_process(self, path):
        """Should this folder's own files be compared and tidied?"""
        if self.is_excluded(path):
            return False
        if not path.name.startswith("_"):
            return True
        # The underscore rule is what keeps the tool out of the _superseded
        # folders it creates. Only an explicit include overrides it.
        return self.is_included(path)


def build_scope(root, include_values, exclude_values):
    """Turn the raw include and exclude settings into a Scope."""
    scope = Scope(root=root)

    for label, values in (("include", include_values),
                          ("exclude", exclude_values)):
        if values is None:
            continue
        if not isinstance(values, list):
            raise ValueError(
                'Setting "{}" must be a list of paths, written in square '
                'brackets, for example ["_binder"].'.format(label)
            )
        for value in values:
            text = tidy_setting_text(value, label)
            kind, resolved = parse_scope_entry(text, label, root)
            if label == "include":
                scope.include_text.append(text)
                target = (scope.include_folders if kind == "folder"
                          else scope.include_patterns)
            else:
                scope.exclude_text.append(text)
                target = (scope.exclude_folders if kind == "folder"
                          else scope.exclude_patterns)
            target.append(resolved)

    return scope


def folders_to_process(scope):
    """
    Walk the tree from the root and return the folders whose files should be
    compared, in a stable, predictable order.
    """
    found = []
    root = scope.root

    # os.walk visits every folder beneath root. With topdown=True (the default)
    # it hands us the list of subfolder names *before* descending, and editing
    # that list in place prunes the walk - the standard way to skip whole
    # branches cheaply. Pruning is also what makes exclusion inherited: once a
    # folder is skipped, nothing inside it is ever looked at, so there is no
    # need to ask again further down. Symbolic links to folders are not
    # followed by default, which is what we want: a link should not cause the
    # same tree to be tidied twice.
    for dirpath, dirnames, _filenames in os.walk(root):
        current = Path(dirpath)

        # dirnames[:] = ... replaces the contents of the existing list rather
        # than rebinding the name. os.walk only notices the former.
        dirnames[:] = sorted(
            name for name in dirnames if scope.should_descend(current / name)
        )

        if current == root:
            # The root was chosen deliberately by whoever edited the settings,
            # so the underscore rule does not apply to it. An explicit exclude
            # still does.
            process = not scope.is_excluded(current)
        else:
            process = scope.should_process(current)

        if process:
            found.append(current)

    return found


# ---------------------------------------------------------------------------
# The matching rule
# ---------------------------------------------------------------------------

def split_version(file_path):
    """
    Split a filename into (document identity, extension, version number).

    Path.stem is the filename without its final extension; Path.suffix is that
    extension including the dot. A file with no _v suffix is version 0, which
    is what makes "Foo.md is superseded by Foo_v1.md" fall out of the same
    comparison as everything else rather than needing a special case.
    """
    stem = file_path.stem
    extension = file_path.suffix

    match = VERSION_SUFFIX.match(stem)
    if match:
        return match.group("base"), extension, int(match.group("number"))
    return stem, extension, 0


def plan_folder(folder):
    """
    Work out what should move in one folder. Nothing is changed here.

    Returns (moves, events). Splitting the decision from the action is what
    makes --dry-run trustworthy: the dry run and the live run take exactly the
    same decisions, and only the second half of the program differs.
    """
    moves = []
    events = []

    # Group the folder's files by (identity, extension). A dictionary of lists:
    # the key identifies the document, the list holds its versions.
    groups = {}
    try:
        entries = sorted(folder.iterdir())
    except OSError as error:
        events.append(Event("ERROR", folder, "cannot read folder: {}".format(error)))
        return moves, events

    for entry in entries:
        if not entry.is_file():
            continue  # subfolders are visited in their own right by the walk
        base, extension, version = split_version(entry)
        # setdefault returns the existing list for this key, or inserts a new
        # empty list first. Saves the usual "if key not in dict" dance.
        groups.setdefault((base, extension), []).append((version, entry))

    for (base, extension), members in sorted(groups.items()):
        if len(members) < 2:
            continue  # a file with no versioned sibling stays put

        numbers = [version for version, _entry in members]
        highest = max(numbers)

        # Two files can only share a version number through leading zeros
        # (Foo_v08 and Foo_v8) or a case difference in the _v. Which one is
        # current is then genuinely unclear, so the tool declines to guess and
        # leaves the whole group alone for a human to sort out.
        if len(set(numbers)) != len(numbers):
            names = ", ".join(entry.name for _version, entry in members)
            events.append(Event(
                "AMBIGUOUS", folder,
                "{}{}: duplicate version numbers, nothing moved ({})"
                .format(base, extension, names)
            ))
            continue

        superseded_dir = folder / SUPERSEDED_FOLDER_NAME

        for version, entry in sorted(members):
            if version == highest:
                continue  # the current version stays exactly where it is

            destination = superseded_dir / entry.name

            # Never overwrite. An existing file of the same name in
            # _superseded means two different documents are competing for one
            # archive slot; that is a decision for a person, not for a script.
            if destination.exists():
                events.append(Event(
                    "CONFLICT", folder,
                    "{} left in place: {}/{} already exists"
                    .format(entry.name, SUPERSEDED_FOLDER_NAME, entry.name)
                ))
                continue

            moves.append(PlannedMove(
                source=entry,
                destination=destination,
                reason="v{} superseded by v{}".format(version, highest),
            ))

    return moves, events


# ---------------------------------------------------------------------------
# Doing the work
# ---------------------------------------------------------------------------

def apply_moves(moves, dry_run):
    """
    Carry out the planned moves (or, in a dry run, describe them).

    Returns the list of events describing what happened.
    """
    events = []

    for move in moves:
        folder = move.source.parent

        if dry_run:
            events.append(Event(
                "WOULD MOVE", folder,
                "{}  ({})".format(move.source.name, move.reason)
            ))
            continue

        try:
            # Created lazily, so folders with nothing to archive never gain an
            # empty _superseded. mkdir with exist_ok=True is a no-op if it is
            # already there.
            move.destination.parent.mkdir(exist_ok=True)

            # A last existence check immediately before the move. plan_folder
            # already checked, but the destination could have appeared since -
            # and shutil.move would silently overwrite it on Linux and macOS.
            if move.destination.exists():
                events.append(Event(
                    "CONFLICT", folder,
                    "{} left in place: {}/{} appeared during the run"
                    .format(move.source.name, SUPERSEDED_FOLDER_NAME,
                            move.source.name)
                ))
                continue

            shutil.move(str(move.source), str(move.destination))
            events.append(Event(
                "MOVED", folder,
                "{}  ({})".format(move.source.name, move.reason)
            ))
        except OSError as error:
            # A locked file, a read-only folder, a permissions problem. Report
            # it and carry on with the rest - one bad file should not abandon
            # the whole tree half-tidied.
            events.append(Event(
                "ERROR", folder,
                "{} could not be moved: {}".format(move.source.name, error)
            ))

    return events


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def build_report(scope, settings_path, dry_run, folder_count, events):
    """
    Build the run report as a list of lines.

    One function produces both the on-screen report and the log entry, so the
    two can never drift apart.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing changed)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("version cleanup   {}   {}".format(timestamp, mode))
    lines.append("root:     {}".format(scope.root))
    lines.append("settings: {}".format(settings_path))
    # Scope overrides are echoed only when in use. They decide which folders
    # were touched, so a log entry is not self-explaining without them.
    if scope.include_text:
        lines.append("include:  {}".format(", ".join(scope.include_text)))
    if scope.exclude_text:
        lines.append("exclude:  {}".format(", ".join(scope.exclude_text)))
    lines.append("folders processed: {}".format(folder_count))
    lines.append("-" * 72)

    if not events:
        lines.append("Nothing to do - every document in the tree is already "
                     "at its current version.")
    else:
        # Events are reported grouped by folder, which is how someone reading
        # the report actually thinks about the tree.
        current_folder = None
        for event in events:
            if event.folder != current_folder:
                current_folder = event.folder
                lines.append("")
                lines.append("[{}]".format(relative_to(event.folder,
                                                       scope.root)))
            lines.append("  {:<11} {}".format(event.kind, event.detail))

    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1

    summary = ", ".join(
        "{} {}".format(counts[kind], kind.lower())
        for kind in ("MOVED", "WOULD MOVE", "CONFLICT", "AMBIGUOUS", "ERROR")
        if kind in counts
    ) or "no changes"

    lines.append("")
    lines.append("-" * 72)
    lines.append("Result: {}".format(summary))
    lines.append("=" * 72)
    return lines


def relative_to(path, root):
    """Show a path relative to the root when possible - shorter to read."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


def append_to_log(log_path, lines):
    """
    Append one entry to the log. The log is never rewritten or trimmed.

    Failing to write the log must not lose the report that is already on
    screen, so a problem here is reported and swallowed.
    """
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        # "a" is append mode: the file is created if absent, and writes always
        # go to the end. newline="" leaves line endings to us, so the log looks
        # the same on every platform.
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
        # The root is resolved first, because "~/" in the other settings is
        # measured from it.
        root = resolve_one_folder(
            tidy_setting_text(settings.get("root", ".."), "root"), "root"
        )
        scope = build_scope(root, settings.get("include"),
                            settings.get("exclude"))
        log_path = resolve_one_folder(
            tidy_setting_text(settings.get("log_file", "version_cleanup.log"),
                              "log_file"),
            "log_file", root=root
        )
    except ValueError as error:
        print("SETTINGS PROBLEM")
        print(error)
        return 1

    if not root.is_dir():
        print("SETTINGS PROBLEM")
        print('The "root" setting does not point at a folder that exists:')
        print("  {}".format(root))
        print("  (from settings file {})".format(settings_path))
        return 1

    folders = folders_to_process(scope)

    all_events = []
    for folder in folders:
        moves, plan_events = plan_folder(folder)
        all_events.extend(plan_events)
        all_events.extend(apply_moves(moves, dry_run))

    # Report in folder order rather than in the order things happened, so
    # conflicts and moves in the same folder appear together.
    all_events.sort(key=lambda event: (str(event.folder), event.kind))

    lines = build_report(scope, settings_path, dry_run, len(folders),
                         all_events)
    print("\n".join(lines))

    # Dry runs are logged too, clearly marked, so the log is a complete record
    # of every time the tool was pointed at the tree.
    append_to_log(log_path, lines)
    print("\nLog: {}".format(log_path))

    had_problems = any(event.kind in ("ERROR",) for event in all_events)
    return 1 if had_problems else 0


def main():
    parser = argparse.ArgumentParser(
        description="Move superseded document versions into _superseded "
                    "subfolders. Reads its settings from {} beside the script."
                    .format(SETTINGS_FILENAME)
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",  # present = True, absent = False
        help="report what would move without changing anything",
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
