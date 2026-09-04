# Documentation Methodology Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 2** (2026-08-31). Assembles the v21 Foundation consolidation masters.

## Binder manifest

- `DocumentationMethodology_Index_v6.md` — sha256 `4b9cd44ac3fa`
- `DocumentationMethodology_Design_v18.md` — sha256 `7635b32f20e1`
- `DocumentationMethodology_Decisions_v19.md` — sha256 `3bb6101d99e3`
- `AIDE_DocumentationMethodology_Standard_v21.md` — sha256 `6629c6d004ff`
- `DocumentationMethodology_Guide_v21.md` — sha256 `e80fbdd3ca9f`

---

<!-- BEGIN SOURCE: DocumentationMethodology_Index_v6.md -->
# Documentation Methodology — Index

> **Version 6** (2026-08-31). Adopts `AIDE_Index@v1`, records the v21 top-level-topic and live
> work-state model, and moves generic Index ownership to Core.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v21}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v6 | Index | Current |
| `DocumentationMethodology_Design` | v18 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v19 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v21 | Standard | Current; identity `AIDE_DocumentationMethodology@v21` |
| `DocumentationMethodology_Guide` | v21 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v21` and consumed through `AIDE_Index@v1`.

A DocumentationTopic represents one self-describing top-level documentation topic and resolves its
own governing Index/Document Register. A chat project/master folder may host one or several such
topics; the container boundary is not itself the semantic topic boundary.

### Migration state

- v18 — `OnUpdate` legacy structure/conformance transition.
- v19 — `None`.
- v20 — `None`.
- v21 — `None`; new Index/work-state/topic semantics apply prospectively/on substantive update.

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v5` | `DocumentationMethodology_Index_v6` |
| `DocumentationMethodology_Design_v17` | `DocumentationMethodology_Design_v18` |
| `DocumentationMethodology_Decisions_v18` | `DocumentationMethodology_Decisions_v19` |
| `AIDE_DocumentationMethodology_Standard_v20` | `AIDE_DocumentationMethodology_Standard_v21` |
| `DocumentationMethodology_Guide_v20` | `DocumentationMethodology_Guide_v21` |

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, DocumentationMethodology_Design_v18
References: DocumentationMethodology_Guide_v21
<!-- END SOURCE: DocumentationMethodology_Index_v6.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Design_v18.md -->
# Documentation Methodology — Design

> **Version 18** (2026-08-31). Reconciles Documentation Methodology with Core Index, makes
> top-level topic the semantic anchor, separates WIP from Working, and strengthens live
> OpenItems/WorkRegister and WorkPackage reconciliation semantics.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Documentation Methodology provides the common document/corpus contract for AIDE-governed work.

It owns:

- governed document naming and filename structure;
- document types and document-specific lifecycle/disposition;
- lifecycle state meanings including Current, Superseded and Archived;
- governed-history and dead-locator preservation requirements;
- top-level-topic/subtopic/document organisation semantics;
- documentation-specific Index extensions, including document/topic/type/assets registers;
- document metadata-container placement/coexistence;
- authoritative-master versus generated-consumption-artifact distinction;
- document distribution rules; and
- document output/version discipline.

It does **not** own:

- generic Index/Item/Item Type semantics — `AIDE_Index`;
- generic Domain resolution — `AIDE_Domain`;
- physical repository/storage workflow — Working Practices/environment;
- formal identity — Core;
- Tags/Dependencies/Migration/Review semantics — their owners;
- generic WorkPackage execution/return — Build/WorkPackage;
- Messaging envelope/schema/transport behaviour — Messaging; or
- platform packaging/deployment mechanics.

The governing rule remains one semantic owner per mechanism.

## §2 — Top-level topic is the documentation anchor

A **container** is a practical storage/context boundary such as a master folder, chat project,
workspace or another shared context pool.

A container may contain one or more **top-level topics**.

Documentation state that historically used “project-wide” as shorthand is anchored to the
**top-level topic**, not automatically to the container.

```text
container
├── Top-level Topic A
│   ├── documents
│   ├── OpenItems
│   └── WorkRegister
└── Top-level Topic B
    ├── documents
    ├── OpenItems
    └── WorkRegister
```

Current AIDE containers are often 1:1 with top-level topics, but that is a convenience rather than
a semantic rule.

## §3 — Naming model

Normal governed Markdown filename:

```text
{TopLevelTopic}_{Subtopic...}_{DocType}[_{Key}]_v{N}.md
```

- The top-level topic prefix is always the semantic anchor for governed topic material.
- Omit subtopic segments when the document is top-level-topic-wide.
- Compound subtopic segments may express subdivision/instantiation and may nest.
- Add a key only where the DocType/working pattern requires one.
- Keep `_v{N}` last.

This wording replaces the older conceptual `{Project}_{Topic}_...` description. Existing filenames
that already begin with the top-level topic prefix normally require no rename.

A filename is a legible locator; applicable Index/document registration remains authoritative.

## §4 — Principal document/work-state model

```text
WIP
  current volatile persisted context

Working
  substantial exploratory/formative material

OpenItems
  durable live attention still unresolved/pending/future

Brief / Requirements
        ↓
      Design  ← Decisions
        ↓
     outcomes

WorkRegister
  confirmed downstream consequences still undelivered
        ↓
   WorkPackage(s)
        ↓
      Outcome
        ↓
reconcile WorkRegister
```

These roles are deliberately distinct.

### WIP

`WIP` is a high-churn persisted checkpoint of **current active work context**.

Use it when loss of the current conversation/session/platform context would materially impair
continuation and the state is not yet appropriately represented elsewhere.

WIP may hold:

- current position and active thread;
- reasoning/thinking not yet routed;
- draft fragments;
- candidate OpenItems or WorkRegister consequences;
- current source pointers; and
- a resume point.

WIP is not authoritative and temporary duplication is acceptable.

A WIP normally anchors to one top-level topic. A subtopic/thread key may be used where several
parallel active work contexts would otherwise make one WIP noisy.

### Working

`Working` is substantial exploratory/formative material worth preserving as an independent body of
work, even when its eventual authoritative destination is not yet known.

Working is **not merely “Design in progress.”** It may precede a Brief/Design entirely and may later
feed Design, Decisions, a Brief, Reference, proposal, Review response or several destinations.

Use Working when the exploratory material itself has enough volume/coherence to be useful beyond a
short current-context checkpoint.

### OpenItems

`OpenItems` is the durable live attention register: current, pending, deferred or future items whose
loss would matter and which still require thought, revisit, investigation or progression.

It contains only live/open state. When an item resolves, route any durable result where it belongs
and remove the OpenItem. Do not retain a closed-items archive/tombstone history merely to prove the
item once existed.

Default scope is one register per top-level topic. A subtopic may have its own delegated OpenItems
where use/volume/cadence makes that materially clearer.

### WorkRegister

`WorkRegister` is the top-level-topic-wide live queue/ledger of **confirmed downstream consequences
or work not yet fully delivered**.

It is especially the reconciliation layer between committed Design and delivered reality.

Whenever a confirmed Design change creates a downstream implementation/output consequence that is
not fully completed in the same pass, record enough detail in WorkRegister to determine later
whether the committed Design has been delivered.

A WorkRegister item records, proportionately:

- identifier where useful;
- source/triggering confirmed Design change;
- the committed change;
- specific required downstream outcome/code/build/document changes;
- target outcome(s)/location(s);
- current delivery state;
- WorkPackage/action mapping;
- returned result where not closed; and
- remaining work.

One WorkPackage may cover several WorkRegister items; one WorkRegister item may require several
WorkPackages.

When all consequences are delivered and reconciled, remove the WorkRegister item. Preserve durable
reasoning/state only in the appropriate authoritative artefacts.

Default scope is one WorkRegister per top-level topic. Delegate only when an independently useful
subtopic queue is justified by volume/cadence.

## §5 — Routing and lifecycle between live states

During active work:

```text
WIP
├── substantial exploratory body → Working
├── unresolved durable attention → OpenItems
├── confirmed position           → Design / other authoritative owner
├── material reasoning           → Decisions
├── confirmed work owed          → WorkRegister
└── transient/no longer useful   → discard
```

An OpenItem may become active through WIP/Working and then resolve to Design/Decisions,
WorkRegister, another owner or nothing durable.

A WorkRegister item does not need to have been an OpenItem first; a confirmed Design change can
create it directly.

## §6 — Versioning and currency

A document version counts **issued/persisted checkpoints**, not keystrokes.

For WIP specifically, visible filename versioning is useful as a currency/transport signal across
chat/project/platform contexts.

```text
Capabilities_Messaging_WIP_v7.md
```

Within one editing context, draft/edit freely. Increment WIP version when a new persisted checkpoint
is issued for reuse/resumption/sync so a human or AI can tell at a glance which context file is the
latest.

Prior issued WIP versions become Superseded when replaced.

Working follows normal issued-output versioning. OpenItems and WorkRegister increment when a new
register state is issued/persisted.

## §7 — WIP/Working disposition

WIP normally has no independent terminal-history value. Once its useful content is safely routed,
it may be withdrawn/disposed; archive only where the WIP itself has unusual independent value.

Working may persist for a much longer period. On completion:

