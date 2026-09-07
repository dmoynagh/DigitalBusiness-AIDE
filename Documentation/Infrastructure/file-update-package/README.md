# file update package

Deploys a **FileUpdatePackage** — a zip of updated documents produced by a Chat
or Cowork session — into the master document tree, superseding what it replaces
and rebuilding the binder afterwards.

This folder is the **master copy**. To use the tool, copy
`file_update_package.py` and `file_update_package_settings.json` to wherever it
should run from, then edit that copy's settings. Each instance keeps its own
settings file and its own log beside the script, so instances never interfere
with each other.

**It never overwrites.** A file already sitting where a package wants to write,
and not named as the one being replaced, is reported as a `CONFLICT` and left
exactly where it is.

---

## What a package looks like

A zip file containing the documents at their paths relative to the
documentation root, plus a manifest called `_manifest.json` at the zip root:

```
ProjectDesign_2026-09-07.zip
├── _manifest.json
└── Project Design/
    ├── ProjectDesign_Design_v8.md
    └── ProjectDesign_Index_v8.md
```

```json
{
  "created": "2026-09-07T10:00:00Z",
  "description": "Project Design master files - binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "update",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    {
      "path": "Project Design/ProjectDesign_Index_v8.md",
      "action": "create"
    }
  ],
  "user_instructions": "Review the new Overview document before publishing."
}
```

| Field | Meaning |
| --- | --- |
| `path` | Where the file goes, measured from the documentation root. Forward slashes. |
| `action` | `create` for a new file, `update` for one that replaces an existing document. |
| `replaces` | Update only, optional. The **filename** — not a path — of the document being superseded. The tool finds it and moves it into `_superseded`. |
| `description` | Optional. Shown in the report and the completion summary. |
| `user_instructions` | Optional. Shown to you, and the tool waits for you to acknowledge them before it touches anything. |
| `created` | Optional, informational. Packages are ordered by file modification time, not by this. |

**Leaving `replaces` out of an update** means "this replaces the file already at
this path" — that file is moved into `_superseded` and the new one written in
its place. Use it for documents whose filenames do not carry a version.

`Documentation/_config/repo_config.json` maps topic names to folder paths, for
whoever is *building* a package. The tool does not read it; it has its own
settings.

---

## What it does

1. Finds the newest unprocessed `.zip` in the drop folder. Any others wait their
   turn and are reported by name.
2. Validates the package — a zip, with a manifest, that names files it actually
   contains. Anything wrong and the whole package is rejected: `INVALID`, and
   nothing at all is deployed.
3. Shows the package's instructions, if it has any, and waits for you.
4. For each file: moves the document it replaces into `_superseded`, then writes
   the new one.
5. Runs the binder builder. It decides for itself whether a rebuild is needed.
6. Moves the package into `_superseded` inside the drop folder — but only if the
   deploy was complete.
7. Prints a completion summary and holds the window open until you have read it.

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

Double-clicking `file_update_package.py` in File Explorer runs it. If it opens
in Notepad instead, right-click it → **Open with** → **Choose another app** →
pick **Python**, and tick **Always use this app to open .py files**.

Or from a terminal:

```
python "C:\path\to\file_update_package.py"
```

---

## Settings

The script reads `file_update_package_settings.json` from **its own folder** —
not from wherever the terminal happens to be pointing. If that file is missing,
the script writes a fresh one with default values and explanatory notes, then
tells you to check it.

```json
{
  "documentation_root": "..",
  "drop_folder": "~/_fileupdatepackages",
  "binder_builder": "~/_tools/binder_builder.py",
  "log_file": "file_update_package.log"
}
```

| Setting | Meaning |
| --- | --- |
| `documentation_root` | The root of the tree packages deploy into. Manifest paths are measured from here. |
| `drop_folder` | Where packages are put to be deployed. |
| `binder_builder` | The binder builder to run afterwards. Point it at the **running instance**, so it uses that instance's settings. Set it to `""` to skip the trigger. |
| `log_file` | Where the run log is appended. |

### The three path forms

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_fileupdatepackages"` | that exact folder |
| Root-anchored | `"~/_fileupdatepackages"` | measured from `documentation_root` |
| Script-relative | `".."` | measured from the folder holding the script |

`"~"` here means **the documentation root**, never your home folder. The tool
never expands `~` the way a shell would.

