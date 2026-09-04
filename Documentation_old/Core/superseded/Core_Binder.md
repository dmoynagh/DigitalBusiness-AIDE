# Core Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.

## Binder manifest

- `Core_Index_v3.md` — sha256 `53f872f0099a`
- `Core_System_Design_v6.md` — sha256 `777f04693f7e`
- `Core_System_Decisions_v5.md` — sha256 `5dacfae99a2f`
- `Core_Domain_Design_v1.md` — sha256 `a2a4b700400b`
- `Core_Domain_Decisions_v1.md` — sha256 `f4590f0937dc`
- `AIDE_Domain_Standard_v1.md` — sha256 `271e2c561c96`
- `Core_Bootstrap_Design_v2.md` — sha256 `ac7505e45cb1`
- `Core_Bootstrap_Decisions_v2.md` — sha256 `4535c9d7e0a3`
- `AIDE_Bootstrap_Standard_v1.md` — sha256 `ff71a00d2eda`

---

<!-- BEGIN SOURCE: Core_Index_v3.md -->
# Core — Index

> **Version 3** (2026-08-31). Registers Bootstrap as a Core system foundation and records
> Principles and Working Practices as top-level independently deployable AIDE guidance concerns.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic:** Core  
**Project container / master folder:** `AIDE/Core/`

Core holds the system-wide foundations and the reference view of the AIDE structure. Development
and product Domains remain consumers of AIDE rather than children of the Core corpus.

## Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Core | None | `Core` | independent | expanded |
| Domain | Core | `Core_Domain` | inherits | expanded |
| Bootstrap | Core | `Core_Bootstrap` | inherits | expanded |

## Local configuration

None.

