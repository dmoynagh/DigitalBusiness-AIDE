# AIDE Rebuild — WIP

> **Version 5** (2026-09-06). Reworks §11a from a blank page as change management: the
> definition / detection / execution split, the settled change-definition model, the detection
> working with four of six questions closed, the cross-standard dependency resolution, and a
> requirements schedule to score models against. Execution is not started. Working document —
> does not conform to the full documentation methodology by design.

**Location:** `AIDE/documentation/_rebuild/`
**Status:** Active working document. Archive when the rebuild completes.

---

## Contents

- **Purpose and scope** — why this document exists, what the rebuild is.
- **Method** — parallel rebuild through a filter, not in-place edit.
- **The lifecycle model** — four modes, cross-cutting threads.
- **The design half** — brief, design, decisions; universal across project types.
- **AIDE scope and containers** — what AIDE is, the root, how containers earn their place.
- **Structure vs transport** — meaning drives the tree; binders carry documents into context.
- **Infrastructure** — machinery that acts on the corpus; the tool work.
- **Deployment** — parked; custom single-instance deploy.
- **Rebuild-wide policy** — set aside anything without a demonstrated requirement.
- **Decisions doctype** — reworked definition, closed.
- **Doctype / block-type model** — composition, what was cut.
- **Block catalogue** — the universal blocks, closed and parked.
- **Versioning model** — identity, drafts, publish, filename.
- **Format and rendering model** — fields, compact, per-format mapping, portability flag.
- **Change management** — definition settled, detection largely settled, execution open; requirements schedule.
- **Filter rules** — the sieve for passing old material into the new structure.
- **Folder structure** — repo layout for the rebuild.
- **Open questions** — parked, to resolve during the rebuild.
- **Next actions** — where to pick up.

---

## 1. Purpose and scope

Unchanged from v2. AIDE's substance is largely right; the corpus has drifted (bloat, buried
defining material, over-engineered deployment). The rebuild strips what doesn't serve a defined
outcome, refocuses what does, restructures so defining material sits at the top, and ensures every
part has a stated outcome, objective and definition of done.

Standing driver: the standards and behaviours that shape how AI works with you should be live in
your sessions, not just designed on paper. Everything else serves that.

---

## 2. Method

Unchanged from v2. Parallel rebuild through a filter, not in-place edit. Nothing gets in unless it
earns its place. Old corpus is a source to mine, not a thing to edit. Filtering may use the old
material to hand; shaping should not be done inside a context loaded with the old corpus.

---

## 6a. Infrastructure — the payload boundary

Payload = Standards, Tools, guidance loaded into the AI to shape behaviour (Capabilities).
Infrastructure = machinery that acts on the corpus and is never loaded into an AI session.

### Tool work done (prior session, folded in here)

Two Infrastructure utilities exist as Python, each with a design doc:

- **VersionCleanup** (`VersionCleanup_Design_v2`) — carries the "a tool cleans up after itself"
  principle and the three-form path model.
- **BinderBuilder** (`BinderBuilder_Design_v1`) — captures format, manifest, the supersession rule
  as D7 with a rejected alternative, and the ratified three-form path model.

### Tool placement (settled)

- Masters for the utilities live in an **Infrastructure** folder under the documentation root.
- Running instances are copied into an **`_tools`** folder at the documentation root — master
  versus execution point.
- These are Infrastructure utilities, NOT capability Tools. Infrastructure is machinery acting on
  the corpus, never loaded into an AI session.

### Consequence from the versioning model (this session)

VersionCleanup must be revised to understand **draft state**, not just a trailing `_v<number>`:
- group `v27-draft1 ... v27-draftN` together;
- treat flat `v27` as a different, terminal, immutable thing — not merely the highest number in the
  group;
- parse the generic `-{key}{n}` suffix and validate the key against the defined set (one member
  today: `draft`).

---

## 6b. Deployment — parked

Deployment is over-engineered for current scale ("sledgehammer") — package-manager-grade machinery
for one person and two platforms; complexity compounded when delegated to AI.

- Will hand-write a **custom single-instance deploy**.
- Extensible/distributed model revisited only if a real need appears.
- **Placement deliberately deferred** — decide where it goes once we know what it does.