- **Superseded/withdrawn** where its substantive value is fully represented elsewhere; or
- **Archived** where the Working document itself has independent historical/research value.

Physical handling is owned by Working Practices/environment.

## §8 — Binder/context and live-state registration

A normal project/topic Binder is a stable/current knowledge consumption artefact, not a live work
queue.

By default exclude these high-churn/internal live-state documents from the normal Binder:

```text
WIP
Working
OpenItems
WorkRegister
```

Load them separately when resuming or managing active work.

The documentation Index must not reintroduce the same churn indirectly. A live-state checkpoint
such as `..._WIP_v7.md` **does not by itself require an Index or Binder reissue**.

For live-state documents, the documentation Index may:

- omit the individual live versions from the stable Document Register; and
- optionally register the active **series/locator** in a compact `Live state` section where that
  materially helps discovery.

A series entry is intentionally version-agnostic, for example `Capabilities_Messaging_WIP`; the
current issued checkpoint is established from the available/current file and its visible `_vN`
filename when the live state is actually loaded. Do not claim a current WIP version from a stale
Index row.

Reconcile creation/withdrawal of live-state series at the next normal corpus/output checkpoint.
This keeps Index/Binder stable while preserving discoverability.

A specialised Binder may include live state explicitly where its stated purpose requires it, but
omission from the normal Binder is the default.

Index remains a normal Binder source because its stable structural/documentation map is useful
without carrying every live-state revision.

## §9 — Documentation-specific use of Index

Generic Index semantics come from `AIDE_Index@v1`.

Documentation Methodology defines documentation-specific extensions, including:

- top-level topic/subtopic declarations;
- Document Register and current version/type/lifecycle facts;
- custom document type declarations;
- documentation assets/unmanaged-file records;
- dead locator/rename/rehoming records; and
- documentation-local configuration.

The documentation Index may present these as owner-defined sections alongside generic `Contents`.

The Index is authoritative for the documentation registration facts it owns. It is not thereby
authoritative for another registered item's internals.

### DocumentationTopic Item Type

Documentation Methodology defines the semantic Item Type `DocumentationTopic`.

A DocumentationTopic is a self-describing documentation boundary for **one top-level topic**. It
resolves the documentation Index (or authoritative Index section) governing that topic and its
Document Register.

A practical container may host one or several DocumentationTopics. The Item Type therefore does
not mean “chat project”, “master folder” or another storage/context container, even where the
current layout happens to be 1:1.

Identification is based on authoritative top-level-topic/Index declarations rather than folder
naming alone.

It provides:

- top-level-topic identity and self-describing documentation-boundary behaviour;
- documentation Index/Document Register resolution; and
- optional container/project mapping properties where known.

A parent repository Index may register/describe/locate a DocumentationTopic and stop at that
self-describing boundary. Where several top-level topics share one physical container, the parent
may register the container structurally and the topics as distinct logical Items beneath it.

Whether DocumentationTopic is Domain-capable is owned by `AIDE_Domain`, not by this definition.

## §10 — Established document types

Documentation Methodology continues to own document-specific lifecycle integration for Brief,
Requirements, Design, Decisions, WIP, Working, Review, Guide, Reference, Glossary, Overview,
WorkPackage/Outcome integration, Index, OpenItems and WorkRegister.

Messaging owns Message envelope/schema/transport semantics and any Messaging-specific Message type
contract. Where a Message is persisted as a governed file, Documentation Methodology supplies only
normal naming/lifecycle/metadata hosting unless Messaging explicitly defines a document integration
rule.

Custom types remain valid and owner-defined under the normal custom-type contract.

## §11 — Design and Decisions

Design remains the confirmed current position. Decisions preserves synthesized substantive
reasoning/history for a future Design reader and is not a downstream outcome input.

A Decisions event remains owed for substantive confirmed Design changes, material requirement
changes and credible rejected alternatives likely to be re-derived. Editorial/mechanical changes
do not create ceremony by themselves.

Substantive Design and its Decisions reasoning are issued in the same pass.

## §12 — WorkPackage integration and WorkRegister reconciliation

Generic WorkPackage execution belongs to `AIDE_WorkPackage` / Build.

When a WorkPackage is created from WorkRegister items, the package identifies the covered item IDs
and the portion of each obligation it is authorised to deliver.

On return:

- Build reports the result/evidence for the mapped work;
- the director/owning process reconciles each WorkRegister item;
- completed obligations are removed;
- partial/blocked obligations retain the returned result and remaining work; and
- design-shaping feedback returns to Project Design before changed execution is authorised.

Build does not silently close the owning WorkRegister.

## §13 — Lifecycle/disposition boundary

Current, Superseded and Archived remain semantic lifecycle states independent of physical storage.
Working Practices/environment owns the physical implementation.

Generated Binders/Bundles remain non-authoritative consumption artefacts assembled from masters.

## §14 — Metadata host boundary

Document layout may contain title/version preamble, header metadata, temporary owner-labelled
state, body, footer metadata and an Internal section.

Documentation Methodology owns placement/coexistence/compact rendering; semantic owners retain
their field meanings.

## §15 — Conformance and migration

Documentation Methodology conformance remains a normal dependency checkpoint.

v18 remains `OnUpdate`; v19/v20/v21 are `None` transitions.

v21 changes the canonical operating model but does not require mass rewriting/renaming of existing
documents. Existing Indexes/live registers adopt the new model on their next substantive update or
when an operation specifically requires v21 semantics.

## §16 — Published outcomes

This Design produces:

```text
AIDE_DocumentationMethodology@v21
DocumentationMethodology_Guide_v21
```

The Standard is the canonical AI-facing runtime contract; the Guide is the fuller human companion.

---
Dependencies: AIDE_Index@v1, AIDE_Dependencies@v2, AIDE_Migration@v1
References: DocumentationMethodology_Decisions_v19, WorkingPractices_Design_v5, AIDE_WorkPackage@v2
<!-- END SOURCE: DocumentationMethodology_Design_v18.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Decisions_v19.md -->
# Documentation Methodology — Decisions

> **Version 19** (2026-08-31). Preserves the complete prior decision history and records the Core
> Index ownership split, top-level-topic anchor, WIP/Working distinction, live-only registers, and
> WorkRegister/WorkPackage reconciliation model.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## D1 — Metadata containers are generic hosts

**Decision.** DocMeth owns placement/coexistence/compact rendering for header metadata, temporary
state and footer metadata. Contributing owners retain semantics.

## D2 — Documentation Methodology conformance is a Dependency

**Decision.** Retire the special `Methodology: vN` footer from v18. A document records its
saved/proven DocMeth conformance through `AIDE_Dependencies`.

**Reason.** This removes a duplicate version-gap/checkpoint mechanism and lets Migration govern
Required/OnUpdate/None transitions consistently.

## D3 — v18 migration posture is OnUpdate

**Decision.** v18 is `OnUpdate`.

**Reason.** v17 documents remain safely readable. The metadata/conformance model should be applied
when a document is next changed rather than forcing a corpus-wide rewrite merely to refresh
metadata. An operation that explicitly requires v18-only semantics can require migration first.

## D4 — Tags and Dependencies are hosted, not redefined

**Decision.** `Tags:` and `Dependencies:` are footer properties hosted by DocMeth. Their internal
grammar/build/query/conformance semantics remain with `AIDE_Tags` and `AIDE_Dependencies`.

## D5 — Identity is header metadata

**Decision.** Formal Core `Identity:` metadata is hosted in the header container where a governed
document exposes a referenceable identity. Filename and formal identity remain distinct.

## D6 — Temporary state is compact and owner-labelled

**Decision.** An optional temporary state container is placed near the top of the document.
Entries require stable owner identity plus concise human-readable title/message. The owner alone
defines lifecycle/content.

## D7 — WorkPackage execution semantics move to Build

**Decision.** DocMeth retains WorkPackage/Outcome document naming and archive integration but
delegates generic WorkPackage contract/execution/validation/return semantics to
`AIDE_WorkPackage@v1` and `AIDE_Build@v1`.

## D8 — Machine content remains compact

**Decision.** Metadata, derived state and generated operational content should be as compact as
practicable in human-readable documents.

## D9 — Re-establish a current Documentation Methodology Design

**Decision.** `DocumentationMethodology_Design_v15` is the confirmed internal model from which
the current published outcomes are produced.

**Reason.** A distributable outcome should have an authoritative defining source. The v18 Guide
already describes Design as the confirmed internal position; the operational closure package had
not included the older Design master.

## D10 — Publish a canonical Documentation Methodology Standard

**Decision.** Produce `AIDE_DocumentationMethodology_Standard_v1` with formal capability identity
`AIDE_DocumentationMethodology@v18`.

**Reason.** Documentation Methodology is reusable AI-facing behavioural infrastructure and should
use the same Design → canonical Standard → Build/Deployment path as other AIDE capabilities.

## D11 — Retain the Guide as a human companion

**Decision.** `DocumentationMethodology_Guide_v18` remains the human-readable explanatory outcome.
It is not replaced by the Standard.

**Reason.** The Standard is the concise AI operating contract; the Guide carries richer examples,
rationale and detailed explanatory material. Both derive from the same Design.

