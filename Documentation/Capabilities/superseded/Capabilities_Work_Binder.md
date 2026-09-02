# Capabilities Work Binder

> **Generated Binder — do not edit directly.** This file is a GPT Project consumption artefact, not an authoritative source document. Edit the individual master documents and regenerate the Binder.

Each source document below is included byte-for-byte unchanged between explicit source boundaries.

## Binder manifest

- `Capabilities_WorkRegister_v10.md` — sha256 `93eb025d1ef2`
- `Capabilities_OpenItems_v12.md` — sha256 `2e38d1075caa`
- `Capabilities_DocMethReviewItems_v3.md` — sha256 `256205f3085a`

---

<!-- BEGIN SOURCE: Capabilities_WorkRegister_v10.md -->
# Capabilities — Work Register

> **Version 10** (2026-08-29). Completes Migration, Standards/Tools reconciliation, shared
> version distinctions, and the producer-side Package/Deployment Manifest contract. Deployment and
> empirical platform evidence are now the next substantive work.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## WR1 — Reconcile Standards child corpus

**Status:** Completed

`Capabilities_Standards_Brief` v2 / `Capabilities_Standards_Design` v4 now retain the weight,
facilitation, Production/Usage and canonical-output model while consuming Tags, Scope,
Dependencies, Migration, Review, Build and Deployment boundaries rather than restating them.

---

## WR2 — Reconcile Tools child corpus

**Status:** Completed

`Capabilities_Tools_Brief` v2 / `Capabilities_Tools_Design` v2 retain logical actions,
inputs/decisions/escalation, reporting, failure/idempotency and canonical Tool behaviour; shared
Scope/Dependencies/Migration and Build-side platform realisation replace the stale local models.

---

## WR3 — Migration component design and production standard

**Status:** Completed

Produced `Capabilities_Migration_Brief` v1, `Capabilities_Migration_Design` v1,
`AIDE_Migration@v1`, and `Capabilities_Migration_Tool_Design` v1 covering:

- Required-on-use / OnUpdate-on-save / None;
- version-level posture and positive transition history;
- `MigrationSummary` fast path and skill-header optimisation guidance;
- checkpoint-on-save semantics;
- ordered multi-dependency execution using dependency declaration order;
- Required update through current including pending OnUpdate work;
- NotApplicable/Deferred/Failed semantics;
- durable partial progress and compact owner-labelled temporary state;
- exact-version treatment under governing consumer policy; and
- supported migration baselines/history pruning.

---

## WR4 — Deployment component design

**Status:** Open — next substantive architecture pass; requires user design input

Fixed inputs now include valid Package + Manifest, logical Deployment Sets, capability-local Build,
set-aware Deployment, and minimal producer manifest semantics.

Still define:

- Deployment Set lifecycle/state and removal semantics;
- Deployment Config ownership/inheritance/overrides;
- full vs incremental composition per platform;
- conflict handling;
- atomicity, partial failure, resumption and rollback posture;
- publication/Git/account/workspace mechanics;
- verification of successful deployment; and
- platform-specific deployment builders.

---

## WR5 — Scope component review/design

**Status:** Completed at model/design level

`Capabilities_Scope_Design` v1 / `AIDE_Scope@v1`.

---

## WR6 — Dependencies component review/design

**Status:** Completed at model/design/Standard level — v2 reconciliation complete

v2 adds default processing precedence from declaration order and final Migration-aligned checkpoint
semantics.

---

## WR7 — Review component design

**Status:** Completed at model/design/Standard/Tool-specification level

External Environment/communication seams remain tracked by WR14.

---

## WR8 — Shared identity/version contract

**Status:** Completed for the producer/pre-Deployment boundary

Current distinctions:

- DocMeth document version;
- capability release version;
- dependency conformance checkpoint;
- package build identity/integrity; and
- deployment state.

Deployment may add target-state fields but must not collapse these meanings.

---

## WR9 — Package/manifest contract

**Status:** Completed at producer boundary; Deployment may extend only by demonstrated need

Package = payload/build instance of one capability release.

Manifest = logical deployment intent with PackageId, capability identity/release, logical target
set/platform, contribution selection, replace/remove intent where needed, and integrity.

Physical destination belongs Deployment Config.

---

## WR10 — Platform evidence and build/deployment standards

**Status:** Open — empirical; may run before/alongside Deployment

For Claude, OpenAI/ChatGPT/Codex and other supported surfaces establish:

- actual capability representation;
- Build adaptation;
- identity/version/MigrationSummary visibility;
- Scope/trigger realisation;
- bootstrap behaviour;
- composition;
- install/update/remove;
- publication/pickup; and
- deployment verification/failure state.

