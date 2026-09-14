# FileUpdatePackage Deployer — Design

> **Version 2** (2026-09-14). Updated to match the deployed tool. Major changes from version 1:
> actions are now `create`, `replace` and `move` (`update` remains accepted as a synonym for
> `replace`); replaced files and processed packages are deleted rather than moved to `_superseded`;
> the tool runs as part of the `aide` CLI rather than as a standalone script; and successful deploys
> are committed to git automatically.

**Script source:** `aide-cli/src/aide/utilities/fup.py` in the deploy repo, distributed via `aide update`
**Design documentation:** `Documentation/Infrastructure/file-update-package`
**Run via:** `aide fup` (or `aide fup --dry-run`)

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings and the package format.
- **Path logic** — absolute, root-anchored and base-relative forms.
- **Processing model** — find, validate, gate, deploy, commit, trigger, clean up.
- **Execution behaviour** — `aide fup`, dry run, the completion summary.
- **Folder naming check** — advisory, and why it is here.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Deploy a FileUpdatePackage — a zip of updated documents produced by a Chat or Cowork
session — into the master document tree, replacing what it supersedes, and leave the user in no
doubt about what happened.

**Boundary — hard.** It places and moves whole files. It does **not** merge, patch or edit content,
it does not decide what belongs in a package, and it does not do general version resolution — it
deletes the single document each replace entry names, and moves what each move entry names. It is
Infrastructure: it acts on the corpus and is never loaded into an AI session itself.

**It never overwrites.** A file already sitting where a package wants to write, and not named as
the one being replaced, is a `CONFLICT`: reported, skipped, left exactly as it was.

**Shape.** A utility in the `aide` CLI, sibling to version cleanup and the binder builder.

**Pipeline position.**

```text
(a session produces a package)
        ↓
aide fup  →  git commit  →  binder builder
```

The deployer commits affected files and triggers the binder builder itself, so a deploy leaves the
tree committed and the binder current. Version cleanup remains a separate pass over the tree.

---

## 2. Inputs

### 2.1 Settings

Settings come from the project's aide configuration, under the `fup` key. The tool uses the project
root — the directory containing `_aide/` — as the documentation root.

| Setting | Purpose |
|---|---|
| `drop_folder` | Where packages are put to be deployed. Default `~/_fileupdatepackages`. |
| `log_file` | Log file location. Default `~/_aide/file_update_package.log`. |
| `trigger_binder` | Whether to run the binder builder after a deploy. Default `true`. |

### 2.2 The package

A zip file carrying documents at their paths relative to the documentation root, plus a manifest at
the zip root:

```json
{
  "description": "Project Design master files — binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "replace",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    { "path": "Project Design/ProjectDesign_Index_v8.md", "action": "create" },
    {
      "action": "move",
      "old_path": "Standards/OldName_v3.md",
      "new_path": "Standards/NewName_v3.md"
    }
  ]
}
```

**Per-entry fields for `create` and `replace`** (each object in `files`):

| Field | Meaning |
|---|---|
| `path` | Where the file goes, relative to the documentation root, forward slashes. The zip must contain a member at this path. |
| `action` | `create` — the file is new. `replace` — it replaces an existing document. (`update` is accepted as a backward-compatible synonym for `replace`.) |
| `replaces` | *Replace only, optional.* The **filename** of the document being replaced. The tool finds it and deletes it. Omitted, a replace deletes the file at its own `path` — see D4. |

**Per-entry fields for `move`:**

| Field | Meaning |
|---|---|
| `action` | `move` — relocate an existing document within the tree. No zip member is needed. |
| `old_path` | The current location of the file, relative to the documentation root. Must exist. |
| `new_path` | The destination, relative to the documentation root. Must not exist. |

**Package-level fields:**

