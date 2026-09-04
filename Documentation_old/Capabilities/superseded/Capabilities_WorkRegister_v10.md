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
