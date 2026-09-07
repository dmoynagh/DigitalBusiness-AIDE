# AIDE Rebuild — WIP

> **Version 12** (2026-09-07). Item 8 per-component design review begun. Principles
> reviewed: design pass complete, standard pending the Standards definition — see
> §15c. Session also settled the three-layer authoring model (design / decisions /
> lean standard), the standard-authoring quality bar, separate-AI review of each
> authored standard as a standing step, incremental per-component output into the new
> system via binders, and Project Design + Standards as the next two components.
> Working document — does not conform to the full documentation methodology by design.

**Location:** `AIDE/documentation/_rebuild/`
**Status:** Active working document. Archive when the rebuild completes.

---

## Contents

- **Purpose and scope** — why this document exists, what the rebuild is.
- **Method** — parallel rebuild through a filter, not in-place edit.
- **The lifecycle model** — unchanged from v2, not yet written up.
- **The design half** — unchanged from v2, not yet written up.
- **AIDE scope and containers** — open; depends on Q8 (which containers earn their place). Not written.
- **Structure vs transport** — unchanged from v2, not yet written up.
- **Infrastructure** — machinery that acts on the corpus; the tool work.
- **Deployment** — parked; custom single-instance deploy.
- **Rebuild-wide policy** — set aside anything without a demonstrated requirement.
- **Decisions doctype** — reworked definition, closed.
- **Doctype / block-type model** — composition, what was cut.
- **Block catalogue** — the universal blocks, closed and parked.
- **Versioning model** — identity, drafts, publish, filename.
- **Format and rendering model** — fields, compact, per-format mapping, portability flag.
- **Change management** — settled end to end: migration records, read-time detection, execution and commands, schedule scored.
- **Filter rules** — the sieve for passing old material into the new structure.
- **Folder structure** — repo layout for the rebuild.
- **Open questions** — parked, to resolve during the rebuild.
- **Next actions** — where to pick up.
- **Item 7 progress** — component naming: standing rules, purpose lines, candidates, open items.
- **Cross-session items** — Stage 0 deliverable and marketplace-add question.

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
- **Stage 0 deliverable** scoped in a separate session (2026-09-03) — see §15b.

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

**A doctype includes a block as defined; it does not modify it.** A doctype may not suppress a
block's fields, add fields to it, or otherwise adjust its shape on inclusion. Defining a derived
block type that overrides a base is the same design in another form and is equally excluded. Where
two doctypes need different shapes, those are two blocks, which may share a smaller common block —
composition, not override. Added on review (v8): override-on-include is inheritance under another
name and brings back what the cuts below removed — precedence when two doctypes adjust the same
block differently, drift when the base changes underneath, and a reader unable to tell what shape a
block actually has here. The accepted cost is duplication between near-identical blocks, which is
visible; override chains are not. Revisit on a demonstrated case per §6c (the demonstrated-
requirement rule).

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
- Markdown: a single delimited line, fixed field order (title, doctype, identity, date),
  delimiter ` | `. Pipe chosen over middot and semicolon: ASCII, no collision with title text, and
  it reads as structure rather than punctuation. Revisit only if a renderer treats the line as a
  table.
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

**Dependencies** — the standards this document is built on, and the version of each it was last
brought into line with. Closed this session; resolved by the change-management work (§11a).
- Field form: a flat list of `standard@version` pairs, one entry per standard.
- Contents: direct and inherited standards alike, listed explicitly and not distinguished. Flat and
  self-contained so detection reads one field and needs no graph walk.
- The version is a **conformance stamp** — what the document reached — not a constraint. No presence
  levels (`!`, `!!`) and no exact pins (`@!vN`); those were runtime-availability concerns and belong
  to deployment currency, which the change-management work separated out.
- A document does not list its own identity's standard; identity carries that version.
- **Placement: header, immediately after Declaration, before Contents.** Moved from the footer
  position the old model used. The currency check gates use, so a partial read from the top must be
  able to answer "may I use this" without reading to the end — which is the boundary-proximity
  principle applied to the consumer that runs first.
- Kept a separate block rather than folded into the Declaration: Declaration is fixed, compact and
  not overridable, and a variable-length list would change its character.
- Name: `Dependencies` retained over `Implements`, `GovernedBy`, `Uses` and `Conformance`. The word
  carries the necessity — the standard must be present for the document to function — which is what
  CM-Q6 (no modification where standards are absent) turns on. The value's shape changed, so no
  reader will mistake it for the old field.
- Markdown: `Dependencies: A@vN, B@vN` — pipe separates Declaration fields, comma separates list
  members, so the two header lines are visibly different shapes.
- Structured formats: a `dependencies` key as a sibling of `aide`, holding the list.

Structural blocks total four: Declaration, Header, Body, Footer. Contents and Summary place into
Header. Body is between Header and Footer.

### Parked (need a case through the filter)

**Parking confirmed this session.** These blocks exist to serve downstream machinery — drift
detection, classification, citation. Until the components that consume them come through the filter
and demonstrate the need, there is nothing to anchor the decision to; deciding now would be deciding
ahead of requirement. They return when the component that needs them does. (Dependencies has since
been closed — see above and §11a.)