---

## 6c. Rebuild-wide policy — demonstrated requirement

**Set aside anything without a demonstrated requirement.** If a need surfaces, it comes back with a
reason. Applied this session to the Internal section, Temporary owner-labelled state, Overview,
Type metadata, and (pending filter) Dependencies/Tags/References.

---

## 7. Decisions doctype — CLOSED

**Done criteria:** no valuable knowledge is lost. Design + Decisions together must allow the full
development path to be recreated and understood. Framing: other docs are a snapshot of the now;
Decisions and knowledge are everything else.

Eight agreed points:

1. **Purpose broadened.** Accumulated reasoning, alternatives, learnings and decision history
   valuable to a topic's past, present and future evolution — not only the direct path to the
   current position.
2. **Knowledge boundary.** Topic-scoped reasoning goes to Decisions; reasoning with no owning topic
   goes to Knowledge. Cross-topic reasoning lives where it most applies; single record + reference
   preferred over duplication; prompt the user if in doubt.
3. **Two new triggers.** (a) investigation/reasoning that shaped understanding whether or not it
   produced a decision; (b) content removed or replaced in any document — check it survives
   elsewhere, capture if valuable. Trigger (b) makes supersession an active checkpoint.
4. **Immutability relaxed.** Compaction allowed — consolidate duplicates, merge related reasoning —
   provided substance survives and temporal reference is retained where sequence affects
   interpretation. Changing a past decision's meaning is a new decision, not compaction. A
   cumulative log is not required.
5. **Authority tightened.** Design must be sufficient alone to produce the outcome; reasoning
   pertinent to current design choices belongs in Design. Decisions informs but does not override
   or supplement Design as executable authority. Design governs on conflict.
6. **Retention chain.** Conversation to WIP/Working to Decisions. Reasoning is persisted to WIP or
   Working when those update, then promoted to Decisions as Design is confirmed. Same-pass rule
   retained.
7. **Scope follows Design.** Absorbed into parent when Design merges; may split when Design splits
   and volume warrants. Split by closure state, not chronology.
8. **Exclusions unchanged.** Editorial, formatting, metadata, migration, mechanical maintenance
   alone do not create an entry.

Two variants drafted (in transcript): a fuller design-length definition, and a standard-length
version roughly half the length (rationale stripped, operative rules kept) for use inside a skill.

---

## 8. Doctype / block-type model — AGREED

Terminology change: "doctypes and sections" becomes "doctypes and block types." A block is a subset
of document content that may span one or more sections. Sections remain the unit of navigation,
storage and organisation.

Four rules:

- A **doctype** is the root definition for a document; states what it defines and which blocks it
  includes.
- A **block** is a named content definition mapping to one or more sections; blocks may include
  other blocks; composition recurses; no cycles.
- **Shared content is a block, not inheritance.** Universals live in a common block that doctypes
  include.
- **One source of truth.** Content defined in one place. Flag ambiguity rather than resolve
  silently.

Also: hosting rules attach to the block, not the section — one authoritative instance per semantic
scope, permitted hosts owner-defined, moves between hosts are structural not semantic. Contiguity
of a block's sections is a default, not a rule.

**Cut as over-engineered:** multiple doctype inheritance, abstract doctypes, block self-assignment
to doctypes (push model), collision precedence machinery (most-specific / last-declared). Residual
collision rule: doctype defines resolution if needed; otherwise flag to user.

DocMeth owns the doctype/block structure, how to use and apply it.

Catalogue scope: DocMeth holds only blocks common across documents or usable by any document.
Area/owner-specific blocks are defined in their topical area and merge at runtime. No central
repository.

### Catalogue preamble (rendering model)

- A block is a named set of **fields** with meaning.
- A block has a default **density**: compact or expanded. Doctype may override.
- Rendering follows the **format rendering rule**: structured formats express fields as native
  properties; prose formats express them as a heading or a delimited line.
- A block may use whatever structures suit its information (sections, tables, lists). Each maps to a
  native default in the format in use. **If anything a block defines would not port cleanly across
  formats, flag it for confirmation rather than deciding silently.**

---

## 9. Block catalogue

