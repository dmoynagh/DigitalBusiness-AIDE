# Version Cleanup — Design

> **Version 2** (2026-09-04). Adds objective, contents, definition of done and sibling
> relationships; records the three-form path model's ratification as an Infrastructure-wide
> convention; reframes verification as required cases rather than a build record. No behaviour
> change from v1.

## Contents

- **Position and objective** — what this is, what it must achieve, its boundary.
- **The matching rule** — document identity, version comparison, deliberate limits.
- **Folder scope** — descend versus process, and the three path forms.
- **Archive behaviour** — where superseded files go and what is never overwritten.
- **Execution model** — master/instance deployment and script-folder resolution.
- **The three files** — script, settings contract, log contract.
- **Run modes and report vocabulary.**
- **Definition of done, idempotence, boundary, required verification cases.**

## Position

Version cleanup is the first piece of **Infrastructure** for the AIDE documentation corpus:
machinery that acts on the document tree but is never loaded into an AI session. It has no
authority over document content and states no methodology; it enforces one physical property of
the tree.

It is a **single-action tool**, not a framework. Sibling tools are separate scripts run in
sequence. There is deliberately no action registry, plugin system or shared base class. Any
commonality between siblings is resolved when the duplication is visible, not in anticipation of
it.

### Relationship to siblings

Version cleanup runs **first** in the corpus pipeline, so tools downstream can take what they find
without version reasoning:

```text
version cleanup  →  binder builder  →  (later siblings)
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
  → move every lower version into that folder's _superseded
  → report + append log entry
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
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` superseded |
| `Foo.md`, `Foo_v1.md` | `Foo.md` superseded — absent suffix is v0 |
| `Foo_v3.md` alone | stays, suffix or not |
| `Foo_v1.md`, `Foo_v2.txt` | different documents — extension is part of identity |
| `Foo_v2_draft.md` | no match — the suffix must be terminal |

Treating an unsuffixed file as v0 removes the special case: `Foo.md` versus `Foo_v1.md` is decided
by the same comparison as `Foo_v8.md` versus `Foo_v9.md`.

Highest number stays; all lower versions move. Version numbers are compared numerically, so
`_v10` outranks `_v9`.

### Deliberate limits

- **Case.** `_v` and `_V` are both recognised. The document identity itself is compared with exact
  case, so `Foo_v1.md` and `foo_v2.md` are two documents and neither moves. Conservative by intent.
- **Ties.** Two files can share a version number only through leading zeros (`Foo_v08.md`,
  `Foo_v8.md`). Which is current is then genuinely unclear, so the tool reports `AMBIGUOUS` and
  moves nothing in that group.
- **Compound extensions.** Only the final extension is treated as the extension, so
  `Foo_v8.tar.gz` has identity `Foo_v8.tar` and never matches. Not a concern for a document corpus.

**The general shape:** where a rule does not determine an answer, report it and move nothing. This
applies to every case in this class, not only ties.

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

- The underscore rule is what keeps the tool out of the `_superseded` folders it creates. It is
  the mechanism, not a convention layered on top of one.
- The **root** is an explicit choice in the settings file, so the underscore rule does not apply
  to it. An explicit exclude still does.
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

**Status: ratified as the Infrastructure-wide convention** (2026-09-04). This is not a local choice
of this tool. Binder builder and later siblings use the same vocabulary; a divergent path model in
a sibling is a defect.

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
  absolute path or one relative to the script folder, and rejects `~/` with that explanation.
- `..` is rejected inside a relative entry. A pattern has no anchor for it, so silently accepting
  one would produce an entry that never matches.
- Path comparison goes through `os.path.normcase`: case-insensitive on Windows, case-sensitive
  elsewhere. Matching therefore follows the local filesystem rather than diverging from it.
- The multi-segment form needs lookahead. A folder matching a *proper prefix* of an include
  pattern is descended into but not processed, which is how `_binder/current` reaches `current`
  through an underscore-prefixed parent.
- A relative `exclude` entry is correspondingly broad: `_superseded` would skip every such folder
  in the tree. That is the intent, and it is stated in the shipped settings file.

## Archive behaviour

Superseded files move into `_superseded`, a subfolder of the folder the file came from. It is
created lazily — a folder with nothing to archive never gains an empty `_superseded`.

**Nothing is ever overwritten.** If the destination name already exists, the source file is left
in place and the run reports `CONFLICT`. Two different documents competing for one archive slot is
a decision for a person. The destination is re-checked immediately before the move, because
`shutil.move` overwrites silently on Linux and macOS.

Files are moved, not copied and deleted; source and destination are always on the same volume.

## Execution model

