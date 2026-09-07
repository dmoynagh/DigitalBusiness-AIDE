# FileUpdatePackage Deployer — Design

> **Version 1** (2026-09-07). First issue. Third tool in the Infrastructure family, after version
> cleanup and the binder builder, and the one that closes the loop: it takes the output of a Chat or
> Cowork session and puts it into the master tree.

**Master/source folder:** `Documentation/Infrastructure/file-update-package`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — the settings file, and the package format.
- **Path logic** — absolute, root-anchored and script-relative forms.
- **Processing model** — find, validate, gate, deploy, trigger, file away.
- **Execution behaviour** — live by default, dry run, double-click, the completion summary.
- **Folder naming check** — advisory, and why it is here.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Deploy a FileUpdatePackage — a zip of updated documents produced by a Chat or Cowork
session — into the master document tree, superseding what it replaces, and leave the user in no
doubt about what happened.

**Boundary — hard.** It places whole files. It does **not** merge, patch or edit content, it does
not decide what belongs in a package, and it does not do general version resolution — it moves the
single document each manifest entry names, and nothing else. It is Infrastructure: it acts on the
corpus and is never loaded into an AI session itself.

**It never overwrites.** A file already sitting where a package wants to write, and not named as
the one being replaced, is a `CONFLICT`: reported, skipped, left exactly as it was.

**Shape.** A single-action tool, sibling to version cleanup and the binder builder. No actions
framework, no shared base class, no plugin system.

**Pipeline position.**

```text
(a session produces a package)
        ↓
file update package  →  binder builder
```

The deployer triggers the binder builder itself, so a deploy leaves the binder current. Version
cleanup remains a separate, human-run pass over the tree: the deployer supersedes only what a
manifest names.

---

## 2. Inputs

### 2.1 The settings file

JSON, read on launch, from the script's own folder.

| Setting | Purpose |
|---|---|
| `documentation_root` | The root of the tree packages deploy into. Manifest paths are measured from here, and it is the anchor for `~/` in the other settings. |
| `drop_folder` | Where packages are put to be deployed. Default `~/_fileupdatepackages`. |
| `binder_builder` | The binder builder script to run after a deploy. Point it at the **running instance**, not the master, so it uses that instance's settings. Empty string skips the trigger. |
| `log_file` | Log file location. Named to match both siblings. |

The script writes a commented default settings file if none is present, rather than failing.

### 2.2 The package

A zip file carrying documents at their paths relative to the documentation root, plus a manifest at
the zip root:

```json
{
  "created": "2026-09-07T10:00:00Z",
  "description": "Project Design master files — binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "update",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    { "path": "Project Design/ProjectDesign_Index_v8.md", "action": "create" }
  ],
  "user_instructions": "Review the new Overview document before publishing."
}
```

| Field | Meaning |
|---|---|
| `path` | Where the file goes, relative to the documentation root, forward slashes. |
| `action` | `create` — the file is new. `update` — it replaces an existing document. |
| `replaces` | *Update only, optional.* The **filename** of the document being superseded. The tool finds it and moves it to `_superseded`. Omitted, an update supersedes the file at its own `path` — see D4. |
| `description` | Optional. Shown in the report header and the completion summary. |
| `user_instructions` | Optional. Shown to the user, who must acknowledge before the deploy proceeds. |
| `created` | Optional, informational. The tool orders packages by filesystem modification time, not by this field. |

**`Documentation/_config/repo_config.json`** maps topic names to folder paths for whoever is
*building* a package. The tools do not read it; they have their own settings.

---

## 3. Path logic

