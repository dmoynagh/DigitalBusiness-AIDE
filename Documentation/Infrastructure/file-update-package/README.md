# file update package

Deploys a **FileUpdatePackage** — a zip of updated documents produced by a Chat
or Cowork session — into the master document tree, deleting what it replaces
and rebuilding the binder afterwards.

The tool is `aide fup`, one of the utilities built into the `aide` CLI
(`aide-cli`, in the deploy repo `DigitalBusiness-AIDE-Deploy`, distributed via
`aide update`). This folder holds the design documentation for the tool, not
the tool itself — there is no standalone script to run here.

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
      "action": "replace",
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

A third action, `move`, renames or relocates a document already in the tree
without touching its content — no `path` inside the zip is needed for it:

```json
{
  "action": "move",
  "old_path": "Standards/OldName_v3.md",
  "new_path": "Standards/NewName_v3.md"
}
```

| Field | Meaning |
| --- | --- |
| `path` | Where the file goes, measured from the documentation root. Forward slashes. `create`/`replace` only. |
| `action` | `create` for a new file, `replace` for one that supersedes an existing document, `move` to rename or relocate a file already in the tree. `update` is still accepted as a synonym for `replace`, for packages built before the rename. |
| `replaces` | `replace` only, optional. The **filename** — not a path — of the document being superseded. The tool finds it and deletes it. |
| `old_path` / `new_path` | `move` only, required. Both measured from the documentation root. |
| `description` | Optional. Shown in the report and the completion summary. |
| `user_instructions` | Optional. Shown to you; a live run in an interactive console waits for you to press Enter before deploying anything (see *The instructions gate* below). |
| `created` | Optional, informational. Packages are ordered by file modification time, not by this. |

**Choosing `create` vs `replace`.** `create` means the file does not yet exist in
the tree. If a file already sits at the destination path — from a prior deploy,
a partial run, or manual placement — use `replace`, not `create`. The tool will
`CONFLICT` on a `create` that finds an occupied path rather than risk
overwriting something it was not told about.

**Leaving `replaces` out of a `replace`** means "this replaces the file already
at this path" — that file is deleted and the new one written in its place. Use
it for documents whose filenames do not carry a version.

`Documentation/_config/repo_config.json` maps topic names to folder paths, for
whoever is *building* a package. The tool does not read it; it has its own
settings.

---

## What it does

1. Finds the newest unprocessed `.zip` in the drop folder. Any others wait their
   turn and are reported by name.
2. Validates the package — a zip, with a manifest, that names files it actually
   contains and actions it recognises. Anything wrong and the whole package is
   rejected: `INVALID`, and nothing at all is deployed.
3. Shows the package's instructions, if it has any, and — in a live run with an
   interactive console — waits for you to acknowledge them.
4. For each entry: `create` writes a new file; `replace` deletes the document
   it supersedes, then writes the new one; `move` renames or relocates a file
   already in the tree, content unchanged.
5. Runs `aide binder`, unless `trigger_binder` is set to `false` or nothing was
   deployed. It decides for itself whether a rebuild is needed.
6. Deletes the package from the drop folder — but only if the deploy was
   complete. If anything deployed, the tool also stages and commits the
   change, with a message such as `fup: applied ProjectDesign_2026-09-07 (1
   replaced, 1 created)`.
7. Prints a completion summary.

There is no `_superseded` folder in any of this — deleted files and the
processed package are gone from the working tree, and git history is the
record of what they contained.

---

## Running it

From anywhere inside a project (the tool walks up from the current folder to
find `_aide/`):

```
aide fup              # live — the only prompt is the package's own instructions, if it has any
aide fup --dry-run    # report only, changes nothing
```

The dry run takes the same decisions as a live run — it validates the package,
works out what would be deleted and what would conflict — and reports them
with `WOULD REPLACE`, `WOULD CREATE`, `WOULD MOVE` and `WOULD DELETE`. It is
the safe way to look at a package you did not build yourself. A dry run shows
`user_instructions` but does not wait for acknowledgement, since nothing is
actually about to happen.

---

## The instructions gate

If the manifest carries `user_instructions`, they are printed before anything
is touched. In a live run with an interactive console attached, the tool then
waits — `Press Enter to continue with the deploy, or Ctrl+C to stop...` —
before deploying. Outside an interactive console (a script, a CI-style run) it
logs that it continued without acknowledgement rather than hanging. Either way
the completion summary's `user instructions:` line states exactly what
happened: shown and acknowledged, shown but not acknowledged (and why), or
present but not gated (dry run).

---

## Settings

`aide fup` reads the `fup` key of the project's per-project runtime settings
file, `_aide/settings.json` — not a settings file of its own:

```json
{
  "fup": {
    "drop_folder": "~/_fileupdatepackages",
    "trigger_binder": true,
    "log_file": "~/_aide/utilities/file-update-package/file_update_package.log"
  }
}
```

