# Binder Builder — Design

> **Version 7** (2026-09-08). Replaces v6's statement of the live-state convention with the test
> the corpus owner actually applies: **durability, not cadence**. Open-items documents join work
> registers inside the binder. v6 was right about registers and gave the wrong reason — it argued
> from write cadence, which is not the distinguishing property. Owner's statement relayed in
> `tool-pipeline/aide-rebuild-chat/003`. No code change, no behaviour change.
>
> v6 (2026-09-08) corrected v5's claim that registers are excluded. v5 (2026-09-07) added several
> binder definitions per folder — see §4b and BinderBuilder D13.

**Master/source folder:** `Documentation/Infrastructure/binder-builder`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings file: root, folder scope, file scope, output.
- **Path logic** — absolute, folder-relative and root-relative forms.
- **Processing model** — walk, collect, order, assemble.
- **Several definitions in one folder** — many binders, one run.
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
class, no plugin system. One instance folder may define several binders (§4b); each is still one
settings file, one scope, one output.

**Pipeline position.** `version cleanup` → `binder builder`. Version cleanup leaves only current
documents in the live tree, so the binder builder can take what it finds without version reasoning.

---

## 2. Inputs — the settings file

JSON, read on launch. A settings file **is** a binder definition: it declares one binder's scope.
An instance folder may hold several of them — see §4b.

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

**Live state is excluded by convention, not by rule.** The tool holds no opinion about which
filenames are live state and never has: it applies the `exclude_files` patterns a binder's own
settings give it, and hard-coding names into the tool is what this sentence exists to forbid.

The convention itself belongs to the corpus, not to this tool, and is stated here only so that a
settings file can be read against it. The test is one line:

> **The test is durability, not cadence.**
>
> The working document holds what is current-and-transient, plus pending content destined for
> masters not yet written. Everything that outlives the session is binder-class.

| Class | In the binder? |
|---|---|
| **The working document** — work in progress, working notes | **No.** Loaded separately when active state is needed. |
| **Work registers** | **Yes.** |
| **Open-items documents** | **Yes.** A parked question outlives the session by definition — that is what parking means. |

**Cadence is not the test, and mistaking it for one is the trap.** Registers and open-items
documents both churn at session cadence in raw terms. The discipline that makes them binder-safe is
that they are *written at master update*, and that discipline is available to any document. What
cannot be made binder-safe is content that is meaningless outside the session that produced it.

Items accumulate in the working document between master updates and move across when masters
update, so a reader wanting current register or open items checks the working document **as well
as** the register or open-items document.

**History, because both corrections were made against this tool's settings and both mattered.** v5
and earlier listed registers among the excluded, which was wrong (corrected v6, from
`tool-pipeline/aide-rebuild-chat/002`). v6 admitted registers on a cadence argument, which reached
the right answer by the wrong route and left open-items documents excluded; the owner replaced it
with the durability test in `tool-pipeline/aide-rebuild-chat/003`.

In both cases the running instance's `exclude_files` carried the pattern in question, invisible
only because no such document existed yet. Each would have dropped a document out of the binder the
moment the first masters landed — a binder that looks complete and quietly is not, which is the
failure §5a exists to make loud. A convention error in this table is not a documentation matter; it
is a defect waiting for its first input.

---

## 4b. Several definitions in one folder

Every `binder_builder_settings*.json` in the script's own folder is a binder definition. So a folder
holds `binder_builder_settings.json`, and beside it `binder_builder_settings_projectdesign.json`,
`binder_builder_settings_infrastructure.json`, and as many more as the corpus needs. **One run
builds all of them**, in file order — the plain name first, then the rest alphabetically.

**A binder is identified by its `name` setting.** That was already required to be unique: it names
the output file and drives the version scan, so two definitions sharing a name would supersede each
other's binder on alternate runs. Sharing is refused before anything runs, naming both files.

### Selection

| Command | Effect |
|---|---|
| `python binder_builder.py` | Every definition in the folder. |
| `python binder_builder.py ProjectDesign Infrastructure` | Just those two. |
| `python binder_builder.py --list` | What is defined here. Builds nothing. |

A selector matches a binder's `name`, or the filename of its settings file with or without the
extension, case-insensitively. **A selector that matches nothing stops the whole run** and prints
what is available: "build these four", three-quarters done, is worse than not started.

`--dry-run` and `--force` apply to whatever was selected.

### Isolation

One definition failing must not take the others down — the entire point of the feature is that four
binders stay current, and one mistyped settings file is not a reason for three good binders to go
stale. So a settings file that cannot be read, or one whose `root` does not exist, is reported as
its own `SETTINGS PROBLEM` block and the run carries on with the rest. The run exits `1`.

An unreadable settings file is reported **whether or not the run was narrowed to other binders**. It
is a fact about the folder rather than about the selection.

### The roll-up

When more than one binder ran — or when a settings file could not be read — the run ends with one
line for the folder as a whole:

