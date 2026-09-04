# Core Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 1** (2026-08-31). First independently versioned Core Binder; assembles the generic Index, Domain v2 and corrected Foundation state.

## Binder manifest

- `Core_Index_v4.md` — sha256 `bdc00300bbad`
- `Core_System_Design_v7.md` — sha256 `6ee2792ab67e`
- `Core_System_Decisions_v6.md` — sha256 `4204f66ae929`
- `Core_Index_Design_v1.md` — sha256 `f86b5a6f9d35`
- `Core_Index_Decisions_v1.md` — sha256 `c46e8926b98c`
- `AIDE_Index_Standard_v1.md` — sha256 `a85fc86937fa`
- `Core_Domain_Design_v2.md` — sha256 `1d5d708d1d35`
- `Core_Domain_Decisions_v2.md` — sha256 `d5a49328b5cc`
- `AIDE_Domain_Standard_v2.md` — sha256 `61a6d571a5c9`
- `Core_Bootstrap_Design_v2.md` — sha256 `ac7505e45cb1`
- `Core_Bootstrap_Decisions_v2.md` — sha256 `4535c9d7e0a3`
- `AIDE_Bootstrap_Standard_v1.md` — sha256 `ff71a00d2eda`

---

<!-- BEGIN SOURCE: Core_Index_v4.md -->
# Core — Index

> **Version 4** (2026-08-31). Adopts the generic Core Index framework, registers Index as a Core
> foundation, and corrects the Project Design physical/container mapping.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

`{scope: "AIDE/Core", type: DocumentationTopic}`

## Contents

- **Core** — AIDE system-wide foundations and reference architecture.
  - **Index** — generic hierarchical item registration and Item Type framework.  
    `{design: Core_Index_Design_v1, standard: AIDE_Index@v1}`
  - **Domain** — contextual operating/governance boundary resolution.  
    `{design: Core_Domain_Design_v2, standard: AIDE_Domain@v2}`
  - **Bootstrap** — stable startup activation seam and Profile/Contribution model.  
    `{design: Core_Bootstrap_Design_v2, standard: AIDE_Bootstrap@v1}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Core | None | `Core` | independent | expanded |
| Index | Core | `Core_Index` | inherits | expanded |
| Domain | Core | `Core_Domain` | inherits | expanded |
| Bootstrap | Core | `Core_Bootstrap` | inherits | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Core_Index` | v4 | Index | Current |
| `Core_System_Design` | v7 | Design | Current |
| `Core_System_Decisions` | v6 | Decisions | Current |
| `Core_Index_Design` | v1 | Design | Current |
| `Core_Index_Decisions` | v1 | Decisions | Current |
| `AIDE_Index_Standard` | v1 | Standard | Current; identity `AIDE_Index@v1` |
| `Core_Domain_Design` | v2 | Design | Current |
| `Core_Domain_Decisions` | v2 | Decisions | Current |
| `AIDE_Domain_Standard` | v2 | Standard | Current; identity `AIDE_Domain@v2` |
| `Core_Bootstrap_Design` | v2 | Design | Current |
| `Core_Bootstrap_Decisions` | v2 | Decisions | Current |
| `AIDE_Bootstrap_Standard` | v1 | Standard | Current; identity `AIDE_Bootstrap@v1` |

### Current context/container map

Chat-project/master-folder/container boundaries are working/context boundaries. They may contain one or more top-level
topics and are not semantic ownership boundaries.

| Canonical concern | Current master folder/container |
|---|---|
| Core | `AIDE/Core/` |
| Principles | `AIDE/Principles/` |
| Working Practices | `AIDE/Working Practices/` |
| Project Design | `AIDE/Project Design/` |
| Build | `AIDE/Build/` |
| Capabilities | `AIDE/Capabilities/` |
| AI Deployment | `AIDE/AI Deployment/` |
| Documentation Methodology | `AIDE/Document Methodology/` |
| Generated common bundles | `Documentation/_bundles/` or current environment equivalent |

The canonical and physical name for Project Design is **Project Design**. Earlier current-document
references to `Design Project` were documentation/configuration errors, not a historical folder
rename.

### Local configuration

None.

### Assets

None.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: Core_System_Design_v7, Core_Index_Design_v1, Core_Domain_Design_v2, Core_Bootstrap_Design_v2
<!-- END SOURCE: Core_Index_v4.md -->

---

<!-- BEGIN SOURCE: Core_System_Design_v7.md -->
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
<!-- END SOURCE: Core_System_Design_v7.md -->

---

<!-- BEGIN SOURCE: Core_System_Decisions_v6.md -->
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
<!-- END SOURCE: Core_System_Decisions_v6.md -->

---

<!-- BEGIN SOURCE: Core_Index_Design_v1.md -->
# Core Index — Design

> **Version 1** (2026-08-31). Establishes Index as a generic Core-owned structural register and
> extension host, separate from Documentation Methodology's documentation-specific Index usage.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Index is the generic AIDE mechanism for maintaining an authoritative, human-readable view of
significant items within a defined boundary.

Core/Index owns:

- the meaning of an Index;
- Index scope/identity;
- hierarchical item registration;
- the generic Item and Item Type Definition contracts;
- physical `Folder` / `File` fallback classification;
- containment/delegation boundaries;
- owner-defined extension/property hosting;
- generic authority and update-preservation rules; and
- the compact runtime Item Type Registry projection.

Core/Index does **not** own:

- the internals of registered items;
- document lifecycle/type semantics;
- Domain-defining authority;
- native solution/project membership semantics;
- arbitrary owner-specific properties/sections; or
- a universal metadata/query/configuration language.

The defining authority boundary is:

> **An Index is authoritative for the items it registers within its scope and for the information
> it owns about those registrations. Registration does not make the Index authoritative for the
> registered item's internals.**

This Design produces:

```text
AIDE_Index@v1
```

## §2 — Level 1 model

An Index is:

> **an authoritative, hierarchical view of significant items within a defined boundary, together
> with information and optional specialised sections applicable to that boundary.**

The minimum model is deliberately small:

```text
Index
├── identity / scope
├── Contents
│   └── registered Items arranged by containment/location
└── optional owner-defined extension sections
```

The Contents view is not required to enumerate every physical file or folder. It registers items
whose existence/location/properties are useful to the Index's purpose and may stop at delegated or
self-describing boundaries.

## §3 — Scope and identity

Every Index states what it represents. Examples include:

- a repository;
- a folder/container;
- a documentation top-level topic/corpus;
- a top-level topic or branch;
- another owner-defined structural boundary.

The Index's identity/scope is not limited to AIDE documentation.

An Index may be colocated with what it represents, but physical filename/location is not its entire
semantic identity.

## §4 — Contents and Item

`Contents` is the generic structural view.

Items are arranged by **containment/location**, not grouped primarily by type.

A registered Item may expose, as applicable:

- display name / identity;
- locator/path, often implicit from the tree;
- semantic Item Type(s);
- concise human description;
- compact owner-defined properties/details; and
- a pointer/delegation to another self-describing boundary.

Type is metadata about an item, not the organising principle of the hierarchy.

Mixed item kinds may coexist in one Contents tree: folders, projects, files, documents, assets,
references, native structures or another significant item.

A project/container root locator is **not universally required**. A self-describing project folder
may be located by the parent Index and then resolve its own internal root/index from within that
folder.

## §5 — Item Type Definition

An **Item Type Definition** supplies a reusable semantic classification for Items.

The generic contract says only:

1. **how an item can be identified as the type**; and
2. **what becomes available/applicable once identified.**

Conceptual form:

```yaml
ItemType:
  Name: DocumentationTopic
  Identify: <declarative recognition evidence>
  Provides: <properties / semantic capabilities made available>
```

The type owner defines its recognition and provisions. The Index framework does not reinterpret
those semantics.

Recognition should prefer cheap, observable evidence such as:

- explicit declared identity/type;
- filename/extension/name pattern;
- structural marker;
- authoritative native relationship; or
- simple container-content evidence.

Do not turn Item Type Definition into arbitrary executable matching logic.

### Composability, not inheritance

An Item may satisfy more than one semantic Item Type.

For example, one physical directory might be both:

```text
Folder
DocumentationTopic
GitRepository
```

No Item Type inheritance/class hierarchy is defined in v1. Add one only if a demonstrated need
cannot be represented by independent composable types.

## §6 — Physical fallback

Physical form and semantic type are separate.

When no semantic Item Type applies:

```text
physical directory → Folder
physical file      → File
```

`Folder` and `File` are immediate Core fallback types. They do not imply richer semantics.

An Item may retain its physical classification while also satisfying one or more semantic types.

