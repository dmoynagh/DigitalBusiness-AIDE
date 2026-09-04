# Capabilities Migration — Brief

> **Version 3** (2026-09-02). Adds aggregate Required-Migration and Update operations without changing per-artefact transition ownership.

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

- `AIDE_Migration@v3` — the stable authoring, build, checking, execution, and state contract;
- a per-artefact Migration Tool providing Check, Apply, Update, Status/Resume behaviour; and
- `AIDE_UpdateTool@v1` — aggregate target resolution, authoritative-corpus selection,
  orchestration and reporting across Domains, Documentation Topics or selected artefact sets.

Domain-wide Required Migration selects only artefacts with outstanding applicable Required work;
it does not sweep artefacts solely because OnUpdate work exists. An explicitly requested aggregate
Update is the qualifying update operation and reconciles applicable Required and OnUpdate work for
each selected authoritative artefact under normal per-artefact Migration rules.

## Boundaries

Migration does not own:

- dependency identity or version-state resolution — Dependencies;
- applicability language — Scope;
- document placement/rendering for temporary operational state — Documentation Methodology;
- platform-specific skill/plugin/bundle representations — Build-side platform Standards/Tools;
- installation/distribution — Deployment; or
- dependency exact-version satisfaction — Dependencies; an unsatisfied exact pin blocks affected
  use and is not an ordinary Migration version gap. Migration does not silently move or relax pins.

## Success signals

- A consumer can determine cheaply whether Required work may exist before loading migration detail.
- Required work blocks only affected use, not unrelated work or session startup by default.
- OnUpdate work waits safely until modification.
- Transition execution is ordered, resumable, and truthful about partial success.
- The conformance checkpoint always represents the last state actually proven and saved.
- Platform implementations can optimise discovery without changing Migration semantics.
- Aggregate operations never rewrite external-owner/consuming artefacts merely because they are
  reachable from a selected Domain; they report them unless explicitly selected with authority.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v14, Capabilities_Migration_Design_v3
References: AIDE_Dependencies@v3, AIDE_Scope@v2, AIDE_Domain, AIDE_UpdateTool@v1
