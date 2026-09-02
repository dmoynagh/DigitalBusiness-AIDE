# AIDE Migration — Standard

> **Identity:** `AIDE_Migration@v3`
> **Common name:** Migration
> **Version 3** (2026-09-02). Defines the aggregate-operation seam and authoritative-corpus treatment while preserving per-artefact Migration semantics.

---

## Contents

- **Transition contract** — postures, summaries, owner declarations and affected-use/update triggers.
- **Execution integrity** — ordering, saved checkpoints, outcomes, failure state and resumability.
- **Dependency constraints** — exact-version blocks and supported-baseline handling.
- **Aggregate operation seam** — authoritative selection plus Required-Migration and Update behaviour.

## Summary

Migration applies owner-declared version transitions to one dependent artefact at a time. Required
work gates affected reliance; OnUpdate work waits for a qualifying save; None requires no consumer
transformation. Only verified saved state advances dependency conformance checkpoints, and partial
success remains durable and resumable.

`AIDE_UpdateTool` may orchestrate this behaviour over Domains, session Domains, Documentation
Topics, explicit artefacts or criteria-selected sets. It owns aggregate selection and reporting,
but each artefact remains governed by this Standard and `AIDE_MigrationTool`. Required-Migration
selection does not sweep OnUpdate-only artefacts; explicit aggregate Update reconciles Required and
OnUpdate work for every selected authoritative artefact.

## Purpose

Safely move a dependent artefact from its last proven dependency conformance checkpoint toward the
currently available dependency version using owner-declared transitions rather than inferred deltas.

## Transition posture

Every released migratable capability version declares exactly one posture:

```text
Required | OnUpdate | None
```

- `Required` — applicable work must complete before affected use.
- `OnUpdate` — old state remains usable; apply on the next modification/save.
- `None` — no state change is required for existing consumers.

Posture is version-level. Items inside one version do not mix postures.

## MigrationSummary

Expose a compact summary:

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8   # optional
```

Use the summary as a cheap negative/possible-work test. It does not replace detailed transition
history or Scope evaluation.

Where skill headers or equivalent metadata are eagerly loaded/discoverable, platform builds should
surface this summary there and load detailed transition instructions only when the summary indicates
possible work.

## Transition declaration

For each released version:

```yaml
Transition:
  Version: v18
  Posture: Required | OnUpdate | None
  Scope: <optional AIDE_Scope declaration>
  Change: <why existing consumers are affected>
  Items:
    - <ordered transition instruction>
  Success: <how completion is proven>
```

`None` may contain only version and posture.

Transition instructions must be explicit enough to produce the required state and establish
success. They may invoke existing Tools. Do not encode generic platform packaging/invocation
mechanics in the canonical transition.

## Required check

When an artefact is about to be relied upon for relevant use:

1. query its versioned dependencies;
2. compare each checkpoint with `LatestRequiredVersion`;
3. load detailed transition history only where Required work may exist;
4. evaluate Scope/current state; and
5. if applicable Required work remains, migrate before affected use continues.

There is no general Migration startup sweep. `!!` remains the Dependencies startup-presence
posture.

## OnUpdate

When an artefact is modified/saved, reconcile pending migration work through the current available
version.

OnUpdate does not block ordinary use. If Required work causes a save, apply pending applicable
OnUpdate work in that same update where possible.

## Ordering

- Discover relevant pending work before changing the artefact.
- Process dependencies of the artefact being processed in their declared order unless a more specific
  governing order applies. A saved conformance checkpoint creates no ordering by itself; mutual
  conformance checkpoints between artefacts create no cross-artefact migration order.
- Process versions oldest to newest.
- Process items within one version in declared order.
- Re-evaluate applicability before each version.
- Stop on unresolved conflict rather than silently choosing.

## Checkpoint

The dependency conformance version is the last **saved, proven** checkpoint.

- Do not advance it because a newer version merely exists.
- Persist a new checkpoint only when the artefact itself is updated/saved.
- `None` and `NotApplicable` count as traversed for the next saved checkpoint.
- On partial success, persist only through the last successful version.

## Outcomes

`Completed` — applicable work succeeded.

`NotApplicable` — the dependency applies but the transition does not; treat the version as traversed
for the next saved checkpoint.

`Deferred` — applicable work was authoritatively postponed; do not advance through it; maintain a
Migration-owned temporary state entry and surface the consequence.

`Failed` — execution could not complete; discard partial changes from the failed version, preserve
prior successful work/checkpoints, maintain temporary state, and report noisily.

## Failure state

On defer/failure, write/update a compact owner-labelled state entry using the generic document-state
location/rendering supplied by the governing document methodology. Include enough information to
understand the current condition, and where known state what would make the migration succeed.
Remove the Migration-owned entry after a later successful update resolves it.

## Exact-version constraints

`X@!vN` is a hard present dependency constraint owned by `AIDE_Dependencies`, not a saved
conformance checkpoint or ordinary Migration gap. If exact vN is unavailable, affected use or
migration requiring the dependency is blocked and another version may not silently substitute.
Migration reports the dependency block and does not move/relax the pin by inference. Changing the
pin is an explicit dependent-artefact modification.

## Supported baseline

Retain detailed history needed to migrate from the oldest supported conformance version to current.
If `SupportedBaseline` is declared, a consumer older than it is outside the normal migration path
and requires explicit recovery/upgrade handling.

## Failure and safety

- Missing required transition history → fail loudly.
- Dependency version regression → report; do not treat as forward migration.
- Dependency state changes mid-run → stop and resume after state stabilises.
- Concurrent artefact modification → do not overwrite newer work.
- Ambiguous/contradictory transition instruction → stop and identify the owning version.
- Re-running resumes from persisted successful checkpoints and must not duplicate completed work.

## Aggregate operations and authority

`AIDE_UpdateTool` owns aggregate target resolution, authoritative-corpus selection, orchestration
and whole-operation reporting. Supported target forms are one Domain, multiple Domains, current
session Domains, a Documentation Topic, explicit artefacts and criteria-selected sets inside an
authorised boundary.

Mutation is limited to authoritative artefacts within the selected target and work authority.
External-owner/consuming artefacts encountered through reachability or dependency resolution are
reported and skipped unless independently selected through an authoritative target with authority
to modify them. Multi-Domain selection does not imply Domain inheritance or merging.

For aggregate **Required Migration**, select/invoke Apply only where applicable Required work is
outstanding. Do not select an artefact solely for OnUpdate work. If Required work causes a save,
normal per-artefact OnUpdate-through-current behaviour still applies.

For aggregate **Update**, the explicit request is a qualifying update for each selected authoritative
artefact. Invoke per-artefact Update and reconcile applicable Required and OnUpdate work through
current where possible.

The aggregate result never advances dependency checkpoints itself. Per-artefact Migration advances
only through proven saved state and reports Completed, NotApplicable, Deferred or Failed truthfully.
Preserve successful artefacts when another fails and report overall partial completion.

Governed documents participate through their genuine `AIDE_DocumentationMethodology` dependency.
Do not create or require a synthetic universal `AIDE_Doc` dependency solely as a migration hook.

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
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Migration_Design_v3, AIDE_Dependencies@v3, AIDE_Scope@v2
References: AIDE_MigrationTool@v3, AIDE_UpdateTool@v1, AIDE_Domain
