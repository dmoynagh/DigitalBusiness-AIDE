# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v2`
> **Common name:** Deploy
> **Version 2** (2026-08-31). Adds required-presence mismatch handling and policy-gated target mutation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v2
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve each Target's effective Deployment Policy/authority together with destination/channel facts.
3. Resolve desired members, package/build identities, platform contributions and applicable required-presence facts.
4. Validate integrity and deterministic composability.
5. Read/resolve observed target state where possible.
6. Compare desired composition and applicable required presence with observed state.
7. If required material is absent, report a reconciliation mismatch/blocker; do not treat Set omission as removal of the requirement and do not silently expand Set membership.
8. Determine the minimum target actions needed to reach valid desired state.
9. Apply only target mutations permitted by Deployment Policy; otherwise return the required confirmation/manual/external next action without mutating.
10. Run the Target's verification contract, including required-presence checks where relevant.
11. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent from payload structure and do not silently choose between conflicting contributions.

A source/catalog locator is not authority to fetch or install. Generic acquisition of missing packages/material is outside this Tool release unless an established environment mechanism explicitly supplies that operation under resolved trust and Deployment Policy.

## Verify

Run the configured verification contract without intentionally changing desired composition.
Report installed/published state separately from runtime-content availability, applicable required-presence state and active-session pickup where those can differ.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report desired Set composition, configured Targets, effective policy posture where material, last observed/verified state, required-presence mismatches, failed/unverified Targets and the next reconciliation action.

Where target mutation is not currently permitted, distinguish “action required” from technical deployment failure.

## Failure and idempotency

Re-running the same desired state reconciles from observed state. A matching verified Target needs no semantic redeployment. Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete.

Policy-denied/unconfirmed actions must not be attempted merely because credentials or write access exist.

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
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Deployment@v2
References: AIDE_Build@v1, AIDE_Dependencies@v2
