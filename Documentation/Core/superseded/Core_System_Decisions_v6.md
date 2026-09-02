# Core System — Decisions

> **Version 6** (2026-08-31). Preserves the existing decision history and records the Project Design path correction, top-level-topic/container distinction and Core-owned generic Index architecture.
>
> Created: 2026-08-28 | Last modified: 2026-08-31

## D1 — AIDE is the umbrella AI-development system

**Decision.** AIDE is the overall system. Development/product Domains consume it but remain
outside it.

## D2 — Project Design replaces ambiguous top-level “Design”

**Decision.** The generic design methodology is named **Project Design**.

**Reason.** Bare `Design` is overloaded; `Project Design` describes software, documentation,
capability, business, creative and other substantial project work without narrowing to software.

## D3 — Build is behavioural execution

**Decision.** Build means objective-driven execution of defined work, not software compilation or
coding. Current/future execution-capable AI products implement the behaviour.

**Reason.** Behavioural standards are durable across products and allow non-code production.

## D4 — WorkPackage belongs under Build

**Decision.** WorkPackage is the generic governed handoff into Build and returns a WorkPackage
Outcome.

## D5 — Development/product Domain workflows remain Domain-owned

**Decision.** A development/product Domain owns the workflow that composes Project Design, Build
and other AIDE services for its substantive work. AIDE does not create a giant generic Workflow
owner.

**Boundary.** Core ownership of the common Domain context contract does not transfer a
development/product Domain's substantive workflow ownership to Core.

## D6 — Generic Deployment is promoted out of Capabilities

**Decision.** Capabilities no longer owns generic deployment mechanics. AI Deployment owns
set-aware composition, delivery/reconciliation and verification. Capabilities remains a producer
of canonical capabilities, packages and logical deployment intent.

**Reason.** Deployment semantics concern platforms, surfaces, representations, channels,
destinations and observed state and can apply to deployables beyond Capabilities.

## D7 — Project containers need not mirror conceptual ownership

**Decision.** GPT Project/master-folder boundaries are operational context containers and may be
more granular than the conceptual AIDE tree.

The current layout is:

```text
Core/
Design Project/
Build/
Capabilities/
AI Deployment/
Document Methodology/
bundles/
```

**Reason.** A dedicated project is valuable when a workstream has enough context/lifecycle to
benefit from isolation. Forcing physical context boundaries to mirror conceptual ownership creates
unnecessary coupling.

## D8 — Canonical terminology and physical folder label may differ

**Decision.** The canonical topic is `Project Design`; the current physical/GPT Project container
is `Design Project`. Documentation must state the mapping rather than silently treating the terms
as different concepts.

## D9 — Documentation Methodology conformance uses Dependencies + Migration

**Decision.** From Documentation Methodology v18, per-document conformance is represented through
the generic Dependencies model rather than a special `Methodology: vN` footer line.

**Reason.** Dependencies already owns saved/proven conformance checkpoints and Migration owns
version-gap transitions. Keeping a second DocMeth-only mechanism adds duplication.

## D10 — Metadata host/owner boundary remains system-wide

**Decision.** Documentation Methodology owns generic document metadata placement; each capability
owns the semantics of its contributed metadata/state.

## D11 — AIDE retains a small stable bootstrap layer

**Decision.** `{bootstrap}` remains the generic best-effort early-discovery marker. Operational
logic lives in the owning Standards/Tools rather than being copied into permanent platform
instructions.

## D12 — Domain is a Core-owned system foundation

**Decision.** Core owns the common Domain contract used across AIDE to resolve a named
operating/governance context when one is relevant.

**Reason.** Project Design, Build, Capabilities, Documentation Methodology, Environment/AI
Deployment and future AIDE concerns need one shared context model rather than separate local Domain
semantics.

**Boundary.** Development/product Domains remain outside the AIDE system tree and consume AIDE.
Their substantive workflows and work remain theirs. The detailed Domain model and its reasoning
are owned by `Core_Domain_Design` and `Core_Domain_Decisions`, not duplicated here.

## D13 — Bootstrap is extended by environment-specific Profiles

**Trigger / problem.** The stable `{bootstrap}` marker prevents permanent platform instructions
from carrying operational component logic, but the existing model does not say how one unchanged
machine-level bootstrap can activate different AIDE subsets in different environments.

**Alternatives considered.**

- Hard-code the current AIDE operating set into ChatGPT/Claude/Codex machine instructions.
  Rejected because every release or environment change would require editing persistent
  platform configuration.
- Treat every available `{bootstrap}` block as an undifferentiated startup set. Rejected because
  physical availability is not the same thing as the intended startup posture for the environment.

**Decision.** Add a Core-owned **Bootstrap Profile** between the stable persistent platform
bootstrap and component Bootstrap Contributions.

A Profile identifies only `what`, `why` and `where`. Component Contributions remain thin and
separate from full Standards/Tools/guidance, which are loaded when needed.

**Consequences.** One stable platform instruction can support full AIDE development, a
Principles/Working-Practices-only environment, another future subset, or no AIDE Profile at all.

## D14 — Bootstrap reuses Dependencies and does not deploy

**Decision.** Bootstrap does not create a second dependency language or an installation mechanism.