| Field | Meaning |
|---|---|
| `description` | Optional. Shown in the report header and the completion summary. |
| `user_instructions` | Optional. Shown to the user, who must acknowledge before the deploy proceeds. Omit the field when there are no instructions; an empty string is equivalent to omission. |
| `created` | Optional, informational. The tool orders packages by filesystem modification time, not by this field. |

---

## 3. Path logic

Settings paths accept three forms:

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_fileupdatepackages` | Exact folder. |
| **Root-anchored** | `~/_fileupdatepackages` | Measured from the documentation root (the project root). |
| **Base-relative** | `_fileupdatepackages` | Measured from the base directory passed to the resolver. |

`~` never means the home folder. Home expansion is not performed anywhere in these settings.

**Manifest paths are not settings paths.** They come from an untrusted zip and are checked
separately and harder — see §4.2.

---

## 4. Processing model

1. Resolve settings; use the project root as the documentation root.
2. Run the folder naming check over the tree (§6).
3. Find every `.zip` in the top level of the drop folder. None → `SKIPPED`.
4. Take the **newest by modification time**. Report the rest as `SKIPPED` — waiting, not processed.
5. Validate the package as a whole (§4.1). Any problem → `INVALID`, nothing is deployed.
6. If the manifest carries `user_instructions`: show them and wait for acknowledgement (§4.3).
7. For each manifest entry in order (§4.4): delete what it replaces, then write or move the file.
8. Delete the package — **only if the deploy was complete** (§4.6).
9. Commit affected files to git (§4.7).
10. Trigger the binder builder (§4.5), unless nothing was written or disabled.
11. Report and log.

### 4.1 Validation is a gate, not a filter

A package deploys as a whole or is rejected as a whole. Rejected for: not a zip; no `_manifest.json`;
a manifest that is not valid JSON or not an object; no `files` list; an entry with no usable path;
an `action` that is not `create`, `replace` or `move`; `replaces` on a create; `replaces` containing
a folder separator; the same destination listed twice; a move whose `old_path` or `new_path` is
invalid; and — the important one — **a create or replace entry naming a file the zip does not
contain**.

`update` is accepted as a backward-compatible synonym for `replace` and is silently mapped to it
during validation.

A package that is wrong in one place is not deployed in the places it happens to be right. Deploying
the good half of a badly-built package leaves the tree in a state nobody designed, and leaves the
session that built it believing its work landed.

### 4.2 Package paths are untrusted input

Every manifest path — `path`, `old_path` and `new_path` — is checked before it is used: no absolute
paths, no drive letters, no `..` segment, no trailing separator, not empty. The resolved destination
is then checked again to be inside the documentation root, which catches the case a purely textual
check cannot — a symbolic link in the tree carrying a well-formed relative path somewhere else
entirely.

Files are written from `zipfile.read()` into a validated destination rather than with
`ZipFile.extract()`, which derives the destination from the member name.

### 4.3 The user instructions gate

If the manifest carries `user_instructions`, they are printed in a banner and the tool waits for
Enter **before anything is written**. Stopping there — Ctrl+C — stops a deploy that has not started,
rather than one that is half done.

The wait is skipped, and the summary says so in those words, when there is no interactive console.
A run triggered by another tool must not block forever on a keypress nobody is there to press.

### 4.4 One entry, in order

**Replace entries:**

| Step | Behaviour |
|---|---|
| **Find what it replaces** | Beside the new file first — v7 and v8 of one document live in the same folder — then the rest of the tree. |
| **Found once** | Delete it. `DELETED`. |
| **Not found** | `SKIPPED`, naming it. The new file still deploys. |
| **Found more than once** | `CONFLICT`, naming every place. **Nothing is removed** — see D5. The new file still deploys. |
| **Destination taken** | `CONFLICT`. Nothing is written and nothing is overwritten, ever. |
| **Otherwise** | Write the file. `REPLACED`. |

A replace whose predecessor sits at the destination itself clears its own way: the deletion removes
it, and the never-overwrite check that follows is then a genuine test rather than a formality.
A dry run reports this correctly rather than reporting a conflict against a file it would itself
have removed.

**Create entries:**

The file is written to its destination. `CREATED`. If the destination is already occupied,
`CONFLICT` — nothing is written.

**Move entries:**

| Step | Behaviour |
|---|---|
| **Source does not exist** | `CONFLICT`. Nothing happens. |
| **Destination exists** | `CONFLICT`. Nothing happens. |
| **Otherwise** | Move the file. `MOVED`. Parent directories at the destination are created as needed. |

Both `old_path` and `new_path` are validated the same way as any other manifest path (§4.2).

### 4.5 The binder builder trigger

Run after any deploy that wrote or moved something, unless disabled by the `trigger_binder` setting.
The binder module is imported and called directly within the same process.

**Best-effort.** The deploy has already happened by the time this runs. A binder builder that fails
is reported as an `ERROR` on that step and the deploy stands.

### 4.6 Package disposal

A successful, complete deploy deletes the package from the drop folder. A run with any `CONFLICT`
or file-level `ERROR` leaves the package in the drop folder — whoever sorts the conflict out needs
the package still to hand.

### 4.7 Git commit

After a successful live deploy, the tool commits all affected files — every file that was written,
moved, deleted, or the package itself — to git. The commit message names the package and
summarises the counts (e.g. `fup: applied SomeName_FUP (2 replaced, 1 created)`).

Dry runs do not commit.

---

## 5. Execution behaviour

- Part of the `aide` CLI; invoked as `aide fup` or `aide fup --dry-run`.
- Python, standard library only (within the aide CLI framework).
- `--dry-run` reports what would be deployed and changes nothing.
- Appends one entry per run to the log, dry runs included and marked.

### Report vocabulary

`REPLACED` / `WOULD REPLACE` · `CREATED` / `WOULD CREATE` · `MOVED` / `WOULD MOVE` ·
`DELETED` / `WOULD DELETE` · `CONFLICT` · `SKIPPED` · `INVALID` · `BINDER` ·
`PROCESSED` / `WOULD PROCESS` · `ERROR`

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `SKIPPED` covers nothing-to-do
cases: no packages at all, a package waiting its turn, and a `replaces` that names nothing in the
tree. `INVALID` is §4.1 — the package was rejected and nothing in it was deployed.

**Events are reported in the order they happened**, not sorted. A deploy is a sequence: a deletion
and the write that depended on it read as one story. The folder heading still changes as the run
moves through the tree.

### The completion summary

The primary output, not an afterthought. Every run ends with it, whatever happened:

```text
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              good.zip
                        Project Design master files - binder sweep complete
  files replaced:       1
  files created:        1
  files moved:          0
  files deleted:        1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered
  the package is now:   deleted
  folder naming:        no misspelled folders found
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

