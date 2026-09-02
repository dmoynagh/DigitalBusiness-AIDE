# Project Design Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder version 1** (2026-08-31). First independently versioned Binder; assembles the Foundation-consolidated current masters.

## Binder manifest

- `ProjectDesign_Index_v2.md` — sha256 `40078a5dd499`
- `ProjectDesign_Design_v2.md` — sha256 `294eafa9ea05`
- `ProjectDesign_Decisions_v2.md` — sha256 `2b617d7aef6e`
- `AIDE_ProjectDesign_Standard_v2.md` — sha256 `c06d2ceef674`

---

<!-- BEGIN SOURCE: ProjectDesign_Index_v2.md -->
# Project Design — Index

> **Version 2** (2026-08-31). Adopts Core Index, corrects the physical Project Design path and
> registers the WorkRegister consequence/reconciliation contract.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

`{scope: "AIDE/Project Design", type: DocumentationTopic}`

## Contents

- **Project Design** — generic methodology for defining substantial work and reconciling committed
  Design with downstream delivery.  
  `{standard: AIDE_ProjectDesign@v2}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v2 | Index | Current |
| `ProjectDesign_Design` | v2 | Design | Current |
| `ProjectDesign_Decisions` | v2 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v2 | Standard | Current; identity `AIDE_ProjectDesign@v2` |

### Container

Current physical/master folder:

```text
AIDE/Project Design/
```

This folder has always used `Project Design`; earlier references to `AIDE/Design Project/` were
incorrect current documentation/configuration.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: ProjectDesign_Design_v2, AIDE_ProjectDesign@v2, AIDE_WorkPackage@v2
<!-- END SOURCE: ProjectDesign_Index_v2.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Design_v2.md -->
# Project Design — Design

> **Version 2** (2026-08-31). Adds explicit downstream-consequence capture through WorkRegister
> and WorkRegister-to-WorkPackage delivery reconciliation.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## §1 — Purpose and boundary

Project Design defines **what is to be achieved, why, under what requirements/constraints, and what
approach/outcome has been determined** before execution is handed to Build.

It is generic across software, documentation, capability development, business/process work,
creative production and other substantial work.

Project Design owns the reusable design method. It does not execute the work and does not own the
physical container in which the topic happens to be discussed.

## §2 — Core model

```text
Intent / need
    ↓
Brief / requirements / constraints
    ↓
Decisions + current model/approach
    ↓
Design (committed current state)
    ↓
identify downstream consequences
    ↓
fully delivered now? ── yes → reconciled
    │
    no
    ↓
WorkRegister
    ↓
select manageable work chunk(s)
    ↓
WorkPackage(s)
    ↓
Build
    ↓
Outcome
    ↓
reconcile WorkRegister
    ├── complete → remove item
    └── partial/blocked/design issue → retain/update or revise Design