## Document register

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Core_Index` | v3 | Index | established | Current |
| `Core_System_Design` | v6 | Design | established | Current |
| `Core_System_Decisions` | v5 | Decisions | established | Current |
| `Core_Domain_Design` | v1 | Design | established | Current |
| `Core_Domain_Decisions` | v1 | Decisions | established | Current |
| `AIDE_Domain_Standard` | v1 | Standard | established | Current |
| `Core_Bootstrap_Design` | v2 | Design | established | Current |
| `Core_Bootstrap_Decisions` | v2 | Decisions | established | Current |
| `AIDE_Bootstrap_Standard` | v1 | Standard | established | Current |

### Withdrawn, renamed or rehomed

None.

## Core subtopics

| Subtopic | Core role | Authoritative design | Canonical outcome |
|---|---|---|---|
| Domain | System-wide operating/governance-context foundation | `Core_Domain_Design_v1` | `AIDE_Domain@v1` |
| Bootstrap | Stable AIDE activation/startup foundation | `Core_Bootstrap_Design_v2` | `AIDE_Bootstrap@v1` |

Development/product Domains are consumers of AIDE and are not Core subtopics or components of the
AIDE system tree.

## Project-container map

| Canonical concern | Master folder / GPT Project |
|---|---|
| Core | `Core` |
| Principles | `Principles` |
| Working Practices | `Working Practices` |
| Project Design | `Design Project` |
| Build | `Build` |
| Capabilities | `Capabilities` |
| AI Deployment | `AI Deployment` |
| Documentation Methodology | `Document Methodology` |
| Generated common bundle | `bundles` |

Project-container boundaries are operational context boundaries; they do not have to mirror the
conceptual ownership tree one-for-one.

## Assets register

None.

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: Core_System_Design_v6, Core_Domain_Design_v1, Core_Bootstrap_Design_v2
<!-- END SOURCE: Core_Index_v3.md -->

---

<!-- BEGIN SOURCE: Core_System_Design_v6.md -->
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
<!-- END SOURCE: Core_System_Design_v6.md -->

---

<!-- BEGIN SOURCE: Core_System_Decisions_v5.md -->
# Core System — Decisions

> **Version 5** (2026-08-31). Adds the Bootstrap Profile/Contribution model and records
> Principles and Working Practices as top-level independently deployable AIDE guidance.
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


---
Dependencies: !AIDE_DocumentationMethodology@v19, Core_System_Design_v6
References: AIDeployment_Decisions_v1, ProjectDesign_Decisions_v1, Build_Decisions_v1, Core_Domain_Decisions_v1, Core_Bootstrap_Decisions_v2, Principles_Decisions_v3, WorkingPractices_Decisions_v2
<!-- END SOURCE: Core_System_Decisions_v5.md -->

---

<!-- BEGIN SOURCE: Core_Domain_Design_v1.md -->
# Core Domain — Design

> **Version 1** (2026-08-31). First blank-sheet issuance of the AIDE Domain model.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Domain defines the common AIDE concept used to identify the named operating/governance context
within which work is being performed.

A Domain gives AIDE one stable term for a boundary that may physically be represented by an Index,
solution, project, explicit Domain declaration, or another recognised structure added later.

Domain belongs under **AIDE Core** because Project Design, Build, Capabilities, AI Deployment,
Documentation Methodology and future AIDE concerns may all consume Domain context.

Core/Domain owns:

- the meaning of Domain;
- recognised Domain-defining structures and the minimum relationships needed to resolve them;
- implicit versus explicit Domain formation;
- Domain discovery and resolution;
- Domain naming/alias conventions needed for navigation and resolution;
- the Domain settings-host and Branch conventions; and
- deterministic ambiguity/failure behaviour.

Individual development/product Domains remain outside the AIDE system tree. They consume AIDE and
retain ownership of their own substantive work and domain-specific workflows.

### Blank-sheet status

This Design is a new model. Earlier `AIDE_Domain` design/decision documents were never implemented
and impose **no compatibility, migration, schema or behavioural requirements** on this Design.
Useful historical reasoning may be reconsidered independently, but no earlier mechanism is carried
forward merely because it existed.

### Declared output

This Design is intended to produce one canonical AI-facing Domain Standard:

```text
AIDE_Domain@v1
```

The canonical Standard should be deployable wherever AIDE may need Domain resolution, including
Design-side and Build-side environments. No dedicated Domain Tool is currently demonstrated.

---

## §2 — Level 1 model

A **Domain is a named AIDE operating/governance context**.

It exists to provide:

1. **one vocabulary for a contextual boundary** — AIDE can refer to "the Domain" whether the
   physical structure is an Index, solution, project or explicit declaration;
2. **a common Domain settings host** — independently owned settings can be stored in a predictable
   Domain-relative location without Domain taking ownership of their semantics; and
3. **explicit composition/clarification** — where existing structures do not themselves express the
   intended larger or different Domain.

A Domain is semantic, not inherently an artefact.

```text
Domain
├── implicit  — inferred from recognised authoritative structure
└── explicit  — declared when the natural interpretation is insufficient or wrong
```

AIDE operation does not require a Domain to exist. "No Domain context" is a legitimate state.

---

## §3 — Domain is contextual, not artefact-owned

An artefact normally does **not** declare its Domain.

Domain membership is resolved from the target artefact's or work target's authoritative structural
context when Domain information is required.

A document therefore does not normally need to know:

- the Domain's current name;
- whether a Domain exists; or
- how the Domain was resolved.

Do not resolve Domain merely because an artefact exists. Resolve it when the current operation
needs Domain context.

### Relative Domain references

Where the actual name is not part of the meaning, documents, Standards and Tools should refer to:

```text
the Domain
```

meaning the effective Domain resolved for the current target/context.

This is preferred to embedding the current Domain name and avoids unnecessary rename coupling.

Explicit Domain names are appropriate where identity itself matters, such as:

- navigation/conversation;
- explicit composition;
- cross-Domain reference;
- provenance where required; or
- an explicit Domain declaration.

---

## §4 — Domain identity, names and aliases

An implicit Domain takes its name/identity from the authoritative recognised structure that
establishes it.

Examples:

- an Index-backed Domain uses the Index's declared project/topic identity;
- a solution-backed Domain uses the solution's recognised identity;
- a standalone project-backed Domain uses the project's recognised identity.

Filename matching may be used as a discovery hint, but an available authoritative declared identity
wins.

Where rename continuity or alternate lookup names are needed, the Domain's authoritative metadata
representation may record previous names/aliases. These exist primarily for human/AI navigation,
reference resolution and continuity.

Do not require ordinary member artefacts to be rewritten merely because the Domain is renamed.

The exact alias field names and formal identity representation are Standard/schema details. They
must preserve Core's general formal-identity principles where formal referenceable identity is
required.

---

## §5 — Recognised Domain-defining structures

The initial demonstrated Domain-capable structure types are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

Domain owns enough recognition knowledge to resolve these consistently wherever the Domain Standard
is deployed.

It does not absorb their full semantics.

Examples:

- Domain needs to know that a solution authoritatively contains its member projects; it does not
  own build/compilation semantics.
- Domain needs to know that a root Index may have delegated/child Indexes; Documentation
  Methodology still owns Index/register behaviour.

Additional Domain-capable structure types are added only when a demonstrated use case warrants
them.

A repository/worktree is currently a recognised **discovery boundary**, not automatically a
Domain-defining structure.

---

## §6 — Natural containment and structural children

Recognised authoritative containment is preserved.

Example:

```text
Foo.sln
├── Foo.Api.csproj
├── Foo.Core.csproj
└── Foo.Tests.csproj
```

resolves as one `Foo` Domain where those projects are members of the solution.

Likewise:

```text
Capabilities_Index
├── Review_Index
└── Migration_Index
```

remains one `Capabilities` Domain where the child Indexes are delegated/contained by the root
Index.

### No implicit child Domains

A contained structure does **not** create another Domain merely because it could independently act
as a root.

Therefore:

- a project contained by a solution is not a child Domain;
- a delegated/child Index is not a child Domain;
- another recognised structure inside an effective Domain does not create a child Domain solely
  because it exists.

A child Domain would require an explicit Domain declaration.

Child-Domain semantics, including inheritance, settings propagation, nesting, precedence and
parent/child composition, are deliberately **not designed** until a real use case establishes the
need.

---

## §7 — Co-root structures and identity matching

Recognised Domain-capable structures sharing a physical root are evaluated by authoritative
identity and recognised relationships, not proximity alone.

### Matching identity

Where co-root recognised structures have the same authoritative identity, they form one implicit
Domain.

Example:

```text
Foo.sln
Foo_Index
```

where the Index declares project/topic identity `Foo`:

```text
→ Foo Domain
```

When a matching Index coexists with a solution/project:

- the Index is the preferred AIDE Domain metadata/settings host;
- the solution/project retains authority over its native structure and membership; and
- the Index does not become the owner of the solution/project.

This provides an AIDE-controlled overlay for settings and Domain metadata without requiring the
native project/solution format to carry AIDE-specific configuration.

### Different identity

Co-root recognised structures with different identities remain separate implicit Domains by
default.

```text
Foo.sln
Womble_Index
```

means:

```text
Foo Domain
Womble Domain
```

Likewise, multiple standalone project files in one folder with no enclosing solution are separate
implicit Domains by default.

```text
Foo.csproj
Bar.csproj
```

means:

```text
Foo Domain
Bar Domain
```

If the intended reality differs from these defaults, use an explicit Domain declaration.

---

## §8 — Domain membership versus native/corpus membership

Domain membership and a constituent structure's native membership are different questions.

A solution remains authoritative for which projects belong to it.

An Index remains authoritative for which documents are registered in its governed corpus and for
its document/topic/type configuration.

The Domain provides the wider AIDE operating boundary.

Therefore, AIDE-governed artefacts structurally contained within an **unambiguous** effective Domain
may resolve to that Domain even when they are not members of the native solution/project registry.

Example:

```text
Foo.sln
Foo_Architecture_Design_v3.md
Foo_WorkPackage_...
```

The AIDE documents may resolve to the `Foo` Domain while Documentation Methodology separately
determines how/where they are registered and governed as documents.

This distinction prevents Domain from duplicating Index or native project/solution membership
semantics.

### Shared physical containers

A physical folder may legitimately contain several Domains.

Where several Domains share a physical container, location alone is insufficient to assign an
otherwise ambiguous artefact. Domain resolution must use stronger evidence such as:

- authoritative identity;
- recognised native containment;
- Index relationship; or
- an explicit Domain declaration.

Do not guess from proximity.

---

## §9 — Explicit Domains

Use an explicit Domain declaration when the implicit structural interpretation is incomplete,
ambiguous or intentionally different.

Examples include:

- several solutions form one product Domain;
- several standalone projects form one Domain;
- a differently named Index and solution form one Domain;
- several solutions plus a documentation Index form one Domain; or
- structures that would otherwise match implicitly are deliberately separated.

An explicit Domain composes or clarifies recognised roots. It does not recreate their internal
registries.

### `AIDE_Domain.yaml`

Explicit Domain declarations use an AIDE-owned YAML representation named:

```text
AIDE_Domain.yaml
```

One physical location has one such declaration container.

The file is capable of holding multiple independent Domain declarations:

```yaml
Domains:
  - ...
  - ...
