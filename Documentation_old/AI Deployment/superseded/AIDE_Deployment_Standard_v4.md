# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v4`
> **Common name:** AI Deployment
> **Version 4** (2026-08-31). Aligns Deployment reconciliation with the Build v3 output
> contract and explicit Build-owned composition posture.
>
> **Default weight:** Requirement

## Purpose

Make built deployable material available in intended AI runtime surfaces, reconcile desired composition and applicable required presence with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes:

- current Build output(s) with Build-declared `CompositionPosture: MemberContribution | AssembledConsumptionArtefact`;
- authoritative/canonical source identity/version provenance and concrete Build-output/package identity and integrity evidence;
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
3. validate authoritative/canonical source provenance, Build-output/package identity, integrity evidence and Build-declared composition posture;
4. where the Target requires set-level assembly, mechanically assemble eligible `MemberContribution` outputs deterministically without semantically re-rendering them;
5. treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary; if that composition must change, require the corresponding replacement Build output;
6. fail visibly on missing posture-compatible Build output or incompatible ownership/path/identity/namespace/posture claims;
7. compare desired composition and required presence with observed deployed state;
8. surface any missing required material as a reconciliation mismatch/blocker rather than treating it as optional;
9. determine the necessary install/update/replace/remove actions;
10. apply only actions permitted by the effective Deployment Policy;
11. verify the resulting target/runtime state; and
12. persist/report Deployment Result and observed Deployment State.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

Mechanical full reassembly versus incremental patching is target implementation detail only within the Build-declared composition posture. `MemberContribution` outputs may be mechanically reassembled or patched where the Target contract permits. Deployment must not decompose or alter the internal semantic/member composition of an `AssembledConsumptionArtefact`; a different internal composition requires another Build output. If a required semantic transformation or posture-compatible output is absent, Deployment blocks/returns that need upstream rather than producing it itself.

## Production and provenance boundary

Build is upstream of Deployment. It renders/transforms current authoritative/canonical semantics into concrete Build outputs and supplies source identity/version provenance, Build-output/package identity and integrity evidence, and one `CompositionPosture`: `MemberContribution` or `AssembledConsumptionArtefact`.

Deployment owns desired Set composition and target-state reconciliation. It consumes that posture rather than deriving another one. Any Deployment-time composition is mechanical assembly of eligible `MemberContribution` outputs required by the Target representation. An `AssembledConsumptionArtefact` remains atomic at its internal semantic/member-composition boundary. Deployment preserves supplied semantics and source/build provenance in either case.

Observed deployed state, an older Bundle/package, runtime verification or successful deployment status may be used as reconciliation evidence but do not become semantic production authority or substitute for canonical/build provenance.

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

Removal is the consequence of desired-state reconciliation. A Deployment-owned assembly of `MemberContribution` outputs may be reassembled without the removed member. If removal changes the internal semantic/member composition of an `AssembledConsumptionArtefact`, Deployment requires the corresponding replacement Build output. An independently installed member may be uninstalled. Removal is still subject to the effective Deployment Policy.

## Artefact neutrality and manual channels

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other deployable artefacts use the same Deployment model when Build supplies the required target-compatible Build output and composition posture. Their semantic owner does not become the deployment owner, and Deployment does not collapse their semantic roles or infer missing Bootstrap meaning during assembly.

A manually replaced project Bundle is a valid representation/channel implementation where the platform lacks automation. Later automated sync/install can replace that channel without changing Deployment Set semantics.

## Boundaries

- Producer/domain owns logical artefact semantics and its declared requirements.
- `AIDE_Dependencies` owns dependency/required-presence semantics.
- Build owns semantic rendering/transformation into concrete Build outputs and owns their source provenance, Build-output/package identity/integrity and `CompositionPosture`.
- AI Deployment owns desired Set selection, posture-respecting mechanical target assembly of eligible `MemberContribution` outputs, atomic handling of `AssembledConsumptionArtefact` outputs, policy-aware delivery/reconciliation, mismatch reporting and verification.
- Environment/platform configuration owns physical target facts, access references and actual target-change policy/authority values.
- Bootstrap owns startup discovery/surfacing, not deployment action or verification.

```yaml
MigrationSummary:
  CurrentVersion: v4
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

```yaml
Transition:
  Version: v3
  Posture: None
```

```yaml
Transition:
  Version: v4
  Posture: None
```

No persisted consumer-state transformation is required to adopt v4.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v4, AIDE_Dependencies@v2
References: AIDE_Build@v3