The same three forms as the sibling tools, ratified as the Infrastructure-wide convention
(version-cleanup/claude-code/001, 2026-09-04):

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_fileupdatepackages` | Exact folder. |
| **Root-anchored** | `~/_fileupdatepackages` | Measured from `documentation_root`. |
| **Script-relative** | `..` | Measured from the folder holding the script. |

`documentation_root` itself cannot use `~/`, because it is what `~/` means — the same rule and the
same error message as `root` in both siblings. See D2.

**The folder-relative *pattern* form does not appear here.** In the siblings it exists for `include`
and `exclude`, which describe *classes* of folder across a tree. This tool has no such setting:
every path names one place. Nothing is missing — there is nowhere for a pattern to apply.

`~` never means the home folder. Home expansion is not performed anywhere in these settings.

**Manifest paths are not settings paths.** They come from an untrusted zip and are checked
separately and harder — see §4.2.

---

## 4. Processing model

1. Resolve settings; resolve `documentation_root`.
2. Run the folder naming check over the tree (§6).
3. Find every `.zip` in the top level of the drop folder. None → `SKIPPED`, exit `0`.
4. Take the **newest by modification time**. Report the rest as `SKIPPED` — waiting, not processed.
5. Validate the package as a whole (§4.1). Any problem → `INVALID`, nothing is deployed.
6. If the manifest carries `user_instructions`: show them and wait for acknowledgement (§4.3).
7. For each manifest entry in order (§4.4): supersede what it replaces, then write the new file.
8. Trigger the binder builder (§4.5), unless nothing was written.
9. Move the package into `_superseded` inside the drop folder — **only if the deploy was complete**.
10. Report, log, print the completion summary, hold the window open.

### 4.1 Validation is a gate, not a filter

A package deploys as a whole or is rejected as a whole. Rejected for: not a zip; no `_manifest.json`;
a manifest that is not valid JSON or not an object; no `files` list; an entry with no usable `path`;
an `action` that is not `create` or `update`; `replaces` on a create; `replaces` containing a folder
separator; the same destination listed twice; and — the important one — **a manifest naming a file
the zip does not contain**.

A package that is wrong in one place is not deployed in the places it happens to be right. Deploying
the good half of a badly-built package leaves the tree in a state nobody designed, and leaves the
session that built it believing its work landed.

### 4.2 Package paths are untrusted input

Every manifest `path` is checked before it is used: no absolute paths, no drive letters, no `..`
segment, no trailing separator, not empty. The resolved destination is then checked again to be
inside the documentation root, which catches the case a purely textual check cannot — a symbolic
link in the tree carrying a well-formed relative path somewhere else entirely.

Files are written from `zipfile.read()` into a validated destination rather than with
`ZipFile.extract()`, which derives the destination from the member name.

### 4.3 The user instructions gate

If the manifest carries `user_instructions`, they are printed in a banner and the tool waits for
Enter **before anything is written**. Stopping there — Ctrl+C — stops a deploy that has not started,
rather than one that is half done.

The wait is skipped, and the summary says so in those words, when there is no interactive console.
A run triggered by another tool must not block forever on a keypress nobody is there to press. This
is the same reasoning as the exit pause in both siblings.

### 4.4 One entry, in order

| Step | Behaviour |
|---|---|
| **Find what it replaces** | Beside the new file first — v7 and v8 of one document live in the same folder — then the rest of the tree, skipping `_superseded` folders throughout. |
| **Found once** | Move it into `_superseded` beside itself. `SUPERSEDED`. |
| **Not found** | `SKIPPED`, naming it. The new file still deploys. |
| **Found more than once** | `CONFLICT`, naming every place. **Nothing is moved** — see D5. The new file still deploys. |
| **Destination taken** | `CONFLICT`. Nothing is written and nothing is overwritten, ever. |
| **Otherwise** | Write the file. `DEPLOYED` for an update, `CREATED` for a create. |

An update whose predecessor sits at the destination itself clears its own way: the supersession
moves it, and the never-overwrite check that follows is then a genuine test rather than a formality.
A dry run reports this correctly rather than reporting a conflict against a file it would itself
have moved.

### 4.5 The binder builder trigger

Run unconditionally after any deploy that wrote something, with no arguments, in live mode. The
binder builder's own change detection (BinderBuilder_Design_v4 §4a) decides whether a rebuild is
actually needed, so this tool does not have to know or care.

`stdin` is closed rather than inherited, which is what stops the binder builder pausing for a
keypress at the end of its own run. Its `Result:` line is carried up into this report; its full
report is in its own log.

**Best-effort.** The deploy has already happened by the time this runs. A binder builder that is
missing, that will not start, that exits non-zero or that runs past its timeout is reported as an
`ERROR` on that step and the deploy stands — including the package being filed away, because the
files did land.

### 4.6 Partial deploys keep their package

A run with any `CONFLICT` or file-level `ERROR` leaves the package in the drop folder. Whoever sorts
the conflict out needs the package still to hand, and a package sitting under `_superseded` reads as
one that was fully applied. The report says which files landed and which did not.

---

## 5. Execution behaviour

Matches both siblings, so the three tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be deployed and changes nothing.
- Reads settings on launch — no arguments required, so **double-click works on Windows**.
- Appends one entry per run to the log, dry runs included and marked.
- Cross-platform; Windows primary.

### Report vocabulary

`DEPLOYED` / `WOULD DEPLOY` · `CREATED` / `WOULD CREATE` · `SUPERSEDED` / `WOULD SUPERSEDE` ·
`CONFLICT` · `SKIPPED` · `INVALID` · `BINDER` · `PROCESSED` / `WOULD PROCESS` · `ERROR`

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `SKIPPED` covers both nothing-to-do
cases: no packages at all, a package waiting its turn, and a `replaces` that names nothing in the
tree. `INVALID` is §4.1 — the package was rejected and nothing in it was deployed.

**Events are reported in the order they happened**, not sorted, unlike both siblings. A deploy is a
sequence: a supersession and the write that depended on it read as one story. The folder heading
still changes as the run moves through the tree.

### The completion summary

The primary output, not an afterthought. Every run ends with it, whatever happened, and the window
stays open until it has been read:

```text
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              good.zip
                        Project Design master files - binder sweep complete
  files updated:        1
  files created:        1
  files superseded:     1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered - 24 included, 1 written, 1 superseded
  the package is now:   moved to _superseded/
  folder naming:        1 folder(s) close to a convention name but not matching it
    - _superceded  (expected "_superseded")
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

