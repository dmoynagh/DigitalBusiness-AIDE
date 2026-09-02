# Project Design Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.

Physical project/master folder: `AIDE/Design Project/`. Canonical topic name: **Project Design**.

## Binder manifest

- `ProjectDesign_Index_v1.md` — sha256 `d49a2d6c64c5`
- `ProjectDesign_Design_v1.md` — sha256 `2c7d19fbab17`
- `ProjectDesign_Decisions_v1.md` — sha256 `13b7a286cdca`
- `AIDE_ProjectDesign_Standard_v1.md` — sha256 `f6bdcb561326`

---

<!-- BEGIN SOURCE: ProjectDesign_Index_v1.md -->
# Project Design — Index

> **Version 1** (2026-08-30). Registers the initial Project Design corpus and canonical Standard.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic:** Project Design  
**Project container / master folder:** `AIDE/Design Project/`  
**Purpose:** Generic methodology for defining substantial work before execution.

## Topic declarations

| Name | Parent | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v1 | Index | Current |
| `ProjectDesign_Design` | v1 | Design | Current |
| `ProjectDesign_Decisions` | v1 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v1 | Standard | Current; identity `AIDE_ProjectDesign@v1` |

## Relationships

- Build consumes defined work through `AIDE_WorkPackage`.
- Domain-owned production workflows compose Project Design and Build.
- Documentation Methodology is a dedicated project/container because of its size and lifecycle, while remaining design-methodology material conceptually.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Build_Design_v1
<!-- END SOURCE: ProjectDesign_Index_v1.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Design_v1.md -->
# Project Design — Design

> **Version 1** (2026-08-30). Establishes Project Design as AIDE's generic methodology for defining substantial work before execution, independent of project domain or AI product.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## §1 — Purpose and boundary

Project Design defines **what is to be achieved, why, under what requirements and constraints, and what approach/outcome has been determined** before execution is handed to Build.

It is generic across software, documentation, capability development, business/process work, creative production, and other substantial projects.

Project Design owns the reusable design method. It does not own a domain's production workflow and does not execute the resulting work.

## §2 — Core model

```text
Intent / need
    ↓
Brief / requirements / constraints
    ↓
Decisions and model/approach
    ↓
Design Outcome
    ↓
WorkPackage where execution is required
    ↓
Build
    ↓
Build Outcome
    ↓
confirm completion OR resolve returned design issue
```

The loop may repeat. A Build Outcome can close the work or return evidence/questions that require Project Design to revise the defined outcome and issue further work.

## §3 — Principal concepts

### Intent and Brief

States the objective, need, scope, success conditions and important non-goals. The amount of ceremony is proportionate to the stakes; not every task requires a separate Brief document.

### Requirements and constraints

States what the outcome must satisfy. Requirements may be project-specific or consumed from applicable Standards. They remain distinct from implementation choices.

### Decisions

Records material design choices, credible rejected alternatives, reasoning and consequences. Decisions inform the current Design; downstream execution consumes the Design/defined outcome rather than reconstructing decisions history.

### Design

The authoritative current model/approach: what is now determined. It must contain every consideration that downstream work needs to honour.

### Design Outcome

The defined deliverable, contract or state that execution is intended to produce. It may be a canonical Standard/Tool, software behaviour, document set, asset specification, implementation contract, or another domain-defined outcome.

### Review

Independent Review is applied under `AIDE_Review` where required, configured, or materially valuable. Review informs the Lead; it does not take ownership of the design.

## §4 — Layered design control

For substantial design, the preferred primary checkpoint is a short two-layer overview before detailed specification.

**Layer 1 — Intent / system view**

- purpose and intended outcome;
- governing premises;
- ownership and explicit non-ownership;
- principal inputs/outputs; and
- relationship to surrounding architecture.

**Layer 2 — Model**

- principal concepts/entities;
- responsibilities and relationships;
- major lifecycle/flow; and
- important rules and distinctions.

Detailed schemas, metadata, mechanics and wording should expand a model already clear at these two layers. If the design cannot be explained simply at this level, first test whether the model is unclear or unnecessarily complicated.

## §5 — Domain-owned workflows

A production workflow belongs to the domain whose work it orchestrates.

A domain workflow may compose Project Design, Build, Review, capabilities and other AIDE services in any sequence the domain requires. It does not redefine their generic semantics.