`documentation_root` cannot itself use `"~/"` — it is what `"~/"` means. Use
`".."`, which is what an instance sitting in a `_tools` folder wants, or a full
path.

This is the same path model as version cleanup and the binder builder,
deliberately. Three Infrastructure tools with different path semantics would be
a trap. (The *pattern* form those two accept in `include` and `exclude` has no
equivalent here: every setting in this tool names one place.)

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes; a single backslash is an escape character in JSON and will
break the file.

---

## Running it

Live by default — the only prompt is the package's own instructions, if it has
any:

```
python file_update_package.py
```

Report only, changes nothing:

```
python file_update_package.py --dry-run
```

The dry run takes the same decisions as a live run — it validates the package,
works out what would be superseded and what would conflict — and reports them
with `WOULD DEPLOY`, `WOULD CREATE` and `WOULD SUPERSEDE`. It is the safe way to
look at a package you did not build yourself.

---

## The completion summary

This is the point of the run. It is printed whatever happened, and the window
stays open until you have read it:

```
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              ProjectDesign_2026-09-07.zip
                        Project Design master files - binder sweep complete
  files updated:        1
  files created:        1
  files superseded:     1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered - 24 included, 1 written, 1 superseded
  the package is now:   moved to _superseded/
  folder naming:        no misspelled folders found
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

Every conflict and every error is listed individually, with the filename and the
reason. The last line is one of:

| Status | When |
| --- | --- |
| `COMPLETED SUCCESSFULLY` | Nothing went wrong. Also the "no packages to deploy" case. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed, some did not. |
| `FAILED - nothing was deployed` | The package was rejected, or every file in it conflicted. |

---

## The report

| Kind | Meaning |
| --- | --- |
| `DEPLOYED` / `WOULD DEPLOY` | An updated file written into place. |
| `CREATED` / `WOULD CREATE` | A file that did not exist before. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The document being replaced, moved into `_superseded`. |
| `CONFLICT` | A destination is taken, or a `replaces` matched more than one file. Nothing overwritten, nothing moved. |
| `SKIPPED` | No packages to deploy, a package waiting its turn, or a `replaces` naming a file that is not in the tree. |
| `INVALID` | The package was rejected. Nothing in it was deployed. |
| `BINDER` | The binder builder was triggered, and what it said. |
| `PROCESSED` / `WOULD PROCESS` | The package itself, moved into `_superseded`. |
| `ERROR` | A filesystem refusal, or a binder builder run that failed. |

Events appear in the order they happened, so a supersession and the write that
depended on it read as one story. The exit code is `0` unless an `ERROR`
occurred — note that a `CONFLICT` and a rejected package both exit `0`, because
nothing failed: the tool did exactly what it should with what it was given. The
completion summary is where you read the outcome.

### Three cases worth understanding

**`INVALID` — the package was rejected.** Validation is a gate, not a filter. A
package that is wrong in one place is not deployed in the places it happens to
be right, because deploying half of a badly-built package leaves the tree in a
state nobody designed. Fix the package and drop it in again.

**`CONFLICT` — something was in the way.** Either a file already sits where the
package wants to write and the package did not name it as superseded, or a
`replaces` filename was found in several folders and the tool will not guess
which one you meant. Nothing is overwritten and nothing is moved. The run says
exactly which file and why.

**A partial deploy keeps its package.** If anything conflicted, the zip stays in
the drop folder rather than moving to `_superseded` — you will need it when you
sort the conflict out, and a package filed away reads as one that was fully
applied.

---

## The folder naming check

Every run walks the tree and reports any folder whose name is *nearly* one of
the conventions — `_superceded` where `_superseded` was meant, and so on. It
appears in the completion summary and nowhere else.

Only folders whose names start with an underscore are looked at, which is the
class every convention name belongs to. An ordinary folder is never flagged.

It is advisory. It never renames anything, never blocks a deploy and never
changes the exit code.

It exists because a misspelled underscore folder is invisible to every tool in
this family: they all skip underscore folders, so a misspelling does no damage
and raises no complaint — it just quietly splits a convention in two and stays
that way. Naming it on every run is how it stops being forgotten.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date and the mode. The entry is the whole report, completion
summary included. The log is never rewritten or trimmed.

---

## Scope

It places whole files. It does not merge, patch or edit content, it does not
decide what belongs in a package, and it does not do general version resolution
— it moves the single document each manifest entry names. Tidying the rest of
the tree is version cleanup's job.
