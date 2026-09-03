# AIDE Deployment Registry — Tool

> **Identity:** `AIDE_DeploymentRegistryTool@v1`
> **Common name:** Deployment Registry
> **Version 1** (2026-09-02). First AI-Deployment-owned package registration, lifecycle and Release Batch Tool.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentRegistryTool@v1
  CommonName: Deployment Registry
  PrimaryInvocation: deployment-registry
  LogicalActions: [Register, BeginBatch, ReleaseBatch, AbandonBatch, Deprecate, Withdraw, Status]
```

## Trigger and inputs

Use for publication/registration of a successfully validated Deployable Package into a configured
Deployment Registry or for Registry-owned package lifecycle/Release Batch actions.

Resolve as applicable:

- Registry identity/locator and authority;
- validated Deployable Package source, `PackageKind`, Logical Package Identity and `PackageId`;
- integrity and Build validation/provenance evidence;
- optional Release Batch identity;
- lifecycle reason/successor where Deprecate/Withdraw is requested; and
- expected package identities/validation conditions where a Batch declares them.

Do not infer a Registry destination merely from an ordinary Build output path.

## Register

1. Resolve the configured Registry and authority to change it.
2. Validate the package against `AIDE_Deployment@v5` and its PackageKind contract.
3. Verify PackageId/integrity and sufficient Build/source provenance.
4. Preserve owner-specific dependency, Migration, Tags, degradation/limitation and extension
   metadata without redefining their semantics.
5. If the same PackageId already exists with identical verified package state, return idempotent
   `Registered`/existing receipt.
6. If the same PackageId exists with conflicting state, fail visibly.
7. If a Release Batch is supplied, stage the package/lifecycle-current change under that open Batch
   without changing ordinary Current visibility.
8. Otherwise store the immutable package, update Current Package for the Logical Package Identity
   as authorised, emit the applicable Registry event and return the registration receipt/state.

Register does not deploy the package to a runtime Target.

## BeginBatch

1. Resolve Registry and authority.
2. Create one unique open Release Batch identity.
3. Record optional expected Logical Package Identities and other explicit release validation
   conditions.
4. Return the Batch identity/state.

Do not infer that an arbitrary series of registrations forms one Batch merely because they are close
in time.

## ReleaseBatch

1. Resolve the open Batch and all staged changes.
2. Validate all staged PackageIds/integrity and package contracts again where needed.
3. Validate any declared expected-package conditions and lifecycle/current-pointer transitions.
4. Fail without changing visible Current Registry state if the Batch is incomplete, conflicting or
   otherwise invalid.
5. Make the staged Registry Current/lifecycle changes visible as one Registry transaction using the
   strongest atomicity the Registry implementation supports; if exact atomic replacement cannot be
   guaranteed, preserve prior state on failure and report the limitation.
6. Mark the Batch Released.
7. Emit one `ReleaseBatchReleased` event plus any required compact changed-package facts for
   downstream Deployment Trigger evaluation.

ReleaseBatch creates no cross-runtime deployment transaction guarantee.

## AbandonBatch

Mark an Open Batch Abandoned and remove/ignore its staged Registry visibility changes. Do not delete
or invalidate the producer Build outputs merely because the Registry batch is abandoned.

## Deprecate

1. Resolve the exact package instance and Registry authority.
2. Mark it `Deprecated` in Registry-owned metadata.
3. Record concise reason and successor/replacement where established.
4. Preserve the immutable package payload and existing exact historical references.
5. Emit a Registry event so configured Deployment Triggers may re-evaluate affected Sets.

Deprecation does not itself remove material from runtime targets.

## Withdraw

1. Resolve the exact package instance and Registry authority.
2. Mark it `Withdrawn` and remove it from ordinary new/current resolution eligibility.
3. If it is Current, move Current to an authorised valid replacement in the same Registry
   transaction or leave the Logical Package Identity without an ordinary Current package.
4. Preserve the immutable package for historical/evidential or explicitly authorised recovery use.
5. Emit `PackageWithdrawn`/current-change state for Deployment Trigger evaluation.

Withdrawal does not directly uninstall runtime material; resulting removal is owned by normal
Deployment reconciliation.

## Status

Report, as requested:

- Registry identity and reachable/authority state where material;
- Logical Package Identity → Current Package relation;
- exact PackageId, PackageKind, integrity and lifecycle state;
- package/member Tags where supplied;
- open/released/abandoned Release Batch state;
- deprecation/withdrawal reason/successor;
- registration receipt/provenance; and
- unresolved validation/conflict conditions.

Do not claim target/runtime Deployment state from Registry state.

## Failure and idempotency

- invalid/unvalidated package → reject;
- identical re-registration → idempotent;
- PackageId collision with different content → fail visibly;
- failed Register/Release → preserve prior visible Registry state;
- repeated same-state Deprecate/Withdraw → idempotent;
- unavailable destination authority → `Blocked`, not technical `Failed` merely because credentials
  are absent/unusable;
- physical purge is not a v1 action.

A successful producer Build remains successful when Registry registration fails; report Registry
post-Build state separately and preserve the validated package for safe retry.

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
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v5, AIDE_Build@v6, AIDE_Tags@v2
References: AIDeployment_Registry_Design_v1, AIDE_PublishBuildOutputTool@v1