Anything left out falls back to the package default shipped with `aide-cli`
(shown above — these *are* the defaults).

| Setting | Meaning |
| --- | --- |
| `drop_folder` | Where packages are put to be deployed. |
| `trigger_binder` | Whether to run `aide binder` after a deploy that wrote something. Set `false` to skip it. |
| `log_file` | Where the run log is appended. |

There is no `binder_builder` path setting any more — `aide fup` calls `aide
binder` in-process, using the project's own binder settings
(`_aide/utilities/binder-builder/`), so there is nothing to point at.

### Path forms

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_fileupdatepackages"` | that exact folder |
| Root-anchored | `"~/_fileupdatepackages"` | measured from the documentation root (the project root, where `_aide/` lives) |

`"~"` here means **the documentation root**, never your home folder. The tool
never expands `~` the way a shell would.

This is the same path model as version cleanup and the binder builder,
deliberately. Three Infrastructure tools with different path semantics would be
a trap. (The *pattern* form those two accept in `include` and `exclude` has no
equivalent here: every setting in this tool names one place.)

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes; a single backslash is an escape character in JSON and will
break the file.

---

## The completion summary

This is the point of the run. It is always printed:

```
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              ProjectDesign_2026-09-07.zip
                        Project Design master files - binder sweep complete
  files replaced:       1
  files created:        1
  files moved:          0
  files deleted:        1
  conflicts:            0
  errors:                0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered
  the package is now:   deleted
  folder naming:        no misspelled folders found
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

`files deleted` counts the superseded document each `replace` removes — a
`replace` produces both a `DELETED` event (the old file) and a `REPLACED`
event (the new one), so a package with one `replace` typically shows `files
replaced: 1` and `files deleted: 1`. Every conflict and every error is listed
individually, with the filename and the reason. The last line is one of:

| Status | When |
| --- | --- |
| `COMPLETED SUCCESSFULLY` | Nothing went wrong. |
| `COMPLETED SUCCESSFULLY - there was nothing to do` | No packages in the drop folder. |
| `COMPLETED SUCCESSFULLY - dry run, nothing was changed` | Dry run, no problems found. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed, some did not. |
| `FAILED - nothing was deployed` | The package was rejected, or every file in it conflicted. |

---

## The report

| Kind | Meaning |
| --- | --- |
| `REPLACED` / `WOULD REPLACE` | An updated file written into place. |
| `CREATED` / `WOULD CREATE` | A file that did not exist before. |
| `MOVED` / `WOULD MOVE` | A file renamed or relocated, content unchanged. |
| `DELETED` / `WOULD DELETE` | The document a `replace` superseded, removed from the tree. |
| `CONFLICT` | A destination is taken, a `replaces` matched more than one file, or a `move` source/destination is missing or already occupied. Nothing overwritten, nothing moved. |
| `SKIPPED` | No packages to deploy, a package waiting its turn, or a `replaces` naming a file that is not in the tree. |
| `INVALID` | The package was rejected. Nothing in it was deployed. |
| `BINDER` | `aide binder` was triggered, and what it said. |
| `PROCESSED` / `WOULD PROCESS` | The package itself, deleted from the drop folder. |
| `ERROR` | A filesystem refusal, or a binder run that failed. |

Events appear in the order they happened, so a deletion and the write that
depended on it read as one story. The exit code is `0` unless an `ERROR`
occurred — note that a `CONFLICT` and a rejected package both exit `0`, because
nothing failed: the tool did exactly what it should with what it was given. The
completion summary is where you read the outcome.

### Three cases worth understanding

**`INVALID` — the package was rejected.** Validation is a gate, not a filter. A
package that is wrong in one place is not deployed in the places it happens to
be right, because deploying half of a badly-built package leaves the tree in a
state nobody designed. Fix the package and drop it in again.

**`CONFLICT` — something was in the way.** A file already sits where the
package wants to write and the package did not name it as replaced; a
`replaces` filename was found in several folders and the tool will not guess
which one you meant; or a `move` source doesn't exist or its destination is
already occupied. Nothing is overwritten, deleted, or moved. The run says
exactly which file and why.

**A partial deploy keeps its package.** If anything conflicted, the zip stays in
the drop folder rather than being deleted — you will need it when you sort the
conflict out, and a package that's gone reads as one that was fully applied.

---

## The folder naming check

Every run walks the tree and reports any folder whose name is *nearly* one of
the conventions — `_fileupdatepackagse` where `_fileupdatepackages` was meant,
`_bnder` where `_binder` was meant, and so on. It appears in the completion
summary and nowhere else.

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
summary included. By default the log lands at
`_aide/utilities/file-update-package/file_update_package.log`. The log is
never rewritten or trimmed.

---

## Scope

It places whole files. It does not merge, patch or edit content, it does not
decide what belongs in a package, and it does not do general version resolution
— it acts on the entries each manifest names. Tidying the rest of the tree is
`aide cleanup`'s job.
