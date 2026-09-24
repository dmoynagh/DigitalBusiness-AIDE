> identity: VersionCleanup_Design@v5 | doctype: design | updated: 2026-09-24

# Version Cleanup — Design

> **Version 5** (2026-09-24). A live run commits **only the files it deleted**, named by explicit
> path; anything else already staged is left staged and out of the commit. `aide cleanup --help`
> (or `-h`) prints usage and does nothing else. Both come from fixes to the shared `aide` CLI made
> for the binder builder (BinderBuilder_Design D22). See D4.
>
> **Version 4** (2026-09-24). Rewritten to match the deployed tool. The utility is now `aide
> cleanup`, one of the utilities built into the `aide` CLI (`aide-cli`, in the deploy repo),
> rather than a standalone script with its own settings file and log. It is **dry run by
> default**; `--apply` deletes. Superseded versions are **deleted outright**, not moved to
> `_superseded` — git history is the archive, and a live run commits the deletions itself. See
> Decisions D1–D3. No change to the matching rule, the folder scope model, or the path forms.
>
> v3 (2026-09-04) corrected the master folder path after the rename to `version-cleanup`. v2
> added objective, contents, definition of done and sibling relationships; recorded the
> three-form path model's ratification as an Infrastructure-wide convention; reframed
> verification as required cases rather than a build record. No behaviour change from v1.

## Contents

- **Position and objective** — what this is, what it must achieve, its boundary.
- **The matching rule** — document identity, version comparison, deliberate limits.
- **Folder scope** — descend versus process, and the three path forms.
- **Deletion behaviour** — what is removed, what is never touched, and the commit that follows.
- **Execution model** — a CLI utility, not a standalone script.
- **Inputs** — the settings key, defaults, the log.
- **Run modes and report vocabulary.**
- **Definition of done, idempotence, boundary, required verification cases.**
- **Decisions** — with reasons.

## Position

Version cleanup is a utility built into the `aide` CLI: machinery that acts on the document tree
but is never loaded into an AI session. It has no authority over document content and states no
methodology; it enforces one physical property of the tree.

It is a **single-action utility**, not a framework. Sibling utilities (`aide binder`, `aide fup`)
are separate modules in the same CLI. There is deliberately no action registry, plugin system or
shared base class beyond the CLI's own discovery of `name` / `description` / `run`. Any
commonality between siblings is resolved when the duplication is visible, not in anticipation of
it.

### Relationship to siblings

Version cleanup runs **first** in the corpus pipeline, so tools downstream can take what they find
without version reasoning:

```text
aide cleanup  →  aide binder  →  aide fup (deploys, then re-triggers aide binder itself)
```

Binder builder supersedes its own previous output within its own folder, so version cleanup never
needs pointing at `_binder`. The governing principle: **a tool cleans up after itself; version
cleanup handles supersession it did not cause.**

## Objective

Keep the live document tree holding exactly one version of each document, so anything reading the
tree — a person, a sibling tool, or an AI loading context — finds the current document without
having to reason about which one it is.

```text
document tree containing many versions per document
  → walk each folder
  → group that folder's files by document identity
  → keep the highest version in place
  → delete every lower version
  → report + commit (live run only) + append log entry
```

## The matching rule

Two files are the same document at different versions when their filenames are identical except
for a `_v<number>` suffix immediately before the extension, and their extensions match.

```text
identity  =  (filename with any trailing _v<number> removed, extension)
version   =  the digits in that suffix, or 0 when there is no suffix
```