```

## §3 — Principal concepts

### Intent / Brief

States the objective, need, scope, success conditions and important non-goals. Ceremony is
proportionate to stakes.

### Requirements and constraints

States what the outcome must satisfy. Requirements remain distinct from implementation choices.

### Decisions

Records material design choices, credible rejected alternatives, reasoning and consequences.
Decisions informs future Design; downstream delivery consumes the current Design/defined outcome.

### Design

The authoritative current model/approach. It contains every consideration downstream work must
honour.

### WorkRegister consequence

A confirmed Design change is a **commitment** to the current model. If that commitment requires
code, build, document, deployment-input or another produced outcome to change and the consequence
is not fully delivered in the same pass, the owning top-level topic records it in WorkRegister.

The consequence must be described in sufficient detail to determine later whether the production
outcome actually caught up with the Design.

This is not a generic backlog rule; it is the reconciliation seam between committed Design and
undelivered reality.

### WorkPackage

WorkPackage is a bounded execution contract built from some or all relevant WorkRegister
obligations (or directly defined work where no register item is needed).

### Review

Independent Review applies under `AIDE_Review` where required/configured/materially useful. Review
does not take design ownership.

## §4 — Layered design control

For substantial design, establish a compact two-layer checkpoint before deep mechanics:

1. **Intent/system** — purpose, premises, ownership/boundaries, inputs/outputs, surrounding
   relationships.
2. **Model** — principal concepts, responsibilities, relationships, lifecycle/flow, major rules.

If this cannot be made clear, reassess the model before adding machinery.

## §5 — Domain-owned workflows

A domain/top-level work concern owns the workflow that composes Project Design, Build, Review and
other AIDE services. Project Design supplies the generic design behaviour only.

## §6 — Consequence capture rule

After each substantive confirmed Design change:

1. identify downstream outcomes affected;
2. identify the concrete changes required in each outcome;
3. if all are delivered/verified in the same pass, no WorkRegister debt remains;
4. otherwise create/update the owning top-level topic's WorkRegister with the undelivered
   consequence(s).

A WorkRegister item should identify, proportionately:

- source Design/decision;
- committed change;
- required implementation/output changes;
- target outcome/location;
- current state; and
- later WorkPackage/result/remaining information.

Do not leave a confirmed Design change with an implicit “implementation later” assumption.

## §7 — Handoff to Build

When execution is required, create/authorise a WorkPackage conforming to `AIDE_WorkPackage@v2`.

If sourced from WorkRegister, identify the covered register item IDs and the portion of each
obligation included in this manageable work chunk.

Build should not need Decisions history to reconstruct the intended result.

## §8 — Return and reconciliation

Build returns an Outcome stating actual work, produced/changed state, validation, deviations,
unresolved work and design feedback.

Project Design/director then:

- confirms acceptance where the defined result is satisfied;
- reconciles each mapped WorkRegister item;
- removes a fully delivered WorkRegister item;
- records returned result/remaining work on any item still outstanding;
- resolves design-shaping feedback and issues revised/further work; or
- explicitly accepts a residual difference/risk within authority.

Execution evidence is input to reconciliation; it does not silently rewrite Design.

## §9 — Simplicity and escalation

Routine reversible implementation detail belongs to Build authority. Changes to objective, major
scope, acceptance, ownership, architecture or policy return to Project Design.

When implementation accumulates compensating exceptions, test whether a simpler model/boundary/
requirement removes the complexity first.

## §10 — Intended output

```text
AIDE_ProjectDesign@v2
```

Migration posture is `None`: the release strengthens future consequence tracking/handoff but does
not require mass rewriting historical Design/WorkPackages.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Review@v1, AIDE_WorkPackage@v2
References: ProjectDesign_Decisions_v2, Build_Design_v4
<!-- END SOURCE: ProjectDesign_Design_v2.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Decisions_v2.md -->
# Project Design — Decisions

> **Version 2** (2026-08-31). Preserves the initial Project Design decisions and records the
> WorkRegister consequence/reconciliation contract plus the physical naming correction.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## D1 — Use Project Design rather than Design or Solution Design

**Decision.** The top-level methodology is named **Project Design**. `Design` remains a valid
artefact/stage within it.

**Reason.** Bare `Design` is overloaded while `Solution Design` is unnecessarily software-shaped.

## D2 — Project Design is domain-independent

**Decision.** Project Design defines reusable behaviour for determining substantial work, not a
software-development lifecycle or product-specific process.

## D3 — Domain production workflows remain domain-owned

**Decision.** Do not introduce a generic top-level Workflow owner for all production scenarios. The
substantive domain/top-level concern composes Project Design, Build and other AIDE services.

## D4 — Project Design and Build form an iterative loop

**Decision.** The generic handoff is Design Outcome → WorkPackage → Build → Outcome, with the return
reconciled by the design/work owner.

## D5 — Layered overviews are a design-control mechanism

**Decision.** For substantial design, establish compact intent/system and model layers before deep
mechanics.

## D6 — Confirmed Design creates an explicit delivery obligation where outcomes must change

**Trigger / problem.** Once Design is changed, the committed current position can diverge from code,
built artefacts or other production outcomes. Without an explicit record, later readers cannot tell
which design changes have actually been implemented.

**Alternatives considered.** Put implementation status in Design; rely on WorkPackage history;
leave consequences to memory/current chat.

**Decision.** After a substantive Design change, identify every material downstream consequence.
If a consequence is not fully delivered in the same pass, record it in the owning top-level topic's
WorkRegister with enough detail to verify eventual delivery.

**Reason.** Design should remain the clean current model while WorkRegister truthfully represents
the gap between commitment and delivered reality.

## D7 — WorkRegister is not merely a backlog

**Decision.** Treat WorkRegister as the live undelivered-design-consequence ledger. A row records the
committed change, required downstream change(s), target outcome, delivery state, WorkPackage mapping,
returned result when still open and remaining work.

**Consequence.** Completed rows are removed after reconciliation; durable reasoning/evidence remains
with Design/Decisions/Outcome where it belongs.

## D8 — WorkPackages select manageable portions of WorkRegister obligations

**Decision.** One WorkPackage may group all/part of several WorkRegister items, and one large item
may require several WorkPackages.

**Reason.** The register should represent obligations at the useful design-consequence level while
Build execution can be chunked for safe/manageable delivery.

## D9 — Build return is reconciled against the source obligations

**Decision.** On Outcome return, the director reconciles mapped WorkRegister items. Complete items
are removed; partial/blocked items retain returned evidence and remaining work; design-level
feedback returns to Project Design.

**Boundary.** Build does not silently close WorkRegister state owned by the top-level topic.

## D10 — Correct the Project Design container path

**Decision.** The current physical/master folder is `AIDE/Project Design/`. Earlier
`AIDE/Design Project/` references were factual documentation/configuration errors, not a historical
rename.

## D11 — Issue Project Design v2

**Decision.** Publish the strengthened contract as `AIDE_ProjectDesign@v2`, migration posture
`None`.

**Reason.** The release changes future design/delivery behaviour but does not require rewriting
historical WorkPackages or Design documents.

---
Dependencies: !AIDE_DocumentationMethodology@v21, ProjectDesign_Design_v2
References: AIDE_WorkPackage@v2, Build_Decisions_v4
<!-- END SOURCE: ProjectDesign_Decisions_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_ProjectDesign_Standard_v2.md -->
# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v2`
> **Common name:** Project Design
> **Version 2** (2026-08-31). Adds explicit downstream-consequence capture and WorkRegister-to-WorkPackage reconciliation while preserving the established Project Design model.
>
> **Default weight:** Expectation

