# Capabilities — Design

> **Version 3** (2026-08-28). Replaces design-side platform outcome generation with canonical
> capability production followed by Build WorkPackage handoff and build-side platform
> realisation. Adds Build Config and Deployment Set, and embeds transition declarations in the
> canonical Standard/Tool for build-side extraction and adaptation.
>
> This document states the current position. Historical and superseded positions remain in
> `Capabilities_Decisions` v9.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## §1 — Scope

This design defines the parent architecture for reusable AI-facing capability infrastructure
within AIDE. It establishes component responsibilities, contracts, and the principal flows from
capability design through canonical production, Build handoff, platform realisation, packaging,
deployment, runtime dependency/migration behaviour, and review.

Each component develops detailed design beneath this parent. A component design may add internal
structure but may not silently take ownership assigned elsewhere here.

---

## §2 — Architectural model

Capabilities has seven peer components:

```text
Capabilities
├── Standards
├── Tools
├── Scope
├── Dependencies
├── Migration
├── Deployment
└── Review
```

Standards and Tools define capability kinds and canonical production. Scope, Dependencies,
Migration, Deployment, and Review provide shared behaviour.

Build execution is not an eighth Capabilities component. The generic design-side-to-build-side
handoff and WorkPackage lifecycle belong to AIDE Build. Capabilities consumes that mechanism.

### Governing principles

- **One owner per mechanism.**
- **Capability meaning before platform realisation.**
- **Design-side outputs are self-contained for handoff.**
- **Generic platform implementation knowledge belongs Build side.**
- **Build is capability-local; Deployment is set-aware.**
- **Declared transitions before inferred deltas.**
- **Topic placement is ownership, not side exclusivity.**

---

## §3 — Capability design and canonical production

The common design-side flow is:

```text
Capability Design
      ↓
Build Capability
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage
```

### Capability Design

The Capability Design contains the complete generic capability design.

Where a particular platform requires capability-specific behaviour or constraint, the Design may
contain a platform-specific section. Platform sections are **delta-only**. Their absence means
the generic design applies unchanged.

Platform sections state capability-specific intent, not generic implementation mechanics. For
example, a Tool may require a particular discoverability behaviour on Claude; the Design does
not need to know that Claude may realise that behaviour using a skill or plugin.

A separate platform Design document is not required by the architecture. It may be introduced as
a scaling choice if platform-specific design material becomes independently substantial.

### Build Capability

`Build Capability` consumes the Capability Design and produces the canonical Standard and/or
Tool outcomes declared by that Design.

The canonical outcome carries:

- the complete generic capability definition;
- any capability-specific platform addenda required by the Design;
- Required Migration and On-Update declarations applicable to that capability/version.

The canonical outcome is the authoritative capability artefact passed into Build. Build side
does not normally reopen the internal Capability Design.

---

## §4 — Build Config

Every buildable capability has an effective **Build Config**.

It declares:

- **Platforms** — explicit target platforms or the current supported-platform default set.
- **Side** — Design, Build, or both; default is **both**.
- **Deployment Set(s)** — named logical deployment destinations/groupings.

Build Config describes intended production and placement. It does not encode generic platform
implementation mechanics such as plugin structures, repository paths, bundle assembly rules, or
platform-specific file formats.

Build Config may be stored and managed on Design side or Build side according to working
preference. By WorkPackage execution time there must be one resolved effective configuration.
Operational storage location does not transfer authority over capability intent.

---

## §5 — Build WorkPackage handoff

The canonical capability and its effective Build Config are used to create a **Build
WorkPackage** under the AIDE Build/WorkPackage Standard.

The WorkPackage contains everything capability-specific required for execution, including the
canonical Standard/Tool files and effective build/deployment intent.

The Build-side environment supplies reusable knowledge such as platform build Standards, Tools,
references, package builders, and deployment builders.

### Handoff rule

**If Build side must reopen the Capability Design to understand what result is required, the
WorkPackage is incomplete.**

Conversely, generic Claude/Codex/ChatGPT implementation mechanics do not belong in the
WorkPackage merely to make it self-contained; they belong in the Build-side capability/platform
Standards and Tools available to the executor.

WorkPackage execution returns a WorkPackage Outcome under the Build methodology. The generic
return contract is not owned by Capabilities.

---

## §6 — Build-side platform realisation

Build side combines:

```text
Canonical Standard / Tool
        +
capability-specific platform addenda
        +
effective Build Config
        +
Build WorkPackage
        +
platform Build Standards / Tools / references
        ↓
Platform contribution(s)
```

A **Platform Contribution** is the capability-local implementation material produced for a
target platform. It may not be independently deployable because Deployment may need to assemble
many contributions into one Deployment Set artefact.

Generic platform adaptation belongs entirely on Build side. The design side does not need to
know whether a platform uses skills, plugins, configuration files, command collections, merged
context files, or another representation.

Platform builders may extract and adapt capability content, scope information, command
definitions, and migration information according to the Standards governing that platform.

---

## §7 — Standards

Standards defines what a Standard is, how it is structured and weighted, how canonical Standard
outcomes are built, and how sessions operate under applicable Standards.

Standards publishes at least:

- **Standards Production Standard**
- **Standards Usage Standard**

The Production Standard governs canonical Standard authoring/build. Platform adaptation is
governed by Build-side platform Standards rather than embedded in each Standard Design.

Standards declares applicability through Scope, dependencies through Dependencies, transition
declarations under Migration's model, and uses Review profiles for assessment.

---

## §8 — Tools

Tools defines invokable capability behaviour and its logical commands.

A canonical Tool contains the platform-independent behaviour and command semantics, plus any
capability-specific platform addenda. Build-side platform Standards determine how those logical
commands are represented and invoked on the target platform.