### Closed

**Declaration** (renamed from "preamble"). Mandatory in every governed document; its presence is
the DocMeth conformance marker and the corpus recognition mechanism. First block, fixed placement,
not overridable. Fields: title, doctype (root of the composition chain), identity, date. Density
compact. No separate version field — identity carries the version.
- Structured formats: a reserved top-level `aide` key holding the fields as sub-properties (nested,
  one level: `aide.identity`, not `aide_identity`). Presence of `aide` = governed.
- Markdown: a single delimited line, fixed field order (title, doctype, identity, date).
- The name "Declaration" lives in the methodology, not in the document; nothing emits the word.

**Header, Footer** — placement containers only, no semantics. Blocks declare they place into them
and may carry a hint. Ties resolved by doctype instruction or defined method. Containers are
themselves blocks. No literal marker line in markdown; footer start already marked by a horizontal
rule; body start is the first heading that is not Contents or Summary.

**Boundary proximity principle.** Value increases toward the file boundaries. Header runs
high-to-low from the top; footer runs low-to-high to the end (most important closest to file
start/end). Containers declare the gradient; blocks place against it.

**Version note** — metadata, top of footer (low-value end). One line, current version only, never
a list. Historical version notes do not accumulate anywhere; Decisions holds what mattered.

**Contents** — lets a reader decide whether to read the document and what it covers, at lowest cost.
Primary consumer is a file-scanning AI making a partial-read-and-stop decision; humans benefit too.
- Curated semantic map, grouped descriptive entries, not a heading repetition.
- Stable heading or section-number locators, never line numbers.
- Rendered inline / delimited, never a vertical list (expressed as density: compact).
- Placed immediately after the Declaration, before Summary.
- Included when a file-scanning agent could not decide whether to keep reading from the Declaration
  alone; doctype owners may set a per-type default.
- Doctype owner defines depth.

**Summary** — states what the document establishes, absorbed quickly.
- States the key model, key points and defining items — the substance, not a gesture at it.
- Stated, not explained. No expansion, reasoning or qualification; that is the body's role.
- The body expands, it does not restate. Re-establishing what the Summary states is a defect.
- Placed after Contents, before the body.
- Omitted only where the document is short enough that the Summary would substantially restate it.
- Doctype owner defines applicability and depth.
- Default exclusions: Decisions, WIP, WorkRegister, OpenItems, Index, structured data.

**Body** — the document's substance.
- Every governed document has a body; the only mandatory content block.
- Holds the authority; body governs on conflict with Summary.
- Expands what the Summary states; does not restate it.
- Structure is doctype-defined; the block model imposes no section shape.
- Everything not claimed by another block is body (default host).
- Density expanded.

Structural blocks total four: Declaration, Header, Body, Footer. Contents and Summary place into
Header. Body is between Header and Footer.

### Parked (need a case through the filter)

**Parking confirmed this session.** These blocks exist to serve downstream machinery — drift
detection, classification, citation. Until the components that consume them come through the filter
and demonstrate the need, there is nothing to anchor the decision to; deciding now would be deciding
ahead of requirement. They return when the component that needs them does. (Dependencies has since
been substantially resolved by the migration work — see §11a.)

- **Dependencies** — footer, `!AIDE_...@vN` form; "built against." Confirmed this session as the
  cascade record for migration, at **standard** granularity, not per-doctype or per-block. Survival
  is effectively decided; its exact form waits on the migration brief (§11a).
- **Tags** — footer property, AIDE_Tags-owned.
- **References** — footer, citation without conformance semantics; "related reading." Decide with
  Dependencies.
- **Overview** — returns as a discussion. Case to test is a topic-or-corpus-scale TLDR, not the old
  document-level one.

### Set aside

- **Internal section** — purpose overlaps Decisions; old spec already warned against using it as a
  hidden second body.
- **Temporary owner-labelled state** — no current user.

### Cut

- **Type metadata** — superseded by doctype in the Declaration.

---

## 10. Versioning model — CLOSED

Applies to versioning generally; the two-rhythm split applies at the publish boundary.

- **Identity** — authoritative, in the Declaration. Carries the contract version and draft state:
  `@v27-draft2` while working, `@v27` on publish. Absence of a draft marker means published and
  immutable.
