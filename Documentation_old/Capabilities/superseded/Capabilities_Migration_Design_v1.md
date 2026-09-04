# Capabilities Migration — Design

> **Version 1** (2026-08-29). First issuance. Establishes version-level Required/OnUpdate/None
> transitions, fast migration summaries, use/update triggers, ordered multi-dependency execution,
> truthful partial progress, temporary state, supported baselines, and exact-version handling.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## §1 — Purpose and ownership

Migration answers:

> Given an artefact last proven conformant against dependency version X and a newer version Y now
> available, what declared transition work applies, when must it occur, and how far can the saved
> conformance checkpoint safely advance?

Migration owns transition classification, declaration structure, summary/index semantics,
version-range resolution, ordering, execution posture, progress/failure/defer state, and the
logical Migration Tool actions.

The changed capability owner authors the actual transition intent. Dependencies supplies identity,
conformance checkpoint, available version, version relation, and exact-version facts. Scope supplies
applicability. Documentation Methodology supplies generic document state placement/rendering.

---

## §2 — Core model

```text
Dependent artefact
  dependency conformance checkpoint = vX
        +
Available dependency = vY
        ↓
Dependency Query
        ↓
MigrationSummary fast check
        ↓ when work may exist
supported transition history vX+1..vY
        ↓
Scope/applicability
        ↓
Required / OnUpdate / None
        ↓
ordered execution
        ↓
save successful state
        ↓
advance persisted checkpoint
```

Migration never infers transitions by diffing old and new capability text.

---

## §3 — Version-level transition posture

Each released capability version has exactly one posture for existing consumers:

- `Required` — applicable transition work must complete before affected use can continue.
- `OnUpdate` — old state remains usable; applicable work occurs on the next modification/save.
- `None` — no state change is required for existing consumers.

Posture belongs to the release version. Multiple migration items may exist within the release but
all share that posture.

A release with no transition effect positively declares `None`; absence is not used to imply no
transition.

---

## §4 — Transition declaration

Canonical shape:

```yaml
Transition:
  Version: v18
  Posture: Required | OnUpdate | None
  Scope: <optional AIDE_Scope declaration>
  Change: <why existing consumers are affected>
  Items:
    - <ordered transition instruction>
    - <ordered transition instruction>
  Success: <how successful completion is established>
```

`None` requires only version and posture.

A transition is written to produce the required new state, not to encode generic platform
mechanics. It must be sufficiently explicit for an AI to apply safely and determine success.
Where ambiguity or missing prerequisites prevent a safe result, execution stops rather than
inventing a substantive decision.

A transition may invoke an existing Tool where that Tool is the safest deterministic implementation
of part of the change. The transition remains responsible for its outcome and success condition.

---

## §5 — MigrationSummary fast path

Every versioned migratable capability exposes a compact summary:

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8   # optional
```

The summary is an index, not migration evidence. It allows the normal case to avoid loading
transition detail.

### Use fast path

If the dependent checkpoint is at or beyond `LatestRequiredVersion`, no Required transition detail
needs to be loaded for ordinary use.

If it is older, load the relevant detailed history and evaluate applicability.

### Update fast path

When the artefact is modified, compare its checkpoint with the current version and
`LatestOnUpdateVersion`; load transition detail only where pending Required/OnUpdate work may exist.

### Platform optimisation

Where a platform eagerly loads/discovers skill headers or equivalent metadata, Build should surface
`MigrationSummary` there. Detailed transition instructions remain on-demand. Other platforms use
the strongest equivalent cheap-discovery representation.

This is a recommended implementation methodology, not a change to the platform-independent
Migration semantics.

---

## §6 — Required trigger

Required Migration is checked when an artefact is about to be **relied upon for relevant use**.
Merely existing, being listed, or being read as historical/background material does not by itself
force migration.

Execution is:

```text
relevant use
  ↓
Dependency Query
  ↓
checkpoint < LatestRequiredVersion?
  no → continue
  yes → inspect detailed transitions
  ↓
applicable Required transition outstanding?
  no → continue
  yes → migrate before affected use continues