---

## Purpose

Define substantial work coherently before execution: establish intent and requirements, determine the current model/approach, review proportionately, and hand execution to Build through a complete WorkPackage where needed.

## Apply proportionately

Use the amount of structure justified by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Establish the work

For work that needs design, establish enough of the following to remove material ambiguity:

- objective/need and intended outcome;
- authorised scope and non-goals;
- requirements and constraints;
- material assumptions/uncertainties;
- decisions and credible alternatives where consequential;
- the current design/model/approach; and
- defined deliverables or acceptance signals.

Do not allow detailed implementation to become the place where unresolved design is silently decided.

## Use a layered checkpoint for substantial design

Before descending into extensive mechanics, maintain a compact view of:

1. **Intent/system:** purpose, premises, ownership/boundaries, inputs/outputs and surrounding relationships.
2. **Model:** principal concepts, responsibilities, relationships, lifecycle/flow and major rules.

If this view is difficult to make clear, reassess the model before adding mechanisms.

## Record authoritative state

Design records the current confirmed position. Decisions record material reasoning and rejected alternatives. Downstream outcomes consume the confirmed Design/defined outcome, not Decisions history.

Confirmed material must be written according to the governing Documentation Methodology rather than left only in conversation.

## Track undelivered Design consequences

Whenever the confirmed Design changes, identify the downstream outcomes that must change for
delivered reality to remain aligned.

For each consequence:

```text
fully delivered in the same pass → no standing obligation remains
not fully delivered               → record in the owning top-level topic's WorkRegister
```

The WorkRegister entry must state the source Design change and required downstream code/build/
document/production changes in enough detail that later delivery can be reconciled. WorkRegister is
not a list of undecided ideas; it records already-confirmed work/consequences that remain owed.

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v2`.

A WorkPackage may be created directly from defined work or select manageable portions of one or
more WorkRegister obligations. Where it is sourced from WorkRegister, identify the source item IDs
and the portion of each obligation covered.

The package must make the required result, authority, work-specific inputs and acceptance clear.
WorkRegister references are traceability, not a substitute for a self-contained execution contract.
Do not embed generic execution-platform knowledge already supplied by the Build environment.

## Handle Build return

On Build Outcome:

- reconcile returned evidence against each mapped WorkRegister obligation where applicable;
- remove a WorkRegister item only when its full confirmed consequence is actually delivered;
- retain partial/blocked items with the returned result and remaining work;
- close/record completion when acceptance and the committed outcome are satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

Build may resolve implementation detail within authority; it does not silently change objectives,
major scope, acceptance or architecture and does not silently close the owning WorkRegister.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

---
Dependencies: !AIDE_DocumentationMethodology@v21, ProjectDesign_Design_v2, AIDE_Review@v1
References: AIDE_WorkPackage@v2
<!-- END SOURCE: AIDE_ProjectDesign_Standard_v2.md -->
