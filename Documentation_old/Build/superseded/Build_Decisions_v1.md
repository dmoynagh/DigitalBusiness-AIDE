# Build — Decisions

> **Version 1** (2026-08-30). Records the decisions establishing Build as generic execution/production behaviour and WorkPackage as its principal governed handoff.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## D1 — Retain Build and define it behaviourally

**Decision.** Retain **Build** as the AIDE area for objective-driven execution/creation. It is not defined as compilation, coding or any particular product.

**Reason.** The common behaviour is taking defined work and producing/validating artefacts. Current products are implementations of that behaviour rather than its definition.

## D2 — WorkPackage is the principal governed handoff into Build

**Decision.** Build consumes a WorkPackage containing work-specific intent, authority, inputs, outputs and acceptance; Build environments supply reusable implementation/platform knowledge.

**Reason.** This makes the handoff self-contained without copying generic execution knowledge into every project.

## D3 — Build has bounded implementation authority

**Decision.** Build may resolve ordinary implementation detail within authorised scope but returns objective, scope, acceptance, architecture or policy changes to the work owner/Project Design.

**Reason.** Execution needs autonomy to be efficient without silently becoming a second design authority.

## D4 — Build standards describe behaviour, not products

**Decision.** Codex, Claude Code, ChatGPT Work, Claude Co-work and future systems are Build environments/implementations. Generic Build Standards do not encode their product mechanics.

**Reason.** Behavioural contracts remain stable while products and platform capabilities change.

## D5 — Every executed WorkPackage returns evidence

**Decision.** Build returns an Outcome recording actual work, outputs, validation, deviations, unresolved issues and design feedback.

**Reason.** The director of work must be able to reconcile execution without reconstructing the Build session, and completion must mean more than artefact creation.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v1
References: ProjectDesign_Design_v1, Core_System_Design_v4
