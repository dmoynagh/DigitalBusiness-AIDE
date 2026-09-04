# AIDE Documentation Methodology — Standard

> **Identity:** `AIDE_DocumentationMethodology@v18`
> **Common name:** Documentation Methodology
> **Version 18**
> > **Published:** 2026-08-31
>
> **Default weight:** Expectation

## Purpose

Provide the canonical AI-facing contract for creating, naming, structuring, recording, versioning,
distributing and maintaining AIDE-governed document corpora.

This Standard is the normal runtime/deployable representation of Documentation Methodology.
`DocumentationMethodology_Guide_v18` is its fuller human-oriented companion.

## Ownership boundary

**Weight: Requirement**

Documentation Methodology owns governed document naming, type/document lifecycle, corpus structure,
Index/register behaviour, document metadata-container placement, archive/supersession conventions,
document distribution rules, asset/unmanaged recording, and document output/version discipline.

Do not absorb semantics owned elsewhere:

- Core owns formal Identity.
- `AIDE_Tags` owns Tags content/build/query.
- `AIDE_Dependencies` owns dependency identity, presence, order, version and conformance checkpoints.
- `AIDE_Migration` owns transition discovery/execution/progress.
- `AIDE_Review` owns generic Review lifecycle.
- `AIDE_WorkPackage` / `AIDE_Build` own generic execution/return behaviour.
- Project/domain owners own substantive document content and project-specific topic choices.

Where this Standard hosts another owner's metadata/state, preserve that owner's semantics.

## Core corpus principles

**Weight: Expectation**

1. Keep one authoritative answer per question; reference rather than restate.
2. Route information by kind: Brief defines, Design determines, Decisions records reasoning,
   outcomes deliver, OpenItems tracks unresolved work, WorkRegister tracks confirmed consequences,
   Index records the corpus.
3. Treat filenames as legible locators and the nearest authoritative Index as the resolver.
4. Distribute only document types whose distribution contract permits it.
5. Keep human-readable documents as short as their function permits and conclusion-first.
6. A confirmed change with a downstream consequence is applied in the same pass or registered.
7. Version issued outputs, not drafting edits.
8. Do not leave material confirmed state only in conversation where it is at risk of loss.
9. Prefer an existing mechanism over adding another one.

## Naming

**Weight: Requirement**

Normal governed Markdown filename:

```text
{Project}_{Topic}_{DocType}[_{Key}]_v{N}.md
```

- Omit Project only for standalone material outside a project.
- Omit Topic for project-wide registers.
- Resolve DocType from an established or locally declared custom type.
- Add a key only where the type's contract calls for one.
- Keep the version suffix last.
- Compound Topic segments may express instantiation/subdivision and may nest.
- A filename is not the authoritative type/topic registry; the Index is.

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
- WorkPackage: opening date mandatory; a separate WorkPackage Outcome uses the same key.
- Archive marker `_Archived_{date}` is inserted after DocType and before an existing key.

## Document role model

**Weight: Requirement**

```text
Brief / Requirements
        ↓
      Design  ← Decisions
        ↓
     outcomes
```

- **Brief** — objective, scope, requirements, success signals; optional by stakes.
- **Requirements** — standing cross-topic requirements when size warrants splitting from Brief.
- **Design** — confirmed current position; declares produced outcomes and external handlers.
- **Decisions** — reasoning/history informing future Design. It is not a downstream outcome input.
- **Working** — mutable design-in-progress.
- **Review** — faithful point-in-time assessment record. Generic Review behaviour comes from
  `AIDE_Review`.
- **Guide** — distributable explanatory outcome.
- **Reference** — distributable lookup outcome.
- **Glossary** — distributable definitions.
- **Overview** — standing narrative/orientation outcome.
- **WorkPackage** — document representation of a unit of Build work; execution semantics are
  `AIDE_WorkPackage`.
- **WorkPackage_Outcome** — separate live return document where used; folds into WorkPackage on
  archival.
- **Message** — governed cross-project transmission.
- **Index** — corpus/topic/document/configuration registry.
- **OpenItems** — unresolved/in-flight work.
- **WorkRegister** — confirmed downstream consequences not yet applied.

Project-wide registers omit Topic.

An outcome must have an authoritative defining source. Decisions never substitutes for missing
Design content.

## Condensed and expanded topic documents

**Weight: Guidance**

A small topic may hold its internal Brief/Design/Decisions/Working material in one condensed file.
Use the highest-order confirmed content as its DocType.

Expand when retrieval, independent edit cadence, Working archival, blind review, or explicit
instruction makes separation valuable.

Index and WorkRegister remain container-level rather than condensing into a topic file. A Guide
does not condense into its Design because they have different roles/distribution.

## Working

**Weight: Expectation**

Working is Design in progress and may change freely.

