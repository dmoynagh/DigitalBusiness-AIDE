# Documentation Methodology — Design

> **Version 20** (2026-09-01). Review A R2 preflight correction: updates current generic Index
> consumption/conformance to `AIDE_Index@v2` without changing the v19 design semantics.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

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

There is one current WIP series per top-level topic in the normal AIDE workflow. Its canonical
filename is:

```text
{TopLevelTopic}_WIP_v{N}.md
```

Do not create independent subtopic/thread WIP series. When several active subtopics or threads
coexist, preserve their identity inside the top-level WIP using concise internal sections such as
`Active thread — Messaging` or `Active thread — Architecture Review A`. WIP is the continuation
container for the top-level topic, not another semantic subtopic document series.

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
Capabilities_WIP_v7.md
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

A series entry is intentionally version-agnostic, for example `Capabilities_WIP`; the current
issued checkpoint is established from the available/current file and its visible `_vN` filename
when the live state is actually loaded. Do not claim a current WIP version from a stale Index row.
For WIP, the locator names the single top-level-topic series; active subtopic/thread identity remains
inside the WIP.

Reconcile creation/withdrawal of live-state series at the next normal corpus/output checkpoint.
This keeps Index/Binder stable while preserving discoverability.

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

v18 remains `OnUpdate`; v19/v20/v21/v22/v23 are `None` transitions.

v21 changed the canonical operating model without requiring mass rewriting/renaming. v22 clarifies
`DocumentationTopic` recognition and corrects the WIP-series rule prospectively. v23 corrects current
generic Index consumption/conformance to `AIDE_Index@v2`. None of these requires historical/
superseded WIP renames or a corpus-wide rewrite; current material adopts the current semantics on its
next qualifying substantive update/save under normal Dependencies/Migration behaviour.

## §16 — Published outcomes

This Design produces:

```text
AIDE_DocumentationMethodology@v23
DocumentationMethodology_Guide_v23
```

The Standard is the canonical AI-facing runtime contract; the Guide is the fuller human companion.

---
Dependencies: AIDE_Index@v2, AIDE_Dependencies@v2, AIDE_Migration@v1
References: DocumentationMethodology_Decisions_v21, WorkingPractices_Design_v5, AIDE_WorkPackage@v2