- **Filename** — informative, mirrors the identity: `_v27-draft2.md` then `_v27.md`. Never
  authoritative.
- **Draft numbering** — filename and identity both carry the draft number and match; identity wins
  on conflict. Draft numbering is optional in the scheme, on by default. Self-describing is the
  better failure mode (a file pasted without its name still states what it is).
- **Reference forms** — `@v27` resolves to the published contract; `@v27-draft` resolves to the
  highest draft present.
- **Publish** — drops the draft marker in both identity and filename; creates the immutable
  contract. Published numbers are never reused.
- **Next cycle** — opens immediately at the next integer, `@v28-draft1`. No live drafts ever sit
  under a published version.
- **`.n`** — reserved, unused. Available for minor published releases later without colliding with
  draft counters.
- **Naming grammar** — `{name}_v{integer}-{key}{n}`. Exactly one key defined: `draft`. An undefined
  key is a conformance error, not a tolerated variant. Expressed as a named token, not a hardcoded
  literal, so adding a key later is a list addition, not a grammar reinterpretation.

Design documents (and other unpublished docs) run on a single rhythm — identity and file move
together. Only published outcomes (Standards, deployed contracts) use the two-rhythm split.

Every document has an identity in its Declaration regardless of publish state; filename is
informative only. This is a corpus-integrity requirement: the filename can be renamed and is
outside the content, so it cannot be authoritative.

Versioning documentation to revise: naming grammar, publish transition, published immutability,
reference forms, `.n` reservation, draft support.

---

## 11. Format and rendering model — CLOSED

- Governed documents today are Markdown. Filename grammar fixes `.md`.
- Escape hatches already in the corpus: **Assets** (filename/format fixed by consuming tool) and
  **Unmanaged files** (held but not governed).
- Future doctypes may use other formats: machine-readable / performance docs stay Markdown; Design,
  Brief, Overview, Guides could be HTML. YAML and JSON usable as document types or embedded inside
  docs as defined by blocks.

### HTML assessment (searched this session)

The pro-HTML position is a personal opinion piece by an Anthropic Claude Code engineer (Thariq
Shihipar, 9 May 2026), not Anthropic guidance. Its argument is human engagement with long
plans/audits/reports, not machine consumption. HTML is less token-efficient than Markdown; the
"more info per size" claim is expressiveness per screen line, not tokens. Markdown is still held to
win for chained agent handoffs, short content, and git repos where diffs matter — the exact profile
of this corpus. Recommendation: no change now. HTML earns a place only for long human-facing
artefacts, e.g. a topic-scale Overview if that returns.

### Rendering model

- **Format rendering rule** (DocMeth, stated once): a block is a named set of fields; structured
  formats express fields as native properties; prose formats express them as a heading or delimited
  line.
- **Density axis:** compact or expanded, per-block default, doctype override. Compact/expanded
  render per format (markdown inline vs headings; JSON flow vs pretty-print).
- **Per-format default mapping table:** each abstraction maps to one native construct by default, so
  any block renders with zero per-block, per-format instruction. HTML defaults: fields to a
  description list (`dl`, `dt`/`dd`); compact to inline; expanded to block; header/body/footer to
  their natural HTML equivalents. A correct document needs no per-block HTML; styling
  (colour, collapsibility, layout) is separate optional polish.
- **Renderers per format** are separate specs (Infrastructure), not DocMeth core and not block
  definitions. Markdown renderer trivial; HTML renderer substantial. Build none now.
- **Portability flag:** anything a block defines that would not port cleanly across formats is
  flagged for confirmation, not decided silently.

---

## 11a. Change management — WORKED, PARTIALLY SETTLED

Reworked from a blank page this session (2026-09-06), per the brief this section commissioned in
v4. The v4 content is superseded; what survives from it is noted inline.

### The split that unblocked it

The subject had been running as one problem and behaving like a spider's web. It is three:

- **A — Change definition.** What changed, in which version, and what the fix is.
- **B — Detection.** Which documents are behind, and how that is known.
- **C — Execution.** Who applies the fix, where, when, and with what authority.