```

Each array element is a separate Domain declaration.

Two Domain entries being stored in the same file implies no parent/child, composition, inheritance
or other relationship between them.

This allows several explicit Domains to coexist at one physical location without inventing
multiple Domain filenames.

The canonical Standard/schema should define a small deterministic structured representation.
Domain declarations should contain only information Domain owns or hosts, such as:

- Domain identity/current name and aliases/previous names where needed;
- the recognised roots being explicitly composed/clarified; and
- Domain settings/Branch setting declarations.

Do not place Tags, Standards applicability, Build behaviour, Deployment behaviour, document
membership or native project membership into Domain simply because the declaration file is
available.

---

## §10 — Domain settings host

Domain does **not** define Domain settings.

It defines only the standard location, representation and coexistence conventions by which setting
owners may place settings in Domain context.

The owner of a setting defines:

- setting name/schema;
- allowed values;
- meaning;
- defaults;
- validation;
- consumption;
- precedence; and
- any inheritance/override/combination behaviour.

Domain must not become a generic configuration engine.

### Root settings

A setting declaration with no Branch is attached to the Domain root:

```yaml
Settings:
  SomeSetting:
    ...
```

### Branch settings

A setting declaration may be attached to a structural subtree using `Branch`:

```yaml
Branch: docs/api
Settings:
  SomeSetting1:
    ...
  SomeSetting2:
    ...
