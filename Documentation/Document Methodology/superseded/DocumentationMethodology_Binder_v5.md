# Documentation Methodology Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 5** (2026-09-01). Review B R1 remediation: assembles the v24 current masters
> implementing the accepted documentation/work-state findings without adopting Review C / Dependencies policy.

## Binder manifest

- `DocumentationMethodology_Index_v9.md` — sha256 `4ce7ab063603`
- `DocumentationMethodology_Design_v21.md` — sha256 `842392a30ccf`
- `DocumentationMethodology_Decisions_v22.md` — sha256 `91a27e8a9992`
- `AIDE_DocumentationMethodology_Standard_v24.md` — sha256 `129c0cd2b877`
- `DocumentationMethodology_Guide_v24.md` — sha256 `943a4193e980`

---

<!-- BEGIN SOURCE: DocumentationMethodology_Index_v9.md -->
# Documentation Methodology — Index

> **Version 9** (2026-09-01). Review B R1 remediation: advances the current Documentation
> Methodology corpus to v24 and records the clarified work-state/discoverability semantics.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v24}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v9 | Index | Current |
| `DocumentationMethodology_Design` | v21 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v22 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v24 | Standard | Current; identity `AIDE_DocumentationMethodology@v24` |
| `DocumentationMethodology_Guide` | v24 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v24` and consumed through `AIDE_Index@v2`.

A DocumentationTopic is the logical boundary/scope of one top-level documentation topic. Its
governing Index declares/describes that logical Item and is used to recognise and resolve its
Document Register; the Markdown Index file is not itself the semantic boundary. Subtopics remain
subordinate structures rather than separate DocumentationTopics. A chat project/master folder may
host one or several top-level DocumentationTopics. `AIDE_Domain` alone decides whether the Item Type
may establish or participate in Domain resolution.

### Migration state

- v18 — `OnUpdate` legacy structure/conformance transition.
- v19 — `None`.
- v20 — `None`.
- v21 — `None`; new Index/work-state/topic semantics apply prospectively/on substantive update.
- v22 — `None`; `DocumentationTopic` clarification and root-WIP series rule apply prospectively.
- v23 — `None`; current generic Index consumption/conformance corrected to `AIDE_Index@v2`.
- v24 — `None`; Review B R1 work-state/discoverability/owner-seam clarifications.

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v8` | `DocumentationMethodology_Index_v9` |
| `DocumentationMethodology_Design_v20` | `DocumentationMethodology_Design_v21` |
| `DocumentationMethodology_Decisions_v21` | `DocumentationMethodology_Decisions_v22` |
| `AIDE_DocumentationMethodology_Standard_v23` | `AIDE_DocumentationMethodology_Standard_v24` |
| `DocumentationMethodology_Guide_v23` | `DocumentationMethodology_Guide_v24` |

---
Dependencies: !AIDE_DocumentationMethodology@v24, AIDE_Index@v2, DocumentationMethodology_Design_v21
References: DocumentationMethodology_Guide_v24
<!-- END SOURCE: DocumentationMethodology_Index_v9.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Design_v21.md -->
# Documentation Methodology — Design

> **Version 21** (2026-09-01). Review B R1 remediation: clarifies WorkRegister admission and
> reconciliation, WIP thread exit, Working discoverability, OpenItem negative closure, and the
> Documentation Methodology / Working Practices owner seam.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## §1 — Purpose and ownership

Documentation Methodology provides the common document/corpus contract for AIDE-governed work.

It owns:

- governed document naming and filename structure;
- document types and document-specific lifecycle/disposition;
- lifecycle state meanings including Current, Superseded and Archived;
- WIP/Working/OpenItems/WorkRegister semantic meanings, routing/lifecycle meanings and
  authority/non-authority boundaries;
- Binder/live-state semantic treatment and documentation-specific discoverability requirements;
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
- operational checkpoint/output timing, practical cross-context transfer/sync, or physical
  repository/storage workflow — Working Practices/environment;
- formal identity — Core;
- Tags/Dependencies/Migration/Review semantics — their owners;
- generic WorkPackage execution/return — Build/WorkPackage;
- Messaging envelope/schema/transport behaviour — Messaging; or
- platform packaging/deployment mechanics.

The governing rule remains one semantic owner per mechanism. Documentation Methodology may explain
how its document states participate in an operating workflow, but operational timing/transfer/file
handling is non-normative here and is resolved by Working Practices or the environment.

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
  confirmed work owed by the owning top-level topic and not yet fully delivered
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

Use it when volatile current context needs a document representation and is not yet appropriately
represented elsewhere. WIP may hold:

- current position and active thread;
- reasoning/thinking not yet routed;
- draft fragments;
- candidate OpenItems or WorkRegister obligations;
- current source pointers; and
- a resume point.

WIP is not authoritative and temporary duplication is acceptable.

There is one current WIP series per top-level topic in the normal AIDE workflow. Its canonical
filename is:

```text
{TopLevelTopic}_WIP_v{N}.md
```

Do not create independent subtopic/thread WIP series. When several active subtopics or threads
coexist, preserve their identity inside the top-level WIP using concise internal sections such as
`Active thread — Messaging` or `Active thread — Architecture Review B`.

A WIP thread has its own exit rule. Once an `Active thread — ...` section's useful material is
safely routed to the appropriate owners, remove that thread from the **next** WIP checkpoint. Routed
material must not accumulate indefinitely beside still-active continuation state. Withdraw/dispose
the whole WIP series only when no active continuation thread remains, subject to the exceptional
archival rule in §7.

### Working

`Working` is substantial exploratory/formative material worth preserving as an independent body of
work, even when its eventual authoritative destination is not yet known.

Working is **not merely “Design in progress.”** It may precede a Brief/Design entirely and may later
feed Design, Decisions, a Brief, Reference, proposal, Review response or several destinations.

Use Working when the exploratory material itself has enough volume/coherence to be useful beyond a
short current-context checkpoint.

Because a Working series may include subtopic/key structure that is not derivable from the
owning top-level-topic name, its active version-agnostic series locator is registered in the topic
Index `Live state` section under §8.

### OpenItems

`OpenItems` is the durable live attention register: current, pending, deferred or future items whose
loss would matter and which still require thought, revisit, investigation or progression.

It contains only live/open state. When an item resolves, route any durable result where it belongs
and remove the OpenItem. Do not retain a closed-items archive/tombstone history merely to prove the
item once existed.

