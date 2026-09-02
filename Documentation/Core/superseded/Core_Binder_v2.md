# Core Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 2** (2026-09-01). Review A Round 1 remediation checkpoint: reconciles Domain-owned recognition authority, one Domain-neutral Item Type recognition projection, Propagation Stop semantics, and Bootstrap Profile gating.

This Binder is a project-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Core_Index_v5.md` — sha256 `82e938f7c99b`
- `Core_System_Design_v8.md` — sha256 `bc836c9cd563`
- `Core_System_Decisions_v7.md` — sha256 `018d0b952501`
- `Core_Index_Design_v2.md` — sha256 `59619e2b013b`
- `Core_Index_Decisions_v2.md` — sha256 `ccd9702c5aaa`
- `AIDE_Index_Standard_v2.md` — sha256 `744f57397942`
- `Core_Domain_Design_v3.md` — sha256 `3e2b9fdbe2a9`
- `Core_Domain_Decisions_v3.md` — sha256 `c2875278c987`
- `AIDE_Domain_Standard_v3.md` — sha256 `31d930f77298`
- `Core_Bootstrap_Design_v3.md` — sha256 `dc38ef4f75f5`
- `Core_Bootstrap_Decisions_v3.md` — sha256 `c47b286e719d`
- `AIDE_Bootstrap_Standard_v2.md` — sha256 `e1fab36c2b82`

---

<!-- BEGIN SOURCE: Core_Index_v5.md -->
# Core — Index

> **Version 5** (2026-09-01). Registers the Review A Round 1 Core substrate remediation:
> `AIDE_Index@v2`, `AIDE_Domain@v3`, `AIDE_Bootstrap@v2` and their coordinated current
> Design/Decisions, while leaving the operational container map unchanged.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Core", type: DocumentationTopic}`

## Contents

- **Core** — AIDE system-wide foundations and reference architecture.
  - **Index** — generic hierarchical item registration and Item Type framework.  
    `{design: Core_Index_Design_v2, standard: AIDE_Index@v2}`
  - **Domain** — contextual operating/governance boundary resolution.  
    `{design: Core_Domain_Design_v3, standard: AIDE_Domain@v3}`
  - **Bootstrap** — stable startup activation seam and Profile/Contribution model.  
    `{design: Core_Bootstrap_Design_v3, standard: AIDE_Bootstrap@v2}`

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
| `Core_Index` | v5 | Index | Current |
| `Core_System_Design` | v8 | Design | Current |
| `Core_System_Decisions` | v7 | Decisions | Current |
| `Core_Index_Design` | v2 | Design | Current |
| `Core_Index_Decisions` | v2 | Decisions | Current |
| `AIDE_Index_Standard` | v2 | Standard | Current; identity `AIDE_Index@v2` |
| `Core_Domain_Design` | v3 | Design | Current |
| `Core_Domain_Decisions` | v3 | Decisions | Current |
| `AIDE_Domain_Standard` | v3 | Standard | Current; identity `AIDE_Domain@v3` |
| `Core_Bootstrap_Design` | v3 | Design | Current |
| `Core_Bootstrap_Decisions` | v3 | Decisions | Current |
| `AIDE_Bootstrap_Standard` | v2 | Standard | Current; identity `AIDE_Bootstrap@v2` |

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
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v2
References: Core_System_Design_v8, Core_Index_Design_v2, Core_Domain_Design_v3, Core_Bootstrap_Design_v3
<!-- END SOURCE: Core_Index_v5.md -->

---

<!-- BEGIN SOURCE: Core_System_Design_v8.md -->
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
<!-- END SOURCE: Core_System_Design_v8.md -->

---

<!-- BEGIN SOURCE: Core_System_Decisions_v7.md -->
# Core System — Decisions

> **Version 7** (2026-09-01). Preserves the existing system decision history and records only the
> cross-foundation consequences of Review A Round 1: Domain approval remains Domain-owned after
> registry simplification, Bootstrap Profile selection is startup-subset authority, and no new
> registry-build or startup-ordering subsystem is introduced.
>
> Created: 2026-08-28 | Last modified: 2026-09-01

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

## D25 — Domain-approved recognition remains Domain-owned after registry simplification

**Decision.** Simplifying runtime recognition to one generic optional `ItemTypeRegistry` does not
move Domain authority into Index, Item Type owners or the registry. Core/Domain publishes the
approved Domain recognition set and separately tests recognised semantic identities against it.

**Reason.** Recognition optimisation and governance authority are different concerns. Reusing one
recognition projection should remove duplication without allowing extensibility owners to create
Domain roots.

**Consequence.** Generic Index remains non-Domain-defining. Domain may additionally own minimum
native Solution/Project recognition that does not need to be represented as Item Types.

## D26 — Effective Bootstrap Profile is startup-subset authority

**Decision.** Inside Bootstrap, one effective Profile is the authority that selects the
Profile-driven AIDE startup set. No Profile means no Profile-selected AIDE startup set and does not
automatically activate every deployed Bootstrap Contribution.

**Reason.** Deployment/availability and startup selection are distinct. Profile gating is required
for Bootstrap to remain genuinely subset-neutral on a host carrying multiple AIDE subsets.

## D27 — Do not introduce new registry-build or startup-ordering subsystems

**Decision.** The Review A corrections do not create either a dedicated recognition-registry build
subsystem or a Bootstrap Contribution ordering engine.

- compiled Item Type recognition remains optional derived output with normal provenance and direct
  authoritative recognition as fallback; and
- Bootstrap Contributions are peer/order-independent, with required material expressed through the
  normal Dependencies mechanism.

**Reason.** The findings can be resolved by clarifying authority and eligibility. Separate build
or orchestration mechanisms would add architecture beyond the demonstrated need.

---
Dependencies: !AIDE_DocumentationMethodology@v22, Core_System_Design_v8
References: Core_Index_Decisions_v2, Core_Domain_Decisions_v3, Core_Bootstrap_Decisions_v3, WorkingPractices_Decisions_v5
<!-- END SOURCE: Core_System_Decisions_v7.md -->

---

<!-- BEGIN SOURCE: Core_Index_Design_v2.md -->
# Core Index — Design