**Immediate proof:** package a representative Standard (recommended `AIDE_Tags`) as an OpenAI
plugin/skill implementation and test end-to-end in ChatGPT web and Codex before making the proposed
shared OpenAI plugin the primary Deployment mapping. Treat the ChatGPT bundle as compatibility/
bootstrap/fallback until evidence resolves the route.

---

## WR11 — WorkPackage handoff to AIDE Build

**Status:** Moved outside Capabilities

---

## WR12 — Documentation Methodology review handoff

**Status:** Open — intentionally later

`Capabilities_DocMethReviewItems` v3 now includes generic temporary document state, compact
machine-content rendering, metadata containers, Tags/Dependencies/Identity, and Migration/update
integration.

---

## WR13 — Tags component design and Standard

**Status:** Completed at model/design level

---

## WR14 — Review external environment and communication handoff

**Status:** Open — separate shared architecture work

Environment resolver must supply current model/reviewer/capability/route/fallback/preferences facts.
Shared communication must supply direct/indirect send/return, correlation, delivery/failure state and
AI Message relay. Review and future Research consume these without owning transport.

---

## Current sequence

1. Platform evidence proof where it materially informs Deployment (especially OpenAI plugin/skills).
2. Deployment design (`WR4`).
3. Complete broader platform build/deployment standards/evidence (`WR10`) as required/parallel.
4. Resolve Environment/shared communication ownership (`WR14`) with the owning workstreams.
5. Documentation Methodology review later (`WR12`).

WorkPackage remains the separate AIDE Build workstream.

---

**Depends on:** `Capabilities_Decisions` v12.

**References:** `Capabilities_Design` v6, `Capabilities_OpenItems` v12,
`Capabilities_Migration_Design` v1, `Capabilities_DocMethReviewItems` v3.

**Methodology:** v17
<!-- END SOURCE: Capabilities_WorkRegister_v10.md -->

---

<!-- BEGIN SOURCE: Capabilities_OpenItems_v12.md -->
# Capabilities — Open Items

> **Version 12** (2026-08-29). Closes Migration, Standards/Tools reconciliation, shared version
> distinctions and the producer-side Package/Manifest question. Deployment behaviour and platform
> evidence are now the principal open Capabilities work.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## Q1 — Deployment Set contract

**Status:** Open — Deployment pass

Define set lifecycle/state, membership/removal semantics, composition/rebuild and verification.

## Q2 — Deployment Config ownership and shape

**Status:** Open — Deployment pass

Define where logical Deployment Set/platform mappings live, inheritance/overrides, credentials/
access boundaries, and physical destination resolution.

## Q3 — Deployment assembly/failure behaviour

**Status:** Open — Deployment pass

Define full vs incremental assembly, conflicts, atomicity, partial failure, resumption, rollback
posture, integrity verification, and publication state.

## Q4 — Scope boundary

**Status:** Resolved — `Capabilities_Scope_Design` v1 / `AIDE_Scope@v1`.

## Q5 — Dependencies contract

**Status:** Resolved — `Capabilities_Dependencies_Design` v2 / `AIDE_Dependencies@v2`.

v2 adds declaration-order processing precedence and final saved-checkpoint semantics.

## Q6 — Review purpose/model/integration

**Status:** Resolved — Review child corpus v1.

## Q7 — Shared identity and version contract

**Status:** Resolved for current architecture

Distinct concepts are:

- document version;
- capability release version;
- dependency conformance version;
- package build identity/integrity; and
- deployment state.

Deployment may define additional state fields but not another semantic capability version without a
demonstrated need.

## Q8 — Capability Package and Deployment Manifest contract

**Status:** Resolved at producer boundary

Package identifies the concrete build of one capability release. Manifest carries only logical
placement/lifecycle intent needed by Deployment: PackageId, capability identity/release, target
Deployment Set/platform, contribution selection, replace/remove intent where required, and
integrity. Physical destinations are Deployment Config.

Deployment may extend this contract only where its design demonstrates another required input.

## Q9 — Build Config inheritance/defaults

**Status:** Open — detail, not current blocker

Confirmed fields remain platforms, side (default both), and Deployment Set(s). Resolve inheritance/
overrides when Environment/Deployment configuration is designed.

## Q10 — WorkPackage integration

**Status:** Moved to AIDE Build.

## Q11 — Platform build/deployment evidence

**Status:** Open — empirical and now immediately useful