A resolution to **no change** normally leaves no durable row. If the negative conclusion and its
reason are material and could credibly be raised again, preserve that conclusion first in Decisions
or another genuinely proper durable owner, then remove the OpenItem. Otherwise remove it with no
separate history.

Default scope is one register per top-level topic. A subtopic may have its own delegated OpenItems
where use/volume/cadence makes that materially clearer.

### WorkRegister

`WorkRegister` is the top-level-topic-wide live queue/ledger of **confirmed work owed by the owning
top-level topic and not yet fully delivered**.

Admission is broader than Design consequences but narrower than a generic backlog:

- include genuinely confirmed/committed/owed work whose delivery remains incomplete;
- exclude ideas, possible future work, unconfirmed findings and unresolved matters still requiring
  judgment — those remain OpenItems/Working/other appropriate live state until confirmed; and
- remove an obligation once its full owed result is delivered and owner reconciliation is complete.

Confirmed Design consequences are a mandatory producer subset of this general type rule. Whenever a
confirmed Design change creates a downstream implementation/output consequence that is not fully
completed in the same pass, that consequence **must** create/update WorkRegister. This producer rule
does not define the complete admission boundary.

A WorkRegister item records, proportionately:

- identifier where useful;
- source/trigger for the confirmed obligation;
- the committed/owed change or result;
- specific required downstream outcome/code/build/document changes;
- target outcome(s)/location(s);
- current delivery/reconciliation state;
- WorkPackage/action mapping;
- compact returned result while still open; and
- remaining obligation/blocker.

Where one obligation is deliberately split across several WorkPackages, its required changes must
be independently identifiable, normally as an enumerated/bulleted set. Each WorkPackage `Covers`
mapping then identifies the exact portions it claims; structured sub-obligation IDs are not
required.

A returned result in WorkRegister is compact reconciliation state, not copied execution evidence.
Retain only the current/terminal WorkPackage status, stable WorkPackage/Outcome reference, concise
returned result where useful, and remaining obligation/blocker. Detailed execution/validation
evidence remains in the WorkPackage Outcome and is referenced rather than copied.

When a mapped Outcome has been received but full owner reconciliation is not completed in the same
uninterrupted step, first record `Returned — reconciliation pending` in the existing package/action
mapping or equivalent compact register state. If reconciliation is immediate, no ceremonial
intermediate persisted state is required.

One WorkPackage may cover several WorkRegister items; one WorkRegister item may require several
WorkPackages.

When all owed work is delivered and reconciled, remove the WorkRegister item. Preserve durable
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
WorkRegister, another owner or nothing durable. A negative/no-change conclusion is preserved only
when the conclusion itself has a proper durable owner and material future value.

A WorkRegister item does not need to have been an OpenItem first. Confirmed owed work may enter the
register directly; a confirmed Design change with an undelivered downstream consequence is one
mandatory direct producer.

## §6 — Versioning and currency

A document version counts **issued/persisted checkpoints**, not keystrokes.

For WIP specifically, visible filename versioning is a currency signal:

```text
Capabilities_WIP_v7.md
```

Within one editing context, draft/edit freely. Whenever an operating process issues a new persisted
WIP checkpoint, increment the version so the current issued checkpoint is visibly distinguishable.
Prior issued WIP versions become Superseded when replaced.

Operational decisions about **when** to checkpoint, how to transfer/sync the file between contexts,
and how to verify replacement belong to Working Practices/environment.

Working follows normal issued-output versioning. OpenItems and WorkRegister increment when a new
register state is issued/persisted.

## §7 — WIP/Working disposition

WIP normally has no independent terminal-history value. Route/remove each completed active thread
from the next checkpoint once its useful material is safe elsewhere. Withdraw/dispose the whole WIP
when no active continuation thread remains; archive only where the WIP itself has unusual independent
historical value.

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

Load them separately when active work state is needed.

The documentation Index must not reintroduce the same churn indirectly. Individual live-state
versions stay outside the stable Document Register unless there is a specific reason otherwise.

**Working has a targeted discoverability rule.** When a new Working series is issued, the owning
topic Index shall contain a version-agnostic locator for that Working series in a `Live state`
section, for example:

```text
Capabilities_Messaging_Working
```

The locator identifies the series, not one `_vN` checkpoint. Issuing a **new** Working series and
its locator is one semantic corpus change; the Index must be current for that issuance. Reissuing a
later version in the same Working series therefore does not require an Index update. When the
Working series ceases to be live, remove/withdraw the locator from the Index. Working Practices/
environment owns the physical replacement/staging mechanics, not whether the locator is required.

This Working rule is **not** a requirement to maintain a complete live-state manifest for WIP,
OpenItems or WorkRegister. Their live versions remain outside the stable Document Register, and no
new mandatory locator is created for them by this rule. Owner-defined/locally justified locators
may still exist without implying manifest completeness.

A specialised Binder may include live state explicitly where its stated purpose requires it, but
omission from the normal Binder is the default.

Index remains a normal Binder source because its stable structural/documentation map is useful
without carrying every live-state revision.

## §9 — Documentation-specific use of Index

Generic Index semantics come from `AIDE_Index@v2`.

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

A `DocumentationTopic` Item is the **logical boundary/scope of one top-level documentation topic**.
The governing Index document (or authoritative Index section) declares/describes that logical Item
and provides the authoritative evidence used to recognise and resolve it; the Markdown Index file
is not itself the semantic boundary merely because the declaration is written there.

For example, a declaration such as:

```text
{scope: "AIDE/Core", type: DocumentationTopic}
```

in `Core_Index_vN.md` means that the Index declares/describes the logical `AIDE/Core` top-level
DocumentationTopic boundary. Recognition may inspect that authoritative declaration to identify
the logical topic scope it describes.

A practical container may host one or several DocumentationTopics. The Item Type therefore does
not mean “chat project”, “master folder” or another storage/context container, even where the
current layout happens to be 1:1.

It provides:

- top-level-topic identity;
- self-describing documentation-boundary behaviour;
- governing Index/Document Register resolution; and
- optional known container/project mapping.

Subtopics remain subordinate structures inside the top-level topic. A subtopic does not become a
separate DocumentationTopic merely because it has its own Design, Decisions or Index section.

A parent repository Index may register/describe/locate a DocumentationTopic and stop at that
self-describing boundary. Where several top-level topics share one physical container, the parent
may register the container structurally and the topics as distinct logical Items beneath it.

