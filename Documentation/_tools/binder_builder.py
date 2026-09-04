#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
binder builder - gather the documents of a defined scope into one file.

WHAT IT DOES
    Walks a folder tree, collects every in-scope file, and writes them into a
    single Markdown "binder" that can be dropped into an AI session's context,
    so a whole topic loads as one artefact rather than as many files.

    The binder carries a header, a manifest of what it contains with a sha256
    digest per file, and then each source file verbatim between comment
    delimiters.

WHAT IT DOES NOT DO
    It does not resolve versions - that is version cleanup's job, run first -
    and it does not deploy. It collects and assembles, nothing else.

    Source content is copied UNMODIFIED. No reformatting, no heading demotion,
    no normalisation. A binder that alters its sources would be worse than no
    binder at all.

HOW IT IS RUN
    Live by default. Pass --dry-run to see the report without writing
    anything. It reads its settings from a JSON file sitting beside this
    script, so it can simply be double-clicked on Windows.

    The settings file IS the binder definition - it declares the scope. One
    binder means one instance folder; a second binder means a second copy of
    the tool, not a second entry in one settings file.

DESIGN NOTE
    This is one tool that does one thing, and a sibling to version cleanup.
    The path logic, settings loader and plan/apply split below are deliberately
    the same shape as that tool's, copied rather than imported: there is no
    shared module, no plugin system and no base class between them.