For Claude/OpenAI/ChatGPT/Codex establish representation, skill/plugin/header discovery,
MigrationSummary visibility, Scope/trigger/bootstrap realisation, composition, install/update/remove,
publication/pickup, and verification/state.

**OpenAI hypothesis to test, not architecture yet:** one OpenAI plugin containing skills may be a
common primary Deployment Set representation for ChatGPT and Codex, with a project bundle retained
as compatibility/bootstrap/fallback. Prove this using a representative Standard before Deployment
locks the mapping.

## Q12 — Environment settings home consumed by Review

**Status:** Open — external to Review

Resolve storage/inheritance for available AI families/models/capabilities/routes/fallbacks,
preferences and access/usage/cost constraints.

## Q13 — Shared communication capability ownership

**Status:** Open — external to Review; coordinate with Research

Resolve permanent ownership of direct/indirect inter-AI send/return, correlation, delivery/failure
state and AI Message relay.

## Q14 — Migration model

**Status:** Resolved

`Capabilities_Migration_Design` v1 / `AIDE_Migration@v1` / Migration Tool Design v1 cover trigger,
posture, summary, transition history, ordering, checkpoints, partial failure/defer, exact-version
policy seam and supported baseline.

---

**Depends on:** `Capabilities_Decisions` v12.

**References:** `Capabilities_Design` v6, `Capabilities_WorkRegister` v10.

**Methodology:** v17
<!-- END SOURCE: Capabilities_OpenItems_v12.md -->

---

<!-- BEGIN SOURCE: Capabilities_DocMethReviewItems_v3.md -->
# Capabilities — DocMeth Review Items

> **Version 3** (2026-08-29). Adds the generic compact temporary-document-state requirement, the
> compact machine-content principle, and reconciles update behaviour with the completed Migration
> contract.
>
> Created: 2026-08-28 | Last modified: 2026-08-29

---

## Purpose

Keep Capabilities decisions that affect Documentation Methodology visible without resolving them
inside the Capabilities architecture pass. Each item below is a review input, not an instruction
to edit DocMeth in isolation.

---

## DR1 — Move dependency semantics to Dependencies and generalise footer hosting

**Source decisions:** `Capabilities_Decisions` v10 (`D46`, `D65`–`D68`),
`Core_System_Decisions` v2 (`D10`)

Review `DocumentationMethodology_Guide` v17 §3c, especially:

- the meaning/rendering of `Depends on` and `References`;
- dependent-side declaration;
- version history/footer-update behaviour;
- the fixed three-line footer shape.

Target boundary:

- **DocMeth** owns generic document header/footer metadata containers, placement, and block-hosting
  rules;
- **Dependencies** owns the `Dependencies:` property content, compact grammar, required/startup
  posture, identity resolution, conformance-version meaning, and advancement rules;
- **Migration** owns consequences of a version gap;
- **References** remain non-dependency citations and should be retained/reworked only where their
  document-specific value remains demonstrated.

The DocMeth review should make it possible for future components to add metadata blocks without
DocMeth enumerating or semantically owning them.

---

## DR2 — Reconcile the `Methodology` footer line with generic Dependencies

`DocumentationMethodology_Guide` v17 treats `Methodology: v17` as a special per-document
conformance record. Dependencies now provides a generic conformance-checkpoint model.

Review whether Methodology remains specialised, becomes a normal generated dependency (for
example on `AIDE_DocumentationMethodology`), or uses the Dependencies semantics with a
DocMeth-specific rendering.

Do not assume all documents in a project must move together until this is re-evaluated against
Required Migration and On-Update.

---

## DR3 — Keep local document types local by default

**Source decision:** `D53`

Retain the confirmed boundary that domains may define the types needed for their own outcomes;
DocMeth owns genuinely shared document types/components. Cross-domain recurrence is evidence for
promotion, not automatic promotion.

This pass has introduced a Capabilities-local `Standard` managed type for generated Standard
outputs. Treat that as another candidate to evaluate later, not as an instruction to promote it
now.

---

## DR4 — Do not pre-promote package manifest and build record

Package/Deployment Manifest remains a Capabilities production/deployment contract. Do not create
shared DocMeth types unless reuse outside Capabilities demonstrates the same semantic/lifecycle
need.

---

## DR5 — Confirm existing shared types/components rather than re-adding them

`DocumentationMethodology_Guide` v17 already includes Overview and created/last-modified metadata.
Do not duplicate them from older Capabilities work items.

---

## DR6 — Audit generic behaviour accumulated in DocMeth

The creation of Tags, Scope, Dependencies, Migration, and Review as shared Capabilities
components is evidence that some behaviour may have accumulated in DocMeth because no generic
owner existed.

