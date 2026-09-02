# Build — Decisions

> **Version 2** (2026-08-31). Adds decisions for canonical-to-derived representation, composable Build outputs, provenance, and the Build/AI Deployment boundary.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

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

## D6 — Canonical meaning remains upstream of platform/consumption representation

**Decision.** When Build renders or packages governed capability material, the current canonical Standard/Tool or other authoritative outcome supplies the semantics. Build does not reconstruct missing meaning from Decisions history or from an older derived Bundle/package.

**Reason.** A derived representation must be reproducible from authoritative state. Letting Build infer semantics from history or a stale consumption artefact would create a parallel source of truth and make platform outputs drift from the capability they claim to represent.

**Alternative rejected.** Treat an existing Bundle/package as the convenient production baseline and patch it forward. This is faster locally but makes a derived artefact authoritative by accident and can miss newer canonical releases.

## D7 — Build preserves composability and semantic role boundaries

**Decision.** Build may produce explicitly authorised subsets and combinations without assuming a fixed all-AIDE package. Distinct upstream roles remain distinct through rendering unless an authorised representation combines them without changing their semantic responsibilities.

**Reason.** Principles, Working Practices and future Standards may be independently deployable, while Bootstrap/Profile/Contribution/full guidance have deliberately different roles. Packaging convenience must not erase those architectural boundaries.

**Alternative rejected.** Define one fixed full-AIDE package and make subset builds exceptions. That would simplify one packaging path but undermine independent deployment and turn composition policy into Build architecture.

## D8 — Build output is not Deployment state

**Decision.** Build may produce platform-compatible artefacts, packages and assembled consumption representations, but their production does not claim installation, target reconciliation or runtime availability. AI Deployment owns those target-state concerns.

**Reason.** Keeping artefact production separate from environment reconciliation preserves truthful status and avoids making successful generation indistinguishable from successful deployment.

**Boundary consequence.** AI Deployment may still own desired Deployment Set composition and target-state orchestration, but wording that makes Deployment itself the semantic renderer/builder of target artefacts should be reconciled so the two areas do not claim the same production responsibility.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v2
References: ProjectDesign_Design_v1, Core_System_Design_v4, AIDE_Deployment@v1