```

`Branch` means a Domain-relative structural location/subtree.

Domain defines the Branch attachment convention. It does not define what a setting owner does with
declarations found at different Branches.

Exact Branch path normalization/serialization is a Standard/schema detail and should remain small.

### Preferred hosts

Typical authoritative hosts are:

```text
Index-backed implicit Domain
→ root Index may host Domain settings

solution/project + matching Index
→ Index is preferred Domain metadata/settings host

explicit Domain
→ the Domain entry in AIDE_Domain.yaml hosts Domain settings
```

A solution/project-only Domain that needs Domain metadata/settings may introduce an explicit Domain
representation rather than modifying native project formats merely to carry AIDE configuration.

---

## §11 — Discovery is target-based and upward

Domain resolution begins from the current target or focus, not from a global session Domain.

One session may work with artefacts from different Domains.

Starting from a target artefact, project or focused folder, Domain discovery examines the local and
available enclosing structural context.

A local recognised structure is only a **candidate implicit Domain root** until discovery
establishes that it is not incorporated into an enclosing authoritative Domain.

Example:

```text
/Product
  Product.sln
  /src
    /Foo
      Foo.csproj
      /Handlers   ← current focus
```

If `Foo.csproj` is a member of `Product.sln`, the effective Domain is `Product`, not `Foo`.

Likewise, a solution must be checked for an applicable enclosing explicit Domain before it
establishes its own implicit Domain.

### Do not stop at the first marker

Upward discovery is not "nearest marker wins".

It collects enough available evidence to determine the effective authoritative Domain boundary.

Physical ancestry is a discovery path, not proof of composition.

---

## §12 — Discovery boundaries

Upward discovery must not scan indefinitely.

Search through the available enclosing path only as far as the nearest meaningful operational
discovery boundary appropriate to the current context.

Common boundaries include:

- an explicitly supplied search/discovery boundary;
- workspace/container root;
- repository/worktree root;
- user Documents root;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- another recognised user/application storage root; and
- filesystem/mount root as the final fallback.

The exact platform mechanism for identifying these boundaries may vary, but Domain semantics remain
the same.

A discovery boundary limits **searching**. It does not limit what an explicit Domain declaration may
reference if the Standard permits that reference.

For example, an explicitly declared Domain may compose roots from two repositories without
requiring ordinary upward discovery to search beyond each repository root.

---

## §13 — Resolution model

For a target/focus:

```text
target
  ↓
