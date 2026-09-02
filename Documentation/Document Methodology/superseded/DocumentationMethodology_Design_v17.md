# Documentation Methodology — Design

> **Version 17** (2026-08-31). Separates document lifecycle semantics from physical
> repository/storage workflow, preserves governed-history requirements, and declares the v20
> Standard/Guide outcomes.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Documentation Methodology provides the common document/corpus contract for AIDE-governed work.

It owns:

- governed document naming and filename structure;
- document types and their document-specific lifecycle;
- lifecycle state/disposition semantics, including **Current**, **Superseded** and **Archived**;
- the requirement to preserve governed document history and dead-locator resolvability where needed;
- topic/document organisation semantics and Index/register behaviour;
- document metadata-container placement and coexistence;
- the authority boundary between authoritative masters and generated consumption artefacts;
- distribution rules for document types;
- document output/version discipline;
- asset/unmanaged-file recording boundaries; and
- document-specific rendering/integration of externally owned metadata or state.

It does **not** own:

- the substantive content or quality criteria of another domain's documents;
- physical repository/storage layout or management-folder names;
- movement of files between current, superseded or archival storage locations;
- repository sweep/external-archive cadence, Change Delivery staging, or Binder placement/replacement workflow;
- formal identity semantics — Core;
- Tags grammar/build/query — `AIDE_Tags`;
- dependency identity/version/conformance semantics — `AIDE_Dependencies`;
- transition execution — `AIDE_Migration`;
- generic Review lifecycle — `AIDE_Review`;
- generic WorkPackage execution/return behaviour — `AIDE_WorkPackage` / `AIDE_Build`; or
- platform packaging/deployment mechanics.

The governing principle is one owner per mechanism: Documentation Methodology defines document
semantics and hosts document structure; Working Practices or the applicable environment realises
those semantics physically.

## §2 — Layered model

### Level 1 — intent/system

A governed corpus should let a human or AI answer, cheaply and reliably:

- what documents exist and which are current;
- what each document is for;
- what filename/type/lifecycle rules apply;
- what is internal versus distributable;
- what is confirmed versus working/history;
- what changed, what remains open, and what consequences are pending;
- what metadata/state is attached without conflating ownership; and
- what version/conformance state the document actually proves.

The model favours a small number of durable conventions over procedural ceremony.

### Level 2 — principal concepts

```text
Brief / Requirements
        ↓
      Design  ← Decisions
        ↓
     outcomes
        │
        ├── Standard / Guide / Reference / Glossary / Overview
        └── WorkPackage (document integration only)

Working = Design in progress
Review  = point-in-time assessment record
Message = governed cross-project transmission
Index / OpenItems / WorkRegister = corpus registers
Asset / Unmanaged = explicitly outside normal governed-type behaviour
```

A document's **type** determines its document role/lifecycle. A domain owns the subject matter.
The Index is authoritative for what exists and for local topic/type configuration.

## §3 — Naming and topic model

Normal governed Markdown filename:

```text
{Project}_{Topic}_{DocType}[_{Key}]_v{N}.md
```

Project-wide registers omit Topic. Point-in-time types use the applicable date-sequence/key rules.
Compound topic segments express instantiation or subdivision and may nest.

A filename is legible; the nearest authoritative Index resolves topic/type/current version.

Cross-references may be explicitly version-qualified or deliberately unqualified. The form carries
the author's intent; neither form is silently converted into the other.

## §4 — Document types and outcomes

The established document types and their document-specific semantics are published by the
Documentation Methodology Standard/Guide. The confirmed Design must determine the substantive
behaviour needed to produce those outcomes; the Guide is not a substitute source for capability
meaning missing from Design.

Key model rules:

- Brief defines objective/scope/requirements.
- Design records the confirmed current position and declares outputs.
- Decisions records the synthesized reasoning/history needed by a future Design reader to
  understand why the confirmed position exists and what credible paths were set aside. It informs
  future Design and is not a downstream outcome input.
- A Decisions event is owed for a change to the confirmed substantive Design position, a
  requirement established or materially revised, or a rejected alternative a future reader could
  reasonably re-derive. Purely editorial, formatting, metadata, migration, mechanical maintenance,
  or application of an already-recorded decision does not by itself create a new Design decision.
- Decisions depth is proportional to the thinking actually involved. As applicable, preserve the
  trigger/requirement, problem found, genuine alternatives, key distinctions/reasoning, decision,
  and important consequences/trade-offs. Preserve enough to reconstruct why the decision was
  reached; do not preserve discussion merely because it occurred.
- Non-trivial rejected alternatives receive at least a brief reason. Genuinely trivial alternatives
  may be omitted.
- A substantive Design change and its Decisions record are produced in the same pass so confirmed
  reasoning is not left only in conversation. Existing Decisions entries remain historical and are
  not retroactively rewritten; later entries may supersede, refine, reverse, constrain or
  reinterpret them.
- Decisions follows Design granularity. An independently expanded child Design normally has its
  substantive reasoning at that same child scope; parent-level reasoning remains parent-level.
  Condensed topics may satisfy the same rule with a Decisions section.
- Decisions history splits only when retrieval quality deteriorates; prefer closure/state-based
  volumes over arbitrary chronology, and do not delete or rewrite history merely to shorten the
  active record.
- Working is mutable design-in-progress. When its items complete, the document's lifecycle may
  resolve to Archived where the Working record itself merits terminal retention, or to
  Superseded/withdrawn where its substantive value is fully represented in retained authoritative
  records; the physical handling of either state is external.
- Review is a point-in-time assessment record; generic assessment behaviour belongs to
  `AIDE_Review`.