Every attempt to settle one moved the other two. The old corpus fused them as well: the Dependencies
footer line carried both a conformance fact (B) and a runtime-presence level (C). Separated, each is
tractable. **A is settled. B is largely settled. C is not started.**

### Scope

Change management is defined **for standards**. Reuse as a general framework for other item types is
a nice-to-have, not a constraint on this design. Standard granularity also resolves the
dependency-granularity question that v4 worked twice: a document depends on a standard, and the
standard's internal doctype and block structure is the standard's own business. Same conclusion as
v4, reached as a consequence rather than a choice.

---

### A. Change definition — SETTLED

> **Publishing a standard version requires a migration record for that version. The record is a set
> of condition-to-action tasks that take a document from the previous version to this one.
> Conditions are evaluated against definitions, not inferred from document content. "No action" is
> stated, not implied. One accumulating migration file per standard, held alongside it and shipped
> with it.**

Points, each settled this session:

- **Migration is created at publish, not after.** A version is not published until its migration
  record is written. This is enforceable as a publish gate rather than remembered as a discipline —
  which matters, because the recorded failure of the old model was not bad design but that nothing
  ever executed.
- **Every version has a record, including "no action."** Positive declaration. Absence is ambiguous
  (nothing changed, or the author forgot); presence is a fact. Retained from the old model's
  positive-posture rule.
- **The record is condition-to-action tasks.** A standard may publish several doctypes and block
  types; each task carries the condition under which it applies — *if the document's doctype is X*,
  *if the doctype uses block type Y* — so one migration covers a corpus of differently-shaped
  documents.
- **Conditions resolve against the doctype definition, never against document content.** The doctype
  definition is the only source of truth for which block types a doctype currently uses. Inferring
  block usage from what a document looks like is guesswork and breaks the fail-visibly rule.
- **Held beside the definition, not inside it.** Definitions are payload and load into sessions;
  every token counts. Migration content is read only when migration is needed. Same seam as the
  payload/infrastructure boundary in §6a (what loads into an AI session versus what acts on the
  corpus from outside). The old model already did this as `migrations.md` alongside the standard.
- **Accumulates.** Every transition from the supported baseline to current is retained, so a
  document several versions behind can walk forward step by step. Pruning is possible only once
  nothing is proven to be sitting at the pruned version — which is the one job that requires a
  wide check.
- **Ships with the standard.** Without the fix present at the point the need is detected, all
  detection can do is stop work. Detection without remedy is a blocked session, which is the failure
  mode that causes a check to be disabled.

**Consequence worth noting.** The migration file is the portable asset and the executor is a
convenience built on top of it. Every consumption path — runtime check, another repo, a batch run,
or a human reading it — reads the same file. Nothing else has to be portable.

---

### B. Detection — LARGELY SETTLED

**The question detection answers:** does this document need work under the current standards, and
what work.

**Runtime is the only complete picture.** A document loaded for use is loaded with the things it
depends on; that is the only moment where document, applicable standards, their versions and their
migration records all exist together. This was the premise of the original methodology and it is
correct. It also composes without tracking: a document in a repository untouched for eight months
is checked the moment it is next used, and nobody had to remember that repository existed.

**Read is use.** If a document is read, a currency check runs.

Six detection questions were worked (numbered CM-Q1 to CM-Q6 to avoid collision with the Q-series in §14, the rebuild-wide open questions); four are settled.

**CM-Q1 — which standards apply to a document?** *Settled: declaration, repaired by migration.*
Derivation from doctype is truer; declaration is the practical compromise. The known risk of
declaration is a stale association — a doctype moves from standard A to standard B and the
document's declared dependency no longer reflects reality. That is repairable by an ordinary
condition-to-action task in A's migration: *if doctype is X, add standard B as a dependency*. So
declaration stops being lossy, at declaration cost. **A corpus-wide "global action" that all
documents check regardless of standard versioning was considered and rejected** as a second
mechanism sitting permanently in the check path; the demonstrated-requirement rule (§6c) applies.
Revisit only if a case forces it.

**CM-Q2 — what was the document last brought into line with?** *Settled in principle.* The document must
carry this; nothing else remembers. Exact form (one stamp per standard, or one combined) is open and
falls out of the execution design.

