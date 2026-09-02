# Core System — Decisions

> **Version 4** (2026-08-31). Integrates Core ownership of Domain and removes ambiguity between the
> Core Domain foundation and development/product Domain workflow ownership.
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

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v5
References: AIDeployment_Decisions_v1, ProjectDesign_Decisions_v1, Build_Decisions_v1, Core_Domain_Decisions_v1
