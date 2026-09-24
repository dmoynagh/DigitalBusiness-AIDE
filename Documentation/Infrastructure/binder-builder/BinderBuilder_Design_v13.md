> identity: BinderBuilder_Design@v13 | doctype: design | updated: 2026-09-24

# Binder Builder — Design

> **Version 13** (2026-09-24). Two fixes to live behaviour. A live rebuild now commits **only the
> binder files it wrote or deleted**, named by explicit path; anything else already staged is left
> staged and out of the commit. Before, it committed the whole index, so a rebuild swept in
> whatever else happened to be staged. And `aide binder --help` (or `-h`) now prints usage and
> exits; before, it ran a live build. See D22.
>
> **Version 12** (2026-09-24). Closes the open item v11 logged: the duplicate-`name` refusal D13
> requires is now implemented. `run()` loads every definition found before building or deleting
> anything, checks the set for a shared `name`, and — if any is found — refuses the whole run,
> naming the shared name and every settings file that declares it, without building or deleting a
> single file. Verified against the live Documentation tree. See D21.
>
> **Version 11** (2026-09-24). Rewritten to match the deployed tool. Binder builder is now a
> utility in the `aide` CLI, invoked as `aide binder`, not a standalone script run from an
> instance folder. It **deletes its own previous output** rather than moving it to `_superseded`
> — git history is the archive, and a live rebuild commits the written and deleted files itself.
> There is no default settings file written when none is found: the run reports what it expected
> and where. There is no per-binder selection by name any more — every run builds every
> definition found. `CONFLICT` is retired: deletion has no destination to collide with, and a
> fresh version number cannot collide with an existing file either. See D19, D20.
>
> **Open, not resolved in this pass:** D13's "a duplicate `name` is refused before anything runs"
> is not implemented in the live tool — two definitions sharing a `name` currently both build,
> each free to delete the other's output in turn, with no warning. This is a design requirement
> the code does not meet, not a documented behaviour change; see §10 Open.
>
> **Version 10** (2026-09-08). **Reverses §5a's empty-scope rule.** An empty scope now writes an
> empty binder, stamped as empty on its own face, instead of writing nothing and leaving the
> previous binder in place. The old rule protected a good binder from being replaced by an empty
> one; what it actually produced was a binder that went on asserting content the scope no longer
> held. See D18.
>
> v9 (2026-09-08) named a settings file and its log for the binder they belong to —
> `binder_builder_{name}_settings.json` and `binder_builder_{name}.log` — so a folder holding
> four definitions can be read without opening any of them. Older filenames still work: the
> discovery glob was widened, not replaced.
>
> v8 (2026-09-08) gave `exclude_files` the same three path forms as `include` and
> `exclude`, so an exclusion can name where a file is and not only what it is called. Added §4c, the
> scope resolution order as five layers, requested in `binder-settings/aide-rebuild-chat/001`. Added
> a `_comment_defaults` key to the shipped settings so the invisible default skips are visible to a
> reader of the settings file. Existing settings files were unaffected: an entry with no `/` in it
> behaves exactly as it always did.
>
> v7 (2026-09-08) replaced the live-state convention with the durability test. v6 corrected v5's
> claim that registers are excluded. v5 (2026-09-07) added several binder definitions per folder —
> see §4b and BinderBuilder D13.

**Design documentation:** `Documentation/Infrastructure/binder-builder`
**Script source:** `aide-cli/src/aide/utilities/binder.py` in the deploy repo, distributed via `aide update`
**Run via:** `aide binder` (or `--list`, `--dry-run`, `--force`)

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings file: root, folder scope, file scope, output.
- **Path logic** — absolute, folder-relative and root-relative forms.
- **Path forms for `exclude_files`** — the same three, applied to files.
- **Processing model** — walk, collect, order, assemble.
- **Change detection** — when a rebuild is skipped, and when it never is.
- **Several definitions in one folder** — many binders, one run.
- **Scope resolution, as layers** — the five layers, and what each can do.
- **Binder output format** — header, manifest, source delimiters.
- **Versioning and output placement.**
- **Execution behaviour** — a CLI utility, live by default, dry run, the git commit.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Gather the current documents of a defined scope into a single file that can be
dropped into an AI session's context, so a whole topic loads as one artefact rather than many.

