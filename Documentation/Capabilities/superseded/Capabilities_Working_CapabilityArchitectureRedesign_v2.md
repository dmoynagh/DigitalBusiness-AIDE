# Capabilities — Working — Capability Architecture Redesign

> **Working version 2** (2026-09-02). Extends the preserved Capability architecture redesign with
> confirmed Knowledge semantics, platform-agnostic Working Context architecture, Topic Binder
> refinements, and retained OpenAI deployment evidence from the August 2026 empirical tests. This is
> continuation/design state, not yet an issued canonical Standard. `Capabilities_WIP_v17` points to
> this document as the detailed active working record.

## Current position

Programme:

`AIDE Architecture — Peer Review Programme`

Completed:

- `Review A — Core substrate` — Complete at High.
- `Review B — Documentation/work-state model` — Complete at High.
- `Review C — Capabilities semantic architecture` — Complete at High.

Held:

- `Review D — design-to-production` — **ON HOLD**. Its previous baseline is stale because the
  Capability production/build model and AI Deployment seam are being materially redesigned.

External active WIP:

- **AI Deployment** — active design work in another working context. Coordinate through handoff while
  overlapping work remains active; obtain a return handoff when its design is finalised.

Current Capabilities work:

- blank-sheet redesign of Capability definition, element production, release/versioning, migration,
  Capability Build, package production and post-build handoff;
- cross-topic workflow/documentation architecture consequences discovered during that redesign.

## Confirmed Capability model

### Capability and Capability Elements

- **Capability** — coherent functional component/area, for example Messaging.
- **Capability Element** — constituent part of a Capability.
- **Capability Element Type** — type/kind of Element. Initial types are `Standard` and `Tool`; the
  model is extensible.
- Hierarchical Element naming is useful where appropriate, for example `Messaging.Format`,
  `Messaging.Delivery`, `Messaging.Actions`.
- Capability structure/relationships may be documented by the Capability itself; do not require a
  universal generic relationship graph where it adds no value.

### Capability Definition

Every Capability has **one required current Capability Definition document**.

It is the stable Capability-level contract/control document and may contain compact capability-level
Brief/Purpose and Requirements rather than requiring separate Brief/Requirements documents.
Separate documents remain optional when size, complexity or lifecycle warrants them.

Expected Capability Definition concerns include, as relevant:

- identity and current Capability release;
- purpose/brief, boundary and capability-level requirements;
- Capability Elements and composition/relationships;
- capability-level Dependencies;
- Platform Definition;
- Build Platforms;
- Element Production mapping/state;
- Capability Release History/composition;
- post-Build intent.

Do not duplicate detailed Element semantics or design reasoning here when their authoritative home is
an Element, Design or Decisions document.

### Design relationship

- Design is knowledge, not a mandatory one-document-per-output pipeline.
- A Capability may have zero, one or many Design documents.
- One Design contribution may affect several Elements; one Element may aggregate several Design
  contributions.
- Design contributions may be whole documents or sections/blocks.
- Confirmed results may be written directly to the appropriate authoritative home; do not require
  `chat -> Design -> Standard/Tool` where Design would merely duplicate the outcome.
- When current Design contributions conflict materially, reconcile the design; Build must not choose.

### Update Capability Elements

The current design-side `Build Capability Tool` concept should be renamed/reframed as
**Update Capability Elements**.

Purpose:

- produce, refresh or validate canonical Capability Elements where the Capability's documented
  production model calls for derivation from Design/other inputs;
- evaluate changes in Element production inputs;
- create a new Element release only when the resulting canonical Element meaning actually changes.

It is not mandatory for directly authored Elements where no derivation/update step is needed.

### Element Production state

Element source/dependency tracking is **design-side production state**, not Build input and not part of
consumer-facing Element semantics by default.

The Capability Definition is the normal required host for an **Element Production** section that can
record, per Element:

- applicable source/design contributions;
- applicable production Standards/Tools/dependencies;
- current versions last evaluated.

Rule:

`input changed -> reassess Element -> semantic Element change?`

- **No:** advance the current evaluated-input checkpoint; Element release remains unchanged.
- **Yes:** update/validate the Element and, on successful confirmation, create the next Element
  release.

A changed upstream document/version makes an Element potentially stale; it does not automatically
create a new Element release.

### Release/version model

Keep these identities distinct:

1. source document version — DocMeth-controlled working/canonical document revision;
2. Capability Element release — semantic released Element version;
3. Capability release — confirmed composition of Element releases plus applicable Capability-level
   definition;
4. Capability Package/build identity — concrete Build output identity;
5. deployment state/identity — AI Deployment concern.