A Standard may describe a procedure but may not define a named invokable action. Standards and
Tools may be sibling outcomes from one Design.

---

## §9 — Scope

Scope answers:

> **Should this capability be considered or applied in this context?**

The current two-layer model remains provisional pending the Scope component review:

1. deterministic/mechanical applicability;
2. reasoned/context applicability.

The Scope review must distinguish runtime applicability from:

- Build Config platform targeting;
- Design/Build side targeting;
- Deployment Set membership;
- platform retrieval/discovery implementation.

Those concerns may inform one another but are not assumed to be one mechanism.

No generic platform implementation technique belongs in a Capability Design merely because
Scope needs to be realised effectively on that platform.

---

## §10 — Dependencies

Dependencies answers:

> **What does this artefact rely on, what version was it last conformed against, and is that
> dependency available?**

It owns dependency identity/version declaration, dependency/reference semantics, availability
checks, version-gap detection, and declaration advancement after successful conformance.

A version gap is exposed to Migration. Dependencies does not install capabilities, deploy
packages, or execute transitions.

Detailed contract remains subject to the Dependencies review.

---

## §11 — Migration

Migration owns transition semantics, canonical transition production rules, ordering, execution
postures, and transition Tools.

Every relevant change is classified as:

- **Required Migration** — blocking for applicable work until transitioned or explicitly
  deferred;
- **On-Update** — existing state remains usable, but declared steps apply during the next
  qualifying modification;
- **No transition**.

### Transition source

Required Migration and On-Update declarations are written into the canonical Standard or Tool
that owns the changed dependency. They must be structurally and semantically unequivocal.

The capability builder uses the **Migration Build Standard** to turn those declarations into
canonical migration information.

Build-side platform and Deployment Set builders extract and adapt that canonical information
into whatever representation their target requires. Physical separation into source migration
files is not a parent requirement.

### Runtime tools

Migration defines at least:

- `/migrations-check`
- `/migrations-apply`
- `/update-doc`

`/update-doc` remains idempotent and stops/defers on Required Migration.

---

## §12 — Package boundary

Build side packages the platform contributions produced for one capability into a completed
**Capability Package**.

The package is capability-local and contains everything Deployment needs from that capability,
including platform contributions, identity/version information, transition material, removals,
and manifest information as required by the package contract.

The package is the hard production/deployment boundary:

> **Once a valid package exists, Deployment must not need the Capability Design or perform
> capability-design judgement.**

ZIP is the preferred physical container where practical, but the architecture defines Package
as the logical release object rather than coupling it permanently to one container format.

Exact manifest and identity/version schemas remain open.

---

## §13 — Deployment

Deployment accepts completed Capability Packages and realises them through named **Deployment
Sets**.

### Deployment Set

A Deployment Set is a named logical collection/destination to which capabilities are assigned.

Example:

```text
Deployment Set: workflow-core

Claude
  → plugin "workflow-core"

Codex
  → corresponding Codex capability collection

ChatGPT
  → merged project bundle
  → workflow_core_bundle.md
```

The Build Config names `workflow-core`; it does not encode those physical mappings.

A Deployment Config maintained with the Build/deployment environment resolves a Deployment Set
name to the concrete repository, path, plugin, collection, bundle, or other target required by a
platform.

### Set-aware composition

Build is capability-local. Deployment is set-aware.

Deployment may need to assemble contributions from multiple packages into one platform artefact.
For ChatGPT, for example, the contributions from all packages assigned to one Deployment Set may
be merged into one bundle file. That bundle is a Deployment Set output, not an individual
capability outcome.

Deployment owns:

- package validation at the boundary;
- Deployment Set resolution;
- composition/assembly;
- replacement and removal;
- distribution/publication;
- deployment resumption/idempotency requirements;
- rejection of defective or contradictory packages.

Host pickup/synchronisation remains external unless a platform contract explicitly brings it
into scope.

---

## §14 — Review

Review defines reusable independent assessment behaviour.

The lead owns the current model/outcome and its net coherence. The reviewer identifies evidence,
risks, omissions, conflicts, and alternatives. Findings and proposed remedies remain distinct;
the lead owns disposition.

Detailed review profiles and outcome/tooling remain to be finalised.

---

## §15 — Principal flow

```text
DESIGN SIDE

Capability Design
      ↓
Build Capability
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage

══════════════════ HANDOFF ══════════════════

BUILD SIDE

WorkPackage
 + canonical capability
 + platform Build Standards / Tools / references
      ↓
Platform contribution(s)
      ↓
Capability Package
      ↓
Deployment
      ↓
Deployment Set composition
      ↓
publish / distribute
      ↓
WorkPackage Outcome returned
```

Migration information travels with the canonical capability, is transformed during build, and is
carried through package/deployment in the form required by each platform.

---

## §16 — Deliberately open

- Detailed Deployment design: configuration, composition, removal, partial failure, resumption,
  and platform-specific builders.
- WorkPackage Standard and Outcome model under AIDE Build.
- Scope model confirmation and boundary with Build Config/platform retrieval.
- Dependencies contract confirmation.
- Review component finalisation.
- Shared identity/version contract.
- Package/manifest contract.
- Detailed platform Build Standards for Claude, Codex, ChatGPT, and later platforms.
- Reconciliation of existing Standards and Tools child documents against this parent.

---

**Depends on:** `Capabilities_Brief` v3, `Capabilities_Decisions` v9.

**References:** `Core_System_Design` v2, `Capabilities_Overview` v8,
`Capabilities_Standards_Design` v3 (revision required),
`Capabilities_Tools_Design` v1 (revision required).

**Methodology:** v17
