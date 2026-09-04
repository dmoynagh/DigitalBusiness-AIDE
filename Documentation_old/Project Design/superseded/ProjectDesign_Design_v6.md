# Project Design — Design

> **Version 6** (2026-09-02). Defines Design/Brief Summary depth and the Summary-to-Overview escalation rule.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

## Contents

- **Purpose and operating model** — Project Design's boundary, lifecycle flow and principal concepts. §1–§3
- **Design quality and authority** — layered design, decision discipline, current authority and proportionate structure. §4–§7
- **Review, handoff and reconciliation** — independent assessment, WorkPackage handoff and Build return. §8–§10
- **Flexible contribution model** — many-to-many Design contributions, permitted section hosts and cross-Topic work. §11–§12
- **Document orientation** — Design/Brief Summary coverage and when to create or rely on Overview. §13

## Summary

Project Design establishes what substantial work is intended to achieve, why, under which
requirements and constraints, and what current model or approach has been confirmed before
execution. It separates design authority from Build execution: confirmed Design identifies any
undelivered downstream consequences, WorkRegister preserves those obligations, WorkPackage bounds
an executable slice, and the returned Outcome is reconciled by the owning design process.

Design is confirmed knowledge rather than a mandatory one-document-per-output pipeline. A work area
may use zero, one or several reconciled Design documents or semantic sections, and may author the
proper authoritative outcome directly when intermediate prose would only duplicate it. Current
contributions must not conflict materially, and Build must not choose among unresolved designs.

Substantial Design documents normally use a semantic Contents map and a genuine high-level Summary.
The Summary communicates the objective, model, major relationships, key logic and boundaries while
the body retains the detailed authority. If adequate high-level coverage would materially duplicate
or bloat the Design, an Overview should carry the fuller high-level representation. A current
Overview permits a smaller Design Summary but does not remove the Design's minimum self-orientation.

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

The authoritative current model/approach, which may be represented by one or several reconciled Design contributions or directly in another authoritative semantic owner. Every consideration downstream work must honour is present in a current authoritative input.

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
AIDE_ProjectDesign@v6
```

Migration posture is `None`: v6 adds prospective Design/Brief orientation and the Overview
escalation rule without requiring mass rewriting historical Design, Brief or Overview documents.


## §11 — Design contributions and semantic-section hosting

Design is confirmed knowledge, not a mandatory one-document-per-output pipeline. A work area may
use zero, one or several Design documents/sections where the authoritative outcome can be written
directly to its proper owner without duplicative Design prose.

One Design contribution may affect several outputs; one output may aggregate several Design
contributions. Contributions may be whole documents or identified sections. Current contributions
must not conflict materially; reconcile conflict before Build rather than asking Build to choose.

Brief, Purpose, Requirements and Considerations are semantic sections. Their baseline Project
Design meaning remains stable while a domain Standard may permit them in a domain control document
such as Capability Definition. Keep one authoritative instance for each scope and externalise only
when size, lifecycle, retrieval, reuse or complexity warrants it.

## §12 — Cross-Topic reconciliation

Topic ownership identifies the baseline and durable destination. It does not require the work to be
performed in the owning Topic's physical context. A sufficiently sourced and authorised Working
Context may reconcile a coordinated design across Topics. Use Project Handoff only when a genuine
transfer boundary exists under Working Practices.

## §13 — Design, Brief and Overview orientation

Project Design consumes the generic Contents/Summary semantics from Documentation Methodology and
defines their use for its DocTypes.

A substantial **Design** should normally expose:

- Contents — a concise semantic map of significant design information and stable section locations;
  and
- Summary — enough high-level coverage for a reader to understand the objective, overall model or
  approach, principal components/relationships, important logic and boundaries without first
  reading the complete detailed sequence.

Summary depth is proportionate. The body remains the complete authoritative design and carries the
supporting reasoning, precise rules, exceptions and implementation detail. A current related
Overview may reduce the Design Summary to essential objective/model/boundary orientation plus a
clear Overview reference, but someone opening the Design directly must still understand what it is
and how its detail fits together.

If a useful high-level Design representation cannot be expressed proportionately without materially
duplicating or bloating the Design, create an **Overview** rather than continuing to enlarge the
Summary. An Overview may also be created directly on explicit user/work-owner instruction. It is a
purposeful independent document, not only an overflow artefact, and normally does not need its own
Summary because high-level explanation is its primary role.

A substantial **Brief** may use a shorter Summary covering objective/need, scope/boundaries, major
requirements/outcomes and intended result. Small Briefs or Designs whose whole content is already
immediately scannable may omit either section under the value/readability test.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Review@v4, AIDE_WorkPackage@v3
References: ProjectDesign_Decisions_v5, Build_Design_v6