Python 3.8 or newer. Standard library only.
"""

import argparse
import datetime
import fnmatch
import hashlib
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

SETTINGS_FILENAME = "binder_builder_settings.json"
SUPERSEDED_FOLDER_NAME = "_superseded"

# Folders skipped unless the settings explicitly include them. The leading
# underscore rule is the important one: it keeps the walk out of _superseded
# and out of the tool's own _binder output, which is what makes it impossible
# for a binder to contain a previous binder.
ASSET_FOLDER_NAMES = ("assets", "images", "img", "media")

DEFAULT_FILE_TYPES = ("md", "yaml", "yml", "json", "txt", "py")

# Matches "<Name>_Binder_v<number>.md" so the output folder can be scanned for
# the highest version already written. The name is substituted in escaped, and
# matching is done against a case-folded filename, so the pattern itself does
# not need to worry about case.
BINDER_FILENAME = "{name}_Binder_v{number}.md"

# Spots "C:" or "D:" at the start of a settings path, so a Windows path in a
# settings file being run on Mac or Linux fails loudly rather than being
# mistaken for a relative pattern that then silently never matches anything.
WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:")

# Digests are truncated sha256. Twelve hex characters is plenty to answer
# "is this binder still in step with the masters" without filling the manifest
# with noise.
DIGEST_LENGTH = 12

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
  "_comment": "Settings for the binder builder. This file IS the binder definition - it declares what the binder contains. One binder per copy of the tool: a second binder means a second folder with its own copy of the script and its own settings, not a second entry here. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_name": "The binder's name. Used in the heading (\\"<name> Binder\\") and in the filename (\\"<name>_Binder_v<number>.md\\").",
  "name": "Documentation",

  "_comment_root": "The folder the binder is built from, including everything beneath it unless subfolders is false. A relative path is resolved against the folder this script lives in, so \\"..\\" means the parent folder. Give a full path such as \\"C:/Users/you/Documents\\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_subfolders": "true walks the whole tree from root. false collects from root only.",
  "subfolders": true,

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \\"C:/Docs/_binder\\" - names one exact folder. ROOT-ANCHORED - \\"~/_binder\\" - names one exact folder, measured from the root above. RELATIVE - \\"_binder\\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_include": "Folders skipped by default that should be collected from anyway. Skipped by default: any folder whose name starts with an underscore, and the asset folders assets, images, img and media. Including a folder does not include its underscore-prefixed children.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \\"_superseded\\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_file_types": "File extensions to collect, without the dot.",
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],

  "_comment_exclude_files": "Filename patterns to skip regardless of type. * matches anything, ? matches one character. Live state - work in progress, working notes, open items, work registers - is normally excluded here and loaded separately when it is needed. Example: [\\"*_WIP_*\\", \\"*_Working_*\\", \\"README.md\\"]",
  "exclude_files": [],

  "_comment_order": "Optional. Filenames pulled to the front of the binder, in the order listed. Everything not named here follows, sorted by path. A name that matches nothing in scope is reported, not silently ignored.",
  "order": [],

  "_comment_output": "The folder the binder is written to. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder. The default \\"~/_binder\\" is an underscore folder inside the root, so it is skipped by the walk and a binder can never contain itself.",
  "output": "~/_binder",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \\"~/\\" for root-anchored, or relative to the script folder.",
  "log_file": "binder_builder.log"
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


# The vocabulary, in the order a summary line lists it. INCLUDED/WOULD INCLUDE
# and WRITTEN/WOULD WRITE are the same event seen live and in a dry run, which
# is the same shape version cleanup uses for MOVED/WOULD MOVE. CONFLICT and
# ERROR mean exactly what they mean there.
REPORT_KINDS = (
    "INCLUDED",      # file placed in the binder
    "WOULD INCLUDE", # dry run: the same file, nothing written
    "SKIPPED",       # in a collected folder, deliberately left out
    "UNMATCHED",     # an "order" entry naming a file that is not in scope
    "WRITTEN",       # the binder file itself
    "WOULD WRITE",   # dry run equivalent
    "SUPERSEDED",    # the previous binder moved into _superseded
    "WOULD SUPERSEDE",
    "CONFLICT",      # a destination name is already taken; nothing overwritten
    "EMPTY",         # nothing in scope; no binder written, previous left alone
    "INCOMPLETE",    # a source could not be read; the binder has a hole in it
    "ERROR",         # filesystem refusal
)


@dataclass
class SourceFile:
    """One file selected for the binder, with its place in the order."""
    path: Path
    sort_key: tuple


@dataclass
class BinderPart:
    """One assembled section of the binder body, and its digest."""
    path: Path
    label: str      # how the file is named in the manifest and delimiters
    text: str       # the section as it will appear, delimiters included
    digest: str     # sha256 of the source bytes written, truncated


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
        print("This file is the binder definition, so it almost certainly "
              "needs editing.")
        print("Review it, then run the tool again.")
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


def read_string_list(settings, key):
    """Read a settings value that must be a list of strings, or absent."""
    values = settings.get(key)
    if values is None:
        return []
    if not isinstance(values, list):
        raise ValueError(
            'Setting "{}" must be a list, written in square brackets, for '
            'example ["one", "two"].'.format(key)
        )
    return [str(value).strip() for value in values if str(value).strip()]


def read_flag(settings, key, default):
    """Read a true/false setting, rejecting the string "true" politely."""
    value = settings.get(key, default)
    if isinstance(value, bool):
        return value
    raise ValueError(
        'Setting "{}" must be true or false, without quotes around it.'
        .format(key)
    )


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
# the tree being collected from and can never quietly resolve to
# C:\\Users\\someone.
#
# This is the same model as version cleanup, ratified as the Infrastructure-wide
# convention. Two sibling tools with different path semantics would be a trap.

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

    Used for the root, the output folder and the log file. Include and exclude
    go through parse_scope_entry instead, because they also accept patterns.
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
    subfolders: bool = True
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

    def is_skipped_by_default(self, path):
        """
        Folders left out unless the settings ask for them.

        The underscore rule is the load-bearing one: it keeps the walk out of
        _superseded and out of the tool's own _binder output folder, which is
        what makes it structurally impossible for a binder to include a binder.
        Asset folders are excluded by name because their contents are not
        documents.
        """
        name = path.name
        if name.startswith("_"):
            return True
        return os.path.normcase(name) in ASSET_FOLDER_NAMES

    def should_descend(self, path):
        """
        Should the walk go *into* this folder?

        Note the difference between descending and collecting. A folder that is
        not itself collected from may still need to be walked through, because
        something deeper down is on the include list. It is traversed, but its
        own files are left alone.
        """
        if self.is_excluded(path):
            return False
        if not self.is_skipped_by_default(path):
            return True
        if self.is_included(path):
            return True
        # Is this folder on the way to an exactly-named include?
        if any(is_inside(folder, path) for folder in self.include_folders):
            return True
        return self.leads_to_include_pattern(path)

    def should_collect(self, path):
        """Should this folder's own files go into the binder?"""
        if self.is_excluded(path):
            return False
        if not self.is_skipped_by_default(path):
            return True
        # Only an explicit include overrides the default skip. Note that
        # including a folder does not include its underscore-prefixed children:
        # each folder is asked this question in its own right.
        return self.is_included(path)