## §7 — Owner-defined properties and extension sections

Index is an extensible host.

A semantic owner may define:

- properties on Items; and/or
- specialised Index sections/registers.

The owner defines the field names, meaning, permitted values, validation and lifecycle of its
contribution. Index owns only hosting/coexistence and generic structural rules.

Examples include:

- Documentation Methodology → Document Register, topic declarations, custom document types;
- Domain → Domain-owned Index properties/settings;
- Dependencies → dependency-related contribution where one is demonstrated;
- another standard → an Item Type or specialist register.

Specialised registers are added only when their independent use justifies them. The existence of
one projection does not require a generic multi-view/query mechanism.

## §8 — Delegation and self-describing boundaries

An Index may stop at an item that is independently self-describing.

A repository Index can therefore state that a documentation top-level topic exists, describe it
and locate it, then stop. That topic's governing Index/native structure becomes authoritative for
its internals.

Delegation means:

```text
parent Index
  authoritative for registration/location of child boundary
        ↓
child Index / self-describing structure
  authoritative for its own internal registrations
```

Do not duplicate the entire child registry in the parent merely because it is technically
reachable.

## §9 — Representation

The canonical human/AI Index representation is Markdown using:

- headings and lists for structural/hierarchical views;
- YAML flow mappings/sequences for compact structured properties; and
- tables only where an owner-defined section is sufficiently homogeneous/regular for a table to
  improve readability.

Example:

```markdown
- **Capabilities/** — Reusable AIDE capability infrastructure.  
  `DocumentationTopic`  
  `{topics: [Capabilities]}`
```

Use standard YAML flow syntax rather than inventing an AIDE-specific mini-language.

HTML may be generated for presentation, but is not the canonical Index source representation.

## §10 — Update/reconciliation ownership

Index updates are contribution-preserving.

An updater changes only information it owns or is explicitly authorised to reconcile. In
particular:

- discovery may update observed locator/existence facts;
- an Item Type owner may update its own type-derived properties;
- Domain may update Domain-owned properties;
- Documentation Methodology may update its Document Register; and
- human-authored descriptions remain untouched unless explicitly authored/updated.

Unknown owner properties/sections are preserved.

Do not regenerate the whole Index in a way that destroys authored descriptions or another owner's
contributions merely because one derived property changed.

## §11 — Runtime Item Type Registry

Full Index/Item Type source material is not required on every classification operation.

A runtime/build environment may compile loaded Item Type Definitions into a compact
`ItemTypeRegistry` containing only the recognition/provision facts needed for the current work.

Performance posture:

1. load/compile definitions once per relevant context;
2. evaluate cheap selectors first;
3. perform expensive inspection only when needed;
4. lazily load richer type information for enrichment;
5. cache unchanged resolution where safe; and
6. use immediate `Folder` / `File` fallback where no semantic type matches.

The registry is a derived optimisation, not the authoritative source of type semantics.

## §12 — Relationship to Domain

Generic Index existence does **not** automatically establish a Domain.

Core/Domain owns which semantic Item Types are Domain-defining/Domain-capable and may compile a
thin Domain Recognition Registry from those approved types.

This prevents any arbitrary Item Type owner from acquiring Domain authority by setting a flag on
its own definition.

Index may host Domain-owned properties without owning Domain semantics.

## §13 — Relationship to Documentation Methodology

Documentation Methodology consumes the generic Index framework for documentation corpora.

It retains ownership of documentation-specific concerns including:

- DocumentationTopic Item Type semantics;
- topic/document organisation;
- Document Register;
- custom document type registration;
- assets/unmanaged document-corpus records; and
- document lifecycle/current-version resolution.

Documentation Methodology no longer owns generic Index semantics.

## §14 — Deliberately absent from v1

Do not introduce without a demonstrated need:

- Item Type inheritance;
- universal metadata ontology;
- arbitrary executable type matching;
- generic item query language;
- mandatory explicit registration of every physical item;
- HTML as canonical Index source;
- mandatory project-root pointers; or
- automatic recursion through self-describing boundaries.

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: Core_Domain_Design_v2, DocumentationMethodology_Design_v18
<!-- END SOURCE: Core_Index_Design_v1.md -->

---

<!-- BEGIN SOURCE: Core_Index_Decisions_v1.md -->
# Core Index — Decisions

> **Version 1** (2026-08-31). Records the blank-sheet decisions establishing the generic AIDE
> Index and Item Type framework in Core.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Index is a generic Core mechanism

**Decision.** Move generic Index semantics to Core. Documentation Methodology remains a consumer
and extension owner for documentation-specific Index behaviour.

**Reason.** Repositories, projects, documents, native structures and future contexts all need the
same basic structural registration concept. Keeping generic Index inside Documentation Methodology
would make a broadly useful system primitive documentation-specific.

## D2 — Index is an authoritative hierarchical register, not a flat type catalogue

**Decision.** Index organises significant Items by containment/location and is authoritative for
its registrations and Index-owned information.

**Rejected alternative.** Use a flat table grouped by item type. Rejected because mixed structural
containers are naturally navigated hierarchically and type is metadata rather than the primary
location relationship.

## D3 — Registration does not transfer authority over item internals

**Decision.** Registering an item gives the Index authority only over the registration facts it
owns. The registered item/native owner remains authoritative for its internals.

**Reason.** Without this boundary, a repository Index could accidentally become authoritative over
project internals, solution membership or document semantics merely by listing them.

## D4 — Contents may stop at self-describing boundaries

**Decision.** A parent Index need not recursively enumerate an independently self-describing child
container. It locates/describes the boundary and delegates internal discovery.

**Reason.** This keeps hot/high-level Indexes small and avoids duplicate registries.

## D5 — Item Type is the generic semantic classification mechanism

**Decision.** An Item Type Definition states only how the type is identified and what it provides
once identified.

**Reason.** This is sufficient to support semantic types such as DocumentationTopic, solution or
future domain-specific structures without building a universal object model.

## D6 — Prefer composable types over inheritance

**Decision.** An Item may satisfy multiple semantic Item Types. No generic inheritance hierarchy is
introduced in v1.

**Reason.** Physical/semantic classifications overlap naturally and current use cases do not need
class hierarchy machinery.

## D7 — Folder and File are immediate fallbacks

**Decision.** A physical directory/file with no richer semantic classification resolves to
`Folder`/`File`.

**Reason.** The framework remains useful without requiring a formal type definition for every
physical item.

## D8 — Index hosts owner-defined extensions without absorbing their semantics

**Decision.** Semantic owners may define Item properties and specialised Index sections. Core Index
owns only generic hosting/coexistence.

**Reason.** This lets Documentation Methodology, Domain and future owners extend one structural
surface without turning Index into a generic configuration authority.

## D9 — Markdown + YAML flow is the canonical representation

**Decision.** Use Markdown hierarchy plus compact YAML flow mappings/sequences. Tables remain valid
for homogeneous owner-defined sections.

**Rejected alternative.** Canonical HTML. Rejected because it adds context/token bloat and depends
on renderer support without improving the machine-readable source contract.

## D10 — Runtime type resolution uses a thin compiled registry

**Decision.** Item Type Definitions may be compiled into a compact runtime registry; cheap
recognition runs before expensive enrichment and unchanged results may be cached.

**Reason.** Domain and other frequently invoked classification should not require loading or
scanning every full Standard on every operation.

## D11 — Generic Index is not Domain-defining by default

**Decision.** Domain-defining status is assigned by Core/Domain to approved semantic Item Types,
not by generic Index existence or arbitrary type-owner declaration.

**Reason.** Domain formation changes system governance context and therefore requires restricted
system-level authority.

## D12 — Update operations preserve other owners' contributions

**Decision.** An updater changes only the fields/sections it owns or is authorised to reconcile.
Unknown owner contributions and human-authored descriptions are preserved.

**Reason.** A shared Index becomes unsafe if a generated update can erase unrelated semantic or
human information.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Core_Index_Design_v1
References: Core_Domain_Decisions_v2, DocumentationMethodology_Decisions_v19
<!-- END SOURCE: Core_Index_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Index_Standard_v1.md -->
# AIDE Index — Standard

> **Identity:** `AIDE_Index@v1`
> **Common name:** Index
> **Version 1** (2026-08-31). First canonical generic Index/Item Type contract.
>
> **Default weight:** Requirement

## Purpose

Provide one generic AIDE mechanism for maintaining an authoritative hierarchical view of
significant items within a defined boundary while allowing specialised owners to add their own
properties/registers without transferring semantic ownership.

## Index contract

An Index shall identify its scope and provide a hierarchical `Contents` view of the significant
Items it registers.

