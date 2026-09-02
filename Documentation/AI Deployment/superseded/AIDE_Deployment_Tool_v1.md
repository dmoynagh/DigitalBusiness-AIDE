# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v1`
> **Common name:** Deploy
> **Version 1** (2026-08-30). Canonical Tool for target-state deployment reconciliation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v1
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve desired members, package/build identities and platform contributions.
3. Validate integrity and deterministic composability.
4. Read/resolve observed target state where possible.
5. Determine the minimum target actions needed to reach desired state.
6. Apply target actions through the available distribution channel.
7. Run the Target's verification contract.
8. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent from payload structure and do not silently choose between conflicting
contributions.

## Verify

Run the configured verification contract without intentionally changing desired composition.
Report installed/published state separately from runtime-content availability and active-session
pickup where those can differ.

## Status

Report desired Set composition, configured Targets, last observed/verified state, mismatches,
failed/unverified Targets and the next reconciliation action.

## Failure and idempotency

Re-running the same desired state reconciles from observed state. A matching verified Target needs
no semantic redeployment. Failure on one Target does not falsely mark other successful Targets
failed or the whole deployment Complete.

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
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Deployment@v1
References: AIDE_Build@v1