Source documents may advance through several document versions without changing the Element release.

An Element release is created only as the result of successful production/validation confirming a
new semantic Element outcome. Merely invoking or forcing Build never increments an Element release.

A Capability release is a confirmed composition, for example:

```text
Messaging@v8
  Messaging.Format@v5
  Messaging.Delivery@v2
  Messaging.Actions@v5
```

A new Capability release is required when the confirmed Capability composition or substantive
Capability-level definition changes. A force rebuild with identical semantics creates only a new
Capability Package/build identity.

### Release History

`Release History` is a semantic section, not necessarily a dedicated document type.

Element Release History may reside in the Element document, applicable Design, Capability Definition,
or a dedicated history document where scale warrants it. Capability Release History naturally fits
in the Capability Definition unless another permitted host is more appropriate.

Release History records released state/composition, not general change reasoning. Decisions remains
the home for reasoning, alternatives and design evolution.

For traceability, an Element release history may preserve the exact production-input/source versions
that produced that release. Current evaluated-input checkpoints remain separate mutable production
state so later source revisions can be checked and cleared as non-impacting without rewriting the
historic release snapshot.

### Migration

Migration remains attached to the Element release that causes it, using existing `AIDE_Migration`
semantics (`Required`, `OnUpdate`, `None`).

A mutable **Current Migration** section is used while the next Element change is being designed/
produced. On successful confirmation of a new Element release:

- Current Migration is converted into the immutable/versioned migration entry for that release;
- prior supported migration history remains;
- Current Migration is cleared for future work.

Current Migration and migration/release history are semantic sections with flexible permitted hosts,
including the Element document, applicable Design and, where appropriate, Capability Definition.

Capability-level Release History may provide an aggregate migration summary, but authoritative
migration instructions remain with the Element release that caused them.

### Platform Definition and Build Platforms

`Platform Definition` lives in the Capability Definition and records design-owned platform posture/
requirements.

Platform Definition is resolved against current applicable platform Standards/Profiles into
`Build Platforms` on the design/Capability-production side.

Per platform, the minimal model is:

```yaml
BuildPlatforms:
  <Platform>:
    Supported: true|false
    Build: true|false|undefined
    Notes: optional
```

- `Supported` is generated factual state.
- `Build` is designer-owned tri-state selection.
- `Notes` is optional human/status context, not machine-semantic.
- newly supported platforms must be surfaced loudly and must not silently switch `Build` to true;
- `Supported:false` with `Build:true` is a loud/blocking inconsistency, not something to silently
  rewrite.

Build consumes resolved Build Platforms; Build does not execute Platform Definition logic or decide
platform eligibility.

### Capability Build ownership

Ownership rule:

> Generic Build owns reusable Build framework/process/WorkPackage/execution conventions. The semantic
> owner of a buildable domain owns the specialised Standards, Tools and logic required to build that
> domain's outputs using the generic Build framework.

Therefore:

- **Build** owns generic WorkPackage/execution/validation/provenance/output-identity mechanisms.
- **Capabilities** owns the specialised Capability Build Standard/Tools/logic.
- generic platform Standards/Profiles are expected to live in Core or their confirmed generic owner;
  Capability-specific platform realisation rules live under Capabilities and build on those platform
  Standards.

Expected Capabilities-owned build contracts/tools:

- `AIDE_Capability` (or equivalent) — Capability/Definition/Element semantic model;
- `AIDE_CapabilityBuild` — common specialised Capability Build contract;
- platform-specific Capability Build Standards where enough platform-specific logic exists to justify
  them, e.g. `AIDE_CapabilityBuild.<Platform>`;
- **Update Capability Elements** — design-side Element production/update action;
- **Build Capability** — orchestration/transition action that establishes the current Build request and
  produces/authorises the WorkPackage under current methodology;
- **Capability Builder** — Build-side specialised executor that applies Capability Build rules while
  executing the WorkPackage.

Do not redesign WorkPackage during this work unit; use the current generic Build/WorkPackage contract.

### Capability Package

Capability Builder produces a **complete Capability Package** for every successful build.

- one logical platform output area per selected (`Build:true`) platform;
- implementation may use full rebuild, incremental build, cache/reuse or selective rebuild internally;
- affected outputs rebuild when their canonical source or material build dependencies change;
- force build may target the whole Capability, a platform, an Element or an identified portion;
- external contract remains: **incremental internally; complete externally**;
- a successful forced/repeated build can issue a new package identity without changing Capability or
  Element release versions.

Capability Build may turn platform-neutral Element migration definitions into platform-specific
migration actions/material using the applicable Capability Build platform rules and generic platform
Standards.