The Index is authoritative for:

- which items it registers within that scope;
- their Index-owned locator/containment facts; and
- Index-owned information attached to those registrations.

Registration does **not** make the Index authoritative for a registered item's internals.

`Contents` may intentionally omit insignificant physical items and may stop at a delegated or
self-describing boundary.

## Item

A registered Item may expose, as applicable:

```text
name / identity
locator / containment
semantic Item Type(s)
description
compact owner-defined properties
delegated/self-describing boundary pointer
```

Arrange Items primarily by containment/location. Type is metadata, not the primary hierarchy.

## Item Type Definition

An Item Type Definition has two semantic jobs:

1. identify whether an item satisfies the type; and
2. state what the type provides/enables when identified.

Use declarative observable recognition evidence. Prefer cheap evidence such as explicit identity,
name/extension, structural marker or authoritative native relationship before expensive content
inspection.

Do not use the generic Item Type contract as arbitrary executable classification logic.

An Item may satisfy several independent semantic Item Types. No generic type-inheritance hierarchy
exists in v1.

## Physical fallback

If no richer semantic type applies:

```text
physical directory → Folder
physical file      → File
```

Physical classification may coexist with semantic Item Types.

## Extension ownership

An owner may define Item properties or specialised Index sections/registers.

The contributing owner owns:

- field/section meaning;
- values/schema;
- validation;
- lifecycle; and
- update rules.

Index owns generic hosting/coexistence only.

An Index updater shall preserve properties/sections it does not own unless explicitly authorised to
reconcile them.

## Delegation

A parent Index may register and locate a self-describing child boundary without duplicating its
internal registry. The parent remains authoritative for the parent registration; the child/native
owner is authoritative internally.

## Canonical representation

Use Markdown as the canonical human/AI source representation.

Prefer:

- headings/lists for hierarchy;
- YAML flow mappings/sequences for compact structured Item properties; and
- tables for regular homogeneous extension sections.

Do not invent an AIDE-only mini-language where standard YAML flow syntax suffices.

HTML may be generated as presentation but is not canonical source in v1.

## Runtime Item Type Registry

A runtime/build environment may compile available Item Type Definitions into a compact registry.

Use this order where practical:

1. explicit/cheap selectors;
2. structural/native relationship checks;
3. expensive inspection only if necessary;
4. lazy enrichment after classification; and
5. cached reuse for unchanged items where safe.

The compiled registry is derived optimisation state, not semantic authority.

## Domain boundary

Generic Index existence does **not** establish a Domain.

`AIDE_Domain` owns the approved Domain-defining/Domain-capable Item Type set and any thin Domain
Recognition Registry derived from it. An Item Type owner cannot grant itself Domain authority by
setting a local flag.

## Deliberately absent

No v1 requirement exists for:

- type inheritance;
- universal metadata ontology;
- generic query language;
- explicit registration of every file/folder;
- mandatory root pointer for every project/container; or
- automatic recursion into self-describing child boundaries.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: Core_Index_Design_v1, Core_Domain_Design_v2
<!-- END SOURCE: AIDE_Index_Standard_v1.md -->

---

<!-- BEGIN SOURCE: Core_Domain_Design_v2.md -->
# Core Domain — Design

> **Version 2** (2026-08-31). Reconciles the established Domain model with the generic Core
> Index/Item Type framework, restricts Domain-capable assignment to Core/Domain, adds a thin
> recognition projection and adds an explicit propagation-stop boundary without introducing child
> Domain inheritance/merge semantics.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Domain defines the common AIDE concept used to identify the named operating/governance context
within which work is being performed.

A **Domain is a named AIDE operating/governance context**. It is contextual and semantic; it is not
inherently a file and is not an AIDE activation switch.

Core/Domain owns:

- the meaning and identity of Domain;
- which semantic Item Types are approved as Domain-capable/Domain-defining;
- the Domain-relevant structural relationships required for resolution;
- implicit versus explicit Domain formation;
- target-based discovery, resolution and deterministic ambiguity/failure behaviour;
- Domain metadata/settings-host and `Branch` conventions;
- Domain propagation-stop semantics; and
- the thin Domain Recognition Registry projection used for efficient hot-path discovery.

Domain does **not** own the full semantics of an approved Item Type/native structure. Generic
Index/Item/Item Type semantics belong to Core/Index; the Item Type owner remains authoritative for
its recognition and provisions. Domain alone decides whether that type may establish or participate
in Domain resolution.

This Design produces:

```text
AIDE_Domain@v2
```

## §2 — Level 1 model and authority seam

```text
target / focus
    ↓
recognise available Items / semantic Item Types
    ↓
Domain-approved type evidence + structural relationships
    ↓
explicit declaration / containment / co-root evaluation
    ↓
Domain propagation boundary where present
    ↓
effective Domain | No Domain | unresolved/error
```

The previous architecture named `AIDE Index`, solution, project and explicit declaration directly
inside Domain. The v2 refinement separates **type recognition** from **Domain authority**:

```text
Item Type owner
  → what this item is / how it is recognised / what it provides

Core/Domain
  → whether this semantic type is eligible to establish/participate in a Domain
```

This prevents an arbitrary local Item Type or generic Index from silently creating a governance
boundary while preserving the existing natural Domain cases.

## §3 — Applicability

Apply when an operation needs Domain context for a target, focus, setting lookup, navigation,
composition or another Domain-aware behaviour.

```yaml
Scope:
  Context: >
    Apply when the current operation needs to resolve, declare, name, navigate or consume Domain
    context or Domain-hosted settings for a target/focus.
```

Do not resolve Domain merely because an artefact exists. One session may work across several
Domains or with material that has no Domain.

## §4 — Domain model

A **Domain is a named AIDE operating/governance context**.

A Domain may be:

```text
implicit  — established from a Domain-approved semantic Item Type / authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify recognised roots
```

Generic Item/Item Type semantics belong to `AIDE_Index@v1`. A type owner defines what an Item Type
is, how it is identified and what it provides. **Only Core/Domain decides whether a semantic Item
Type is permitted to establish/participate in Domain resolution.**

An arbitrary Item Type cannot self-assign Domain authority, and a generic Index is not
Domain-defining merely because it exists.

Initial Domain recognition continues to cover the demonstrated structural roles represented by the
current system—documentation top-level topic/Index structures, native solution structures, native
project structures and explicit AIDE Domain declarations—but they are consumed through
Domain-approved semantic type/recognition entries rather than a rule that every Index/solution/
project-shaped thing automatically creates Domain authority.

A repository/worktree remains a discovery boundary, not an implicit Domain type.

## §5 — Natural containment

Authoritative structural containment prevents a contained Domain-capable item from establishing a
second implicit Domain.

- a project that is an authoritative member of a solution remains in the solution Domain;
- a delegated/self-describing documentation topic remains in its enclosing effective Domain unless
  propagation is explicitly stopped; and
- another Domain-capable Item inside an effective Domain does not create a child Domain merely
  because it could establish a root when isolated.

Structural children do not create child Domains implicitly. Child-Domain inheritance, settings
propagation, precedence and parent/child composition remain undefined in v2.

### Domain propagation stop

Domain may mark a structural boundary as **Propagation: Stop**. The effect is deliberately narrow:

> an enclosing Domain does not propagate through that boundary; content below it must resolve
> Domain independently.

This does **not** create a child Domain and does not define inheritance, merge or precedence.

Where the boundary is represented as an Index Item, use the Domain-owned contribution, for example:

```yaml
Domain:
  Propagation: Stop
```

Equivalent representation may be defined for another Domain-aware structure. The semantic meaning
belongs to Domain; Index merely hosts the property.

## §6 — Co-root recognised structures

Evaluate recognised structures sharing a physical root by authoritative identity and structural
relationships, not proximity alone.

### Matching identity

Co-root structures with matching authoritative identities form one implicit Domain.

```text
Foo.sln + Foo_Index  → Foo Domain
```

An available declared Index structural/topic identity is authoritative over filename-only matching.
When a matching Index and solution/project represent one Domain, the Index is the preferred
AIDE-controlled Domain metadata/settings host. The native solution/project retains authority over
its own membership and semantics.

### Different identity

Co-root recognised structures with different identities remain separate implicit Domains by
default.

```text
Foo.sln + Womble_Index  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj → Foo Domain + Bar Domain
```

Multiple standalone projects in one folder with no enclosing solution are therefore separate
Domains. If this natural interpretation is not intended, use `AIDE_Domain.yaml` rather than adding
special-case inference.

## §7 — Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a solution remains authoritative for solution/project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native solution/project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## §8 — Domain identity and references

