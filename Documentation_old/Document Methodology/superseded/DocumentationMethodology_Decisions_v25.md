# Documentation Methodology — Decisions

> **Version 25** (2026-09-02). Records the section-host, Knowledge, Binder-boundary and Index-navigation decisions.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

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
The coordinated Build/WorkPackage remediation issued `AIDE_WorkPackage@v3`, which now explicitly
carries the deterministic-enough split-obligation `Covers` rule: each mapped WorkRegister item
identifies the exact portion covered. This makes the accepted clarification explicit without
introducing a new mechanism or structured sub-obligation identifier system, and the existing
WorkRegister/WorkPackage ownership boundary remains unchanged.

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


## D42 — Review B R2 refines D41 and issues the non-substantive v26 closing correction

**Trigger / problem.** D41 accurately recorded the Review B R1 remediation event, but its
`Version-reference sweep` wording overstated the verification performed. The R1 preflight
correction successfully fixed the current in-body references directly identified or affected by the
coordinated R1 remediation; it did not in fact establish that every current executable
capability-version reference across the five-master corpus had been checked. Review B Round 2
subsequently identified two additional active instructions in the canonical Standard: WorkPackage
integration named `AIDE_Build@v4` although current Build is `AIDE_Build@v5`, and Review document
integration named `AIDE_Review@v1` although current Review is `AIDE_Review@v2`.

**Decision.** Preserve D41 unchanged as the historical R1 record and refine it through this later
entry. Correct those two active Standard instructions to `AIDE_Build@v5` and `AIDE_Review@v2` and
issue the resulting Documentation Methodology correction as `AIDE_DocumentationMethodology@v26`
with `DocumentationMethodology_Guide_v26`. The v26 transition posture is `None` because this is a
non-substantive current-reference correction and record clarification rather than a consumer-state
transformation.

**Boundary.** This correction does not perform a general footer `Dependencies:` / `References:`
currency sweep, does not rewrite historical Decisions references, and does not establish a general
rule connecting versioned in-body capability references with dependency/conformance checkpoints.
That broader relationship remains reserved for Review C / Dependencies.

**Consequences.** The current executable Documentation Methodology instructions now target
`AIDE_Build@v5` and `AIDE_Review@v2`; D41 remains visible as the original R1 event while D42 makes the
scope of that verification truthful. No new mechanism, Review B work-state semantic, or general
reference/dependency policy is introduced.


## D43 — Semantic sections may have several permitted hosts but one authority

Documents are hosts. A section owner may define several permitted/default hosts, but each semantic
scope has one authoritative instance. Compact-first hosting and structural relocation avoid a
universal section registry.

## D44 — Knowledge is a top-level-Topic lateral asset store

Create zero or one current Knowledge document per top-level Topic by default, only when needed.
Knowledge is non-executable until reconciled into an authoritative owner and uses stable `K` entries
where useful.

## D45 — Decisions remains deliberately broad

Knowledge does not narrow Decisions. Topic/subtopic-specific investigation, working, alternatives,
reasoning and evolutionary knowledge continue to belong there alongside explicit decision history.

## D46 — Binders are Documentation-Topic work/context boundaries

One Binder per top-level Documentation Topic is the default; partition only for demonstrated
volume/context/work-management need and cover the parent corpus through a lightweight Binder-set
index. Review material is not renamed Binder.

## D47 — Index navigates; Overview explains

Index is the structural/machine navigation entry point. Overview remains a human high-level/TLDR
snapshot. File-based contexts may navigate masters directly.

## D48 — Issue Documentation Methodology v27

Publish `AIDE_DocumentationMethodology@v27` with transition posture `None`. The release adds
prospective hosting/navigation/document-role rules and does not require mass relocation of existing
sections or creation of empty Knowledge documents.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Index@v2, DocumentationMethodology_Design_v24
References: DocumentationMethodology_Guide_v27, Core_Index_Decisions_v1, WorkingPractices_Decisions_v5, AIDE_WorkPackage@v2