- Guide is a distributable explanatory outcome.
- Index, OpenItems and WorkRegister are container-level records with distinct purposes.
- Custom types are local until promoted by demonstrated reuse.
- Assets and unmanaged files are not silently converted into governed document types.

### Lifecycle/disposition boundary

Lifecycle state is semantic, not a folder name:

- **Current** — the issued authoritative version/instance the corpus resolves for normal current use.
- **Superseded** — an older issued version, or a document displaced/withdrawn without reaching an
  archival terminal disposition of its own.
- **Archived** — a document whose type-specific lifecycle has reached an archival terminal
  disposition; the final archival record is frozen except by the type's permitted correction route.

A type may define a completion/absorption path that determines which terminal disposition applies.
The Index preserves enough current/history/rename information to keep the corpus truthful and
resolvable. Governed history is not discarded merely to simplify the active view.

Physical locations do not define these states. Folders, document-management systems, platform
history, external archives or another storage representation may implement them. Working Practices
or the applicable environment owns that physical implementation, including movement, cleanup and
retention-media conventions.

Generated Binders/Bundles are non-authoritative consumption artefacts assembled from authoritative
sources. Documentation Methodology owns that authority distinction; their physical placement,
replacement/supersession workflow and repository staging are operating-practice concerns.

## §5 — Metadata host boundary

A governed document may contain:

```text
Title / version preamble
Header metadata
Temporary owner-labelled state
Body
Footer metadata
Internal section
```

Documentation Methodology owns placement/coexistence/compact rendering.

Known semantic owners include:

- `Identity:` → Core;
- `Tags:` → `AIDE_Tags`;
- `Dependencies:` → `AIDE_Dependencies`;
- migration consequences/state → `AIDE_Migration`.

This is an extensible host, not a closed list.

Machine-generated metadata/state in human-readable documents should be as compact as practicable
while remaining unambiguous and machine-usable.

## §6 — Conformance and migration

Documentation Methodology conformance is a normal dependency checkpoint, not a separate
`Methodology:` version mechanism.

For current documents:

```text
Dependencies: !AIDE_DocumentationMethodology@v20
```

means the saved document is proven conformant through Documentation Methodology capability release
v20, subject to `AIDE_Dependencies` semantics.

The v18 transition posture remains `OnUpdate` for v17→v18. The v19 and v20 releases are `None`:
they change the canonical operating contract but require no structural/content transformation of
existing governed documents.

### Legacy v17 compatibility bridge

v17 predates the generic dependency checkpoint and commonly records:

```text
Methodology: v17
```

For the **v17 → v18 transition only**, when a governed document has no Documentation Methodology
dependency checkpoint but does contain an unambiguous legacy `Methodology: v17` declaration,
Migration interprets that declaration as the document's proven checkpoint:

```text
AIDE_DocumentationMethodology@v17
```

This interpretation exists only to establish migration input. It does not make the legacy line a
current Dependencies declaration and it does not modify the document merely by being read.

On the next qualifying modification/save:

1. use the legacy declaration as the v17 starting checkpoint;
2. apply the declared v18 OnUpdate transition;
3. establish the truthful v18 success state and remove the legacy `Methodology: v17` line;
4. reconcile true legacy `Depends on` relationships into `Dependencies:` while retaining ordinary
   citations as `References:`;
5. traverse the v19 and v20 `None` transitions when processing through current; and
6. save the truthful current dependency checkpoint without unrelated rewriting.

An operation that specifically requires v18-only structure may require the transition before that
operation proceeds.

## §7 — Output/version discipline

A document version counts issued outputs, not every edit in drafting.

Confirmed material must not remain only in conversation where it is at material risk of loss.
A substantive Design change and its Decisions reasoning are issued together in the same pass. The
reasoning is assembled from the work actually developed while it is available, rather than
reconstructed later from only the final Design position.

Do not create versions or files as ceremony; do not leave confirmed durable state unwritten merely
to avoid creating them.

## §8 — Published outcomes

This Design declares two published outcomes for capability release
`AIDE_DocumentationMethodology@v20`:

1. **`AIDE_DocumentationMethodology_Standard_v20.md`**  
   Canonical AI-facing behavioural contract. This is the deployable/runtime outcome used by AIDE
   Build/AI Deployment and included in the common Standards/Tools Bundle.

2. **`DocumentationMethodology_Guide_v20.md`**  
   Human-oriented explanatory companion containing the fuller rationale, examples and detailed
   document-type guidance.

The Standard and Guide derive from this Design and must not disagree about substance.

For this established methodology lineage, the canonical Standard filename version follows the Documentation Methodology release version so the v20 Standard and v20 Guide are visibly one release.

The Design remains the internal authority for future changes. Decisions records the reasoning
behind those changes and is not a downstream production input.

## §9 — Deployment and project-context model

The canonical Standard is the normal AI operating representation.

```text
DocumentationMethodology Design
        ↓
AIDE_DocumentationMethodology Standard
        ↓
Build / generated common Bundle
        ↓
AI Deployment / GPT Project context
```

Once the Standard is present in the common Bundle, ordinary AIDE GPT Projects do not need the
Guide solely to obtain operational methodology behaviour.

The Documentation Methodology GPT Project retains the Guide because it is the human/explanatory
outcome and the working project needs the full corpus.

No dedicated Documentation Methodology Tool is required at this stage. Existing generic Tools
(Migration, Review, Build Capability, etc.) perform the actions they own.

---
Dependencies: !AIDE_DocumentationMethodology@v20, AIDE_Dependencies@v2, AIDE_Migration@v1
References: DocumentationMethodology_Guide_v20, AIDE_StandardsProduction@v1