```text
========================================================================
Result: 4 binder(s) - 1 rebuilt, 2 unchanged, 1 with problems
========================================================================
```

It is **not** printed when a single definition ran cleanly. A folder holding one binder therefore
produces exactly the output it always did, and anything reading the last `Result:` line of this
tool's output — the FileUpdatePackage deployer does — keeps working in both cases, reading the
per-binder line when there is one binder and the roll-up when there are several.

The roll-up is not written to any log: definitions may have different `log_file` settings, and a
folder-level line has no single log to belong to. Every binder's own report is logged as always.

### What makes this safe

A build reads no global state. Every path, every scope, every digest and every log in a build comes
out of one definition, so building four is building one, four times. The `_binder` output folder can
be shared because the version scan, the self-inclusion guard and supersession all match on the
binder's own `<name>_Binder_v<N>.md` class (§6, D9) — `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit side by side without either touching the other.

**The exception, stated:** if an output folder is deliberately brought *into* a binder's scope with
an `include`, that binder's self-inclusion guard will skip its own binders and swallow its
neighbours'. The default `_binder` is underscore-prefixed and therefore outside every walk, so this
cannot happen by accident.

**Change detection is what makes it cheap** (§4a). Four definitions where nothing has changed cost
four manifest comparisons and no writes at all.

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
- Naming one or more binders builds only those; `--list` shows what is defined. See §4b.
- Reads settings on launch — no arguments required, so **double-click works on Windows**, and a
  double-click builds every binder defined in the folder.
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

Put four settings files in one folder and one run keeps all four binders current, each reported
separately and the folder summarised in one line. Name one on the command line and only that one is
built. Name something that is not defined and nothing is built at all. Break one settings file and
the other three still build.

Run it a second time with the tree untouched and it writes nothing, supersedes nothing, consumes no
version number, and says `NO CHANGES` naming the binder it compared against. Change, add or remove
any in-scope file and the next run rebuilds. `--force` rebuilds regardless. A run that cannot
establish a baseline — no previous binder, an unreadable one, an unparseable manifest, a previous
build stamped `INCOMPLETE` — rebuilds rather than skipping.

---

## 9. Decisions

**D1 — The settings file is the binder definition.** No separate definition document. The scope
declaration and the run configuration are the same information; splitting them would create two
things to keep in step. *The second half of this decision — one instance folder per binder — is
reversed by D13; the first half stands and is what makes D13 work.*

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

**D13 — Several definitions in one folder, discovered by glob.** v1 to v4 said one binder means one
instance folder. That was right for what the tool then was and is wrong for what it now is.

*What changed underneath it.* The original reasoning was that a second binder in one settings file
would mean a settings schema with a list of binders in it, and every setting then having to say
which binder it belonged to — a configuration format growing a dimension. That objection still
holds, and this is not that: **one file is still exactly one binder**, with the schema untouched.
What is new is that the folder, not the file, is the unit of "everything here".

*What made it worth doing.* Change detection (D12). Before it, running four definitions meant
writing four binders and consuming four version numbers on every run, so the cost of "keep them all
current" scaled with the number of binders and running them separately was no worse. With it, three
unchanged binders cost three manifest comparisons. "Rebuild whatever needs rebuilding" became a
single cheap act, and the tool should let someone do it in one command.

*Considered and rejected:* a `--settings` argument naming a file. It solves nothing on its own — the
user still runs the tool four times, and now has to remember four filenames — and it makes
double-click, which is how this tool is actually used, the one mode that cannot reach the other
binders.

*Considered and rejected:* a separate list file naming the definitions. A second thing to keep in
step with the folder, which is the same objection as D5 to version numbers in settings. The folder
is the truth.

*Identity is the `name` setting*, not the filename, because `name` already had to be unique — it
decides the output filename. A duplicate is refused before anything runs rather than resolved,
because both plausible resolutions (first wins, last wins) silently give someone a binder they did
not ask for.

**D14 — One bad definition does not stop the good ones.** A settings file that will not parse is
reported and skipped; the rest build. The feature exists so that four binders stay current, and
"three went stale because the fourth had a trailing comma" would defeat it. The run still exits `1`.

*Consequence, accepted:* a run can be partly successful, which neither sibling tool can be. The
roll-up line exists to make that legible in one line rather than requiring the reader to scan four
report blocks.

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
- **Per-definition scheduling.** Every definition is built on every run. A binder whose scope is
  expensive to walk and rarely changes still gets walked. Not a problem at four definitions over a
  corpus this size; the shape of a fix, if it is ever needed, is a `skip_unless` or an interval in
  the settings — state in a settings file, which D5 warns about. **Not now.**
- **Path-logic duplication.** The three path forms now exist in two implementations. The trigger for
  extracting shared code is a **third tool needing it**, not a third mention. The logic is pure
  functions over paths with no state, which is what has kept copying cheap.
- **The `_superceded` misspelling** at the Documentation root remains, alongside correctly-spelled
  folders. Both are underscore-prefixed so both are skipped. A human act to reconcile.