discover local + enclosing Domain evidence within discovery boundary
  ↓
applicable explicit Domain declaration?
  yes → use declared Domain
  no
  ↓
recognised authoritative containment?
  yes → inherit enclosing effective Domain
  no
  ↓
matching co-root recognised identities?
  yes → one implicit Domain
  no
  ↓
independent recognised root?
  yes → implicit Domain
  no
  ↓
no Domain context
```

The resolver uses semantic relationships, not directory proximity alone.

### Ambiguity and contradiction

Fail visibly rather than guess where:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership and does not
  clearly state the intended override;
- several co-located Domains leave an artefact's Domain ambiguous; or
- a referenced Domain/root cannot be resolved reliably.

No generic precedence/merge framework is introduced to hide conflicting Domain claims.

### No Domain

`No Domain context` is a normal result.

It means Domain-scoped context/settings are unavailable. It does **not** mean AIDE is disabled or
that an AIDE-governed document is invalid.

---

## §14 — Relationship to other AIDE concerns

### Core

Core owns Domain as a system-wide foundation and owns the wider formal identity convention.

### Project Design

Project Design may consume Domain context while defining work. Domain does not own the design
workflow; the development/product Domain retains ownership of how Project Design, Build and other
AIDE services are composed for its work.

### Build

Build may resolve Domain from repository/workspace/project/solution context when Domain information
is relevant. Domain behaviour is not redefined separately on Build side.

### Documentation Methodology

Documentation Methodology owns document naming, Index/register mechanics, corpus lifecycle and
document metadata hosting.

Domain may recognise a root Index as a Domain-defining structure and may use the Index as a Domain
settings host. That does not transfer Index semantics into Domain.

### Capabilities

Tags, Scope, Dependencies, Migration, Review, Standards and Tools retain their existing owners.
Domain does not select Standards or duplicate applicability/configuration mechanisms unless a
future demonstrated requirement creates a separate Domain-owned need.

### Environment / AI Deployment

Environment supplies current factual platform/runtime/access information. AI Deployment owns
deployment composition/reconciliation/verification. Domain may host owner-defined settings consumed
by these concerns, but does not own their semantics or operational state.

---

## §15 — Deliberately deferred

The following are not part of v1 Design until demonstrated by a real use case:

- child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository as an implicit Domain-defining structure merely because it is a repository;
- a generic settings precedence/inheritance engine;
- a Domain-specific Tool where the Standard alone is sufficient;
- broad exclusion syntax merely to counteract defaults that can instead be clarified explicitly;
- detailed platform parsers beyond the minimum needed to implement recognised structures; and
- Branch path complexity beyond demonstrated structural-location needs.

---

## §16 — Success signals

The model is successful when:

- the same target resolves to the same Domain across AIDE surfaces given the same observable
  structures;
- simple Index-, solution- and project-backed work needs no Domain file;
- same-name co-root structures naturally converge;
- different-name co-root structures remain separate unless explicitly composed;
- nested project/folder focus resolves to its real enclosing Domain rather than the nearest local
  marker;
- Domain settings have a predictable host without Domain owning their semantics;
- Domain renames do not require rewriting ordinary member documents;
- member artefacts normally carry no Domain metadata;
- existing Index/native membership mechanisms are not duplicated;
- ambiguity fails visibly; and
- the model remains useful with no child-Domain or generic configuration machinery.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: DocumentationMethodology_Design_v15, AIDE_ProjectDesign@v1
<!-- END SOURCE: Core_Domain_Design_v1.md -->

---

<!-- BEGIN SOURCE: Core_Domain_Decisions_v1.md -->
# Core Domain — Decisions

> **Version 1** (2026-08-31). Records the confirmed blank-sheet decisions establishing Domain as
> a Core-owned contextual boundary, discovery and settings-host contract.
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

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_Domain_Design_v1, Core_System_Design_v4
References: DocumentationMethodology_Design_v15, AIDE_ProjectDesign@v1
<!-- END SOURCE: Core_Domain_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Domain_Standard_v1.md -->
# AIDE Domain — Standard

> **Identity:** `AIDE_Domain@v1`
> **Common name:** Domain
> **Version 1** (2026-08-31). First canonical Domain contract produced from the blank-sheet
> `Core_Domain_Design_v1`.
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
implicit  — established from recognised authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify recognised roots
```