### Dependencies

Reuse `AIDE_Dependencies`; do not create a Capability-specific dependency system.

- Capability-level semantic dependency belongs in Capability Definition.
- Element-specific semantic dependency may remain local to the Element.
- distinguish semantic Dependencies from Element production `Sources`/`Production Inputs`.
- dependency information needed downstream should survive into Build/package metadata as required;
  operational satisfaction/composition is left to AI Deployment unless later architecture says
  otherwise.

### Post-Build actions

Post-Build actions should be Tools owned by the area that best understands the destination/mechanism.

Current ownership assumptions:

- generic publish/copy of Build output to a folder/location — likely **Build-owned Tool**;
- publish/register a package into a Deployment Registry — likely **AI Deployment-owned Tool**.

Capabilities declares the requested post-Build action/inputs; Capability Build invokes the relevant
Tool after successful package validation.

### Deployment Registry boundary

Dave has confirmed **Deployment Registry** as the current producer-side term for the source base where
built packages available for later deployment reside with metadata.

AI Deployment is assumed to own the Deployment Registry contract and downstream deployment model.
Capabilities ends after complete Capability Package production and successful nominated post-Build
handoff.

AI Deployment may refine the name/details during its active WIP and must return any required seam
changes to Capabilities once its design is confirmed.

## Confirmed cross-topic architecture consequences

### Section-first documentation model

Confirmed direction:

> Documents are containers/hosts. Semantic sections are the information units. Standards define the
> section meaning and permitted/default document hosts.

General intent:

- one or more permitted hosts may exist for a semantic section;
- one authoritative instance for a particular scope — permitted multiple hosts must not mean competing
  editable copies;
- compact-first: retain sections inside a suitable multi-use document while small/cohesive; externalise
  to a dedicated document when size, complexity, lifecycle, retrieval or reuse justifies it;
- more-specific domain Standards may add context-specific permitted hosts without globally redefining
  the section semantics;
- moving a section between permitted hosts is normally structural rather than semantic.

Examples relevant to Capabilities:

- Capability Definition may host compact Capability-level Brief/Purpose and Requirements;
- Release History and Current Migration have multiple context-dependent permitted homes;
- Element Production belongs naturally in Capability Definition.

Expected reconciliation owners:

- Documentation Methodology — generic section/document-host architecture;
- Project Design — Brief/Requirements/Considerations semantics and baseline hosting as applicable;
- Capabilities — Capability-specific permitted hosts.

No DocMeth handoff has yet been sent; collect the remaining related concepts first and reconcile as one
coherent pass where practical.

### Topic ownership versus Working Context

Confirmed direction:

> Semantic Topic ownership determines authoritative meaning, source baseline, durable destination and
> reconciliation obligations. It does **not** determine where work must be performed.

Work may occur in any suitable Working Context/container — ChatGPT, Claude, Claude Code, Codex, code
workspace, repository or future surface — provided the context has sufficient current authoritative
source material for all materially affected Topics and no conflicting active WIP is being overwritten.

Working Context selection is capability- and reality-based rather than stage- or product-based. Do not
assign Design, intent, precision or execution permanently to named products. Choose a practical surface
for the work and accept/manage its real limitations. Examples include choosing a voice-capable chat
surface while mobile even though it cannot directly commit corpus files, or choosing a file-based
surface when direct multi-file reconciliation materially reduces friction.

A Working Context must be supplied with two distinct kinds of prerequisites:

1. **work/source context** — the Topic Binders, authoritative files, repositories, external material or
   other sources required for the task; and
2. **governing capabilities** — current applicable Standards, Tools, navigation behaviour and other AIDE
   capabilities delivered through a supported platform mechanism.

Passive availability of a Standard in a document corpus is not a substitute for effective capability
activation/triggering. A file-based AI should not be expected to discover governing Standards by
searching filenames when those Standards can be properly deployed as Skills/Plugins or another active
platform representation.

Consequences:

- a working context may directly make coordinated changes across several Topics when it has the current
  authoritative sources and authority for the task;
- do not require cross-Topic Project Handoff merely because semantic ownership differs;
- use Handoff for active/overlapping independent WIP, deliberate transfer/deferment, independent review,
  missing current authority/context or another reason work genuinely needs to continue elsewhere;
- AI Deployment currently qualifies because it has active overlapping WIP;
- when direct authoritative file editing is used, a Git-controlled/versioned corpus is preferred where
  practical so completed semantic work can be committed transactionally and traced; exact commit/push
  automation remains environment/Working-Practices configuration rather than a universal rule.

