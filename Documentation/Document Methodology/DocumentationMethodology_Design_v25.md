# Documentation Methodology — Design

> **Version 25** (2026-09-02). Defines value-based Contents and Summary sections and their relationship to Overview.
>
> Created: 2026-08-31 | Last modified: 2026-09-02

## Contents

- **Purpose, ownership and topic model** — the common documentation contract, boundaries and top-level-topic anchor. §1–§2
- **Naming, work state and lifecycle** — filenames, document/work-state flow, routing, versioning and disposition. §3–§7, §13
- **Indexes, document types and authority** — documentation Index extensions, established types and Design/Decisions responsibilities. §8–§11
- **Execution and metadata integration** — WorkPackage/WorkRegister reconciliation and metadata-host boundaries. §12, §14
- **Conformance and published outcomes** — release/migration posture and canonical outputs. §15–§16
- **Semantic sections and durable knowledge** — permitted hosts, Knowledge and authoritative-section rules. §17–§18
- **Binder and file navigation** — Documentation Topic Binder boundaries and direct source discovery. §19
- **Document orientation** — dual-audience Contents/Summary semantics, DocType control and Overview escalation. §20

## Summary

Documentation Methodology is the common contract for AIDE-governed documents and documentation
corpora. It separates volatile continuation state, exploratory material, unresolved attention,
confirmed design, decision history, owed work, bounded execution and returned outcomes so that each
kind of information has one clear role and authority.

The methodology treats the top-level Documentation Topic and its Index as the main structural and
machine-navigation boundary. Individual authoritative masters remain the source of truth; generated
Binders are context-consumption artefacts. Semantic sections may be hosted in different suitable
documents where their owning Standard permits it, but each semantic scope retains one authoritative
instance.

For substantial human-readable documents, a compact top-of-document Contents block can provide a
semantic map of what information is present and where it can be found. A separate Summary can give
a faithful high-level understanding of what the document establishes. Both are conditional,
dual-audience features: a DocType owner defines whether they apply and their expected depth, and
they are omitted when they would add clutter or compromise the document's function, readability or
usability. Detailed body sections remain authoritative where precision or qualification is needed.

Overview remains a separate high-level document type. It may be created by explicit user/work-owner
instruction or when a useful high-level representation would otherwise overload a document Summary.

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

A normal Documentation Topic Binder is a stable/current knowledge consumption artefact, not a live work queue.

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

Documentation Methodology continues to own document-specific lifecycle integration for Brief, Requirements, Design, Decisions, Knowledge, WIP, Working, Review, Guide, Reference, Glossary, Overview, WorkPackage/Outcome integration, Index, OpenItems and WorkRegister.

Messaging owns Message envelope/schema/transport semantics and any Messaging-specific Message type
contract. Where a Message is persisted as a governed file, Documentation Methodology supplies only
normal naming/lifecycle/metadata hosting unless Messaging explicitly defines a document integration
rule.

Custom types remain valid and owner-defined under the normal custom-type contract.

## §11 — Design and Decisions

Design/Definition/Standards/Tools hold the applicable current confirmed semantic state. Decisions retains topic/subtopic-specific thinking, investigation, working, alternatives, reasoning, knowledge and explicit decision history associated with that semantic area's evolution; it is not a downstream executable input.

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

v18 remains `OnUpdate`; v19/v20/v21/v22/v23/v24/v25 are `None` transitions.

v21 changed the canonical operating model without requiring mass rewriting/renaming. v22 clarifies
`DocumentationTopic` recognition and corrects the WIP-series rule prospectively. v23 corrects current
generic Index consumption/conformance to `AIDE_Index@v2`. v24 clarifies Review B work-state admission,
thread/return/closure semantics, Working discovery and the Working Practices owner seam. v25 is a
pre-Round-2 reference correction only: `AIDE_WorkPackage@v3` now explicitly carries the accepted
split-obligation `Covers` clarification without changing the WorkRegister/WorkPackage ownership
boundary or adding a new mechanism. v26 is the non-substantive Review B R2 closing correction: it
corrects the two additional current executable capability-version references identified in Round 2
and refines the earlier D41 verification record without establishing a general in-body version or
dependency/conformance policy. None of these requires historical/superseded WIP renames or a
corpus-wide rewrite; current material adopts the current semantics on its next qualifying
substantive update/save under normal Dependencies/Migration behaviour.