> **Version 2** (2026-09-01). Retains the generic Core Index/Item/Item Type model while
> reconciling runtime recognition to one optional Domain-neutral `ItemTypeRegistry` and preserving
> Core/Domain as the exclusive owner of Domain eligibility.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

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
- the optional compact runtime `ItemTypeRegistry` projection.

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
AIDE_Index@v2
```

## §2 — Level 1 model

An Index is:

> **an authoritative, hierarchical view of significant items within a defined boundary, together
> with information and optional specialised sections applicable to that boundary.**

The minimum model remains deliberately small:

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
- a top-level topic or branch; or
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

No Item Type inheritance/class hierarchy is defined in v2. Add one only if a demonstrated need
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
- Dependencies → dependency-related contribution where one is demonstrated; or
- another Standard → an Item Type or specialist register.

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

A runtime/build environment may compile available current Item Type Definitions into one compact
`ItemTypeRegistry` containing only recognition/provision facts needed for the current work.

The `ItemTypeRegistry` is **Domain-neutral**. It may accelerate recognition of a semantic Item Type
identity and lookup of that type's declared provisions. It does not contain a type-owner-controlled
`DomainCapable`, `domainDefining`, `DomainContainer` or equivalent field that can grant Domain
authority.

Performance posture:

1. load/compile definitions once per relevant context where useful;
2. evaluate cheap selectors first;
3. perform expensive inspection only when needed;
4. lazily load richer type information for enrichment;
5. cache unchanged resolution where safe; and
6. use immediate `Folder` / `File` fallback where no semantic type matches.

A compiled registry is optional optimisation. A conforming implementation may instead evaluate
current authoritative Item Type Definitions directly.

Any persisted/built compiled registry is ordinary derived output. It must retain enough provenance
to identify the authoritative definitions/releases from which it was derived so stale output can
be invalidated and rebuilt safely. Core does not introduce a separate registry-build subsystem.

## §12 — Relationship to Domain

Generic Index existence does **not** establish a Domain.

`AIDE_Domain` alone owns the approved Domain recognition set. For a semantic Item Type, Domain may
consume a recognised Item Type identity obtained either directly from current authoritative Item
Type Definitions or through the optional `ItemTypeRegistry`, then separately test that identity
against the Domain-owned approved recognition set.

Domain may also use its own minimum native recognisers for approved structures such as Solution and
Project; those recognitions need not be represented as Item Types.

No Item Type owner can make itself Domain-capable through its definition or through registry
metadata. There is no separate Domain-specific compiled recognition registry for semantic Item
Types.

Index may host Domain-owned properties without owning Domain semantics.

## §13 — Relationship to Documentation Methodology

Documentation Methodology consumes the generic Index framework for documentation corpora.

It retains ownership of documentation-specific concerns including:

- `DocumentationTopic` Item Type semantics;
- topic/document organisation;
- Document Register;
- custom document type registration;
- assets/unmanaged document-corpus records; and
- document lifecycle and document-specific Index behaviour.

A governing documentation Index may declare/describe a logical `DocumentationTopic` boundary;
that documentation-specific semantic meaning remains owned by Documentation Methodology rather
than by generic Index.

## §14 — Relationship to other AIDE concerns

Core/Index supplies only the common structural registration/type host. Other AIDE concerns consume
that host without transferring their semantics to Index.

- Domain owns Domain eligibility/resolution and Domain-owned Index properties.
- Native project/solution systems remain authoritative for their own membership and internals.
- Capabilities owners may define Item Types or extensions where demonstrated.
- Build/runtime implementations may optimise recognition while preserving source authority.

## §15 — Deliberately absent

The v2 architecture does not add:

- Item Type inheritance;
- a universal metadata ontology;
- a generic query language;
- explicit registration of every file/folder;
- a mandatory root pointer for every project/container;
- automatic recursion into self-describing child boundaries;
- an owner-self-declared Domain-capable Item Type flag; or
- a separate Domain Recognition Registry artefact.

Add any of these only after a demonstrated need changes the owning Design.

---
Dependencies: !AIDE_DocumentationMethodology@v22
References: Core_Domain_Design_v3, DocumentationMethodology_Design_v19
<!-- END SOURCE: Core_Index_Design_v2.md -->

---

<!-- BEGIN SOURCE: Core_Index_Decisions_v2.md -->
# Core Index — Decisions

> **Version 2** (2026-09-01). Preserves the v1 generic Index decision history and records the
> Review A reconciliation to one optional Domain-neutral Item Type recognition projection with
> direct authoritative recognition as the supported fallback.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## D1 — Index is a generic Core foundation

**Decision.** Index is a generic AIDE structural registration/information-hosting mechanism owned by
Core rather than a documentation-only construct.

**Reason.** Repository/catalogue navigation, documentation corpora, native structures and future
AIDE concerns need the same small concept without making Documentation Methodology the owner of all
structural registration.

## D2 — Index authority stops at the registration boundary

**Decision.** An Index is authoritative for which Items it registers within its scope and for
Index-owned facts about those registrations. Registration does not make the Index authoritative for
the registered Item's internals.

**Reason.** Structural discovery must not transfer authority from native/self-describing owners into
the registry that points at them.

## D3 — Registration is selective

**Decision.** `Contents` registers significant Items and is not required to enumerate every physical
file/folder.

**Reason.** A useful structural view should remain compact and purpose-driven rather than becoming a
filesystem mirror.

## D4 — Parent Indexes may delegate at self-describing boundaries

**Decision.** A parent Index need not recursively enumerate an independently self-describing child
container. It locates/describes the boundary and delegates internal discovery.

**Reason.** This keeps hot/high-level Indexes small and avoids duplicate registries.

## D5 — Item Type is the generic semantic classification mechanism

**Decision.** An Item Type Definition states only how the type is identified and what it provides
once identified.

**Reason.** This is sufficient to support semantic types such as `DocumentationTopic` or future
domain-specific structures without building a universal object model.

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

## D10 — Runtime type resolution may use a thin compiled registry

**Decision.** Item Type Definitions may be compiled into a compact runtime registry; cheap
recognition runs before expensive enrichment and unchanged results may be cached.

**Reason.** Frequently invoked classification should not require loading or scanning every full
Standard on every operation.

## D11 — Generic Index is not Domain-defining by default

**Decision.** Domain-defining status is assigned by Core/Domain to approved recognition, not by
generic Index existence or arbitrary type-owner declaration.

**Reason.** Domain formation changes system governance context and therefore requires restricted
system-level authority.

## D12 — Update operations preserve other owners' contributions

**Decision.** An updater changes only the fields/sections it owns or is authorised to reconcile.
Unknown owner contributions and human-authored descriptions are preserved.

**Reason.** A shared Index becomes unsafe if a generated update can erase unrelated semantic or
human information.

## D13 — Keep one generic Item Type recognition projection

**Decision.** The optional `ItemTypeRegistry` remains the single generic compiled Item Type
recognition projection. Do not create a second Domain-specific registry for the same semantic Item
recognitions.

**Reason.** Domain eligibility is an authority decision applied after recognition, not a second Item
Type recognition system.

**Consequence.** Domain may consume a semantic Item Type identity recognised directly or through
`ItemTypeRegistry`, then apply its own approved recognition set. Domain-owned native recognition is
separate because those structures are not required to be Item Types.

## D14 — Runtime registry does not carry self-granted Domain authority

**Decision.** An Item Type owner cannot make itself Domain-capable through its Item Type Definition
or through metadata in `ItemTypeRegistry`.

**Reason.** The registry is a Domain-neutral recognition/provision optimisation. Core/Domain alone
owns the approved recognition set that controls Domain authority.

**Consequence.** Fields such as `DomainCapable`, `domainDefining`, `DomainContainer` or an equivalent
owner-controlled grant are not part of the generic registry contract.

## D15 — Direct recognition is the supported fallback

**Decision.** A compiled `ItemTypeRegistry` is optional. A conforming implementation may evaluate
current authoritative Item Type Definitions directly.

**Reason.** Recognition correctness must not depend on a separately maintained compiled artefact.

**Consequence.** Persisted compiled forms are derived outputs and retain enough source provenance to
be invalidated/rebuilt safely. Core does not add a registry-build subsystem.

---
Dependencies: !AIDE_DocumentationMethodology@v22, Core_Index_Design_v2
References: Core_Domain_Decisions_v3, DocumentationMethodology_Decisions_v20
<!-- END SOURCE: Core_Index_Decisions_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Index_Standard_v2.md -->
# AIDE Index — Standard

> **Identity:** `AIDE_Index@v2`
> **Common name:** Index
> **Version 2** (2026-09-01). Retains the generic Index/Item/Item Type contract while making the
> optional Item Type registry Domain-neutral and removing the separate Domain recognition registry
> concept.
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
exists in v2.

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

HTML may be generated as presentation but is not canonical source in v2.

## Runtime Item Type Registry

A runtime/build environment may compile available current Item Type Definitions into one compact
`ItemTypeRegistry`.

The registry contains only the recognition/provision facts needed for Item Type recognition and
provision lookup. It is **Domain-neutral** and is derived optimisation state, not semantic or Domain
authority.

Use this order where practical:

1. explicit/cheap selectors;
2. structural/native relationship checks;
3. expensive inspection only if necessary;
4. lazy enrichment after classification; and
5. cached reuse for unchanged items where safe.

A compiled registry is optional. Direct evaluation of current authoritative Item Type Definitions
is a conforming fallback when a compiled registry is absent, stale or unsuitable.

If a compiled registry is persisted/built, preserve enough authoritative source identity/version
provenance to determine whether it remains current and to invalidate/rebuild it safely. This
Standard does not define a separate registry-build subsystem.

## Domain boundary

Generic Index existence does **not** establish a Domain.

`AIDE_Domain` alone owns the approved Domain recognition set. Domain may consume a semantic Item
Type identity recognised directly or through `ItemTypeRegistry`, then separately test that identity
for Domain eligibility.

No Item Type owner or `ItemTypeRegistry` entry may self-grant Domain authority through a
`DomainCapable`, `domainDefining`, `DomainContainer` or equivalent owner-controlled declaration.

Domain may additionally apply Domain-owned native recognisers that are not Item Types. No separate
Domain-specific compiled registry is required for semantic Item Type recognition.

## Deliberately absent

No v2 requirement exists for:

- type inheritance;
- universal metadata ontology;
- generic query language;
- explicit registration of every file/folder;
- mandatory root pointer for every project/container;
- automatic recursion into self-describing child boundaries;
- an owner-self-declared Domain-capable Item Type flag; or
- a separate Domain Recognition Registry artefact.

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
Dependencies: !AIDE_DocumentationMethodology@v22
References: Core_Index_Design_v2, Core_Domain_Design_v3
<!-- END SOURCE: AIDE_Index_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Core_Domain_Design_v3.md -->
# Core Domain — Design

> **Version 3** (2026-09-01). Completes the Domain semantic-recognition refactor by publishing a
> Domain-owned approved recognition set, removing generic Index as a Domain root, retaining minimum
> native Solution/Project recognition, removing the separate Domain recognition registry, and
> completing Propagation Stop, explicit-root assertion and settings-host semantics.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## §1 — Purpose and ownership

Domain defines the common AIDE concept used to identify the named operating/governance context
within which work is being performed.

A **Domain is a named AIDE operating/governance context**. It is contextual and semantic; it is not
inherently a file and is not an AIDE activation switch.

Core/Domain owns:

- the meaning and identity of Domain;
- the explicit, versioned approved recognition set used for Domain resolution;
- the minimum native Solution/Project recognition and containment/membership observations needed by
  Domain;
- implicit versus explicit Domain formation;
- target-based discovery, resolution and deterministic ambiguity/failure behaviour;
- Domain metadata/settings-host and `Branch` conventions;
- Domain propagation-stop semantics; and
- Domain eligibility decisions applied after semantic Item Type recognition.

Domain does **not** own the full semantics of an approved semantic Item Type or native platform
structure. Generic Index/Item/Item Type semantics belong to Core/Index; an Item Type owner remains
authoritative for its own `Identify` and `Provides` contract. Native platforms remain authoritative
for solution/project identity, membership and internal semantics.

Domain alone decides whether recognised evidence may establish or participate in Domain resolution.

This Design produces:

```text
AIDE_Domain@v3
```

## §2 — Level 1 model and authority seam

```text
target / focus
    ↓
