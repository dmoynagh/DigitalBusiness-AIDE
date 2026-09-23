# binder builder

Gathers the current documents of a defined scope into a single file, so a whole
topic can be dropped into an AI session's context as one artefact rather than
as many.

The tool is `aide binder`, one of the utilities built into the `aide` CLI
(`aide-cli`, in the deploy repo `DigitalBusiness-AIDE-Deploy`, distributed via
`aide update`). This folder holds the design documentation for the tool, not
the tool itself — there is no standalone script to run here.

**A settings file is a binder definition.** It declares the scope. To define a
second binder, put a second settings file beside the first — one run builds them
all. See *Several binders in one folder* below.

**Run version cleanup first.** It leaves only current documents in the tree, so
the binder builder can take what it finds without any version reasoning of its
own.

**It will not rebuild for nothing.** If no in-scope file has changed since the
last binder was written, the run reports `NO CHANGES` and writes nothing. See
*Change detection* below.

---

## Running it

From anywhere inside a project (the tool walks up from the current folder to
find `_aide/`):

```
aide binder
```

builds every binder defined for the project. Other flags:

```
aide binder --list       # show what's defined, build nothing
aide binder --dry-run    # report what would happen, write nothing
aide binder --force      # rebuild even if nothing changed
```

There is no per-binder selection by name any more — a run always builds every
definition found. `--dry-run` and `--force` apply to the whole run.

---

## What it produces

```markdown
# <Name> Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 3** (2026-09-04).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `Alpha/Alpha_Design_v3.md` - sha256 `06f6435c91ff`
- `Beta/beta.yaml` - sha256 `75d068ad343e`

---

<!-- BEGIN SOURCE: Alpha/Alpha_Design_v3.md -->
…the file, exactly as it is on disk…
<!-- END SOURCE: Alpha/Alpha_Design_v3.md -->

---

<!-- BEGIN SOURCE: Beta/beta.yaml -->
…
```

Source content is copied **unmodified** — no reformatting, no heading demotion,
no trimming. The manifest lists the files in binder order, with a truncated
sha256 of each source, so a binder can be checked against its masters.

The one adjustment: a newline is added after a source that does not end with
one, so the closing delimiter starts on its own line.

---

## Settings

There are no binder settings in `_aide/settings.json` — a binder's scope is
defined entirely by its own settings file. `aide binder` reads every
`binder_builder*settings*.json` file it finds in the project's per-project
runtime settings folder:

```
_aide/utilities/binder-builder/
```

not from wherever the terminal happens to be pointing, and not from any
package default (`aide-cli` ships none — `"binder": {}` in its defaults). Each
one is a binder. If the folder holds none at all, the run reports what it
expected and where, rather than inventing one — create the first settings file
by hand:

```json
{
  "name": "Documentation",
  "root": "..",
  "subfolders": true,
  "include": [],
  "exclude": [],
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],
  "exclude_files": [],
  "order": [],
  "output": "~/_binder",
  "log_file": "binder_builder_Documentation.log"
}
```

| Setting | Meaning |
| --- | --- |
| `name` | The binder's name — used in the heading and in the filename. |
| `root` | The folder the binder is built from. |
| `subfolders` | `true` walks the whole tree; `false` collects from `root` only. |
| `include` | Folders to collect from that would otherwise be skipped. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `file_types` | Extensions to collect, without the dot. |
| `exclude_files` | Files to skip — by name, or by path. Applied after `file_types`. |
| `order` | Filenames pulled to the front of the binder, in the order listed. |
| `output` | The folder the binder is written to. |
| `log_file` | Where the run log is appended. Defaults to `binder_builder_<name>.log` next to the settings file if left out. |

### Which folders are skipped by default

- Any folder whose name starts with an underscore. This is what keeps the tool
  out of `_superseded` and out of its own `_binder` output — it is the
  mechanism that makes it impossible for a binder to contain a binder.