```

There is no blanket Migration startup scan. `!!` remains Dependencies' startup presence check.
A future capability may explicitly justify startup migration checking, but it is not the default.

---

## §7 — OnUpdate trigger

OnUpdate is triggered when an artefact is edited, revised, regenerated, prepared for changed output,
or otherwise modified/saved.

It does not block ordinary use.

When a Required migration causes an update/save, that save is also the next qualifying update for
pending OnUpdate work. Migration therefore applies all applicable pending transition work through
the current available version as part of the same update where possible.

---

## §8 — Conformance checkpoint behaviour

The dependency checkpoint records the **last saved state proven conformant through that dependency
version**.

Rules:

- Never advance merely because a newer dependency version exists.
- Persist a new checkpoint only when the artefact itself is updated/saved.
- A `None` version or a transition found `NotApplicable` is successfully traversed for conformance
  purposes, but does not force a save merely to refresh metadata.
- When the artefact is next saved, the checkpoint may advance through all successfully traversed
  versions.
- If migration succeeds only through an intermediate version, persist that last successful
  checkpoint and resume later from there.

---

## §9 — Multi-dependency migration ordering

Before changing the artefact, Migration discovers the relevant pending migration work across its
versioned dependencies.

Default order follows the dependency declaration order defined by `AIDE_Dependencies`: earlier
dependencies have higher default processing precedence. A more specific explicit dependency or
governing operation may override that order.

Within one dependency, versions execute oldest to newest. Items inside a version execute in their
declared order.

Applicability is re-evaluated immediately before each version is applied because earlier successful
migrations may legitimately change current state.

If two migrations conflict and no governing rule resolves the conflict, stop rather than silently
choosing an execution result.

---

## §10 — Outcomes

A transition/version evaluation has these relevant outcomes:

### Completed

Applicable work completed and its success condition passed. The version is traversed.

### NotApplicable

The dependency applies to the artefact, but Scope/current state establishes that the transition does
not. The version is treated as successfully traversed and may be included in the next saved
checkpoint.

### Deferred

The transition applies but an authorised decision postpones it. The checkpoint does not advance
through the deferred version. Migration writes/updates its temporary operational state entry and
surfaces the consequence. Required affected use remains blocked unless the governing authority has
explicitly accepted an exception for that use.

### Failed

Execution was attempted but could not complete. Partial changes from the failed version are not
saved. Successful earlier versions remain durable. Migration writes/updates temporary operational
state and reports noisily.

---

## §11 — Partial success and temporary state

Migration is stepwise durable rather than globally all-or-nothing.

If migration succeeds through v10 and fails at v11:

- preserve the successful state through v10;
- save the dependent checkpoint at v10;
- do not save partial v11 changes;
- create/update a compact Migration-owned temporary state entry;
- state why it failed and, where known, what would make it succeed; and
- resume later from v10.

Migration owns the state entry's semantics and lifecycle. Documentation Methodology owns the generic
location and rendering for temporary document state. The expected generic human-facing shape is
compact and owner-labelled, for example:

```text
Migration failure [AIDE_Migration]
v11 failed while targeting v12: required source metadata is unavailable.
```

The Migration entry is removed when a later successful update resolves the condition.

---

## §12 — Exact-version constraints

Dependencies reports exact-version constraints such as `abc@!v8` and whether they are satisfied.
Migration still performs its transition role, but it does not invent what the pin means for that
dependent artefact.

Applicable governing Standards/document rules define the migration treatment, for example:

- migrate only up to the explicit version;
- migrate to current and make the new current version explicit;
- migrate to current and relax the declaration to normal conformance tracking; or
- run migration and then perform other owner-defined actions.

If no applicable governing rule resolves the treatment, Migration stops and escalates rather than
guessing.

---

## §13 — Supported migration baseline and history retention

The canonical capability retains transition history sufficient to migrate from the oldest supported
conformance version to the current release.

`SupportedBaseline` is optional. If omitted, all retained historical transition versions are
supported starting points.

Moving the supported baseline forward is a deliberate capability release decision. A consumer
older than the supported baseline receives an `UnsupportedBaseline` result and requires an explicit
recovery/upgrade procedure; Migration does not silently skip missing history.

Old transition detail may be removed from the normal runtime artefact only after it falls below the
supported baseline and the release still provides a clear unsupported-baseline path.

---

## §14 — Edge and failure conditions

- **Missing transition history:** stop noisily; never infer the missing delta.
- **Available dependency older than checkpoint:** report version regression/downgrade state;
  forward Migration does not resolve it.
- **Dependency disappears or changes during execution:** stop against the moving target, preserve
  completed work, and resume after factual dependency state is stable.
- **Concurrent artefact change:** do not overwrite newer work. Stop before saving conflicting
  migration output and record/report the unresolved state.
- **Ambiguous migration instruction:** stop and identify the owning capability/version.
- **Repeated run:** resume safely from persisted checkpoints and owner state; do not reapply
  successfully completed versions.

Caching a successful check inside one session is an optional platform optimisation. It is invalidated
when the artefact, dependency/version state, or explicit refresh changes.

---

## §15 — Outputs and external seams

This Design produces:

- `AIDE_Migration@v1`; and
- `Capabilities_Migration_Tool_Design_v1`.

Migration consumes:

- `AIDE_Dependencies` for dependency/version facts and default dependency order;
- `AIDE_Scope` for applicability;
- governing capability Standards for transition intent and exact-version treatment;
- Documentation Methodology for generic temporary document-state placement/rendering; and
- Build-side platform knowledge for summary/detail representation.

Deployment distributes built transition material but does not own its semantics.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Dependencies_Design_v2`.

**References:** `Capabilities_Migration_Brief_v1`, `AIDE_Dependencies@v2`, `AIDE_Scope@v1`,
`Capabilities_DocMethReviewItems_v3`.

**Methodology:** v17