Use it for material discussion that must survive beyond chat but is not yet confirmed Design.
When content confirms, move the confirmed position into Design and the material reasoning into
Decisions. Archive/dispose the Working record according to its resolved lifecycle; do not leave it
as a second source of truth.

## Decisions

**Weight: Expectation**

Record enough reasoning to prevent material alternatives/constraints from being re-derived from
scratch later.

A Design change should have a corresponding Decisions entry when the reasoning is material.
Existing Decisions entries are historical records and are not retroactively rewritten to make
today's design look inevitable.

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

A governed Message uses:

```text
{Source}_Message_{Recipient}_{Description}[_Reply-{N}]_{YYYY-MM-DD}-{N}_v{N}.md
```

A promoted Message body is a structured envelope with the fields needed to identify parties,
thread/message identity, revision, reply relation, time state, requested response and optional
forward/merge/lifecycle information.

Rules:

- message identity/threading does not depend on Timestamp;
- Timestamp is read from an available clock; if unavailable, state the reduced/unknown precision
  rather than composing a plausible value;
- a mandatory field must have a representable unknown/none state;
- only the `From` owner issues a new revision of the same message;
- a forward is a new message citing the original;
- the terminator is part of completeness; an incomplete/truncated message is not acted on;
- source marking is used only where source materially changes evidential weight;
- out-of-band statements are marked as such;
- light messages may remain conversation-only; promoted/heavy messages use normal governed-file
  behaviour.

Delivery tracking/transport is owned by the communication process, not this Standard.

## Index

**Weight: Requirement**

Every governed project/container has one authoritative Index for each undelegated branch.

The Index records, as applicable:

- project/topic identity;
- topic declarations and parent/inheritance/mode;
- current document register and versions;
- local/custom type declarations;
- assets/unmanaged-file records;
- delegation to child Indexes;
- withdrawn/renamed/rehomed names where a reader may hold a dead locator; and
- local configuration owned by the project.

Nearest Index wins. Delegate only when a branch has sufficiently independent cadence/size/retrieval
needs; the parent then records the delegated path/pointer rather than duplicating the child list.

## OpenItems and WorkRegister

**Weight: Expectation**

Use **OpenItems** for unresolved/in-flight work and enough context to resume it.

Use **WorkRegister** for consequences of confirmed decisions that are not yet applied.

A confirmed design change with an unapplied downstream consequence belongs in WorkRegister, not
OpenItems. Remove/close entries when their governing lifecycle says their work is resolved; do not
use either register as a second Decisions history.

## Storage, supersession and archival

**Weight: Requirement**

Current master documents remain in the active project/master folder.

- **superseded**: an older issued version or a document replaced/withdrawn before its own terminal
  lifecycle event.
- **archived**: a document whose own type reached its terminal event.
- Generated Binders/Bundles are consumption artefacts; regenerate rather than treating them as
  authoritative masters.

Do not delete governed history merely to simplify the active view. Use the correct disposition.

A living current-document register need not list every lower superseded version where version
sequence already proves their existence; preserve explicit mapping for renamed/rehomed/withdrawn
names where sequence cannot resolve the old locator.

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

A file's `_vN` counts issued outputs of that document, not internal editing operations.

- Draft freely before issue.
- After an issued/delivered document is changed and reissued, increment its document version.
- A rename alone is not a semantic content revision unless the governing lifecycle explicitly
  makes it one.
- Do not issue new versions/documents as ceremony.
- At the end of a material unit of work or key confirmation point, assess whether confirmed state
  is at risk of being left only in conversation.
- Where confirmed material is at material risk of loss, surface the exposure and write the safe
  durable outputs authorised by the work.

## WorkPackage document integration

**Weight: Requirement**

Generic WorkPackage authoring/execution/validation/return semantics come from
`AIDE_WorkPackage@v1` and `AIDE_Build@v1`.

This Standard owns only document integration:

- the WorkPackage is a governed point-in-time document with opening-date key;
- a separate live WorkPackage Outcome uses the same key where produced;
- after the director/Lead reconciles the returned Outcome, it may be appended verbatim to the
  WorkPackage before archival;
- the consolidated archived WorkPackage records the absorbed Outcome locator where useful;
- design-shaping issues returned by Build are resolved by Project Design rather than silently
  settled by document mechanics.

## Documentation Methodology conformance

**Weight: Requirement**

Current conformance is recorded through Dependencies:

```text
Dependencies: !AIDE_DocumentationMethodology@v18
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
  CurrentVersion: v18
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
```

Merely reading/using a v17 document does not trigger this OnUpdate transition.

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

```yaml
Transition:
  Version: v18
  Posture: OnUpdate
```

---
Dependencies: AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_Tags@v1, AIDE_WorkPackage@v1, AIDE_Build@v1
References: DocumentationMethodology_Design_v14, DocumentationMethodology_Guide_v18