An implicit Domain takes its current name/identity from the authoritative recognised structure
that establishes it. Use authoritative declared/native identity when available; filename matching
is only a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names for navigation, cross-Domain
references, composition, provenance or other cases where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## §9 — Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally
wrong—for example to compose several solutions/projects/Indexes, combine differently named roots,
or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Type: Solution
        Path: Product.sln
      - Type: Index
        Path: Product_Index_v1.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Declaration fields

- `Schema` — required declaration-container schema identity; v1 value is `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of recognised roots explicitly composed/clarified by the
  entry.
- `Type` — one of the v2 Domain-approved root roles represented by `Index`, `Solution`, or `Project` for each explicit root; the resolver maps that role to approved semantic recognition rather than granting authority from the token alone.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

The explicit Domain declaration itself is Domain-capable, but its `Roots` identify the recognised
structures whose natural interpretation it composes or clarifies. Co-location of two Domain entries
inside one file creates no relationship between them.

A valid explicit declaration may override the natural implicit grouping of its listed roots. It
does not recreate or replace their internal registries or native membership rules.

## §10 — Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

Preferred authoritative hosts are:

```text
Index-backed implicit Domain
→ root Index local configuration may host Domain metadata/settings

matching solution/project + Index
→ Index is the preferred AIDE Domain metadata/settings host

explicit Domain
→ the Domain entry in AIDE_Domain.yaml hosts Domain metadata/settings
```

Where a root Index hosts Domain metadata/settings, expose one Domain configuration mapping in the
Index's local configuration using the shared field meanings:

```yaml
Domain:
  Aliases: [PreviousName]
  Settings:
    SomeSetting: <owner-defined value>
  Branches:
    - Branch: docs/api
      Settings:
        SomeSetting: <owner-defined value>
```

`Aliases`, `Settings` and `Branches` are optional. The Domain name is inherited from the Index's
authoritative structural/topic identity and `Roots` are not repeated. Core/Index owns generic Index hosting/representation; Documentation Methodology owns any
documentation-specific Index sections. Domain owns the meaning of this Domain configuration payload.

For a solution/project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit `AIDE_Domain.yaml` representation rather than modifying the native format solely to carry
AIDE configuration.

## §11 — Domain Recognition Registry

Runtime Domain discovery should not load every Standard/Item Type definition for every path step.
A build/runtime environment may compile the Domain-approved type assignments into a thin
`DomainRecognitionRegistry` containing only the cheap signatures/relations required for Domain
discovery.

Rules:

- the registry is an optimisation/projection, not the source of Domain authority;
- Core/Domain approval remains authoritative;
- load/compile definitions once per relevant context;
- prefer explicit/native/name/extension/marker evidence before expensive content inspection;
- cache unchanged resolution where safe; and
- if a registry entry cannot be traced to a currently approved semantic type/recognition rule, fail
  or refresh rather than silently granting Domain authority.

## §12 — Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. A nearby project, solution or Index is provisional until applicable enclosing evidence has
been checked.

Do **not** use “nearest marker wins”. Physical ancestry is a discovery path, not proof of
composition.

### Discovery boundaries

Stop upward discovery at the nearest meaningful operational boundary available to the current
context, such as:

- an explicitly supplied discovery boundary;
- workspace/container root;
- repository/worktree root;
- user Documents root;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- another recognised user/application storage root; or
- filesystem/mount root as fallback.

A discovery boundary limits search only. A valid explicit Domain declaration may reference roots
beyond that boundary where the environment can resolve those references.

## §13 — Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing recognised Domain evidence within that boundary, including
   applicable `AIDE_Domain.yaml` declarations and authoritative containment/membership relations.
3. Resolve explicit Domain claims applicable to the target. A valid unambiguous explicit claim
   supplies the effective Domain and may clarify/override the natural grouping of its declared
   roots.
4. Before propagating an enclosing Domain through a structural boundary, apply any Domain-owned
   `Propagation: Stop` declaration. If propagation is stopped, disregard the enclosing Domain for
   content below that boundary and continue resolution independently; the stop does not itself
   create a Domain.
5. Otherwise apply authoritative containment: a contained Domain-capable structure inherits the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate co-root independent recognised roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining independent recognised root, return that
   implicit Domain.
8. If no Domain-capable structure applies, return `No Domain context`.
9. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
   return an unresolved/error result rather than merging, ranking or guessing.

## §14 — Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership without clearly
  expressing the intended override;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## §15 — Ownership boundaries

- **Core/Domain** owns this common context/resolution/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Core/Index** owns generic Index/Item/Item Type behaviour. **Documentation Methodology** owns documentation-specific Index extensions and the `DocumentationTopic` semantic type.
- **Project/solution systems** own native membership and project/build-system semantics.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## §16 — Deliberately absent

The following are not defined by this Standard:

- implicit or generic child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository-as-Domain merely because a repository exists;
- a generic settings precedence/inheritance engine;
- a Domain-specific Tool;
- broad exclusion syntax to counteract normal defaults; or
- platform-specific parser machinery beyond what is required to observe the recognised structures.

If a demonstrated use case later requires one of these mechanisms, change Domain Design first and
produce a later Standard release through the normal capability-production path.

## §17 — Design constraints / deliberately deferred

The v2 architecture deliberately does not add child-Domain inheritance/override/merge,
parent/child settings propagation, arbitrary nested Domain precedence, repository-as-Domain merely
because a repository exists, a generic settings precedence engine, arbitrary self-declared
Domain-capable Item Types, or broad platform parser machinery beyond the recognition contracts
needed by approved types.

The propagation-stop feature is intentionally not a partial inheritance system: it only prevents an
enclosing Domain from flowing through a marked boundary.

## §18 — Success signals

The model is successful when the same observable structures resolve consistently across AIDE
surfaces; generic Indexes can exist without accidentally creating Domains; simple documentation
topics/solutions/projects still need no explicit Domain file where their approved structural type
is sufficient; explicit composition remains available where natural structure is wrong; Domain
recognition can be evaluated cheaply; and ambiguity fails visibly rather than being hidden by
precedence/merge inference.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: Core_Index_Design_v1, Core_Domain_Decisions_v2, DocumentationMethodology_Design_v18
<!-- END SOURCE: Core_Domain_Design_v2.md -->

---

<!-- BEGIN SOURCE: Core_Domain_Decisions_v2.md -->
# Core Domain — Decisions

> **Version 2** (2026-08-31). Preserves the v1 Domain decision history and records the Item Type recognition boundary, Domain-owned approval/registry and propagation-stop model.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Domain is redesigned from a blank sheet

**Decision.** The current Domain model has no compatibility obligation to the earlier
`AIDE_Domain` design/decision corpus.

**Reason.** The earlier model was never implemented or deployed. Preserving its declaration,
activation, scope, standards-composition or membership mechanisms would add constraints without a
real consumer to protect.

**Consequence.** Earlier Domain documents are historical reasoning only. No migration path,
schema bridge or behavioural compatibility layer is required.

---

## D2 — Domain belongs under Core

**Decision.** Domain is a Core-owned system foundation.

**Reason.** Project Design, Build, Capabilities, Documentation Methodology, Environment/AI
Deployment and future AIDE concerns may all need the same Domain context. No one of those concerns
should own the common boundary model.

**Consequence.** Development/product Domains remain outside the AIDE system tree and consume AIDE;
Core owns only the Domain contract.

---

## D3 — Domain is a semantic context, not inherently a file

**Decision.** A Domain is a named AIDE operating/governance context. It may be implicit or explicit.

**Reason.** Existing structures already provide useful natural boundaries. Requiring a declaration
artefact for every Domain would create ceremony and duplicate information.

**Consequence.** `AIDE_Domain.yaml` is an explicit representation, not a prerequisite for Domain
existence.

---

## D4 — Domain has three demonstrated jobs

**Decision.** Domain exists to provide:

1. a common name/vocabulary for an AIDE operating boundary;
2. a standard Domain settings host/convention; and
3. explicit composition/clarification when native structures do not express the intended Domain.

**Reason.** These are the demonstrated needs not cleanly owned by Index, project/solution or other
existing AIDE mechanisms.

**Consequence.** Do not add Domain machinery where an existing structure already answers the
question.

---

## D5 — Domain owns recognition needed for Domain resolution

**Decision.** The Domain Standard defines the recognised Domain-capable structure types and the
minimum structural relationships needed to resolve them consistently.

Initial types are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

**Reason.** A single deployable Domain Standard should behave the same on Design and Build sides
rather than relying on several separate component-specific resolvers.

**Boundary.** Domain learns only Domain-relevant structure. It does not absorb Documentation
Methodology, build-system or project-system semantics.

---

## D6 — Natural authoritative containment beats local implicit roots

**Decision.** A contained recognised structure inherits its enclosing effective Domain rather than
creating another implicit Domain.

Examples:

- a solution's member project remains in the solution Domain;
- a delegated/child Index remains in the root Index Domain.

**Reason.** The authoritative containment relationship already states the larger structure.
Creating an additional Domain would conflate structural subdivision with governance.

---

## D7 — Structural children never create child Domains implicitly

**Decision.** Child Domains require explicit declaration.

**Reason.** Child Indexes, projects and other contained structures are frequently created for
retrieval, organisation or implementation reasons that do not imply a new governance context.

**Consequence.** Child-Domain inheritance, settings propagation, precedence and nesting remain
undefined until a real use case requires them.

---

## D8 — Matching co-root identities form one implicit Domain

**Decision.** Recognised co-root structures whose authoritative identities match are one implicit
Domain.

Example:

```text
Foo.sln
Foo_Index
→ Foo Domain
```

**Reason.** Same structural root plus matching authoritative identity is strong enough evidence
that the structures describe the same contextual boundary.

**Detail.** Index declared project/topic identity is authoritative over filename-only matching.

---

## D9 — Different co-root identities remain separate Domains

**Decision.** Recognised co-root structures with different identities are separate implicit Domains
unless an explicit Domain declaration says otherwise.

Examples:

```text
Foo.sln + Womble_Index → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj with no solution → two Domains
```

**Reason.** Physical co-location is not composition.

**Consequence.** If the default is not the intended model, `AIDE_Domain.yaml` is the clarification
mechanism rather than adding type-specific exceptions.

---

## D10 — A matching Index is the preferred AIDE Domain metadata/settings host

**Decision.** When an Index and solution/project represent the same Domain, the Index is the
preferred AIDE-controlled Domain metadata/settings host.

**Reason.** AIDE controls the Index representation and can safely extend it without modifying
native project/solution formats merely to carry AIDE settings.

**Boundary.** The Index does not become authoritative over native solution/project membership or
semantics.

---

## D11 — Domain membership is distinct from native/corpus membership

**Decision.** Domain answers "what AIDE operating context does this target belong to?" Native
structures answer their own membership questions.

**Reason.** A solution may define project membership while AIDE documents beside/within the
solution still need the solution Domain context. An Index may define its governed document corpus
without becoming the sole definition of the wider Domain.

**Consequence.** AIDE-governed artefacts inside an unambiguous Domain container may inherit the
Domain even when they are not native solution/project members. Documentation Methodology still
owns document registration/governance.

---

## D12 — Artefacts do not normally carry Domain identity

**Decision.** Domain is contextual, not artefact-owned.

Ordinary documents/files do not normally store:

```text
Domain: Foo
```

**Reason.** It duplicates resolvable context, creates rename maintenance and couples artefacts to a
concept they may never need to use.

**Consequence.** Resolve Domain only when an operation needs Domain context.

---

## D13 — Prefer relative references to "the Domain"

**Decision.** Where the actual Domain name is not semantically important, Standards/documents/tools
refer to the effective `Domain` rather than embedding the current name.

**Reason.** Relative reference is portable and rename-safe.

**Exception.** Explicit names remain appropriate for navigation, cross-Domain references,
composition and provenance where identity matters.

---

## D14 — Renames and aliases belong in Domain metadata

**Decision.** Where rename continuity is needed, the authoritative Domain metadata may record
previous names/aliases.

**Reason.** Names are often used for conversational navigation and reference resolution, while
ordinary member artefacts should not require rewrites after a rename.

**Consequence.** Alias/previous-name schema is part of the Domain Standard/detail, not a
document-by-document migration mechanism.

---

## D15 — `AIDE_Domain.yaml` is the explicit composition/clarification mechanism

**Decision.** Use `AIDE_Domain.yaml` when natural implicit rules do not express the intended
Domain.

**Reason.** A dedicated explicit mechanism is simpler than proliferating exceptions across Index,
solution and project rules.

**Examples.** Compose several solutions/projects/Indexes, combine differently named roots, or
deliberately separate structures that would otherwise resolve together.

---

## D16 — One Domain file may contain multiple independent Domain declarations

**Decision.** One physical `AIDE_Domain.yaml` contains a `Domains` collection and may declare
multiple Domains.

**Reason.** A folder may legitimately contain multiple explicit Domains. Restricting one file to
one Domain would require arbitrary extra filenames or directory structure.

**Consequence.** A Domain entry, not the physical file, is the authoritative individual
declaration. Co-location in one YAML file implies no relationship.

---

## D17 — Domain hosts settings but does not define them

**Decision.** Domain defines the location, format and coexistence conventions for Domain-context
settings. Each setting owner defines its own schema and behaviour.

**Reason.** Domain needs a shared context store, but absorbing Review/Build/Deployment/etc.
configuration semantics would turn it into a generic configuration subsystem.

**Consequence.** Domain does not define setting defaults, validation, precedence, inheritance or
combination rules.

---

## D18 — `Branch` is the structural selector for Domain settings

**Decision.** Settings may be attached to the Domain root or to a Domain-relative structural
`Branch`.

Conceptual form:

```yaml
Branch: docs/api
Settings:
  SomeSetting1:
    ...
  SomeSetting2:
    ...
