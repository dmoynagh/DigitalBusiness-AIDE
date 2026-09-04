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
