# AI Deployment Registry — Design

> **Version 2** (2026-09-02). Reconciles Registry events and Release Batches to exact Deployment Set Release resolution.
>
> Created: 2026-09-02 | Last modified: 2026-09-02

## §1 — Purpose

Provide one stable source of validated built supply that AI Deployment can resolve without reopening
producer Design or treating an ordinary filesystem/repository copy as deployment state.

The Registry sits between successful producer Build and Deployment Set resolution:

```text
validated Deployable Package
        ↓
AIDE_DeploymentRegistryTool
        ↓
Deployment Registry
        ↓
Deployment Set resolution / reconciliation
```

The Registry is an interface contract, not a required storage technology. A conforming Registry may
be implemented by a folder, Git repository, package store, service or another mechanism that can
preserve the required identities, bytes, metadata and lifecycle state.

## §2 — Deployable Package

A **Deployable Package** is the generic Registry unit: a validated Build-owned package accepted as
available supply for later Deployment.

`Capability Package` is the first specialised Package kind. Future producer domains may define
other Package kinds without changing generic Registry semantics provided they satisfy this contract.

Keep these identities distinct:

- **Logical Package Identity** — stable producer/package identity used to group successive builds;
- **PackageKind** — producer-defined package contract kind, for example `CapabilityPackage`; and
- **PackageId** — unique identity of one concrete validated Build package instance.

A forced/repeated Build may therefore create another `PackageId` for the same Logical Package
Identity without implying a new semantic capability release.

## §3 — Package acceptance contract

Before a package becomes Registry supply, resolve enough producer-owned information to identify and
use the concrete Build result without semantic inference.

Every accepted package shall expose directly or through its applicable package contract:

```text
PackageKind
Logical Package Identity
PackageId
integrity evidence
source/canonical provenance
Build/production contract provenance sufficient for the package kind
one or more deployment-facing built outputs/members where applicable
Build-owned CompositionPosture for each output where required
payload/file/area identity sufficient to resolve those outputs
Build validation evidence sufficient to establish that the submitted package is the validated result
```

Preserve package-kind-owned metadata needed downstream, including dependency, Migration, Bootstrap,
activation/registration or other owner-defined information where applicable. Generic Registry does
not reinterpret those semantics.

A package/target contract may additionally provide:

- package-level Tags;
- Build-target/member-level Tags;
- surface support, conformance, variation or degradation results;
- successor/replacement information owned by the producer; and
- namespaced extension metadata for specialised Deployment-time Standards/Tools.

Unknown optional extension metadata is preserved. A package that declares an extension mandatory
for correct Deployment is not eligible for an operation that cannot resolve the required handler.

The Registry does not require one universal physical package/manifest format. It requires the
semantic envelope above to be resolvable and unambiguous.

## §4 — Immutability and Current Package

A successfully registered package instance is immutable under its `PackageId`.

- Re-registering the same `PackageId` with the same verified payload/integrity is idempotent.
- Re-registering the same `PackageId` with different bytes, integrity or producer metadata is a
  conflict and fails visibly.
- A later Build of the same Logical Package Identity uses a new `PackageId`.

The Registry separately records a mutable **Current Package** relation for each Logical Package
Identity. `Current` means the package instance normally selected by floating/current resolution; it
is an authority relation, not a synonym for newest timestamp.

Package bytes and producer-owned immutable metadata do not change when Registry lifecycle/current
state changes.

## §5 — Registry-owned lifecycle state

Registry lifecycle state is maintained separately from package payload.

### Available

Normal Registry supply. An Available package may participate in ordinary resolution subject to the
Deployment Set, Build-target compatibility, Dependencies and other governing rules.

### Deprecated

The package remains available but is discouraged. Record a concise reason and successor/replacement
where known.

Deprecation alone does not uninstall or invalidate an already deployed package. Floating/current
resolution should prefer a suitable non-deprecated current replacement where one exists and surface
a warning when a deprecated package remains selected.

### Withdrawn

The package is retained as historical/evidential state but is not eligible for ordinary new/current
resolution. If it was Current, withdrawal must either move Current to a valid replacement in the
same Registry transaction or leave the Logical Package Identity without an ordinary Current package.

Withdrawal may cause a later Deployment Set resolution to change and therefore may lead to removal
through normal Deployment reconciliation. It does not itself mutate runtime targets.

A withdrawn package may be used for explicit authorised recovery/forensic purposes only under the
applicable policy; it is not silently reintroduced by floating resolution.

### Purge

Physical deletion is repository/retention maintenance, not normal package lifecycle. v1 defines no
automatic purge. Historical package instances are retained by default; a future retention contract
may add safe purge after demonstrated need.

## §6 — Tags

Deployable Packages and individual built target/member outputs may carry `AIDE_Tags` values.