def build_scope(root, subfolders, include_values, exclude_values):
    """Turn the raw include and exclude settings into a Scope."""
    scope = Scope(root=root, subfolders=subfolders)

    for label, values in (("include", include_values),
                          ("exclude", exclude_values)):
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


def folders_to_collect(scope):
    """
    Walk the tree from the root and return the folders whose files belong in
    the binder, in a stable, predictable order.
    """
    root = scope.root

    if not scope.subfolders:
        # "subfolders": false means the root and nothing else. An explicit
        # exclude of the root still wins.
        return [] if scope.is_excluded(root) else [root]

    found = []

    # os.walk visits every folder beneath root. With topdown=True (the default)
    # it hands us the list of subfolder names *before* descending, and editing
    # that list in place prunes the walk - the standard way to skip whole
    # branches cheaply. Pruning is also what makes exclusion inherited: once a
    # folder is skipped, nothing inside it is ever looked at, so there is no
    # need to ask again further down. Symbolic links to folders are not
    # followed by default, which is what we want: a link should not cause the
    # same documents to appear in the binder twice.
    for dirpath, dirnames, _filenames in os.walk(root):
        current = Path(dirpath)

        # dirnames[:] = ... replaces the contents of the existing list rather
        # than rebinding the name. os.walk only notices the former.
        dirnames[:] = sorted(
            name for name in dirnames if scope.should_descend(current / name)
        )

        if current == root:
            # The root was chosen deliberately by whoever edited the settings,
            # so the default skips do not apply to it. An explicit exclude
            # still does.
            collect = not scope.is_excluded(current)
        else:
            collect = scope.should_collect(current)

        if collect:
            found.append(current)

    return found


# ---------------------------------------------------------------------------
# File selection
# ---------------------------------------------------------------------------

def matches_any_pattern(name, patterns):
    """
    True if the filename matches one of the exclude_files patterns.

    fnmatch is the standard library's shell-style matcher: * for any run of
    characters, ? for one, [abc] for a set. fnmatch.fnmatch case-folds using
    os.path.normcase, so matching follows the local filesystem the same way
    folder comparison does.
    """
    return any(fnmatch.fnmatch(name, pattern) for pattern in patterns)


def binder_name_pattern(name):
    """
    Matches any binder belonging to this definition: "<Name>_Binder_v<N>.md".

    Used twice, for two different reasons: to find the highest version already
    written, and to keep the tool's own output out of its own input.
    """
    return re.compile(
        r"^" + re.escape(os.path.normcase(name)) + r"_binder_v(\d+)\.md$"
    )