- The asset folders `assets`, `images`, `img` and `media`, by name.

List a folder in `include` to collect from it anyway. Including a folder does
**not** include its underscore-prefixed children: `_binder` included still skips
`_binder/_superseded`.

### The three path forms

**`root`, `output` and `log_file`** take a full path, a `~/` path measured from
`root`, or a path measured from the settings file's own folder — so `".."`
means "the folder above me", and a settings file sitting in
`_aide/utilities/binder-builder/` builds from the project root by default.
(`root` itself cannot use `~/`, since it is what defines the root.)

**`include` and `exclude`** take the same three forms, but the relative one
means something different:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

**`exclude_files` takes the same three forms**, applied to files — see
*Excluding files by path* below.

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at any
depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`, and the walk passes *through* the underscore parent to
reach it without collecting that parent's own files.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree**, never your home folder. The tool
  never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them. Prefer
  absolute or root-anchored for anything non-obvious.

This is the same path model as version cleanup, deliberately. Two Infrastructure
tools with different path semantics would be a trap.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so notes can be carried as keys
beginning with `_comment`. They are ordinary JSON and the tool ignores them.

### Excluding live state

The working document — work in progress, working notes — is loaded separately
when active state is actually needed, so it is normally kept out of the binder.
Do that through `exclude_files` in the binder's own settings rather than
expecting the tool to know the names:

```json
"exclude_files": ["*_WIP_*", "*_Working_*"]
```

**Work registers and open-items documents are a different case: they belong
*in* the binder.** The test is **durability, not cadence** — everything that
outlives the session is binder-class, and a parked question outlives the
session by definition. Both churn at session cadence in raw terms; what makes
them binder-safe is that they are written at master update. Do not add a
`*_WorkRegister_*` or `*_OpenItems_*` pattern here.

Items accumulate in the working document between master updates, so a reader
wanting current register or open items checks the working document as well.

`*` matches any run of characters and `?` matches one, matched
case-insensitively on Windows and case-sensitively elsewhere — the same way the
filesystem does.

### Excluding files by path

An `exclude_files` entry containing a `/` is matched against the file's **path**
rather than its name, using the same three forms as `include` and `exclude`:

| Form | Example | Means |
| --- | --- | --- |
| Filename | `"*_WIP_*"` | the name, wherever the file is |
| Root-anchored | `"~/_rebuild/*.json"` | that exact path, measured from `root` |
| Trailing | `"_rebuild/*.json"` | a **pattern**: any file whose path ends with those segments, so it covers a `_rebuild` folder at any depth |

**An entry with no `/` in it behaves exactly as it always did**, so nothing you
have already written changes.

In the two path forms, `*` stops at a folder separator and `**` crosses them:

| Pattern | `_rebuild/notes.json` | `_rebuild/sub/notes.json` |
| --- | --- | --- |
| `~/_rebuild/*.json` | matches | no |
| `~/_rebuild/*/*.json` | no | matches |
| `~/_rebuild/**/*.json` | matches | matches |

So `*/` is "exactly one folder down" and `**/` is "here and anything below".
Use `**` when you mean recursive.

A bare `~`, a `~name`, or a `..` anywhere in a path pattern is refused with an
explanation rather than quietly matching nothing.

The report names the pattern that dropped each file:

```
SKIPPED  tool_settings.json: matches exclude_files pattern "~/_rebuild/*.json"
```

### Ordering

Files named in `order` come first, in the order listed. Everything else follows,
sorted by path. Matching is on the filename alone, so an `order` entry catches
that file wherever it lives.

An `order` entry that matches nothing in scope is reported as `UNMATCHED` rather
than passed over, because a binder assembled in an order its author did not get
is a quiet defect.

---

## Several binders in one folder

Each settings file in `_aide/utilities/binder-builder/` is one binder, and both
the settings and the log are named for the binder they belong to:

```
_aide/utilities/binder-builder/
├── binder_builder_AIDE_Documentation_settings.json
├── binder_builder_ProjectDesign_settings.json
├── binder_builder_AIDE_Documentation.log
└── binder_builder_ProjectDesign.log
```

So a folder of binders can be read from the listing without opening anything.

To add one, copy an existing settings file to
`binder_builder_<name>_settings.json`, edit it, and set its `name` to match.

**The filename is a convention, not an input.** The tool reads the `name`
*setting*, never the filename, so nothing breaks if they disagree — but
`--list` prints them side by side, which is where you will notice.

**The log name is derived.** Leave `log_file` out and each binder gets
`binder_builder_<name>.log` automatically, so several definitions do not
interleave their runs in one file. Set `log_file` explicitly if you would
rather several binders shared one — one file per folder in run order is
exactly what someone auditing a whole folder wants.

**Give each one a different `name`.** The name decides the output filename, so
two binders sharing one would take turns superseding each other's file. The tool
refuses to run at all if it finds a duplicate, and tells you which two files
clash.

They can share an output folder. `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit happily side by side in one `_binder`: each
definition only ever scans, supersedes and skips binders of its own name.