**Exit code `0` unless an `ERROR` occurred**, matching both siblings. Note the consequence, stated
so it is not later read as a defect: a `CONFLICT` and an `INVALID` package both exit `0`, because
nothing failed — the tool did exactly what it should with what it was given. See §8.

---

## 6. Folder naming check

Every run, before anything else, walks the documentation root and reports any folder whose name is a
near-miss of a convention name — `_superseded`, `_fileupdatepackages`, `_binder`, `_tools`,
`_config`, `_rebuild` — using a similarity threshold rather than a fixed list of misspellings.

**Only underscore folders are candidates.** Every convention name is one, and the restriction is
what keeps the check honest: `Infrastructure/file-update-package`, the master folder of this very
tool, scores above the threshold against `_fileupdatepackages` on similarity alone and is plainly
not a misspelling of it. A summary that cries wolf stops being read.

**It is advisory.** It never renames anything, never blocks a deploy, and never changes the exit
code. It speaks in the completion summary and nowhere else.

It is here because a misspelled underscore folder is invisible to every tool in this family: they
all skip underscore folders, so `_superceded` does no damage and produces no complaint — it just
quietly splits a convention in two, and stays split until something says so. The known instance is
`Documentation/_superceded`, recorded in BinderBuilder_Design_v3 §10 and deliberately left alone;
reconciling it is a human act. Naming it on every run is how it stops being forgotten. See D7.

---

## 7. Definition of done

Drop a well-formed package into the drop folder and run the tool. Each `update` supersedes the
document it names and lands in its place; each `create` lands where it should; nothing anywhere is
overwritten. Instructions in the package are shown and acknowledged before any file is touched. The
binder builder runs afterwards and its outcome is reported. The package is moved to `_superseded`.
The completion summary states, without the user having to interpret anything, how many files were
updated, created and superseded, every conflict and error with its filename and reason, whether the
binder was rebuilt, and a final status line — and the window stays open until it is read.

A dry run reports all of that and changes nothing.

An empty drop folder reports `SKIPPED` and exits `0`. A package that is not a zip, has no manifest,
has an unparseable manifest, or names a file it does not contain, is rejected whole — `INVALID`,
nothing deployed, the package left where it is. A path containing `..` never writes outside the
documentation root. A partial deploy names what landed and what did not, and keeps its package. A
misspelled convention folder anywhere in the tree is named in the summary.

---

## 8. Decisions

**D1 — A third tool, not a mode of an existing one.** Deploying is a different job from tidying
versions and from assembling a binder, and it is the only one of the three that takes an external
input. The three run in sequence and share nothing but conventions.