```

No Branch means Domain-root attachment.

**Reason.** `Scope` is already a defined AIDE applicability concept. `Branch` expresses structural
placement without semantic collision.

**Consequence.** The setting owner decides how declarations found on different Branches combine,
inherit or override, if at all.

---

## D19 — Discovery is target-based, not session-based

**Decision.** Resolve Domain for the current target/focus when needed. Do not assume one session
has one Domain.

**Reason.** A session may work across several Domains or with domainless material.

---

## D20 — Domain discovery searches upward

**Decision.** Starting from the current target/focus, Domain discovery considers available enclosing
paths and recognised structures before allowing a local project/solution/Index to establish an
implicit Domain.

**Reason.** Opening a nested folder or project must not change the effective Domain when a higher
solution or explicit Domain already contains it.

**Consequence.** Do not stop at the nearest marker. Collect enough enclosing evidence to establish
the authoritative effective Domain.

---

## D21 — Upward discovery has meaningful stop boundaries

**Decision.** Upward search stops at the nearest appropriate operational discovery boundary rather
than scanning unbounded ancestors.

Common boundaries include:

- explicit supplied boundary;
- workspace/container root;
- repository/worktree root;
- Documents;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- other recognised user/application storage root; and
- filesystem/mount root as fallback.

**Reason.** Unrestricted ancestor scanning creates surprising governance and accidental matches.

**Consequence.** A discovery boundary limits search only; explicit Domain composition may reference
roots beyond that boundary where supported.

---

## D22 — Repository root is initially a discovery boundary, not an implicit Domain type

**Decision.** Repository/worktree root is not automatically a Domain merely because it is a
repository.

**Reason.** The current demonstrated Domain boundaries are Index, solution, project and explicit
Domain. Repository Domain semantics should be added only if a real case shows value beyond those
structures.

---

## D23 — Ambiguity fails visibly

**Decision.** Domain resolution does not silently merge, rank or guess between contradictory
authoritative claims.

**Reason.** The value of Domain depends on deterministic context resolution.

**Examples.** Conflicting explicit claims, unresolved membership where multiple Domains share a
folder, or broken explicit root references produce an unresolved/error result.

---

## D24 — No Domain is a valid state and does not disable AIDE

**Decision.** Absence of a resolvable Domain means only that Domain context/settings are unavailable.

**Reason.** AIDE Standards, Tools, Documentation Methodology and other behaviours can operate
without a Domain.

**Consequence.** Domain is not an AIDE activation switch.

---

## D25 — Domain produces one canonical Standard

**Decision.** The Domain Design is intended to produce `AIDE_Domain@v1` as the common AI-facing
contract.

**Reason.** Domain resolution must behave consistently across Design-side and Build-side contexts.
One canonical Standard is easier to deploy and reason about than separate local implementations.

**Consequence.** No dedicated Domain Tool is currently justified; add one only if a demonstrated
repeatable action requires it.

## D26 — Domain-capable structures are semantic Item Types

**Trigger / problem.** The v1 Domain contract hard-codes `AIDE Index`, solution and project as
recognised structure kinds. The new generic Index framework introduces an owner-defined Item Type
contract that can classify the same structures without Domain duplicating their full recognition
semantics.

**Decision.** Domain consumes semantic Item Types and maintains the system-approved subset that may
establish Domain context.

**Consequence.** Type owners define recognition/provisions; Domain defines only Domain eligibility
and the Domain-relevant structural relationship contract.

## D27 — Generic Index is not automatically Domain-defining

**Trigger / problem.** Once Index becomes generic, many valid Indexes describe repositories,
collections or other boundaries that should not automatically become governance Domains.

**Decision.** Remove generic `Index` from the implicit Domain-defining rule. A semantic type such as
`DocumentationTopic`, a native `Solution`/`Project`, or explicit Domain declaration must supply
the approved boundary evidence.

**Consequence.** An Index may still host Domain metadata/settings for a Domain established by an
approved type. An unusual Index-backed Domain can use an approved semantic type or explicit
`AIDE_Domain.yaml` rather than relying on generic Index existence.

## D28 — Domain-defining assignment is restricted to Core/Domain

**Decision.** Item Type Definitions cannot set their own `domainDefining: true`-style authority.
Domain owns the approved type list and any derived recognition registry.

**Reason.** Domain context affects governance and must not be obtainable as an accidental extension
privilege.

## D29 — Compile a thin Domain Recognition Registry

**Decision.** Runtime implementations may derive a compact recognition projection from the current
Domain-approved Item Types.

**Reason.** Domain resolution sits on a frequent path and should not repeatedly load every full
Standard or type definition.

**Constraint.** The registry is derived optimisation state. Domain Design plus the owning Item Type
Definitions remain authoritative.

## D30 — Add a Domain propagation-stop boundary without designing inheritance

**Trigger / problem.** An enclosing Domain sometimes must not propagate through a structural
boundary, even though the content below may not yet define its own Domain. Waiting for a full child
Domain inheritance model would leave no clean way to express that current need.

**Decision.** Introduce Domain-owned `DomainPropagation: Stop` semantics. It blocks enclosing Domain
propagation below the marked structure and forces independent resolution beneath it.

**Non-goals.** The marker does not create a child Domain, define inheritance/merge, or set generic
precedence.

## D31 — Issue Domain v2

**Decision.** Publish the reconciled contract as `AIDE_Domain@v2` with migration posture `None`.

**Reason.** The semantic recognition/authority model changes, but no existing governed document
requires automatic content transformation merely to adopt the new release. Indexes and Domain
representations are reconciled when next substantively updated or when an operation specifically
needs the v2 semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Core_Domain_Design_v2, AIDE_Index@v1
References: Core_Index_Decisions_v1, DocumentationMethodology_Decisions_v19
<!-- END SOURCE: Core_Domain_Decisions_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Domain_Standard_v2.md -->
# AIDE Domain — Standard

> **Identity:** `AIDE_Domain@v2`
> **Common name:** Domain
> **Version 2** (2026-08-31). Moves Domain recognition onto Domain-approved semantic Item Types, adds a thin recognition projection and a propagation-stop boundary while retaining the established v1 resolution/settings model.
>
> **Default weight:** Requirement

## Purpose

Provide one consistent AIDE contract for identifying the named operating/governance context
relevant to a target, hosting independently owned Domain-context settings, and explicitly
clarifying/composing Domain roots when natural recognised structure is insufficient.

A Domain is contextual and semantic; it is not inherently a file and is not an AIDE activation
switch.

## Applicability

Apply when an operation needs Domain context for a target, focus, setting lookup, navigation,
composition or another Domain-aware behaviour.

```yaml
Scope:
  Context: >
    Apply when the current operation needs to resolve, declare, name, navigate or consume Domain
    context or Domain-hosted settings for a target/focus.
