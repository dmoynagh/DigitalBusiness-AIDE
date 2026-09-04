# AIDE Migration — Tool

> **Identity:** `AIDE_MigrationTool@v3`
> **Common name:** Migration
> **Version 3** (2026-09-02). Executes one-artefact Migration under optional aggregate Update orchestration.

---

## Contents

- **Purpose, actions and inputs** — the per-artefact execution contract.
- **Check, Apply, Update, Resume and Status** — logical behaviours and checkpoint handling.
- **Integrity, reporting and aggregate seam** — failure safety, resumability and caller interaction.

## Summary

This Tool checks and executes `AIDE_Migration` for one target artefact, preserves only proven saved
progress, resumes without replaying completed work and reports every blocker or partial result.
Aggregate corpus selection is owned by `AIDE_UpdateTool`, which may invoke this Tool but cannot
alter its per-artefact transition or checkpoint semantics.

## Purpose

Check, apply, update, resume, and report migration of dependent artefacts under
`AIDE_Migration@v3`, preserving truthful saved conformance checkpoints and durable partial
progress.

## Logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v3
  CommonName: Migration
  PrimaryInvocation: migration
  LogicalActions: [Check, Apply, Update, Resume, Status]
```

Platform Build may render these actions as slash commands, skills, UI actions, or conversational
intents without changing their semantics.

## Trigger and inputs

Run when affected use requires a Required check, an artefact modification qualifies for OnUpdate,
a migration action is requested, unresolved Migration state is resumed, or another governing
Standard/Tool invokes Migration.

Resolve one target artefact, dependencies and Dependency Query facts, applicable `MigrationSummary`,
detailed transitions when needed, current operation/authority, exact-version constraint result, and
existing Migration-owned state.

Infer safe low-cost facts; ask once for genuinely missing information; escalate substantive
ambiguity or authority conflict.

## Check

1. Query relevant versioned dependencies.
2. For use, compare checkpoints to `LatestRequiredVersion`.
3. For update, compare checkpoints to current/OnUpdate summary state.
4. Load detailed history only where the summary indicates possible work.
5. Evaluate supported baseline and Scope.
6. Return pending Required/OnUpdate work, traversable None/NotApplicable state, defer/failure state,
   and blocking conditions.
7. Make no artefact change.

## Apply

1. Resolve all relevant pending work before changing state.
2. Process dependencies by declared processing precedence unless specifically overridden.
3. Process versions oldest to newest and items in declared order.
4. Re-evaluate applicability before each version.
5. Apply items and verify each version's `Success` condition.
6. Preserve durable success stepwise.
7. When Required causes a save, continue through pending applicable OnUpdate/None versions to
   current where possible.
8. Save only proven state and advance checkpoints only through successfully traversed saved state.
9. Remove Migration-owned temporary state when resolved.

## Update

Perform the intended artefact modification together with all applicable Required and OnUpdate work
through current. Do not stop merely because Required work exists: the operation is already a
qualifying save event.

If work cannot complete, preserve only the last successful state/checkpoint and surface the
unresolved condition.

## Resume

Read persisted checkpoints/state, re-resolve current dependency facts, confirm earlier durable
success, and continue from the first unresolved version without replaying completed work.

## Status

Report artefact, dependency, checkpoint, available/current version, summary relation, pending
Required/OnUpdate work, supported-baseline result, clear/deferred/failed state, and next action.

## Failure and integrity

- Failed version: discard that version's partial changes; keep prior successful work/checkpoint;
  write/update compact Migration-owned state and report noisily.
- Deferred: preserve authorised deferral and consequence; do not advance through it.
- Concurrent artefact change: do not overwrite newer work.
- Moving dependency facts: stop and resume against stable state.
- Missing/ambiguous transition: stop and identify the unresolved owner decision rather than infer it.
- Unsatisfied exact-version constraint: block affected use, report the required exact version, and do
  not substitute/move the pin through Migration.

Check/Status are read-only and idempotent. Apply/Update/Resume are resumable and must not duplicate
already completed version work.

## Reporting

Summary reporting states what was checked/applied, resulting checkpoints, and anything still
blocking or needing attention. Failure, defer, unsupported baseline, exact-version constraint failure, and
conflict always surface regardless of narration preference.

## Aggregate caller seam

`AIDE_UpdateTool` may invoke this Tool once per artefact after resolving an authorised aggregate
selection. Do not expand that resolved target, mutate reachable external-owner artefacts or report
aggregate completion. Return the target's selected transitions, saved checkpoints, skips, blockers,
failure/defer state and next action so the caller can compose a truthful whole-operation report.

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
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, AIDE_Dependencies@v3, Capabilities_Migration_Tool_Design_v3
References: AIDE_Scope@v2, AIDE_UpdateTool@v1