*Consequence, accepted:* the path logic now exists in three implementations. The trigger for
extracting shared code was stated in BinderBuilder_Design_v3 §10 as "a third tool needing it" — and
this is that third tool. It is still not extracted: this tool needs only the one-place resolver,
about forty lines of pure functions over paths with no state, and not the pattern matching that
makes up the bulk of the siblings' path code. A shared module carrying two thirds dead weight for
each importer is worse than the copy. **Re-examine when a fourth tool arrives, or when any tool needs
the pattern form changed.**

**D2 — `documentation_root` cannot use `~/`.** The tool-pipeline brief proposed
`"documentation_root": "~/"`. Rejected as circular: `~/` means "measured from the documentation
root", so it cannot appear in the setting that defines that root. Both siblings reject `~/` in
`root` for exactly this reason and say so in an error message. The shipped default is `".."`, which
is what an instance sitting in `_tools` wants, and the setting comment says why.

**D3 — Newest package only; the rest wait.** Batching would mean deciding what to do when the third
of five packages conflicts, and the honest answer is "a person looks at the report". One package per
run keeps the completion summary about one deploy. Waiting packages are reported by name, so nothing
is silently held back.

Ordering is by filesystem modification time rather than by the manifest's `created` field: the field
is written by whatever produced the package and cannot be relied on, and the file's own timestamp is
the fact the drop folder actually carries.

**D4 — `replaces` is optional on an update.** Where it is absent, the entry supersedes the file at
its own `path`. This is the natural reading of "update" for a document whose filename does not carry
a version, and it never overwrites: the existing file is moved to `_superseded` exactly as a named
one would be.

*Considered and rejected:* treating a missing `replaces` as `INVALID`. Rejected because the
resulting behaviour would be worse — a package that plainly means "here is the new version of this
file" would be refused for a field that adds nothing in that case.

**D5 — An ambiguous `replaces` moves nothing.** A filename found in three folders is a question this
tool must not answer by guessing. All three are named in a `CONFLICT`, none is moved, and the new
file still deploys — so the outcome is visible in the tree as well as in the report, and version
cleanup will surface it again on its next pass.

This is version cleanup's `AMBIGUOUS` shape, reported here as `CONFLICT` because the vocabulary for
this tool was fixed at seven words and a near-duplicate would have to earn its place.

**D6 — The binder builder trigger is best-effort, and it is unconditional.** Unconditional because
the binder builder now decides for itself whether a rebuild is needed (v4 §4a); a deployer that
tried to predict that would duplicate the judgement and eventually disagree with it. Best-effort
because the deploy has already happened: a binder that could not be rebuilt is a stale binder, not a
lost document. It is reported as an `ERROR` and the run exits `1`, but the deploy stands and the
package is still filed away.

**D7 — The folder naming check is advisory and lives here.** It could sit in any of the three tools.
It is here because this is the tool that writes *into* the tree at paths a session composed, which
is exactly where a split convention would first do harm — a package built against `_superceded`
would file documents somewhere no tool looks.

It never renames. Renaming a folder is a decision with consequences the tool cannot see, and the
misspelling it will find most often is a known one that has already been left deliberately.

**D8 — `CONFLICT` and `INVALID` exit `0`.** Consistent with both siblings, where the exit code
reports whether the tool failed rather than whether the outcome was the desired one. The completion
summary is the human channel and it says `FAILED` in plain words. Recorded here because the two
channels disagreeing looks like a defect if it is not written down as a choice. See §9.

---

## 9. Open

- **Exit codes for expected-but-unwanted outcomes.** `EMPTY` in the binder builder, and `CONFLICT`
  and `INVALID` here, all exit `0`. A future orchestrator chaining these tools would want to
  distinguish "did nothing" from "did what was asked". Prefer distinct codes over overloading the
  failure code. **Not now** — the only chaining that exists is this tool calling the binder builder,
  and it reads the report rather than the exit code.
- **Package provenance.** The manifest's `created` field is carried but not used, and there is no
  record in the deployed tree of which package a document arrived in. The log has it. Whether that
  is enough is a question for the first time someone asks "where did this file come from".
- **Path-logic duplication.** Three implementations now. See D1 for the trigger to revisit.
- **The `_superceded` misspelling** at the Documentation root remains, and is now reported on every
  deploy rather than only in a design document. Still a human act to reconcile.
