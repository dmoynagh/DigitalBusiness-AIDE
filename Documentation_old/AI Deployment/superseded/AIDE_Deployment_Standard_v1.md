# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v1`
> **Common name:** AI Deployment
> **Version 1** (2026-08-30). First published deployment contract for reconciling deployable
> artefacts into verified AI runtime targets.

## Purpose

Make built deployable material available in intended AI runtime surfaces, reconcile desired
composition with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes:

- built platform contribution(s) or assembled deployable material;
- producer package/build identity and integrity;
- logical deployment intent / Deployment Set membership; and
- environment-resolved target configuration.

Deployment does not reopen producer Design.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family;
- runtime/surface;
- representation;
- distribution channel;
- destination/account/workspace reference where applicable;
- refresh/session-pickup behaviour where relevant; and
- verification requirements.

Surface, representation and channel are independent facts.

## Reconciliation

For each Target:

1. resolve desired Set membership and target configuration;
2. validate package/contribution identity and integrity;
3. compose the target representation deterministically;
4. fail visibly on incompatible ownership/path/identity/namespace claims;
5. compare desired state with observed deployed state;
6. perform the necessary install/update/replace/remove actions;
7. verify the resulting target/runtime state; and
8. persist/report Deployment Result and observed Deployment State.

Full rebuild versus incremental patching is target implementation detail provided the same
desired state and verification contract are preserved.

## Failure and resumption

There is no generic all-or-nothing transaction across heterogeneous targets.

- Preserve previously verified state when failure occurs before mutation where possible.
- Record each Target independently.
- A multi-target deployment with mixed success is `Partial`.
- Re-running reconciles from observed state and avoids unnecessary semantic redeployment.
- Platform rollback is used only where the target actually supports it.

## Verification

UI presence, an enabled flag, or filesystem existence alone does not prove runtime availability.
Target-specific verification may include discovery, identity/version visibility, content probes,
trigger behaviour and new-session pickup.

## Removal

Removal is the consequence of desired-state reconciliation. An assembled representation may be
rebuilt without the removed member; an independently installed member may be uninstalled.

## Boundaries

- Producer/domain owns logical artefact semantics.
- Build owns target-compatible member/contribution production.
- AI Deployment owns set-aware composition, delivery/reconciliation and verification.
- Environment/platform configuration owns physical target facts and access references.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v1, AIDE_Dependencies@v2
References: AIDE_Build@v1