```

Do not resolve Domain merely because an artefact exists. One session may work across several
Domains or with material that has no Domain.

## Domain model

A **Domain is a named AIDE operating/governance context**.

A Domain may be:

```text
implicit  — established from a Domain-approved semantic Item Type / authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify recognised roots
```

Generic Item/Item Type semantics belong to `AIDE_Index@v1`. A type owner defines what an Item Type
is, how it is identified and what it provides. **Only Core/Domain decides whether a semantic Item
Type is permitted to establish/participate in Domain resolution.**

An arbitrary Item Type cannot self-assign Domain authority, and a generic Index is not
Domain-defining merely because it exists.

Initial Domain recognition continues to cover the demonstrated structural roles represented by the
current system—documentation top-level topic/Index structures, native solution structures, native
project structures and explicit AIDE Domain declarations—but they are consumed through
Domain-approved semantic type/recognition entries rather than a rule that every Index/solution/
project-shaped thing automatically creates Domain authority.

A repository/worktree remains a discovery boundary, not an implicit Domain type.

## Natural containment

Authoritative structural containment prevents a contained Domain-capable item from establishing a
second implicit Domain.

- a project that is an authoritative member of a solution remains in the solution Domain;
- a delegated/self-describing documentation topic remains in its enclosing effective Domain unless
  propagation is explicitly stopped; and
- another Domain-capable Item inside an effective Domain does not create a child Domain merely
  because it could establish a root when isolated.

Structural children do not create child Domains implicitly. Child-Domain inheritance, settings
propagation, precedence and parent/child composition remain undefined in v2.

### Domain propagation stop

Domain may mark a structural boundary as **Propagation: Stop**. The effect is deliberately narrow:

> an enclosing Domain does not propagate through that boundary; content below it must resolve
> Domain independently.

This does **not** create a child Domain and does not define inheritance, merge or precedence.

Where the boundary is represented as an Index Item, use the Domain-owned contribution, for example:

```yaml
Domain:
  Propagation: Stop
```

Equivalent representation may be defined for another Domain-aware structure. The semantic meaning
belongs to Domain; Index merely hosts the property.

## Co-root recognised structures

Evaluate recognised structures sharing a physical root by authoritative identity and structural
relationships, not proximity alone.

### Matching identity

Co-root structures with matching authoritative identities form one implicit Domain.

```text
Foo.sln + Foo_Index  → Foo Domain
```

An available declared Index structural/topic identity is authoritative over filename-only matching.
When a matching Index and solution/project represent one Domain, the Index is the preferred
AIDE-controlled Domain metadata/settings host. The native solution/project retains authority over
its own membership and semantics.

### Different identity

Co-root recognised structures with different identities remain separate implicit Domains by
default.

```text
Foo.sln + Womble_Index  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj → Foo Domain + Bar Domain
```

Multiple standalone projects in one folder with no enclosing solution are therefore separate
Domains. If this natural interpretation is not intended, use `AIDE_Domain.yaml` rather than adding
special-case inference.

## Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a solution remains authoritative for solution/project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native solution/project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## Domain identity and references

An implicit Domain takes its current name/identity from the authoritative recognised structure
that establishes it. Use authoritative declared/native identity when available; filename matching
is only a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names for navigation, cross-Domain
references, composition, provenance or other cases where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally
wrong—for example to compose several solutions/projects/Indexes, combine differently named roots,
or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Type: Solution
        Path: Product.sln
      - Type: Index
        Path: Product_Index_v1.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Declaration fields

- `Schema` — required declaration-container schema identity; v1 value is `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of recognised roots explicitly composed/clarified by the
  entry.
- `Type` — one of the v2 Domain-approved root roles represented by `Index`, `Solution`, or `Project` for each explicit root; the resolver maps that role to approved semantic recognition rather than granting authority from the token alone.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

The explicit Domain declaration itself is Domain-capable, but its `Roots` identify the recognised
structures whose natural interpretation it composes or clarifies. Co-location of two Domain entries
inside one file creates no relationship between them.

A valid explicit declaration may override the natural implicit grouping of its listed roots. It
does not recreate or replace their internal registries or native membership rules.

## Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

Preferred authoritative hosts are:

```text
Index-backed implicit Domain
→ root Index local configuration may host Domain metadata/settings

matching solution/project + Index
→ Index is the preferred AIDE Domain metadata/settings host

explicit Domain
→ the Domain entry in AIDE_Domain.yaml hosts Domain metadata/settings
```

Where a root Index hosts Domain metadata/settings, expose one Domain configuration mapping in the
Index's local configuration using the shared field meanings:

```yaml
Domain:
  Aliases: [PreviousName]
  Settings:
    SomeSetting: <owner-defined value>
  Branches:
    - Branch: docs/api
      Settings:
        SomeSetting: <owner-defined value>
```

`Aliases`, `Settings` and `Branches` are optional. The Domain name is inherited from the Index's
authoritative structural/topic identity and `Roots` are not repeated. Core/Index owns generic Index hosting/representation; Documentation Methodology owns any
documentation-specific Index sections. Domain owns the meaning of this Domain configuration payload.

For a solution/project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit `AIDE_Domain.yaml` representation rather than modifying the native format solely to carry
AIDE configuration.