Defining `DocumentationTopic` does not grant Domain authority. `AIDE_Domain` alone decides whether
this Item Type may establish or participate in Domain resolution; subordinate structures may remain
within an enclosing effective Domain through structural containment without becoming Domain-capable
roots themselves.

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
and the exact portion of each obligation it is authorised to deliver. Where an obligation is split,
its source required changes are independently identifiable so the package `Covers` mapping can name
the precise claimed portions without introducing structured sub-obligation IDs.

On return:

- Build reports result/evidence for the mapped work in the WorkPackage Outcome;
- if the Outcome is received and reconciliation cannot be completed in the same uninterrupted step,
  the owner first records `Returned — reconciliation pending` against the mapping/equivalent compact
  register state;
- the director/owning process reconciles each WorkRegister item;
- completed obligations are removed;
- partial/blocked obligations retain only compact reconciliation state — current/terminal package
  status, stable WorkPackage/Outcome reference, concise returned result where useful, and remaining
  obligation/blocker; and
- design-shaping feedback returns to Project Design before changed execution is authorised.

Detailed execution/validation evidence remains in the WorkPackage Outcome and is referenced rather
than copied into WorkRegister. If owner reconciliation is immediate on receipt, no ceremonial
persisted `Returned — reconciliation pending` state is required.

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

v18 remains `OnUpdate`; v19/v20/v21/v22/v23/v24 are `None` transitions.

v21 changed the canonical operating model without requiring mass rewriting/renaming. v22 clarifies
`DocumentationTopic` recognition and corrects the WIP-series rule prospectively. v23 corrects current
generic Index consumption/conformance to `AIDE_Index@v2`. v24 clarifies Review B work-state admission,
thread/return/closure semantics, Working discovery and the Working Practices owner seam. None of
these requires historical/superseded WIP renames or a corpus-wide rewrite; current material adopts
the current semantics on its next qualifying substantive update/save under normal
Dependencies/Migration behaviour.

## §16 — Published outcomes

This Design produces:

```text
AIDE_DocumentationMethodology@v24
DocumentationMethodology_Guide_v24
```

The Standard is the canonical AI-facing runtime contract; the Guide is the fuller human companion.

---
Dependencies: AIDE_Index@v2, AIDE_Dependencies@v2, AIDE_Migration@v1
References: DocumentationMethodology_Decisions_v22, WorkingPractices_Design_v5, AIDE_WorkPackage@v2
<!-- END SOURCE: DocumentationMethodology_Design_v21.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Decisions_v22.md -->
# Documentation Methodology — Decisions

> **Version 22** (2026-09-01). Review B R1 remediation: preserves prior history and records the
> accepted work-state admission, thread/discovery, owner-seam, reconciliation and negative-closure
> decisions for Documentation Methodology v24.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

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

## D32 — DocumentationTopic is the logical top-level-topic boundary

**Trigger / problem.** Review A exposed an ambiguity at the Core/Documentation Methodology seam.
The current wording says a `DocumentationTopic` is self-describing and is identified through Index
declarations, but it can be read as though the Markdown Index file itself is the semantic Item
because the type marker appears in that file. The model also needs to remain deliberately
top-level-only so subordinate documentation structures are not accidentally promoted into Domain
roots.

**Decision.** `DocumentationTopic` remains a Documentation Methodology-owned semantic Item Type for
**one logical top-level documentation topic boundary/scope**. Its governing Index document (or
authoritative Index section) is the authoritative declaration/description used to recognise and
resolve that logical Item; it is not itself the semantic boundary merely because it contains the
declaration. Recognition may inspect a declaration such as
`{scope: "AIDE/Core", type: DocumentationTopic}` to identify the logical topic scope described by
that Index.

Subtopics remain subordinate structures within the top-level topic and do not become separate
DocumentationTopic Items merely because they have their own Design, Decisions or Index sections.
A practical container may still host several distinct top-level DocumentationTopics.

**Domain boundary.** Defining or recognising `DocumentationTopic` does not grant Domain authority.
`AIDE_Domain` alone decides whether the Item Type may establish or participate in Domain resolution.
Structural containment may keep subordinate material inside an enclosing effective Domain without
making those subtopics Domain-capable roots.

**Consequences.** The Core/Documentation Methodology seam is explicit: Documentation Methodology
defines what the semantic top-level documentation Item is and how its governing declaration resolves
it; Core Index supplies generic Item/Item Type registration mechanics; Domain remains the exclusive
owner of Domain-capability assignment. No existing subtopic is promoted by this clarification.

## D33 — Use one WIP series per top-level topic

**Trigger / problem.** The v21 option to add a subtopic/thread key to WIP created a false model in
which WIP appeared to belong to the currently active subtopic rather than to the top-level
continuation context. Independent series such as `Capabilities_Messaging_WIP_vN` also proliferate
live-state locators, fragment resume state, and make it unclear which WIP should be loaded to resume
the top-level topic.

**Alternatives considered.** Retain independent WIP series for parallel threads. Rejected because
WIP is deliberately a compact volatile continuation container, so thread identity can be carried
inside the file without creating another semantic document series. Collapse Working/OpenItems/
WorkRegister delegation to the same rule. Rejected because those types have different purposes and
may still justify subtopic-specific/delegated scopes under their own rules.

**Decision.** Use one current WIP series per top-level topic in the normal AIDE workflow, named:

```text
{TopLevelTopic}_WIP_v{N}.md
```

Carry concurrent active subtopic/thread identity inside that WIP, for example through concise
`Active thread — ...` sections. Do not maintain independent subtopic-specific WIP series. Retain
visible `_vN` checkpoint versioning for the single series.

**Consequences.** The resume contract is clearer and live-state discovery is simpler. Working
remains independently subtopic-specific where useful, and existing OpenItems/WorkRegister delegation
rules are unchanged. Historical or Superseded subtopic-named WIP files do not require mass rename;
the corrected convention applies to current/new checkpoints.

## D34 — Issue v22 with migration posture None

**Decision.** Publish `AIDE_DocumentationMethodology@v22` and
`DocumentationMethodology_Guide_v22`. The v22 transition posture is `None`.

**Reason.** v22 clarifies semantic interpretation and corrects the current WIP-series convention; it
does not require content transformation of existing governed artefacts. Historical/superseded WIP
files are not mass-renamed, and corpus files are not rewritten solely because v22 is issued.

**Review scope.** This release implements the authorised Review A seam correction and the already
confirmed queued WIP rule only. It does not adopt or pre-empt unrelated Review B work.

## D35 — WorkRegister admits confirmed work owed, with Design consequences as a guaranteed producer