- **Tags** — footer property, AIDE_Tags-owned.
- **References** — footer, citation without conformance semantics; "related reading." Was to be
  decided with Dependencies; that dependency is now discharged, so References can be taken on its
  own merits when its consumer appears.
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

## 11a. Change management — SETTLED

Reworked from a blank page this session (2026-09-06), per the brief this section commissioned in
v4. The v4 content is superseded; what survives from it is noted inline.

### The split that unblocked it

The subject had been running as one problem and behaving like a spider's web. It is three:

- **A — Change definition.** What changed, in which version, and what the fix is.
- **B — Detection.** Which documents are behind, and how that is known.
- **C — Execution.** Who applies the fix, where, when, and with what authority.

Every attempt to settle one moved the other two. The old corpus fused them as well: the Dependencies
footer line carried both a conformance fact (B) and a runtime-presence level (C). Separated, each is
tractable. **All three are now settled** (see the SETTLED headers below).

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
  ever executed. **The gate is a presence check** — a record exists for the version being published,
  and it is either a set of tasks or an explicit "no action." Whether the tasks are *correct* is not
  checkable by anything, which is why the check is cheap and still worth having. It lives in the
  publish operation, not in a separate tool, and **has no override**: an override would be used
  exactly when someone is in a hurry, which is when the record is most likely to be forgotten, and a
  missing record is invisible afterwards because absence looks identical to "nothing to do." The
  accepted cost is that publishing is slightly heavier every time, including for the many versions
  whose honest answer is "no action" — the right trade, since fifty-three cheap records beat one
  silently missing one.
- **Every version has a record, including "no action."** Positive declaration. Absence is ambiguous
  (nothing changed, or the author forgot); presence is a fact. Retained from the old model's
  positive-posture rule.
- **A task has three parts: condition, action, success check.** Revised on review (v8); previously
  stated as condition-to-action only, which left "succeeded" undefined and made the atomic-write
  rule rest on nothing. A standard may publish several doctypes and block types; the **condition**
  decides applicability — *if the document's doctype is X*, *if the doctype uses block type Y* — so
  one migration covers a corpus of differently-shaped documents. The **action** states the work. The
  **success check** states what must be true of the document afterwards, in terms that can be tested
  against it: field present, field non-empty, block present, block absent, value matching a pattern.
- **The success check is authored, not self-assessed.** It is written before the work is done, by
  someone other than whoever applies it, which is why it is worth more than the applier's own
  verdict — the same reason a test written before the code is worth more than one written after.
  Nothing is written to the document until every applicable task's check passes.
- **A task whose success cannot be stated as a checkable outcome is not a migration task.** That is
  the same self-test as the one below: if the change cannot be expressed this way, it is a
  restructure and belongs with a human.
- **Form: structured conditions and success checks, prose actions.** Conditions and checks are
  evaluated mechanically and must be machine-readable. Actions are carried out by an AI, so prose is
  correct — forcing them into structure would amount to building a transformation language, which is
  the over-engineering to avoid.
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

### B. Detection — SETTLED

**The question detection answers:** does this document need work under the current standards, and
what work.

**Runtime is the only complete picture.** A document loaded for use is loaded with the things it
depends on; that is the only moment where document, applicable standards, their versions and their
migration records all exist together. This was the premise of the original methodology and it is
correct. It also composes without tracking: a document in a repository untouched for eight months
is checked the moment it is next used, and nobody had to remember that repository existed.

**Read is use.** If a document is read, a currency check runs.

Six detection questions were worked (numbered CM-Q1 to CM-Q6 to avoid collision with the Q-series in
§14, the rebuild-wide open questions). All six are now closed.

**CM-Q1 — which standards apply to a document?** *Settled: declaration, repaired by migration.*
Derivation from doctype is truer; declaration is the practical compromise. The known risk of
declaration is a stale association — a doctype moves from standard A to standard B and the
document's declared dependency no longer reflects reality. That is repairable by an ordinary
condition-to-action task in A's migration: *if doctype is X, add standard B as a dependency*. So
declaration stops being lossy, at declaration cost. **A corpus-wide "global action" that all
documents check regardless of standard versioning was considered and rejected** as a second
mechanism sitting permanently in the check path; the demonstrated-requirement rule (§6c) applies.
Revisit only if a case forces it.

**CM-Q2 — what was the document last brought into line with?** *Settled: the Dependencies block, one
`standard@version` pair per standard.* The document must carry this; nothing else remembers. A
single whole-document value was ruled out by the cross-standard case, where each standard is used at
its own current available version independently — one value cannot express A at v4 while B is at v6.
Conformance version and dependency declaration are held in **one field**, not two: two lists over the
same set can diverge, and a conformance entry for a standard you do not depend on says nothing.
**The field is machine-findable** — fixed header position, predictable shape — so a named-scope
operation or any later wide scan can read it without parsing whole documents. Full block definition
in §9 (the block catalogue).

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

**CM-Q3 — is a wide corpus scan part of the model?** *Settled: no.* Worked from what a wide scan
would be *for*. Three candidate purposes: correctness, pruning, planning.

- **Correctness does not need it.** An unused document has no impact whether it is ahead or behind,
  and blocking work applies before use. Read-time observation is complete for every document at the
  moment that document matters.