recognise available approved evidence
    ├── semantic Item Type identity
    ├── Domain-owned minimum native recognition
    └── explicit AIDE_Domain declaration
    ↓
Domain-owned approved recognition test
    ↓
explicit declaration / containment / co-root / propagation evaluation
    ↓
effective Domain | No Domain | unresolved/error
```

Recognition and Domain authority are distinct:

```text
Item Type owner
  → identity + Identify + Provides

optional ItemTypeRegistry
  → Domain-neutral recognition/provision optimisation

Core/Domain
  → approved Domain recognition set
  → minimum native Solution/Project recognition
  → Domain resolution authority
```

An external Item Type owner cannot add a field to its type definition or a compiled registry and
thereby become a Domain root.

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

## §4 — Approved Domain recognition set

The approved recognition set is part of the Domain contract itself. It is explicit and versioned
with `AIDE_Domain`; it is not a second standalone registry.

The v3 set is:

| Recognition | Kind | Recognition owner | Domain authority owner |
|---|---|---|---|
| `DocumentationTopic` | semantic Item Type | Documentation Methodology | Core/Domain |
| `Solution` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `Project` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `AIDE_Domain` declaration entry | explicit Domain declaration | Core/Domain | Core/Domain |

A generic `Index` is **not** in the approved set.

### `DocumentationTopic`

`DocumentationTopic` is a Documentation Methodology-owned semantic Item Type representing one
logical top-level-topic documentation boundary. Its governing Index document declares/describes
that logical boundary and supplies the authoritative recognition evidence; the Markdown file is not
itself the semantic boundary merely because the declaration appears there.

Subtopics do not become independent `DocumentationTopic` Items merely because they have their own
Design/Decisions/Index state.

Domain may consume a recognised `DocumentationTopic` identity but only this Domain-owned approval
makes that semantic type Domain-eligible.

### Native `Solution`

Domain owns only the minimum observation needed to recognise a native Solution for Domain purposes:

- a current native/platform-recognised Solution identity/signature; and
- the authoritative project-membership relationship exposed by that native structure when
  membership matters to Domain resolution.

The native platform remains authoritative for solution format, identity details, membership and all
other solution semantics. Domain does not invent an AIDE Solution Item Type merely to use the
native structure.

### Native `Project`

Domain owns only the minimum observation needed to recognise a native Project for Domain purposes:

- a current native/platform-recognised Project identity/signature; and
- its authoritative membership relationship to a recognised enclosing Solution where such a
  relationship exists.

A Project that is an authoritative member of a Solution participates through that containment; a
standalone recognised Project may establish an implicit Domain when no stronger enclosing Domain
relationship applies.

The native platform remains authoritative for project format, internals and membership semantics.

### Explicit `AIDE_Domain` declaration

A valid Domain entry in `AIDE_Domain.yaml` is a Domain-owned explicit recognition. It composes or
clarifies recognised roots. The file/container is not itself evidence that every nearby item is in
the declared Domain; normal applicability and root validation still apply.

## §5 — Domain model

A Domain may be:

```text
implicit  — established from approved recognition and authoritative structural relationships
explicit  — declared in AIDE_Domain.yaml to compose or clarify approved recognised roots
```

A repository/worktree remains a discovery boundary, not an implicit Domain recognition.

An Index may host or declare information used by another approved recognition. In particular, a
documentation Index may declare a `DocumentationTopic`, or may host Domain-owned configuration for
an implicit Domain established by approved evidence. **Index existence alone never establishes
Domain context.**

## §6 — Natural containment and Propagation Stop

Under ordinary authoritative containment, a contained recognised structure remains in the
enclosing effective Domain rather than creating a second implicit Domain.

Examples:

- a Project that is an authoritative member of a Solution remains in the Solution Domain; and
- a subordinate documentation structure remains in the enclosing Domain unless propagation is
  deliberately stopped.

The current rule is:

> Under ordinary authoritative containment, structural children do not create a second implicit
> Domain. A deliberate `Propagation: Stop` terminates that containment propagation; independent
> resolution below the stop may establish another Domain, but it is not modelled as a child Domain.

### Propagation Stop meaning

Canonical meaning:

> The enclosing effective Domain does not propagate through the marked structural boundary.
> Resolution below the boundary continues independently as though that enclosing Domain were absent.
> Independent resolution may therefore yield `No Domain`, an unresolved/error result, or another
> Domain. If another Domain is found below the stop, the current model defines no parent/child
> semantic relationship, inheritance, merge, settings propagation or precedence between the two.

### Supported Stop representation in v3

v3 supports Stop only on a **recognised/registered Domain-aware structural boundary**.

Where represented by an Index Item, the parent Index may register the significant boundary for the
purpose of locating/describing it and hosting the Domain-owned property:

```yaml
Domain:
  Propagation: Stop