**Trigger / problem.** Review B found that current wording could be read two ways: as a general queue
for any confirmed work, or as a ledger only for downstream Design consequences. The architecture
needs one admission rule without weakening the hard rule that confirmed Design cannot silently outrun
delivery.

**Alternatives considered.** Limit WorkRegister to Design consequences only. Rejected because other
work can become genuinely committed/owed without originating in a Design change. Broaden it into a
generic backlog. Rejected because ideas, possible future work and unresolved matters still requiring
judgment need a different live state and would make every register row stop meaning “owed”.

**Decision.** WorkRegister holds **confirmed work owed by the owning top-level topic and not yet fully
delivered**. Admit genuinely committed/owed work; exclude ideas, possible future work, unconfirmed
findings and unresolved matters still requiring judgment. Those remain OpenItems/Working/other
appropriate state until confirmed.

Every confirmed Design change with an undelivered downstream consequence remains a mandatory
producer of WorkRegister state. That is a guaranteed producer rule, not the complete type definition.

**Consequences.** Project Design keeps its hard consequence rule while Documentation Methodology owns
the general register semantics. OpenItems and WorkRegister remain distinct.

## D36 — WIP threads exit independently; whole-file withdrawal follows the last active thread

**Trigger / problem.** One WIP series per top-level topic fixed naming/ownership but did not say when
an internal active thread leaves the shared continuation file. Without an exit rule, already-routed
material can accumulate indefinitely beside active context.

**Decision.** When an `Active thread — ...` section's useful material has been safely routed to its
proper owners, remove that thread from the next WIP checkpoint. Temporary duplication remains valid
while routing is incomplete. Withdraw/dispose the whole WIP only when no active continuation thread
remains, except for unusual independent archival value.

**Consequences.** WIP remains non-authoritative, compact and continuation-focused without collapsing
parallel threads into separate WIP series.

## D37 — Working gets a required version-agnostic live locator; operational handling stays with Working Practices

**Trigger / problem.** Working is deliberately outside the normal Binder and may use subtopic/key
naming, so its active series cannot always be derived from the top-level-topic name. At the same time,
current methodology repeated practical checkpoint/sync/output handling that Working Practices already
owns.

**Decision.** When a new Working series is issued, the owning topic Index must carry a
version-agnostic Working-series locator in `Live state`; new-series issuance and the locator are one
semantic corpus change. Later versions in that same series do not force Index updates. Remove/
withdraw the locator when the series ceases to be live.

This is a targeted Working discoverability rule, not a requirement for a complete WIP/OpenItems/
WorkRegister live-state manifest.

Documentation Methodology remains normative owner of WIP/Working/OpenItems/WorkRegister semantics,
routing/lifecycle meanings, authority boundaries and Binder/live-state semantic treatment. Working
Practices/environment owns operational checkpoint/output timing, practical transfer/sync and
physical file/repository handling. DocMeth may explain the relationship but does not duplicate those
operating rules as normative requirements.

**Consequences.** Active Working is discoverable without Binder churn on every Working version.
The owner seam has one normative source per rule.

## D38 — WorkRegister return state is compact reconciliation state, including a pending marker when needed

**Trigger / problem.** Review B identified ambiguity between “Outcome returned” and “owner has
reconciled the obligation”, and current `returned result` wording could invite copying detailed Build
evidence into WorkRegister.

**Decision.** When a mapped Outcome is received and full owner reconciliation is not completed in the
same uninterrupted step, record `Returned — reconciliation pending` in the existing package/action
mapping or equivalent compact register state before later reconciliation. If reconciliation is
immediate, no ceremonial intermediate persisted state is required.

While an item remains open, retain only the current/terminal WorkPackage status, stable WorkPackage/
Outcome reference, concise returned result where useful, and remaining obligation/blocker. Detailed
execution/validation evidence remains owned by the WorkPackage Outcome and is referenced, not copied.

**Consequences.** “Returned” can no longer be mistaken for “reconciled”, and WorkRegister remains a
live obligation ledger rather than a second execution-evidence store.

## D39 — Split WorkRegister obligations must expose independently identifiable required changes

**Trigger / problem.** A WorkRegister item may span several WorkPackages, but a broad prose
obligation can make it impossible to tell exactly what each package's `Covers` mapping claims.

**Decision.** When an obligation is deliberately split across multiple WorkPackages, express its
required changes so the portions are independently identifiable, normally as an enumerated/bulleted
set. Each WorkPackage mapping identifies the exact portions covered using the existing WorkPackage
`Covers` seam. Do not create structured sub-obligation IDs solely for this purpose.

**Consequences.** The source register becomes reconcilable without adding another identifier system.
Current `AIDE_WorkPackage@v2` already requires each mapped item and the portion covered, so no new
Build/WorkPackage mechanism is required for this Review B pass.

## D40 — Negative OpenItem closure preserves only material reusable conclusions

**Trigger / problem.** Live-only OpenItems correctly removes resolved rows, but a “no change” result
can tempt either an unnecessary tombstone or loss of a conclusion that future work is likely to
re-raise.

**Decision.** Do not keep an OpenItem tombstone merely because the row existed. If a negative
conclusion and its reason are material and could credibly be re-raised, preserve the conclusion first
in Decisions or another genuinely proper durable owner, then remove the OpenItem. Otherwise remove it
with no durable history.

**Consequences.** OpenItems remains live-only while durable reasoning is preserved only when it has
real future value.

## D41 — Issue Review B R1 remediation as v24 with migration posture None

**Decision.** Publish `AIDE_DocumentationMethodology@v24` and
`DocumentationMethodology_Guide_v24`. The v24 transition posture is `None`.

**Reason.** Review B R1 clarifies live work-state semantics and ownership boundaries; it does not
require a mass transformation of existing governed documents. Current live registers/Working/WIP
adopt the clarified rules on their next relevant substantive issue/update.

**Version-reference sweep.** The current five-master corpus was checked for concrete stale in-body
capability-version references that read as current executable instructions. No additional such
current instruction was found. Historical references inside earlier Decisions events remain
historical evidence and are intentionally not rewritten. This does not establish a general policy
for versioned in-body capability references; that question remains outside this Review B pass.

---
Dependencies: !AIDE_DocumentationMethodology@v24, AIDE_Index@v2, DocumentationMethodology_Design_v21
References: DocumentationMethodology_Guide_v24, Core_Index_Decisions_v1, WorkingPractices_Decisions_v5, AIDE_WorkPackage@v2
<!-- END SOURCE: DocumentationMethodology_Decisions_v22.md -->

---

