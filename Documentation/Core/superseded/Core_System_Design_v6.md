# Core System — Design

> **Version 6** (2026-08-31). Adds the Bootstrap Profile/Contribution model and recognises
> Principles and Working Practices as top-level independently deployable AIDE guidance concerns.
>
> Created: 2026-08-28 | Last modified: 2026-08-31

## §1 — AIDE system boundary

**AIDE is the overall AI-development system.** It supplies shared foundations, base guidance,
project-design methodology, build methodology, reusable capabilities, platform/environment
concerns and documentation methodology that may be consumed wherever applicable.

Development/product Domains consume AIDE; they are not components of AIDE.

The principal conceptual areas are:

```text
AIDE
├── Core
│   ├── Domain
│   └── Bootstrap
├── Principles
├── Working Practices
├── Project Design
├── Build
├── Capabilities
├── Environment / platform concerns
│   └── AI Deployment
└── Documentation Methodology (design-methodology concern)
```

Conceptual ownership and GPT Project/master-folder boundaries are related but are **not required
to be identical**.

Principles and Working Practices are part of AIDE but are deliberately independently deployable.
An AI environment may use either/both as general guidance without activating the wider AIDE
development system.

## §2 — Principal areas

### Core

Owns system-wide foundations, identity, Domain, Bootstrap and the reference view of AIDE structure.

#### Domain

Domain is the Core-owned system-wide foundation for resolving the named AIDE operating/governance
context relevant to a target when such context is needed. Project Design, Build, Capabilities,
Documentation Methodology, Environment/AI Deployment and future AIDE concerns may consume that
context without redefining Domain behaviour.

Detailed Domain semantics are owned by `Core_Domain_Design_v1`; the canonical AI-facing contract is
`AIDE_Domain@v1`. This Core ownership does not move development/product Domains into the AIDE system
tree or transfer ownership of their substantive workflows to Core.

#### Bootstrap

Bootstrap is the stable activation seam between persistent platform-level instructions and the
deployable guidance, Standards, Tools and other material available to a specific environment.

The layered model is:

```text
persistent platform bootstrap
        ↓
Bootstrap Profile
        ↓
thin Bootstrap Contributions
        ↓
full guidance / Standards / Tools loaded when needed
```

The persistent platform bootstrap is deliberately tiny and changes rarely.

A Bootstrap Profile is environment-specific and identifies only:

```text
WHAT  — the operating material/capability to bring into play
WHY   — why/when it matters in this environment
WHERE — how the authoritative deployed material can be resolved
```

A Profile is an early-context map, not a compressed copy of the referenced material.

Components may own thin, separately deployable Bootstrap Contributions where they have a
demonstrated early-session need. Detailed behaviour remains in the owning Standard/Tool/guidance
and is loaded only when relevant.

Startup-required presence uses the normal Dependencies mechanism rather than a Bootstrap-specific
dependency language. Bootstrap may surface a missing required item but does not install, update or
reconcile it.

Bootstrap/Profile artefacts may themselves be deployed through AI Deployment. Bootstrap does not
govern Deployment.

Detailed semantics are owned by `Core_Bootstrap_Design_v2`; the canonical AI-facing contract is
`AIDE_Bootstrap@v1`.

### Principles

Principles owns portable base reasoning and problem-solving guidance: the durable premises used to
judge an approach before detailed operating conventions are applied.

Canonical outcome: `AIDE_Principles@v1`.

Principles is independently deployable and may be refined by applicable organisation/group/team/user
Guidance Profiles without requiring a fork of the base Standard.

### Working Practices

Working Practices owns portable cross-surface conventions for how an AI and user practically work
together, including work progression, handoff, verification and output-delivery conventions.

Canonical outcome: `AIDE_WorkingPractices@v1`.

Working Practices is independently deployable and may be refined by the same conceptual Guidance
Profile delta model as Principles.

Principles and Working Practices are siblings: Principles answers how judgement should be guided;
Working Practices answers how work should be carried out and handed over.

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

Bootstrap may state a runtime requirement and may be part of a deployment set, but it does not
decide what the host administrator/environment controller is authorised to install or perform the
deployment itself.

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
├── Principles/
├── Working Practices/
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

Principles and Working Practices are cross-cutting guidance rather than Design-side or Build-side
owners.

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

AIDE maintains a small stable bootstrap layer through the strongest persistent mechanism available
in each participating AI environment.

The persistent instruction discovers/processes an applicable Bootstrap Profile where available.
The Profile defines the environment's startup posture using what/why/where entries. Thin component
Bootstrap Contributions may then perform owner-defined early-session setup/checks. Full operating
material remains lazy and is loaded when the current work requires it.

`{bootstrap}` remains the generic marker for content requiring best-effort early-session
discovery. The marker itself has no component-specific semantics.

No Bootstrap Profile is a valid state; the session continues normally where none is available.
One effective Profile applies by default. Generic profile merging/precedence is not defined.

Platform implementation must not claim stronger startup enforcement than the platform provides.

## §8 — Base guidance and Guidance Profiles

`AIDE_Principles@v1` and `AIDE_WorkingPractices@v1` are base guidance.

More-specific organisation/group/team/user Guidance Profiles may provide small deltas that add,
refine or explicitly override named base guidance. Unmentioned base guidance remains effective.

The shared profile concept is intentionally not promoted into another generic AIDE component yet.
Principles and Working Practices are the current demonstrated consumers; broader generalisation
requires additional evidence.

Host/platform instruction priority remains outside AIDE.

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: ProjectDesign_Design_v1, Build_Design_v1, Capabilities_Design_v8, AIDeployment_Design_v1, Core_Domain_Design_v1, Core_Bootstrap_Design_v2, Principles_Design_v3, WorkingPractices_Design_v2