- **Pruning does need it** — history can only be pruned once nothing is proven to sit behind the
  pruned version, and the documents you would need to hear from are exactly the ones nobody reads.
  **Pruning is deferred**, so this purpose is not live.
- **Planning is marginal** and never blocking.

With pruning deferred, no purpose remains. **No wide scan in the model.** What is retained is the
CM-Q2 constraint that the stamp stays machine-findable, which costs nothing now and keeps the
pruning option open without retro-fitting later. The named-scope operation in execution (E5) also
provides the means to bring a defined tree fully current on demand, should pruning ever be wanted.

**CM-Q4 — what does detection produce?** *Settled: a work list, per document, at read time.* Sorting
blocking from non-blocking requires knowing which tasks apply, which requires evaluating conditions
against definitions. A cheap summary carried alongside the tasks — *does any version in this range
contain a blocking task?* — answers the cheap question without evaluating the full set.

**Accepted consequence, recorded so it is seen as decided rather than missed.** Non-blocking work is
made visible at read time, but only to whoever is reading. If nobody reads a document, nobody learns
it is behind. This is the same shape as the old model's failure, and it is accepted here for a
reason the old model did not have: the old model deferred work *silently and indefinitely* with no
way to ask, whereas here the information is surfaced every time the document is used, and
`/migrations` (below) lets the user ask deliberately. The residual — documents nobody opens — is
accepted because an unread document has no consumer to harm.

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

### C. Execution — SETTLED

Detection has produced a work list on a document about to be used. Six questions, all closed.

**E1 — who may act?** *Settled: authority is a filesystem fact, not a construct.* A session modifies
documents that are in the tree it is working in and writable. If a document is not writable, the
session may request a writable copy. No ownership register is maintained. A standard delivered in a
plugin is reported, never modified — its migration belongs to whoever owns the plugin and runs in
their workflow.

**E2 — what happens at the moment of detection?** *Settled: notify, then offer the choice.* The user
is told, and chooses whether and where to migrate. If migration is deferred to another session, the
resuming session simply runs detection again — no new mechanism, no state carried.

**Where deferral is permitted, the split is by what the session is about to do:**

- **Reading — may proceed on authorisation.** The migration tasks are shown to the user, who judges
  whether they affect the work in hand. The wrongness affects only what comes out, the user has been
  told what it is, and nothing propagates.
- **Writing — may not proceed.** Saving a document known to be behind authors new content under old
  rules and entrenches it, and the stamp cannot advance because no migration ran. That is not a
  deferred problem but a manufactured one — the corpus is made worse by proceeding.

The proceed-anyway decision is **session-scoped and never recorded in the document**. A persisted
override is invisible and outlives its reason. The accepted cost, confirmed on review: a document
you have deliberately chosen to leave behind will re-prompt in every new session.

**Rejected — the executor evaluates whether the pending tasks affect the work in hand.** Considered
and discarded. It is a correctness call the executor cannot be accountable for, and getting it wrong
produces a document that looks right and is wrong — the silent failure the whole design exists to
prevent. It would also require a model of what the requested work touches, which would be the
largest new construct in the design for the thinnest benefit. The tasks are human-readable and
author-written; showing them to the user puts the decision with the party who can be accountable
for it, and keeps the executor dumb (R5).

**E5 — batch and binder loads.** *Settled: detect fully, then present one decision.* Detection is
read-only (R17), so nothing prevents it running across everything before any execution happens. The
single-document case is then a batch of one — same detection, same report, same decision point, no
special handling.

**Rejected — stop mid-load, migrate, continue.** Interleaves execution with a load already in
progress, consumes context exactly where R3 says not to, repeats per affected document, and needs
re-entrancy and partial-load state. It is the option that feels most helpful and behaves worst.

**Independent of binder methodology.** How binders are built and loaded is not yet defined in the new
system, so execution does not depend on knowing a load in advance. When a migration need is
detected, the user is prompted with two questions:

| | Here | Elsewhere |
|---|---|---|
| **This document** | update in this session | new session — in chat, offer cowork or code |
| **All docs in context** | update in this session | new session — in chat, offer cowork or code |

**Defaults (confirmed):** *this document / this session* for one; *all docs / new session* for
several. Context cost scales with document count, not with the size of any single fix.

**"Docs in context" means the same thing on every surface** — documents currently loaded, evaluated
at the moment of the prompt. No accumulation, no session ledger, no tracking. A document read an
hour ago and since dropped from context is not included; it is caught next time it is read.

**Rejected — a per-surface definition of scope** (chat: context; cowork: context; code: current
repo or wherever write access exists). Two faults. It makes the same phrase mean four documents in
chat and seven hundred in code, which is the corpus sweep re-entering through a prompt option. And
it folds write access into scope, when write access is E1 authority — a gate on whether you *may*
act, not a definition of what is *in* scope.

**Named-scope operation, code only.** Scanning and migrating a whole tree, repository, or other
defined scope is a **directed command, not a detection mode** — the user names the scope, the
executor acts. Nothing runs it automatically or on a schedule. Three constraints: **scope is
explicit and never defaulted** (no implicit "current repo"); it **reports before it acts** (counts
and blocking/non-blocking breakdown, then confirmation, using the same read-only detection); and
**the ordinary execution rules apply unchanged**. This is also what would make pruning possible
later, since a named tree can be brought fully current on demand.

