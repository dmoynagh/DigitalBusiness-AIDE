# AIDE Rebuild — WIP

> **Version 4** (2026-09-05). Adds the change-propagation and migration work: the two-layer filter,
> the migration model, the standard-grained dependency correction, the two identified flaws, and the
> blank-page migration brief. Working document — does not conform to the full documentation
> methodology by design.

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
- **Change propagation and migration** — the model, standard-grained dependencies, open flaws.
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

## 11a. Change propagation and migration — WORKED, NOT CLOSED

### The two-layer filter (applies corpus-wide)

Everything in the old corpus exists to perform a task. The filter therefore runs in two layers:

1. **Name each component's task in one line.** Its reason for existing.
2. **Test its contents against that line.** Anything that does not serve the stated task is stripped
   or moved.

Sharper than "is this useful," because almost anything looks useful. DocMeth's line, worked and
essentially settled: **provide clarity and structure so documents are navigable and their content is
predictably placed, delivered through doctypes and block types.** Everything in DocMeth must serve
navigability or predictable placement. This is the reasoning that already justified cutting
inheritance, abstract doctypes and the push model — mechanism that did not earn against the purpose.

### The problem

A doctype or block-type definition changes. Existing documents were built to the old shape. How
does a document know it is behind, and how does it catch up?

Two cases, genuinely different:

- **Definition improved, shape unchanged.** Sharper guidance, a new rule. Old documents remain
  valid; the next one written is better. No action owed. This is the "None" posture that filled the
  old corpus's migration lists.
- **Shape changed.** Fields added, a section split, a restructure. Old documents are structurally
  behind and work is owed. This case is the entire reason Dependencies and Migration exist.

### Scale — why this cannot be manual

Approximately **790 files** in the repository; the binder set alone about 1.4 MB. Add development
projects at one or two a week, each carrying ten to fifteen documents, and the corpus is in the
thousands quickly.

**Consequence:** manual catch-up is not a fallback, it is a non-starter. And the governing test,
stated by the user: *anything defined in these tools and this architecture is there to make life
easier — it should just define it and the system takes care of it, otherwise there is no point
having it.* A migration system that only detects drift and leaves a thousand documents to fix by
hand has failed its own reason for existing. Detection alone is not the deliverable; closing the gap
is.

### The model

Stated at TLDR length, per the user's rule that if it cannot be summed up simply it is probably
already too complicated:

> **A definition has a version. A document stamps the version it was built to. Current differs from
> stamp, the document is behind, which triggers a migration. The change that moved the definition
> carries migration instructions specific enough for Claude to execute against the document. Claude
> applies them, restamps, done.**

Key properties:

- **Fully autonomous by default.** No human in the propagation path. This was already the old
  model's design and it is correct; an earlier proposal in this session to sort migrations into
  mechanical / assisted / judgement tiers was **rejected** as reintroducing complexity the model had
  already designed out.
- **The human's role is upstream only.** When you make the definition change, you write the
  migration instructions alongside it. The discipline: *a shape change is not complete until its
  migration instructions are written.* After that it propagates unattended across thousands of files.
- **Self-testing.** If a change cannot be expressed as executable instructions, that is the signal it
  is a genuine judgement-level restructure — the rare exception, handled by hand.

**Parked design concept (not built):** the migration spec may optionally carry a **judgement
placeholder** that prompts the human for a specific decision. Off by default, not a stage everything
passes through — a feature of the spec, not a tier in the pipeline. Expected to be rarely if ever
used; parked per the demonstrated-requirement rule, to drop in when a change first genuinely needs
it.

### Dependency granularity — the standard, not the definition

An initial framing that documents depend on their doctype was **too shallow**, then corrected twice.

Wrong (too shallow): a document depends on its doctype; doctype version moves, document migrates.

Wrong (too fine): a document depends on its doctype and every block in its composition tree,
enumerated in the footer. Correct in principle, but the fan-out is enormous and the footer
bookkeeping becomes heavy.

**Correct, and how the old system actually worked:** a document depends on the **published
standard** that publishes the definitions it was built under — not on individual doctypes or block
types. A document built using anything under the Capabilities standard registers one dependency: on
Capabilities.

