# Capabilities Migration Tool — Design

> **Version 1** (2026-08-29). First issuance. Specifies the platform-independent Tool that checks,
> applies, resumes, and reports Migration under `AIDE_Migration@v1`.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## §1 — Output and boundary

This Design produces one canonical **Migration Tool**. It orchestrates `AIDE_Migration@v1` against
Dependency Query results and the artefact in hand.

The Tool does not author transition intent, define dependency identity/version semantics, define
Scope, decide document-state placement, or implement platform-specific command/skill/plugin
rendering.

## §2 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v1
  CommonName: Migration
  PrimaryInvocation: migration
  LogicalActions:
    - Check
    - Apply
    - Update
    - Resume
    - Status
```

Platform implementations may render these as `/migrations-check`, `/migrations-apply`,
`/update-doc`, subcommands, skills, UI actions, or conversational intents.

## §3 — Trigger

The Tool runs when:

- relevant use requires a Required Migration check;
- an artefact is being modified and OnUpdate reconciliation is due;
- the user/AI explicitly asks to check/apply/update/resume migration;
- an active Migration failure/defer state is resumed; or
- another governing Standard/Tool invokes Migration.

## §4 — Inputs

Required/resolved inputs include:

- target artefact(s);
- current dependency declarations;
- Dependency Query facts;
- applicable `MigrationSummary` and detailed transition history when needed;
- current operation (`Use`, `Update`, explicit `Check/Apply/Resume`);
- current work authority/scope;
- applicable governing rules for exact-version constraints; and
- existing Migration-owned temporary state where present.

Infer safe low-cost facts; ask once for genuinely missing information; escalate substantive
ambiguity or authority conflicts.

## §5 — Check

1. Query relevant versioned dependencies.
2. For use, compare checkpoint to `LatestRequiredVersion`.
3. For update, compare checkpoint to current/OnUpdate summary state.
4. Load detailed history only where the summary indicates possible work.
5. Evaluate supported baseline and Scope.
6. Return pending Required, OnUpdate, None/NotApplicable, deferred/failed state, and any blocking
   condition.
7. Make no artefact change.

## §6 — Apply

1. Resolve all relevant pending migration work.
2. Order dependencies by declared dependency precedence unless specifically overridden.
3. Process versions oldest to newest.
4. Before each version, re-evaluate applicability/current state.
5. Apply ordered items and verify `Success`.
6. Preserve each successfully completed version as durable progress when saving is appropriate.
7. On Required-triggered update, continue through pending applicable OnUpdate/None versions to the
   current available version where possible.
8. Save only proven successful state and update dependency checkpoints accordingly.
9. Remove resolved Migration-owned temporary state.

## §7 — Update

`Update` is the explicit/idempotent document reconciliation action (commonly rendered
`/update-doc`).

It performs the intended document modification/update together with all pending applicable
Required and OnUpdate transition work through current. It does **not** stop merely because a
Required transition exists; the update is already the qualifying change/save event.

If migration cannot complete, preserve only the last successful state/checkpoint and report the
unresolved condition.

## §8 — Resume

1. Read persisted checkpoints and Migration-owned state.
2. Re-resolve current dependency/version facts.
3. Confirm that prior successful work remains present.
4. Resume from the first unresolved version; do not replay completed versions.
5. Update/replace/remove Migration-owned temporary state according to the new result.

## §9 — Status

Report at least:

- artefact;
- dependency;
- stored checkpoint;
- available/current version;
- summary relation;
- pending Required/OnUpdate work;
- supported-baseline result;
- Migration state: clear/deferred/failed;
- next action needed.

## §10 — Failure handling

### Version failure

Discard partial changes from the failed version, preserve prior successful work, persist the last
successful checkpoint when the artefact is saved, write/update compact Migration-owned state, and
report noisily with a suggested resolution where known.

### Deferred

Record authorised deferral and consequence in Migration-owned state; do not advance through the
deferred version.

### Concurrent change

Do not overwrite newer artefact state. Stop and report/reconcile.

### Moving dependency state

If resolved dependency/version facts change during execution, stop and resume against a stable
state.

### Missing/ambiguous transition

Stop and identify the owning capability/version; do not infer.

## §11 — Idempotency

Check and Status are read-only/idempotent. Update/Apply/Resume are resumable and must not duplicate
already completed version work. Re-running against an unchanged current artefact produces no
substantive migration change.

## §12 — Reporting

Summary reporting states what was checked/applied, the resulting checkpoint(s), and anything still
blocking or needing attention. Failures, deferrals, unsupported baselines, exact-version ambiguity,
and conflict always surface regardless of verbosity preference.

---

**Depends on:** `AIDE_Migration@v1`, `Capabilities_Migration_Design_v1`, `AIDE_Dependencies@v2`.

**References:** `Capabilities_Tools_Design_v2`.

**Methodology:** v17