The initial recognised Domain-capable structure types are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

Domain owns only the recognition and structural relationships needed for Domain resolution. The
recognised structure's owner retains its native semantics and membership rules.

A repository/worktree is a discovery boundary in v1, not an implicit Domain type.

## Natural containment

Authoritative structural containment prevents a contained recognised structure from establishing a
second implicit Domain.

- a project that is a member of a solution remains in the solution Domain;
- a delegated/child Index remains in its enclosing root Index Domain; and
- another recognised structure inside an effective Domain does not create a child Domain merely
  because it could act as a root when isolated.

Structural children never create child Domains implicitly. Child-Domain inheritance, settings
propagation, nesting, precedence and parent/child composition are undefined in v1. If a distinct
child Domain is required, use an explicit declaration and require the result to be unambiguous.

## Co-root recognised structures

Evaluate recognised structures sharing a physical root by authoritative identity and structural
relationships, not proximity alone.

### Matching identity

Co-root structures with matching authoritative identities form one implicit Domain.

```text
Foo.sln + Foo_Index  → Foo Domain
```

An available declared Index project/topic identity is authoritative over filename-only matching.
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
- `Type` — one of `Index`, `Solution`, or `Project` for each explicit root in v1.
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
authoritative project/topic identity and `Roots` are not repeated. Documentation Methodology owns
the Index's document/configuration rendering; Domain owns the meaning of this Domain configuration
payload.

For a solution/project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit `AIDE_Domain.yaml` representation rather than modifying the native format solely to carry
AIDE configuration.

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
4. Otherwise apply authoritative containment: a contained project/Index/recognised structure
   inherits the enclosing effective Domain rather than creating another implicit Domain.
5. Evaluate co-root independent recognised roots: matching authoritative identities converge;
   different identities remain separate.
6. If the target belongs unambiguously to one remaining independent recognised root, return that
   implicit Domain.
7. If no Domain-capable structure applies, return `No Domain context`.
8. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
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
- **Documentation Methodology** owns Index/register/document corpus behaviour and document/config
  rendering.
- **Project/solution systems** own native membership and project/build-system semantics.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## Deliberately absent from v1

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
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Scope@v1, AIDE_Migration@v1, Core_Domain_Design_v1
References: Core_System_Design_v5
<!-- END SOURCE: AIDE_Domain_Standard_v1.md -->

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