## §16 — Published outcomes

This Design produces:

```text
AIDE_DocumentationMethodology@v28
DocumentationMethodology_Guide_v28
```

The Standard is the canonical AI-facing runtime contract; the Guide is the fuller human companion.


## §17 — Semantic sections and document hosts

Documents are governed containers/hosts; a semantic section is increasingly the unit whose meaning,
authority and permitted hosts are defined by its owning Standard.

- Maintain one authoritative instance for a semantic scope. Several permitted hosts do not permit
  competing editable copies.
- Prefer a compact section in a suitable multi-use document. Externalise when size, lifecycle,
  retrieval, reuse or complexity warrants a dedicated document.
- A more-specific domain Standard may add context-specific permitted/default hosts while preserving
  the section's owner-defined meaning.
- Some section types may remain fixed-host where their contract requires it.
- Moving an authoritative section between permitted hosts is normally structural, not a semantic
  change; update Index/navigation facts and eliminate the former editable authority.

## §18 — Knowledge

`Knowledge` is an established durable lateral intellectual-asset type. By default a top-level Topic
has zero or one current Knowledge document, created only when useful. It preserves broad research,
empirical findings, investigations and reusable understanding that do not naturally belong to one
specific subtopic/decision thread.

Knowledge is non-executable until promoted/reconciled into Design, Definition, a Standard/Tool,
Decisions, Principles or another authoritative semantic owner. Prefer stable `K` entry IDs, an
index-first layout and lightweight Related references. Optimise initial capture for retention, then
curate periodically; explicitly supersede/retract material where the historical correction matters.

Decisions remains broad and retains topic/subtopic-specific investigation, working, alternatives,
reasoning and knowledge associated with the evolution of that semantic area. Knowledge does not
narrow Decisions.

## §19 — Documentation Topic Binder boundaries and navigation

Binders apply to Documentation Topics, not code repositories, solutions, arbitrary projects or
non-document work structures. One Binder per top-level Documentation Topic is the default.

A Topic may partition its Binder when volume, context limits or work management justify it. The
mere existence of a subtopic does not. Partitioned boundaries deliberately cover the parent corpus
and use a lightweight Binder-set/index rather than a duplicate giant aggregate. The Topic declares
its Binder boundary/state.

Curated Blind Review material is Review material/a Review package, not a Binder.

The Topic Index is the machine/navigation entry point. It identifies topic/subtopic structure,
current documents, semantic ownership, live-state locations, Binder boundaries and likely task
sources. Overview remains a human-oriented high-level/TLDR current snapshot. File-based contexts may
navigate authoritative sources directly instead of loading concatenated Binder content.

## §20 — Contents, Summary and Overview

`Contents` and `Summary` are reusable top-of-document semantic sections for human-readable
documents, but neither is universal. Their shared objective is to reduce the cost of understanding
and navigating a document for both human and machine readers without increasing the cost of using
the document itself.

`Contents` answers **what significant information is in this document and where is it?** It is a
compact curated semantic map, not an exhaustive repetition of headings. Entries describe useful
information and use stable headings or numbered-section locators rather than line numbers.

`Summary` answers **what does this document establish at a high level?** It provides a faithful,
substantially cheaper-to-consume representation of the document's objective, model/approach, key
logic, boundaries and outcome as appropriate. It is not an independent authority: the detailed
body governs where precision, qualification, evidence or implementation detail is required, and a
material inconsistency is a document defect.

The normal order when both are present is title/identity/header, Contents, Summary, detailed body,
then footer metadata. Each DocType owner defines applicability, role, scope, expected depth and any
specialised/equivalent structure. Do not add either section merely for consistency. Omit or adapt it
when it would not add navigational/comprehension value or would compromise function, purpose,
readability or usability. Index, Decisions, WIP, WorkRegister, OpenItems and structured data do not
use Summary by default unless their DocType later establishes a specific need.

Overview remains an independent optional DocType rather than a universal Summary host. It may be
created by explicit user/work-owner instruction or when a substantial high-level representation
warrants its own document. The applicable domain/DocType Standard owns any rule that reduces a
related document's Summary depth when a current Overview exists.

---
Dependencies: AIDE_Index@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: DocumentationMethodology_Decisions_v26, WorkingPractices_Design_v5, AIDE_WorkPackage@v3
