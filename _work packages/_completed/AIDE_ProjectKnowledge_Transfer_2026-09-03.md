# AIDE Project Knowledge Transfer

**Date:** 2026-09-03  
**Status:** Consolidation complete / closed  
**Purpose:** Preserve durable project-level continuity from the former sibling AIDE ChatGPT projects after their chats and source/context files were consolidated into the single **AIDE** project.

## Authority and use

This document is a **continuity and transfer artefact**, not an authoritative AIDE master.

Use the following precedence:

1. Current authoritative individual masters.
2. Current owner-specific Binders and current live-state documents, interpreted according to their normal authority rules.
3. Current generated Bundles as read-only consumption artefacts.
4. This transfer record and the former project knowledge-transfer documents as historical/continuity context only.

Do not allow an older transfer note, remembered version, stale Binder reference, or historical status statement to override the current authoritative corpus.

## Consolidation scope

The former sibling project knowledge covered:

- Documentation Methodology
- Core
- Build
- Project Design
- Working Practices
- AI Deployment

Their chats and source/context files have been moved into the consolidated **AIDE** project.

The consolidation is **operational/context consolidation only**. It does not merge the semantic ownership of AIDE's top-level topics. The recognised top-level structure remains:

```text
AIDE
├── Core
├── Principles
├── Working Practices
├── Project Design
├── Build
├── Capabilities
├── AI Deployment
└── Documentation Methodology
```

A single physical/chat project may contain all of these concerns while their semantic ownership remains distinct.

## Durable project knowledge retained

### Cross-topic work and ownership

- Different top-level topic ownership alone does **not** require a Project Handoff.
- When the current authoritative source context for all affected topics is available and sufficient, coordinated cross-topic reconciliation may be performed directly in one coherent pass.
- Use a **Project Handoff** only where a genuine transfer boundary exists, such as deferred ownership, unavailable authority/context, independent response/review needs, or concurrency/conflict that prevents direct reconciliation.
- Topic-specific semantic authority remains with the owning topic even when work is performed from the consolidated AIDE project.

### Documentation and lifecycle practice

- Individual current masters are authoritative; generated Binders and Bundles are read-only consumption artefacts and are not edited directly.
- WIP, OpenItems, WorkRegister and similar live-state documents remain outside stable Binder authority where the owning methodology defines them as live state.
- Change Delivery Packages, Project Handoffs and knowledge-transfer files are transfer/application artefacts rather than new authoritative semantic sources unless deliberately promoted through the owning process.
- Management/workflow folders use `_`-prefixed names where applicable, including `_superseded`, `_archived`, `_changeDeliveryPackages`, and `_completed`.
- Generated Binders are versioned; replaced versions follow the applicable superseded/archive workflow.
- Use one current WIP series per top-level topic. Concurrent subthreads belong inside that root WIP rather than in separate subtopic-specific WIP series.

### Output cadence and loss prevention

- Do not issue changed masters or Change Delivery Packages after every small change by default.
- Batch confirmed changes to a meaningful work-unit, session, checkpoint, or explicit output request.
- Avoid unnecessary version churn, but preserve material confirmed reasoning/state before volatile context loss.
- For material multi-file Change Delivery Packages, include concise application instructions identifying what to add, replace, supersede, archive, move, rename, regenerate, or apply, and where.

### Decision and execution posture

- Routine, reversible and low-risk implementation decisions may be resolved autonomously within established authority.
- Design-shaping, architecture, policy, ownership, objective, acceptance, or other high-impact changes should be surfaced for explicit user judgement.
- Prefer compact orientation first: purpose/intent/model, then supporting detail.
- Keep machine-oriented metadata compact where practical in human-readable documents.

### Project Design and Build boundary

- **Project Design** owns intent, requirements, considerations, decisions, design, review and design outcomes/deliverables.
- **Build** performs bounded objective-driven execution and validation; it is not limited to coding or compilation.
- The Project Design → Build handoff uses the current `AIDE_WorkPackage@v3` contract.
- A WorkPackage must remain sufficiently self-contained for execution; WorkRegister mapping provides traceability but does not replace the WorkPackage.
- WorkRegister ↔ WorkPackage mapping may be many-to-many.
- Split obligations use independently identifiable changes plus exact `Covers` mapping; no synthetic structured sub-obligation identifier system is required by the current model.
- Build returns execution evidence. It does not silently close the owning topic's WorkRegister obligation; the directing/owning process performs reconciliation and closure.
- A mapped result awaiting owner reconciliation may remain `Returned — reconciliation pending`.

### Build and deployment seam

- Build output identity is distinct from semantic release identity and from actual deployment state.
- Deployment-facing outputs retain provenance, concrete output/package identity or integrity evidence, and their composition posture.
- `MemberContribution` outputs may be mechanically assembled downstream where permitted.
- `AssembledConsumptionArtefact` outputs are atomic at the semantic/member-composition boundary and are not semantically rebuilt by Deployment.
- A **Build Target** is a producer-side output requirement and is not the same concept as an AI Deployment Target.

### AI Deployment continuity

- AI Deployment is a generic AIDE deployment framework, not a Capabilities-only subsystem.
- It may deploy validated built AIDE material including Capabilities, Standards/Tools, plugins, skills, contributions, Bundles, Bootstrap material and future deployable kinds.
- One generic deployment framework does not imply one runtime or channel. Separate runtimes/channels may remain separate Targets even when they consume the same representation or output.
- A manual Bundle replacement can be a valid deployment-channel implementation; it is not inherently an architectural exception.
- Concrete artefact/package identity should be operationally inspectable where practical.
- Runtime verification must be distinguished from UI presence, installation state, marketplace visibility, or filesystem presence. Fresh-session or runtime probes may be required.
- Semantically unchanged material may still produce a distinct PackageId/build identity and therefore require Registry/Set/Target reconciliation.
- Remaining provider-specific unknowns should be treated as empirical adapter questions unless evidence exposes a missing generic architectural concept.

## Historical checkpoints retained only for context

The following are useful historical continuity but must **not** be reintroduced as current requirements or outstanding work merely because they appeared in transfer material:

- Core Review A completion details and then-current release checkpoints are historical evidence; current Core masters own present semantics and status.
- Earlier `AIDE_WorkPackage@v2` references may remain truthful where genuinely historical, but must not be restored as the current Project Design → Build contract.
- The former Project Design obligation to rebuild a temporary Standards & Tools Bundle after older ProjectDesign content is overtaken by later bundle generations and is not active.
- The AI Deployment transfer's use of AI Deployment Binder v7 and warning that Standards & Tools Bundle v9 was stale were already overtaken by later current artefacts; do not recreate that warning or obligation.
- Older proposed Documentation Methodology structures, obsolete version references, and pre-reconciliation ownership hypotheses remain history unless deliberately re-approved through current authority.
- The Working Practices transfer identified no hidden additional project-specific design state, rule, decision, or obligation beyond the moved chats and current corpus.

## Active-state rule

The completed knowledge-transfer exercise itself introduces **no new active AIDE obligation**.

Any active work must come from the current authoritative/live-state AIDE corpus, not from this consolidation record. Historical transfer notes may explain why a current state exists, but they do not independently reopen completed work.

## Closure

All intended sibling-project project-knowledge transfers have been accounted for and their durable non-authoritative continuity has been retained in the consolidated AIDE project.

**Knowledge-transfer consolidation status: CLOSED.**
