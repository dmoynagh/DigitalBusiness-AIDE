# Capabilities — Work Register

> **Version 7** (2026-08-28). Reconciled after the canonical capability / Build WorkPackage /
> Deployment Set design pass. Retains the seven-component architecture, moves WorkPackage work to
> AIDE Build, and resets remaining work around Deployment, Scope, Dependencies, Review, and shared
> contracts.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## WR1 — Reconcile Standards child corpus

**Status:** Open — architecture now sufficiently shaped for later reconciliation

Rewrite `Capabilities_Standards_Brief` v1 and `Capabilities_Standards_Design` v3 against parent
Design v3.

Retain still-current Standard role, weights, facilitation framing, canonical production, and
Production/Usage output split.

Remove/revise:

- design-side generic platform realisation;
- Scope mechanics duplicated from Scope;
- Deployment mechanics;
- separate migration-source assumptions.

Add the canonical Standard outcome and transition-declaration model.

**Timing:** after Deployment/Scope/Dependencies/Review contracts are stable enough to reference
without another immediate rewrite.

---

## WR2 — Reconcile Tools child corpus

**Status:** Open — architecture now sufficiently shaped for later reconciliation

Rewrite `Capabilities_Tools_Brief` v1 and `Capabilities_Tools_Design` v1 against parent Design v3.

Retain Tool role, logical commands, interaction model, reporting, failure handling, and
idempotency.

Move generic platform implementation to Build-side platform Standards/Tools. Add canonical Tool
production and platform addenda.

---

## WR3 — Migration component design and production standard

**Status:** Open — parent model substantially settled

Create/reconcile Migration Brief and Design around:

- Required Migration / On-Update / no-transition postures;
- transition declarations embedded in canonical Standards/Tools;
- Migration Build Standard;
- canonical migration information;
- extraction/adaptation by platform and Deployment Set builders;
- `/migrations-check`, `/migrations-apply`, `/update-doc`;
- ordering, success/failure, idempotency, and escalation.

The previous requirement for separate source migration files is withdrawn.

---

## WR4 — Deployment component design

**Status:** Current priority

Complete Deployment from the completed Capability Package boundary.

Define:

- Deployment Config;
- Deployment Set identity and membership;
- platform resolution of a Deployment Set;
- package validation;
- composition/assembly from multiple packages;
- replacement/removal;
- deployment state;
- partial failure;
- resumption and idempotency;
- Git/repository publication where applicable;
- platform-specific deployment builders;
- rejection of defective packages.

Use the confirmed example:

```text
Deployment Set: workflow-core

Claude  → plugin "workflow-core"
Codex   → corresponding Codex capability collection
ChatGPT → workflow_core_bundle.md
```

---

## WR5 — Scope component review/design

**Status:** Open — confirm/rework

Review Scope from first principles against the new Build Config and Deployment model.

Explicitly separate:

- runtime applicability;
- Design/Build side applicability;
- build target platforms;
- Deployment Set membership;
- retrieval/discovery/trigger realisation.

Keep only mechanisms that genuinely answer Scope's applicability question.

---

## WR6 — Dependencies component review/design

**Status:** Open — confirm/rework

Confirm the minimal Dependencies contract:

- dependency identity;
- dependency/reference distinction;
- version last conformed/validated against;
- availability;
- version-gap detection;
- declaration advancement;
- handoff of version gaps to Migration.

Check interaction with Build-side installed Standards/Tools, packages, and Deployment Sets without
absorbing installation or deployment responsibility.

---

## WR7 — Review component design

**Status:** Open — finalise

Define:

- lead/reviewer responsibilities;
- finding/evidence/risk/remedy separation;
- disposition;
- review profiles;
- review record/outcome;
- iteration/review closure;
- any generic Review Standard/Tool.

Test profiles against Capability Design, Standard, Tool, Migration, WorkPackage, Package, and
Deployment review cases.

---

## WR8 — Shared identity/version contract

**Status:** Open

Define the minimum shared identity/version vocabulary needed by:

- canonical Standard/Tool;
- dependency declarations;
- transition ranges;
- Capability Package;
- Deployment Set/deployment state.

Distinguish source-document version, capability/release version, dependency conformance version,
transition source/target version, and deployment state where required.

Do not create a new top-level component solely for this contract.

---

## WR9 — Package/manifest contract

**Status:** Open

Define the smallest producer-to-Deployment contract:

- package identity/version;
- contents;
- platform contributions;
- Deployment Set applicability as required;
- transition material;
- removals;
- integrity;
- resumption/deployment-state information where required.

Package remains capability-local. Deployment Set assembly remains Deployment-owned.

---

## WR10 — Platform evidence and build/deployment standards

**Status:** Open — empirical/platform work

For each supported platform, record:

- available capability representation mechanisms;
- build-side adaptation rules;
- identity/version visibility;
- trigger/discovery behaviour;
- publication/update mechanics.

Initial targets:

- Claude;
- Codex;
- ChatGPT.

Generic capability Designs must not absorb this platform knowledge.

---

## WR11 — WorkPackage handoff to AIDE Build

**Status:** Moved outside Capabilities

Create the top-level AIDE **Build** topic and **WorkPackage** subtopic.

Design the WorkPackage Standard and WorkPackage Outcome contract for generic build-side
execution. Capabilities consumes it but does not own it.

Capability-specific requirements for the handoff remain in Capabilities Design/production
standards.

---

## WR12 — Documentation Methodology review handoff

**Status:** Open — intentionally deferred

Use `Capabilities_DocMethReviewItems` v1 when the separate Documentation Methodology review
begins. Add any newly discovered consequences rather than editing DocMeth piecemeal.

---

## Closed / superseded work from v6

- Parent architecture rewrite — completed and further refined in Design v3.
- `Design_Platform_{Name}` as the standard platform-realisation mechanism — superseded.
- Separate source migration artefacts as a parent requirement — superseded.
- Package manifest/build record pre-promotion to DocMeth — remains withdrawn.
- AIDE-scoped Standards Usage outcome — remains superseded by generic Standards Usage Standard.

---

## Current sequence

1. Deployment (`WR4`).
2. WorkPackage under AIDE Build (`WR11`) far enough to define the execution/Outcome contract.
3. Scope (`WR5`).
4. Dependencies (`WR6`).
5. Review (`WR7`).
6. Shared identity/version and package contracts (`WR8`, `WR9`) iteratively with the above.
7. Migration child design (`WR3`) and platform evidence (`WR10`).
8. Reconcile Standards and Tools child corpora (`WR1`, `WR2`).
9. DocMeth review later (`WR12`).

---

**Depends on:** `Capabilities_Decisions` v9.

**References:** `Capabilities_Design` v3, `Capabilities_OpenItems` v9,
`Core_System_Design` v2.

**Methodology:** v17