<!-- BEGIN SOURCE: AIDE_DocumentationMethodology_Standard_v24.md -->
# AIDE Documentation Methodology — Standard

> **Identity:** `AIDE_DocumentationMethodology@v24`
> **Common name:** Documentation Methodology
> **Version 24**
> > **Published:** 2026-09-01
> > **Change:** Review B R1 remediation — WorkRegister admission/reconciliation, WIP thread exit,
> > Working live locator, OpenItem negative closure, and Working Practices owner seam.
>
> **Default weight:** Expectation

## Purpose

Provide the canonical AI-facing contract for creating, naming, structuring, recording, versioning,
distributing and maintaining AIDE-governed document corpora while preserving active work safely
and keeping confirmed Design aligned with delivered outcomes.

This Standard is the normal runtime/deployable representation of Documentation Methodology.
`DocumentationMethodology_Guide_v24` is its fuller human-oriented companion.

## Ownership boundary

**Weight: Requirement**

Documentation Methodology owns governed document naming, document types and document-specific
lifecycle, lifecycle state/disposition semantics, top-level-topic/document organisation,
documentation-specific Index extensions, document metadata-container placement,
governed-history preservation, document distribution rules, asset/unmanaged recording, the
authoritative-master/generated-consumption boundary, document output/version discipline, and the
semantic meanings/routing/authority boundaries of WIP, Working, OpenItems and WorkRegister.

It also owns the semantic treatment of live state relative to normal Binders/Indexes, including the
Working-series discoverability rule defined below.

Operational checkpoint/output timing, practical cross-context transfer/sync, physical repository/
storage layout, management-folder names, file movement, sweep/external-archive cadence, Change
Delivery staging and Binder placement/replacement workflow are operating concerns owned by Working
Practices or the applicable environment. Physical handling does not define a document's semantic
state.

Do not absorb semantics owned elsewhere:

- Core owns formal Identity and generic `AIDE_Index@v2` Item/Item Type/Index behaviour.
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
Operational examples here are explanatory only where the operating rule belongs to Working
Practices/environment.

## Core corpus principles

**Weight: Expectation**

1. Keep one authoritative answer per question; reference rather than restate.
2. Route information by state and role: WIP preserves current volatile context; Working preserves
   substantial exploration; OpenItems tracks live unresolved attention; Brief defines; Design
   determines; Decisions records reasoning; WorkRegister tracks confirmed work owed and not fully
   delivered; WorkPackage bounds execution; Outcome returns evidence; Index records structure/current
   corpus.
3. Treat filenames as legible locators and the applicable authoritative Index as the resolver.
4. Distribute only document types whose distribution contract permits it.
5. Keep human-readable documents as short as their function permits and conclusion-first.
6. Admit only genuinely confirmed/owed work to WorkRegister. Every confirmed Design change with an
   undelivered downstream consequence is a mandatory WorkRegister producer.
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
- WIP: one current series per top-level topic using `{TopLevelTopic}_WIP_vN`. Parallel active
  threads are identified inside the WIP, not through independently named subtopic WIP series.
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
  confirmed work owed by the owning top-level topic and not yet fully delivered
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
- **WorkRegister** — confirmed work owed by the owning top-level topic and not yet fully delivered;
  a live obligation/reconciliation ledger rather than a generic backlog.
- **WorkPackage** — document representation of a bounded unit of Build work; execution semantics are
  `AIDE_WorkPackage`.
- **WorkPackage_Outcome** — separate live return document where used; folds into WorkPackage on
  archival.
- **Message** — Messaging-owned transmission/message semantic type; this methodology supplies only
  generic governed-file integration when persisted.
- **Index** — generic structural registration under `AIDE_Index@v2` plus documentation-specific
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

Use WIP when volatile active thinking/current work state needs a persisted document representation
and is not yet safely represented elsewhere.

WIP may contain current position, reasoning not yet routed, draft fragments, candidate OpenItems or
WorkRegister obligations, source pointers and a clear resume point. Temporary duplication is allowed
because WIP is a continuity checkpoint, not an authoritative source.

WIP anchors to the top-level topic as the single current continuation series for that topic:

```text
{TopLevelTopic}_WIP_v{N}.md
```

Do not create independently named subtopic/thread WIP series. Where several active threads coexist,
carry their identity inside the WIP using concise `Active thread — ...` sections or equivalent
internal structure. This rule is specific to WIP and does not remove legitimate subtopic-specific
Working documents or delegated OpenItems/WorkRegister scopes under their own rules.

When an active thread's useful material has been safely routed to its proper owners, remove that
thread from the next WIP checkpoint. Routed material must not accumulate indefinitely beside active
continuation state. Withdraw/dispose the whole WIP series only when no active continuation thread
remains; archive only where the WIP itself has unusual independent historical value.

When an operating process issues a new persisted WIP checkpoint, increment `_vN` so filename currency
is visible; a replaced issued checkpoint becomes Superseded. Operational checkpoint timing,
transfer/sync and replacement verification belong to Working Practices/environment.

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

Normal stable Binders exclude Working by default. Because an active Working series may not be
locatable from the top-level-topic name alone, the topic Index `Live state` section shall register
the version-agnostic Working-series locator when a new series is issued. Later `_vN` issues in the
same series do not require an Index update; remove/withdraw the locator when the series ceases to be
live.

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

Use `AIDE_Index@v2` for generic Index/Item/Item Type semantics.

Documentation Methodology contributes documentation-specific Index sections/properties where
applicable:

- top-level-topic/subtopic declarations and documentation relationships;
- Document Register and current document version/type/lifecycle facts;
- local/custom document type definitions;
- document assets/unmanaged-file records;
- withdrawn/renamed/rehomed/dead-locator mappings; and
- documentation-local configuration.

### DocumentationTopic Item Type

`DocumentationTopic` is a Documentation Methodology-owned semantic Item Type representing the
**logical boundary/scope of one top-level documentation topic**.

The governing Index document (or authoritative Index section) declares/describes that logical Item
and supplies the authoritative evidence used to recognise and resolve it. A declaration such as:

```text
{scope: "AIDE/Core", type: DocumentationTopic}
```

inside `Core_Index_vN.md` means that the Index declares/describes the logical `AIDE/Core`
DocumentationTopic boundary; it does not mean the Markdown file itself is the semantic boundary.
Recognition may inspect the authoritative governing Index declaration to identify the logical scope
it describes.

The Item provides top-level-topic identity, self-describing documentation-boundary behaviour,
governing Index/Document Register resolution, and optional known container/project mapping. A
parent/repository Index may register and locate a DocumentationTopic and stop at that self-describing
boundary. A physical container may hold one or several DocumentationTopics.

