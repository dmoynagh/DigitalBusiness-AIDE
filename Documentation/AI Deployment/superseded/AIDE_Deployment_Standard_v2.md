# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v2`
> **Common name:** AI Deployment
> **Version 2** (2026-08-31). Adds required-presence reconciliation, target-change policy and
> source/authority separation while preserving the set-aware deployment model.
>
> **Default weight:** Requirement

## Purpose

Make built deployable material available in intended AI runtime surfaces, reconcile desired composition and applicable required presence with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes:

- built platform contribution(s) or assembled deployable material;
- producer package/build identity and integrity;
- logical deployment intent / Deployment Set membership;
- applicable semantic required-presence facts owned by the producing artefact/dependency system; and
- environment-resolved target configuration and target-change policy.

Deployment does not reopen producer Design and does not redefine upstream requirements through Deployment Set membership.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition. It states which producer members should be realised together; omission from the Set does not cancel a member's semantic dependency/required-presence requirement.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family;
- runtime/surface;
- representation;
- distribution channel;
- destination/account/workspace reference where applicable;
- effective target-change policy/authority;
- refresh/session-pickup behaviour where relevant; and
- verification requirements.

Surface, representation, channel and target-change policy are independent facts.

## Deployment Policy

Before mutating a Target, resolve the effective environment/target policy that determines whether and under what conditions the change may be applied.

Policy may permit automatic action, require confirmation/external execution, or otherwise constrain install/update/remove/acquisition behaviour. The exact policy values are environment configuration; this Standard owns only the rule that Deployment must honour them.

Technical access, credentials or a reachable destination do not by themselves establish permission to modify the Target.

## Reconciliation

For each Target:

1. resolve desired Set membership, target configuration and effective Deployment Policy;
2. resolve applicable required-presence facts for intended target use;
3. validate package/contribution identity and integrity;
4. compose the target representation deterministically;
5. fail visibly on incompatible ownership/path/identity/namespace claims;
6. compare desired composition and required presence with observed deployed state;
7. surface any missing required material as a reconciliation mismatch/blocker rather than treating it as optional;
8. determine the necessary install/update/replace/remove actions;
9. apply only actions permitted by the effective Deployment Policy;
10. verify the resulting target/runtime state; and
11. persist/report Deployment Result and observed Deployment State.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

Full rebuild versus incremental patching is target implementation detail provided the same desired state, policy boundary and verification contract are preserved.

## Source and acquisition boundary

A source/catalog locator, trust in that source, permission to acquire/change a Target, and the deployment action itself are separate facts.

Naming or discovering a source does not authorise Deployment to fetch, install or execute it.

Generic package/source acquisition is not required by this release. If required deployable material is unavailable through established environment mechanics, report the missing material/blocker. A future acquisition mechanism may be inserted before reconciliation provided it independently resolves trusted source and Deployment Policy before obtaining or applying material.

## Failure and resumption

There is no generic all-or-nothing transaction across heterogeneous targets.

- Preserve previously verified state when failure occurs before mutation where possible.
- Record each Target independently.
- A multi-target deployment with mixed success is `Partial`.
- A Target that requires an unpermitted/manual action may be reported `Blocked` with the required next action rather than mutated.
- Re-running reconciles from observed state and avoids unnecessary semantic redeployment.
- Platform rollback is used only where the target actually supports it.

## Verification

UI presence, an enabled flag, or filesystem existence alone does not prove runtime availability.
Target-specific verification may include discovery, identity/version visibility, applicable required-presence checks, content probes, trigger behaviour and new-session pickup.

## Removal

Removal is the consequence of desired-state reconciliation. An assembled representation may be rebuilt without the removed member; an independently installed member may be uninstalled. Removal is still subject to the effective Deployment Policy.

## Artefact neutrality and manual channels

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other deployable artefacts use the same Deployment model when Build supplies the required target-compatible contribution/representation. Their semantic owner does not become the deployment owner.

A manually replaced project Bundle is a valid representation/channel implementation where the platform lacks automation. Later automated sync/install can replace that channel without changing Deployment Set semantics.

## Boundaries

- Producer/domain owns logical artefact semantics and its declared requirements.
- `AIDE_Dependencies` owns dependency/required-presence semantics.
- Build owns target-compatible member/contribution production.
- AI Deployment owns set-aware composition, policy-aware delivery/reconciliation, mismatch reporting and verification.
- Environment/platform configuration owns physical target facts, access references and actual target-change policy/authority values.
- Bootstrap owns startup discovery/surfacing, not deployment action or verification.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none
```

```yaml
Transition:
  Version: v1
  Posture: None
```

```yaml
Transition:
  Version: v2
  Posture: None
```

No persisted consumer-state transformation is required to adopt v2.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v2, AIDE_Dependencies@v2
References: AIDE_Build@v1