Every conflict and every error is listed individually with its filename and reason. The final line
is one of:

| Status | When |
|---|---|
| `COMPLETED SUCCESSFULLY` | No conflicts, no errors. Also the "nothing to do" case, and a clean dry run. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice, the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed and some did not. |
| `FAILED - nothing was deployed` | An `INVALID` package, or every entry conflicted. |

**Exit code `0` unless an `ERROR` occurred.** Note the consequence, stated so it is not later read
as a defect: a `CONFLICT` and an `INVALID` package both exit `0`, because nothing failed — the tool
did exactly what it should with what it was given. See D9.

---

## 6. Folder naming check

Every run, before anything else, walks the documentation root and reports any folder whose name is a
near-miss of a convention name — `_fileupdatepackages`, `_binder`, `_aide`, `_rebuild` — using a
similarity threshold rather than a fixed list of misspellings.

**Only underscore folders are candidates.** Every convention name is one, and the restriction is
what keeps the check honest: `Infrastructure/file-update-package`, the documentation folder of this very
tool, scores above the threshold against `_fileupdatepackages` on similarity alone and is plainly
not a misspelling of it. A summary that cries wolf stops being read.

**It is advisory.** It never renames anything, never blocks a deploy, and never changes the exit
code. It speaks in the completion summary and nowhere else.