Each build produces its own report, and the run ends with a line for the folder:

```
========================================================================
Result: 4 binder(s) - 1 rebuilt, 3 unchanged
========================================================================
```

### If one definition is broken

It is reported on its own and the others still build. Several binders staying
current is the point of keeping them together; the rest going stale because one
has a trailing comma would defeat it. The run still exits `1`, and the roll-up
counts it:

```
Result: 4 binder(s) - 4 unchanged, 1 unreadable
```

### Why this is cheap

Change detection. Several definitions where nothing has changed cost a manifest
comparison per definition and no writes at all, so running the lot after every
edit is a sensible habit rather than an expensive one.

---

## Versioning and output

The binder is written as `<Name>_Binder_v<N>.md`, with a counter of its own,
independent of the versions of the documents inside it.

The version is worked out by **scanning the output folder** — highest `N` found,
write `N+1`. Nothing is recorded in settings, because a number kept in settings
drifts from reality the first time a file is moved by hand.

A run that finds nothing changed does not consume a version number — see
*Change detection* below.

On a successful write, the previous binder of that name is moved into
`_superseded` inside the output folder. A tool cleans up after itself; version
cleanup handles supersession it did not cause. Nothing is ever overwritten — if
the `_superseded` slot is taken, the run reports `CONFLICT` and leaves the file
alone.

---

## Change detection

The binder is a derived file. Rebuilding it when nothing has changed produces
the same content under a new version number and pushes a perfectly good binder
into `_superseded` for nothing.

So before writing, the tool compares what it just assembled against the
**manifest of the current binder** — the list of filenames and digests in that
binder's own header. Same files, same digests, and there is nothing to do:

```
change detection: Documentation_Binder_v7.md: 24 file(s) in scope, all matching the manifest - binder not rebuilt

[_binder]
  NO CHANGES       no changes detected since Documentation_Binder_v7.md; binder not rebuilt
```

Nothing is written, nothing is superseded, and no version number is used up.
The previous binder is still the current one.

Change, add or remove any in-scope file and the next run rebuilds, saying what
it noticed:

```
change detection: Documentation_Binder_v7.md: 1 changed, 1 added (Project Design/ProjectDesign_Design_v8.md, Project Design/ProjectDesign_Index_v8.md) - rebuilding
```

There is no state file. The comparison uses the digests the binder already
carries, so there is nothing that can drift out of step with it — and nothing
to clean up if a binder is moved or restored by hand.

**It builds whenever it cannot be sure.** No previous binder, a previous binder
it cannot read, a manifest it cannot parse, a previous build stamped
`INCOMPLETE`, or a source it could not read this time: all rebuild. An
unnecessary rebuild costs a version number; a wrongly skipped one leaves a
binder that misrepresents the tree.

