# Core System — Design

> **Version 7** (2026-08-31). Adds the Core-owned generic Index/Item Type foundation, narrows
> Domain-defining authority to Domain-approved semantic types, establishes top-level topics as the
> semantic anchor distinct from context containers, and corrects the Project Design container path.
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
│   ├── Index
│   ├── Domain
│   └── Bootstrap
├── Principles
├── Working Practices
├── Project Design
├── Build
├── Capabilities
├── Environment / platform concerns
│   └── AI Deployment
└── Documentation Methodology
```

Conceptual ownership, top-level topics and chat-project/master-folder boundaries are related but
are **not required to be identical**.

A **top-level topic** is the normal semantic ownership/state anchor. A chat project, master folder
or workspace is an operational context/storage container and may contain one or several top-level
topics where shared context is useful.

## §2 — Principal areas

### Core

Owns system-wide foundations, identity, generic Index, Domain, Bootstrap and the reference view of
AIDE structure.

#### Index

Index is the generic structural registration and information-hosting foundation.

```text
Index
├── identity / scope
├── hierarchical Contents of significant Items
└── optional owner-defined properties / sections
```

Core/Index owns:

- Index scope/identity and generic authority boundary;
- hierarchical Item registration and containment/delegation;
- the generic Item and Item Type Definition contracts;
- `Folder`/`File` physical fallbacks;
- generic extension/property hosting and preservation; and
- the optional compact runtime Item Type Registry projection.

An Index is authoritative for the items it registers within its scope and for Index-owned
information about those registrations. Registration does not make it authoritative for the
registered item's internals.

Semantic owners may define Item Types, properties and specialised Index sections without
transferring their semantics to Core.

Canonical outcome: `AIDE_Index@v1`.

A generic Index is **not automatically Domain-defining**.

#### Domain

Domain is the Core-owned system-wide foundation for resolving the named AIDE operating/governance
context relevant to a target when such context is needed. Project Design, Build, Capabilities,
Documentation Methodology, Environment/AI Deployment and future AIDE concerns may consume that
context without redefining Domain behaviour.

Domain consumes semantic Item Types rather than treating any generic Index or arbitrarily shaped
file/folder as a governance boundary. The Item Type owner defines recognition/provisions; Core/
Domain alone approves which semantic types may establish or participate in Domain resolution.

For efficient discovery, approved recognition facts may be compiled into a thin
`DomainRecognitionRegistry`. This is derived runtime optimisation state, not semantic authority.

Domain also owns a narrow propagation-stop boundary: an enclosing Domain may be prevented from
propagating through a marked structural boundary. The stop does not create a child Domain and does
not define inheritance, merge or precedence.

Detailed semantics are owned by `Core_Domain_Design_v2`; canonical outcome:
`AIDE_Domain@v2`.

#### Bootstrap

Bootstrap is the stable activation seam between persistent platform-level instructions and the
deployable guidance, Standards, Tools and other AIDE material available to a specific environment.

The layered model remains:

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

A Profile is an early-context map, not a compressed copy of referenced material.

Components may own thin, separately deployable Bootstrap Contributions where there is a
demonstrated early-session need. Detailed behaviour remains in the owning Standard/Tool/guidance
and loads only when relevant.

Startup-required presence uses the normal Dependencies mechanism rather than a Bootstrap-specific
dependency language. Bootstrap may surface a missing requirement but does not install, update or
reconcile it.

Bootstrap/Profile artefacts may themselves be deployed through AI Deployment. Bootstrap does not
govern Deployment.

Detailed semantics: `Core_Bootstrap_Design_v2`; canonical outcome: `AIDE_Bootstrap@v1`.

### Principles

Principles owns portable base reasoning and problem-solving guidance: durable premises used to
judge an approach before detailed operating conventions are applied.

Canonical outcome: `AIDE_Principles@v1`.

Principles is independently deployable and may be refined by applicable organisation/group/team/
user Guidance Profiles without requiring a fork of the base Standard.

### Working Practices

Working Practices owns portable cross-surface conventions for how an AI and user practically work
together, including work progression, preservation of active state, handoff, verification and
output-delivery conventions.

Canonical outcome: `AIDE_WorkingPractices@v1`.

Working Practices is independently deployable and may be refined by the same conceptual Guidance
Profile delta model as Principles.

Principles and Working Practices are siblings: Principles guides judgement; Working Practices
guides how work is carried out and handed over.

### Project Design

Owns the generic method for defining substantial work: intent, requirements, decisions/model,
defined outcomes and the handoff/return relationship with Build.

A confirmed Design change commits the current model. Where it creates a downstream consequence
that is not fully delivered in the same pass, the owning top-level topic records the undelivered
consequence in WorkRegister. WorkPackages may then select manageable portions of those obligations
for execution.

Formal runtime identity: `AIDE_ProjectDesign@v2`.

### Build

Owns generic objective-driven execution of defined work. WorkPackage is the principal governed
handoff into Build and its Outcome is return evidence.

Where a WorkPackage maps to WorkRegister items, Build reports result/evidence/remaining work for
the mapped obligations. The owning/directing process reconciles those results; Build does not
silently close another owner's WorkRegister.

Formal runtime identities include `AIDE_Build@v4` and `AIDE_WorkPackage@v2`.

### Capabilities

Owns reusable AI-facing capability infrastructure:

- Standards;
- Tools;
- Tags;
- Scope;
- Dependencies;
- Migration;
- Review;
- capability-local canonical production and Package/deployment-intent production; and
- Messaging once the pending Messaging capability reconciliation is completed.

Generic AI Deployment remains outside Capabilities.

### Environment / platform concerns

Own factual environment/platform configuration: available surfaces, representations, channels,
destinations, accounts/workspaces, model/runtime facts, access references and other current
environment state.

### AI Deployment

Owns generic set-aware, policy-aware delivery/reconciliation and runtime verification of built
artefacts in AI targets.

AI Deployment consumes Build outputs and their provenance/integrity/composition posture. It may
mechanically assemble eligible `MemberContribution` outputs where a Target requires it; it does not
become a second semantic Build authority.

AI Deployment is maintained in its own master folder/chat project because it is a coherent
workstream. That container boundary does not move producer semantics into Deployment or require all
Environment concerns to share one container.

Bootstrap may state/surface a runtime requirement and may itself be a deployment member, but it
does not decide what the host administrator/environment controller is authorised to install and
does not perform deployment.

### Documentation Methodology

Owns governed document naming, document types and document lifecycle, top-level-topic/document
organisation semantics, document-specific Index extensions/registers, metadata-container hosting,
distribution rules, governed history, and the authority boundary between masters and generated
consumption artefacts.

Documentation Methodology **consumes `AIDE_Index@v1`** for generic Index/Item/Item Type semantics.
It no longer owns generic Index behaviour. It remains owner of documentation-specific additions
such as Document Register, topic declarations, custom document types, asset/unmanaged records and
the `DocumentationTopic` semantic Item Type.

Documentation Methodology is maintained in a dedicated master folder/chat project because of its
size and lifecycle while remaining conceptually a documentation/project-design methodology.

## §3 — Top-level topics and context containers

The current operational master-folder/chat-project layout is:

```text
AIDE/
├── Core/
├── Principles/
├── Working Practices/
├── Project Design/
├── Build/
├── Capabilities/
├── AI Deployment/
└── Document Methodology/
```

These are **context/storage containers**, selected to make working context coherent and easy to
refresh. They are not semantic ownership boundaries and are not required to map one-to-one to
top-level topics.

A container may hold several top-level topics when those topics benefit from access to the same
context pool. Standing workflow registers therefore anchor to the top-level topic by default,
unless their owner explicitly defines a narrower scope.

The physical Project Design folder has always been:

```text
AIDE/Project Design/
```

Earlier current-document references to `AIDE/Design Project/` or a `Design Project` physical
container were factual documentation/configuration errors, not a historical rename.

Generated common bundles live under the applicable generated/management location (currently
`Documentation/_bundles/` in this repository) and are not authoritative master topics.

Physical handling of Superseded/Archived material follows Working Practices after semantic state is
established by the owning methodology.

## §4 — Side and applicability

**Design side** and **Build side** are working contexts, not ownership silos.

A Standard or Tool may apply on Design, Build or both according to Scope/applicability. Container
placement never substitutes for applicability.

Principles and Working Practices are cross-cutting guidance rather than Design-side or Build-side
owners.

## §5 — Formal identities

Internal topic/source-document names stay readable. Formally referenceable/published/deployed AIDE
artefacts use namespaced `AIDE_` identities where collision is plausible.

A referenceable artefact may expose multiple ordered identities:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

Identity resolves by name before version comparison.

## §6 — Document metadata host/owner boundary

Documentation Methodology owns generic document metadata-container placement/coexistence; each
contributing owner owns its block/property semantics.

```text
Core Identity       → header Identity metadata
AIDE_Tags           → footer Tags metadata
AIDE_Dependencies   → footer Dependencies metadata
AIDE_Migration      → migration semantics / owner-labelled temporary state
DocMeth             → placement, coexistence and document-specific rendering
```

The same host/owner principle applies to owner-defined Index properties/sections: the generic host
does not acquire the contribution's semantics.

## §7 — System bootstrap

AIDE maintains a small stable bootstrap layer through the strongest persistent mechanism available
in each participating AI environment.

The persistent instruction discovers/processes an applicable Bootstrap Profile where available.
The Profile defines the environment startup posture using what/why/where entries. Thin component
Bootstrap Contributions may then perform owner-defined early-session setup/checks. Full operating
material remains lazy and loads when current work requires it.

`{bootstrap}` remains the generic marker for content requiring best-effort early-session discovery.
The marker itself has no component-specific semantics.

No Bootstrap Profile is a valid state; the session continues normally where none is available. One
effective Profile applies by default. Generic profile merging/precedence is not defined.

Platform implementations must not claim stronger startup enforcement than the platform provides.

## §8 — Base guidance and Guidance Profiles

`AIDE_Principles@v1` and `AIDE_WorkingPractices@v1` are base guidance.

More-specific organisation/group/team/user Guidance Profiles may provide small deltas that add,
refine or explicitly override named base guidance. Unmentioned base guidance remains effective.

The shared profile concept is intentionally not promoted into another generic AIDE component yet.
Principles and Working Practices are the demonstrated consumers; broader generalisation requires
additional evidence.

Host/platform instruction priority remains outside AIDE.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: Core_Index_Design_v1, Core_Domain_Design_v2, Core_Bootstrap_Design_v2, Principles_Design_v3, WorkingPractices_Design_v5, ProjectDesign_Design_v2, Build_Design_v4