Subtopics are subordinate structures inside the top-level topic and are not separate
DocumentationTopic Items merely because they have their own Design, Decisions or Index sections.

Defining the Item Type does not grant Domain authority. `AIDE_Domain` alone decides whether the
type may establish or participate in Domain resolution; a subtopic cannot elevate itself into a
Domain-capable root through this documentation type.

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
- A no-change/negative resolution normally leaves no durable row. If the conclusion and reason are
  material and could credibly be re-raised, preserve that conclusion first in Decisions or another
  genuinely proper durable owner; otherwise remove it with no separate history.
- Do not maintain a closed-items/tombstone archive inside OpenItems.

### WorkRegister

WorkRegister is the top-level-topic-wide live queue/ledger of **confirmed work owed by the owning
top-level topic and not yet fully delivered**. It is not a generic backlog.

Admission rule:

- include genuinely confirmed/committed/owed work whose delivery remains incomplete;
- exclude ideas, possible future work, unconfirmed findings and unresolved matters still requiring
  judgment; and
- use OpenItems/Working/another proper live state until such material becomes confirmed work owed.

The hard Design consequence rule remains a mandatory subset: whenever confirmed Design changes,
determine whether downstream code/build/document/production outcomes must change. Every such
consequence shall either be fully delivered in the same pass or create/update WorkRegister. This is
a guaranteed producer rule, not the complete WorkRegister admission definition.

Record enough detail to determine later whether the confirmed obligation has actually been
delivered, including as applicable:

```text
ID
source/trigger
confirmed obligation / committed change
specific required downstream changes
target outcomes/locations
current delivery/reconciliation state
WorkPackage/action mapping
compact returned result while still open
remaining obligation/blocker
```

Where one obligation is deliberately split across multiple WorkPackages, make its required changes
independently identifiable, normally as an enumerated/bulleted set. Each WorkPackage `Covers`
mapping identifies the exact portions claimed. Do not introduce structured sub-obligation IDs solely
for this mapping.

When a mapped Outcome is received and full owner reconciliation is not completed in the same
uninterrupted step, first record `Returned — reconciliation pending` in the existing package/action
mapping or equivalent compact register state. Immediate reconciliation needs no ceremonial
intermediate persisted state.

`returned result` means compact reconciliation state only. While the item remains open, retain the
current/terminal WorkPackage status, stable WorkPackage/Outcome reference, concise returned result
where useful, and remaining obligation/blocker. Detailed execution/validation evidence remains
owned by the WorkPackage Outcome and is referenced, not copied.

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

Load these separately when active state is needed. A specialised live-state Binder is valid only
when deliberately designed for that purpose.

Do not reintroduce live-version churn through the stable Document Register.

**Working discoverability:** when a new Working series is issued, the topic Index shall contain a
version-agnostic locator for that series in `Live state`. New-series issuance and the locator form
one semantic corpus change. The current `_vN` is established from the actually available/current
Working file, so later version increments in the same series do not require Index/Binder change.
Remove/withdraw the locator when the Working series ceases to be live.

This targeted rule does not create a mandatory live-state manifest for WIP, OpenItems or WorkRegister.
No completeness claim is implied if the Index also carries locally useful owner-defined locators for
other live series.

Documentation Methodology defines when the semantic Index state is required. Working Practices/
environment owns physical output batching/replacement, transfer and repository handling without
weakening that semantic requirement.

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
- When a WIP continuity checkpoint is issued, version it so filename currency is visible; timing and
  transfer/sync behaviour belong to Working Practices/environment.
- Produce a substantive Design change and its Decisions record in the same pass; editorial or
  mechanical Design maintenance does not create a Decisions event by itself.
- Admit confirmed owed work to WorkRegister according to its general type rule. For every confirmed
  Design change, identify downstream consequences and apply them in the same pass or record the
  undelivered consequences in WorkRegister.

Operational batching/checkpoint triggers are defined by Working Practices/environment rather than by
this Standard.

## WorkPackage document integration

**Weight: Requirement**

Generic WorkPackage authoring/execution/validation/return semantics come from
`AIDE_WorkPackage@v2` and `AIDE_Build@v4`.

This Standard owns document integration:

- the WorkPackage is a governed point-in-time document with opening-date key;
- a separate live WorkPackage Outcome uses the same key where produced;
- when a WorkPackage is sourced from WorkRegister, it identifies the covered item IDs and the exact
  authorised portion of each obligation; where one obligation is split, its source required changes
  are independently identifiable so `Covers` can name the precise portions without sub-obligation
  IDs;
- the Outcome reports result/evidence/remaining work for those mappings;
- the director/owning process reconciles the returned evidence against the WorkRegister and current
  Design—Build does not silently close the register;
- if receipt and full reconciliation are not completed in the same uninterrupted step, the register
  first records `Returned — reconciliation pending`; immediate reconciliation needs no ceremonial
  intermediate persisted state;
- while an item remains open, WorkRegister retains compact status/reference/result/remaining state
  and references detailed Outcome evidence rather than copying it;
- after reconciliation, a returned Outcome may be appended verbatim to the WorkPackage before
  archival where that lifecycle is used; and
- design-shaping issues returned by Build are resolved by Project Design rather than silently
  settled by document mechanics.

## Documentation Methodology conformance

**Weight: Requirement**

Current conformance is recorded through Dependencies:

```text
Dependencies: !AIDE_DocumentationMethodology@v24
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
  CurrentVersion: v24
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

Transition:
  Version: v22
  Posture: None

Transition:
  Version: v23
  Posture: None

Transition:
  Version: v24
  Posture: None
```

Merely reading/using a v17 document does not trigger the v18 OnUpdate transition. v19, v20, v21,
v22, v23 and v24 require no additional artefact transformation; when Migration traverses through current during
a qualifying save, their None transitions may advance the saved checkpoint after the v18 success
condition is satisfied. v22 does not require historical/superseded WIP renames or corpus-wide
rewrites; the corrected root-WIP convention applies prospectively to current/new checkpoints. v23 requires no consumer content transformation; it corrects current conformance to `AIDE_Index@v2`.
v24 requires no consumer content transformation; its clarified live-state semantics apply on the next
relevant substantive issue/update.

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
References: DocumentationMethodology_Design_v21, DocumentationMethodology_Guide_v24
<!-- END SOURCE: AIDE_DocumentationMethodology_Standard_v24.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Guide_v24.md -->
# Documentation & Workflow Methodology — Guide

