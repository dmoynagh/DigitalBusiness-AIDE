# Binder Builder — Design

> **Version 1** (2026-09-04). First design. Defines the binder builder Infrastructure tool: its
> objective, settings, path logic, binder output format and boundaries.

**Master/source folder:** `Documentation/Infrastructure/binder-builder`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings file: root, folder scope, file scope, output.
- **Path logic** — absolute, folder-relative and root-relative forms.
- **Processing model** — walk, collect, order, assemble.
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
| `output` | Folder the binder is written to, and the binder's name. |
| `log` | Log file location. |

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

**Live state is excluded by convention, not by rule.** Work-in-progress, working, open-items and
work-register documents are loaded separately when active state is needed. Exclude them through
`exclude_files` in the binder's own settings rather than hard-coding names into the tool.

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

- Source content is copied **unmodified**. No reformatting, no heading demotion.
- Manifest lists files in binder order.
- Digests are truncated sha256, twelve characters.
- **No hand-written change note** in the header — see Decision D2.

---

## 6. Versioning and output placement

**Name:** `<Name>_Binder_v<N>.md`, with its own counter independent of the documents inside.

**Version resolution:** scan the output folder for existing binders of that name, take the highest
`N`, write `N+1`. Self-managing; no version recorded in settings.

**Placement:** the output folder is declared in settings. Default `_binder` beside the masters — an
underscore folder, therefore excluded from the walk by default, so a binder can never include
itself.

**Supersession:** on a successful write, the binder builder moves the previous binder of that name
into `_superseded` inside the output folder. See Decision D7.

---

## 7. Execution behaviour

Matches version cleanup, so the tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be assembled and writes nothing.
- Reads settings on launch — no arguments required, so **double-click works on Windows**.
- Prints a clear report; **pauses for a keypress before exiting** so the console doesn't vanish.
- Appends one entry per run to the log: binder written, version, files included, any skipped.
- Cross-platform; Windows primary.

---

## 8. Definition of done

Point an instance at a scope and it produces a single, correctly-versioned binder containing every
in-scope current document, with a manifest matching its contents, source files copied unmodified,
a readable on-screen report and a log entry. Dry run produces the same report and writes nothing.

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

---

## 10. Open

- **Descend versus process.** Reaching a folder nested inside an excluded parent requires walking
  *through* that parent without processing it. Two separate questions in the code, not one. Version
  cleanup already separates them; the binder builder must too.
- **The `_superceded` misspelling.** A misspelled folder exists at the Documentation root alongside
  correctly-spelled ones. Both are underscore-prefixed so both are skipped, but it should be
  reconciled by hand before it propagates.