## D12 — Documentation Methodology Standard version follows the established methodology release

**Decision.** The canonical Standard for the current methodology release is
`AIDE_DocumentationMethodology_Standard_v18.md` with formal identity
`AIDE_DocumentationMethodology@v18`.

**Reason.** Documentation Methodology already has an established release lineage through v18.
Using `_v1` for the first Standard representation creates an unnecessary second visible version
number for the same methodology state. Aligning the Standard filename with the methodology
release preserves continuity and makes the Standard/Guide pair visibly one release.

**Scope.** This does not collapse the general distinction between document version, capability
release version, package identity, and deployment state. It is a deliberate alignment for this
existing methodology lineage.

## D13 — Legacy `Methodology: v17` supplies the migration starting checkpoint

**Decision.** For the v17→v18 transition only, where no Documentation Methodology dependency
checkpoint exists, an unambiguous legacy `Methodology: v17` declaration is interpreted by
Migration as proven conformance through `AIDE_DocumentationMethodology@v17`.

The interpretation is read-only until a qualifying update/save. Successful migration writes the
v18 dependency checkpoint and removes the legacy line.

**Reason.** v17 predates the generic Dependencies checkpoint. Without this bridge the v18
transition describes the target change but does not mechanically define where Migration obtains
the old conformance checkpoint.

## D14 — No dedicated Documentation Methodology Tool yet

**Decision.** Do not create a DocMeth-specific Tool at this stage.

**Reason.** The demonstrated actions are already owned by generic capabilities such as Migration,
Build Capability and Review. A new Tool without a distinct repeated action contract would add
machinery rather than capability.

## D15 — The common Bundle becomes the normal operational distribution

**Decision.** Include the Documentation Methodology Standard in the common AIDE Standards/Tools
Bundle. Once a project has that Bundle, the Guide is not separately required merely to obtain
operational DocMeth behaviour.

**Reason.** This makes the methodology deployable through the same common operating environment
as the other AIDE Standards/Tools while preserving the Guide as the richer human companion.


## D16 — Restore the full Decisions contract to the canonical Design and Standard

**Trigger / problem.** Review of current project use found that the v18 Guide still carries the
established substantive Decisions model, while the re-established Design and canonical Standard
compress it to a much weaker rule. The current Standard therefore does not reliably reproduce the
behaviour expected when it is the only runtime representation available to an AI.

The production path makes this a source-completeness problem as well as an output-completeness
problem: canonical Standards are produced from confirmed Design and production is not authorised
to recover missing capability meaning from Decisions history or invent it during compression.

**Alternatives considered.**

- Leave the Standard concise and rely on the Guide when richer behaviour matters. Rejected because
  the Standard is explicitly the normal deployable/runtime representation and the Guide is not
  expected in every consuming project.
- Expand only the Standard by copying behaviour from the Guide. Rejected because that would repair
  the outcome from a source the production contract does not treat as the authoritative capability
  definition, leaving the Design under-specified.
- Weaken the Guide to match the Standard. Rejected because the stronger model addresses the real
  cost of repeated re-derivation and already contains proportionality safeguards.

**Decision.** Retain the established Decisions model and make it explicit in the confirmed Design,
then produce the canonical Standard from that Design. Decisions records synthesized substantive
reasoning for a future Design reader: the trigger/requirement, problem, genuine alternatives, key
reasoning/distinctions, decision, and important consequences/trade-offs as applicable and
proportionate. Non-trivial rejected alternatives remain visible. Existing historical entries are
not rewritten.

**Consequences.** The canonical AI-facing contract becomes sufficient to reproduce the intended
behaviour without requiring the Guide. The Guide remains the richer explanation, not an alternate
source of missing semantics. Existing short historical entries remain valid history; the stronger
recording discipline applies prospectively.

## D17 — Make the event trigger objective and the record synthetic, not transcript-like

**Trigger / problem.** The phrase “when the reasoning is material” in the v18 Standard allows a
substantive Design change to escape the Decisions record based on a subjective judgment that its
reasoning was not important enough. At the same time, strengthening the rule without a boundary
could turn editorial maintenance or ordinary conversation into documentation ceremony.

**Alternatives considered.**

- Keep “material reasoning” as the only trigger. Rejected because it weakens the knowledge-
  preservation rule precisely when the author underestimates future re-derivation risk.
- Record every textual Design edit and every discussion branch. Rejected because this confuses
  document maintenance with design decisions and would create disproportionate burden.

**Decision.** A Decisions event is triggered by a change to the **confirmed substantive Design
position**, a requirement established or materially revised, or a rejected alternative a future
reader could reasonably re-derive. Purely editorial, formatting, metadata, migration, mechanical
maintenance, or application of an already-recorded decision is not by itself a new design
decision.

Preserve the reasoning necessary to reconstruct why the decision was reached; do not preserve
discussion merely because it occurred. Proportionality controls depth. A genuinely trivial
alternative may be omitted.

**Consequences.** The trigger is objective enough to protect knowledge while the depth rule remains
lightweight. `Decision + Reason` remains acceptable for genuinely simple decisions, but it is not a
sufficient template for work that actually involved meaningful alternatives, distinctions or
trade-offs.

## D18 — Keep Decisions at Design granularity and preserve the downstream boundary

**Trigger / problem.** Current project practice has sometimes expanded child Designs while leaving
their substantive reasoning permanently in a parent Decisions register. The v18 Guide already says
Decisions follows Design granularity. A separate inconsistency in the Guide also says in one place
that Decisions may feed a Guide, contradicting the core rule that Decisions informs Design and
nothing downstream.

**Decision.** Retain same-granularity recording: an independently expanded child Design normally
keeps its substantive reasoning in a Decisions record at that same scope; condensed topics may use
a Decisions section. Parent Decisions remains the correct home for parent-level architecture.
Apply this prospectively rather than relocating or rewriting historical entries.

Decisions remains outside downstream outcome production. If reasoning is necessary for correct
implementation or use, that meaning must be represented in the current Design and may then be
expressed in the downstream outcome. Outcomes do not reach back to Decisions as an input.

**Consequences.** Future retrieval aligns the “what” and “why” at the same scope without disturbing
history. Existing parent-level records may be cited from new child Decisions entries where useful.
The contradictory Guide sentence is corrected in the next Guide issue.

## D19 — Issue the correction as v19 with no artefact migration requirement

**Trigger / problem.** v18 has already been issued. Replacing its bytes in place would violate the
issued-output version rule, while issuing a Standard file version different from the methodology
release would undo the deliberate version alignment recorded in D12.

**Decision.** Issue the corrected methodology as `AIDE_DocumentationMethodology@v19`, with
`AIDE_DocumentationMethodology_Standard_v19.md` and `DocumentationMethodology_Guide_v19.md`.
Declare the v19 transition `None` and retain the v18 `OnUpdate` transition history.

**Reasoning.** v19 corrects the canonical behavioural contract and clarifies existing methodology
meaning; it does not require existing governed documents to be structurally or textually rewritten.
A document at the v18 checkpoint can traverse v19 without content migration and persist the v19
checkpoint on its next qualifying save under normal Dependencies/Migration behaviour.

**Consequences.** No mass migration or retrospective Decisions rewrite is required. The common
Standards/Tools Bundle and other runtime distributions should replace the v18 Standard with v19 on
their next regeneration/deployment.


## D20 — Separate lifecycle semantics from physical storage/workflow