Where startup-required presence is declared, use the normal Dependencies mechanism. Bootstrap may
surface a missing requirement at startup; it does not install, update, remove or reconcile it.

**Reason.** Requirement, observed presence, permission/authority to change the host, and deployment
action are distinct facts/concerns.

**Consequence.** Bootstrap/Profile artefacts may be deployed by AI Deployment, but Bootstrap does
not govern Deployment. Future trusted-source acquisition remains possible without placing package
acquisition authority inside Bootstrap.

## D15 — Generic startup-task orchestration is deferred

**Decision.** Do not create a general startup task engine.

**Reason.** The demonstrated needs are Profile activation, thin owner-defined Bootstrap
Contributions and startup-required dependency presence checks. Task orchestration should be added
only if a concrete startup need cannot be expressed cleanly through those mechanisms.

## D16 — Principles and Working Practices are top-level AIDE concerns

**Trigger / problem.** Cross-cutting guidance was previously parked under other work because that
was where the conversation occurred. Reasoning principles and practical AI/user working
conventions apply across projects, Domains and even non-development AI use.

**Decision.** Principles and Working Practices are sibling top-level AIDE concerns.

- Principles owns durable reasoning/problem-solving premises.
- Working Practices owns concrete cross-surface collaboration and operating conventions.

**Consequence.** The Core reference view and operational project-container map include both.

## D17 — Principles and Working Practices are independently deployable base guidance

**Decision.** `AIDE_Principles@v1` and `AIDE_WorkingPractices@v1` are usable as part of full AIDE
or independently.

**Reason.** General AI sessions can benefit from the base guidance without Project Design, Build,
Domain or other development concerns.

## D18 — Guidance Profiles customise base guidance by delta

**Decision.** Organisation/group/team/user Guidance Profiles may add, refine or explicitly
override named Principles/Working Practices guidance without copying/forking the base Standards.

**Alternatives considered.**

- Publish complete team/user-specific copies of the base Standards. Rejected because copied bases
  diverge and turn every base update into a merge exercise.
- Create a new generic top-level profile subsystem now. Deferred because Principles and Working
  Practices are the demonstrated consumers and further generalisation has not yet earned its
  mechanism.

**Consequence.** Unmentioned base guidance remains effective. Equal-specificity conflict fails
visibly unless an explicit ordering exists. Host/platform instruction priority remains outside
AIDE.

## D19 — The operational project-container map expands

**Decision.** The current operational layout adds dedicated `Principles/` and
`Working Practices/` master-folder/GPT Project containers.

**Relationship to D7.** D7 records the earlier container set. This decision updates the current
operational map without rewriting that historical decision.

**Consequence.** Conceptual ownership and project-container boundaries remain intentionally
distinct.

## D20 — Correct the Project Design physical/container mapping

**Trigger / problem.** Current Core documents state that the canonical concern is `Project Design`
while the physical container is `Design Project`. Repository history and current configuration show
that the physical Documentation folder has always been `AIDE/Project Design/`.

**Decision.** Use **Project Design** consistently for the canonical concern and current
project/container name. Replace current operational references to `Design Project/` with
`Project Design/`.

**Consequence.** Treat the earlier mapping as a documentation/configuration error, not as a
historical folder rename. Filename prefix and formal identity remain `ProjectDesign` and
`AIDE_ProjectDesign`.

## D21 — Top-level topic is the semantic anchor; project/container is a context boundary

**Trigger / problem.** Registers and workflow rules described as “project-wide” become ambiguous
when one chat project/master folder hosts several top-level topics sharing the same context pool.

**Decision.** Treat project/chat-project/master-folder as a **container**. Semantic registers and
similar standing state anchor to the **top-level topic** by default unless their owning Standard
explicitly delegates narrower scope.

**Consequence.** A container can validly hold several top-level topics, each with its own live
registers, without implying they form one semantic project.

## D22 — Generic Index belongs to Core

**Trigger / problem.** Index is useful beyond documentation: repository/catalogue navigation,
native structures and future AIDE mechanisms require the same authoritative hierarchical item
concept. Documentation Methodology's existing Index is too specialised to serve as the generic
owner cleanly.

**Decision.** Establish Core/Index and publish `AIDE_Index@v1`. Documentation Methodology becomes a
specialist consumer/extension owner.

**Consequences.** Core owns Items, Item Type Definitions, generic authority, hierarchy, delegation,
extension hosting and the thin runtime type-registry projection. Document-specific registers and
lifecycle remain in Documentation Methodology.

## D23 — Generic Index does not automatically create Domain authority

**Decision.** An arbitrary Index or Item Type cannot declare itself Domain-defining. Core/Domain
owns the approved Domain-capable type set and derives the hot-path recognition projection.

**Reason.** Domain formation changes governance/operating context and therefore requires a
restricted system-level assignment rather than an extensibility side effect.

## D24 — The Core conceptual tree adds Index

**Decision.** Core's principal foundations are now Index, Domain and Bootstrap.

**Consequence.** `Core_Index_Design_v1`, `Core_Index_Decisions_v1` and `AIDE_Index@v1` become
Current Core sources/outcome and are registered in the Core Index.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Core_System_Design_v7
References: Core_Index_Decisions_v1, Core_Domain_Decisions_v2, WorkingPractices_Decisions_v5