> **Identity:** `AIDE_DocumentationMethodology@v24`
> **Version 24** (2026-09-01). Review B R1 remediation: clarifies WorkRegister admission/return,
> WIP thread exit, Working discovery, OpenItem negative closure and the Working Practices owner seam.
>
> **Migration posture:** None for v24. The Review B R1 semantic clarifications require no mass
> consumer-content transformation.

## v24 change summary

- **WorkRegister admission is general but bounded.** It holds confirmed work owed by the owning
  top-level topic and not yet fully delivered; ideas/unconfirmed/unresolved matters remain elsewhere.
  Confirmed Design consequences remain a mandatory producer subset.
- **WIP threads now have an exit rule.** Remove a routed `Active thread — ...` section from the next
  checkpoint; withdraw the whole WIP only after no active continuation thread remains.
- **Working is discoverable without Binder inclusion.** A new Working series gets a version-agnostic
  locator in the topic Index `Live state`; later versions do not churn the Index.
- **Returned is not reconciled.** Use `Returned — reconciliation pending` when an Outcome has arrived
  but owner reconciliation cannot be completed immediately; keep only compact reconciliation state
  in WorkRegister.
- **Split obligations stay simple.** Required changes are independently identifiable and WorkPackage
  `Covers` names the exact portions; no structured sub-obligation IDs are introduced.
- **Negative OpenItems do not create tombstones.** Preserve a material reusable negative conclusion
  in Decisions/another proper durable owner only when it could credibly be re-raised.
- **Ownership seam is explicit.** Documentation Methodology owns work-state semantics, routing,
  authority and Binder/live-state meaning; Working Practices owns operational checkpoint timing,
  transfer/sync and physical file/repository workflow.
- **Review C is not pre-empted.** Historical/stable version references were not rewritten and no new
  general in-body capability-version policy is created.

## 1. The core rule: route information by state

The methodology is easiest to use if each document answers a different question:

| State | Document | Main question |
|---|---|---|
| Current volatile context | `WIP` | What do I need to continue this active work safely? |
| Substantial exploration | `Working` | What thinking/material is being developed before its final home is known? |
| Live attention | `OpenItems` | What still needs attention/revisit/thought? |
| Confirmed model | `Design` | What is the current confirmed position? |
| Reasoning/history | `Decisions` | Why did the confirmed position become this? |
| Confirmed owed work | `WorkRegister` | What confirmed obligation is still not fully delivered? |
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

Use WIP to preserve **the current working context** when volatile context needs a persisted
continuation representation.

Typical content:

```text
Current position
Current thread/problem
Important reasoning not yet represented elsewhere
Draft fragments/candidate wording
Candidate OpenItems
Candidate WorkRegister obligations
Relevant source pointers
Resume from here
```

WIP can be rough. It is allowed to duplicate content temporarily because its job is safe
continuation, not authoritative publication.

### When to checkpoint

Documentation Methodology defines what WIP **is** and how an issued checkpoint is versioned; it does
not own operational checkpoint timing. `AIDE_WorkingPractices` defines practical triggers for when to
persist WIP, when to batch normal file output, and how to transfer/sync/verify context replacement.

The semantic rule here is simply: when the operating process decides that a WIP checkpoint is being
issued, treat it as an issued document checkpoint under the versioning rule below.

### Versioning

Visible filename versioning is intentional:

```text
Capabilities_WIP_v5.md
```

It distinguishes successive issued continuation checkpoints. Edit freely inside the current
context; when a new checkpoint is issued, increment `_vN`; the previous checkpoint becomes
Superseded. Transfer/sync mechanics and verification belong to Working Practices/environment.

There is one current WIP series for the top-level topic. If several threads are active at once, keep
them inside that file, for example:

```markdown
## Active thread — Messaging
...

## Active thread — Architecture Review B
...
```

Do not create `Capabilities_Messaging_WIP_vN` or similar independent subtopic WIP series. This
restriction is specific to WIP; a substantial subtopic may still have its own Working document, and
OpenItems/WorkRegister may still use their separately defined delegation rules.

### Thread exit and end of WIP

Route each thread's material according to state:

```text
still unresolved and durable → OpenItems
large coherent exploration   → Working
confirmed model              → Design
material reasoning           → Decisions
confirmed work owed          → WorkRegister
transient/no longer useful   → discard
```

When an `Active thread — ...` section's useful material is safely routed, remove that thread from
the **next** WIP checkpoint. Do not let routed material accumulate indefinitely beside active
continuation state.

Withdraw/dispose the whole WIP only when no active continuation thread remains. Archive only
exceptionally where the WIP itself has unusual independent historical value.

## 5. Working — substantial exploratory/formative work

Working is **not simply Design in progress**.

It is a substantial body of thinking/material that has become worth preserving independently while
its eventual authoritative form may still be unknown.

Examples:

- an idea worked over several sessions before a Brief exists;
- a concept/review response that may later split across Design and Decisions;
- research plus emerging model not ready to commit; or
- a substantial proposal whose eventual document class is not yet clear.

Working can persist across many work units. It may be repeatedly reworked, split and reframed.

When a **new Working series** is issued, add its version-agnostic series locator to the owning topic
Index `Live state` section, for example `Capabilities_Messaging_Working`. New-series issuance and the
locator are one semantic corpus change. This is required because a Working series can include
subtopic/key structure that cannot be derived reliably from the root topic name. Reissuing `_v2` as
`_v3` within that same series does not require another Index update. Remove/withdraw the locator when
the Working series ceases to be live.

This targeted locator rule does not make the normal Binder include Working and does not create a
complete live-state manifest for WIP/OpenItems/WorkRegister.

When Working resolves:

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
2. create a WorkRegister obligation if confirmed delivery remains; and
3. remove the OpenItem.

A conclusion of **no change** does not justify keeping a tombstone. If the negative conclusion and
reason are material and could credibly be raised again, preserve the conclusion first in Decisions
(or another genuinely proper durable owner) and then remove the OpenItem. If not, remove it with no
durable history.

Do **not** retain closed rows, strikethrough archives or a permanent closed-items section merely for
history. Repository/file history may support forensic questions, but the live register answers what
still needs attention now.

If identifiers are used, non-reuse is a reasonable local convention for stale-reference safety but
is not a v24 requirement.

## 7. WorkRegister — confirmed work owed and delivery reconciliation

WorkRegister answers:

> **What work has this top-level topic genuinely committed/owes that is not yet fully delivered?**

This is broader than Design consequences but narrower than a generic backlog.