```

That registration does not transfer authority over the boundary's internals to the parent Index.

v3 does not add a generic filesystem marker file or arbitrary unregistered-folder exclusion.

### Stop traversal

When resolving upward from a target:

1. identify each crossed recognised structural boundary;
2. inspect the applicable Domain-owned boundary configuration, including a parent Index
   registration where that registration is the authoritative host for the Stop property; and
3. when Stop applies to a crossed boundary, discard the enclosing Domain for content below that
   boundary and continue independent Domain resolution within/below the stopped region.

A Stop is therefore a propagation rule, not a Domain-creation token.

## §7 — Co-root recognised structures

Evaluate approved recognised structures sharing a physical root by authoritative identity and
structural relationships, not proximity alone.

### Matching identity

Approved co-root structures with matching authoritative identities form one implicit Domain where
no stronger explicit/containment rule changes the result.

```text
Foo.sln + DocumentationTopic(Foo)  → one Foo Domain
```

The documentation boundary is recognised as `DocumentationTopic`; a bare generic Index does not
supply a second Domain root.

### Different identity

Approved co-root structures with different identities remain separate implicit Domains by default.

```text
Foo.sln + DocumentationTopic(Womble)  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj               → Foo Domain + Bar Domain
```

If the natural interpretation is not intended, use `AIDE_Domain.yaml` rather than adding
special-case inference.

## §8 — Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a native Solution remains authoritative for Solution/Project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native Solution/Project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## §9 — Domain identity and references

An implicit Domain takes its current name/identity from the authoritative approved recognition that
establishes it. Use authoritative declared/native identity when available; filename matching is only
a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names for navigation, cross-Domain references,
composition, provenance or other cases where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## §10 — Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally wrong—for
example to compose several Solutions/Projects/DocumentationTopics, combine differently named roots,
or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Recognition: Solution
        Path: Product.sln
      - Recognition: DocumentationTopic
        Path: docs/Product_Index_vN.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Root recognition is an assertion

`Recognition` means **expected approved Domain recognition**.

It never grants Domain capability. For every root:

1. the resolver independently recognises the target using the current authoritative semantic Item
   Type definition or Domain-owned native recognition mechanism;
2. the observed recognition must match the declared expected `Recognition`;
3. mismatch fails visibly; and
4. an unknown/unapproved recognition fails visibly.

`Index` is not a valid root-recognition value merely because the path points at an Index document.
A documentation-backed root uses `DocumentationTopic` when that logical top-level-topic boundary is
actually recognised.

If a representation retains the older field name `Type`, it has exactly these expected-recognition
assertion semantics; it is not an authority token.

### Declaration fields

- `Schema` — required declaration-container schema identity; current value remains
  `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of approved recognised roots explicitly composed/clarified
  by the entry.
- `Recognition` — expected approved Domain recognition for the root; validated against observed
  recognition and never self-authorising.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

Co-location of two Domain entries inside one file creates no relationship between them. A valid
explicit declaration may override the natural implicit grouping of its listed roots, but it does
not recreate or replace their internal registries or native membership rules.

## §11 — Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

### Authoritative Domain settings host

If an explicit `AIDE_Domain.yaml` Domain entry governs/composes the effective Domain, **that Domain
entry is the sole authoritative Domain metadata/settings host for that Domain**.

An Index-hosted `Domain:` configuration for the same effective Domain is not merged with the
explicit entry. Duplicate/conflicting host state is an error requiring reconciliation.

For an applicable implicit Domain where no explicit Domain entry governs it, an Index may continue
to host Domain-owned configuration when it is the applicable authoritative host. For a
Solution/Project-only implicit Domain that needs AIDE Domain metadata/settings, an explicit Domain
representation may be introduced rather than modifying the native format solely for AIDE
configuration.

## §12 — Runtime recognition

Domain has no separately named Domain recognition registry.

Domain resolution may use:

- direct current semantic Item Type recognition;
- the optional generic Domain-neutral `ItemTypeRegistry` from `AIDE_Index@v2`;
- Domain-owned minimum native Solution/Project recognisers;
- explicit `AIDE_Domain.yaml` declaration parsing; and
- safe runtime caches.

For semantic Item Types, recognition establishes only the Item Type identity. Domain then compares
that identity against its own current approved recognition set. No semantic Item Type definition
can elevate itself to Domain authority.

Compiled/cached state is derived optimisation only. If current recognition/approval provenance
cannot be established, refresh/directly evaluate or fail visibly rather than granting authority
from stale derived state.

## §13 — Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. A nearby Project, Solution or documentation Index is provisional evidence until applicable
enclosing relationships and approved recognition have been checked.

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

## §14 — Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing approved Domain evidence, including applicable explicit Domain
   declarations, semantic Item Type recognition, native Solution/Project recognition and
   authoritative containment/membership relations.
3. While walking upward, identify every crossed recognised structural boundary and inspect its
   applicable Domain-owned boundary configuration. If `Propagation: Stop` applies, exclude any
   enclosing Domain above that boundary from content below it and continue independent resolution.
4. Resolve explicit Domain claims applicable to the target. Validate every declared root's expected
   `Recognition` against independently observed approved recognition. A valid unambiguous explicit
   claim supplies the effective Domain for its governed/composed roots.
5. Otherwise apply authoritative containment: a contained approved structure participates in the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate remaining independent approved co-roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining independent approved root, return that
   implicit Domain.
8. If no approved recognition applies, return `No Domain context`.
9. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
   return an unresolved/error result rather than merging, ranking or guessing.

## §15 — Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- an explicit root's declared expected recognition does not match observed recognition;
- an explicit root uses an unknown/unapproved recognition;
- two explicit Domains claim the same effective target without a defined resolution;
- an explicit declaration and an Index expose duplicate/conflicting Domain metadata/settings for
  the same effective explicit Domain;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## §16 — Ownership boundaries

- **Core/Domain** owns this common context/resolution/approved-recognition/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Core/Index** owns generic Index/Item/Item Type behaviour and the optional Domain-neutral
  `ItemTypeRegistry`.
- **Documentation Methodology** owns documentation-specific Index extensions and the
  `DocumentationTopic` semantic Item Type.
- **Native project/solution systems** own native membership and project/solution internals; Domain
  observes only the minimum facts needed for resolution.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## §17 — Deliberately absent

The v3 architecture deliberately does not add:

- generic Index as a Domain recognition;
- owner-self-declared Domain-capable Item Type flags;
- a separate Domain Recognition Registry;
- invented AIDE Item Types for native Solution/Project solely to obtain Domain recognition;
- implicit/generic child-Domain inheritance, override or composition;
- parent/child Domain settings propagation;
- arbitrary nested Domain precedence;
- a generic settings precedence/inheritance engine;
- repository-as-Domain merely because a repository exists;
- a generic filesystem Propagation Stop marker or arbitrary unregistered-folder exclusion;
- a Domain-specific Tool; or
- broad platform parser machinery beyond minimum approved recognition observations.

If a demonstrated use case later requires one of these mechanisms, change Domain Design first and
produce a later Standard release through the normal capability-production path.

## §18 — Success signals

The model is successful when:

- Domain authority can be audited from the Domain-owned approved recognition set;
- an external Item Type cannot promote itself into a Domain root;
- generic Indexes may exist without creating Domain context;
- documentation roots use `DocumentationTopic` rather than bare Index recognition;
- native Solutions/Projects work without invented AIDE type owners;
- runtime recognition may be direct or use the generic Item Type projection without duplicating
  registry machinery;
- a Propagation Stop can terminate an enclosing Domain and allow independent resolution below it
  without creating parent/child Domain semantics;
- explicit roots are validated assertions rather than authority grants;
- an explicit Domain has one authoritative Domain metadata/settings host;
- ambiguity fails visibly; and
- `No Domain context` remains a normal result.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v2
References: Core_Index_Design_v2, Core_Domain_Decisions_v3, DocumentationMethodology_Design_v19
<!-- END SOURCE: Core_Domain_Design_v3.md -->

---

<!-- BEGIN SOURCE: Core_Domain_Decisions_v3.md -->
# Core Domain — Decisions

> **Version 3** (2026-09-01). Preserves the full Domain decision history and records the Review A
> corrections that publish the Domain-owned approved recognition set, retain native Solution/Project
> recognition, remove generic Index and the separate Domain recognition registry from the current
> model, and complete Propagation Stop, explicit-root and settings-host semantics.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

> **Current-decision note.** D1–D31 are preserved historical decisions. Where a v3 decision below
> explicitly refines or supersedes a narrower part of an earlier decision, the later decision is the
> current position for that point; the historical text remains unchanged as reasoning history.

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

---

## D26 — Domain consumes semantic Item Types and owns Domain eligibility

**Decision.** Domain consumes semantic Item Types and maintains the system-approved subset that may
establish Domain context.

**Consequence.** Type owners define recognition/provisions; Domain defines only Domain eligibility
and the Domain-relevant structural relationship contract.

---

## D27 — Generic Index is not automatically Domain-defining

**Trigger / problem.** Once Index becomes generic, many valid Indexes describe repositories,
collections or other boundaries that should not automatically become governance Domains.

**Decision.** Remove generic `Index` from the implicit Domain-defining rule. A semantic type such as
`DocumentationTopic`, a native `Solution`/`Project`, or explicit Domain declaration must supply
the approved boundary evidence.

