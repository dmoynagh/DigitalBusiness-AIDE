# Capabilities Migration — Brief

> **Version 1** (2026-08-29). First issuance. Defines the purpose, outcomes, and boundaries of the
> Migration component against the established Dependencies conformance-checkpoint model.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## Purpose

Migration owns the reusable transition model by which an artefact that was last proven conformant
against one dependency version is safely brought forward when a newer version is available.

Migration exists so transition work is **declared by the owner of the changed capability rather
than inferred by comparing old and new artefacts**. It applies only the deltas that the owner has
explicitly stated are required for existing consumers.

## Required model

Every released capability version has one transition posture for existing consumers:

- **Required** — applicable existing artefacts must complete the transition before affected use.
- **OnUpdate** — existing artefacts remain usable; the transition is applied the next time the
  artefact is modified/saved.
- **None** — no state change is required for existing consumers.

Posture is version-level. A version does not mix Required and OnUpdate migration items.

Dependencies supplies the last proven conformance checkpoint and current available version.
Migration resolves the intervening version range and determines what transition work applies.

## Required behaviour

- Required Migration is checked when the dependent artefact is relied upon for relevant use.
- OnUpdate work is checked/applied when the artefact is modified or prepared for changed output.
- If Required work causes an update/save, pending applicable OnUpdate work is applied in that same
  update and the artefact is normally brought to the current available version.
- Persisted conformance checkpoints change only when the artefact itself is updated/saved.
- A transition that is positively evaluated as not applicable counts as traversed when the next
  saved checkpoint is written.
- Migration preserves completed progress, never records a failed step as complete, and remains
  resumable from the last successful checkpoint.

## Transition production

Transition declarations live with the canonical Standard or Tool version that caused them. The
canonical capability retains the supported transition history needed to migrate from its supported
baseline to the current release.

Migration publishes a compact `MigrationSummary` for cheap discovery. Detailed transition history
is loaded only when the summary shows there may be relevant work.

## Outputs

Migration produces:

- `AIDE_Migration@v1` — the stable authoring, build, checking, execution, and state contract; and
- a Migration Tool specification providing logical Check, Apply, Update, Status/Resume behaviour.

## Boundaries

Migration does not own:

- dependency identity or version-state resolution — Dependencies;
- applicability language — Scope;
- document placement/rendering for temporary operational state — Documentation Methodology;
- platform-specific skill/plugin/bundle representations — Build-side platform Standards/Tools;
- installation/distribution — Deployment; or
- semantic decisions about exact-version constraints where the governing dependent Standard must
  define how the constraint should be treated during migration.

## Success signals

- A consumer can determine cheaply whether Required work may exist before loading migration detail.
- Required work blocks only affected use, not unrelated work or session startup by default.
- OnUpdate work waits safely until modification.
- Transition execution is ordered, resumable, and truthful about partial success.
- The conformance checkpoint always represents the last state actually proven and saved.
- Platform implementations can optimise discovery without changing Migration semantics.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Dependencies_Design_v2`.

**References:** `AIDE_Dependencies@v2`, `AIDE_Scope@v1`.

**Methodology:** v17