```text
Documentation/Infrastructure/version-cleanup tool/   ← master, source of truth
        │  copy
        ▼
Documentation/_tools/                                ← instance: own settings, own log
```

Each instance resolves its settings file, its log and its root against **the folder holding the
script**, never against the current working directory. The working directory varies with how the
script was launched (double-click, terminal, scheduler) and is unreliable; the script folder does
not. This is also what gives each instance its own settings and its own log without any instance
registry.

Changes are made to the master and redeployed by copying. Instances are not edited in place except
for their settings file.

## The three files

| File | Role |
| --- | --- |
| `version_cleanup.py` | The script. Standard library only, Python 3.8+, cross-platform. |
| `version_cleanup_settings.json` | Per-instance configuration, read on launch. |
| `version_cleanup.log` | Append-only record, one entry per run. Created on first run. |

`README.md` and this design document travel with the master and are not required at runtime.

### Settings contract

```json
{
  "root": "..",
  "include": [],
  "exclude": [],
  "log_file": "version_cleanup.log"
}
```

- **JSON** — no third-party parser needed, editable by hand, and a syntax error is reported with
  line and column rather than as a stack trace.
- JSON has no comment syntax, so the shipped defaults carry their explanatory notes as keys
  beginning with `_comment`. The loader ignores them. The alternative — a JSONC dialect with a
  hand-written comment stripper — buys nothing and adds a parser to maintain.
- `root` and `log_file` resolve against the script folder when relative, so `".."` means "the
  folder above the tool" — the right default for an instance living in `Documentation/_tools`.
  `include` and `exclude` use the three path forms above.
- A missing settings file is written from the shipped defaults rather than being an error, so a
  bare `.py` copied to a new location bootstraps itself.

### Log contract

Append-only, one entry per run, never rewritten or trimmed. Dry runs are logged too, clearly
marked, so the log is a complete record of every time the tool was pointed at the tree. The
on-screen report and the log entry are produced by one function and cannot drift apart.

## Run modes

| Mode | Behaviour |
| --- | --- |
| default | Live. No confirmation prompt. |
| `--dry-run` | Identical report, `WOULD MOVE` in place of `MOVED`, nothing changed. |

Planning and acting are separate stages: `plan_folder` decides, `apply_moves` acts. A dry run
executes the same decision code as a live run, which is what makes it a trustworthy preview rather
than a parallel implementation.

The script pauses for a keypress before exiting so a double-clicked run can be read. The pause is
skipped when no interactive console is attached, so a scheduled run cannot hang on it.

## Report vocabulary

| Kind | Meaning |
| --- | --- |
| `MOVED` | File moved into `_superseded`. |
| `WOULD MOVE` | Dry run — the same file, unmoved. |
| `CONFLICT` | Destination name already taken; source left in place. |
| `AMBIGUOUS` | Duplicate version numbers in one group; nothing in the group moved. |
| `ERROR` | Filesystem refusal — locked file, permissions, unreadable folder. |

Events are grouped by folder in the report. A single failure does not abandon the run: the tool
reports it and continues, so the tree is never left half-tidied by an unrelated locked file.

Exit code is `0` unless at least one `ERROR` occurred. Conflicts and ambiguities are expected
outcomes requiring human attention, not failures of the run.

## Definition of done

Point an instance at a tree and afterwards that tree holds one version of each document, with
lower versions moved into `_superseded` beside where they lived, a readable on-screen report, and
one appended log entry. A dry run produces the identical report and changes nothing. Conflicts and
ambiguities are reported rather than resolved.

## Idempotence

Running the tool twice over the same tree produces no further movement. `_superseded` folders are
underscore-prefixed and therefore outside scope on the second pass; every remaining folder holds
one version per document, so no group has a superseded member.

## Out of scope — hard boundary

Version cleanup tidies versions. It does not assemble binders, does not deploy, does not edit
document content, does not rename files, and does not delete anything. Superseded material is
moved, never removed. Deletion from `_superseded` is a human act.

## Required verification cases

The cases the tool must handle. This is the regression set for any future change, not a record of
one build.

- **Matching** — multi-version groups including `_v10` versus `_v9`; unsuffixed v0; lone versioned
  files; extension mismatch; leading-zero ambiguity.
- **Scope** — nested folders; default underscore skip; all three include forms (a relative pattern
  catching several `_binder` folders at different depths, root-anchored catching only the top one,
  absolute catching one exact folder); a multi-segment pattern traversing an underscore parent
  without processing it; relative and root-anchored excludes.
- **Refusals** — pre-existing archive conflict; malformed JSON; missing root; `..` in a relative
  entry; bare `~`; `~name`; `~/` in the root setting.
- **Repeatability** — a second live run over a tidied tree moving nothing.