### Working Surface / Platform capability model

Confirmed direction:

> Core/platform architecture should describe factual capabilities and constraints of Working Surfaces.
> Working Practices and Capability Build consume those facts rather than hard-coding product roles.

Candidate factual dimensions include, as evidence warrants: direct file read/write, repository access,
semantic/project retrieval, voice/mobile access, command/shell execution, artifact editing, persistent
instructions, Skills/Plugins, context/source limits and supported deployment mechanisms. Exact schema is
not yet fixed.

A surface may support **multiple deployment mechanisms**. Do not assume one canonical route per platform.
For example Claude may support both plugin/account deployment and bundle/context deployment; OpenAI
surfaces may use different Skill/Plugin/bundle/context routes depending on surface and environment.

Keep separate:

- what the surface/platform **can support**;
- which deployment mechanisms are **supported** for that surface; and
- what AIDE capabilities are **actually deployed/current** in the present environment.

When the desired outcome materially depends on a missing or unknown capability and the context can
detect that fact, surface it loudly before claiming the outcome can be produced correctly. Distinguish
required capability gaps from merely advantageous capability gaps; the latter may be accepted with an
explicit limitation/handoff. Unknown support is not silently treated as supported.

### Session/work-unit completion

A Working Context is temporary and must not remain the sole holder of authoritative semantic state.

When a work unit/session completes:

- reconcile all confirmed in-scope work into the correct owning Topic corpora;
- record confirmed but undelivered obligations in the proper durable work-state mechanism;
- retain only genuinely active continuation state in WIP;
- do not leave confirmed semantic decisions stranded solely in closed chat history;
- completion is a mandatory reconciliation/checkpoint even though outputs may be deliberately batched
  during active work to avoid churn.

### Topic terminology and aliases

- `Topic` remains the normal semantic/governance term; use `Top-level Topic` only where distinction from
  a subtopic matters.
- aliases such as `DocMeth` may be declared/used for convenience without changing canonical identity.
- do not equate Topic with ChatGPT/Claude `Project`; those are Working Context/container forms.

### Binder model

Confirmed direction:

> Topics are semantic boundaries. Binders are generated current-context/work boundaries for
> **Documentation Topics**. They are not a universal scope mechanism for code projects, repositories or
> other non-document work structures.

Rules/direction:

- every top-level Documentation Topic produces one Binder by default;
- a Topic may partition its Binder boundary into child/subtopic Binders when document volume, context
  limits or work-management needs justify it;
- partitioning is practical and compact-first; the mere existence of a subtopic does not justify a new
  Binder;
- when partitioned, child Binder boundaries should provide deliberate complete coverage, with a
  lightweight parent Binder-set/index rather than requiring a duplicate giant aggregate Binder;
- Binder boundary/state should be declared by the Topic;
- a Working Context loads whichever Binders are needed for the task where Binder consumption is the
  practical source mechanism; file-based contexts may instead navigate the authoritative corpus directly
  using the same declared Topic boundary.

Capabilities is the current example of a deliberately partitioned Binder set. A curated Blind Review
file set is **not** a Binder; if transfer packaging is needed, use a separate Review-material/package
concept whose inclusion and deliberate exclusion/withholding are Review semantics.

`Overview` remains a human-oriented high-level/TLDR current snapshot and must not be repurposed as the
primary machine navigation layer. Strengthen/use the Topic `Index` and deployed document-navigation
behaviour for file-based discovery instead.

## Confirmed Knowledge model

`Knowledge` is accepted as a durable documentation/resource concept for preserving valuable lateral
knowledge assets that would otherwise die with the Working Context.

Decisions retains its deliberately broad role: topic/subtopic-specific thinking, investigation, working,
alternatives, knowledge and reasoning associated with the evolution of that area, alongside explicit
decision history. Design/Definition/Standards/Tools hold the current confirmed semantic snapshot/output.

Knowledge is used for valuable broader thinking, deep research, investigation, observations, discoveries
and lateral understanding accumulated in relation to a top-level Topic but not naturally belonging to one
of that Topic's specific subtopic/design/decision threads.

Rules/direction:

- zero or one current Knowledge document per top-level Topic by default, created only when needed;
- no general AIDE-level Knowledge document initially; if material is genuinely durable system-wide
  guidance/premise it may belong in Principles, while later evidence may justify another shared mechanism;
- when several top-level Topics are in one Working Context, place the entry in the Topic that is the most
  natural future retrieval home; use the dominant/focus Topic as the fallback when otherwise ambiguous;