---

## 7. Definition of done

Drop a well-formed package into the drop folder and run the tool. Each `replace` deletes the
document it names and writes the new one in its place; each `create` lands where it should; each
`move` relocates the file; nothing anywhere is overwritten. Instructions in the package are shown
and acknowledged before any file is touched. Affected files are committed to git. The binder builder
runs afterwards. The package is deleted. The completion summary states, without the user having to
interpret anything, how many files were replaced, created, moved and deleted, every conflict and
error with its filename and reason, and a final status line.

A dry run reports all of that and changes nothing.

An empty drop folder reports `SKIPPED`. A package that is not a zip, has no manifest, has an
unparseable manifest, or names a file it does not contain, is rejected whole — `INVALID`, nothing
deployed, the package left where it is. A path containing `..` never writes outside the
documentation root. A partial deploy names what landed and what did not, and keeps its package. A
misspelled convention folder anywhere in the tree is named in the summary.

---

## 8. Decisions

**D1 — Part of the aide CLI, not a standalone script.** The tool runs as `aide fup`, sharing the
project root and settings with the rest of the `aide` framework. This replaces the standalone
settings file and instance-folder model of version 1.

**D2 — `replace` and `move` actions, with `update` backward compat.** The action vocabulary is
`create`, `replace` and `move`. `update` is accepted and silently mapped to `replace` so that
packages built against the earlier schema are not rejected.

**D3 — Newest package only; the rest wait.** Batching would mean deciding what to do when the third
of five packages conflicts, and the honest answer is "a person looks at the report". One package per
run keeps the completion summary about one deploy. Waiting packages are reported by name, so nothing
is silently held back.

Ordering is by filesystem modification time rather than by the manifest's `created` field: the field
is written by whatever produced the package and cannot be relied on, and the file's own timestamp is
the fact the drop folder actually carries.

**D4 — `replaces` is optional on a replace.** Where it is absent, the entry replaces the file at
its own `path`. This is the natural reading of "replace" for a document whose filename does not
carry a version, and it never overwrites: the existing file is deleted before the new one is
written.

**D5 — An ambiguous `replaces` removes nothing.** A filename found in three folders is a question
this tool must not answer by guessing. All three are named in a `CONFLICT`, none is removed, and the
new file still deploys — so the outcome is visible in the tree as well as in the report.

**D6 — Replaced files and processed packages are deleted, not moved to `_superseded`.** The tree is
under version control. Git history is the authoritative record of what was replaced and when. Moving
replaced files to `_superseded` duplicates that record in the filesystem and requires cleanup.
Deletion is simpler, cleaner, and relies on git for recovery.

**D7 — Automatic git commit after deploy.** A deploy that changes the tree should commit those
changes immediately. This keeps the working tree clean, ties each deploy to a single commit with a
descriptive message, and means the binder builder (which runs afterwards) sees a committed state.

**D8 — The binder builder trigger is best-effort and controllable.** Best-effort because the deploy
has already happened: a binder that could not be rebuilt is a stale binder, not a lost document. It
is reported as an `ERROR` and the deploy stands. Controllable via the `trigger_binder` setting so
that deployments in contexts where the binder is not needed can skip it.

**D9 — `CONFLICT` and `INVALID` exit `0`.** The exit code reports whether the tool failed rather
than whether the outcome was the desired one. The completion summary is the human channel and it says
`FAILED` in plain words. Recorded here because the two channels disagreeing looks like a defect if
it is not written down as a choice.

---

## 9. Open

- **Package provenance.** The manifest's `created` field is carried but not used, and there is no
  record in the deployed tree of which package a document arrived in beyond the git commit. The
  commit message names the package. Whether that is enough is a question for the first time someone
  asks "where did this file come from".
