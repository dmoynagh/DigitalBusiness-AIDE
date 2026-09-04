# binder builder

Gathers the current documents of a defined scope into a single file, so a whole
topic can be dropped into an AI session's context as one artefact rather than
as many.

This folder is the **master copy**. To use the tool, copy `binder_builder.py`
and `binder_builder_settings.json` to wherever it should run from, then edit
that copy's settings. Each instance keeps its own settings file and its own log
beside the script, so instances never interfere with each other.

**One binder per instance.** The settings file *is* the binder definition — it
declares the scope. A second binder means a second folder with its own copy of
the tool, not a second entry in one settings file.

**Run version cleanup first.** It leaves only current documents in the tree, so
the binder builder can take what it finds without any version reasoning of its
own.

---

## What it produces

```markdown
# <Name> Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 3** (2026-09-04).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `Alpha/Alpha_Design_v3.md` - sha256 `06f6435c91ff`
- `Beta/beta.yaml` - sha256 `75d068ad343e`

---

<!-- BEGIN SOURCE: Alpha/Alpha_Design_v3.md -->
…the file, exactly as it is on disk…
<!-- END SOURCE: Alpha/Alpha_Design_v3.md -->

---

<!-- BEGIN SOURCE: Beta/beta.yaml -->
…
```

Source content is copied **unmodified** — no reformatting, no heading demotion,
no trimming. The manifest lists the files in binder order, with a truncated
sha256 of each source, so a binder can be checked against its masters.

The one adjustment: a newline is added after a source that does not end with
one, so the closing delimiter starts on its own line.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.
4. To check it worked, open PowerShell and run:

   ```
   python --version
   ```

   It should print something like `Python 3.13.1`.

### Making double-click work

The standard installer associates `.py` files with the Python launcher, so
double-clicking `binder_builder.py` in File Explorer should just run it. If it
instead opens in Notepad or asks which app to use:

1. Right-click `binder_builder.py` → **Open with** → **Choose another app**.
2. Pick **Python** (or browse to `C:\Windows\py.exe`).
3. Tick **Always use this app to open .py files**.

The script pauses with *"Press Enter to close..."* when it finishes, so the
console window stays open long enough to read the report.

### Running it from a terminal instead

```
python "C:\path\to\binder_builder.py"
```

---

## Settings

The script reads `binder_builder_settings.json` from **its own folder** — not
from wherever the terminal happens to be pointing. If that file is missing, the
script writes a fresh one with default values and explanatory notes, then tells
you to check it. Since the settings file is the binder definition, a fresh one
almost always needs editing.

```json
{
  "name": "Documentation",
  "root": "..",
  "subfolders": true,
  "include": [],
  "exclude": [],
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],
  "exclude_files": [],
  "order": [],
  "output": "~/_binder",
  "log_file": "binder_builder.log"
}
```

| Setting | Meaning |
| --- | --- |
| `name` | The binder's name — used in the heading and in the filename. |
| `root` | The folder the binder is built from. |
| `subfolders` | `true` walks the whole tree; `false` collects from `root` only. |
| `include` | Folders to collect from that would otherwise be skipped. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `file_types` | Extensions to collect, without the dot. |
| `exclude_files` | Filename patterns to skip regardless of type. |
| `order` | Filenames pulled to the front of the binder, in the order listed. |
| `output` | The folder the binder is written to. |
| `log_file` | Where the run log is appended. |

### Which folders are skipped by default

- Any folder whose name starts with an underscore. This is what keeps the tool
  out of `_superseded` and out of its own `_binder` output — it is the
  mechanism that makes it impossible for a binder to contain a binder.
- The asset folders `assets`, `images`, `img` and `media`, by name.

List a folder in `include` to collect from it anyway. Including a folder does
**not** include its underscore-prefixed children: `_binder` included still skips
`_binder/_superseded`.

### The three path forms

**`root`, `output` and `log_file`** take a full path, a `~/` path measured from
`root`, or a path measured from the folder the script lives in — so `".."`
means "the folder above me", and an instance sitting in `Documentation/_tools`
builds from `Documentation` by default. (`root` itself cannot use `~/`, since it
is what defines the root.)

