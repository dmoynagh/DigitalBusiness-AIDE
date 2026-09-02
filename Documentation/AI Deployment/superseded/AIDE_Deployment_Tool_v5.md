# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v5`
> **Common name:** Deploy
> **Version 5** (2026-09-02). Resolves deployable supply through the Deployment Registry while retaining v4 posture-aware reconciliation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v5
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve the configured Deployment Registry and the exact eligible Deployable Package/member supply required by the Set.
3. Resolve each Target's effective Deployment Policy/authority together with destination/channel facts.
4. Resolve exact PackageId/member identities, integrity, authoritative/canonical source/build provenance, Build-declared `CompositionPosture`, package/member Tags where selection uses them, required package-kind extensions, and applicable required-presence facts.
5. Reject ordinary selection of Withdrawn package instances; surface Deprecated selected supply and its successor/replacement state where known.
6. Validate that each built output is usable under its declared posture for the required Target operation and that required extension handlers are available.
7. If a required semantic transformation/posture-compatible output has not been supplied in eligible Registry material, report a Build/material blocker; do not manufacture it from canonical source, Design history, older package, Registry metadata or observed deployed content.
8. Read/resolve observed target state where possible.
9. Compare desired composition and applicable required presence with observed state.
10. If required material is absent, report a reconciliation mismatch/blocker; do not treat Set omission as removal of the requirement and do not silently expand Set membership.
11. Mechanically assemble eligible `MemberContribution` outputs where the Target representation requires set-level assembly, preserving supplied semantics/provenance. Treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary.
12. If desired reconciliation requires changing the internal semantic/member composition of an `AssembledConsumptionArtefact`, require the corresponding replacement Build output rather than decomposing/rebuilding it.
13. Determine the minimum target actions needed to reach valid desired state.
14. Apply only target mutations permitted by Deployment Policy; otherwise return the required confirmation/manual/external next action without mutating.
15. Run the Target verification contract, using producer-declared surface variation/degradation information to determine the expected applicable behaviour and including required-presence checks where relevant.
16. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent, package kind semantics or composition posture from payload structure. Registry/deployed state is reconciliation evidence only, not a source for semantic production.

A source/Registry locator is not authority to acquire/install. Generic acquisition of missing packages outside established Registry/environment mechanics remains outside this Tool release.

## Verify

Run the configured verification contract without intentionally changing desired composition.

Report Registry/package identity and lifecycle separately from destination publication/install state, runtime-content availability, applicable required-presence state, declared degradation/variation and active-session pickup where those can differ.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report, as applicable:

- desired Deployment Set composition and configured Targets;
- resolved Registry and exact PackageIds/member identities;
- package lifecycle (`Available | Deprecated | Withdrawn`) and successor state where material;
- effective policy posture;
- source/build provenance, integrity and composition posture;
- package/member Tags used for selection;
- last observed/verified target state;
- required-presence, missing-package, required-extension or posture-incompatible mismatches;
- declared surface degradation/variation relevant to verification;
- failed/unverified Targets; and
- next reconciliation action.

Do not infer canonical/build provenance or composition posture from deployment status alone.

## Failure and idempotency

Re-running the same concrete desired state reconciles from observed state. A matching verified Target needs no semantic redeployment.

A Registry event/trigger that resolves to the same concrete desired package/member set is a no-op for target mutation.

Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete. Policy-denied/unconfirmed actions must not be attempted merely because credentials/write access exist.

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
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v5, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDE_DeploymentRegistryTool@v1, AIDE_Build@v6