**Migration is an AI task on every surface.** Established on review (v8), correcting an earlier
implication. Because actions are prose written for an AI to interpret, no script can be the thing
that applies them. On code, a script is a *launcher* only: it enumerates a named scope, reads
stamps, sequences the work, collects failures and resumes. The per-document work — evaluate
conditions, apply actions, verify success checks, write — is the AI's on every surface. There is no
verification-strength difference between surfaces; the difference is only how much un-intelligent
surrounding automation exists. This also means "the executor" is one actor, not a script directing an
AI, and the stamp is written by whoever did the work, after the checks pass, in the same operation
as the document.

**Commands.** `/migrations` reports and changes nothing; `/migrate` runs the same detection then
offers the same prompt and acts. In chat and cowork their scope is documents in context, identical
to a read-triggered check — the named-scope operation stays code-only. `/migrate` reuses the E5
prompt rather than replacing it: one path through execution, two entry points. Their value is that
the user can take the initiative rather than only being interrupted, which serves R2 better than
read-triggering alone. This restores the old model's diagnostic/destructive split, which was right.
Names may be revisited if collisions appear.

**E6 — failure partway.** *Settled: transition is atomic; the run banks what completed.* Two levels,
and the distinction matters because "migration" was doing double duty:

- A **transition** is one version step (v28 to v29) containing a set of tasks.
- A **run** is the whole walk (v26 to v29), which is three transitions in sequence.

**Within a transition: all tasks succeed or nothing is written.** There is no stamp value that
describes a half-applied transition — the document is no longer v28 and not yet v29, so any recorded
version is a lie. In practice the executor works on a copy and writes back only on complete success,
so "rollback" means nothing was written; a crash mid-transition is indistinguishable from a failure
mid-transition, and there is nothing to undo. No journal or rollback mechanism is needed.

**Across a run: each completed transition is kept and stamped.** A document at v26 whose third
transition fails ends cleanly at v28, with the failure reported and its reason recorded. Discarding
banked work because a later step failed would mean repeating it on every attempt and never making
progress past one bad transition. This is the old model's stepwise-durable rule, correctly scoped.

Both rules exist to protect one property: **the stamp only ever holds a version the document
genuinely reached.**

**The stamp is written in the same operation as the transition, atomically.** Written separately, a
crash between them leaves a converged document claiming the old version, which is then migrated
twice.

---

### The model in thirty seconds

> **Publishing a standard version requires a migration record for it — condition-to-action tasks
> that carry a document from the previous version to this one, shipped with the standard. When a
> document is read, it is checked: the standards it declares, what it was last brought into line
> with, what is current. Anything that makes the old shape *wrong* is applied before use; anything
> that merely makes it *old* can wait, but is shown every time. The user chooses whether to migrate
> this document or everything in context, here or in another session. Each version step succeeds
> whole or not at all, and the stamp only ever records a version the document actually reached.**

---

### Requirements schedule

Built to score models against; scored below.

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
- **R5.** The mechanism carries no standard-specific knowledge — everything specific to a standard
  lives in its migration record, so the mechanism never needs updating when a standard changes.
  *(Reworded on review; previously "the executor is dumb," which misdescribed it — see R23.)*
- **R23.** The action fully describes the work to be done. The executor carries out what the action
  states; it does not infer intent, fill gaps, or improve on the instruction. Reasoning is used in
  service of applying the action as written — resolving how to express the change in this document's
  format, or locating where the action's target sits — not in deciding what the work is. Where an
  action requires judgement, it must say so explicitly. This is the principle behind R10.
- **R6.** A version is not published until its migration record is written.
- **R7.** Migration content is held beside the definition, not inside it.
- **R8.** History accumulates; prunable only once nothing is proven to sit behind.
- **R13.** Every version has a migration record, including an explicit "no action."
- **R14.** A migration record is a set of condition-to-action tasks; conditions evaluate against
  definitions.
- **R15.** The migration record travels with the standard.
- **R22.** Conditions are read from the doctype definition and cover inclusion only — *is the
  doctype X*, *does the doctype use block type Y*. **Reduced on review (v8).** It previously required
  a wider vocabulary able to interrogate how a doctype modified an included block. With doctype
  modification of included blocks disallowed in §8, no such case arises and the requirement shrinks
  to what the settled conditions already do.

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

### Schedule scored

Against the settled model. Amber means satisfied by discipline or convention rather than mechanism.

| | Requirement | |
|---|---|---|
| R0 | Scoped to standards | pass |
| R1 | Authority — modify only what you own | pass (E1) |
| R2 | Raised in workflow, automated, never silent | pass (E2, commands) |
| R3 | Never consumes working context unchosen | pass (E2, E5 defaults) |
| R4 | Wrong before old | pass (CM-Q5) |
| R5 | Mechanism carries no standard-specific knowledge | pass |
| R6 | No publish without a migration record | pass — presence check in the publish operation, no override |
| R7 | Held beside the definition | pass |
| R8 | History accumulates, prunable later | pass — pruning deferred, option preserved by CM-Q2 |
| R10 | Preserve unrelated content; fail visibly | pass — backed by R23 (the action is the whole scope of the work) and by per-task success checks |
| R11 | No Decisions entry for migration | pass |
| R12 | Statable in thirty seconds | pass |
| R13 | Every version has a record, including "no action" | pass |
| R14 | Condition-to-action; conditions on definitions | pass |
| R15 | Travels with the standard | pass |
| R16 | Detection states its own scope | pass |
| R17 | Detection is read-only | pass |
| R18 | No modification where standards absent | pass |
| R19 | Severity per task | pass |
| R20 | Cheap summary for the blocking question | pass |
| R21 | Standard behind its dependencies is detectable | pass — near-trivial once doctype modification of included blocks is disallowed; standards are governed documents and are checked on read like any other |
| R22 | Conditions read from the doctype definition, inclusion only | pass |
| R23 | Action fully describes the work | pass — stated as a principle; enforced in practice by the success check |