**Consequence.** An Index may still host Domain metadata/settings for a Domain established by an
approved type. An unusual Index-backed Domain can use an approved semantic type or explicit
`AIDE_Domain.yaml` rather than relying on generic Index existence.

---

## D28 — Domain-defining assignment is restricted to Core/Domain

**Decision.** Item Type Definitions cannot set their own `domainDefining: true`-style authority.
Domain owns the approved type list and any derived recognition registry.

**Reason.** Domain context affects governance and must not be obtainable as an accidental extension
privilege.

---

## D29 — Compile a thin Domain Recognition Registry

**Decision.** Runtime implementations may derive a compact recognition projection from the current
Domain-approved Item Types.

**Reason.** Domain resolution sits on a frequent path and should not repeatedly load every full
Standard or type definition.

**Constraint.** The registry is derived optimisation state. Domain Design plus the owning Item Type
Definitions remain authoritative.

---

## D30 — Add a Domain propagation-stop boundary without designing inheritance

**Trigger / problem.** An enclosing Domain sometimes must not propagate through a structural
boundary, even though the content below may not yet define its own Domain. Waiting for a full child
Domain inheritance model would leave no clean way to express that current need.

**Decision.** Introduce Domain-owned `DomainPropagation: Stop` semantics. It blocks enclosing Domain
propagation below the marked structure and forces independent resolution beneath it.

**Non-goals.** The marker does not create a child Domain, define inheritance/merge, or set generic
precedence.

---

## D31 — Issue Domain v2

**Decision.** Publish the reconciled contract as `AIDE_Domain@v2` with migration posture `None`.

**Reason.** The semantic recognition/authority model changes, but no existing governed document
requires automatic content transformation merely to adopt the new release. Indexes and Domain
representations are reconciled when next substantively updated or when an operation specifically
needs the v2 semantics.

---

## D32 — Domain publishes the approved recognition set

**Decision.** `AIDE_Domain` publishes the explicit versioned set of recognitions permitted to
establish or participate in Domain resolution.

The v3 set is `DocumentationTopic`, native `Solution`, native `Project`, and an explicit
`AIDE_Domain` declaration entry.

**Reason.** Domain eligibility is a governance authority decision and must be auditable from the
Domain contract itself rather than inferred from other owners' extensibility metadata.

**Refines.** D5 and D26. The current set is narrower and explicit; generic Index is not an approved
recognition.

## D33 — Use semantic Item Type indirection only where a genuine semantic owner exists

**Decision.** Use an existing reusable semantic Item Type such as `DocumentationTopic` where its
owner genuinely defines reusable recognition/provisions. Keep Solution and Project as minimum
Domain-owned native observations rather than inventing AIDE Item Type owners solely for Domain.

**Reason.** Forcing every native structure through an invented Item Type would add ownership and
schema machinery without improving the authority boundary.

**Boundary.** Native platforms remain authoritative for Solution/Project identity, membership and
internals. Domain owns only the minimum recognition/containment facts it consumes.

## D34 — Generic Index remains non-Domain-defining

**Decision.** Generic `Index` remains outside the approved Domain recognition set.

**Reason.** Index is a structural host/registry and may describe many non-governance boundaries.
Documentation-backed Domain roots use the approved `DocumentationTopic` semantic Item Type instead.

**Refines.** D5, D6, D8, D9, D10, D15, D19 and D22 where their historical wording/examples
used Index as a literal or potentially Domain-establishing boundary. Those entries remain historical
reasoning; the current rule is that generic Index is not approved Domain recognition.

## D35 — Remove the separate Domain Recognition Registry

**Decision.** Do not maintain a separately named Domain Recognition Registry for semantic Item Type
recognition. Domain may consume direct semantic recognition or the optional generic Domain-neutral
`ItemTypeRegistry`, then apply its own approved recognition set.

**Reason.** A second registry duplicates recognition mechanics. Domain eligibility is the distinct
Domain-owned decision.

**Supersedes.** D29's separate registry architecture and refines D28's historical reference to a
Domain-derived recognition registry. Runtime caching remains allowed as derived implementation
optimisation.

## D36 — Propagation Stop terminates propagation and permits independent resolution below

**Decision.** `Propagation: Stop` removes the enclosing effective Domain from content below the
marked boundary. Resolution below continues independently and may yield `No Domain`, an error, or
another Domain.

If another Domain is found, v3 defines no parent/child semantic relationship, inheritance, merge,
settings propagation or precedence between the two Domains.

**Reason.** A stop is useful only if it actually resets contextual propagation. Independent
recognition below is not the same thing as child-Domain semantics.

**Refines.** D7 and D30. Structural children do not ordinarily create a second implicit Domain; a
Stop changes propagation and thereby permits independent resolution.

## D37 — Propagation Stop is limited to recognised/registered structural boundaries in v3

**Decision.** v3 supports Stop only where the crossed boundary is a recognised/registered
Domain-aware structural boundary whose Domain-owned configuration can be located reliably.

A parent Index registration may host the Stop property for a significant boundary without becoming
authoritative for that boundary's internals.

**Reason.** This is implementable with current structure. A generic filesystem marker or arbitrary
unregistered-folder exclusion would introduce a new recognition mechanism not justified by the
finding.

## D38 — Explicit-root recognition is a validated assertion, not an authority grant

**Decision.** An explicit Domain root's `Recognition` value states the expected approved Domain
recognition. The resolver independently recognises the target and requires the observed recognition
to match.

Unknown/unapproved or mismatched recognition fails visibly. Generic `Index` is not valid merely
because the target path points to an Index document.

**Reason.** Explicit configuration may clarify composition but must not mint Domain authority by
typing arbitrary paths.

**Compatibility.** If a representation retains the field name `Type`, it has these same assertion
semantics.

## D39 — An explicit Domain entry is the sole Domain metadata/settings host where it governs

**Decision.** When an explicit `AIDE_Domain.yaml` entry governs/composes the effective Domain, that
entry is the sole authoritative Domain metadata/settings host for that Domain.

An Index-hosted Domain configuration for the same effective Domain is not merged; duplicate or
conflicting host state is an error requiring reconciliation.

**Reason.** Two simultaneous Domain-owned hosts create undefined precedence and can make effective
settings depend on discovery order.

**Refines.** D10 and D17 for explicit Domains. Index-hosted Domain configuration remains valid for
an applicable implicit Domain where no explicit entry governs it.

## D40 — Issue Domain v3 with migration posture None

**Decision.** Publish the corrected contract as `AIDE_Domain@v3` with migration posture `None`.

**Reason.** v3 changes the current semantic contract and resolution rules but does not require an
automatic transformation of existing governed artefacts solely because the Domain release changed.
Existing explicit declarations/configuration are reconciled when substantively updated or when the
v3 semantics are applied to them.

---
Dependencies: !AIDE_DocumentationMethodology@v22, Core_Domain_Design_v3, AIDE_Index@v2
References: Core_Index_Decisions_v2, DocumentationMethodology_Decisions_v20
<!-- END SOURCE: Core_Domain_Decisions_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Domain_Standard_v3.md -->
# AIDE Domain — Standard

> **Identity:** `AIDE_Domain@v3`
> **Common name:** Domain
> **Version 3** (2026-09-01). Completes the Domain recognition contract with an explicit
> Domain-owned approved recognition set, native Solution/Project minimum recognition, no generic
> Index root or separate Domain recognition registry, and complete Propagation Stop, explicit-root
> assertion and settings-host rules.
>
> **Default weight:** Requirement

## Purpose