def collect_files(scope, folders, file_types, exclude_files, order,
                  output_folder, output_path, name):
    """
    Choose the files that go into the binder, in binder order. Nothing is read
    here beyond the directory listings.

    Returns (sources, events). Splitting selection from assembly - and both
    from writing - is what makes --dry-run trustworthy: the dry run takes
    exactly the same decisions as a live run, and only the last step differs.
    """
    sources = []
    events = []

    # Order entries are matched on filename, case-folded the way the local
    # filesystem folds names. The dictionary maps a folded filename to its
    # position in the list, which becomes the primary sort key.
    order_rank = {}
    for position, name in enumerate(order):
        order_rank.setdefault(os.path.normcase(name), position)
    order_seen = set()

    wanted_extensions = {"." + extension.lstrip(".").lower()
                         for extension in file_types}

    own_binder = binder_name_pattern(name)

    for folder in folders:
        try:
            entries = sorted(folder.iterdir())
        except OSError as error:
            events.append(Event("ERROR", folder,
                                "cannot read folder: {}".format(error)))
            continue

        for entry in entries:
            if not entry.is_file():
                continue  # subfolders are visited in their own right

            # The defensive self-inclusion check. The output folder is normally
            # underscore-prefixed and therefore already outside the walk, but
            # if someone points "output" at a collected folder, the binder must
            # not swallow itself. Two things are refused: the file this run is
            # about to write, and any earlier binder of this same definition
            # sitting in the output folder. The second is the one that actually
            # bites - this run's own output does not exist yet, but last run's
            # does, and including it would nest a binder inside a binder and
            # double the corpus on every build.
            if normalise(entry) == normalise(output_path):
                events.append(Event(
                    "SKIPPED", folder,
                    "{}: this is the binder's own output file".format(entry.name)
                ))
                continue
            if normalise(entry.parent) == normalise(output_folder) and \
                    own_binder.match(os.path.normcase(entry.name)):
                events.append(Event(
                    "SKIPPED", folder,
                    "{}: this is an earlier version of this binder"
                    .format(entry.name)
                ))
                continue

            if entry.suffix.lower() not in wanted_extensions:
                # Not reported. A document tree is full of files of other
                # types and listing every one of them would bury the report.
                continue

            if matches_any_pattern(entry.name, exclude_files):
                events.append(Event(
                    "SKIPPED", folder,
                    "{}: matches an exclude_files pattern".format(entry.name)
                ))
                continue

            folded = os.path.normcase(entry.name)
            if folded in order_rank:
                rank = order_rank[folded]
                order_seen.add(folded)
            else:
                # Everything not named in "order" sorts after everything that
                # is. len(order_rank) is one past the last explicit position.
                rank = len(order_rank)

            # Within a rank, sort by path so the binder is reproducible.
            # normcase keeps the ordering consistent with how the filesystem
            # itself compares names.
            sources.append(SourceFile(
                path=entry,
                sort_key=(rank, os.path.normcase(str(entry))),
            ))

    sources.sort(key=lambda source: source.sort_key)

    # An "order" entry that matched nothing is a quiet defect: the binder is
    # assembled in an order its author did not get. Say so.
    for name in order:
        if os.path.normcase(name) not in order_seen:
            events.append(Event(
                "UNMATCHED", scope.root,
                'order entry "{}" matched no file in scope'.format(name)
            ))

    return sources, events


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
# Encoding, stated rather than inherited from the platform:
#
#   READ   the file's bytes, then decode as UTF-8. The "utf-8-sig" codec is
#          used, which is plain UTF-8 except that it removes a byte-order mark
#          if one is present. This is the single deviation from byte-for-byte
#          copying, and it is deliberate: a BOM is a start-of-file marker, and
#          leaving one embedded halfway down a binder produces a stray U+FEFF
#          in the middle of the text.
#   WRITE  UTF-8, no BOM, opened in BINARY mode so that no line-ending
#          translation can happen. Line endings therefore pass through exactly
#          as they were in the source.
#
# Nothing else is altered: no reformatting, no heading demotion, no trimming,
# no normalisation of blank lines. The one adjustment is that a newline is
# added after a source that does not end with one, so that the closing
# delimiter sits on its own line.

BEGIN_DELIMITER = "<!-- BEGIN SOURCE: {label} -->"
END_DELIMITER = "<!-- END SOURCE: {label} -->"


def read_source(path):
    """
    Read one source file. Returns (text, digest).

    The digest is taken over the bytes that will actually be written into the
    binder - text.encode("utf-8") - and not over a separate read of the file.
    That is what makes the manifest a statement about the binder rather than a
    statement about the tree at some other moment.

    Raises OSError for a filesystem refusal and UnicodeDecodeError for a file
    that is not text; both mean the binder cannot contain this file.
    """
    data = path.read_bytes()
    text = data.decode("utf-8-sig")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:DIGEST_LENGTH]
    return text, digest