**Trigger / problem.** The v19 methodology correctly distinguishes Current, Superseded and Archived
material, but also embeds one repository implementation into that meaning: current masters in an
active/master folder, `/superseded` and `/archived` folders, sweep/no-guarantee behaviour, cold
storage, and an `assets\` holding convention. Working Practices design identified these as
operating conventions rather than intrinsic document-lifecycle semantics. Keeping them in
Documentation Methodology makes the methodology less portable to document-management systems,
platform-native history, external archive storage, or differently structured repositories.

**Alternatives considered.**

- Retain the filesystem model in Documentation Methodology because it is simple and already works.
  Rejected because it makes a local implementation part of the semantic contract and forces
  unrelated environments to imitate it.
- Move supersession/archive ownership entirely to Working Practices. Rejected because the meaning
  of document states, type terminal events, version transitions and history preservation are
  document-governance concerns and must remain stable across implementations.
- Keep lifecycle semantics here and delegate only physical realisation. Adopted because it creates
  one clean seam without weakening the preservation model.

**Decision.** Documentation Methodology retains:

- **Current** as the issued authoritative version/instance resolved for normal current use;
- **Superseded** as an older issued version or a document displaced/withdrawn without reaching an
  archival terminal disposition of its own;
- **Archived** as a document whose type-specific lifecycle reaches an archival terminal
  disposition, with the archival record frozen except through its permitted correction route;
- document versioning, type-specific completion/terminal rules and the `_Archived_{date}` document
  filename marker;
- the requirement not to discard governed history merely to simplify the active view;
- Index/history/dead-name records needed to keep old locators and terminal history intelligible; and
- the distinction between authoritative masters and generated Binders/Bundles as non-authoritative
  consumption artefacts.

Documentation Methodology relinquishes ownership of:

- physical current/master locations and management-folder names;
- physical movement of Superseded/Archived files;
- sweep, external-archive and repository-size-management cadence;
- Change Delivery Package staging/completion folders;
- Binder placement, physical replacement/supersession workflow, and analogous generated-artefact
  repository handling; and
- default physical asset holding folders.

Those implementation choices belong to Working Practices or the applicable environment.

**Constraints on implementations.** Physical handling must preserve the semantic state, required
governed history, and enough locator/history information for the corpus to remain truthful. Moving
history outside the active repository is valid; silently treating absence from the active context
as non-existence is not. A local folder convention may still use names such as `_superseded/` or
`_archived/`; those names no longer define the lifecycle state itself.

**Consequences.** The Guide's storage section becomes a lifecycle/disposition section. Literal
repository folders and sweep guarantees are removed from the methodology. Existing repositories do
not need to rearrange their files merely because of this change. Working Practices can now own the
underscore-prefixed management-folder convention and Change Delivery/Binder handling without
competing with Documentation Methodology.

## D21 — Issue the ownership correction as v20 with no artefact migration requirement

**Trigger / problem.** D20 changes the canonical operating contract and therefore cannot replace
issued v19 bytes in place. The established Documentation Methodology release/Standard/Guide version
alignment remains in force.

**Decision.** Issue `AIDE_DocumentationMethodology@v20`,
`AIDE_DocumentationMethodology_Standard_v20.md` and `DocumentationMethodology_Guide_v20.md`.
Declare the v20 transition `None` and retain the v18 `OnUpdate` plus v19 `None` transition history.

**Reasoning.** The release changes ownership and interpretation of physical handling, not the
required structure or content of existing governed documents. A v19-conformant document remains
usable without rewrite. Existing physical folder arrangements may remain as environment/Working
Practices choices.

**Consequences.** No corpus-wide document migration or repository rearrangement is required. Runtime
representations should adopt the v20 Standard on their next normal bundle/build/deployment pass.

## D22 — Generic Index ownership moves to Core

**Trigger / problem.** The established Documentation Methodology Index has become the basis for a
more general need: hierarchical registration of repositories, projects/containers, native
structures and mixed item types. Those semantics are not intrinsically documentation-specific.

**Alternatives considered.** Keep expanding the Documentation Methodology Index; create a separate
ProjectRegister; make Domain own structural registration.

**Decision.** Adopt `AIDE_Index@v1` as the generic Index/Item/Item Type owner in Core.
Documentation Methodology retains only documentation-specific extensions: topic declarations,
Document Register, custom document types, assets/unmanaged document records, history/dead-locator
facts and local documentation configuration.

**Consequences.** A separate `ProjectRegister` is unnecessary. A repository project catalogue is a
generic Index use. Existing documentation Indexes migrate on substantive update rather than by
mass rewrite.

## D23 — Top-level topic replaces project/container as the semantic register anchor

**Trigger / problem.** A chat project/master folder can contain several top-level topics sharing
context. Describing OpenItems/WorkRegister and naming semantics as “project-wide” makes the
container accidentally semantic.

**Decision.** Treat top-level topic as the default semantic anchor. Containers are practical
context/storage boundaries and may contain several top-level topics.

**Consequences.** Filename semantics are described as
`{TopLevelTopic}_{Subtopic...}_{DocType}...`; existing filenames already using that effective
prefix normally need no rename. Standing registers are top-level-topic-wide by default.

## D24 — Add WIP as a distinct high-churn persistence DocType

**Trigger / problem.** Active AI work can develop substantial current context before it belongs in
Design, Decisions, Working or a durable register. Chat/session/platform changes can lose or evict
that thinking.

**Alternatives considered.** Put all current thinking into OpenItems; broaden WorkRegister; broaden
Working to cover both short-lived context checkpoints and substantial exploratory bodies.

**Decision.** Establish **WIP** as a distinct DocType for volatile persisted current-work context.
Its purpose is continuation/currency, not authority or historical preservation.

**Consequences.** WIP may duplicate transiently, is updated frequently, is normally outside the
Binder, and is disposed once useful material has been routed. Visible filename versioning is
retained as a cross-chat/platform currency signal.

## D25 — Working remains a distinct longer-lived exploratory DocType

**Decision.** Working is substantial exploratory/formative material with independent value during
development and is not limited to “Design in progress.” It may exist before the eventual Brief,
Design or destination is even known.

**Reason.** Collapsing Working into WIP would make long-form exploratory reasoning indistinguishable
from short current-context checkpoint state.

## D26 — OpenItems is a live attention register, not historical storage

**Decision.** OpenItems contains only current/pending/deferred/future items still requiring
attention. Resolved items are removed after any durable result is routed to the appropriate owner.

**Reason.** Retaining closed rows creates a second Decisions/history store and makes every visible
entry stop meaning “attention required.”

**Scope.** One OpenItems per top-level topic by default; create/delegate a subtopic register only
when use/volume/cadence justifies it.

## D27 — WorkRegister is the live undelivered-design-consequence ledger

**Decision.** WorkRegister records confirmed downstream consequences/work that are not yet fully
delivered. It is the reconciliation layer between committed Design and actual code/build/document/
production outcomes.

A Design change with a downstream consequence is either fully delivered in the same pass or
recorded in sufficient detail in WorkRegister. There is no third state in which committed Design
changes silently outrun delivery.

**Consequences.** Each live item records what changed, what downstream result must change, where it
lands, WorkPackage/action mapping, current state, returned result if not closed, and remaining work.
Completed items are removed rather than retained as history.

## D28 — WorkPackage may consume part or all of one or more WorkRegister items

**Decision.** WorkPackages identify the WorkRegister obligations they cover. One package may group
several items into a manageable work chunk; one large item may span several packages.

On return, the director reconciles the mapped items. Completed obligations are removed; partial or
blocked items retain returned evidence and what remains. Build does not silently close the source
register.

## D29 — Normal Binders exclude live/high-churn work state

**Decision.** WIP, Working, OpenItems and WorkRegister are excluded from a normal stable/current
Binder by default and loaded separately when active work state is needed.

**Reason.** Including frequently updated live state makes Binders churn and blurs stable project
knowledge with current operational queues.

**Exception.** A deliberately specialised Binder may include live state if its stated purpose
requires it.

## D30 — Messaging owns Message schema/semantics

**Decision.** Messaging owns the AI-MESSAGE envelope/schema, message-specific type semantics and
transport/receipt workflow. Documentation Methodology supplies generic governed-file
naming/lifecycle/metadata hosting only when a message is persisted.

**Reason.** Message field semantics and message process form one communication capability and
should not be split across DocMeth and Messaging merely because a message can become a file.

**Transition.** The existing Messaging corpus is reconciled into the new capability in its owning
pass; current working message conventions remain usable meanwhile.

## D31 — Issue v21 with migration posture None

**Decision.** Publish `AIDE_DocumentationMethodology@v21` and `DocumentationMethodology_Guide_v21`.
The v21 transition posture is `None`.

**Reason.** The canonical operating model changes substantially, but existing governed documents do
not require automatic mass content transformation. Current Indexes/registers adopt the model when
next substantively updated; existing filenames already expressing the top-level topic normally need
no rename.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, DocumentationMethodology_Design_v18
References: DocumentationMethodology_Guide_v21, Core_Index_Decisions_v1, WorkingPractices_Decisions_v5, AIDE_WorkPackage@v2
<!-- END SOURCE: DocumentationMethodology_Decisions_v19.md -->

---

<!-- BEGIN SOURCE: AIDE_DocumentationMethodology_Standard_v21.md -->
# AIDE Documentation Methodology — Standard

> **Identity:** `AIDE_DocumentationMethodology@v21`
> **Common name:** Documentation Methodology
> **Version 21**
> > **Published:** 2026-08-31
> > **Change:** Core Index ownership split; top-level-topic anchor; WIP/Working distinction; live-only registers; WorkRegister/WorkPackage reconciliation.
>
> **Default weight:** Expectation

## Purpose

Provide the canonical AI-facing contract for creating, naming, structuring, recording, versioning,
distributing and maintaining AIDE-governed document corpora while preserving active work safely
and keeping confirmed Design aligned with delivered outcomes.

This Standard is the normal runtime/deployable representation of Documentation Methodology.
`DocumentationMethodology_Guide_v21` is its fuller human-oriented companion.

## Ownership boundary

**Weight: Requirement**

Documentation Methodology owns governed document naming, document types and document-specific
lifecycle, lifecycle state/disposition semantics, top-level-topic/document organisation,
documentation-specific Index extensions, document metadata-container placement,
governed-history preservation, document distribution rules, asset/unmanaged recording, the
authoritative-master/generated-consumption boundary, and document output/version discipline.

Physical repository/storage layout, management-folder names, file movement, sweep/external-archive
cadence, Change Delivery staging and Binder placement/replacement workflow are operating concerns
owned by Working Practices or the applicable environment. Physical location does not define a
document's lifecycle state.

Do not absorb semantics owned elsewhere:

- Core owns formal Identity and generic `AIDE_Index@v1` Item/Item Type/Index behaviour.
- `AIDE_Domain` owns Domain resolution and which semantic Item Types may establish/stop Domain
  propagation.
- `AIDE_Tags` owns Tags content/build/query.
- `AIDE_Dependencies` owns dependency identity, presence, order, version and conformance checkpoints.
- `AIDE_Migration` owns transition discovery/execution/progress.
- `AIDE_Review` owns generic Review lifecycle.
- `AIDE_WorkPackage` / `AIDE_Build` own generic execution/return behaviour.
- Messaging owns Message envelope/schema/threading/receipt/transport behaviour and message-specific
  document semantics.
- Subject-matter owners own substantive document content and top-level-topic/subtopic choices.

Where this Standard hosts another owner's metadata/state, preserve that owner's semantics.

## Core corpus principles

**Weight: Expectation**

1. Keep one authoritative answer per question; reference rather than restate.
2. Route information by state and role: WIP preserves current volatile context; Working preserves
   substantial exploration; OpenItems tracks live unresolved attention; Brief defines; Design
   determines; Decisions records reasoning; WorkRegister tracks confirmed undelivered consequences;
   WorkPackage bounds execution; Outcome returns evidence; Index records structure/current corpus.
3. Treat filenames as legible locators and the applicable authoritative Index as the resolver.
4. Distribute only document types whose distribution contract permits it.
5. Keep human-readable documents as short as their function permits and conclusion-first.
6. A confirmed Design change with a downstream consequence is applied in the same pass or recorded
   in WorkRegister in enough detail to reconcile delivery later.
7. Version issued outputs/checkpoints, not drafting keystrokes.
8. Do not leave material confirmed state or valuable active thinking solely in volatile conversation
   where loss would materially impair continuation.
9. Prefer an existing mechanism over adding another one.

## Naming

**Weight: Requirement**

A chat project, master folder, workspace or similar shared context pool is a **container**. A
container may hold one or more **top-level topics**. The top-level topic, not the container, is the
normal semantic anchor for governed topic documentation and standing registers.

Normal governed Markdown filename:

```text
{TopLevelTopic}_{Subtopic...}_{DocType}[_{Key}]_v{N}.md
```

- Use the top-level-topic filename prefix first.
- Omit subtopic segments for top-level-topic-wide documents/registers.
- Resolve DocType from an established or locally declared custom type.
- Add a key only where the type/working pattern calls for one.
- Keep the version suffix last.
- Compound subtopic segments may express instantiation/subdivision and may nest.
- A filename is not the authoritative type/topic registry; the applicable Index is.
- Existing filenames already using the effective top-level-topic prefix do not require rename merely
  because older methodology called that first slot `Project`.

Cross-references may be deliberately:

```text
abc_Design_v5   # tied to that issued version
abc_Design      # resolves to current
```

Preserve the author's chosen form.

### Point-in-time keys

Use date-sequence `{YYYY-MM-DD}-{N}` where the type requires a dated instance.

- Review: date mandatory; optional single-segment label may follow the date-sequence.
- Working: no key normally; label/date only when the actual working pattern needs it.
- WIP: no key normally; use a subtopic/thread key where several parallel active contexts within one
  top-level topic need independent WIP series.
- WorkPackage: opening date mandatory; a separate WorkPackage Outcome uses the same key.
- Archive marker `_Archived_{date}` is inserted after DocType and before an existing key.

## Document role model

**Weight: Requirement**

```text
WIP
  current volatile persisted context

