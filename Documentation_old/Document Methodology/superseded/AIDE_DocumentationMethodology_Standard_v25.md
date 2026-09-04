# AIDE Documentation Methodology — Standard

> **Identity:** `AIDE_DocumentationMethodology@v25`
> **Common name:** Documentation Methodology
> **Version 25**
> > **Published:** 2026-09-01
> > **Change:** Review B R1 pre-Round-2 preflight correction — align the current split-obligation
> > WorkPackage seam with `AIDE_WorkPackage@v3`; no new mechanism or ownership change.
>
> **Default weight:** Expectation

## Purpose

Provide the canonical AI-facing contract for creating, naming, structuring, recording, versioning,
distributing and maintaining AIDE-governed document corpora while preserving active work safely
and keeping confirmed Design aligned with delivered outcomes.

This Standard is the normal runtime/deployable representation of Documentation Methodology.
`DocumentationMethodology_Guide_v25` is its fuller human-oriented companion.

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
`AIDE_WorkPackage@v3` and `AIDE_Build@v4`.

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
Dependencies: !AIDE_DocumentationMethodology@v25
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
  CurrentVersion: v25
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

Transition:
  Version: v25
  Posture: None
```

Merely reading/using a v17 document does not trigger the v18 OnUpdate transition. v19, v20, v21,
v22, v23, v24 and v25 require no additional artefact transformation; when Migration traverses through current during
a qualifying save, their None transitions may advance the saved checkpoint after the v18 success
condition is satisfied. v22 does not require historical/superseded WIP renames or corpus-wide
rewrites; the corrected root-WIP convention applies prospectively to current/new checkpoints. v23 requires no consumer content transformation; it corrects current conformance to `AIDE_Index@v2`.
v24 requires no consumer content transformation; its clarified live-state semantics apply on the next
relevant substantive issue/update. v25 requires no consumer content transformation; it corrects the
current Review B split-obligation seam to the explicit `AIDE_WorkPackage@v3` contract without
changing the mechanism or ownership boundary.

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
References: DocumentationMethodology_Design_v22, DocumentationMethodology_Guide_v25