| Case | Behaviour |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` deleted |
| `Foo.md`, `Foo_v1.md` | `Foo.md` deleted — absent suffix is v0 |
| `Foo_v3.md` alone | stays, suffix or not |
| `Foo_v1.md`, `Foo_v2.txt` | different documents — extension is part of identity |
| `Foo_v2_draft.md` | no match — the suffix must be terminal |

Treating an unsuffixed file as v0 removes the special case: `Foo.md` versus `Foo_v1.md` is decided
by the same comparison as `Foo_v8.md` versus `Foo_v9.md`.

Highest number stays; all lower versions are deleted. Version numbers are compared numerically, so
`_v10` outranks `_v9`.

### Deliberate limits

- **Case.** `_v` and `_V` are both recognised. The document identity itself is compared with exact
  case, so `Foo_v1.md` and `foo_v2.md` are two documents and neither is touched. Conservative by
  intent.
- **Ties.** Two files can share a version number only through leading zeros (`Foo_v08.md`,
  `Foo_v8.md`). Which is current is then genuinely unclear, so the tool reports `AMBIGUOUS` and
  deletes nothing in that group.
- **Compound extensions.** Only the final extension is treated as the extension, so
  `Foo_v8.tar.gz` has identity `Foo_v8.tar` and never matches. Not a concern for a document corpus.

**The general shape:** where a rule does not determine an answer, report it and delete nothing.
This applies to every case in this class, not only ties.

## Folder scope

Grouping is **per folder**. The walk is recursive and visits every folder, but each folder is
compared only against itself. Cross-folder version relationships are handled manually and are out
of scope.

Two distinct questions are asked of every folder:

| Question | Rule |
| --- | --- |
| **Descend** into it? | Not excluded, and either its name does not start with `_`, or it is on the include list, or it is an ancestor of something on the include list. |
| **Process** its own files? | Not excluded, and either its name does not start with `_`, or it is on the include list. |

The distinction matters: an underscore-prefixed folder that merely sits on the path to an included
folder is walked through without its own files being touched.

- The underscore rule is what keeps the tool out of folders such as `_binder` and `_aide` by
  default. It is the mechanism, not a convention layered on top of one.
- The **root** is an explicit choice in the settings, so the underscore rule does not apply to it.
  An explicit exclude still does.
- Exclude wins over include. Pruning at an excluded folder is what makes exclusion inherited:
  once a branch is skipped, nothing inside it is ever asked about again.
- Directory symlinks are not followed, so a link cannot cause one tree to be tidied twice.

### Path forms for include and exclude

The tree needs two different kinds of statement: *this exact folder*, and *any folder shaped
like this*. Three spellings carry them.

| Form | Example | Resolution |
| --- | --- | --- |
| Absolute | `C:/Docs/_binder` | one exact folder |
| Root-anchored | `~/_binder` | one exact folder, measured from `root` |
| Relative | `_binder` | a **pattern**, tested against every folder the walk reaches |

**Status: ratified as the Infrastructure-wide convention.** This is not a local choice of this
tool. Binder builder and the file update package use the same vocabulary; a divergent path model
in a sibling is a defect.

A relative entry is not resolved once at startup. It is a shape, matched when a folder's path
**ends with** the entry's segments, so `_binder` covers a `_binder` subfolder at any depth and
`_binder/current` matches any `.../_binder/current`. The comparison is made against the path
measured from the root, so a pattern can never reach above the root, and the root itself is never
matched by one.

Consequences taken deliberately:

- `~` means the **root of the tree**, never the home folder. `expanduser` is never called on
  these settings, so `~/` cannot quietly resolve to a user profile directory. This is a one-way
  door on that character across Infrastructure.
- The `root` setting itself cannot use `~/`, since it is what defines the root. It takes an
  absolute path or one relative to the project root, and rejects `~/` with that explanation.
- `..` is rejected inside a relative entry. A pattern has no anchor for it, so silently accepting
  one would produce an entry that never matches.
- Path comparison goes through `os.path.normcase`: case-insensitive on Windows, case-sensitive
  elsewhere. Matching therefore follows the local filesystem rather than diverging from it.
- The multi-segment form needs lookahead. A folder matching a *proper prefix* of an include
  pattern is descended into but not processed, which is how `_binder/current` reaches `current`
  through an underscore-prefixed parent.
- A relative `exclude` entry is correspondingly broad: `_binder` would skip every such folder in
  the tree. That is the intent.

## Deletion behaviour

Superseded files are **deleted outright**. There is no `_superseded` folder for this tool: the
tree is under version control, and git history is the record of what a deleted version contained.

There is nothing for a superseded file to conflict with — deletion has no destination, so the
`CONFLICT` outcome the old archive model needed does not apply. The only failure mode is a
filesystem refusal (locked file, permissions), reported as `ERROR`, with the file left in place.

**Live runs commit their own deletions.** When `--apply` deletes at least one file, the tool
stages and commits the deletions itself, with a message such as `cleanup: deleted 2 superseded
version(s)`. The commit holds only those deletions, named by explicit path; anything else already
staged is left staged and out of the commit (D4). Dry runs never commit.

See Decision D3.

## Execution model

The utility is a module in the `aide` CLI (`aide-cli/src/aide/utilities/cleanup.py`, in the
deploy repo `DigitalBusiness-AIDE-Deploy`), distributed via `aide update` and invoked as `aide
cleanup`. This folder holds the design documentation; there is no standalone script here to run.

The CLI locates the **project root** by walking up from the current folder until it finds `_aide/`
— the working directory itself is never trusted, since it varies with how the command was
launched. Settings, the default root, and the default log path are all resolved against the
project root, never against the script's own location: there is no "script folder" any more, and
no per-instance settings file.

Utility changes are made in the deploy repo via Code and distributed via `aide update`.

## Inputs

Settings come from the project's own configuration, `_aide/settings.json`, under the `cleanup`
key. Anything left out falls back to the package default shipped with `aide-cli`:

```json
{
  "cleanup": {
    "include": [],
    "exclude": [],
    "log_file": "~/_aide/utilities/version-cleanup/version_cleanup.log"
  }
}
```

| Setting | Meaning |
| --- | --- |
| `root` | The folder to tidy, including everything beneath it. Defaults to the project root (where `_aide/` lives). |
| `include` | Underscore-prefixed folders to process anyway — see path forms above. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `log_file` | Where the run log is appended. Default `~/_aide/utilities/version-cleanup/version_cleanup.log`. |

`root` and `log_file` resolve against the project root when written with `~/`, or relative to the
project root otherwise. A missing settings file is not an error — the package defaults apply.

### The log

Append-only, one entry per run, never rewritten or trimmed. Dry runs are logged too, clearly
marked, so the log is a complete record of every time the tool was pointed at the tree. The
on-screen report and the log entry are produced by one function and cannot drift apart.

## Run modes

| Mode | Behaviour |
| --- | --- |
| default | **Dry run.** Reports what would be deleted; nothing changes. |
| `--apply` | Live. Deletes the files and commits the deletion. |
| `-h` / `--help` | Prints usage. Nothing is scanned, deleted or committed. |

This is the reverse of v1–v3's default. See Decision D2.

Planning and acting are separate stages: `plan_folder` decides, `apply_deletions` acts. A dry run
executes the same decision code as a live run, which is what makes it a trustworthy preview rather
than a parallel implementation.

## Report vocabulary

| Kind | Meaning |
| --- | --- |
| `DELETED` | File deleted. |
| `WOULD DELETE` | Dry run — the same file, untouched. |
| `AMBIGUOUS` | Duplicate version numbers in one group; nothing in the group deleted. |
| `ERROR` | Filesystem refusal — locked file, permissions, unreadable folder. |

Events are grouped by folder in the report. A single failure does not abandon the run: the tool
reports it and continues, so the tree is never left half-tidied by an unrelated locked file.

Exit code is `0` unless at least one `ERROR` occurred. Ambiguity is an expected outcome requiring
human attention, not a failure of the run.

## Definition of done

Point the tool at a project and, on `--apply`, the tree afterwards holds one version of each
document, with lower versions deleted, the deletion committed to git, a readable on-screen report,
and one appended log entry. The default dry run produces the identical report and changes nothing.
Ambiguity is reported rather than resolved.

## Idempotence

Running the tool twice over the same tree produces no further deletion. Every remaining folder
holds one version per document after the first `--apply`, so no group has a member below the
highest version on the second pass.

## Out of scope — hard boundary

Version cleanup tidies versions. It does not assemble binders, does not deploy, does not edit
document content, and does not rename files. Superseded material is deleted outright — there is no
`_superseded` folder for this tool, and git history is the record of what was removed.

## Required verification cases

The cases the tool must handle. This is the regression set for any future change, not a record of
one build.

- **Matching** — multi-version groups including `_v10` versus `_v9`; unsuffixed v0; lone versioned
  files; extension mismatch; leading-zero ambiguity.
- **Scope** — nested folders; default underscore skip; all three include forms (a relative pattern
  catching several `_binder` folders at different depths, root-anchored catching only the top one,
  absolute catching one exact folder); a multi-segment pattern traversing an underscore parent
  without processing it; relative and root-anchored excludes.
- **Modes** — default run reports `WOULD DELETE` and changes nothing; `--apply` deletes and
  commits; a dry run and the live run it previews report identically apart from the verb;
  `--help` does nothing but print usage.
- **Commit isolation** — with an unrelated file staged, `--apply` commits only the deletions and
  the unrelated file is still staged afterwards.
- **Refusals** — malformed JSON; missing root; `..` in a relative entry; bare `~`; `~name`; `~/`
  in the root setting.
- **Repeatability** — a second `--apply` run over a tidied tree deleting nothing.

## Decisions

**D1 — A utility in the `aide` CLI, not a standalone script.** The tool runs as `aide cleanup`,
sharing the project root and settings with the rest of the `aide` framework — the same move made
for the file update package (FileUpdatePackage_Design D1). This replaces the standalone settings
file, standalone log, and script-folder resolution model of v1–v3.

**D2 — Dry run by default; `--apply` to act.** v1–v3 ran live by default with `--dry-run` as the
opt-in preview. That is reversed here: a bare `aide cleanup` only reports. Version cleanup acts
across the whole scope in one command with no per-item review — unlike the file update package,
which processes one already-built, already-inspected package at a time — so the safer default is
to look before deleting. `--apply` is the deliberate act.

**D3 — Deletion replaces archiving; no `_superseded` folder.** The tree is under version control.
Git history is the authoritative record of what was deleted and when. Moving superseded versions
to `_superseded` duplicated that record in the filesystem and required manual cleanup that never
happened in practice. Deletion is simpler, relies on git for recovery, and a live run commits the
deletion itself so the record is made at the moment it is true.

This supersedes the archive behaviour described in v1–v3 of this design (the "Archive behaviour"
section, since replaced by "Deletion behaviour" above). It matches the same move already made for
the file update package (FileUpdatePackage_Design D6) and the git-as-history convention already
recorded for Core Structure (Working Practices' Decisions and Design: "git-as-history decision,
superseded-folder pattern dropped, git is the version history" — WP_Decisions_v5, WP_Design_v7;
operationalised in WP_FileOps_Working_v1's "Archived file handling" note).

**D4 — A live run commits only its own deletions; help does nothing.** The `aide` CLI's shared
commit step used to commit the whole index, so a cleanup could sweep in whatever else was staged.
It now commits exactly the deleted paths, by explicit path, and leaves anything else staged
untouched. `-h` / `--help` is caught at the CLI entry point and prints usage before the utility
runs. Made for the binder builder (BinderBuilder_Design D22); cleanup shares the code, so it gets
the same fix.