**Timestamps are not used.** A file touched but not changed, or a checkout that
rewrites every modification time, would both trigger a pointless rebuild. The
comparison is over content.

`aide binder --force` rebuilds anyway. A dry run reports the same comparison as
`WOULD CHECK` and writes nothing either way.

---

## The report

| Kind | Meaning |
| --- | --- |
| `INCLUDED` | File placed in the binder, with its digest. |
| `WOULD INCLUDE` | Dry run — the same file, nothing written. |
| `SKIPPED` | In a collected folder, deliberately left out — an `exclude_files` match, or the tool's own output. |
| `UNMATCHED` | An `order` entry naming a file that is not in scope. |
| `NO CHANGES` | Nothing in scope has changed since the last binder. Nothing written, nothing superseded. |
| `WOULD CHECK` | Dry run — the same comparison, reported rather than acted on. |
| `WRITTEN` / `WOULD WRITE` | The binder itself. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The previous binder moved into `_superseded`. |
| `CONFLICT` | A destination name is already taken; nothing overwritten. |
| `EMPTY` | Nothing in scope. An empty binder is written, saying so. |
| `INCOMPLETE` | A source could not be read. The binder has a hole in it. |
| `ERROR` | A filesystem refusal — a locked file, permissions, an unreadable folder. |

Events are grouped by folder. The exit code is `0` unless at least one `ERROR`
occurred.

### Two cases worth understanding

**`EMPTY` — nothing was in scope.** The binder is still written, and says so on
its own first screenful:

```
> **EMPTY BINDER - nothing was in scope when this was built.**
>
> This is a statement about the tree, not a failure: the scope genuinely
> contained no files. If that is unexpected, the scope settings are where
> to look.
```

The previous binder is superseded as usual, so it is in `_superseded` and one
move from being restored if this was not what you wanted.

This is deliberate. Writing nothing sounds safer, but it leaves a binder in the
output folder presenting as current while asserting content the scope no
longer holds — and that binder is what gets loaded into a session. A stale
binder that looks authoritative is the worst thing this tool could produce. An
empty one that says it is empty is merely surprising.

`EMPTY` is reported whether or not anything was written, because an empty scope
is far more often a settings mistake than a true statement. If you see it and
did not expect it, check `include`, `exclude_files` and `file_types` first.

Running again with the scope still empty writes nothing further — change
detection sees an empty binder and an empty scope and reports `NO CHANGES`.

**`INCOMPLETE` — a source could not be read.** The binder is written, but it has
a hole in it, so it is stamped as incomplete in three places: the report, the
log, and a block near the top of the binder itself naming every missing file.
The previous binder is **not** superseded, so the last good one stays available.
A plausible-looking binder that is quietly missing a document is the worst thing
this tool could produce, so it is made loud in every place someone might look.

---

## Text encoding

Stated explicitly rather than left to the platform:

- **Read** as UTF-8, with a byte-order mark removed if one is present. That BOM
  removal is the only deviation from byte-for-byte copying, and it is
  deliberate: a BOM is a start-of-file marker, and leaving one embedded halfway
  down a binder puts a stray character in the middle of the text.
- **Write** as UTF-8 without a BOM, in binary mode so that no line-ending
  translation can happen. Line endings pass through exactly as they were in the
  source.

A file that is not valid UTF-8 cannot go into the binder. It is reported as an
`ERROR`, and the binder it would have gone into is stamped `INCOMPLETE`.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log lands
next to the settings file it belongs to, under
`_aide/utilities/binder-builder/`, unless `log_file` says otherwise. The log is
never rewritten or trimmed. If it grows unwieldy, archive or delete it by hand;
the tool will start a fresh one.

---

## Scope

It collects and assembles. It does not resolve versions — that is `aide
cleanup`'s job, run first — and it does not deploy. It is Infrastructure: it
acts on the corpus and is never loaded into an AI session itself.