Working
  substantial exploratory/formative material

OpenItems
  live unresolved/pending/deferred/future attention

Brief / Requirements
        ↓
      Design  ← Decisions
        ↓
     outcomes

WorkRegister
  confirmed downstream consequences still undelivered
        ↓
   WorkPackage(s)
        ↓
      Outcome
        ↓
reconcile WorkRegister
```

- **WIP** — high-churn, non-authoritative current-work checkpoint used so valuable thinking can
  survive chat/session/platform/context loss.
- **Working** — substantial exploratory/formative body worth preserving while it develops; it may
  predate a Brief/Design and may later feed several destinations.
- **OpenItems** — live durable attention still requiring thought/revisit/investigation/progression.
- **Brief** — objective, scope, requirements, success signals; optional by stakes.
- **Requirements** — standing cross-topic requirements when size warrants splitting from Brief.
- **Design** — confirmed current position; declares produced outcomes and external handlers.
- **Decisions** — reasoning/history informing future Design. It is not a downstream outcome input.
- **Review** — faithful point-in-time assessment record. Generic Review behaviour comes from
  `AIDE_Review`.
- **Guide** — distributable explanatory outcome.
- **Reference** — distributable lookup outcome.
- **Glossary** — distributable definitions.
- **Overview** — standing narrative/orientation outcome.
- **WorkRegister** — confirmed downstream work/consequences that remain undelivered.
- **WorkPackage** — document representation of a bounded unit of Build work; execution semantics are
  `AIDE_WorkPackage`.
- **WorkPackage_Outcome** — separate live return document where used; folds into WorkPackage on
  archival.
- **Message** — Messaging-owned transmission/message semantic type; this methodology supplies only
  generic governed-file integration when persisted.
- **Index** — generic structural registration under `AIDE_Index@v1` plus documentation-specific
  extensions defined here.
- **Asset / Unmanaged** — explicitly outside normal governed document-type behaviour.

An outcome must have an authoritative defining source. Decisions never substitutes for missing
Design content.

## Condensed and expanded topic documents

**Weight: Guidance**

A small subtopic may hold its internal Brief/Design/Decisions/Working material in one condensed
file. Use the highest-order confirmed content as its DocType.

Expand when retrieval, independent edit cadence, Working disposition, blind review, or explicit
instruction makes separation valuable.

Generic Index remains structural. Documentation-specific Document Register and top-level-topic
standing WorkRegister remain outside a condensed subtopic file. OpenItems may be top-level-topic
wide by default or delegated to a subtopic when volume/cadence warrants it. A Guide does not
condense into its Design because they have different roles/distribution.

## WIP

**Weight: Expectation**

Use WIP when active thinking/current work state must survive interruption, chat/session context
loss, platform switching or another likely context discontinuity and is not yet safely represented
elsewhere.

WIP may contain current position, reasoning not yet routed, draft fragments, candidate OpenItems or
WorkRegister consequences, source pointers and a clear resume point. Temporary duplication is
allowed because WIP is a continuity checkpoint, not an authoritative source.

Draft freely inside one editing context. When issuing/persisting a checkpoint for reuse, sync or
resumption, increment `_vN` so the filename visibly signals currency. A replaced issued checkpoint
becomes Superseded.

WIP is normally outside the stable Binder and normally withdrawn/disposed after its useful content
has been routed. Archive only where the WIP itself has unusual independent historical value.

## Working

**Weight: Expectation**

Working is substantial exploratory/formative material that is useful to preserve independently
while it develops. It is **not limited to Design in progress**: an idea, review fallout, research or
other substantial block may exist for some time before its eventual authoritative destination is
known.

Working may later feed Design, Decisions, Brief, Reference, proposal, Review response or several
owners. Do not leave Working as a competing source once material confirms elsewhere.

On completion, resolve disposition: **Archived** where the Working record itself has independent
historical/research value; otherwise **Superseded/withdrawn** where its substantive value is fully
represented in retained authoritative records. Physical handling belongs to Working
Practices/environment.

Normal stable Binders exclude Working by default; load it separately when active/exploratory state
is needed.

## Decisions

**Weight: Requirement**

Decisions preserves **synthesized substantive reasoning for a future Design reader**, not only the
final outcome. Preserve enough of the path to reconstruct why the confirmed position exists
without turning the record into a transcript. As applicable and proportionate, include the
trigger/requirement, problem found, alternatives genuinely considered, key distinctions/reasoning,
decision, and important consequences/trade-offs.

A Decisions event is owed when:

- the confirmed substantive Design position changes;
- a requirement is established or materially revised; or
- a rejected alternative could reasonably be re-derived and reconsidered later.

Purely editorial, formatting, metadata, migration, mechanical maintenance, or application of an
already-recorded decision does not by itself create a new Design decision. A genuinely trivial
alternative may be omitted; otherwise a rejected alternative receives at least a brief reason.
Proportionality controls depth, not whether a substantive event disappears from the record.

Produce a substantive Design change and its Decisions record in the same pass. Assemble the entry
from the reasoning actually developed while it is available; confirmed reasoning at material risk
of being left only in conversation overrides ordinary restraint on document output.

Existing entries are historical and are not retroactively rewritten. Later entries may supersede,
refine, reverse, constrain, or reinterpret an earlier decision while leaving the earlier record
intact.

Keep Decisions at Design granularity. An independently expanded child Design normally keeps its
substantive reasoning in a Decisions record at that same scope; a condensed topic may use a
Decisions section. Parent-level architectural reasoning remains parent-level.

Split Decisions history only when retrieval quality deteriorates or unrelated settled history
obscures the live record. Prefer closure/state-based volumes with pointers over arbitrary
chronological trimming. Do not delete or rewrite history merely to shorten the active file.

Decisions informs future Design and is **not** an input to downstream outcomes. If a consideration
is required for correct implementation or delivery, it must be represented in the current Design
or other authoritative downstream input.

## Review document integration

**Weight: Requirement**

A governed Review document is a faithful point-in-time assessment record.

Do not rewrite a finding's substantive text because it was later resolved/disputed. Record
resolution/status separately. Archive according to the document lifecycle once its findings meet
the archival condition.

Use `AIDE_Review@v1` for the assessment lifecycle itself; this Standard governs only the document
representation/lifecycle.

## Message document integration

**Weight: Requirement**

Messaging owns Message schema/fields, envelope/thread identity, revision, source marking,
receipt/reconciliation state, light/heavy promotion criteria and transport workflow.

Documentation Methodology does **not** duplicate that schema.

When Messaging promotes a Message to a governed file, apply the generic document behaviours owned
here—filename/version placement, Current/Superseded/Archived lifecycle, metadata-container hosting,
governed-history handling and distribution integration—except where the Messaging-owned Message
contract deliberately specifies a message-specific rule.

A light conversation-only message is not required to become a governed document.

## Index

**Weight: Requirement**

Use `AIDE_Index@v1` for generic Index/Item/Item Type semantics.

Documentation Methodology contributes documentation-specific Index sections/properties where
applicable:

- top-level-topic/subtopic declarations and documentation relationships;
- Document Register and current document version/type/lifecycle facts;
- local/custom document type definitions;
- document assets/unmanaged-file records;
- withdrawn/renamed/rehomed/dead-locator mappings; and
- documentation-local configuration.

### DocumentationTopic Item Type

`DocumentationTopic` is a Documentation Methodology-owned semantic Item Type representing one
self-describing **top-level documentation topic**. Identification relies on authoritative topic/Index
declarations rather than folder naming alone.

A parent/repository Index may register and describe a DocumentationTopic, locate it and stop at that
self-describing boundary. A physical container may hold one or several DocumentationTopics.

Defining the Item Type does not grant Domain authority. `AIDE_Domain` alone decides whether a type
is Domain-capable/domain-defining.

The documentation Index is authoritative for the documentation registration/configuration facts it
owns; registration does not make it authoritative for another Item's internals.

## OpenItems and WorkRegister

**Weight: Expectation**

### OpenItems

OpenItems is the durable **live attention register**: current, pending, deferred or future items
whose loss would matter and which still require thought, revisit, investigation or progression.

- Default one OpenItems register per **top-level topic**.
- Create/delegate a subtopic register only when use/volume/cadence materially warrants it.
- Keep entries concise enough to resume; use WIP/Working for substantial active material.
- When resolved, route any durable outcome appropriately and remove the item.
- Do not maintain a closed-items/tombstone archive inside OpenItems.

### WorkRegister

WorkRegister is the top-level-topic-wide live queue/ledger of **confirmed downstream consequences or
work not yet fully delivered**. It is the reconciliation layer between committed Design and
delivered reality, not merely a generic backlog.

Whenever confirmed Design changes, determine whether downstream code/build/document/production
outcomes must change. Every such consequence shall either be fully delivered in the same pass or be
recorded in WorkRegister.

Record enough detail to determine later whether the committed Design has actually been delivered,
including as applicable:

```text
ID
source/triggering Design change
committed change
specific required downstream changes
target outcomes/locations
current delivery state
WorkPackage/action mapping
returned result while still open
remaining work
```

One WorkPackage may cover some/all of several WorkRegister items; one WorkRegister item may be split
across several WorkPackages. Completed items are removed after reconciliation. Do not retain
completed rows as a second Decisions/Outcome history.

Default one WorkRegister per top-level topic. Delegate only where an independently useful subtopic
queue is justified by volume/cadence.

## Binder and live-state treatment

**Weight: Expectation**

A normal Binder is a stable/current knowledge consumption artefact, not a live work queue. Exclude
by default:

```text
WIP
Working
OpenItems
WorkRegister
```

Load these separately when resuming/managing active work. A specialised live-state Binder is valid
only when deliberately designed for that purpose.

Do not reintroduce the same churn through Index. Individual live-state versions may be omitted from
the stable Document Register; where discovery benefits, an Index may hold a compact version-agnostic
`Live state` series/locator entry (for example `Capabilities_Messaging_WIP`). The current checkpoint
version is established from the actually available/current file, not an old Index row. Reissuing a
new `_vN` in the same live series therefore does not itself require an Index/Binder issue. Reconcile
series creation/withdrawal at the next normal corpus/output checkpoint.

## Lifecycle, supersession and archival

**Weight: Requirement**

Lifecycle state is independent of storage representation:

- **Current** — the issued authoritative version/instance the corpus resolves for normal current use.
- **Superseded** — an older issued version, or a document displaced/withdrawn without reaching an
  archival terminal disposition of its own.
- **Archived** — a document whose type-specific lifecycle reaches an archival terminal disposition;
  the final archival record is frozen except through the type's permitted correction route.

A type may define completion, withdrawal, absorption or another terminal path that determines the
correct disposition. The `_Archived_{date}` filename marker remains the document-naming expression
for an archival disposition where that convention applies.

Generated Binders/Bundles are consumption artefacts assembled from authoritative sources; they are
not authoritative masters. Regenerate them from their source set rather than editing them as the
source of truth.

Do not discard governed history merely to simplify the active view. A living current-document
register need not list every lower Superseded version where version sequence already proves their
existence, but preserve explicit mapping for renamed/rehomed/withdrawn names and enough archived
history/locator information to keep the corpus truthful.

Physical storage may use repository folders, external archives, a document-management system,
platform-native history or another representation. The applicable Working Practices/environment
owns physical placement, movement, retention media and cleanup; those choices must not erase the
semantic state or required governed history.

## Metadata containers

**Weight: Requirement**

Document layout may contain:

```text
Title / version preamble
Header metadata
Temporary owner-labelled state
Body
Footer metadata
Internal section
```

Header metadata is immediately after title/version preamble. Temporary state follows header
metadata and precedes ordinary body content. Footer metadata follows body and precedes the Internal
section where present.

Known properties:

```text
Identity: ...
Tags: ...
Dependencies: ...
References: ...
Type: ...
```

This list is extensible.

- Identity semantics belong to Core.
- Tags semantics belong to `AIDE_Tags`.
- Dependencies semantics belong to `AIDE_Dependencies`.
- Migration state semantics belong to `AIDE_Migration`.
- References is a document citation relationship without conformance semantics.
- Custom-type pointer/rendering remains a Documentation Methodology concern.

Keep generated metadata/state compact.

## Internal section

**Weight: Guidance**

Use an Internal section for durable bookkeeping that helps later maintainers but is not part of
the document's distributed substantive body, such as delivery/correction notes, absorbed-document
pointers or other lifecycle trace information defined by this methodology.

Do not use Internal as a hidden second body for substantive rules.

## Distribution

**Weight: Requirement**

Distribution follows document type and project policy.

Internal working/decision/register material does not travel merely because it is useful context.
Published outcomes such as Guides/References/Standards may travel according to their contract.

A consuming project may adopt a distributed Guide/Reference as a resource without becoming its
owner.

## Assets

**Weight: Expectation**

An Asset is produced/held by the corpus but its filename is fixed by the consuming tool/system
rather than by this document naming convention.

Record enough ownership, path, purpose/currency/lifecycle information in the Index/assets register
to manage it truthfully.

Do not rename an Asset into the document naming convention merely for aesthetic consistency.
Use Reference instead only where the file is actually a governed lookup document whose filename
the corpus owns.

## Unmanaged files

**Weight: Expectation**

An unmanaged file is held by the container but deliberately not governed by this methodology.

Record it in the Index with management=`unmanaged`, filename and recorded date. Optional attributes
such as purpose, editable posture, versioned posture, source and lifecycle are recorded only when
established; unknown values are stated as not established rather than guessed.

A type-looking segment in an unmanaged filename does not confer governed type/version/lifecycle
behaviour.

Review/prompt cadence for unmanaged files is owned by the process/interface that manages the
container, not by this Standard.

## Claimed versus verified

**Weight: Requirement**

Do not compose plausible metadata, times, versions, paths, delivery facts or successor names where
the fact should be observed/read.

Distinguish:

- verified/read state;
- declared/claimed state; and
- unknown/unestablished state.

Where the system cannot verify a mandatory value, represent that limitation explicitly.

## Output and version discipline

**Weight: Requirement**

A file's `_vN` counts issued outputs/checkpoints, not internal editing operations.

- Draft freely before issue.
- After an issued/delivered document is changed and reissued, increment its document version.
- A rename alone is not a semantic content revision unless the governing lifecycle explicitly
  makes it one.
- Do not issue new versions/documents as ceremony.
- WIP is intentionally versioned when a persisted continuity checkpoint is issued so filename
  currency is visible across chat/project/platform contexts.
- Produce a substantive Design change and its Decisions record in the same pass; editorial or
  mechanical Design maintenance does not create a Decisions event by itself.
- For every confirmed Design change, identify downstream consequences. Apply them in the same pass
  or record the undelivered consequences in WorkRegister.
- At the end of a material work unit or key confirmation point, assess whether confirmed state or
  valuable active thinking is at risk of being left only in volatile conversation/context.
- Where state is materially at risk, preserve it using the least-heavy correct mechanism—often WIP
  for current context—then consolidate normal deliverable output at the appropriate checkpoint.

## WorkPackage document integration

**Weight: Requirement**

Generic WorkPackage authoring/execution/validation/return semantics come from
`AIDE_WorkPackage@v2` and `AIDE_Build@v4`.

This Standard owns document integration:

- the WorkPackage is a governed point-in-time document with opening-date key;
- a separate live WorkPackage Outcome uses the same key where produced;
- when a WorkPackage is sourced from WorkRegister, it identifies the covered item IDs and the
  authorised portion of each obligation;
- the Outcome reports result/evidence/remaining work for those mappings;
- the director/owning process reconciles the returned evidence against the WorkRegister and current
  Design—Build does not silently close the register;
- after reconciliation, a returned Outcome may be appended verbatim to the WorkPackage before
  archival where that lifecycle is used; and
- design-shaping issues returned by Build are resolved by Project Design rather than silently
  settled by document mechanics.

## Documentation Methodology conformance

**Weight: Requirement**

Current conformance is recorded through Dependencies:

```text
Dependencies: !AIDE_DocumentationMethodology@v21
```

The dependency version is the last saved/proven Documentation Methodology capability release
against which the document is conformant.

A newer methodology release does not itself rewrite all existing documents. Migration posture
determines when the checkpoint advances.

### Legacy v17 checkpoint bridge

For the **v17 → v18 transition only**:

If all of the following are true:

1. the document is a governed pre-v18 document;
2. it has no resolved `AIDE_DocumentationMethodology` dependency checkpoint; and
3. it contains an unambiguous legacy `Methodology: v17` declaration,

then Migration shall interpret that legacy declaration as the starting conformance checkpoint
`AIDE_DocumentationMethodology@v17`.

This interpretation:

- is a compatibility input to Migration only;
- does not change the document on read/use;
- does not create a modern dependency declaration until a qualifying save/update succeeds; and
- must fail visibly rather than guess if multiple/contradictory legacy methodology declarations
  exist.

### v18 transition

```yaml
MigrationSummary:
  CurrentVersion: v21
  LatestRequiredVersion: none
  LatestOnUpdateVersion: v18
  SupportedBaseline: v17