Review candidate behaviour one concern at a time:

- tag/classification generation or matching that belongs to Tags;
- applicability or trigger behaviour that belongs to Scope;
- dependency/version-gap behaviour that belongs to Dependencies;
- transition behaviour that belongs to Migration;
- reusable assessment and disposition behaviour that belongs to Review.

Move behaviour only where the receiving component has a complete contract and DocMeth can consume
it without losing document-specific semantics.

---

## DR7 — Integrate Migration with document update without turning every edit into a full rewrite

A local edit is a qualifying update event for declared transition instructions; it is not permission
to reinterpret every current Standard and rework the whole document.

`/update-doc` should point to `AIDE_Migration` rather than restating transition logic. Under the
completed Migration contract, an update does **not** stop merely because Required Migration exists:
the document is already being changed/saved, so applicable Required and pending OnUpdate work are
reconciled together as far as successfully possible.

---

## DR8 — General header/footer metadata containers

**Source decision:** `Core_System_Decisions` v2 `D10`

Introduce or reconcile a generic document metadata-container model:

```text
Header metadata container
Body
Footer metadata container
```

DocMeth decides where these containers appear and how independently owned metadata blocks/properties
are added and formatted. The owner of each block decides its internal content and behaviour.

This prevents DocMeth from needing explicit knowledge of every capability that later contributes
machine metadata.

Current known consumers are:

- Identity → header metadata;
- Tags → footer metadata;
- Dependencies → footer metadata.

These examples must not become a closed list.

---

## DR9 — Tags footer property

`AIDE_Tags` defines compact document storage such as:

```text
Tags: design, release-ready, doctype:[design, platformdesign]
```

DocMeth should host the property in the footer metadata container without owning Tag Builder,
group, generation, cleanup, or query semantics.

Review how this interacts with the current mandatory footer shape and the `Internal` section.

---

## DR10 — Identity header metadata

**Source decision:** `Core_System_Decisions` v2 `D9`

A referenceable governed document may expose compact header metadata:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first identity is primary; later entries are alternate/exposed identities. Version belongs to
an identity entry, and identity matching ignores version.

Review the physical header placement, relationship to filename/document version, and whether the
existing Index identity/topic mechanisms need any reconciliation. Do not collapse canonical
identity into filename merely because filenames are currently the primary document locator.

---

## DR11 — Generic temporary document state container

Several capabilities need to attach temporary operational state to a document without making the
document methodology understand that state semantically. Examples include migration failure/defer,
validation errors, update errors, concurrency/conflict state, and incomplete processing.

DocMeth should define a generic compact location/structure/rendering for independently owned
temporary state entries. Each entry should require a human-readable title/name and a stable owner so
the owning capability can safely create, update, replace, or remove only its own entry.

Preferred human-facing shape:

```text
Title [Owner]
Message
```

The owner defines the meaning/lifecycle/content. DocMeth defines only placement, structure,
formatting, and coexistence of multiple owner entries.

---

## DR12 — Compact metadata and machine-generated content in human-readable documents

Adopt a general rendering principle for documents that may be read by humans:

> Metadata, derived state, and other machine-generated content should be as compact as practicable
> while remaining unambiguous and machine-usable.

This applies across Identity, Tags, Dependencies, migration summaries/state, validation state, and
future generated metadata. Prefer compact one-line/two-line forms over multi-line diagnostic blocks
inside the document; richer diagnostics belong in the active session/work record where appropriate.

---

## Review disposition

For each item, the later DocMeth review should record one of:

- retained in DocMeth as document-specific;
- moved to and consumed from a Capabilities component;
- split across a shared component and DocMeth rendering;
- deferred pending a component design;
- rejected, with reason.

No item in this document is considered applied until that review updates DocMeth and records its
own decisions.

---

**Depends on:** `Capabilities_Decisions` v12, `Core_System_Decisions` v2,
`DocumentationMethodology_Guide` v17.

**References:** `Capabilities_Design` v6, `Capabilities_WorkRegister` v10,
`Capabilities_Tags_Design` v1, `Capabilities_Dependencies_Design` v2,
`Capabilities_Migration_Design` v1.

**Type definition:** `DocMethReviewItems` — review input. Holds consequences and questions for a
separate Documentation Methodology review without redesigning DocMeth in the originating pass.
Nearest established type: `Message`. Living until every item is dispositioned in the DocMeth
review. Internal.

**Methodology:** v17
<!-- END SOURCE: Capabilities_DocMethReviewItems_v3.md -->

---