**CM-Q5 — where does the wrong/old severity live?** *Settled: on the task, not the version.* The
governing test:

> **Blocking = the old shape produces a *wrong* result. Non-blocking = the old shape produces an
> *old* result.**

The user's framing was discoverability — if a change alters whether a document can be found and
used, it must be applied before use. Widened slightly: a renamed field that now means something
else, or a consumer silently reading a moved block and getting nothing, are also wrong rather than
merely dated. A release can genuinely mix both kinds; version-level severity forces the whole
release up to its most severe member, so one wrong-making change makes three cosmetic ones blocking.
This restores the old model's original task-level classification, which a later decision had moved
to release level.

**CM-Q6 — can detection run without the standard present?** *Settled: no, and that is a safety rule.*
If the standards are not present the session is operating outside the methodology environment.
That is a legitimate choice, at the user's risk — but **documents must not be modified there.**

**CM-Q3 — when does detection run?** *Open.* Read/use is primary and free. Session start is best-effort
and unreliable in chat. On-demand and a wide sweep are the same thing at different scopes. The live
question: does read-time observation alone satisfy the requirement to know what is outstanding
across documents nobody has opened, or is an explicit wide check a required part of the model? This
decides whether a sweep is part of the design or a convenience someone may build later. It is the
last item detection owes.

**CM-Q4 — what does detection produce?** *Provisional: a work list, not a flag.* Sorting wrong from old
requires knowing which tasks apply, which requires evaluating conditions. The cost concern is met by
a cheap summary carried alongside the tasks — *does any version in this range contain a
wrong-making task?* — answering the cheap question without evaluating the full set. Confirm with CM-Q3.

---

### Cross-standard dependencies — SETTLED

The case: a block type owned by standard B is used by a doctype owned by standard A, and the block
type changes.

**Standards declare dependencies on standards. Documents inherit them.** A document implementing a
doctype from A declares A, and also A's declared dependencies, including B. A change to the block
type moves B's version and produces B's migration; the document is reached through the inherited
dependency. This reuses the standards-declare-their-own-dependencies cascade already noted in v4
rather than adding a construct.

**Each standard is used at its own current available version, independently.** Not "the newest
standard wins." If B is at v6 and A still declares B at v4, the document records B at the version it
actually read the block type from — v6. A stamp claiming v4 when the session used v6 would be a lie.

**Consequence: A can be behind its own dependency without A's version moving.** The document is
internally consistent; the standards are not. This is a standard-to-standard currency problem and it
is invisible to document-level detection.

Two solutions were considered and one rejected:

- **Rejected — publish multiple versions of a standard and let documents pull the matching one.**
  Compatibility-matrix machinery, and it creates retrieval ambiguity for an AI deciding which to
  use.
- **Rejected — halt all work whenever a standard is behind a standard it depends on.** Considered
  and argued down. Any standard update would block the environment until every dependent standard
  was republished, one at a time, creating a self-inflicted outage whose only lesson is to avoid
  updating standards. It also treats every mismatch as wrong when most are merely old, which
  contradicts the task-level severity settled at CM-Q5.
- **Adopted — apply the wrong/old test to the mismatch itself.** Halt on the consequence, not the
  condition. B's migration may carry tasks conditioned on a dependent standard's behaviour — *if you
  extend this block type's X field, do this* — so A becomes detectably behind through the ordinary
  mechanism. A document loading A then gets either "A is behind, nothing applies to you" (proceed,
  flagged) or "A is behind and it affects the block type you use" (block).

**Falls out of this, flagged now to avoid surprise at format-definition time:** the condition
vocabulary must be wider than "is this doctype X." It has to express conditions about another
standard's behaviour. Cross-standard coordination lives in migration instructions, because the
standard author is the only party who knows what needs coordinating.

---

### C. Execution — NOT STARTED

Requirements are captured below; no model proposed. The three things it must resolve:

- **Authority.** A session modifies only documents it has authority over. A standard delivered in a
  plugin is never modified by a consuming session — its migration belongs to whoever owns the
  plugin and runs in their workflow. The consuming session reports and stops.