Transition:
  Version: v18
  Posture: OnUpdate
  Change: >
    Move document conformance to AIDE_Dependencies, adopt extensible metadata/state containers,
    and delegate generic WorkPackage execution semantics to AIDE_WorkPackage.
  Items:
    - Resolve the starting checkpoint using Dependencies or the legacy-v17 bridge.
    - Replace the legacy Methodology: v17 checkpoint with !AIDE_DocumentationMethodology@v18.
    - Convert legacy Depends on relationships that are true conformance dependencies to Dependencies: syntax.
    - Preserve References as citations where no conformance obligation exists.
    - Host Identity, Tags and temporary owner state under the v18 container placement rules where present.
    - Preserve unrelated content; do not rewrite merely to make the document look newer.
  Success: >
    The saved document uses v18 metadata placement where applicable, records a truthful
    AIDE_DocumentationMethodology@v18 dependency checkpoint, and has no contradictory legacy
    Methodology footer.

Transition:
  Version: v19
  Posture: None

Transition:
  Version: v20
  Posture: None

Transition:
  Version: v21
  Posture: None
```

Merely reading/using a v17 document does not trigger the v18 OnUpdate transition. v19, v20 and v21
require no additional artefact transformation; when Migration traverses through current during a
qualifying save, their None transitions may advance the saved checkpoint after the v18 success
condition is satisfied.

An operation specifically requiring a v18-only structure may require migration before that
operation proceeds.

## Build and deployment

**Weight: Context**

This Standard is the canonical deployable Documentation Methodology outcome.

Platform Build may render it as a skill, plugin contribution, bundle member, instructions or
another supported representation without changing semantics.

The common AIDE Standards/Tools Bundle is a valid assembled representation. The human Guide is not
required in every consuming project once this Standard is available there, though it may be added
when richer explanatory context is useful.

---
Dependencies: AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_Tags@v1, AIDE_WorkPackage@v2, AIDE_Build@v4
References: DocumentationMethodology_Design_v18, DocumentationMethodology_Guide_v21
<!-- END SOURCE: AIDE_DocumentationMethodology_Standard_v21.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Guide_v21.md -->
# Documentation & Workflow Methodology — Guide

> **Identity:** `AIDE_DocumentationMethodology@v21`
> **Version 21** (2026-08-31). Human-oriented companion for the Core Index ownership split,
> top-level-topic model, WIP/Working distinction, live registers and Design-to-delivery
> reconciliation.
>
> **Migration posture:** None for v21. Existing governed documents do not require mass rewrite or
> rename solely because this release changes the canonical conceptual model.

## v21 change summary

- **Generic Index moved to Core.** `AIDE_Index@v1` owns generic Item/Item Type/hierarchy/extension
  hosting. Documentation Methodology owns documentation-specific Index sections and the
  `DocumentationTopic` top-level-topic type.
- **Top-level topic is the semantic anchor.** A chat project/master folder is a container and may
  hold several top-level topics.
- **WIP is now a distinct DocType.** It preserves volatile current work context cheaply across
  interruptions, sessions and platforms.
- **Working stays distinct.** It is substantial exploratory/formative material that may live much
  longer and may precede any Design.
- **OpenItems is live-only.** Resolved items leave the register rather than accumulating as history.
- **WorkRegister is the undelivered-design-consequence ledger.** It links committed Design to actual
  implementation/output and tracks WorkPackage allocation/return until delivered.
- **Normal Binders exclude WIP, Working, OpenItems and WorkRegister.** Load live state separately.
- **Messaging owns Message schema/semantics.** DocMeth supplies only generic governed-file
  integration for persisted messages.

## 1. The core rule: route information by state

The methodology is easiest to use if each document answers a different question:

| State | Document | Main question |
|---|---|---|
| Current volatile context | `WIP` | What do I need to continue this active work safely? |
| Substantial exploration | `Working` | What thinking/material is being developed before its final home is known? |
| Live attention | `OpenItems` | What still needs attention/revisit/thought? |
| Confirmed model | `Design` | What is the current confirmed position? |
| Reasoning/history | `Decisions` | Why did the confirmed position become this? |
| Confirmed undelivered work | `WorkRegister` | What committed consequence is still owed? |
| Bounded execution | `WorkPackage` | What is Build authorised to deliver now? |
| Execution evidence | `Outcome` | What was actually delivered/observed? |
| Structural map | `Index` | What significant things are registered here and where? |

The most important practical test is:

> **Do not lose thinking, but do not turn every transient thought into permanent history.**

WIP is the cheap capture layer that makes those two goals compatible.

## 2. Container versus top-level topic

A **container** is a practical context/storage boundary: a chat project, master folder, workspace or
similar pool of shared material.

A container may hold more than one top-level topic because the topics benefit from the same context.
The container is therefore not automatically the semantic scope of registers.

Default structure:

```text
Container
├── Top-level Topic A
│   ├── Index/document set
│   ├── OpenItems
│   └── WorkRegister
└── Top-level Topic B
    ├── Index/document set
    ├── OpenItems
    └── WorkRegister
