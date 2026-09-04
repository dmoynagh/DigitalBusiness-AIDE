# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v5`
> **Common name:** AI Deployment
> **Version 5** (2026-09-02). Adds the Deployment Registry/Deployable Package boundary,
> immutable Registry lifecycle and Release Batches while retaining v4 desired-state reconciliation.
>
> **Default weight:** Requirement

## Purpose

Make validated built deployable material available for intended AI runtime surfaces, reconcile desired composition and applicable required presence with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes validated **Deployable Packages** from the configured **Deployment Registry**.

A Deployable Package supplies, directly or through its PackageKind contract:

- Logical Package Identity, unique concrete PackageId and integrity evidence;
- authoritative/canonical source and Build provenance sufficient to identify the produced result;
- deployment-facing built outputs/members and Build-owned `CompositionPosture: MemberContribution | AssembledConsumptionArtefact` where applicable;
- applicable producer-owned dependency/Migration and other required downstream metadata; and
- package-kind-specific validation evidence and extensions needed for correct Deployment.

`Capability Package` is the first specialised Deployable Package kind. Deployment does not reopen producer Design, reconstruct canonical semantics, or treat Registry/deployed state as semantic production authority.

## Deployment Registry

The Deployment Registry is the authoritative source of validated built supply available to Deployment. Its physical implementation may be a folder, Git repository, package store, service or another configured mechanism that preserves the required contract.

Registry package instances are immutable under `PackageId`. A stable Logical Package Identity may have successive PackageIds; Registry-owned `Current Package` state identifies the instance normally selected by current/floating resolution.

Registry-owned lifecycle state is separate from immutable package content:

```text
Available   — normal resolution eligibility
Deprecated  — remains available but discouraged; warn/prefer suitable replacement
Withdrawn   — retained historically but excluded from ordinary new/current resolution
```

Physical purge is retention maintenance and is not an automatic v5 Deployment lifecycle action.

Use `AIDE_DeploymentRegistryTool` for Register, Release Batch and Registry lifecycle actions. Generic ordinary Build publication does not establish Registry state.

## Tags

Deployable Packages and individual built target/member outputs may carry `AIDE_Tags` values.

For Deployment selection, the effective Tags for a built target/member are the union of Package Tags and that target/member's Tags. Use `AIDE_Tags` Boolean query semantics; satisfy applicable freshness requirements before relying on generated Tags.

Tags are classification/selection only. They do not replace semantic Dependencies, Scope, Build-target compatibility, Migration posture or Deployment Policy.

## Release Batch and triggers

A Release Batch may stage several package registrations/lifecycle changes until an explicit Release operation validates and exposes them together.

Batch Release is an atomic **Registry visibility** boundary only; it does not claim an all-or-nothing transaction across heterogeneous runtime Targets.

Registry events may cause configured Deployment Triggers to re-evaluate affected Deployment Set Definitions. Re-evaluation is idempotent: if the concrete desired result is unchanged, no deployment package/delivery mutation is required.

Detailed Set selectors/output definitions/Delivery Actions remain governed by the current Deployment Set configuration and may be refined independently of this Registry contract.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition. It states which eligible built members should be realised together; omission from the Set does not cancel a member's semantic dependency/required-presence requirement.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family and runtime/surface;
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

Technical access, credentials, Registry availability or a reachable destination do not by themselves establish permission to modify the Target.

## Reconciliation

For each requested Set/Target:

1. resolve the applicable Deployment Set, selected Registry supply and configured Target/Policy;
2. resolve exact PackageId/member/build-output identity and verify package/member integrity/provenance;
3. reject ordinary selection of Withdrawn packages and surface Deprecated selection where no suitable non-deprecated result replaces it;
4. resolve applicable semantic required-presence facts for intended target use;
5. validate Build-declared composition posture and required package-kind extensions/handlers;
6. where the Target requires set-level assembly, mechanically assemble eligible `MemberContribution` outputs deterministically without semantically re-rendering them;
7. treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary; if that composition must change, require the corresponding replacement Build output;
8. fail visibly on missing posture-compatible Build output, unresolved mandatory extension, or incompatible ownership/path/identity/namespace/posture claims;
9. read/resolve observed target state where possible;
10. compare desired composition and applicable required presence with observed deployed state;
11. surface missing required material as a mismatch/blocker rather than making Set omission redefine the requirement;
12. determine the minimum install/update/replace/remove actions needed;
13. apply only actions permitted by Deployment Policy;
14. run the Target verification contract; and
15. persist/report per-Target Deployment Result and observed Deployment State.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