**R9 — "what is outstanding" answerable without opening every document — is withdrawn.** It was the
requirement the wide scan existed to serve, and it fell with it (CM-Q3). It is now a **stated
limitation**: corpus-wide currency cannot be answered. What can be answered is that every document
used is current, which under the settled model is the only claim that bears on correctness.

**No ambers remain after the v8 review.** Both cleared for reasons worth recording: R10 gained a
principle behind it (R23, the action is the whole scope of the work) and a mechanical backstop (the
per-task success check); R21 shrank once doctype modification of included blocks was disallowed,
since the stale-adjustment risk it guarded against can no longer arise.

**The one gap the review found was success.** The model said a transition writes only if all tasks
succeed, without saying what succeeding meant for an AI applying text instructions — atomic-on-
success with success undefined. The three-part task closes it. Three further review points shrank to
nothing once doctype modification was disallowed, which is the better outcome: the model got smaller
under review rather than larger.

**Standing, by choice: no reconciliation path.** Every comparable system that started lazy later
added a sweep. This one does not, and the correctness argument holds — an unused document harms
nobody. The operability cost is real: migration history can never be simplified, and corpus currency
cannot be stated. Mitigated by the machine-findable stamp (CM-Q2) and the code-side named-scope
command (E5). Debt with a repayment plan, not a hole.

---

### From the old methodology — keep unchanged

Assessed against the full decision chain in the Capabilities core binder. The user's suspicion that
this is an application problem more than a design one is largely borne out: the mechanism was
designed, declared fifty-five times, and never asked to do anything.

- **Owner authors the transition; the mechanism carries no standard-specific knowledge.** Right, and now R5. (The old wording was "the executor is dumb"; reworded on review — the applier reasons, it just does not decide what the work is.)
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
audit use — a wide check is how you learn it is safe to prune migration history (R8) — and with
pruning deferred at CM-Q3 that purpose is not live. What survives is the code-side named-scope
operation (E5), which provides the same reach as a directed command rather than as a check.

### Owed next

Nothing outstanding in the model. Carried forward to the corpus build:

1. **Author the migration-format standard**, carrying the three-part task shape (condition, action,
   success check), the structured/prose form split, R23 (the action fully describes the work) and
   R10 (preserve unrelated content) as hard inputs. Authored with the doctype set, not before it.
2. Land the R6 publish gate wherever the publish operation is defined.

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

Added v8:
- Overview returns as a discussion — topic-or-corpus-scale TLDR is the case to test.
- Deployment placement deferred until its behaviour is known.
- Standard-length vs design-length Decisions variants both drafted; confirm which is canonical when
  the doctype set is built.
- Change management: the migration-format standard is not yet authored; the three-part task shape,
  the structured/prose form split, R23 (action fully describes the work) and R10 (preserve unrelated
  content) are hard inputs. Authoring waits for the doctype set, per the standing sequence. (§11a)
- References block: no longer blocked by Dependencies; decide on its own merits when a consumer
  appears. (§9)
- Does each remaining component have a stated one-line task? Needed before its contents can be
  filtered.

Added v10 (item 7 naming pass):
- §3–5 (lifecycle model, design half, AIDE scope and containers, structure vs transport) are not
  blockers for item 7; downgraded to documentation debt in Contents.
- "Component" confirmed as the single word for the ownership unit. The old
  Capabilities-internal usage (D43, D60, D92) is subsumed.
- Capabilities is a grouping label for now, not a component — revisited if it earns a purpose.
- Q8 (Deployment and Principles container survival) is partly addressed: Deployment is parked with
  a purpose line but deferred mechanism; Principles has a settled purpose line. Neither is closed —
  survival as containers depends on the full picture.
- Tags, Scope, Dependencies form a runtime-machinery cluster with a chain of risk: Dependencies
  shrank under §11a, Scope lost a consumer at CM-Q1, Tags depends on Scope. If Scope falls, Tags
  almost certainly falls with it. All three are candidates with survival open.
- Stage 0 deliverable scoped (2026-09-03 session) — see §15b.
- Open empirical question: whether a CLI-side marketplace-add tracks subsequent merged-PR releases
  automatically, or needs per-release manual action. (2026-09-05 session) — see §15b.

---

## 15. Next actions

1. Fold the two variant Decisions drafts into the rebuild corpus when the doctype set is authored.
2. Revise VersionCleanup for draft-state grouping and key validation.
3. Revise versioning documentation for the draft model.
4. Carry the migration-format standard (§11a) into the standards-authoring pass with the three-part
   task shape, the form split, R23 and R10 as hard inputs; land the R6 publish gate with the publish
   operation.
