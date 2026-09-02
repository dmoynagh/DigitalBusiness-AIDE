# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v3`
> **Common name:** Deploy
> **Version 3** (2026-08-31). Clarifies mechanical target assembly, Build-output requirements and provenance handling.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v3
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve each Target's effective Deployment Policy/authority together with destination/channel facts.
3. Resolve desired members, canonical/source provenance, package/build identities, platform contributions/authorised assembled Build outputs and applicable required-presence facts.
4. Validate integrity and that any required Deployment-time composition can be performed as deterministic mechanical assembly of the supplied built material.
5. If the Target requires a semantic transformation or assembled Build output that has not been supplied/resolved, report a Build/material blocker; do not manufacture it from canonical source, Design history, an older Bundle/package or observed deployed content.
6. Read/resolve observed target state where possible.
7. Compare desired composition and applicable required presence with observed state.
8. If required material is absent, report a reconciliation mismatch/blocker; do not treat Set omission as removal of the requirement and do not silently expand Set membership.
9. Mechanically assemble the selected built material where the Target representation requires set-level assembly, preserving supplied member semantics and provenance.
10. Determine the minimum target actions needed to reach valid desired state.
11. Apply only target mutations permitted by Deployment Policy; otherwise return the required confirmation/manual/external next action without mutating.
12. Run the Target's verification contract, including required-presence checks where relevant.
13. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent from payload structure, semantically rewrite supplied contributions, or silently choose between conflicting contributions. Observed target content is reconciliation evidence only, not a source for semantic production.

A source/catalog locator is not authority to fetch or install. Generic acquisition of missing packages/material is outside this Tool release unless an established environment mechanism explicitly supplies that operation under resolved trust and Deployment Policy.

## Verify

Run the configured verification contract without intentionally changing desired composition.
Report installed/published state separately from runtime-content availability, applicable required-presence state and active-session pickup where those can differ.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report desired Set composition, configured Targets, effective policy posture where material, resolved source/build provenance where supplied, last observed/verified state, required-presence or missing-Build-output mismatches, failed/unverified Targets and the next reconciliation action. Do not infer canonical/build provenance from deployment status alone.

Where target mutation is not currently permitted, distinguish “action required” from technical deployment failure.

## Failure and idempotency

Re-running the same desired state reconciles from observed state. A matching verified Target needs no semantic redeployment. Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete.

Policy-denied/unconfirmed actions must not be attempted merely because credentials or write access exist.

```yaml
MigrationSummary:
  CurrentVersion: v3
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

No persisted consumer-state transformation is required to adopt v3.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Deployment@v3
References: AIDE_Build@v1, AIDE_Dependencies@v2