Examples include a code-development workflow, capability-production workflow, documentation-production workflow, or branding-production workflow.

## §6 — Handoff to Build

Where execution is required, Project Design creates or authorises a WorkPackage conforming to `AIDE_WorkPackage`.

The handoff must define enough work-specific intent that Build does not need to reconstruct the design process to know the required result.

Generic execution/platform knowledge belongs to the Build environment and applicable Standards/Tools; it is not copied into every WorkPackage merely for self-containment.

## §7 — Return from Build

Build returns a WorkPackage Outcome stating what was done, what was produced, validation evidence, deviations, unresolved issues and any design question discovered during execution.

Project Design then:

- confirms/records completion where the defined outcome is satisfied;
- resolves a design issue and issues revised/further work; or
- explicitly accepts a residual difference/risk within the work owner's authority.

Execution evidence is input to Project Design state; it does not silently rewrite the Design.

## §8 — Simplicity and escalation

A sound conceptual model should normally permit a clean implementation. When downstream execution requires accumulating exceptions, compensating mechanisms or special cases, Project Design should consider whether ownership, boundaries, requirements or the model itself should be simplified before adding further machinery.

Routine reversible detail may be resolved during execution. Changes to objective, authorised scope, acceptance, major ownership or architecture return to Project Design.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Review@v1
References: Build_Design_v1, AIDE_WorkPackage@v1
<!-- END SOURCE: ProjectDesign_Design_v1.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Decisions_v1.md -->
# Project Design — Decisions

> **Version 1** (2026-08-30). Records the decisions establishing Project Design as the generic design-side AIDE methodology and separating domain workflows from the reusable Project Design/Build contracts.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## D1 — Use Project Design rather than Design or Solution Design

**Decision.** The top-level methodology is named **Project Design**. `Design` remains a valid artefact/stage within it.

**Reason.** Bare `Design` is too overloaded, while `Solution Design` implies a narrower technical/software context. Project Design applies naturally to the intended range of substantial work.

## D2 — Project Design is domain-independent

**Decision.** Project Design defines reusable behaviour for determining substantial work, not a software-development lifecycle or product-specific process.

**Reason.** Software, documentation, capability, business and creative projects share the same core questions of intent, requirements, decisions, approach and outcomes.

## D3 — Domain production workflows remain domain-owned

**Decision.** Do not introduce a generic top-level Workflow owner for all production scenarios. A domain owns the workflow that composes Project Design, Build and other AIDE concerns for its type of work.

**Reason.** A universal workflow layer would have to understand every domain and would duplicate semantics already owned by Project Design and Build.

## D4 — Project Design and Build form an iterative loop

**Decision.** The generic handoff is Design Outcome → WorkPackage → Build → Build Outcome, with the outcome returning to Project Design where completion or a design issue must be reconciled.

**Reason.** Execution can reveal evidence or constraints that legitimately change the next design state without transferring design authority into Build.

## D5 — Layered overviews are a design-control mechanism

**Decision.** For substantial design, use a short intent/system layer and model layer as the primary checkpoint before detailed mechanics.

**Reason.** A compact complete view makes drift, boundary errors, missing concepts and unnecessary complexity easier to detect. Difficulty explaining the model simply is evidence to reconsider the model before expanding the specification.

---
Dependencies: !AIDE_DocumentationMethodology@v18, ProjectDesign_Design_v1
References: Core_System_Design_v4, Build_Design_v1
<!-- END SOURCE: ProjectDesign_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_ProjectDesign_Standard_v1.md -->
# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v1`
> **Common name:** Project Design
> **Version 1** (2026-08-30). Initial behavioural contract for defining substantial project work and handing defined execution to Build.
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

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v1`.

The package must make the required result, authority, work-specific inputs and acceptance clear. Do not embed generic execution-platform knowledge that is already supplied by the Build environment.

## Handle Build return

On Build Outcome:

- close/record completion when acceptance is satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

Build may resolve implementation detail within authority; it does not silently change objectives, major scope, acceptance or architecture.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

---
Dependencies: !AIDE_DocumentationMethodology@v18, ProjectDesign_Design_v1, AIDE_Review@v1
References: AIDE_WorkPackage@v1
<!-- END SOURCE: AIDE_ProjectDesign_Standard_v1.md -->

---