5. Block-catalogue filter — Tags and References remain parked pending their consuming components;
   Dependencies is closed (§9).
6. Then versioning session (version metadata, migration state, change summaries are all blocks).
7. Name the one-line task for each remaining component, then filter its contents
   against it. **Naming pass COMPLETE — see §15a.** Thirteen components have settled
   purpose lines. Three candidates have draft lines with survival open (Tags, Scope,
   Dependencies). Core is deferred by design. The Capabilities grouping question was
   worked 2026-09-07 and confirmed: it stays a container until a demonstrated need
   forces otherwise. The filter half of this item is folded into item 8.
8. Per-component design and purpose review — in chat, one component at a time. For
   each component: flesh out its purpose, check its approach and design against how
   we now work and what we've learned, confirm it is more than a migration gate, and
   get it into a state that can be properly implemented. This is a design review, not
   just a content filter, and is deliberately kept in chat rather than Claude Code.
   Run the documentation_old filter per component as part of this pass. **In
   progress — Principles reviewed 2026-09-07, see §15c.**
   - Component order: Principles (done, design only) → **Project Design → Standards**
     next, because they define the document types everything else is written in →
     then the remaining components. Standards also answers the authoring bar that
     Principles is waiting on.
   - Output as you go: once a component's design is complete, author its masters into
     the new system and add/update them in that component's binder. The binder is the
     single context-loaded artefact — update one binder, not many loose files. Keep
     outputs small and reviewable rather than one large pass at the end.
   - Standing step: each authored standard is reviewed by a separate AI before it is
     accepted.
9. Author the new corpus at deployable length.

---

## 15a. Item 7 progress — component naming

Working section. Records the standing rules, settled purpose lines, candidates,
new components surfaced, and open items from the item 7 naming pass (v9–v10,
voice sessions 2026-09-07).

### Unit and terminology

**Component** is the single word for the ownership unit — any unit that adds
or extends functionality. It applies at every level. The old
Capabilities-internal usage (D43 "seven top-level Capabilities components,"
D60, D92) is subsumed; the word now means the same thing everywhere.

**Capabilities** is an organisational grouping — a wrapper for components
that extend the development environment (standards, tools, etc.). It is not
itself a component unless it earns a purpose. Components inside the
Capabilities grouping are components in their own right; the grouping is
just filing.

### Standing rules

These govern the whole naming pass and downstream filter work.

1. **Owner is whoever knows the most about it.** Ownership goes to the
   component with the deepest knowledge of the thing. Applies to block types,
   document types, workflow artefacts, and boundary disputes.

2. **Documentation methodology owns structure and mechanics, not content
   definitions.** It defines how documents are built and how the document
   workflow runs. It does not hold a registry of document types belonging to
   other components. The only things that live in methodology are genuinely
   global — a type used across many components where no single component knows
   the most about it.

3. **Each component defines its own block types and document types.** Project
   Design defines objectives, requirements, considerations. Working Practices
   defines work-in-progress, work register. Standards defines what a standard
   is (provisionally in methodology — see open items). Being written down as a
   document does not make something methodology's business.

4. **A purpose line is a filter criterion, not a description.** Its job is to
   reject content. A good line carries an outcome, a consumer, and a visible
   edge. If it rejects nothing from the component's own current documents, it
   was written from the corpus rather than from need.

5. **Mode and interaction pattern are separate axes.** Mode is the
   contract — what role an external AI plays. Interaction pattern (one-shot,
   multi-round, conversational) is how many rounds it takes. Any mode can use
   any pattern. Adversarial/challenge is an approach or style applied to a
   mode, not a separate mode. Adjudication (resolving competing outputs) is a
   role within a workflow, not a separate mode.

6. **Purpose and role first; everything must align to it.** If a piece of
   content cannot trace back to the component's purpose, it is scope creep.
   This is the test that discharges item 7 into item 8 (filter).

### Settled purpose lines