- **Where it runs.** Applying migrations inside a working session consumes context and takes
  management of that context away from the user. Provisional direction: **raise the migration and
  offer the choice** — current session for a single owned document with a small fix, a separate
  session or task for anything larger. Default not yet set.
- **Read triggering a write.** A read is use, so a check runs on read. Whether a read may cause a
  *write* is unresolved, and is the operationally uncomfortable point: loading a binder of thirty
  documents should not silently rewrite thirty files. The wrong/old split is the likely answer —
  blocking work applies before use, non-blocking work waits for a save the document was getting
  anyway — but pending non-blocking work must then be reportable rather than silently deferred,
  which is precisely how the old model's on-update work was allowed to never happen.

---

### Requirements schedule

Built this session to score candidate models against. Not yet applied to any model.

**Knowns**

- **K1.** The full dependency-and-version picture for a document exists only at runtime, when it is
  loaded with what it depends on.
- **K2.** Multiple repositories with independent lifecycles; ~790 documents growing 10–30 a week.
- **K3.** A document is composed from several definitions; those definitions are published by
  standards.
- **K4.** Shape changes are rare; improvements are frequent.
- **K5.** Standards arrive via plugins/skills the consuming session does not own.
- **K6.** Runtime observability differs per surface; startup checks are best-effort in chat.
- **K7.** The doctype definition is the only source of truth for which block types a doctype
  currently uses.

**Requirements**

Scope
- **R0.** Change management is defined for standards; extensibility to other item types is a
  nice-to-have, not a constraint.

The migration record
- **R5.** Owner writes the fix; the executor is dumb and carries no knowledge of any specific
  standard.
- **R6.** A version is not published until its migration record is written.
- **R7.** Migration content is held beside the definition, not inside it.
- **R8.** History accumulates; prunable only once nothing is proven to sit behind.
- **R13.** Every version has a migration record, including an explicit "no action."
- **R14.** A migration record is a set of condition-to-action tasks; conditions evaluate against
  definitions.
- **R15.** The migration record travels with the standard.

Detection
- **R4.** Wrong before old: a change making old shape produce a wrong result applies before use; an
  old-result change may wait.
- **R9.** "What is outstanding?" is answerable without opening every document.
- **R16.** Detection is bounded by what is observable where it runs, and states its own scope. A
  clean result means "nothing outstanding among what I could see."
- **R17.** Detection is read-only; it never modifies a document.
- **R18.** Where required standards are absent, documents are not modified.
- **R19.** Severity is per task, not per version.
- **R20.** A cheap summary answers "could blocking work apply here" without evaluating the full task
  set.
- **R21.** A standard behind its own declared dependencies is a detectable state.

Execution
- **R1.** A session modifies only what it has authority over; plugin-delivered content is reported,
  never modified.
- **R2.** Migration is raised in the workflow and automated — never silent, never hand-edited.
- **R3.** Execution never consumes the working session's context without the user choosing it.
- **R10.** Preserve unrelated content; fail visibly rather than guess.
- **R11.** Migration alone creates no Decisions entry.

Whole
- **R12.** The model is statable in thirty seconds.

---

### From the old methodology — keep unchanged

Assessed against the full decision chain in the Capabilities core binder. The user's suspicion that
this is an application problem more than a design one is largely borne out: the mechanism was
designed, declared fifty-five times, and never asked to do anything.

- **Owner authors the transition; the executor is dumb.** Right, and now R5.
- **Transition shape** — version, statement of change, ordered items, success condition. Exactly
  what an executor needs. Keep unchanged.
- **Positive declaration; never infer deltas by diffing definition text.** Right and load-bearing.
- **The checkpoint records *proven* conformance, not the version that happens to be installed.**
  Subtle and right.
- **Stepwise durable, records partial progress.** Required for any batch execution.
- **Authority boundary** — mutate only what you own, report the rest. Already the correct answer to
  the plugin-ownership problem in C.
- **"Preserve unrelated content; do not rewrite merely to make the document look newer."** The
  single most important sentence in the old migration material, currently buried as one item inside
  one transition. **Promote to a standing rule.** An AI sweeping a document will want to violate it
  on every pass, because tidying always looks like improvement.