def assemble_parts(sources, root):
    """
    Read every source and build its section of the binder body.

    Returns (parts, missing, events). `missing` holds the files that could not
    be read: if it is not empty the binder has a hole in it, and every caller
    downstream treats that as loud.
    """
    parts = []
    missing = []
    events = []

    for source in sources:
        label = relative_to(source.path, root).replace("\\", "/")
        try:
            text, digest = read_source(source.path)
        except UnicodeDecodeError as error:
            missing.append(label)
            events.append(Event(
                "ERROR", source.path.parent,
                "{} is not UTF-8 text and was left out: {}"
                .format(source.path.name, error.reason)
            ))
            continue
        except OSError as error:
            missing.append(label)
            events.append(Event(
                "ERROR", source.path.parent,
                "{} could not be read and was left out: {}"
                .format(source.path.name, error)
            ))
            continue

        # The one permitted adjustment: guarantee the closing delimiter starts
        # on a line of its own. An empty file gets no added newline beyond the
        # one that separates the two delimiters.
        body = text
        if body and not body.endswith("\n"):
            body += "\n"

        parts.append(BinderPart(
            path=source.path,
            label=label,
            text="{}\n{}{}\n".format(
                BEGIN_DELIMITER.format(label=label),
                body,
                END_DELIMITER.format(label=label),
            ),
            digest=digest,
        ))

    return parts, missing, events


def build_binder_text(name, version, parts, missing):
    """
    Compose the whole binder: header, manifest, then the bodies.

    The manifest is written from the same `parts` list that produces the body,
    in the same order, using digests computed during assembly. The manifest and
    the body cannot describe different things because they are generated from
    one source of truth in one pass.
    """
    today = datetime.date.today().isoformat()

    lines = []
    lines.append("# {} Binder".format(name))
    lines.append("")
    lines.append("> **Generated Binder - do not edit directly.** Edit the "
                 "individual master documents")
    lines.append("> and regenerate the Binder.")
    lines.append("> **Binder Version {}** ({}).".format(version, today))
    lines.append("")
    lines.append("This Binder is a current-context consumption artefact; "
                 "authoritative masters remain")
    lines.append("individual files.")
    lines.append("")

    # An incomplete binder announces itself in its own first screenful. A
    # reader who never sees the console report or the log still cannot mistake
    # it for the whole topic.
    if missing:
        lines.append("> **INCOMPLETE BINDER - {} source file(s) could not be "
                     "read and are missing:**".format(len(missing)))
        for label in missing:
            lines.append("> - `{}`".format(label))
        lines.append(">")
        lines.append("> Do not treat this Binder as a complete statement of "
                     "its scope until it is rebuilt.")
        lines.append("")

    lines.append("## Binder manifest")
    lines.append("")
    if parts:
        for part in parts:
            lines.append("- `{}` - sha256 `{}`".format(part.label, part.digest))
    else:
        lines.append("- (no files)")
    lines.append("")

    header = "\n".join(lines) + "\n"

    sections = []
    for part in parts:
        sections.append("---\n\n" + part.text)

    return header + "\n".join(sections)


# ---------------------------------------------------------------------------
# Versioning and output
# ---------------------------------------------------------------------------

def next_binder_version(output_folder, name):
    """
    Work out this binder's version number by looking at the output folder.

    The folder is the truth; no version is recorded in settings, because a
    number kept in settings drifts from reality the first time a file is moved
    by hand. Scan for existing binders of this name, take the highest, add one.

    Returns (version, previous_path). previous_path is the binder being
    replaced, or None if this is the first.
    """
    pattern = binder_name_pattern(name)

    highest = 0
    previous = None
    if output_folder.is_dir():
        for entry in sorted(output_folder.iterdir()):
            if not entry.is_file():
                continue
            match = pattern.match(os.path.normcase(entry.name))
            if not match:
                continue
            number = int(match.group(1))
            if number > highest:
                highest = number
                previous = entry

    return highest + 1, previous