**`include` and `exclude`** take the same three forms, but the relative one
means something different:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at any
depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`, and the walk passes *through* the underscore parent to
reach it without collecting that parent's own files.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree**, never your home folder. The tool
  never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them. Prefer
  absolute or root-anchored for anything non-obvious.

This is the same path model as version cleanup, deliberately. Two Infrastructure
tools with different path semantics would be a trap.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so the notes in the shipped settings
file are carried as keys beginning with `_comment`. They are ordinary JSON and
the tool ignores them. Leave them, edit them, or delete them as you prefer.

### Excluding live state

Work-in-progress, working, open-items and work-register documents are loaded
separately when active state is actually needed, so they are normally kept out
of the binder. Do that through `exclude_files` in the binder's own settings
rather than expecting the tool to know the names:

```json
"exclude_files": ["*_WIP_*", "*_Working_*", "*_OpenItems_*", "*_WorkRegister_*"]
```

`*` matches any run of characters and `?` matches one, matched
case-insensitively on Windows and case-sensitively elsewhere — the same way the
filesystem does.

### Ordering

Files named in `order` come first, in the order listed. Everything else follows,
sorted by path. Matching is on the filename alone, so an `order` entry catches
that file wherever it lives.

An `order` entry that matches nothing in scope is reported as `UNMATCHED` rather
than passed over, because a binder assembled in an order its author did not get
is a quiet defect.

---

## Versioning and output

The binder is written as `<Name>_Binder_v<N>.md`, with a counter of its own,
independent of the versions of the documents inside it.

The version is worked out by **scanning the output folder** — highest `N` found,
write `N+1`. Nothing is recorded in settings, because a number kept in settings
drifts from reality the first time a file is moved by hand.

On a successful write, the previous binder of that name is moved into
`_superseded` inside the output folder. A tool cleans up after itself; version
cleanup handles supersession it did not cause. Nothing is ever overwritten — if
the `_superseded` slot is taken, the run reports `CONFLICT` and leaves the file
alone.

---

## Running it

Live by default — there is no confirmation prompt:

```
python binder_builder.py
```

Report only, writes nothing:

```
python binder_builder.py --dry-run
```

The dry run takes exactly the same decisions as a live run — it reads every
source and computes every digest — and reports them with `WOULD INCLUDE` and
`WOULD WRITE` in place of `INCLUDED` and `WRITTEN`. It is the safe way to check
a new scope before letting the tool write anything.

---

## The report

| Kind | Meaning |
| --- | --- |
| `INCLUDED` | File placed in the binder, with its digest. |
| `WOULD INCLUDE` | Dry run — the same file, nothing written. |
| `SKIPPED` | In a collected folder, deliberately left out — an `exclude_files` match, or the tool's own output. |
| `UNMATCHED` | An `order` entry naming a file that is not in scope. |
| `WRITTEN` / `WOULD WRITE` | The binder itself. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The previous binder moved into `_superseded`. |
| `CONFLICT` | A destination name is already taken; nothing overwritten. |
| `EMPTY` | Nothing in scope. No binder written; any previous binder left alone. |
| `INCOMPLETE` | A source could not be read. The binder has a hole in it. |
| `ERROR` | A filesystem refusal — a locked file, permissions, an unreadable folder. |

Events are grouped by folder. The exit code is `0` unless at least one `ERROR`
occurred.

### Two cases worth understanding

**`EMPTY` — nothing was in scope.** No binder is written and the previous binder
is left exactly where it is. An empty binder replacing a good one would be a
loss of information dressed up as a successful build. If you see this, the scope
settings are almost certainly wrong.

**`INCOMPLETE` — a source could not be read.** The binder is written, but it has
a hole in it, so it is stamped as incomplete in three places: the report, the
log, and a block near the top of the binder itself naming every missing file.
The previous binder is **not** superseded, so the last good one stays available.
A plausible-looking binder that is quietly missing a document is the worst thing
this tool could produce, so it is made loud in every place someone might look.

---

## Text encoding

Stated explicitly rather than left to the platform:

- **Read** as UTF-8, with a byte-order mark removed if one is present. That BOM
  removal is the only deviation from byte-for-byte copying, and it is
  deliberate: a BOM is a start-of-file marker, and leaving one embedded halfway
  down a binder puts a stray character in the middle of the text.
- **Write** as UTF-8 without a BOM, in binary mode so that no line-ending
  translation can happen. Line endings pass through exactly as they were in the
  source.

A file that is not valid UTF-8 cannot go into the binder. It is reported as an
`ERROR`, and the binder it would have gone into is stamped `INCOMPLETE`.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log is never
rewritten or trimmed. If it grows unwieldy, archive or delete it by hand; the
tool will start a fresh one.

---

## Scope

It collects and assembles. It does not resolve versions — that is version
cleanup's job, run first — and it does not deploy. It is Infrastructure: it acts
on the corpus and is never loaded into an AI session itself.
