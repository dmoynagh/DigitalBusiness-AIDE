# Binder Builder — Design

> **Version 4** (2026-09-07). Adds change detection: a run whose scope is byte-for-byte what the
> last binder recorded reports `NO CHANGES` and writes nothing, and `--force` overrides that. No
> other behaviour change from v3, and no change to the output format, the settings schema or the
> meaning of any existing report word.

**Master/source folder:** `Documentation/Infrastructure/binder-builder`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings file: root, folder scope, file scope, output.
- **Path logic** — absolute, folder-relative and root-relative forms.
- **Processing model** — walk, collect, order, assemble.
- **Change detection** — when a rebuild is skipped, and when it never is.
- **Binder output format** — header, manifest, source delimiters.
- **Versioning and output placement.**
- **Execution behaviour** — live by default, dry run, double-click.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Gather the current documents of a defined scope into a single file that can be
dropped into an AI session's context, so a whole topic loads as one artefact rather than many.

**Boundary — hard.** It collects and assembles. It does **not** resolve versions (that is version
cleanup's job, run first) and it does **not** deploy. It is Infrastructure: it acts on the corpus
and is never loaded into an AI session itself.

**Shape.** A single-action tool, sibling to version cleanup. No actions framework, no shared base
class, no plugin system.

**Pipeline position.** `version cleanup` → `binder builder`. Version cleanup leaves only current
documents in the live tree, so the binder builder can take what it finds without version reasoning.

---

## 2. Inputs — the settings file

JSON, read on launch. The settings file **is** the binder definition: it declares the binder's
scope. One instance folder per binder.

| Setting | Purpose |
|---|---|
| `root` | The path the binder is built from. Anchor for root-relative paths. |
| `subfolders` | `true` — walk the tree from root. `false` — process `root` only. |
| `include` | Folders to process that would otherwise be skipped. |
| `exclude` | Folders to skip. |
| `file_types` | Extensions to include. Default: `md`, `yaml`, `yml`, `json`, `txt`, `py`. |
| `exclude_files` | Filename patterns to skip regardless of type. |
| `order` | Optional. Filenames pulled to the front of the binder, in the order listed. |
| `output` | Folder the binder is written to. |
| `name` | The binder's name. Used in both the `# <name> Binder` heading and the `<name>_Binder_v<N>.md` filename. Must contain no path separator. |
| `log_file` | Log file location. Named to match version cleanup; the two tools must not disagree on the name of the same setting. |

The script writes a commented default settings file if none is present, rather than failing.

### Default folder exclusions

Skipped unless explicitly included:

- Folders with a leading underscore — this keeps the tool out of `_superseded` and out of its own
  `_binder` output.
- Asset folders by name: `assets`, `images`, `img`, `media`.

---

## 3. Path logic

Three forms, resolved as follows. **This supersedes the script-relative behaviour built into
version cleanup v1**; both tools should share this rule.

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_binder` | Exact folder. Survives the instance being moved. |
| **Folder-relative** | `_binder` | A **pattern**, tested against every folder the walk reaches: matches any folder whose path **ends with those segments**. Multi-segment works — `_binder/current` matches any `…/_binder/current`, and the walk passes through the underscore parent to reach it without processing that parent. |
| **Root-relative** | `~/_binder` | Anchored to the `root` setting. One exact folder. |

**Ratified as the Infrastructure-wide convention** (version-cleanup/claude-code/001, 2026-09-04).

**Rejected as errors, not silently tolerated:** `..` inside a relative entry (a pattern has no
anchor for it), bare `~`, `~name`, and `~/` in the `root` setting.

**Consequence, deliberate:** `~` no longer means home directory anywhere in these settings. Home
expansion is dropped for include and exclude paths.

**Consequence, deliberate:** a short exclude entry is powerful. `"exclude": ["_superseded"]` removes
every such folder in the tree. That is the intent, but it means an innocuous-looking entry can take
out a whole class of folders. Prefer absolute or root-relative for anything non-obvious.

**Including a folder does not include its underscore children.** `_binder` included still skips
`_binder/_superseded`.

---

## 4. Processing model

1. Resolve settings; resolve `root`.
2. Walk from `root` (or process `root` alone if `subfolders` is false), applying folder scope rules
   at each step.
3. Collect files matching `file_types` and not matching `exclude_files`.
4. Order: files named in `order` first, in that order; everything else alphabetically by path.
5. Assemble the binder.
6. Write it to `output`, append to the log, report on screen.

**Descend and process are two separate questions.** Reaching a folder nested inside an excluded
parent means walking *through* that parent without collecting from it — which is how a
`_binder/current` include pattern traverses the underscore-prefixed parent and collects only from
`current`. Fusing the two questions would make multi-segment include patterns unreachable.

**Live state is excluded by convention, not by rule.** Work-in-progress, working, open-items and
work-register documents are loaded separately when active state is needed. Exclude them through
`exclude_files` in the binder's own settings rather than hard-coding names into the tool.

---

## 4a. Change detection

A binder is a derived artefact. If every in-scope file is byte-for-byte what it was when the last
binder was written, rebuilding produces the same content under a new version number and pushes a
perfectly good binder into `_superseded` for nothing. Untidy when someone runs the tool by hand;
wasteful once the FileUpdatePackage deployer runs it after every deploy.

**The comparison needs no new state.** The answer is already in the binder: §5's manifest lists
every file it contains with a digest of that file's content. Reading that manifest back and
comparing it against the digests this run computed answers "has anything in scope changed" exactly
— additions and removals included, because the comparison is over the *set* of files as well as
over the digests.

1. Assemble as normal, computing a digest per file. Nothing is written yet.
2. Parse the manifest of the current binder into filename → digest pairs.
3. Same set of labels, same digests → report `NO CHANGES`, write nothing, supersede nothing,
   consume no version number. Otherwise rebuild as normal.

**Every uncertainty resolves towards rebuilding.** The tool always builds when:

| Case | Why |
|---|---|
| No previous binder | First run. Nothing to compare against. |
| The previous binder cannot be read, or is not UTF-8 | No baseline. |
| Its manifest heading is absent, or any entry will not parse | The contents of that binder cannot be established, and guessing at the rest would be worse than rebuilding. |
| The previous binder is stamped `INCOMPLETE` | It is missing files by definition, so "nothing changed" measured against it would hold the hole open indefinitely. |
| A source could not be read *this* run | The run is already incomplete; §5a governs it, not this section. |
| `--force` | The stated override. |

The asymmetry is deliberate. An unnecessary rebuild costs a version number. A wrongly skipped one
leaves a binder that misrepresents the tree, which is the failure this tool exists to prevent.

**Report.** `NO CHANGES` live, `WOULD CHECK` in a dry run. Both name the binder compared against.
Every run — skipped or not — also carries a `change detection:` line in the report header stating
what the comparison found, so a log entry that rebuilt says why it rebuilt and not only that it did.

**The check is placed before the `INCLUDED` events are raised**, not after: a run that rebuilds
nothing must not claim to have included anything.

**The comparison reads the format §5 writes.** The manifest reader and the manifest writer are two
halves of one contract and have to change together. The reader is deliberately lenient about the
separator between the filename and the digest and strict about everything else, so a hand-tidied
binder still parses while an unrecognisable one falls back to rebuilding.

---

## 5. Binder output format

```markdown
# <Name> Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version <N>** (<date>).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `<filename>` — sha256 `<12-char digest>`
- `<filename>` — sha256 `<12-char digest>`

---

<!-- BEGIN SOURCE: <filename> -->
<full file content, unmodified>
<!-- END SOURCE: <filename> -->

---

<!-- BEGIN SOURCE: <next filename> -->
…
```

- Source content is copied **unmodified**, with exactly two stated exceptions:
  - A trailing newline is added where a source lacks one, so the closing delimiter sits on its own
    line.
  - A leading byte-order mark is stripped. A BOM is a start-of-file marker; one left embedded
    halfway down a binder puts a stray `U+FEFF` in the middle of the text.
- **Encoding.** Read bytes and decode `utf-8-sig`. Write UTF-8 without BOM, **in binary mode** —
  text mode on Windows rewrites every `\n` as `\r\n` and would silently alter every source line
  ending in the binder.
- Manifest lists files in binder order.
- Digests are truncated sha256, twelve characters, computed over **the source content as read**,
  not the section as written. D3's purpose is answering "does this binder match the masters"; a
  digest including the tool's own added newline answers a different question.
- **No hand-written change note** in the header — see Decision D2.
- Where assembly is incomplete, a block near the top of the binder lists every missing file.

---

## 5a. Incomplete and empty runs

Both cases share one rule: **a defective binder never displaces a good one.**

| Case | Behaviour |
|---|---|
| **Empty scope** — no in-scope files found | Write nothing. Report `EMPTY`. Previous binder untouched. |
| **Incomplete** — a source cannot be read or decoded | Write the binder, but do **not** supersede the previous one, so the last good binder stays available beside the holed one. Report `ERROR` naming the file, plus `INCOMPLETE`, and list the missing files in the binder's own header block and the log. |

---

## 6. Versioning and output placement

**Name:** `<name>_Binder_v<N>.md`, with its own counter independent of the documents inside.

**Version resolution:** scan the output folder for existing binders of that name, take the highest
`N`, write `N+1`. Self-managing; no version recorded in settings.

**Placement:** the output folder is declared in settings. Default `_binder` beside the masters — an
underscore folder, therefore excluded from the walk by default.

**Self-inclusion guard.** Skip any file in the output folder matching `<name>_Binder_v<N>.md`.

This is stated against the **artefact class**, not the artefact. A guard written against "the file
I am about to write" defends nothing, because that file does not exist when the guard runs — but
*last* run's binder does, and would be swallowed as an ordinary source, doubling the corpus on
every build. See Decision D9.

**Supersession:** on a successful and complete write, the binder builder moves the previous binder
of that name into `_superseded` inside the output folder. See Decision D7.

---

## 7. Execution behaviour

Matches version cleanup, so the tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be assembled and writes nothing.
- `--force` rebuilds even when §4a finds nothing changed. It is the only way to consume a version
  number deliberately.
- Reads settings on launch — no arguments required, so **double-click works on Windows**.
- Prints a clear report; **pauses for a keypress before exiting** so the console doesn't vanish.
- Appends one entry per run to the log: binder written, version, files included, any skipped.
- Cross-platform; Windows primary.

### Report vocabulary

`INCLUDED` / `WOULD INCLUDE` · `SKIPPED` · `UNMATCHED` · `NO CHANGES` / `WOULD CHECK` ·
`WRITTEN` / `WOULD WRITE` · `SUPERSEDED` / `WOULD SUPERSEDE` · `CONFLICT` · `EMPTY` ·
`INCOMPLETE` · `ERROR`

`NO CHANGES` is §4a: nothing in scope has changed, so no binder was written and the previous one
remains current. `WOULD CHECK` is the dry-run twin — the same comparison, reported rather than
acted on. Neither is a failure; both exit `0`.

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `UNMATCHED` is an `order` entry
naming a file not in scope — a binder assembled in an order its author did not get is a quiet
defect, so it is reported. Files whose extension is simply not in `file_types` are **not** reported;
a document tree is full of them and listing each would bury the report.

**Exit code `0` unless an `ERROR` occurred**, matching version cleanup. Note the consequence: an
`EMPTY` run exits `0`, so a script chaining the tools would not see it. Accepted for now — see §10.

---

## 8. Definition of done

Point an instance at a scope and it produces a single, correctly-versioned binder containing every
in-scope current document, with a manifest matching its contents, source files copied unmodified,
a readable on-screen report and a log entry. Dry run produces the same report and writes nothing.

Run it a second time with the tree untouched and it writes nothing, supersedes nothing, consumes no
version number, and says `NO CHANGES` naming the binder it compared against. Change, add or remove
any in-scope file and the next run rebuilds. `--force` rebuilds regardless. A run that cannot
establish a baseline — no previous binder, an unreadable one, an unparseable manifest, a previous
build stamped `INCOMPLETE` — rebuilds rather than skipping.

---

## 9. Decisions

**D1 — The settings file is the binder definition.** No separate definition document. The scope
declaration and the run configuration are the same information; splitting them would create two
things to keep in step. One instance folder per binder.

**D2 — Drop the hand-written change note from the binder header.** The old format carried an
authored line describing what changed in that issue. A generator cannot write it, and the binder is
a disposable regenerated artefact — a changelog on it duplicates the version lines the masters
already carry. *Reversible if a real need appears: add a `note` setting.*

**D3 — Keep the sha256 manifest digests.** Weak keep. They cost nothing to generate and answer
"does this binder match the masters" if a verification tool ever wants them.

**D4 — No partitioned binder sets.** The old corpus split one topic across five binders plus a set
index because of volume. Real problem, not today's problem. Build one binder per instance; revisit
if a topic genuinely exceeds a usable context.

**D5 — Version resolution by scanning output, not by settings.** A version number in settings is
state that drifts from reality. The folder is the truth.

**D6 — Path logic is shared with version cleanup.** Folder-relative evaluated per walk step,
root-relative via `~/`, absolute exact; home expansion dropped. Two Infrastructure tools with
different path semantics would be a trap.

**D7 — The binder builder supersedes its own previous output.** On a successful write it moves the
prior binder of that name into `_superseded` within the output folder.

*Considered and rejected:* leaving it for version cleanup. Rejected because the default output
folder is `_binder`, which version cleanup skips by the underscore rule — it would have to be
explicitly included purely to tidy up after every build. And this is not general supersession: the
tool knows exactly which single file it just replaced, so there is no scanning, grouping or version
reasoning to duplicate.

**Principle:** a tool cleans up after itself. Version cleanup handles supersession it didn't cause.

**D8 — `output` and `name` are two settings.** v1 gave one key described as carrying both the
folder and the binder's name. One key cannot do both jobs; the heading and the filename need the
name, the write needs the folder. Split, with `name` rejecting any path separator.

**D9 — Guards are written against the artefact class, not the artefact.** v1's self-inclusion check
("if a resolved input file is the output path, skip") is a no-op: the output file does not exist
when the guard runs. The previous run's binder does, and was swallowed as a source in test — six
files became seven, and the corpus would double on every build. The rule is to match the class
`<name>_Binder_v<N>.md`.

*Generalisable:* any Infrastructure tool that both reads and writes inside one tree needs its guard
written this way. This belongs to the Infrastructure container definition when that is written.

**D10 — Digests cover source content, not the written section.** They differ by one byte where a
source lacks a trailing newline. D3's stated purpose is comparison against the masters, so the
digest must describe the master.

**D11 — BOM stripping is a stated exception to byte-for-byte copying.** Accepted deliberately, and
named here so it is not later read as a defect.

**D12 — Change detection compares against the binder's own manifest, and keeps no state of its
own.** The alternatives were a sidecar state file recording what the last run saw, and timestamp
comparison against the binder's modification time.

*A sidecar file was rejected* because it is a second source of truth that drifts the first time a
binder is moved, restored or hand-edited — the same reasoning as D5, which put the version number
in the folder rather than in settings. The binder already carries a digest per file; that manifest
*is* the record of what the last build saw, and it cannot drift from the binder because it is part
of it.

*Timestamps were rejected* because they answer a different question. A file touched but not
changed, a checkout that rewrites every modification time, a copy across a filesystem — all move
timestamps without moving content. D3 kept the digests for exactly this purpose and this is the
verification tool it anticipated.

*Consequence, accepted:* the reader in §4a is coupled to the writer in §5. They are two halves of
one contract and are marked as such in both places.

*Consequence, accepted:* a change that leaves every digest identical — a file renamed to a name that
sorts to the same place, then back — is invisible. A digest comparison is a content comparison, and
that is the question worth answering.

---

## 10. Open

- **`EMPTY` and `NO CHANGES` exit codes.** Both are `0`, consistent with treating expected outcomes
  as non-failures. A caller therefore cannot distinguish "binder rebuilt" from "nothing written"
  by exit code alone. The FileUpdatePackage deployer, which now chains this tool, does not need to:
  it reports the binder builder's outcome by reading its report, and a skipped rebuild is a correct
  outcome for it rather than a condition to handle. Prefer a distinct exit code for "nothing
  written" over overloading the failure code if a caller ever does need to branch on it. **Not
  now.**
- **Path-logic duplication.** The three path forms now exist in two implementations. The trigger for
  extracting shared code is a **third tool needing it**, not a third mention. The logic is pure
  functions over paths with no state, which is what has kept copying cheap.
- **The `_superceded` misspelling** at the Documentation root remains, alongside correctly-spelled
  folders. Both are underscore-prefixed so both are skipped. A human act to reconcile.
