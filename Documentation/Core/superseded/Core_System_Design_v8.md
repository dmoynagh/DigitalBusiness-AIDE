# Core System — Design

> **Version 8** (2026-09-01). Reconciles the Review A Core substrate corrections across the
> reference architecture: Domain-owned approved recognition with one generic Item Type projection,
> operational Bootstrap Profile gating, and the logical top-level `DocumentationTopic` seam.
>
> Created: 2026-08-28 | Last modified: 2026-09-01

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
- the optional compact runtime `ItemTypeRegistry` projection.

An Index is authoritative for the items it registers within its scope and for Index-owned
information about those registrations. Registration does not make it authoritative for the
registered item's internals.

Semantic owners may define Item Types, properties and specialised Index sections without
transferring their semantics to Core.

Canonical outcome: `AIDE_Index@v2`.

The optional `ItemTypeRegistry` contains only Domain-neutral Item Type recognition/provision facts.
Direct evaluation of current authoritative Item Type Definitions remains a valid fallback. No Item
Type owner can use its definition or registry metadata to self-grant Domain authority.

A generic Index is **not automatically Domain-defining**.

#### Domain

Domain is the Core-owned system-wide foundation for resolving the named AIDE operating/governance
context relevant to a target when such context is needed. Project Design, Build, Capabilities,
Documentation Methodology, Environment/AI Deployment and future AIDE concerns may consume that
context without redefining Domain behaviour.

Domain publishes and owns the approved Domain recognition set. The current set comprises:

- `DocumentationTopic` where a genuine reusable semantic Item Type owner exists;
- Domain-owned minimum native `Solution` recognition;
- Domain-owned minimum native `Project` recognition; and
- explicit `AIDE_Domain` declaration entries.

For semantic Item Types, Domain may consume recognition directly from the authoritative type
definition or through the generic Domain-neutral `ItemTypeRegistry`; it then independently applies
its approved recognition set. Runtime recognition reuse therefore does not grant Domain authority.

Native Solution/Project systems remain authoritative for their own formats, membership and
internals. Domain owns only the minimum recognition and containment/membership observations it
needs for Domain resolution; it does not invent AIDE Item Type owners for those native structures.

Generic `Index` remains non-Domain-defining. A documentation Index may declare/describe a
`DocumentationTopic` or host Domain-owned configuration for an applicable Domain, but Index
existence alone never establishes Domain context.

No separate Domain-specific recognition registry is part of the current architecture. Safe runtime
caches remain derived optimisation only.

Domain also owns a narrow propagation-stop boundary. `Propagation: Stop` terminates an enclosing
Domain's propagation through a recognised/registered structural boundary and independent resolution
continues below it. That independent resolution may find another Domain, but no parent/child Domain
semantics, inheritance, merge, settings propagation or precedence are defined.

Detailed semantics are owned by `Core_Domain_Design_v3`; canonical outcome:
`AIDE_Domain@v3`.

#### Bootstrap

Bootstrap is the stable activation seam between persistent platform-level instructions and the
deployable guidance, Standards, Tools and other AIDE material available to a specific environment.

The layered model is:

```text
persistent platform bootstrap
        ↓
resolve one effective Bootstrap Profile, if any
        ↓
establish the Profile startup set
        ↓
process applicable Bootstrap Contributions belonging to that startup set
        ↓
full guidance / Standards / Tools loaded when needed
```

The persistent platform bootstrap is deliberately tiny and changes rarely.

A Bootstrap Profile is environment-specific and identifies only:

```text
WHAT  — identity/material to bring into the startup set
WHY   — concise rationale for including it
WHERE — how the authoritative deployed material can be resolved
```

`WHY` is human/AI-readable rationale, not executable applicability syntax. Bootstrap does not create
a second Scope language.

One effective Profile applies by default. **No Profile is valid and means there is no
Profile-selected AIDE startup set; deployed AIDE Bootstrap Contributions are not automatically
processed merely because they are physically available.** Physical deployment is not startup
selection.

Components may own thin, separately deployable Bootstrap Contributions where there is a
demonstrated early-session need. A Contribution is startup-eligible only when its owning material/
capability is selected by the effective Profile, absent a future explicitly defined persistent
primitive.

Bootstrap Contributions are order-independent. A peer Contribution may not require another peer to
run first or depend on peer startup side effects. Required material presence uses the normal
Dependencies mechanism rather than Contribution ordering.

`{bootstrap}` remains deliberately primitive pre-capability/pre-Index discovery. Bootstrap cannot
assume richer Index/Item Type machinery is already available to discover itself, so `{bootstrap}`
and Item Type recognition remain intentionally separate.

Startup-required presence uses the normal Dependencies mechanism rather than a Bootstrap-specific
dependency language. Bootstrap may surface a missing requirement but does not install, update or
reconcile it.

Bootstrap/Profile artefacts may themselves be deployed through AI Deployment. Bootstrap does not
govern Deployment.

Detailed semantics: `Core_Bootstrap_Design_v3`; canonical outcome: `AIDE_Bootstrap@v2`.

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

Documentation Methodology **consumes `AIDE_Index@v2`** for generic Index/Item/Item Type semantics.
It no longer owns generic Index behaviour. It remains owner of documentation-specific additions
such as Document Register, topic declarations, custom document types, asset/unmanaged records and
the `DocumentationTopic` semantic Item Type.

`DocumentationTopic` means the **logical top-level-topic documentation boundary/scope**. The
governing Index document declares/describes that logical Item; the Markdown file does not become
the semantic boundary merely because it carries the declaration. Subtopics are subordinate
structures inside that top-level topic and do not become independent `DocumentationTopic` Items
merely because they have their own Design/Decisions/Index state.

This semantic Item Type ownership does not grant Domain authority. Core/Domain alone decides that
`DocumentationTopic` is in the approved Domain recognition set.

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

The persistent instruction resolves one effective Bootstrap Profile where available. The Profile
selects the startup set using `What` entries, with non-executable `Why` rationale and `Where`
locators. Only applicable Bootstrap Contributions belonging to selected owning material/capabilities
are processed automatically.

No Bootstrap Profile is a valid state. It means no Profile-selected AIDE startup set and therefore
no automatic processing of unrelated deployed AIDE Contributions merely because they are
available. One effective Profile applies by default; generic profile merging/precedence is not
defined.

Bootstrap Contributions are order-independent and cannot rely on peer startup side effects.
`{bootstrap}` remains the generic best-effort pre-Index discovery marker; the marker itself has no
component-specific semantics and does not depend on Item Type recognition for initial discovery.

Full operating material remains lazy and loads when current work requires it.

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
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v2
References: Core_Index_Design_v2, Core_Domain_Design_v3, Core_Bootstrap_Design_v3, Principles_Design_v3, WorkingPractices_Design_v5, ProjectDesign_Design_v2, Build_Design_v4