**Boundary — hard.** It collects and assembles. It does **not** resolve versions (that is version
cleanup's job, run first) and it does **not** deploy. It is Infrastructure: it acts on the corpus
and is never loaded into an AI session itself.

**Shape.** A single-action utility in the `aide` CLI, sibling to version cleanup and the file
update package. No actions framework, no shared base class, no plugin system beyond the CLI's own
discovery of `name` / `description` / `run`. One instance folder may define several binders (§4b);
each is still one settings file, one scope, one output.

**Pipeline position.** `aide cleanup` → `aide binder` (also re-triggered by `aide fup` after a
deploy). Version cleanup leaves only current documents in the live tree, so the binder builder can
take what it finds without version reasoning.

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
| `exclude_files` | Files to skip. Filename patterns, or path-qualified patterns — see §3a. Applied after `file_types`; see §4c. |
| `order` | Optional. Filenames pulled to the front of the binder, in the order listed. |
| `output` | Folder the binder is written to. |
| `name` | The binder's name. Used in both the `# <name> Binder` heading and the `<name>_Binder_v<N>.md` filename. Must contain no path separator. |
| `log_file` | Log file location. Named to match version cleanup; the two tools must not disagree on the name of the same setting. |

A folder holding none of these settings files is reported — what was expected, and where — rather
than the tool inventing one. See Decision D19.

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

## 3a. Path forms for `exclude_files`

`exclude_files` takes the same three forms §3 gives `include` and `exclude`, read as files rather
than folders:

| Form | Example | Meaning |
|---|---|---|
| **Filename** | `*_WIP_*` | Matched against the name alone, wherever the file appears. |
| **Root-anchored** | `~/_rebuild/*.json` | One exact path, measured from `root`. |
| **Trailing** | `_rebuild/*.json` | A **pattern**: any file whose path ends with those segments, so one entry covers a `_rebuild` folder at any depth. |

**An entry with no `/` in it is the filename form and behaves exactly as it always did.** That is
what makes this change invisible to every settings file written before it.

### Wildcards

`?` matches one character. `*` and `**` differ between the forms, and the difference is the point:

| Pattern | `_rebuild/notes.json` | `_rebuild/sub/notes.json` |
|---|---|---|
| `~/_rebuild/*.json` | matches | **no** |
| `~/_rebuild/*/*.json` | **no** | matches |
| `~/_rebuild/**/*.json` | matches | matches |

In a path form **`*` stops at a folder separator and `**` crosses them**, `**` standing for zero or
more whole segments. In the filename form there are no separators to stop at, so `*` is
unrestricted as before.

**This is glob's rule, not `fnmatch`'s, and the substitution is deliberate.** `fnmatch`'s `*`
matches `/` as well as everything else, so `~/_rebuild/*.json` under `fnmatch` would also match
`_rebuild/anything/deep/x.json` and the qualification would mean nothing at all. See D15.

**Refused, not tolerated:** a bare `~`, `~name`, and `..` anywhere in a path form — the same
rejections §3 makes, for the same reason. A pattern that cannot mean anything is a settings error,
not a pattern that quietly matches nothing.

Matching is case-folded the way the local filesystem folds names, and paths are spelled with
forward slashes on every platform, so one settings file behaves the same everywhere.

**The report names the pattern that dropped a file** — `SKIPPED  x.json: matches exclude_files
pattern "~/_rebuild/*.json"` — which is the question anyone with four entries in a settings file
actually has.

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

## 4a. Change detection

A binder is a derived artefact. If every in-scope file is byte-for-byte what it was when the last
binder was written, rebuilding produces the same content under a new version number and deletes a
perfectly good binder for nothing. Untidy when someone runs the tool by hand; wasteful once the
FileUpdatePackage deployer runs it after every deploy.

**The comparison needs no new state.** The answer is already in the binder: §5's manifest lists
every file it contains with a digest of that file's content. Reading that manifest back and
comparing it against the digests this run computed answers "has anything in scope changed" exactly
— additions and removals included, because the comparison is over the *set* of files as well as
over the digests.

1. Assemble as normal, computing a digest per file. Nothing is written yet.
2. Parse the manifest of the current binder into filename → digest pairs.
3. Same set of labels, same digests → report `NO CHANGES`, write nothing, delete nothing,
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

## 4b. Several definitions in one folder

Every `binder_builder_settings*.json` in the script's own folder is a binder definition. So a folder
holds `binder_builder_settings.json`, and beside it `binder_builder_settings_projectdesign.json`,
`binder_builder_settings_infrastructure.json`, and as many more as the corpus needs. **One run
builds all of them**, in file order — the plain name first, then the rest alphabetically.

**A binder is identified by its `name` setting.** That was already required to be unique: it names
the output file and drives the version scan, so two definitions sharing a name would delete each
other's binder on alternate runs. Sharing is refused before anything runs, naming both files. *This
refusal is stated as a requirement but is not yet implemented in the live tool — see §10 Open.*

### File naming

The name goes in the filenames too, so a folder of four definitions can be read without opening any
of them:

| File | Form | Example |
|---|---|---|
| Settings | `binder_builder_{name}_settings.json` | `binder_builder_AIDE_Documentation_settings.json` |
| Log | `binder_builder_{name}.log` | `binder_builder_AIDE_Documentation.log` |

**The log name is derived, not required.** A definition that says nothing about `log_file` gets a
log named for itself, which is what keeps four definitions from interleaving four runs in one file.
Setting `log_file` explicitly still points several binders at one log, deliberately, and that
remains a legitimate choice — one file per folder in run order is exactly what someone auditing a
whole folder wants.

**The filename is a convention, not an input.** The tool reads the `name` *setting*, never the
filename, so the two can in principle disagree — nothing breaks if they do, and `--list` prints
them side by side, which is where a disagreement shows up. Enforcing agreement was considered and
rejected: it would break the two older spellings below for no gain beyond tidiness.

**Older filenames still work.** The discovery glob is `binder_builder*settings*.json`, deliberately
wider than the convention, and matches all three of:

- `binder_builder_{name}_settings.json` — the convention.
- `binder_builder_settings.json` — the original single-definition name. Sorts first when present.
- `binder_builder_settings_{x}.json` — the spelling this document recommended between v5 and v8.

A convention tidied after publication must not break the files written while the old one stood. See
D17.

### Selection

There is no per-binder selection by name in the live tool. `aide binder` builds every definition
found; `aide binder --list` shows what is defined without building anything. `--dry-run` and
`--force` apply to the whole run.

### Isolation

One definition failing must not take the others down — the entire point of the feature is that four
binders stay current, and one mistyped settings file is not a reason for three good binders to go
stale. So a settings file that cannot be read, or one whose `root` does not exist, is reported as
its own `SETTINGS PROBLEM` block and the run carries on with the rest. The run exits `1`.

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
be shared because the version scan, the self-inclusion guard and the delete-previous step all match
on the binder's own `<name>_Binder_v<N>.md` class (§6, D9) — `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit side by side without either touching the other.

**The exception, stated:** if an output folder is deliberately brought *into* a binder's scope with
an `include`, that binder's self-inclusion guard will skip its own binders and swallow its
neighbours'. The default `_binder` is underscore-prefixed and therefore outside every walk, so this
cannot happen by accident.

**Change detection is what makes it cheap** (§4a). Four definitions where nothing has changed cost
four manifest comparisons and no writes at all.

---

## 4c. Scope resolution, as layers

Scope is decided in five layers. **Each layer can only narrow what the previous one admitted**, and
at any level an exclusion beats an inclusion.

| Layer | Rule |
|---|---|
| **1 — Defaults** | Underscore folders and the asset folders `assets`, `images`, `img`, `media` are skipped unless overridden. |
| **2 — Include** | Overrides a default skip for named folders. Including a folder does not include its own default-skipped children. |
| **3 — Folder exclude** | Wins over include, always, along with everything beneath. |
| **4 — File types** | Only the listed extensions are collected from in-scope folders. |
| **5 — File exclude** | `exclude_files` drops matching files from what layer 4 admitted. The last word. |

**Layers 4 and 5 are sequential, not independent** — `exclude_files` is applied to what `file_types`
already selected. Confirmed against the build, and it has one observable consequence worth stating:
a file whose extension is not in `file_types` is dropped at layer 4 and never reaches layer 5, so it
produces no `SKIPPED` event. Only files that were genuinely in scope and then excluded are reported.
That is deliberate — §7 explains why unlisted extensions are silent — but it means the report shows
layer 5's decisions and not layer 4's.

Because layer 5 can only remove, a path-qualified pattern there **cannot conflict with a folder-level
include or exclude.** It can make an included folder contribute less; it can never make an excluded
folder contribute anything. That is what makes adding path qualification at layer 5 safe rather than
a second, competing scope language.

**The layers are stated in a settings file too, not only here.** `_comment_defaults` in the shipped
settings names layer 1 in plain language, because layer 1 is the only one with no entry anywhere to
show for it — a reader who has never seen this document would otherwise have to infer the underscore
and asset-folder rules from behaviour. See D16.

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

The two cases look alike and are opposite. **An incomplete binder is defective; an empty binder is
correct.** A binder missing files it should contain cannot be trusted about anything. A binder
containing nothing, because nothing was in scope, is an accurate statement about the tree.

| Case | Behaviour |
|---|---|
| **Empty scope** — no in-scope files found | **Write the binder.** It carries an `EMPTY BINDER` block in its header and a manifest reading `(no files)`. The previous binder is deleted as usual. Report `EMPTY`. |
| **Incomplete** — a source cannot be read or decoded | Write the binder, but do **not** delete the previous one, so the last good binder stays available beside the holed one. Report `ERROR` naming the file, plus `INCOMPLETE`, and list the missing files in the binder's own header block and the log. |

The rule for the incomplete case is unchanged: **a defective binder never displaces a good one.**

**Change detection covers the empty case** (§4a), which is what stops it churning. An empty scope
whose current binder is already empty compares equal — nothing added, nothing removed — and reports
`NO CHANGES`. Only a transition into or out of empty writes anything.

**`EMPTY` is reported even when nothing is written**, because an empty scope is far more often a
mistake in the settings than a true statement about the tree, and nobody should have to infer it
from a binder with nothing in it.

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

**Deletion:** on a successful and complete write, the binder builder deletes the previous binder of
that name from the output folder. Git history is the archive — there is no `_superseded` folder for
this tool any more. See Decision D20 (supersedes D7).

---

## 7. Execution behaviour

A utility in the `aide` CLI, invoked as `aide binder`:

- Python, standard library only.
- Runs **live by default**; `--dry-run` reports what would be assembled and writes nothing.
- `--force` rebuilds even when §4a finds nothing changed. It is the only way to consume a version
  number deliberately.
- `--list` shows what is defined, without building anything. Every other run builds every
  definition found — see §4b.
- Settings are discovered from `_aide/utilities/binder-builder/` in the project (§2, §4b), never
  from wherever the terminal happens to be pointing.
- A live run that wrote or deleted anything commits those files to git, mirroring version cleanup
  and the file update package. See Decision D19. The commit holds **only** those files, named by
  explicit path; anything else already staged is left staged and out of the commit. See D22.
- `-h` / `--help` prints usage and exits. Nothing is built, deleted or committed. See D22.
- Prints a clear report.
- Appends one entry per run to the log: binder written, version, files included, any skipped.
- Cross-platform; Windows primary.

### Report vocabulary

`INCLUDED` / `WOULD INCLUDE` · `SKIPPED` · `UNMATCHED` · `NO CHANGES` / `WOULD CHECK` ·
`WRITTEN` / `WOULD WRITE` · `DELETED` / `WOULD DELETE` · `EMPTY` · `INCOMPLETE` · `ERROR`

`NO CHANGES` is §4a: nothing in scope has changed, so no binder was written and the previous one
remains current. `WOULD CHECK` is the dry-run twin — the same comparison, reported rather than
acted on. Neither is a failure; both exit `0`.

`ERROR` carries the same meaning across all three sibling utilities: a filesystem refusal — a
locked file, permissions, an unreadable folder. `CONFLICT` has been retired for this tool: deletion
has no destination to collide with, and a freshly-scanned version number cannot already be taken.
`UNMATCHED` is an `order` entry naming a file not in scope — a binder assembled in an order its
author did not get is a quiet defect, so it is reported. Files whose extension is simply not in
`file_types` are **not** reported; a document tree is full of them and listing each would bury the
report.

**Exit code `0` unless an `ERROR` occurred.** An `EMPTY` run exits `0`: it wrote a binder, and the
binder is correct. See §10.

---

## 8. Definition of done

Point an instance at a scope and it produces a single, correctly-versioned binder containing every
in-scope current document, with a manifest matching its contents, source files copied unmodified,
a readable on-screen report and a log entry. Dry run produces the same report and writes nothing.

An `exclude_files` entry naming a path — `~/_rebuild/*.json` — drops exactly the files at that
path and no others; the same entry written without a `~/` prefix drops them under a folder of that
name at any depth; an entry with no `/` behaves as it always did. A pattern that cannot mean
anything stops that binder with an explanation rather than matching nothing quietly. The report
names the pattern that dropped each file.

A folder of four definitions can be read from its file listing alone: each settings file and each
log carries its binder's name. A settings file written under either older spelling is still
discovered and built.

Put four settings files in one folder and one run keeps all four binders current, each reported
separately and the folder summarised in one line. Break one settings file and the other three still
build.

Point it at a scope that is empty and it writes a binder saying so, stamped `EMPTY BINDER` in its
own header, rather than leaving a binder that asserts content the scope no longer holds. Run it
again with the scope still empty and it writes nothing further.

Run it a second time with the tree untouched and it writes nothing, deletes nothing, consumes no
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

**D7 — The binder builder supersedes its own previous output.**

*Status: superseded by D20 — the binder builder now deletes its own previous output rather than
moving it to `_superseded`. The reasoning below is kept for the record.*

On a successful write it moves the prior binder of that name into `_superseded` within the output
folder.

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
user still runs the tool four times, and now has to remember four filenames.

*Considered and rejected:* a separate list file naming the definitions. A second thing to keep in
step with the folder, which is the same objection as D5 to version numbers in settings. The folder
is the truth.

*Identity is the `name` setting*, not the filename, because `name` already had to be unique — it
decides the output filename. A duplicate is refused before anything runs rather than resolved,
because both plausible resolutions (first wins, last wins) silently give someone a binder they did
not ask for. See D21 for how the refusal is enforced.

**D18 — An empty scope writes an empty binder.** Reverses the rule v1 to v9 held, that an empty
scope writes nothing and leaves the previous binder alone.

*The original reasoning, and why it was wrong.* The old rule called an empty binder replacing a good
one "a loss of information dressed up as a successful build". That framing has a false premise: the
previous binder was **superseded, not deleted** — it moved to `_superseded` beside the new one, and
recovering it was a file move. Almost nothing was lost. [Since superseded by D20: the previous
binder is now deleted outright, not moved; git history serves the recovery purpose `_superseded`
served here.] What the rule produced instead was worse: a binder sitting in the output folder,
presenting as current, asserting content the scope no longer held. A stale binder that looks
authoritative is precisely the failure this tool exists to prevent, and the old rule manufactured
one deliberately.

*The case that exposed it.* Exclusions are tightened until everything in scope is excluded. The tool
reported `EMPTY`, wrote nothing, and left a binder that still contained every excluded file. The
report said the scope was empty; the binder said otherwise; the binder is what gets loaded into a
session.

*What replaces the guard.* Three things, none of which the old rule provided. The binder says
`EMPTY BINDER` in its own header, so a reader who never sees a report cannot mistake it. The run
reports `EMPTY` whether or not it wrote, so a misconfigured scope stays loud. And the previous
binder's content is recoverable from git history, one checkout away from being restored.

*Consequence, accepted:* a typo in `root` now replaces a good binder with an empty one. That is a
real regression in one narrow case, recoverable from git, and it is preferred to the
alternative — a stale binder that nothing announces at all.

*Generalisable:* refusing to record an unwelcome state does not prevent the state, it only removes
the record. This tool's job is to describe the tree, including when the tree is empty.

**D17 — Settings and log are named for the binder; the glob is widened rather than replaced.**
`binder_builder_{name}_settings.json` and `binder_builder_{name}.log`. The reason is the one D13
created: once a folder can hold four definitions, four files called some variation of "settings"
have to be told apart, and opening each one to find out which binder it defines is exactly the
friction D13 was meant to remove.

*The glob is `binder_builder*settings*.json`, not the convention itself.* Three spellings now exist
in the wild — this document recommended `binder_builder_settings_{x}.json` between v5 and v8, and
`binder_builder_settings.json` predates definitions entirely. Narrowing the glob to the new
convention would have silently stopped discovering files written on this document's own advice, and
a binder that stops being built without saying so is the failure mode this tool most needs to avoid.
The cost of the wider glob is that it also matches names nobody intends to write; that costs
nothing, because an unintended match is a settings file that either parses or is reported.

*The log name is derived rather than mandated.* A definition may still name its log explicitly and
share one, which is the right answer for a folder someone audits as a whole.

*The filename is not read.* Identity stays in the `name` setting, per D13. The filename is a
convenience for humans reading a folder listing, and `--list` shows both so drift is visible.

**D15 — Path-qualified `exclude_files` uses glob's wildcards, not `fnmatch`'s.** In a path form
`*` stops at a folder separator and `**` crosses them.

*Why it cannot be `fnmatch`.* `fnmatch`'s `*` matches `/`, so `~/_rebuild/*.json` would also match
`_rebuild/deep/nested/x.json`. Every path-qualified pattern would then be silently recursive, the
qualification would carry no information, and there would be no way to express "this folder only" at
all. The one thing the feature exists to do could not be said.

*Consequence, accepted:* two wildcard dialects in one settings file — `fnmatch` for the filename
form, glob for the path forms. Considered and rejected: moving the filename form to glob as well.
Under glob, `*_WIP_*` still behaves identically because a filename contains no separators, so the
change would be invisible in every case anyone has written — but it would be a behaviour change to
existing settings for no benefit, and this design has consistently refused those.

*Consequence, accepted:* `~/_rebuild/*/*.json` means "exactly one folder below `_rebuild`", not
"`_rebuild` and everything under it". The recursive form is `~/_rebuild/**/*.json`. The request that
prompted this feature described the `*/` spelling as recursive; that reading is not available
without giving `*` `fnmatch` semantics and losing the non-recursive form entirely. Raised with the
requester rather than resolved silently.

**D16 — Defaults are documented in the settings file, not only in the design.** Layers 2 to 5 of
§4c each have a key in the settings file, so a reader sees them. Layer 1 has none: the underscore
rule and the asset-folder list are enforced by the tool with nothing in the settings to show for
them, and a reader who has never opened this document can only infer them from behaviour — usually
after being surprised. `_comment_defaults` states them where that reader is already looking.

*Generalisable:* any tool in this family whose behaviour includes a rule with no corresponding
setting should state that rule in the settings file. Silent defaults are the ones that get
rediscovered by accident.

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

**D19 — A utility in the `aide` CLI, not a standalone script.** The tool runs as `aide binder`,
sharing the project root and settings discovery with the rest of the `aide` framework — the same
move already made for version cleanup and the file update package. Settings are discovered from
`_aide/utilities/binder-builder/` in the project (§2, §4b) rather than from a script's own folder,
and a folder holding none is reported rather than seeded with an invented default: with several
definitions possible per folder (D13), there is no longer a single "the" default to write. A live
run that wrote or deleted anything commits those files to git, matching version cleanup
(VersionCleanup_Design D3) and the file update package (FileUpdatePackage_Design D7).

**D20 — Deletion replaces archiving for the binder's own previous output; no `_superseded`
folder.** Supersedes D7. The tree is under version control; git history is the record of what the
previous binder contained. A live rebuild deletes the prior binder of that name and commits the
deletion alongside the write, the same move made for version cleanup (VersionCleanup_Design D3) and
the file update package (FileUpdatePackage_Design D6). `CONFLICT` is retired along with it: the old
archive model needed it for a taken `_superseded` slot, and deletion has no slot to take.

D18's empty-scope decision stands unchanged — an empty scope still writes a binder that says so —
but its stated recovery path (moving the previous binder to `_superseded`) is now git history
instead of a filesystem move.

**D21 — The duplicate-`name` refusal is enforced before any definition is built or deleted.**
`run()` loads every settings file it discovers into a `Definition` first — exactly as it always
did for `--list` — and only then checks the resulting set for a `name` claimed by more than one.
Finding one refuses the entire run: nothing is built, nothing is deleted, for *any* definition in
the folder, not only the clashing pair. The report names the shared `name` and every settings file
that declares it.

*Scope of the refusal, deliberate.* A folder holding four definitions where two clash refuses all
four, not just the two that clash. The alternative — build the two with unique names, refuse only
the clashing pair — was rejected: it would make "the run partly worked" the normal experience of a
mistake that is trivial to fix (rename one file), and D14's isolation is for a settings file that
will not parse, a different failure with a different shape, not for this one.

*Placement in `run()`, deliberate.* The check sits after settings loading and before the
`--list` / build branch, so `--list` is refused under a duplicate exactly as a live run is — both
are "something runs" in the sense D13 means, and `--list` printing two same-named definitions
side by side is not a substitute for the refusal the name collision itself warrants.

*Relationship to D14.* D14's per-definition isolation — a settings file that will not parse is
reported and skipped, the rest still build — is unaffected and orthogonal. A definition that
fails to load never reaches the duplicate check at all; a duplicate name is found only among
definitions that *did* load cleanly, and D14 continues to isolate parse failures exactly as
before.

**D22 — A rebuild commits only its own files; help never builds.** Two faults in the live tool,
both of which produced mismatched commits on 2026-09-24.

*Commit.* The shared commit step in the `aide` CLI staged the binder's files and then committed
the whole index, so anything someone else had staged went into a commit titled
`binder: rebuilt … binder`. It now commits exactly the paths the rebuild wrote or deleted, by
explicit path (git's commit-with-paths, which commits only those paths). Anything else staged
stays staged, untouched, for its owner to commit. This is the rule the document manager service
already follows. The step is shared, so version cleanup (VersionCleanup_Design D4) and the file
update package (FileUpdatePackage_Design D10) get the same fix.

*Help.* `aide binder --help` was not recognised, and the binder ignores arguments it does not
know, so it ran a live build and commit. The CLI entry point now checks for `-h` / `--help`
before running any utility and prints that utility's usage instead. It is handled once, at the
entry point, so no utility can run on a help request — including `aide fup --help`, which would
otherwise have applied packages. `aide --help` lists the commands.

Both are covered in the CLI's binder tests: a build with an unrelated file staged commits only
the binder files and leaves the other file staged; `--help` and `-h` print usage and build and
commit nothing.

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