## Production and provenance boundary

Build/specialised producer Build is upstream of Deployment. It renders/transforms current authoritative semantics into concrete deployable outputs/packages and owns their source/build provenance, identity/integrity and composition posture.

Deployment Registry registration validates/preserves that output as supply; it does not make the Registry a semantic producer.

Deployment owns desired Set selection and target-state reconciliation. Any Deployment-time composition is mechanical assembly of eligible `MemberContribution` outputs required by the Target representation. An `AssembledConsumptionArtefact` remains atomic at its internal semantic/member-composition boundary.

Observed target content, an older package, a Registry lifecycle state or successful deployment status may be evidence for reconciliation but do not substitute for canonical/Build provenance.

## Package lifecycle versus runtime removal

Registry lifecycle and runtime lifecycle are separate.

- `Deprecated` does not itself remove deployed material.
- `Withdrawn` removes the package from ordinary new/current Registry resolution; any resulting change to desired Set composition is handled by normal Deployment reconciliation.
- runtime removal remains subject to Dependencies, composition posture, Target mechanics and Deployment Policy.

A Deployment-owned assembly of `MemberContribution` outputs may be reassembled without a no-longer-desired member. If removal changes the internal semantic/member composition of an `AssembledConsumptionArtefact`, Deployment requires the corresponding replacement Build output.

## Source and acquisition boundary

A Registry/source locator, trust in that source, package lifecycle, permission to acquire/change a Target and the deployment action itself are separate facts.

Generic acquisition of packages not already available through established Registry/environment mechanics remains outside this release. Missing required deployable supply is reported/blocked rather than silently fetched from an arbitrary location.

## Failure, resumption and atomicity

There is no generic all-or-nothing transaction across heterogeneous Deployment Targets.

- preserve previously verified target state when failure occurs before mutation where possible;
- record each Target independently;
- a multi-target deployment with mixed success is `Partial`;
- a policy-denied/manual action may return `Blocked` with the next action rather than mutating;
- re-running reconciles from observed state and avoids unnecessary redeployment; and
- platform rollback is used only where actually supported.

Release Batch atomicity applies only to visibility of coordinated Registry changes, not to later target mutations.

## Verification

UI presence, an enabled flag, Registry registration, repository publication or filesystem existence alone does not prove runtime availability.

Target-specific verification may include package/member integrity, publication/install acknowledgement, discovery, identity/version visibility, applicable required-presence checks, Migration/cheap metadata visibility, content probes, trigger behaviour and fresh-session pickup where relevant.

Producer-declared surface variation/degradation information informs what behaviour is expected on each surface; verification must not fail a surface merely for functionality explicitly declared irrelevant/unsupported there, but must fail when a required/full-conformance condition is not met.

## Artefact neutrality and manual channels

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other built deployable artefacts use the same Registry/Deployment model when their producer supplies a conforming Deployable Package/output. Their semantic owner does not become the deployment owner.

A manually replaced project Bundle is a valid representation/channel implementation where the platform lacks automation. Later automated sync/install can replace that channel without changing the Registry or desired-composition semantics.

## Boundaries

- Producer/domain owns logical artefact semantics and PackageKind-specific Build/package content.
- `AIDE_Dependencies` owns dependency/required-presence semantics.
- `AIDE_Migration` owns consumer transition semantics.
- `AIDE_Tags` owns tag content/build/query semantics; Deployment consumes Tags for selection where configured.
- Build owns semantic rendering/transformation, source/build provenance, output/package identity/integrity and composition posture.
- AI Deployment owns the Deployment Registry contract/lifecycle, desired Set selection, posture-respecting mechanical assembly, policy-aware target reconciliation/delivery, mismatch reporting and verification.
- Environment/platform configuration owns physical Registry/Target facts, access references and actual policy/authority values.
- Bootstrap owns startup discovery/surfacing, not Registry registration, deployment action or verification.

```yaml
MigrationSummary:
  CurrentVersion: v5
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None

Transition:
  Version: v5
  Posture: None
```

No persisted consumer-state transformation is required to adopt v5.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDeployment_Design_v5, AIDE_Build@v6, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDeployment_Registry_Design_v1, AIDE_DeploymentRegistryTool@v1, AIDE_CapabilityBuild@v1