| # | Component | Purpose line | Key boundaries / reject-test notes |
|---|---|---|---|
| 1 | Documentation methodology | Define how documents are structured and created — the generic mechanics. | Not a registry of doc types. Specific types live with whoever knows the most. Provisionally holds the definition of what a standard *is* (see open items). |
| 2 | Standards | Make sure standards are applied, honoured, and kept current across the environment. | Owns use, application, and migration of standards. Does NOT own the document-shape definition of a standard (provisionally methodology). |
| 3 | Migration | Bring a document into line with the current version of every standard it depends on, before it is used. | Rejects: Migration Tool content (migration is an AI task, not a script), wide corpus scan material, presence levels and exact pins. |
| 4 | Review | Give work an independent check by a separate reasoning path, so problems are caught before the work is trusted. | Doesn't own fixing or quality rules. Already has five Types (Check, Inspect, Evaluate, Robust, Stress Test) — the challenge/adversarial concept is covered by Robust and Stress Test as approach, not a separate mode. |
| 5 | Research | Get an answer to an open question by putting more than one AI on it and pooling what comes back, so the result is stronger than any single pass. | Convergent — pools toward one answer. Distinguished from parallel solutioning (which keeps answers apart). NEW component. |
| 6 | Parallel solutioning | Get two or more AIs to each produce their own design from the same brief, independently, so different approaches can be compared before committing. | Divergent — deliberately keeps approaches independent. Resolution (picking the winner) is a separate flexible role: human, lead AI, or both depending on automation level. NEW component. |
| 7 | Consultation | Bring an external AI in to discuss something you're working through — a single question or an evolving thread — so its input shapes your thinking. | Defined by the ownership test: primary actor retains ownership of the work; external AI advises without owning the outcome. Renamed from "contributory input." NEW component. |
| 8 | Messaging | Carry a message between AIs reliably — across sessions, platforms, or models — with a known envelope and confirmed receipt. | Owns the envelope and receipt. Does not own message content (sender's job) or route selection (platform transport). |
| 9 | Principles | Give any AI the durable, portable reasoning and interaction premises to think and act well — independent of platform or methodology. | Portability is the defining test. If a candidate principle only makes sense inside AIDE, it's not a principle — it's methodology or working practices. |
| 10 | Working practices | Own the workflows and behaviours for getting work done — including work-in-progress, work registers, and how design and build hand over — whatever the task. | Owns workflow artefacts end to end, definitions included. WIP and work register are NOT methodology's business. Divisional boundaries with project design and build to be resolved by "knows the most." |
| 11 | Project design | Produce a coherent specification for work of any size — one scalable architecture from simple single-document to complex multi-document structures. | Defines its own block types (objectives, requirements, considerations) and document types. Does not need to know about build. Handover mechanics belong to working practices. |
| 12 | Build | Take defined work and execute it — produce the outcome, report what was done. | Generic core plus specialised paths by work type. Core-vs-path ownership boundary deferred for "knows the most." Handover loop goes to working practices. |
| 13 | Tools | Encapsulate a repeatable invokable action — anything you'd "run" rather than "follow" — so its mechanism and safety checks aren't re-derived each time. | Heart is the invocability test (D24, the standard-tool boundary): "if you would say 'run X,' X is a tool; if you would say 'follow the approach in Y,' that is a standard." NOT limited to executable code — migration is a tool and it's an AI task. |

### Candidates — survival open

These have draft purpose lines but their survival as standalone components is
unresolved. All sit in the runtime-machinery cluster. There is a chain of
risk: Dependencies shrank under §11a (the change-management model), Scope lost
a consumer at CM-Q1 (document-applicability answered by declaration), and Tags
depends on Scope. If Scope falls, Tags almost certainly falls with it.

| Candidate | Draft purpose line | Flag | Trigger to resolve |
|---|---|---|---|
| Tags | Attach machine-readable labels to items so they can be selected by query. | Highest risk — only demonstrated consumer is Scope's machine layer. Block already parked (§9). | Resolved when Scope resolves, or when another consumer demonstrates a need. |
| Scope | Decide whether a given standard, tool, or rule applies in the current situation, so the AI only follows what's relevant. | One of two consumers removed by CM-Q1 (declaration model). Remaining consumer is runtime applicability. | Work through what actually needs runtime applicability; the answer falls out. |
| Dependencies | Let a document declare which standards it depends on and at what version. | Moderate-to-strong risk of not being a component. §11a reduced it to one block, one field. | May resolve as a block owned by whoever owns change management, not a standalone component. |

### Deferred

| Component | Reason | Trigger |
|---|---|---|
| Core | Cannot be judged until everything else has declared what it needs. Core is defined by leftover shared requirements that have no natural home elsewhere. | Resolve last, after all other component purpose lines are settled. |
| AI Deployment | Parked (§6b). Purpose line settled: "Get the finished standards and behaviours live in a session, on whatever surface is in use." Mechanism deferred — will be hand-written, single-instance. | Revisit when mechanism is designed. |

### Capabilities grouping — worked 2026-09-07

Worked as the final item of the naming pass. Confirmed: Capabilities stays an
organisational wrapper, not a component. It earns no purpose line at this stage
because it does no work of its own — every job it could claim is already owned
by a component inside it. Kept provisional under the demonstrated-need rule: if
it later shows a purpose of its own, it graduates to a component then. No
container-tree or ownership consequences were decided in this pass.

### New component candidates — parked

| Candidate | Description | Status |
|---|---|---|
| Decomposed collaboration | Different AIs solve different parts of a larger problem, then results are assembled. | Real pattern. Parked — no demonstrated need for a solo developer. |

### Open items from this pass

1. **Standards definition placement.** Where the concept of a standard, and its
   document type, is defined — methodology or the standards component.
   Provisionally in methodology (it's a document-shape question; sits naturally
   beside other doc-type definitions). Leaning toward capabilities. Review once
   the full standards side is worked through.

2. **Divisional boundaries: project design / build / working practices.** The
   handover between these three has plausible ownership claims from each side.
   Parked for "knows the most" once all three are named and side by side.

3. **Build specialisation paths.** Where the boundary sits between build's
   generic core and each specialised path, and whether a given path is owned
   inside build or by the component that knows that output type.

4. **Consultation external review.** A prompt was sent to an external AI asking
   whether consultation is a coherent distinct mode or collapses into another.
   Response received and triaged:
   - **Accepted:** the ownership test (who owns the outcome) as the defining
     boundary; separating mode from interaction pattern.
   - **Accepted with caution:** three proposed new modes (decomposed
     collaboration, adversarial challenge, adjudication). Challenge is already
     covered by Review's Robust and Stress Test types. Adjudication is the
     resolution role already noted in parallel solutioning. Decomposed
     collaboration is parked as a genuine pattern without demonstrated need.
   - **Rejected:** the four-axis model (mode, topology, lifecycle, integration)
     — over-engineering.
   - **Accepted:** rename from "contributory input" to "consultation."

5. **Core's eventual scope.** The previous Core design material (index, domain
   resolution, bootstrap, platform) is held as reference, not commitment. When
   another component surfaces a shared requirement with no natural home, check
   it against what Core originally proposed. Consideration only.

