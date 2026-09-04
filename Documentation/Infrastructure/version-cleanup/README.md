# version cleanup

Moves superseded document versions out of the live tree, so a folder only ever
shows the current version of each document.

This folder is the **master copy**. To use the tool, copy `version_cleanup.py`
and `version_cleanup_settings.json` to wherever it should run from, then edit
that copy's settings. Each instance keeps its own settings file and its own log
beside the script, so instances never interfere with each other.

---

## What it does

In each folder it visits, it looks for files whose names are identical apart
from a `_v<number>` suffix immediately before the extension. The highest number
stays put; every lower version moves into a `_superseded` subfolder of the same
folder.

| Files in a folder | Result |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` moves, `Foo_v9.md` stays |
| `Foo.md`, `Foo_v1.md` | `Foo.md` moves — no suffix counts as v0 |
| `Foo_v3.md` on its own | nothing happens |
| `Foo_v1.md`, `Foo_v2.txt` | nothing happens — extensions must match too |

Grouping is **per folder**. The walk is recursive, but `Foo_v8.md` in one folder
is never compared with `Foo_v9.md` in another. Anything more complicated than
that is a manual job.

Folders whose name starts with an underscore are skipped, which is what keeps
the tool out of the `_superseded` folders it creates.

Nothing is ever overwritten. If a file of the same name is already sitting in
`_superseded`, the source file is left where it is and the run reports a
conflict.

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
double-clicking `version_cleanup.py` in File Explorer should just run it. If it
instead opens in Notepad or asks which app to use:

1. Right-click `version_cleanup.py` → **Open with** → **Choose another app**.
2. Pick **Python** (or browse to `C:\Windows\py.exe`).
3. Tick **Always use this app to open .py files**.

The script pauses with *"Press Enter to close..."* when it finishes, so the
console window stays open long enough to read the report.

### Running it from a terminal instead

```
python "C:\path\to\version_cleanup.py"
```

---

## Settings

The script reads `version_cleanup_settings.json` from **its own folder** — not
from wherever the terminal happens to be pointing. If that file is missing, the
script writes a fresh one with default values and explanatory notes, then tells
you to check it.

```json
{
  "root": "..",
  "include": [],
  "exclude": [],
  "log_file": "version_cleanup.log"
}
```

| Setting | Meaning |
| --- | --- |
| `root` | The folder to tidy, including everything beneath it. |
| `include` | Underscore-prefixed folders to process anyway. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `log_file` | Where the run log is appended. |

**`root` and `log_file`** take a full path, or a path measured from the folder
the script lives in — so `".."` means "the folder above me", and an instance
sitting in `Documentation/_tools` tidies `Documentation` by default.

**`include` and `exclude`** take three kinds of path:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at
any depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree being tidied**, never your home
  folder. The tool never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so the notes in the shipped settings
file are carried as keys beginning with `_comment`. They are ordinary JSON and
the tool ignores them. Leave them, edit them, or delete them as you prefer.

**Exclude always wins over include**, and excluding a folder excludes
everything inside it.

To reach a folder nested inside an underscore-prefixed one, just name the
folder you actually want — the walk passes through the underscore folder to
get there without processing its own files.

Example: process every `_binder` in the tree, plus the one `_holding` folder
at the top, and stay out of one scratch area entirely.

```json
{
  "root": "..",
  "include": ["_binder", "~/_holding"],
  "exclude": ["~/Working Practices/scratch"],
  "log_file": "version_cleanup.log"
}
```

The run report echoes the include and exclude lists whenever they are in use,
so a log entry always says which rules produced it.

---

## Running it

Live by default — there is no confirmation prompt:

```
python version_cleanup.py
```

Report only, changes nothing:

```
python version_cleanup.py --dry-run
```

The dry run produces exactly the same report as a live run, with `WOULD MOVE`
in place of `MOVED`. It is the safe way to check a new `root` or a new
include/exclude list before letting the tool loose on a tree.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log is
never rewritten or trimmed. If it grows unwieldy, archive or delete it by hand;
the tool will start a fresh one.

---

## When it declines to act

Two cases where the tool deliberately does nothing and tells you instead:

- **CONFLICT** — a file of that name already exists in `_superseded`. Two
  different documents are competing for one archive slot. Resolve it by hand.
- **AMBIGUOUS** — two files in the folder claim the same version number, which
  can only happen through leading zeros (`Foo_v08.md` and `Foo_v8.md`). Nothing
  in that group moves, because which one is current is genuinely unclear.

---

## Scope

It tidies versions. It does not build binders and it does not deploy anything.
Those are separate tools, run in sequence.
