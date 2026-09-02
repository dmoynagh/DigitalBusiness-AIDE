# AIDE Migration — Standard

> **Identity:** `AIDE_Migration@v1`
> **Common name:** Migration
> **Version 1** (2026-08-29). First published transition authoring, fast-check, execution,
> checkpoint, failure, and resumption contract.

---

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
- Process dependencies in their declared order unless a more specific governing order applies.
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

If a dependency uses an exact-version requirement, follow the migration treatment defined by the
applicable governing Standard/document rule. That rule may preserve the pin, move it, relax it, or
require follow-on actions.

If no governing rule determines the treatment, stop and escalate rather than infer.

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

---

**Depends on:** `Capabilities_Migration_Design_v1`, `AIDE_Dependencies@v2`, `AIDE_Scope@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
