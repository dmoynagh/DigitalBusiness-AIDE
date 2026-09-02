# Capabilities — Work Register

> **Version 12** (2026-08-30). Moves generic Deployment to the AI Deployment
> workstream, closes the immediate OpenAI evidence gate, and closes the DocMeth review handoff.
> Standards Production/Usage Standards, canonical Review/Migration Tools, and Build Capability Tool
> Design/outcome are complete. Deployment and empirical platform evidence remain next.
>
> Created: 2026-08-27 | Last modified: 2026-08-30

---

## WR1 — Reconcile Standards child corpus

**Status:** Completed

`Capabilities_Standards_Brief` v2 / `Capabilities_Standards_Design` v4 retain the weight,
facilitation, Production/Usage and canonical-output model while consuming Tags, Scope,
Dependencies, Migration, Review, Build and Deployment boundaries rather than restating them.

Canonical outputs are now published as `AIDE_StandardsProduction@v1` and
`AIDE_StandardsUsage@v1`.

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
`AIDE_Migration@v1`, `Capabilities_Migration_Tool_Design` v1, and canonical
`AIDE_MigrationTool@v1` covering:

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

**Status:** Moved to AI Deployment — completed at initial generic model/Standard/Tool level

Generic Deployment is no longer a Capabilities-owned component. The producer Package +
deployment-intent boundary remains here; `AIDE_Deployment@v1` and `AIDE_DeploymentTool@v1`
own set-aware target reconciliation and verification.


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

**Status:** Completed at model/design/Standard/canonical-Tool level

Canonical `AIDE_ReviewTool@v1` is published. External Environment/communication seams remain
tracked by WR14.

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

**Status:** Immediate architecture gate completed; ongoing implementation evidence external

The tested local shared OpenAI plugin/skill route is rejected as a common ChatGPT + Codex runtime
mapping. Broader hosted/account/public routes and Claude/other platform mechanics remain empirical
implementation work for Build + AI Deployment target adapters.


---

## WR11 — WorkPackage handoff to AIDE Build

**Status:** Moved outside Capabilities

---

## WR12 — Documentation Methodology review handoff

**Status:** Completed by Documentation Methodology v18

`Capabilities_DocMethReviewItems` v4 now includes generic temporary document state, compact
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

## WR15 — Build Capability Tool

**Status:** Completed at Design/canonical-Tool level

`Capabilities_BuildCapability_Tool_Design` v1 and `AIDE_BuildCapabilityTool@v1` formalise the
previously implicit `Build Capability` production step as a named design-side Tool. It produces
canonical Standard/Tool outcomes from confirmed Design and stops before Build Config, WorkPackage,
platform Build, Package/Manifest and Deployment.

---

## Current sequence

1. Treat the Capabilities architecture as stable producer infrastructure.
2. Use AIDE Build for platform contribution production.
3. Use AI Deployment for set-aware target reconciliation/verification.
4. Resolve Environment/shared communication ownership with the owning workstreams.
5. Apply Documentation Methodology v18 OnUpdate as changed documents are saved.

WorkPackage remains the separate AIDE Build workstream.

---

**Depends on:** `Capabilities_Decisions` v14.

References: `Capabilities_Design` v8, `Capabilities_OpenItems` v14,
`Capabilities_Migration_Design` v1, `Capabilities_DocMethReviewItems` v4.

Dependencies: !AIDE_DocumentationMethodology@v18