Consequences:

- **Migrations group at the standard.** Change a doctype or block; its migration attaches to the
  publishing standard's migration set. The standard's version moves.
- **The cascade runs on standards.** A thousand doctypes may live across fifteen or sixteen
  standards, so the whole corpus check is fifteen or sixteen version comparisons, not thousands.
- **The fine-grained tree stays internal** to each standard — the standard's concern, not something
  every document enumerates.
- **Standards declare their own dependencies**, and documents inherit them, giving a broad cascade
  through the existing model.
- A document may depend on **multiple standards** (DocMeth, Capabilities, whatever context applies).

### Identified flaws (open)

**Flaw 1 — dependency lists are a save-time snapshot.** A document records the dependencies that
existed when it was written. Add a block to a doctype later and existing documents do not know they
have gained a dependency. The footer can under-record; a stamped list is only as current as the last
save.

*Largely mitigated by standard-granularity:* if the addition happens **within** a standard the
document already depends on, the tie already exists — the standard version moves and the document is
flagged. The residual gap is only the rare addition made **outside** any standard the document
already depends on. Either lived with, or handled explicitly by the standard.

**Flaw 2 — a document is built from multiple definition sources.** Not one tree but several
overlapping ones, layered onto a single document. The dependency picture is the union.

**The heart of both:** a document's true dependencies are a **derived fact about the definitions**,
not a static list the document carries. A footer snapshot freezes something derived.

### Direction to explore (not decided)

**Resolve dependencies at check time, not save time.** Do not trust the footer as authority;
recompute the document's true dependency set from the current definitions when the migration check
runs, and treat the footer as a cache for change detection rather than the source of truth. This
kills flaw 1 outright and handles flaw 2 naturally as multi-root resolution. Open question is whether
it is affordable at scale.

### Change-trigger research (prior, to be reused)

Earlier platform testing established that **plugin version changes were difficult to detect**, but
**skill version was detectable through metadata**. The conclusion drawn was that checking whether a
set of standards had changed was more reliable than chasing a single plugin value against an ambient
"last plugin applied" value, which became messy. Different trigger points exist and are observable to
different degrees per surface; the design must anchor on what is actually observable, not on a
clean-paper assumption.

### Owed — blank-page migration brief

User's assessment: the existing migration methodology is probably **not bad** — it may be an
application problem rather than a design one. Permission given to step back and reconsider from a
blank page, defending neither the existing model nor the one proposed in this session.

Required shape of that piece:

1. The problem, in a few lines.
2. The considerations — scale; multi-standard layering; snapshot versus derived; change trigger
   points and what is actually observable on each platform.
3. A proposed model and a thirty-second methodology.
4. Where it is forced to compromise, and what those compromises cost.
5. Explicit flags where the existing methodology is already right and should not be touched.

Written to be argued with, in the register of the handoff analysis. Constraint from the user:
**model first, limits second** — do not open by restricting cascade scope; find the model that does
what was wanted, and only then consider compromises.

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
- Migration: is resolve-at-check-time affordable at scale? (§11a)
- Migration: how is the out-of-standard-scope addition handled — lived with, or explicit? (§11a)
- Does each remaining component have a stated one-line task? Needed before its contents can be
  filtered.

---

## 15. Next actions

1. Fold the two variant Decisions drafts into the rebuild corpus when the doctype set is authored.
2. Revise VersionCleanup for draft-state grouping and key validation.
3. Revise versioning documentation for the draft model.
4. **Write the blank-page migration brief** (§11a) — problem, considerations, model and
   thirty-second methodology, compromises and their cost, plus flags where the existing methodology
   is already right. First substantive item for the next desktop session.
5. Block-catalogue filter — Tags / References remain parked pending their consuming components;
   Dependencies resolves out of the migration brief.
6. Then versioning session (version metadata, migration state, change summaries are all blocks).
7. Name the one-line task for each remaining component, then filter its contents against it.
8. Run the filter over documentation_old, document by document.
9. Author the new corpus at deployable length.