## Domain Recognition Registry

Runtime Domain discovery should not load every Standard/Item Type definition for every path step.
A build/runtime environment may compile the Domain-approved type assignments into a thin
`DomainRecognitionRegistry` containing only the cheap signatures/relations required for Domain
discovery.

Rules:

- the registry is an optimisation/projection, not the source of Domain authority;
- Core/Domain approval remains authoritative;
- load/compile definitions once per relevant context;
- prefer explicit/native/name/extension/marker evidence before expensive content inspection;
- cache unchanged resolution where safe; and
- if a registry entry cannot be traced to a currently approved semantic type/recognition rule, fail
  or refresh rather than silently granting Domain authority.

## Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. A nearby project, solution or Index is provisional until applicable enclosing evidence has
been checked.

Do **not** use “nearest marker wins”. Physical ancestry is a discovery path, not proof of
composition.

### Discovery boundaries

Stop upward discovery at the nearest meaningful operational boundary available to the current
context, such as:

- an explicitly supplied discovery boundary;
- workspace/container root;
- repository/worktree root;
- user Documents root;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- another recognised user/application storage root; or
- filesystem/mount root as fallback.

A discovery boundary limits search only. A valid explicit Domain declaration may reference roots
beyond that boundary where the environment can resolve those references.

## Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing recognised Domain evidence within that boundary, including
   applicable `AIDE_Domain.yaml` declarations and authoritative containment/membership relations.
3. Resolve explicit Domain claims applicable to the target. A valid unambiguous explicit claim
   supplies the effective Domain and may clarify/override the natural grouping of its declared
   roots.
4. Before propagating an enclosing Domain through a structural boundary, apply any Domain-owned
   `Propagation: Stop` declaration. If propagation is stopped, disregard the enclosing Domain for
   content below that boundary and continue resolution independently; the stop does not itself
   create a Domain.
5. Otherwise apply authoritative containment: a contained Domain-capable structure inherits the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate co-root independent recognised roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining independent recognised root, return that
   implicit Domain.
8. If no Domain-capable structure applies, return `No Domain context`.
9. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
   return an unresolved/error result rather than merging, ranking or guessing.

## Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership without clearly
  expressing the intended override;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## Ownership boundaries

- **Core/Domain** owns this common context/resolution/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Core/Index** owns generic Index/Item/Item Type behaviour. **Documentation Methodology** owns documentation-specific Index extensions and the `DocumentationTopic` semantic type.
- **Project/solution systems** own native membership and project/build-system semantics.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## Deliberately absent from v2

The following are not defined by this Standard:

- implicit or generic child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository-as-Domain merely because a repository exists;
- a generic settings precedence/inheritance engine;
- a Domain-specific Tool;
- broad exclusion syntax to counteract normal defaults; or
- platform-specific parser machinery beyond what is required to observe the recognised structures.

If a demonstrated use case later requires one of these mechanisms, change Domain Design first and
produce a later Standard release through the normal capability-production path.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, AIDE_Scope@v1, AIDE_Migration@v1, Core_Domain_Design_v2
References: Core_System_Design_v7, AIDE_Index@v1
<!-- END SOURCE: AIDE_Domain_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Core_Bootstrap_Design_v2.md -->
# Core Bootstrap — Design

> **Version 2** (2026-08-31). Reissued against Core Domain integration and Documentation
> Methodology v19; confirms Bootstrap Profiles, thin Contributions, dependency reuse and the
> deployment boundary.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Bootstrap is the stable AIDE activation seam between an AI platform's persistent machine-level
instructions and the deployable guidance, Standards, Tools and other AIDE material available to a
particular environment.

Bootstrap belongs to Core because it must work before any individual component can assume its full
operating material is already in context.

Core/Bootstrap owns:

- the stable bootstrap primitive;
- Bootstrap Profile semantics;
- Bootstrap Contribution discovery/ordering conventions;
- best-effort early-session processing;
- the boundary between startup activation and lazy detailed context; and
- deterministic failure when competing startup posture cannot be resolved.

It does not own the substantive behaviour of the material it activates.

## §2 — Level 1 model

```text
persistent platform bootstrap
        ↓
Bootstrap Profile
        ↓
thin Bootstrap Contributions
        ↓
full guidance / Standards / Tools loaded when needed
```

The machine-level instruction should be tiny and rarely changed. Environment-specific behaviour
changes by deploying/changing the Profile and referenced material, not by rewriting global
instructions for every release.

## §3 — Persistent platform bootstrap

Deploy the stable primitive through the strongest persistent mechanism available to the platform,
for example ChatGPT Custom Instructions, Claude instructions, Codex/global machine instructions or
an equivalent future surface.

Its job is only to:

1. discover an applicable Bootstrap Profile where available;
2. establish/process that Profile before substantive work where the platform permits;
3. process applicable available Bootstrap Contributions;
4. continue normally where no Profile is available; and
5. reconsider bootstrap only when materially new startup/profile/environment information becomes
   available.

Do not hard-code current AIDE component versions or copy detailed operational Standards into the
persistent platform instruction.

Platform implementations must not claim stronger startup enforcement than the platform provides.

## §4 — Bootstrap Profile

A Bootstrap Profile is an environment-specific **startup map**.

Each Profile entry identifies only:

```text
WHAT  — the guidance/capability/material to bring into play
WHY   — why or when it matters in this environment
WHERE — how the authoritative deployed material can be resolved
```

The Profile does not reproduce the referenced material.

Examples of possible Profiles include:

```text
AIDE Development
General Working
Documentation
Build-oriented environment
```

A general Profile may identify only Principles and Working Practices. A full development Profile
may additionally establish awareness of Core, Domain, Project Design, Build, Documentation
Methodology and relevant Capabilities.

### One effective Profile by default

At most one effective Profile applies to an environment/context by default.

Profile merging/precedence is not designed in v1. If competing Profiles are simultaneously
applicable and no explicit future composition rule resolves them, fail visibly rather than invent
an order.

No Profile is a valid state.

## §5 — Bootstrap Contributions

A Bootstrap Contribution is a **thin, separately deployable early-session instruction** owned by
the Standard, behaviour or component that needs it.

A Contribution exists only where delay until normal use would lose meaningful value.

It should contain only enough to identify:

- its owner/identity;
- the early concern/action/check;
- why/when it applies; and
- where the detailed authoritative material can be loaded when needed.

The full Standard, Tool, history or Guide remains separate.

`{bootstrap}` is the generic marker for content requiring best-effort early-session discovery.
The marker supplies no component-specific semantics.

## §6 — Startup-required dependencies

Bootstrap does not create another dependency grammar.

Where a Profile or owner requires material to be present at startup, declare that through
`AIDE_Dependencies`. The Dependencies owner defines the presence/version/startup marker semantics.

Bootstrap supplies the early-session opportunity to evaluate or surface that requirement.

A missing required item is a visible environment/deployment condition. Bootstrap does not silently
reinterpret the requirement because a deployment set omitted the item.

A startup presence check does not imply a blanket startup migration/current-version scan.

## §7 — Startup tasks

Do not introduce a generic startup-task framework in the current model.

The demonstrated needs are covered by:

- Profile activation;
- owner-defined thin Bootstrap Contributions; and
- startup-required dependency presence checks.

If a future early-session action cannot fit these mechanisms without distortion, design the
additional task concept from that demonstrated case.

## §8 — Deployment boundary

Bootstrap can be part of Deployment but does not govern Deployment.

Keep separate:

```text
requirement            → declaring owner + Dependencies
observed environment   → Environment / applicable presence mechanism
startup surfacing      → Bootstrap
permission/authority   → host administrator / controlling deployment process
deployment action      → AI Deployment
```

Bootstrap never gains installation authority merely by declaring a requirement or locator.

AI Deployment owns installation/update/remove/reconciliation/verification. The entity authorised to
control the host environment decides what may be deployed according to that environment's process
or policy; Core Bootstrap does not define a new formal deployment role.

## §9 — Future source acquisition

The architecture must permit a future flow such as:

```text
required identity missing
        ↓
trusted source/catalog resolution
        ↓
host/deployment policy permits acquisition
        ↓
AI Deployment obtains / installs / verifies
```

Trusted-source resolution, package acquisition and automatic remediation are intentionally not
designed now.

A Profile's `WHERE` field is a locator/discovery aid, not authority to execute or install content
from an arbitrary source.

## §10 — Context economy

Bootstrap is not a universal eager include.

A Profile should establish only:

- what must be recognised now;
- what must be checked now;
- what must merely be discoverable; and
- where authoritative detail can be resolved.

Load full Standards/Tools/guidance when the current work needs them.