Provide one consistent AIDE contract for identifying the named operating/governance context
relevant to a target, hosting independently owned Domain-context settings, and explicitly
clarifying/composing Domain roots when natural approved structure is insufficient.

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
implicit  — established from Domain-approved recognition and authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify approved recognised roots
```

Generic Item/Item Type semantics belong to `AIDE_Index@v2`. An Item Type owner defines the type's
identity, `Identify` and `Provides` semantics. **Only Core/Domain decides whether a recognised
semantic Item Type identity may establish or participate in Domain resolution.**

External Item Type owners cannot self-elevate to Domain capability. No Item Type owner, generic
Index, or registry entry can self-grant Domain authority.

## Approved Domain recognition set

The approved recognition set is authoritative Domain contract state and is versioned with this
Standard. Do not derive Domain eligibility from a type-owner flag or create a separate approval
register solely for this purpose.

The following table is the authoritative v3 approved recognition set:

| Recognition | Kind | Recognition owner | Domain authority owner |
|---|---|---|---|
| `DocumentationTopic` | semantic Item Type | Documentation Methodology | Core/Domain |
| `Solution` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `Project` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `AIDE_Domain` declaration entry | explicit Domain declaration | Core/Domain | Core/Domain |

A generic `Index` is **not** approved Domain recognition.

### `DocumentationTopic`

`DocumentationTopic` is the Documentation Methodology-owned semantic Item Type for one logical
**top-level documentation topic boundary**. Its governing Index document declares/describes that
logical boundary and supplies the recognition evidence; the Index file itself is not the semantic
boundary merely because it hosts the declaration.

Subtopics do not become independent `DocumentationTopic` Items merely because they have their own
Design/Decisions/Index state.

A documentation Index may therefore be the representation used to recognise a
`DocumentationTopic`, but generic Index existence never establishes a Domain.

### Native `Solution` recognition

For Domain purposes, recognise a Solution only from the minimum current native/platform evidence
needed to establish:

- the native Solution identity/signature; and
- authoritative project membership where membership affects Domain containment.

The native platform remains authoritative for Solution format, membership and internals. This
Standard does not define an AIDE Solution Item Type.

### Native `Project` recognition

For Domain purposes, recognise a Project only from the minimum current native/platform evidence
needed to establish:

- the native Project identity/signature; and
- authoritative membership in an enclosing recognised Solution where that relationship exists.

A Project that is a member of a Solution remains within that Solution's effective Domain under
normal propagation. A standalone recognised Project may establish an implicit Domain where no
stronger enclosing Domain applies.

The native platform remains authoritative for Project format, membership and internals. This
Standard does not define an AIDE Project Item Type.

### Explicit Domain declaration recognition

A valid Domain entry in `AIDE_Domain.yaml` is Domain-owned approved recognition. It may compose or
clarify approved roots but does not grant arbitrary nearby structures Domain capability.

A repository/worktree remains a discovery boundary, not an implicit Domain recognition.

## Natural containment

Under ordinary authoritative containment, a contained approved structure does not create a second
implicit Domain.

- a Project that is an authoritative member of a Solution remains in the Solution Domain; and
- a subordinate recognised documentation structure remains in its enclosing effective Domain while
  propagation continues.

The current rule is:

> Under ordinary authoritative containment, structural children do not create a second implicit
> Domain. A deliberate `Propagation: Stop` terminates that containment propagation; independent
> resolution below the stop may establish another Domain, but it is not modelled as a child Domain.

## Domain propagation stop

Use:

```yaml
Domain:
  Propagation: Stop
```

only on a recognised/registered Domain-aware structural boundary for which the Domain-owned
property can be resolved reliably.

Canonical meaning:

> The enclosing effective Domain does not propagate through the marked structural boundary.
> Resolution below the boundary continues independently as though that enclosing Domain were absent.
> Independent resolution may therefore yield `No Domain`, an unresolved/error result, or another
> Domain. If another Domain is found below the stop, this Standard defines no parent/child semantic
> relationship, inheritance, merge, settings propagation or precedence between the two.

Where an Index Item represents the significant crossed boundary, a parent Index registration may
host the Domain-owned Stop property. That registration does not transfer authority over the
boundary's internals.

v3 does not define a generic filesystem Stop marker or arbitrary unregistered-folder exclusion.

### Stop traversal

While walking upward from the target:

1. identify every crossed recognised structural boundary;
2. inspect applicable Domain-owned boundary configuration, including a parent Index registration
   where that registration is the authoritative host; and
3. if Stop applies, discard the enclosing Domain for content below the boundary and continue
   independent resolution.

Stop terminates propagation; it does not itself create a Domain.

## Co-root recognised structures

Evaluate approved recognised structures sharing a physical root by authoritative identity and
structural relationships, not proximity alone.

### Matching identity

Approved co-root structures with matching authoritative identities form one implicit Domain where
no stronger rule changes the result.

```text
Foo.sln + DocumentationTopic(Foo)  → one Foo Domain
```

### Different identity

Approved co-root structures with different identities remain separate implicit Domains by default.

```text
Foo.sln + DocumentationTopic(Womble)  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj               → Foo Domain + Bar Domain
```

A bare generic Index beside `Foo.sln` does not establish a separate Womble Domain. If the natural
interpretation is not intended, use `AIDE_Domain.yaml` rather than adding special-case inference.

## Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a native Solution remains authoritative for Solution/Project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native Solution/Project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## Domain identity and references

An implicit Domain takes its current name/identity from the authoritative approved recognition that
establishes it. Use authoritative declared/native identity when available; filename matching is only
a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally
wrong—for example to compose several Solutions/Projects/DocumentationTopics, combine differently
named roots, or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Recognition: Solution
        Path: Product.sln
      - Recognition: DocumentationTopic
        Path: docs/Product_Index_vN.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Declaration fields

- `Schema` — required declaration-container schema identity; current value is `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of approved recognised roots explicitly composed/clarified
  by the entry.
- `Recognition` — expected approved Domain recognition for the root. It is an assertion, not an
  authority grant.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

### Root-recognition validation

For each explicit root:

1. independently recognise the target through current authoritative semantic Item Type recognition
   or the applicable Domain-owned native recogniser;
2. compare the observed recognition with the declared expected `Recognition`;
3. fail visibly on mismatch; and
4. fail visibly on unknown/unapproved recognition.

The token itself never creates Domain capability. `Index` is not a valid value merely because the
path identifies an Index document.

If an existing representation retains the field name `Type`, it has exactly these assertion
semantics.

The explicit Domain declaration itself is approved Domain recognition. Co-location of two Domain
entries in one file creates no relationship between them. A valid explicit declaration may change
the natural grouping of its listed roots but does not replace their internal registries or native
membership rules.

## Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

### Authoritative settings host

Where an explicit `AIDE_Domain.yaml` entry governs/composes the effective Domain:

- that Domain entry is the **sole authoritative Domain metadata/settings host** for that Domain;
- an Index-hosted `Domain:` configuration for the same effective Domain is not merged; and
- duplicate/conflicting Domain host state is an error requiring reconciliation.

Index-hosted Domain configuration remains valid for an applicable **implicit** Domain where no
explicit Domain entry governs it.

For a Solution/Project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit Domain representation rather than modifying the native format solely to carry AIDE
configuration.

## Runtime recognition

No separately named Domain recognition registry is part of the current architecture.

Domain resolution may use:

- direct current semantic Item Type recognition;
- the optional generic Domain-neutral `ItemTypeRegistry` from `AIDE_Index@v2`;
- Domain-owned native Solution/Project recognisers;
- explicit Domain declaration parsing; and
- safe runtime caches.

For a semantic Item Type, recognition produces its identity/provisions only. Domain must compare
that recognised identity against the current approved recognition set before treating it as
Domain-eligible.

No semantic Item Type definition or `ItemTypeRegistry` entry may elevate itself to Domain authority.
Compiled/cached state is derived optimisation only. If its current authoritative provenance cannot
be established, refresh/directly evaluate or fail visibly rather than granting Domain authority.

## Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. Do **not** use “nearest marker wins”. Physical ancestry is a discovery path, not proof of
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
2. Collect local and enclosing Domain evidence through approved semantic/native/explicit
   recognition and authoritative containment/membership relationships.
3. While walking upward, inspect every crossed recognised structural boundary for applicable
   Domain-owned `Propagation: Stop`. Where Stop applies, exclude enclosing Domain evidence above the
   boundary from content below it and continue independent resolution.
4. Resolve applicable explicit Domain claims and validate every root's expected `Recognition`
   against independently observed approved recognition. A valid unambiguous explicit claim supplies
   the effective Domain for its governed/composed roots.
5. Otherwise apply authoritative containment: a contained approved structure participates in the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate remaining independent approved co-roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining approved root, return that implicit Domain.
8. If no approved recognition applies, return `No Domain context`.
9. If authoritative claims are contradictory or assignment remains ambiguous, return an
   unresolved/error result rather than merging, ranking or guessing.

## Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- an explicit root's expected recognition mismatches observed recognition;
- an explicit root uses unknown/unapproved recognition;
- two explicit Domains claim the same effective target without defined resolution;
- an explicit Domain entry and Index expose duplicate/conflicting Domain host state for the same
  effective Domain;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## Ownership boundaries

- **Core/Domain** owns the approved-recognition, context/resolution and Domain settings-host
  contract.
- **Core/Index** owns generic Index/Item/Item Type behaviour and the optional Domain-neutral
  `ItemTypeRegistry`.
- **Documentation Methodology** owns documentation-specific Index extensions and
  `DocumentationTopic` semantics.
- **Native Solution/Project systems** own their identities, memberships and internals; Domain
  observes only the minimum facts required for resolution.
- **Setting owners** own all setting semantics, including precedence and inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not duplicate them.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour.

## Deliberately absent from v3

This Standard does not define:

- generic Index as a Domain recognition;
- owner-self-declared Domain-capable Item Type flags;
- a separate Domain Recognition Registry;
- invented AIDE Solution/Project Item Types solely for Domain;
- implicit/generic child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository-as-Domain merely because a repository exists;
- a generic settings precedence/inheritance engine;
- a generic filesystem Propagation Stop marker or arbitrary unregistered-folder exclusion;
- a Domain-specific Tool; or
- broad platform-specific parser machinery beyond minimum recognition observations.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v2, AIDE_Scope@v1, AIDE_Migration@v1, Core_Domain_Design_v3
References: Core_System_Design_v8, Core_Index_Design_v2
<!-- END SOURCE: AIDE_Domain_Standard_v3.md -->

---

<!-- BEGIN SOURCE: Core_Bootstrap_Design_v3.md -->
# Core Bootstrap — Design

> **Version 3** (2026-09-01). Retains the thin Bootstrap/Profile/Contribution architecture while
> making effective Profile selection the startup-subset gate, defining Profile `Why` as rationale,
> making Contributions order-independent, and clarifying `{bootstrap}` as deliberately pre-Index
> discovery.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## §1 — Purpose and ownership

Bootstrap is the stable Core-owned activation seam between persistent platform-level instructions
and deployable AIDE guidance, Standards, Tools and other material.

It exists to let one small, rarely changing platform bootstrap support different AIDE subsets
without copying the current operating set into permanent platform instructions.

Core/Bootstrap owns:

- the stable persistent bootstrap contract;
- effective Bootstrap Profile resolution;
- Profile startup-set selection;
- Bootstrap Contribution discovery/eligibility;
- the order-independence contract for Contributions;
- the primitive `{bootstrap}` discovery cue; and
- the boundary between early awareness/checks and lazy full material.

Bootstrap does not own capability semantics, Scope, dependency semantics, deployment, package
acquisition, platform permission/authority or a generic startup-task engine.

## §2 — Stable layered model

The stable flow is:

```text
persistent platform bootstrap
        ↓
resolve one effective Bootstrap Profile, if any
        ↓
establish the Profile startup set
        ↓
process applicable Bootstrap Contributions belonging to that startup set
        ↓
load full detail lazily when current work requires it
```

The persistent instruction is deliberately tiny and changes rarely. It uses the strongest
persistent mechanism the platform supplies but must not claim stronger startup guarantees than the
platform actually provides.

## §3 — Bootstrap Profile

A Profile is an environment-specific startup map.

Each entry carries only:

```text
What
Why
Where
```

- **What** — identity/material to bring into the Profile startup set.
- **Why** — concise human/AI-readable rationale for why the Profile includes it.
- **Where** — locator/discovery information for the authoritative deployed material.

`Why` is **not executable conditional syntax** and does not create a Bootstrap applicability
language. Conditional applicability inside substantive capability behaviour uses the normal owner
and applicability mechanisms.

`Where` is a locator/discovery aid. It does not authorise installation, execution or acquisition of
arbitrary content.

A Profile may use the normal Dependencies mechanism for required-presence facts. Bootstrap does not
invent separate dependency syntax.

## §4 — Effective Profile and startup subset

At most one effective Bootstrap Profile applies by default.

If multiple competing Profiles are applicable and no governing composition rule exists, fail
visibly rather than inventing merge/precedence.

**No Profile is valid.** Its operational meaning is now explicit:

> No Profile means there is no Profile-selected AIDE startup set and therefore no automatic
> processing of deployed AIDE Bootstrap Contributions merely because those Contributions are
> physically available.

Physical deployment/availability is not startup selection.

This gate is what makes the stable bootstrap subset-neutral on a host where several AIDE subsets
may be deployed simultaneously.

## §5 — Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that needs best-effort early-session discovery
when its owning material/capability belongs to the effective Profile startup set.

A Contribution is separate from the owner's full detailed material and remains small enough to
process without eagerly loading that full material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/rationale; and
- where detailed owner material can be resolved when needed.

The owner defines the Contribution's substantive semantics. Bootstrap defines discovery,
eligibility and the order-independence contract.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

### Eligibility

A Contribution is eligible for automatic startup processing only when its owning material/capability
is brought into play by the effective Profile, unless a future explicitly defined persistent
bootstrap primitive says otherwise.

The mere presence of a deployed `{bootstrap}` block does not make it part of the startup set.

## §6 — Contributions are order-independent

Bootstrap Contributions are peer, order-independent early contributions.

A Contribution must not:

- require another peer Contribution to execute first;
- depend on a peer Contribution's startup side effects; or
- rely on platform file/discovery order as semantic sequencing.

Required material presence is expressed through the normal Dependencies mechanism.

If a future demonstrated startup case genuinely requires ordered actions, design that requirement
explicitly. Do not infer an ordering engine from current Contribution discovery.

## §7 — `{bootstrap}` is deliberately pre-Index

`{bootstrap}` is a primitive pre-capability/pre-Index discovery cue.

Bootstrap runs before richer AIDE Index/Item Type machinery can be assumed available. Its own
initial discovery must therefore not depend on Item Type recognition or on loading the generic
`ItemTypeRegistry`.

The two recognition mechanisms are intentionally separate:

```text
{bootstrap}
  → minimal early discovery cue

AIDE_Index / Item Types
  → richer semantic recognition after that machinery is available
```

This separation is architectural, not temporary duplication.

## §8 — Dependencies and missing requirements

Use `AIDE_Dependencies` for requirement/presence/version semantics.

If startup processing reveals required material is missing:

- surface the missing requirement;
- do not silently weaken or erase it;
- do not silently install/update/remove material; and
- hand remediation to the environment/deployment process authorised to change the host.

A startup presence check does not itself trigger a blanket Migration/current-version sweep.

A Deployment Set omission does not erase a semantic required-presence fact.

## §9 — Deployment and acquisition boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- Deployment Set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package/source acquisition; or
- deployment verification.

Trusted-source resolution, package acquisition and automatic remediation remain intentionally
undesigned. A Profile's `Where` field never grants authority to acquire/install content.

A future authorised deployment process may obtain missing required material from trusted configured
sources without changing this Bootstrap boundary.

## §10 — Context economy

Bootstrap is not a universal eager include.

A Profile should establish only:

- what belongs in the startup set;
- what must be recognised or checked early;
- what must merely be discoverable; and
- where authoritative detail can be resolved.

Load full Standards/Tools/guidance only when current work needs them, unless the Profile deliberately
selects that material as startup guidance.

Thin Bootstrap information and lazy detailed material are a first-class design requirement.

## §11 — Subset-neutral examples

The same persistent bootstrap may support, for example:

```text
General Working Profile
  → Principles + Working Practices

AIDE Development Profile
  → broader AIDE operating set

No Profile
  → no Profile-selected AIDE startup set
```

Several subsets may be physically deployed to the same host. Only the effective Profile selects
which subset participates in Profile-driven startup processing.

## §12 — Intended output

This Design produces the canonical AI-facing Bootstrap contract:

```text
AIDE_Bootstrap@v2
```