```

Many current AIDE containers happen to be 1:1. Do not turn that convenience into a rule.

## 3. Naming

Normal governed Markdown filename:

```text
{TopLevelTopic}_{Subtopic...}_{DocType}[_{Key}]_v{N}.md
```

Examples:

```text
Capabilities_Design_v9.md
Capabilities_Review_Design_v2.md
Capabilities_WIP_v3.md
Capabilities_Messaging_Working_v2.md
Core_WorkRegister_v1.md
```

The earlier methodology described the first slot as `{Project}`. Most existing filenames already
use the top-level topic there, so the conceptual correction normally requires no rename.

The version suffix is last. It counts issued/persisted outputs, not every edit.

## 4. WIP — current active work persistence

### Purpose

Use WIP to preserve **the current working context** when losing the conversation/session/platform
cache would make continuation materially harder.

Typical content:

```text
Current position
Current thread/problem
Important reasoning not yet represented elsewhere
Draft fragments/candidate wording
Candidate OpenItems
Candidate WorkRegister consequences
Relevant source pointers
Resume from here
```

WIP can be rough. It is allowed to duplicate content temporarily because its job is safe
continuation, not authoritative publication.

### When to checkpoint

Useful triggers include:

- before ending a material work session;
- before switching chats/projects/platforms;
- before changing to unrelated work likely to displace context;
- after a substantial reasoning block not yet represented durably;
- when an AI judges context loss/eviction would be costly; or
- when the user explicitly wants a current physical context file.

Do not update on every conversational turn merely because WIP exists.

### Versioning

Visible filename versioning is intentional:

```text
Capabilities_Messaging_WIP_v5.md
```

It lets a person or AI verify that the file loaded into a project/context is the latest issued
checkpoint even when the UI does not make replacement/sync state obvious.

Edit freely inside the current context. When issuing a new checkpoint for reuse/sync/resumption,
increment `_vN`; the previous checkpoint becomes Superseded.

### End of WIP

At a useful checkpoint route its contents:

```text
still unresolved and durable → OpenItems
large coherent exploration   → Working
confirmed model              → Design
material reasoning           → Decisions
confirmed work owed          → WorkRegister
transient/no longer useful   → discard
```

Once the WIP has no continuation value, withdraw/dispose it. Archive only exceptionally where the
WIP itself has unusual independent historical value.

## 5. Working — substantial exploratory/formative work

Working is **not simply Design in progress**.

It is a substantial body of thinking/material that has become worth preserving independently while
its eventual authoritative form may still be unknown.

Examples:

- an idea worked over several sessions before a Brief exists;
- a concept/review response that may later split across Design and Decisions;
- research plus emerging model not ready to commit;
- a substantial proposal whose eventual document class is not yet clear.

Working can last days/weeks/months. It may be repeatedly reworked, split and reframed.

When it resolves:

- move current confirmed state to the appropriate authoritative source;
- move material reasoning to Decisions where warranted;
- move remaining live attention to OpenItems;
- move confirmed delivery obligations to WorkRegister; then
- Supersede/withdraw Working if fully absorbed, or Archive it if the Working artefact itself remains
  independently valuable.

## 6. OpenItems — live durable attention

OpenItems answers:

> **What must not be forgotten and still needs attention?**

It may contain:

- open questions;
- current/pending/future tasks not yet confirmed delivery obligations;
- ideas/concepts not yet ready for Design;
- deferred concerns;
- investigations/reminders;
- pending review/message threads; and
- pointers to active WIP/Working.

Keep enough context to resume, but do not turn the register into a Working document.

### Scope

Default: one OpenItems register per top-level topic.

Create/delegate a subtopic register only when the amount/cadence of live state makes that easier to
use. Do not create one merely because a child topic exists.

### Closure

Every visible row means attention is still required.

When resolved:

1. preserve any genuinely durable outcome in its proper owner (Design/Decisions/etc.);
2. create WorkRegister consequence if confirmed delivery remains; and
3. remove the OpenItem.

Do **not** retain closed rows, strikethrough archives or a permanent closed-items section merely for
history. Git/file history can answer forensic questions; the live register should answer what still
needs attention now.

If identifiers are used, non-reuse is a reasonable local convention for stale-reference safety but
is not a v21 requirement.

## 7. WorkRegister — confirmed work and undelivered Design consequences

WorkRegister answers:

> **What have we already committed to that is not yet fully delivered?**

This is stronger than a generic backlog.

### Hard Design consequence rule

Whenever confirmed Design changes, ask:

```text
Does this change require any downstream code/build/document/production outcome to change?
```

If no: nothing is owed.

If yes:

```text
fully delivered in the same pass? → done
not fully delivered?              → WorkRegister
```

There is no safe third state where Design says one thing and production silently remains on an
older outcome with no record of the gap.

### Entry depth

The entry must be detailed enough to reconcile delivery later. A useful shape is:

```markdown
## WR23 — Implement revised equality semantics