Thin bootstrap information and lazy detailed material are a deliberate design requirement.

## §11 — Relationship to Principles and Working Practices

Bootstrap activates guidance; it does not own guidance semantics.

For example:

```text
General Working Profile
  WHAT  AIDE_Principles
  WHY   base reasoning/problem-solving guidance
  WHERE deployed guidance location

  WHAT  AIDE_WorkingPractices
  WHY   base collaboration/operating conventions
  WHERE deployed guidance location
```

The same persistent platform bootstrap can therefore support full AIDE, a narrow guidance-only
environment or no AIDE Profile.

## §12 — Intended output

This Design produces the canonical AI-facing Bootstrap contract:

```text
AIDE_Bootstrap@v1
```

Exact platform rendering of the persistent instruction, Profile and Contributions belongs to
Build/AI Deployment and should preserve these semantics without adding platform-specific behaviour
to Core.

## §13 — Deliberately deferred

- Profile merging/composition.
- Generic startup-task orchestration.
- Automatic source/package acquisition.
- Trusted package catalogs.
- Generic installer behaviour.
- Broad startup migration scans.
- Full Standards/Tools inside Bootstrap Contributions.
- Platform-specific enforcement beyond demonstrated capability.

---
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies
References: Core_System_Design_v6, Core_Bootstrap_Decisions_v2
<!-- END SOURCE: Core_Bootstrap_Design_v2.md -->

---

<!-- BEGIN SOURCE: Core_Bootstrap_Decisions_v2.md -->
# Core Bootstrap — Decisions

> **Version 2** (2026-08-31). Reissued against current Core/Documentation Methodology and records
> the confirmed Bootstrap/Profile architecture.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Bootstrap remains a Core system primitive

**Decision.** Bootstrap belongs to Core.

**Reason.** It operates before individual AIDE components can assume detailed operating material is
in context and is consumed across participating environments.

## D2 — Persistent platform bootstrap is tiny and stable

**Decision.** The machine/platform-level instruction contains only stable Profile discovery and
activation behaviour and changes rarely.

**Rejected alternative.** Hard-code the current AIDE operating set in each platform's permanent
instructions. Rejected because every release/environment change would require machine-level
maintenance.

## D3 — Environment-specific startup posture is a Bootstrap Profile

**Decision.** A Profile identifies only `what`, `why` and `where`.

**Reason.** The Profile is an early-context map, not a second copy of capability behaviour.

## D4 — Bootstrap Contributions are thin and separate

**Decision.** Component early-session contributions are separately deployable from the full
Standard/Tool/guidance.

**Reason.** Startup discovery should not require eager loading of large operating contracts.

## D5 — Lazy context is a first-class goal

**Decision.** Bootstrap establishes awareness, locators and genuinely early checks; detailed
material loads only when relevant.

## D6 — One effective Profile by default

**Decision.** At most one effective Bootstrap Profile applies by default.

**Reason.** No demonstrated need currently justifies merge/precedence machinery.

**Consequence.** Competing Profiles fail visibly until an explicit composition model is designed.
No Profile remains valid.

## D7 — Startup-required presence reuses Dependencies

**Decision.** Bootstrap does not introduce its own dependency grammar.

**Reason.** Dependencies already owns requirement identity and presence/version semantics.

**Consequence.** Bootstrap supplies the startup opportunity and surfaces unresolved requirements;
it does not redefine dependency semantics or trigger blanket startup migration.

## D8 — Bootstrap does not deploy

**Decision.** Missing required material is surfaced at runtime, not silently installed by
Bootstrap.

**Reason.** Requirement, environment state, authority to change the host and deployment action are
separate concerns.

## D9 — Core does not create a new deployment-authority role

**Decision.** Bootstrap refers to the host administrator/controlling deployment process rather than
defining a new formal Core role.

**Reason.** If a formal authority/permission role is needed, its semantics belong with the
environment/deployment process that owns installation and reconciliation.

## D10 — Deployment Set does not erase semantic requirement

**Decision.** A capability/Profile may require an item even if the current Deployment Set omitted
it.

**Reason.** Otherwise a deployment misconfiguration would erase the requirement runtime checking
exists to detect.

## D11 — Bootstrap may be deployed but does not govern Deployment

**Decision.** Bootstrap/Profile/Contribution artefacts may be deployment inputs while AI Deployment
retains deployment semantics.

## D12 — Future trusted acquisition remains possible

**Decision.** Do not block future trusted-source/catalog resolution and authorised automatic
acquisition.

**Boundary.** Source resolution/acquisition is deferred and a Profile locator never grants
installation authority.

## D13 — Generic startup-task orchestration is deferred

**Decision.** Do not create a generic startup task framework.

**Reason.** Profile activation, thin Contributions and startup-required presence checks cover the
demonstrated needs.

## D14 — Bootstrap is subset-neutral

**Decision.** The same stable bootstrap primitive must support full AIDE, Principles/Working
Practices only, another future subset or no Profile.

**Reason.** The activation layer should not force the software-development system into unrelated AI
sessions.

---
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies, Core_Bootstrap_Design_v2
References: Core_System_Decisions_v5
<!-- END SOURCE: Core_Bootstrap_Decisions_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Bootstrap_Standard_v1.md -->
# AIDE Bootstrap — Standard

> **Identity:** `AIDE_Bootstrap@v1`
> **Common name:** Bootstrap
> **Version 1** (2026-08-31). First canonical Bootstrap contract produced from
> `Core_Bootstrap_Design_v2`.
>
> **Default weight:** Requirement

## Purpose

Keep AIDE's platform-level activation instruction small and stable while allowing each environment
to select a changeable startup posture through a Bootstrap Profile and thin component Bootstrap
Contributions.

## Stable bootstrap contract

Use the strongest persistent instruction mechanism the platform provides.

The persistent bootstrap shall:

1. discover an applicable Bootstrap Profile where available;
2. establish/process the Profile before substantive work where reasonably possible;
3. process applicable available `{bootstrap}` Contributions;
4. continue normally where no Profile exists; and
5. avoid repeatedly reprocessing unchanged bootstrap state during the same session.

Do not embed a release-by-release list of AIDE components or reproduce detailed Standards/Tools in
the permanent platform instruction.

Do not claim stronger startup guarantees than the host platform provides.

## Bootstrap Profile

A Profile is an environment-specific startup map.

Each entry carries only:

```text
What
Why
Where
```

- **What** — identity/name of guidance, capability or material to bring into play.
- **Why** — concise reason or relevance condition.
- **Where** — locator/discovery information for the authoritative deployed material.

`Where` identifies how material can be resolved; it does not grant permission to execute/install
arbitrary content.

A Profile may use normal Dependencies metadata to declare required presence. Bootstrap does not
create separate dependency syntax.

One effective Profile applies by default. If multiple competing Profiles are applicable and no
governing composition rule exists, surface the conflict rather than inventing precedence.

No Profile is valid; continue without AIDE bootstrap activation.

## Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that requires best-effort early-session
discovery.

A Contribution shall be separate from the owner's full detailed material and remain short enough
to process without eagerly loading that material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/reason; and
- where detailed owner material can be resolved if needed.

The owner defines the contribution's substantive semantics. Bootstrap defines only
discovery/ordering.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

## Context economy

Bootstrap establishes awareness and genuinely early checks; it is not a universal eager include.

Load full Standards, Tools, Guides, migration histories and other detailed material only when the
current work needs them, unless the Profile deliberately identifies that material as startup
guidance.

## Dependencies and missing requirements

Use `AIDE_Dependencies` for requirement/presence/version semantics.

If startup processing reveals required material is missing:

- surface the missing requirement;
- do not silently weaken or erase the requirement;
- do not silently install/update/remove material; and
- hand remediation to the environment/deployment process that is authorised to change the host.

A startup presence check does not itself trigger a blanket migration/current-version sweep.

## Deployment boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- deployment-set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package acquisition; or
- deployment verification.

A future authorised deployment process may obtain a missing requirement from trusted configured
sources. This Standard does not define that acquisition mechanism.

## Startup tasks

No generic startup-task engine exists in v1.

Use Profile activation, thin owner Contributions and startup-required dependency checks. Add a
generic task mechanism only after a demonstrated early-session need cannot be represented by these
mechanisms cleanly.

## Subset-neutral operation

The same persistent bootstrap may activate, for example:

```text
General Working
  → Principles + Working Practices

AIDE Development
  → broader AIDE operating set
```

or operate with no Profile.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies
References: Core_Bootstrap_Design_v2, Core_System_Design_v6
<!-- END SOURCE: AIDE_Bootstrap_Standard_v1.md -->