Exact platform rendering of the persistent instruction, Profile and Contributions belongs to
Build/AI Deployment and must preserve these semantics without adding platform-specific behaviour to
Core.

## §13 — Deliberately deferred

- Profile merging/composition.
- Generic startup-task orchestration.
- Ordered Contribution execution.
- Automatic source/package acquisition.
- Trusted package catalogs.
- Generic installer behaviour.
- Broad startup migration scans.
- Full Standards/Tools inside Bootstrap Contributions.
- Item Type dependence for initial `{bootstrap}` discovery.
- Platform-specific enforcement beyond demonstrated capability.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Dependencies
References: Core_System_Design_v8, Core_Bootstrap_Decisions_v3
<!-- END SOURCE: Core_Bootstrap_Design_v3.md -->

---

<!-- BEGIN SOURCE: Core_Bootstrap_Decisions_v3.md -->
# Core Bootstrap — Decisions

> **Version 3** (2026-09-01). Preserves the v2 Bootstrap decision history and records effective
> Profile gating, no-Profile startup behaviour, non-executable `Why`, order-independent
> Contributions and the deliberately pre-Index role of `{bootstrap}`.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

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

## D15 — Effective Profile gates the Contribution startup set

**Decision.** The effective Bootstrap Profile defines the Profile-selected AIDE startup set.
Automatic startup processing considers only applicable Contributions whose owning material/
capability is brought into play by that set, unless a future explicit persistent primitive defines
an exception.

**Reason.** Physical deployment is availability, not startup intent. Without Profile gating, a host
with several deployed AIDE subsets would activate all available Contributions and cease to be
subset-neutral.

## D16 — No Profile does not activate every deployed Contribution

**Decision.** No Profile remains a valid state, but it means there is no Profile-selected AIDE
startup set and therefore no automatic processing of deployed AIDE Bootstrap Contributions merely
because they are physically available.

**Reason.** “No Profile” must not silently mean “all deployed AIDE”. That would invert the purpose
of Profile selection.

## D17 — Profile `Why` is rationale, not applicability syntax

**Decision.** `Why` is concise human/AI-readable rationale for including a Profile entry. It is not
an executable conditional expression and creates no second Scope/applicability language.

**Reason.** Bootstrap needs an explanation for startup selection, not a new rule engine. Conditional
behaviour remains with the substantive owner and normal applicability mechanisms.

## D18 — Bootstrap Contributions are order-independent

**Decision.** Peer Bootstrap Contributions must not require another Contribution to have executed
first or depend on peer startup side effects. Required material presence is expressed through the
normal Dependencies mechanism.

**Reason.** No demonstrated need justifies a startup orchestration/order engine, and platform file
order is not a stable semantic contract.

**Consequence.** If a future startup case genuinely requires ordered actions, design that mechanism
explicitly rather than extending current Contributions implicitly.

## D19 — `{bootstrap}` deliberately remains pre-Index

**Decision.** `{bootstrap}` is a primitive pre-capability/pre-Index discovery cue and does not depend
on Item Type recognition for its own initial discovery.

**Reason.** Bootstrap runs before richer AIDE Index/Item Type machinery can be assumed available.
Requiring that machinery to discover Bootstrap would create a circular startup dependency.

**Consequence.** `{bootstrap}` discovery and Item Type recognition remain intentionally separate.

## D20 — Issue Bootstrap v2

**Decision.** Publish the corrected runtime contract as `AIDE_Bootstrap@v2` with migration posture
`None`.

**Reason.** The startup selection semantics change, but no automatic transformation of existing
governed artefacts is required solely because the Bootstrap release changed.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Dependencies, Core_Bootstrap_Design_v3
References: Core_System_Decisions_v7
<!-- END SOURCE: Core_Bootstrap_Decisions_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Bootstrap_Standard_v2.md -->
# AIDE Bootstrap — Standard

> **Identity:** `AIDE_Bootstrap@v2`
> **Common name:** Bootstrap
> **Version 2** (2026-09-01). Makes effective Profile selection the startup-set gate, defines
> Profile `Why` as rationale, makes Contributions order-independent, and clarifies `{bootstrap}` as
> deliberately pre-Index while retaining thin/lazy subset-neutral Bootstrap.
>
> **Default weight:** Requirement

## Purpose

Keep AIDE's platform-level activation instruction small and stable while allowing each environment
to select a changeable startup subset through a Bootstrap Profile and thin component Bootstrap
Contributions.

## Stable bootstrap contract

Use the strongest persistent instruction mechanism the platform provides.

The persistent bootstrap shall:

1. resolve one effective Bootstrap Profile where available;
2. establish the Profile-selected startup set;
3. process applicable `{bootstrap}` Contributions only for owning material/capabilities brought
   into play by that startup set;
4. continue normally where no Profile exists without automatically processing unrelated deployed
   AIDE Contributions; and
5. load full detail lazily when current work requires it.

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

- **What** — identity/material to bring into the Profile startup set.
- **Why** — concise human/AI-readable, non-executable rationale for why the Profile includes it.
- **Where** — locator/discovery information for the authoritative deployed material.

`Why` is not executable conditional syntax and does not create a Bootstrap Scope/applicability
language. Conditional applicability inside substantive capability behaviour uses the normal owning
mechanisms.

`Where` identifies how material can be resolved; it does not grant permission to execute, acquire or
install arbitrary content.

A Profile may use normal Dependencies metadata to declare required presence. Bootstrap does not
create separate dependency syntax.

One effective Profile applies by default. If multiple competing Profiles are applicable and no
governing composition rule exists, surface the conflict rather than inventing precedence.

### No Profile

No Profile is valid.

No Profile means:

```text
no Profile-selected AIDE startup set
→ no automatic processing of deployed AIDE Bootstrap Contributions merely because they are present
```

Physical deployment/availability is not startup selection. When no Profile resolves, unrelated
deployed Contributions are not processed automatically.

## Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that requires best-effort early-session
discovery when its owning material/capability belongs to the effective Profile startup set.

A Contribution shall be separate from the owner's full detailed material and remain short enough
to process without eagerly loading that material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/rationale; and
- where detailed owner material can be resolved if needed.

The owner defines the Contribution's substantive semantics. Bootstrap defines only discovery,
eligibility and the order-independence contract.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

### Eligibility

A Contribution is eligible for startup processing only when its owning material/capability is
selected into the effective Profile startup set, unless a future explicitly defined persistent
bootstrap primitive says otherwise.

### Order independence

Bootstrap Contributions are order-independent.

A Contribution must not:

- require another peer Contribution to have executed first;
- depend on another peer Contribution's side effects; or
- use platform file/discovery order as semantic sequencing.

Express required material presence through `AIDE_Dependencies`.

If a future demonstrated startup case requires ordered actions, design that requirement explicitly;
do not infer a startup ordering engine from current Contributions.

## `{bootstrap}` versus Item Type recognition

`{bootstrap}` is deliberately a primitive pre-capability/pre-Index discovery cue.

Bootstrap runs before richer AIDE Index/Item Type machinery can be assumed available, so its own
initial discovery must not depend on Item Type recognition or `ItemTypeRegistry`.

The Bootstrap cue and Item Type recognition mechanisms are intentionally separate.

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
- hand remediation to the environment/deployment process authorised to change the host.

A startup presence check does not itself trigger a blanket migration/current-version sweep.

## Deployment boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- Deployment Set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package acquisition; or
- deployment verification.

A future authorised deployment process may obtain a missing requirement from trusted configured
sources. This Standard does not define that acquisition mechanism.

## Startup tasks

No generic startup-task or Contribution-ordering engine exists in v2.

Use Profile selection, order-independent thin owner Contributions and startup-required dependency
checks. Add another mechanism only after a demonstrated startup need cannot be represented cleanly
through these contracts.

## Subset-neutral operation

The same persistent bootstrap may activate, for example:

```text
General Working
  → Principles + Working Practices

AIDE Development
  → broader AIDE operating set

No Profile
  → no Profile-selected AIDE startup set
```

Several AIDE subsets may be physically deployed at once without all becoming startup-active.

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
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Dependencies
References: Core_Bootstrap_Design_v3, Core_System_Design_v8
<!-- END SOURCE: AIDE_Bootstrap_Standard_v2.md -->