Status: In progress

Source:
Json_Design — equality section / decision reference

Committed design change:
Unknown properties are preserved but excluded from semantic equality unless recognised.

Required outcome changes:
- Update equality comparer.
- Update hash-code behaviour.
- Add/modify tests.
- Review diff semantics for consistency.

WorkPackages:
- WP-31 — comparer + tests — Complete
- WP-34 — diff review — Pending

Returned result:
WP-31 completed comparer/tests successfully.

Remaining:
Diff semantics still require reconciliation.
```

Do not make the WorkRegister duplicate the full implementation plan. It records the **obligation
and delivery reconciliation**, while WorkPackage owns the bounded execution contract.

### WorkPackage mapping

One WorkPackage can cover several WorkRegister items to create a manageable work chunk.

One large WorkRegister item can be delivered through several WorkPackages.

The package should identify the relevant item IDs and which portion of each obligation it covers.

On Outcome return, the director reconciles the register:

- fully delivered → remove item;
- partial → record returned result and remaining work;
- blocked → record blocker/remaining; or
- design problem → return to Project Design, then revise/re-authorise work appropriately.

The closed WorkRegister row is not retained merely as history. Durable Design/Decisions/Outcome
records already own what should survive.

## 8. Design and Decisions

Design remains the current confirmed answer.

Decisions records synthesized reasoning needed to understand why that answer exists and what
credible alternatives were rejected. It is not a transcript and is not an input to downstream
outcomes.

A Decisions event is owed for:

- substantive confirmed Design change;
- requirement established/materially revised; or
- credible rejected alternative a future reader could reasonably re-derive.

Editorial/formatting/metadata/migration/mechanical maintenance alone does not create a Decisions
event.

Produce substantive Design and Decisions reasoning together so the “what” and “why” do not become
separated by context loss.

## 9. Generic Index and documentation extensions

Generic Index is now `AIDE_Index@v1` in Core.

Its minimum shape is:

```text
Index identity/scope
Contents — hierarchical significant Items
owner-defined extension sections
```

A generic Index is authoritative for its registrations and Index-owned facts, not for the internals
of every thing it lists.

### Documentation extensions

Documentation Methodology contributes, where applicable:

- topic declarations;
- Document Register;
- custom document type declarations;
- assets/unmanaged documentation records;
- rename/rehoming/dead-locator history; and
- local documentation configuration.

This means a documentation Index can look like:

```markdown
# Capabilities — Index

`{scope: "AIDE/Capabilities", type: DocumentationTopic}`

## Contents
...

## Documentation
### Top-level topics
...
### Document register
...
### Local configuration
...
```

### DocumentationTopic

`DocumentationTopic` is a semantic Item Type owned by Documentation Methodology. It identifies
one self-describing **top-level documentation topic**, not the chat project/master folder that may
happen to contain it.

A repository/root Index can register a DocumentationTopic, give enough description/location to
select it, and stop. The topic resolves its own governing Index/document register. Where one
physical container hosts several top-level topics, the Index may show the container structurally
with several distinct DocumentationTopic Items beneath it.

Domain decides whether that type is Domain-capable; the type does not self-assign Domain authority.

## 10. Binder, Index and live-state churn

A normal Binder answers:

> What stable/current knowledge should a consuming AI load for this topic?

That is different from:

> What are we actively working on right now?

Normal Binders therefore exclude:

- WIP;
- Working;
- OpenItems; and
- WorkRegister.

When resuming work, load the Binder **plus** the relevant live-state files.

### Do not make the Index a back door for WIP churn

If every `Capabilities_Messaging_WIP_v5 → v6` checkpoint forced the Index to update its Document
Register, and every Index update forced a Binder rebuild, excluding WIP from Binder would achieve
nothing.

So live-state documents use a deliberately lighter Index relationship:

```text
stable Document Register
    → authoritative/stable corpus documents

optional Live state section
    → active series/locator, version-agnostic
```

Example:

```markdown
### Live state

- `Capabilities_Messaging_WIP` — current Messaging work checkpoint.
- `Capabilities_OpenItems` — live attention register.
```

The current issued version is read from the actually available file (`..._v7.md`), not inferred
from an old Index row. Reissuing `_v7` as `_v8` in the same series therefore does **not** require an
Index or Binder issue.

Creation/withdrawal of a live-state series is reconciled at the next normal corpus/output
checkpoint. The generic Index contract permits this because an Index registers significant Items;
it does not have to enumerate every physical file.

A specialised live-state Binder remains possible if a workflow deliberately needs one.

## 11. Message ownership

The existing AI-MESSAGE system has outgrown document-schema ownership by Documentation
Methodology.

Messaging owns:

- message type/envelope fields;
- identity/threading/revision semantics;
- source marking;
- receipt/reconciliation state;
- messaging commands/workflow; and
- light/heavy message persistence criteria.

Documentation Methodology only supplies generic governed-file behaviour when a message is promoted
to a file: version/lifecycle/metadata hosting and any common naming rules that Messaging chooses to
consume.

The Messaging capability is reconciled in its own pass; v21 establishes the ownership boundary.

## 12. Lifecycle and storage

Lifecycle is semantic:

- **Current** — authoritative for normal current use;
- **Superseded** — replaced/displaced older issue;
- **Archived** — type-specific terminal historical record.

Physical folders/storage do not create those states. Working Practices/environment decides how the
current repository realises them.

## 13. Migration to v21

v21 has posture `None`.

Do not mass-rewrite current documents simply because:

- the generic Index owner moved to Core;
- the conceptual filename slot is now called TopLevelTopic instead of Project; or
- WIP/live-register semantics were improved.

When an existing Index/OpenItems/WorkRegister/Working document is next substantively updated, use
the current v21 model.

Current AIDE foundation projects may be migrated together as an explicit consolidation pass.

## 14. Practical summary

Use this small mental model:

```text
Don't lose current thinking       → WIP
Substantial thinking needs a home → Working
Don't forget unresolved attention → OpenItems
Confirmed answer                  → Design
Why                               → Decisions
Confirmed delivery still owed     → WorkRegister
Execute a manageable chunk        → WorkPackage
What actually happened            → Outcome
What exists / where to go         → Index
```

That separation is the point. It lets the system preserve knowledge without making every document a
history, queue, scratchpad and source of truth at the same time.

---
Dependencies: AIDE_Index@v1, AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_WorkPackage@v2
References: DocumentationMethodology_Design_v18, AIDE_DocumentationMethodology@v21, WorkingPractices_Design_v5
<!-- END SOURCE: DocumentationMethodology_Guide_v21.md -->