- **Fail visibly rather than guess** where declarations are contradictory.
- **Migration alone creates no Decisions entry.**

**What actually failed, stated plainly.** Not the runtime-observation premise, which is sound. Three
things: severity was moved from task level to release level; non-blocking work waited for a save
that frequently never came, with no way to ask how much was outstanding; and the result was declared
the designed steady state, which closed the question rather than answering it. Across the visible
binder set: roughly fifty-three transitions declared "no action," exactly one on-update, exactly one
required, and no evidence any document ever traversed either.

### Considered and withdrawn this session

Recorded so it is not re-proposed. A **change-time push model** was worked at length — sweep the
corpus when a definition changes, converge before commit, treat the stamp as evidence rather than
trigger. It was withdrawn on two grounds the user raised: it cannot reach documents in project
repositories with independent lifecycles without manual per-repository tracking, which is the
original problem wearing a different hat; and runtime observation gets that case right for free,
because the check costs nothing when the material is already loaded. What survives from it is the
audit use — a wide check is how you learn it is safe to prune migration history (R8) — and that is
now the open question at CM-Q3.

### Owed next

1. Close **CM-Q3** — is a wide check part of the model or a later convenience.
2. Confirm **CM-Q4** once CM-Q3 lands.
3. Work **execution (C)** against the requirements schedule.
4. Then score the resulting model against the full schedule, honestly, pass/fail per requirement.

---

## 12. Filter rules

Unchanged from v2. The eight-question sieve; disposition per item is moves as-is / moves reshaped /
left behind. Owner = whoever knows the most. Live why stays with the current document; historical
why goes to Decisions.

---

## 13. Folder structure

Unchanged from v2. `AIDE/documentation/` holds all AIDE documentation; `_rebuild/` holds this
rebuild's working docs; `documentation_old/` is the previous corpus, source to mine not to edit.
`_rebuild` docs need not conform to full spec but use simple visible versioning.

Adds this session: an **Infrastructure** folder under the documentation root for tool masters, and
an **`_tools`** folder at the documentation root for running instances.

---

## 14. Open questions

Carried from v2: Q1 Brief/Considerations boundary (parked); Q2 container names — Working Practices
name collision (workflow map vs portable conduct conventions), one must be renamed; Q3 process
container split by mode (no for now); Q4 acceptance testing placement (deferred); Q5 AIDE containers
(confirmed by filter); Q6 built/deployed artefacts under documentation (open, case by case); Q7
Build-branch outcomes (not yet worked); Q8 Deployment and Principles survival as containers (open);
Q9 binder scope declaration form (open).

Added this session:
- Overview returns as a discussion — topic-or-corpus-scale TLDR is the case to test.
- Deployment placement deferred until its behaviour is known.
- Standard-length vs design-length Decisions variants both drafted; confirm which is canonical when
  the doctype set is built.
- Change management CM-Q3: is a wide corpus check part of the model, or a later convenience? Decides
  whether a sweep exists in the design at all. (§11a)
- Change management CM-Q4: does detection produce a work list or a flag? Follows CM-Q3. (§11a)
- Change management: execution is not started — authority, where migrations run, and whether a read
  may cause a write. (§11a)
- Change management CM-Q2 form: one conformance stamp per standard, or one combined? Falls out of
  execution. (§11a)
- Does each remaining component have a stated one-line task? Needed before its contents can be
  filtered.

---

## 15. Next actions

1. Fold the two variant Decisions drafts into the rebuild corpus when the doctype set is authored.
2. Revise VersionCleanup for draft-state grouping and key validation.
3. Revise versioning documentation for the draft model.
4. **Close change-management CM-Q3 and CM-Q4, then work execution** (§11a) against the requirements
   schedule; score the result pass/fail per requirement. First substantive item for the next
   desktop session.
5. Block-catalogue filter — Tags / References remain parked pending their consuming components;
   Dependencies resolves out of change management (§11a) once execution settles the stamp form.
6. Then versioning session (version metadata, migration state, change summaries are all blocks).
7. Name the one-line task for each remaining component, then filter its contents against it.
8. Run the filter over documentation_old, document by document.
9. Author the new corpus at deployable length.
