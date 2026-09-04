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
