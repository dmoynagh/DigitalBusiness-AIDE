# AIDE Dependencies — Standard

> **Identity:** `AIDE_Dependencies@v3`
> **Common name:** Dependencies
> **Version 3** (2026-09-01). Defines position-dependent capability-reference semantics, non-ordering checkpoints, hard exact constraints and local declaration precedence.

---

## Purpose

Declare what an artefact relies on; resolve dependency identity; report presence/version state; and
preserve the last saved, proven conformance checkpoint.

## Storage

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

The governing document methodology supplies the metadata container. This Standard owns the
`Dependencies:` content contract.

## Presence and version grammar

```text
dependency      normal relationship
!dependency     required on relevant use/access
!!dependency    best-effort startup presence check + required thereafter
dependency@vN   last saved/proven conformance checkpoint
dependency@!vN  exact available version vN required
```

Markers compose.

Resolve identity name first, ignoring version; compare version after resolution. Multiple matches
fail visibly.

## Declaration order

Dependency order is significant. Earlier entries have higher **default processing precedence**
when an operation needs deterministic ordering, unless an explicit relationship or governing
operation supplies another order.

This is processing/foundational precedence, not requirement severity. It applies to dependencies of
the artefact being processed and does not sequence independent artefacts or peer Bootstrap
Contributions. A conformance checkpoint by itself creates no processing order.

## Reference positions

Position determines the role of a capability version reference:

| Position | Meaning |
|---|---|
| `Dependencies: X@vN` | this artefact's last saved/proven conformance checkpoint against X |
| `Dependencies: X@!vN` | hard present exact-version constraint |
| `Dependencies: X` | dependency without version tracking |
| `References:` | reader/evidence pointer; no currency or conformance obligation |
| current executable body | operational instruction; versionless by default, specific release only when deliberately required |

A checkpoint is backward-looking saved evidence. It imposes no resolution/execution order and
mutual checkpoints are not an operational dependency cycle. Newer availability alone does not make
a behind-current checkpoint stale or defective.

Canonical production validates current executable capability references separately from dependency
checkpoint advancement.

## Dependency Query

Return at least resolution, requirement level, conformance version, available version, version
relation/gap, exact-version result, and effective declaration order where needed.

Dependencies reports facts. Migration/current operations decide the consequence.

## Conformance checkpoint

A recorded version advances only when the dependent artefact is updated/saved in a state proven
through that version.

- availability alone never advances it;
- `None`/`NotApplicable` migration versions may count as traversed but are persisted only on the
  next artefact save;
- failed/deferred migration does not advance through the unresolved version;
- partial success advances only through the last saved proven version.

## Exact-version constraints

`abc@!v8` requires exactly v8 to be available. If it is unavailable the dependency is unsatisfied
and affected use requiring it is blocked; another version may not silently substitute. The mismatch
is not a saved conformance gap or ordinary Migration trigger. Changing/removing the pin is an
explicit dependent-artefact change that is validated and saved normally.

## Required/startup-required

`!` is checked on relevant use/access and missing identity is surfaced prominently.

`!!` additionally requests a best-effort startup **presence** check through the Core bootstrap
mechanism. It does not imply a general startup Migration scan.

## Dependency Builder

Standards may contribute `AIDE_DependencyBuilder` definitions. Builders own only their generated
Group/Prefix output, preserve meaningful order, are idempotent, and fail visibly when applicable
output cannot be derived correctly. Group keys remain invisible to non-owning consumers.

```yaml
MigrationSummary:
  CurrentVersion: v3
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
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Dependencies_Design_v3
References: AIDE_Migration@v2