For Deployment selection, the effective tag set of a target/member is the union of:

```text
Package Tags + target/member Tags
```

Use the existing `AIDE_Tags` exact Boolean query semantics where tag selection is used. Registry
publication shall not knowingly publish stale generated Tags when those Tags are part of governed
package state.

Tags are classification/selection data. They do not replace:

- semantic Dependencies or required presence;
- Scope;
- Build-target compatibility;
- Migration posture; or
- Deployment Policy.

## §7 — Release Batch

A **Release Batch** groups Registry publications that must become visible to downstream automatic
resolution together.

The minimum v1 model is:

```text
Open
  ↓ Release
Released

Open
  ↓ Abandon
Abandoned
```

While a Batch is Open:

- packages may be validated and staged;
- staged instances do not replace ordinary Current Package state; and
- batch-triggered Deployment automation does not run from each staged package.

`Release` validates the batch as a coherent Registry transaction, including any declared expected
package set, conflicts, integrity and lifecycle actions. Only after successful validation are the
staged Current/lifecycle changes made visible together.

Release therefore provides an **atomic Registry visibility boundary**. It does not claim atomic
publication or rollback across heterogeneous runtime Deployment Targets.

An expected package list is optional and acts as a release validation condition. Explicit Release,
not inferred package count alone, is the authoritative signal that the producer/director considers
the batch complete.

## §8 — Registry events and Deployment triggers

Registry state changes may emit semantic events such as:

```text
PackageCurrentChanged
PackageDeprecated
PackageWithdrawn
ReleaseBatchReleased
```

A **Deployment Trigger** may map relevant Registry events to re-evaluation of one or more Deployment
Set Definitions. Trigger configuration is separate from Registry storage and may be automatic or
manual.

A Registry event means “desired supply may have changed”, not “redeploy unconditionally”. The
receiving Deployment process resolves the affected Set and compares its exact selected PackageIds,
built outputs and final Deployment Output content with the current Desired Release. If unchanged,
an automatic Registry-triggered invocation is a true no-op: no new Set release and no delivery
retry. An explicit/manual Reconcile may still retry or re-verify incomplete Targets of the existing
Desired Release.

There is no generic downstream Deployment Package. Registry supply is a Deployable Package; the
resolved set-level consumables are Deployment Outputs under an immutable Deployment Set Release.

## §9 — Registry publication boundary

Registry registration is an AI-Deployment-owned post-Build action.

Generic Build may nominate `AIDE_DeploymentRegistryTool` after successful output validation. The
Registry Tool owns acceptance/registration semantics; generic `AIDE_PublishBuildOutputTool` remains
for ordinary filesystem/repository publication and does not claim Registry state.

A Registry action result is separate from the immutable producer package. A Registry publication
failure does not erase a successfully validated Build package and may be resumed/retried against the
same PackageId where safe.

## §10 — Package metadata versus Registry metadata

Keep producer/package and Registry state distinct.

**Immutable producer/package state** includes, as applicable:

```text
PackageKind
Logical Package Identity
PackageId
integrity
source/build provenance
built member/target outputs
CompositionPosture
package/member Tags
dependency/migration/extension information
Build validation evidence
producer-declared limitations/degradation information
```

**Registry-owned mutable state** includes:

```text
Current Package relation
Available / Deprecated / Withdrawn
reason/successor where applicable
Release Batch staging/release state
registration receipt/evidence
retention/purge state where later implemented
```

Changing Registry state must not rewrite an immutable package merely to keep the two views in one
file.

## §11 — Physical implementation and authority

Environment/platform configuration resolves the Registry locator, access mechanism, credentials,
retention implementation and transaction mechanics.

Technical write access does not by itself grant authority to Register, Release, Deprecate or
Withdraw. The Registry Tool must operate under the applicable work/Deployment authority.

The Registry is trusted built supply only to the extent established by its configured source,
producer provenance, integrity and governing policy. Registering a package does not itself grant
permission to deploy it to a runtime Target.

## §12 — Failure and idempotency

- invalid package contract/integrity → reject; do not create Current state;
- duplicate PackageId with identical verified content → idempotent success;
- duplicate PackageId with conflicting content → fail visibly;
- failed Register outside a Batch → preserve prior Current state;
- failed Batch Release → preserve prior visible Registry state and keep/return staged state for
  correction or abandonment;
- Deprecate/Withdraw repeated with the same intended state → idempotent;
- missing required package-kind extension handler → block the affected downstream operation rather
  than dropping the extension;
- Registry action failure never converts a valid producer Build into a failed Build result.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v8, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDeployment_Design_v6, AIDeployment_SetRelease_Design_v1, AIDE_CapabilityBuild@v3, AIDE_PublishBuildOutputTool@v1
