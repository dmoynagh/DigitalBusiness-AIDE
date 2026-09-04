# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v6`
> **Common name:** Deploy
> **Version 6** (2026-09-02). Resolves immutable Set releases and executes layered Delivery Action/Target reconciliation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v6
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set Definition, its current Desired Release and selected/all configured Targets.
2. Resolve the configured Deployment Registry and exact eligible Current Deployable Package/member supply required by the Set selector.
3. Resolve exact PackageId/Build Target/member identities, integrity, Definition/Profile and source/Build provenance, Build-declared `CompositionPosture`, effective Tags, reach/applicability/conformance/degradation, required extensions and applicable required-presence facts.
5. Reject ordinary selection of Withdrawn package instances; surface Deprecated selected supply and its successor/replacement state where known.
6. Validate that each built output is usable under its declared posture for the required Target operation and that required extension handlers are available.
7. If a required semantic transformation/posture-compatible output has not been supplied in eligible Registry material, report a Build/material blocker; do not manufacture it from canonical source, Design history, older package, Registry metadata or observed deployed content.
8. Resolve every required Deployment Output Definition and mechanically assemble candidate Outputs
   from eligible `MemberContribution`s, treating `AssembledConsumptionArtefact`s as atomic.
9. Stamp candidate Outputs with Set release/output identity and resolution digest, then validate all
   required Outputs together before issuing a release.
10. Compare exact provenance and final Output content with Desired Release. If changed and valid,
    assign/freeze the next `<Set>@vN`; if invalid, retain the last Desired Release. An automatic
    Registry invocation with unchanged resolution returns no release/delivery action.
11. For explicit/manual invocation, continue for Targets that are failed, blocked, mismatched or
    unverified even when the Desired Release is unchanged.
12. Read/resolve observed publication, platform-installed/attached and runtime state where possible.
13. Compare Desired Release and applicable required presence with observed Target state. Do not
    silently expand Set membership to hide a missing requirement.
14. Determine the minimum configured Delivery Actions needed and apply only policy-permitted target
    mutations; otherwise return the required manual/confirmation/external next action.
15. Verify Output, publication, platform resolution and runtime layers applicable to the Target,
    including the intrinsic release marker and behaviour probe where required.
16. Record desired/publication/platform/runtime releases, verification status/assurance and
    mismatches in per-Target Deployment State.
17. Return one Deployment Result with target action/state and overall `Complete | Partial | Blocked | Failed`.

Do not infer producer intent, package kind semantics or composition posture from payload structure. Registry/deployed state is reconciliation evidence only, not a source for semantic production.

A source/Registry locator is not authority to acquire/install. Generic acquisition of missing packages outside established Registry/environment mechanics remains outside this Tool release.

## Verify

Run the configured verification contract without intentionally changing desired composition.

Report Registry/package identity and lifecycle separately from Desired Release, publication,
installed/attached platform state, runtime-observed release/content, applicable required-presence,
declared degradation/variation and active-session pickup. Record `Enforced | Advisory` assurance.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report, as applicable:

- Deployment Set Definition revision, Desired Release and configured Targets;
- exact immutable Set release members, Output identities/integrity and resolution digest;
- resolved Registry and exact PackageIds/member identities;
- package lifecycle (`Available | Deprecated | Withdrawn`) and successor state where material;
- effective policy posture;
- source/build provenance, integrity and composition posture;
- package/member Tags used for selection;
- last observed publication, installed/attached platform and runtime target state;
- verification status, assurance, evidence and evidence time;
- required-presence, missing-package, required-extension or posture-incompatible mismatches;
- declared surface degradation/variation relevant to verification;
- failed/unverified Targets; and
- next reconciliation action.

Do not infer canonical/build provenance or composition posture from deployment status alone.

## Failure and idempotency

Re-running the same concrete desired state reconciles from observed state. A matching verified Target needs no semantic redeployment.

An automatic Registry event/trigger that resolves to the same exact Set release is a no-op for
release/delivery. An explicit Reconcile may retry/re-verify incomplete Targets of that release.

Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete. Policy-denied/unconfirmed actions must not be attempted merely because credentials/write access exist.

```yaml
MigrationSummary:
  CurrentVersion: v6
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

Transition:
  Version: v6
  Posture: None
```

No persisted consumer-state transformation is required to adopt v6.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v6, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDeployment_SetRelease_Design_v1, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v1, AIDE_DeploymentRegistryTool@v1, AIDE_Build@v8
