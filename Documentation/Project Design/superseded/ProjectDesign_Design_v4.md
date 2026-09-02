# Project Design — Design

> **Version 4** (2026-09-01). Pre-Round-2 preflight correction: updates the active Build
> handoff to `AIDE_WorkPackage@v3` after coordinated Review B R1 remediation; all Project Design
> Review B R1 substantive semantics remain unchanged.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

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

Documentation Methodology owns the general WorkRegister type/admission semantics: WorkRegister holds
confirmed work owed by the owning top-level topic and not yet fully delivered.

Project Design owns one mandatory producer rule into that general type. A confirmed Design change is
a **commitment** to the current model. If that commitment requires code, build, document,
deployment-input or another produced outcome to change and the consequence is not fully delivered in
the same pass, the owning top-level topic records the consequence in WorkRegister.

The consequence must be described in sufficient detail to determine later whether the production
outcome actually caught up with the Design.

Project Design does not define WorkRegister as exclusively Design-generated work and does not make it
a generic backlog. Other confirmed work may be valid there under its governing owner/type contract;
unresolved ideas, possible work and unconfirmed attention remain outside WorkRegister.

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
3. if all are delivered/verified in the same pass, no Design-generated WorkRegister obligation
   remains; and
4. otherwise create/update the owning top-level topic's WorkRegister with the undelivered
   consequence(s).

A Design-generated WorkRegister item should identify, proportionately:

- source Design/decision;
- committed change;
- required implementation/output changes;
- target outcome/location;
- current state; and
- later WorkPackage/result/remaining information.

Do not leave a confirmed Design change with an implicit “implementation later” assumption.

This rule is a Project Design producer guarantee. It does not redefine or limit other WorkRegister
admission permitted by Documentation Methodology.

## §7 — Handoff to Build

When execution is required, create/authorise a WorkPackage conforming to `AIDE_WorkPackage@v3`.

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

If a mapped Outcome is received and reconciliation cannot be completed in the same uninterrupted
step, before leaving that context preserve a compact `Returned — reconciliation pending` state on
the owning WorkRegister item(s) with a pointer to the Outcome. Keep detailed execution evidence in
the Outcome rather than duplicating it into the register. Reconciliation is completed by Project
Design/the directing owner when work resumes; Build does not close the obligation.

Execution evidence is input to reconciliation; it does not silently rewrite Design.

## §9 — Simplicity and escalation

Routine reversible implementation detail belongs to Build authority. Changes to objective, major
scope, acceptance, ownership, architecture or policy return to Project Design.

When implementation accumulates compensating exceptions, test whether a simpler model/boundary/
requirement removes the complexity first.

## §10 — Intended output

```text
AIDE_ProjectDesign@v4
```

Migration posture is `None`: v4 is a preflight correction to the current WorkPackage handoff target;
it preserves the v3 ownership/admission, split-mapping and return-state semantics and does not require
mass rewriting historical Design, WorkRegister, WorkPackage or Outcome records.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Review@v1, AIDE_WorkPackage@v2
References: ProjectDesign_Decisions_v3, Build_Design_v4