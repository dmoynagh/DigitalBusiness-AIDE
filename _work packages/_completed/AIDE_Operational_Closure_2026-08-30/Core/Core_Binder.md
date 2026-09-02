# Core Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.

## Binder manifest

- `Core_Index_v1.md` — sha256 `cc3438f287ae`
- `Core_System_Design_v4.md` — sha256 `6970c1fa8bd3`
- `Core_System_Decisions_v3.md` — sha256 `4cdd1fc48b06`

---

<!-- BEGIN SOURCE: Core_Index_v1.md -->
# Core — Index

> **Version 1** (2026-08-30). Registers the current Core system architecture files after the
> operational closure pass.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic:** Core  
**Project container / master folder:** `AIDE/Core/`

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Core_Index` | v1 | Index | Current |
| `Core_System_Design` | v4 | Design | Current |
| `Core_System_Decisions` | v3 | Decisions | Current |

## Project-container map

| Canonical concern | Master folder / GPT Project |
|---|---|
| Core | `Core` |
| Project Design | `Design Project` |
| Build | `Build` |
| Capabilities | `Capabilities` |
| AI Deployment | `AI Deployment` |
| Documentation Methodology | `Document Methodology` |
| Generated common bundle | `bundles` |

---
Dependencies: !AIDE_DocumentationMethodology@v18
References: Core_System_Design_v4
<!-- END SOURCE: Core_Index_v1.md -->

---

<!-- BEGIN SOURCE: Core_System_Design_v4.md -->
# Core System — Design

> **Version 4** (2026-08-30). Reconciles the AIDE architecture with Project Design, generic Build,
> dedicated AI Deployment, the new project-container model, and Documentation Methodology v18.
>
> Created: 2026-08-28 | Last modified: 2026-08-30

## §1 — AIDE system boundary

**AIDE is the overall AI-development system.** It supplies shared foundations, project-design
methodology, build methodology, reusable capabilities, platform/environment concerns and
documentation methodology that may be consumed wherever applicable.

Development/product domains consume AIDE; they are not components of AIDE.

The principal conceptual areas are:

```text
AIDE
├── Core
├── Project Design
├── Build
├── Capabilities
├── Environment / platform concerns
│   └── AI Deployment
└── Documentation Methodology (design-methodology concern)
```

Conceptual ownership and GPT Project/master-folder boundaries are related but are **not required
to be identical**.

## §2 — Principal areas

### Core

Owns system-wide foundations, identity, bootstrap and the reference view of AIDE structure.

### Project Design

Owns the generic method for defining substantial work: intent, requirements, decisions/model,
defined outcomes and the handoff/return relationship with Build.

Formal runtime identity: `AIDE_ProjectDesign@v1`.

### Build

Owns generic objective-driven execution of defined work. WorkPackage is the principal governed
handoff into Build and its Outcome is the return evidence.

Formal runtime identities include `AIDE_Build@v1` and `AIDE_WorkPackage@v1`.

### Capabilities

Owns reusable AI-facing capability infrastructure:

- Standards
- Tools
- Tags
- Scope
- Dependencies
- Migration
- Review
- capability-local canonical production and Package/deployment-intent production.

**Generic Deployment is no longer a Capabilities component.**

### Environment / platform concerns

Own factual environment/platform configuration: available surfaces, representations, channels,
destinations, accounts/workspaces, model/runtime facts, access references and other current
environment state.

### AI Deployment

Owns generic set-aware composition, publication/install/update/remove reconciliation and
verification of deployable artefacts in AI runtime targets.

AI Deployment is maintained in its own master folder/GPT Project because it is an active,
coherent workstream. That project-container boundary does not move producer semantics into
Deployment or require every Environment concern to live in the same GPT Project.

### Documentation Methodology

Owns document naming, types, corpus structure/lifecycle, generic metadata-container placement and
document-specific rendering. Generic Identity, Tags, Dependencies, Migration and Review semantics
remain with their AIDE owners.

Documentation Methodology is maintained in a dedicated master folder/GPT Project because of its
size and independent lifecycle, while remaining conceptually a project/design methodology.

## §3 — Project containers and master folders

The current operational GPT Project/master-folder layout is:

```text
AIDE/
├── Core/
├── Design Project/
├── Build/
├── Capabilities/
├── AI Deployment/
├── Document Methodology/
└── bundles/
```

These are **context containers**, selected to make each GPT Project coherent and easy to refresh.
They do not have to mirror the conceptual ownership tree one-for-one.

Canonical topic terminology remains **Project Design** even though the current physical container
is named `Design Project`.

Each master folder may contain a `superseded/` subfolder for prior issued versions. Current master
files remain in the folder root.

`bundles/` contains generated consumption artefacts and is not an authoritative master topic.

## §4 — Side and applicability

**Design side** and **Build side** are working contexts, not ownership silos.

A Standard or Tool may apply on Design, Build or both according to Scope. Project/container
placement never substitutes for applicability.

## §5 — Formal identities

Internal topic and source-document names stay readable. Formally referenceable/published/deployed
AIDE artefacts use namespaced `AIDE_` identities where collision is plausible.

A referenceable artefact may expose multiple ordered identities:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

Identity resolves by name before version comparison.

## §6 — Document metadata-container boundary

Documentation Methodology owns generic header/footer metadata containers and temporary-state
placement for governed documents. The contributing owner owns each block/property's semantics.

```text
Core Identity       → header Identity metadata
AIDE_Tags           → footer Tags metadata
AIDE_Dependencies   → footer Dependencies metadata
AIDE_Migration      → migration semantics / owner-labelled temporary state
DocMeth             → placement, coexistence and document-specific rendering
```

## §7 — System bootstrap

AIDE maintains a small stable bootstrap layer deployed through the strongest persistent mechanism
available in each participating AI environment.

`{bootstrap}` marks instructions requiring best-effort early-session discovery. Components own
their own bootstrap content; the marker itself has no component-specific semantics.

Platform implementation must not claim stronger startup enforcement than the platform provides.

---
Dependencies: !AIDE_DocumentationMethodology@v18
References: ProjectDesign_Design_v1, Build_Design_v1, Capabilities_Design_v8, AIDeployment_Design_v1
<!-- END SOURCE: Core_System_Design_v4.md -->

---

<!-- BEGIN SOURCE: Core_System_Decisions_v3.md -->
# Core System — Decisions

> **Version 3** (2026-08-30). Reconciles the top-level model with Project Design, the dedicated
> project-container layout, AI Deployment promotion, and Documentation Methodology v18.
>
> Created: 2026-08-28 | Last modified: 2026-08-30

## D1 — AIDE is the umbrella AI-development system

**Decision.** AIDE is the overall system. Product/development domains consume it but remain
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

## D5 — Domain production workflows remain domain-owned

**Decision.** A domain owns the workflow that composes Project Design, Build and other AIDE
services for that domain. AIDE does not create a giant generic Workflow owner.

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

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: AIDeployment_Decisions_v1, ProjectDesign_Decisions_v1, Build_Decisions_v1
<!-- END SOURCE: Core_System_Decisions_v3.md -->

---