---

## 15b. Cross-session items

Items from other sessions that belong in the WIP so it holds all current work.

### Stage 0 deliverable (scoped 2026-09-03)

Three artefacts:

1. **Always-on bundle** — Principles, Working Practices, human working model.
   Deployed to: claude.ai project instructions, user preferences, CLAUDE.md,
   ChatGPT project.
2. **One plugin with five skills** — Messaging (known-good control), Review,
   DocMethodology, Standards & Tools, currency probe.
3. **Written acceptance test.**

**Exclusions:** Tags, Scope, Dependencies, Migration (all pre-filter or
unresolved), the whole AI Deployment mechanism, the production chain, plugin
commands/agents/hooks/MCP.

**Naming constraint:** must not carry the AIDE_Core set identity or a release
number the real production chain will want.

### Marketplace-add empirical question (noted 2026-09-05)

Open question: whether a CLI-side `marketplace-add` tracks subsequent
merged-PR releases automatically, or needs per-release manual action. To be
tested empirically.

---

## 15c. Item 8 progress — per-component design review

Per-component design and purpose review (item 8). One component at a time, in
chat. Records what each pass settled and what remains before the component can
be signed off.

### Three-layer authoring model (applies to every component)

Settled 2026-09-07 while reviewing Principles; general to the rebuild.

1. **Design document** — elaborates each element: what it is, and the reasoning
   for why it exists. Depth and clarification live here.
2. **Decisions** — records the thinking and valuable knowledge worked through to
   get there, as normal.
3. **Standard** — the published artefact. Hard bar: extremely brief and
   concise, because it is loaded into memory and applied constantly alongside a
   stack of other standards. No bloat, no restating, nothing superfluous —
   **but brevity is never bought at the cost of what the standard is trying to
   achieve.** Lean and accurate, both. This authoring bar is itself an input to
   defining the Standards component.

**Standing step:** each authored standard is reviewed by a separate AI before
acceptance, to confirm it implements the design in a form that is usable and
lean.

**Sign-off rule that falls out of this:** a component's design pass being
complete does not sign the component off. Sign-off waits until its standard is
authored (which needs the Standards component defined) and cross-reviewed.

### Principles — reviewed 2026-09-07 (design pass complete)

**Purpose line — confirmed.** Give any AI the durable, portable reasoning and
interaction premises to think and act well, independent of platform or
methodology. The defining test is made explicit: **portability = universality**
— does the premise hold outside AIDE, yes or no. Anything true only inside AIDE
is not a principle; it drops to working practices. "Interaction" stays, because
a universal interaction premise is still a principle. The real filter is
"independent of platform or methodology."

**Elements.** Nine premises remain.

- Eight pass the universality test cleanly (value over compliance; purpose
  before mechanism; model before elaboration; keep the working set
  comprehensible; observation over prediction; loud failure over quiet
  absorption; verified truth over plausible assertion; confirmed state over
  assumed state).
- **P5 (authoritative evidence over incidental inference)** — premise is
  universal and the existing statement already passes the test as written; it
  needs no rewording. The only change is presentational: its examples are
  AIDE-specific (declared/member-project relationships, `AIDE_Domain`, folder
  proximity and Domains), so they are demoted clearly to illustration beneath
  the premise rather than reading as part of it. Note P5 already carries D7 —
  it replaced the original seed wording "Domains are declared, not detected."
- **P6 (information holder decides the boundary)** — MOVED to working practices.
  As written it is about which component/project/domain answers a boundary
  question — AIDE-context behaviour, not a universal premise.

**Guidance Profiles** — the Add / Refine / Override delta model. MOVED to
working practices for now, to be reviewed when working practices is worked.

**Start that review from the existing decisions, not from scratch.** D4 sets the
delta model (profiles may Add, Refine or explicitly Override named base
guidance; unmentioned base guidance stays effective; equal-specificity
contradictions fail visibly). D5 already answers the "where does it live"
question: Principles and Working Practices share the same conceptual profile
model, and **no new top-level profile component is created yet** because those
two are the demonstrated consumers. That decision stands unless something
overturns it.

The open question that travels with it is therefore not placement but
**whether the profile model earns its place at all for a solo developer** — the
demonstrated-need rule (§6c). D5 assumes organisation/group/team/user profiles
as consumers; a solo developer may have none of those.

**Status: design pass complete; everything above pending the next update.**
Principles cannot be signed off until its standard is authored against the
authoring bar (needs Standards defined) and cross-reviewed by a separate AI.