- use lightweight related-Topic references/tags rather than duplicate authoritative copies;
- optimise initial capture for retention rather than perfect classification;
- periodically curate Knowledge (for example a monthly sweep where useful), moving/consolidating entries
  into another Topic, Decisions, Design/current semantic owners or Principles when their proper home becomes
  clearer; obsolete/disproved knowledge should be explicitly superseded/retracted rather than silently
  erased where the history remains valuable;
- stable `K` entry identifiers and an index-first retrieval structure are preferred, with minimal metadata
  sufficient for retrieval/correction;
- Knowledge may inform later Design/decisions but is not a hidden executable authority. If a finding becomes
  required/current semantics, reconcile it into the proper authoritative owner.

## Retained platform/deployment evidence — point in time

### Claude

Claude deployment behaviour has been empirically tested in separate work and is treated as the current
known baseline for the mechanisms actually proven there. This Working record does not duplicate all of
that evidence; later platform/profile reconciliation should consume the dedicated evidence/current source.
Allow multiple Claude deployment mechanisms, including plugin/account and bundle/context routes where
applicable.

### OpenAI empirical baseline — 2026-08-30

Retain these tested findings for later platform/Capability Build/AI Deployment work. They are point-in-time
evidence, not permanent platform guarantees:

- **Codex CLI/local plugin was proven:** package/plugin validation passed; the installed `AIDE Tags` Skill
  was discoverable explicitly and implicitly; the governed Boolean/group behaviour, capability identity and
  `MigrationSummary` were successfully exercised; an unrelated negative-trigger case did not invoke it.
- Codex local plugin updates were session/cache bound in the test: an existing session remained on its
  baseline cache while a new session loaded the updated build.
- A Codex local marketplace/plugin being visible in ChatGPT desktop metadata did **not** prove runtime Skill
  execution there. Ordinary desktop Chat could not load the Skill body, and the local marketplace/plugin did
  not appear in ChatGPT web.
- **ChatGPT Cloud Work personal standalone Skill was proven:** a personal Skill installed through ChatGPT web
  triggered implicitly in Web Work and desktop Cloud Work using body-only probes; an unrelated negative case
  did not trigger it. The same remote Skill updated in place and existing/new Work conversations resolved the
  updated body without reinstall/restart in that test.
- The tested personal standalone Skill was unavailable in ordinary Chat and was not discovered by Codex's
  local Skill picker.
- Therefore one installed OpenAI artefact/route did not serve all tested surfaces. Treat runtime surface,
  representation and distribution channel as separate deployment facts; UI/metadata presence is weaker than
  runtime probe evidence.
- At that point the proven practical split was: Codex CLI/local plugin; ChatGPT Cloud Work/personal standalone
  Skill; ordinary Chat/project-context Bundle fallback. Hosted/cloud/plugin routes that might broaden ordinary
  Chat or cross-surface reach remained untested.

Current OpenAI documentation and product capabilities may expose additional routes, including Git-backed or
workspace plugin distribution. Do **not** promote those possibilities to confirmed AIDE platform facts until
we resume controlled testing. Add new mechanisms to the platform model when empirically confirmed rather than
replacing the proven baseline by assumption.

## Coordination / current constraints

- **AI Deployment:** active WIP elsewhere. Do not directly overwrite its unsettled design. Supply
  confirmed producer-side assumptions through handoff and require a return seam handoff when its
  design is committed.
- **All other relevant Topics:** understood to be committed/persisted at present; cross-topic changes
  may be made from a suitably sourced Working Context.
- **Review D:** remain on hold until the redesigned Capability/Build/AI Deployment seam is committed and
  can be reviewed against a truthful current baseline.

## Next actions

1. Continue the current design discussion and collect the remaining related architecture concepts.
2. Before a broad corpus modification pass, load the current Binders/masters for every materially
   affected committed Topic (expected at minimum DocMeth, Project Design and Working Practices; add
   Build/Core where concrete rules are affected).
3. Reconcile the confirmed section-first, Knowledge, Working Context/Topic, surface-capability,
   session-closeout, Index-navigation and Binder-boundary architecture as one coherent cross-topic pass.
4. Reconcile the confirmed Capability redesign into the Capabilities corpus and production contracts.
5. Coordinate only the overlapping AI Deployment seam through handoff while its WIP remains active.
6. Preserve the 2026-08-30 OpenAI tests as the empirical baseline; resume bounded OpenAI/other-platform
   deployment tests later and add routes only when confirmed.
7. Re-baseline and resume Review D only after these seams are committed.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v3, AIDE_Messaging@v2
References: Capabilities_WorkRegister_v17, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-09-01-3_Capabilities_v1