def write_binder(output_folder, filename, text):
    """
    Write the binder. Binary mode, UTF-8, no BOM, no newline translation.

    Text mode would rewrite "\\n" as "\\r\\n" on Windows, which would silently
    alter every source line ending in the file. Binary mode is the guarantee
    that what was read is what is written.
    """
    output_folder.mkdir(parents=True, exist_ok=True)
    path = output_folder / filename
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    return path


def supersede_previous(previous, dry_run):
    """
    Move the binder this run replaced into _superseded beside it.

    A tool cleans up after itself. The output folder is normally underscore-
    prefixed, so version cleanup skips it by design and would have to be
    explicitly pointed at it purely to tidy after every build. And this is not
    general supersession: the tool knows the single file it just replaced, so
    there is no scanning, grouping or version reasoning here.

    Nothing is ever overwritten.
    """
    folder = previous.parent
    destination = folder / SUPERSEDED_FOLDER_NAME / previous.name

    if dry_run:
        return Event("WOULD SUPERSEDE", folder,
                     "{} -> {}/".format(previous.name, SUPERSEDED_FOLDER_NAME))

    if destination.exists():
        return Event(
            "CONFLICT", folder,
            "{} left in place: {}/{} already exists"
            .format(previous.name, SUPERSEDED_FOLDER_NAME, previous.name)
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
                .format(previous.name, SUPERSEDED_FOLDER_NAME, previous.name)
            )
        shutil.move(str(previous), str(destination))
        return Event("SUPERSEDED", folder,
                     "{} -> {}/".format(previous.name, SUPERSEDED_FOLDER_NAME))
    except OSError as error:
        return Event("ERROR", folder,
                     "{} could not be superseded: {}"
                     .format(previous.name, error))


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def relative_to(path, root):
    """Show a path relative to the root when possible - shorter to read."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return str(path)
    return str(relative) if str(relative) != "." else "."


def build_report(scope, settings_path, dry_run, folder_count, events):
    """
    Build the run report as a list of lines.

    One function produces both the on-screen report and the log entry, so the
    two can never drift apart.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY RUN (nothing written)" if dry_run else "LIVE"

    lines = []
    lines.append("=" * 72)
    lines.append("binder builder   {}   {}".format(timestamp, mode))
    lines.append("root:     {}".format(scope.root))
    lines.append("settings: {}".format(settings_path))
    if not scope.subfolders:
        lines.append("subfolders: false - root folder only")
    # Scope overrides are echoed only when in use. They decide which folders
    # were collected from, so a log entry is not self-explaining without them.
    if scope.include_text:
        lines.append("include:  {}".format(", ".join(scope.include_text)))
    if scope.exclude_text:
        lines.append("exclude:  {}".format(", ".join(scope.exclude_text)))
    lines.append("folders collected from: {}".format(folder_count))
    lines.append("-" * 72)

    if not events:
        lines.append("Nothing happened, which should not be possible - please "
                     "report this.")
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
            lines.append("  {:<16} {}".format(event.kind, event.detail))

    counts = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1

    summary = ", ".join(
        "{} {}".format(counts[kind], kind.lower())
        for kind in REPORT_KINDS if kind in counts
    ) or "nothing to do"

    lines.append("")
    lines.append("-" * 72)
    lines.append("Result: {}".format(summary))
    lines.append("=" * 72)
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

        name = str(settings.get("name", "Documentation")).strip()
        if not name:
            raise ValueError('Setting "name" cannot be empty - it names the '
                             "binder and its file.")
        # The name becomes a filename, so it cannot contain path separators or
        # the characters Windows refuses in one.
        if any(character in name for character in '\\/:*?"<>|'):
            raise ValueError(
                'Setting "name" is "{}", which contains a character that '
                'cannot appear in a filename.'.format(name)
            )

        # The root is resolved first, because "~/" in the other settings is
        # measured from it.
        root = resolve_one_folder(
            tidy_setting_text(settings.get("root", ".."), "root"), "root"
        )
        subfolders = read_flag(settings, "subfolders", True)
        scope = build_scope(root, subfolders,
                            read_string_list(settings, "include"),
                            read_string_list(settings, "exclude"))

        file_types = read_string_list(settings, "file_types") \
            or list(DEFAULT_FILE_TYPES)
        exclude_files = read_string_list(settings, "exclude_files")
        order = read_string_list(settings, "order")

        output_folder = resolve_one_folder(
            tidy_setting_text(settings.get("output", "~/_binder"), "output"),
            "output", root=root
        )
        log_path = resolve_one_folder(
            tidy_setting_text(settings.get("log_file", "binder_builder.log"),
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

    version, previous = next_binder_version(output_folder, name)
    filename = BINDER_FILENAME.format(name=name, number=version)
    output_path = output_folder / filename

    # --- decide -----------------------------------------------------------
    folders = folders_to_collect(scope)
    sources, events = collect_files(scope, folders, file_types, exclude_files,
                                    order, output_folder, output_path, name)
    parts, missing, assembly_events = assemble_parts(sources, root)
    events.extend(assembly_events)

    for part in parts:
        events.append(Event(
            "WOULD INCLUDE" if dry_run else "INCLUDED",
            part.path.parent,
            "{}  (sha256 {})".format(part.path.name, part.digest)
        ))

    # --- act --------------------------------------------------------------
    # An empty scope writes nothing at all. Replacing a good binder with an
    # empty one is a data-loss shape, so the previous binder is left exactly
    # where it is and the run says why.
    if not parts:
        events.append(Event(
            "EMPTY", root,
            "no files in scope - no binder written, any previous binder left "
            "untouched"
        ))
    else:
        binder_text = build_binder_text(name, version, parts, missing)

        if missing:
            events.append(Event(
                "INCOMPLETE", output_folder,
                "{} source file(s) could not be read; the binder is stamped "
                "INCOMPLETE and the previous binder has been left in place"
                .format(len(missing))
            ))

        written_ok = True
        if dry_run:
            events.append(Event(
                "WOULD WRITE", output_folder,
                "{}  ({} files, {} bytes)"
                .format(filename, len(parts),
                        len(binder_text.encode("utf-8")))
            ))
        else:
            try:
                written = write_binder(output_folder, filename, binder_text)
                events.append(Event(
                    "WRITTEN", output_folder,
                    "{}  ({} files, {} bytes)"
                    .format(written.name, len(parts), written.stat().st_size)
                ))
            except OSError as error:
                written_ok = False
                events.append(Event("ERROR", output_folder,
                                    "could not write {}: {}"
                                    .format(filename, error)))

        # Supersede only a genuinely successful, complete write. An incomplete
        # binder must not displace the last good one, and neither must a write
        # that failed.
        if previous is not None and written_ok and not missing:
            events.append(supersede_previous(previous, dry_run))

    # --- report -----------------------------------------------------------
    # Report in folder order rather than in the order things happened, so
    # everything concerning one folder appears together.
    events.sort(key=lambda event: (str(event.folder), event.kind))

    lines = build_report(scope, settings_path, dry_run, len(folders), events)
    print("\n".join(lines))

    # Dry runs are logged too, clearly marked, so the log is a complete record
    # of every time the tool was pointed at the tree.
    append_to_log(log_path, lines)
    print("\nLog: {}".format(log_path))

    # Exit code follows version cleanup: 0 unless the filesystem refused
    # something. A file that could not be read raises an ERROR of its own, so
    # an incomplete binder always exits 1 through that. An EMPTY run does not:
    # it is reported loudly on screen and in the log, but nothing failed.
    had_problems = any(event.kind == "ERROR" for event in events)
    return 1 if had_problems else 0


def main():
    parser = argparse.ArgumentParser(
        description="Assemble the documents of a defined scope into a single "
                    "binder file. Reads its settings from {} beside the "
                    "script.".format(SETTINGS_FILENAME)
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",  # present = True, absent = False
        help="report what would be assembled without writing anything",
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
