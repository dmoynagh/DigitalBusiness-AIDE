# Core System — Design

> **Version 5** (2026-08-31). Integrates Domain as a Core-owned system foundation while preserving
> development/product Domains as external consumers of AIDE.
>
> Created: 2026-08-28 | Last modified: 2026-08-31

## §1 — AIDE system boundary

**AIDE is the overall AI-development system.** It supplies shared foundations, project-design
methodology, build methodology, reusable capabilities, platform/environment concerns and
documentation methodology that may be consumed wherever applicable.

Development/product Domains consume AIDE; they are not components of AIDE.

The principal conceptual areas are:

```text
AIDE
├── Core
│   └── Domain
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

Owns system-wide foundations, identity, Domain, bootstrap and the reference view of AIDE structure.

#### Domain

Domain is the Core-owned system-wide foundation for resolving the named AIDE operating/governance
context relevant to a target when such context is needed. Project Design, Build, Capabilities,
Documentation Methodology, Environment/AI Deployment and future AIDE concerns may consume that
context without redefining Domain behaviour.

Detailed Domain semantics are owned by `Core_Domain_Design_v1`; the canonical AI-facing contract is
`AIDE_Domain@v1`. This Core ownership does not move development/product Domains into the AIDE system
tree or transfer ownership of their substantive workflows to Core.

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
References: ProjectDesign_Design_v1, Build_Design_v1, Capabilities_Design_v8, AIDeployment_Design_v1, Core_Domain_Design_v1