### Admission rule

Put an item in WorkRegister only when the work is genuinely **confirmed/committed/owed** and some of
that owed result remains undelivered.

Do **not** put these in WorkRegister merely because they may matter later:

- ideas or possible future work;
- unconfirmed Review findings;
- unresolved questions/concerns still requiring judgment; or
- speculative improvements.

Those belong in OpenItems/Working/another appropriate live state until the owning topic actually
commits the work.

### Hard Design consequence producer rule

Whenever confirmed Design changes, ask:

```text
Does this change require any downstream code/build/document/production outcome to change?
```

If no: nothing is owed from that Design change.

If yes:

```text
fully delivered in the same pass? → done
not fully delivered?              → WorkRegister
```

There is no safe third state where Design says one thing and production silently remains on an
older outcome with no record of the gap. This is a **mandatory producer rule**, not the whole
WorkRegister definition.

### Entry depth

The entry must be detailed enough to reconcile delivery later. A useful shape is:

```markdown
## WR23 — Implement revised equality semantics

Status: In progress

Source:
Json_Design — equality section / decision reference

Confirmed obligation:
Deliver the revised equality semantics across implementation, tests and related documentation.

Required outcome changes:
- Update equality comparer.
- Update hash-code behaviour.
- Add/modify tests.
- Review diff semantics for consistency.

WorkPackages:
- WP-31 — Covers: equality comparer; tests — Complete
- WP-34 — Covers: diff semantics review — Returned — reconciliation pending

Returned result:
WP-34 / Outcome-34 — Complete; diff review found no additional implementation change.

Remaining:
Owner reconciliation of the diff conclusion is still required.
```

Do not make WorkRegister duplicate the full implementation plan or Outcome evidence. It records the
**obligation and reconciliation state**.

If one obligation will be split across several WorkPackages, write the required changes so the
portions are independently identifiable—normally bullets like the example. Each WorkPackage
`Covers` mapping names the exact claimed portions. No extra sub-obligation identifier scheme is
needed.

### Return and reconciliation

A returned Outcome and a reconciled obligation are distinct states.

If a mapped Outcome arrives and the owner cannot complete full reconciliation in the same
uninterrupted step, update the mapping/equivalent compact state first to:

```text
Returned — reconciliation pending
```

If reconciliation is immediate, do not persist that intermediate state ceremonially.

While the WorkRegister item remains open, keep only:

- current/terminal WorkPackage status;
- stable WorkPackage/Outcome reference;
- concise returned result where it helps reconciliation; and
- remaining obligation/blocker.

Detailed execution, validation and evidence stay in the WorkPackage Outcome. Reference them; do not
copy them into WorkRegister.

On reconciliation:

- fully delivered → remove item;
- partial → keep compact returned state plus remaining obligation;
- blocked → keep blocker/remaining obligation; or
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

Generic Index is `AIDE_Index@v2` in Core.

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

`DocumentationTopic` is a semantic Item Type owned by Documentation Methodology. The Item is the
**logical boundary/scope of one top-level documentation topic**, not the chat project/master folder
that may happen to contain it and not the Markdown Index file itself.

The governing Index declares/describes the logical Item. For example:

```text
{scope: "AIDE/Capabilities", type: DocumentationTopic}
```

inside `Capabilities_Index_vN.md` means “this Index declares/describes the logical
`AIDE/Capabilities` top-level DocumentationTopic boundary.” Recognition can inspect that
authoritative declaration to identify the scope, and the topic then resolves its governing
Index/document register through it.

A repository/root Index can register a DocumentationTopic, give enough description/location to
select it, and stop. Where one physical container hosts several top-level topics, the Index may show
the container structurally with several distinct DocumentationTopic Items beneath it.

A subtopic is not promoted into a DocumentationTopic merely because it has separate Design,
Decisions or an Index section. Domain remains the only owner that decides whether
`DocumentationTopic` may establish/participate in Domain resolution; the type does not self-assign
Domain authority.

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

Load relevant live state separately when doing active work.

### Working locator without live-state manifest churn

Working needs one special discovery rule because its series name may contain subtopic/key structure
that cannot be derived from the top-level topic name.

When a new Working series is issued, add a version-agnostic locator to the topic Index:

```markdown
### Live state

- `Capabilities_Messaging_Working` — active Messaging exploratory Working series.
```

The current issued version is resolved from the actually available file, not stored as `_vN` in the
Index. Therefore `Capabilities_Messaging_Working_v2 → v3` does **not** require an Index/Binder issue.
When that Working series ceases to be live, remove/withdraw the locator.

This is deliberately **not** a requirement to enumerate WIP, OpenItems and WorkRegister as a
complete live-state manifest. Their individual live versions remain outside the stable Document
Register. A topic may still use locally useful owner-defined locators without implying completeness.

Documentation Methodology defines these semantic inclusion/discoverability rules, including that a
new Working-series issue carries its Index locator. Working Practices owns physical batching/
replacement, repository handling and context transfer/sync.

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

## 13. Migration to v24

v24 has posture `None`.

Do not mass-rewrite current documents simply because the work-state semantics were clarified.
Existing current WIP/Working/OpenItems/WorkRegister artefacts adopt the v24 rules on their next
relevant substantive issue/update under normal Dependencies/Migration behaviour.

Do not mass-rename historical or Superseded subtopic-named WIP files. New/current continuity
checkpoints continue to use the single `{TopLevelTopic}_WIP_vN` series.

This pass also checked the current Documentation Methodology masters for concrete stale in-body
capability-version references that would otherwise read as current executable instructions. No
additional current executable stale reference required correction. Historical version references in
Decisions remain history. No general in-body capability-version policy is established here; that is
outside Review B R1.

## 14. Practical summary

Use this small mental model:

```text
Don't lose current thinking       → WIP
Substantial thinking needs a home → Working
Don't forget unresolved attention → OpenItems
Confirmed answer                  → Design
Why                               → Decisions
Confirmed work still owed         → WorkRegister
Execute a manageable chunk        → WorkPackage
What actually happened            → Outcome
What exists / where to go         → Index
```

That separation is the point. It lets the system preserve knowledge without making every document a
history, queue, scratchpad and source of truth at the same time.

---
Dependencies: AIDE_Index@v2, AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_WorkPackage@v2
References: DocumentationMethodology_Design_v21, AIDE_DocumentationMethodology@v24, WorkingPractices_Design_v5, AIDE_WorkingPractices
<!-- END SOURCE: DocumentationMethodology_Guide_v24.md -->

---
