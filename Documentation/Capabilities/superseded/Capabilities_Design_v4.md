# Capabilities — Design

> **Version 4** (2026-08-28). Adds Tags as an eighth component, finalises Tags/Scope/Dependencies,
> consumes the Core identity/bootstrap primitives, and separates the capability payload from the
> Deployment Manifest at the producer-to-Deployment boundary.
>
> This document states the current position. Historical and superseded positions remain in
> `Capabilities_Decisions` v10.
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

Capabilities has eight peer components:

```text
Capabilities
├── Standards
├── Tools
├── Tags
├── Scope
├── Dependencies
├── Migration
├── Deployment
└── Review
```

Standards and Tools define capability kinds and canonical production. Tags, Scope, Dependencies,
Migration, Deployment, and Review provide shared behaviour.

Build execution is not an eighth Capabilities component. The generic design-side-to-build-side
handoff and WorkPackage lifecycle belong to AIDE Build. Capabilities consumes that mechanism.

### Governing principles

- **One owner per mechanism.**
- **Capability meaning before platform realisation.**
- **Design-side outputs are self-contained for handoff.**
- **Generic platform implementation knowledge belongs Build side.**
- **Build is capability-local; Deployment is set-aware.**
- **Semantic complexity resolved before runtime matching.**
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

## §9 — Tags

Tags answers:

> **What classifications does this artefact carry, and does it satisfy this tag expression?**

Tags is a general classification/query substrate rather than a Scope-only mechanism.

The model is:

```text
semantic owner
  resolves/denormalises source meaning
        ↓
Tag Builder embedded in the owning Standard
        ↓
flat tags on the artefact
        ↓
Boolean tag query
```

A Tag Builder defines how it detects applicable artefacts, reads its source information,
generates current tags, and identifies the generated output it owns. Builders are discovered
from available Standards and run against the artefact in hand.

Generated ownership may use an owned prefix or an owned `{key}:[...]` group. Groups are storage
and cleanup structure only: every consumer except the owning builder ignores group keys and sees
only a flat set of tag values.

For governed Markdown documents, Tags uses one compact footer metadata property:

```text
Tags: design, release-ready, doctype:[design, platformdesign]
```

Tag values contain no whitespace; `-` and `_` are available separators.

Tag matching supports only exact tag values with `!`, `&`, `|`, and parentheses. No inheritance
or semantic logic is evaluated at query time.

Detailed contract: `Capabilities_Tags_Design` v1 / `AIDE_Tags@v1`.

---

## §10 — Scope

Scope answers:

> **Should this Standard, Tool, rule, behaviour, or other referenceable capability apply here?**

Scope has two optional layers:

1. **Machine Scope** — an `AIDE_Tags` Boolean expression.
2. **Context Scope** — an assessable natural-language condition interpreted by the AI against the
   current context.

Both constrain applicability when both are present. Machine Scope evaluates first and may
short-circuit contextual evaluation.

Omission is permissive:

- no Machine Scope → no tag restriction;
- no Context Scope → no contextual restriction;
- neither → generally applicable;
- `Disabled: true` → never applicable.

Scope returns applicability only; it does not execute the scoped behaviour.

Concrete platform retrieval/discovery/trigger implementation is a Build-side platform concern.
Scope provides semantic applicability and the platform builder may transform it into the strongest
available trigger/discovery representation.

Detailed contract: `Capabilities_Scope_Design` v1 / `AIDE_Scope@v1`.

---

## §11 — Dependencies

Dependencies answers:

> **What does this artefact rely on, can that identity be resolved, what version was it last
> conformed against, and what version is available?**

A dependency may contribute to an artefact's correct schema, design, content, interpretation,
conformance, maintenance, or execution.

For governed Markdown documents, the compact declaration is:

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

Presence postures are:

- normal dependency — checked when relevant;
- `!` required — check on relevant access/use and raise missing state prominently;
- `!!` startup-required — best-effort session-start check and required thereafter.

Version semantics are separate from identity matching. `abc@v8` means last successfully
conformed against v8; `abc@v12` still resolves and exposes a `v8 → v12` version gap.
`abc@!v8` requires exactly v8.

Dependency Query reports identity resolution, requirement level, conformance version, available
version, version relation/gap, and exact-version result. Migration and the current operation
consume that factual state.

Dependency Builders mirror Tag Builders: other Standards may embed generation rules, discoverable
from the available Standards set, with builder-owned output identified by group or prefix.

A conformance marker advances only after all applicable migration/update work through the new
checkpoint succeeds. Installed/current version alone never advances it.

Detailed contract: `Capabilities_Dependencies_Design` v1 / `AIDE_Dependencies@v1`.

---

## §12 — Migration

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

Build-side platform and Deployment Set builders extract and adapt that canonical information into
whatever representation their target requires. Physical separation into source migration files is
not a parent requirement.

### Runtime tools

Migration defines at least:

- `/migrations-check`
- `/migrations-apply`
- `/update-doc`

`/update-doc` remains idempotent and stops/defers on Required Migration.

Dependencies supplies the conformance checkpoint/version-gap state Migration evaluates.

---

## §13 — Shared identity and bootstrap primitives

Capabilities consumes two system-level Core primitives rather than defining local substitutes.

### Identity

A referenceable artefact may expose:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first identity is primary; later entries are alternate/exposed identities. Version belongs to
the individual identity entry. Identity matching is by name; consumers such as Dependencies
compare version after resolution.

Internal topic/source names stay simple. Formal published/referenceable AIDE identities use the
`AIDE_` namespace, while common names remain available in prose.

### Bootstrap

Core defines the generic `{bootstrap}` discoverability marker and the small stable system
instruction that tells each environment to process available bootstrap blocks at session start on
a best-effort basis.

Components may contribute bootstrap content. Dependencies uses it for `!!` checking; future
Migration or Environment behaviours may use it independently.

---

## §14 — Package and Deployment Manifest boundary

Build side produces a completed **Capability Package** plus a **Deployment Manifest**.

The Capability Package is the capability-local payload. It contains the platform contributions
and other release material produced for that capability.

The Deployment Manifest is the machine-readable deployment intent/metadata Deployment needs to
place and maintain that payload. Its minimum fields are driven by demonstrated Deployment needs
and include, at least where applicable:

- package identity/version;
- Deployment Set membership;
- platform applicability;
- replacement/removal information.

Transition information and integrity/resumption information are included where required by the
final package/deployment contracts.

The producer-to-Deployment boundary is:

```text
Capability Package
      +
Deployment Manifest
      ↓
Deployment
```

Once that boundary is valid, Deployment must not reopen Capability Design or infer capability
intent from payload structure.

ZIP remains a preferred physical package container where practical; the logical contract is not
coupled to one container format.

---

## §15 — Deployment

Deployment accepts completed Capability Packages plus their Deployment Manifests and realises
them through named **Deployment Sets**.

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

Deployment may assemble contributions from multiple packages into one platform artefact. For
ChatGPT, contributions assigned to one Deployment Set may be merged into one bundle file; that
bundle is a Deployment Set output, not an individual capability outcome.

Deployment owns:

- package/manifest validation at the boundary;
- Deployment Set resolution;
- composition/assembly;
- replacement and removal;
- distribution/publication;
- deployment resumption/idempotency requirements;
- rejection of defective or contradictory inputs.

Host pickup/synchronisation remains external unless a platform contract explicitly brings it into
scope.

Detailed Deployment design remains intentionally deferred until the upstream capability contracts
and known components are complete enough to give Deployment a stable mechanical input.

---

## §16 — Review

Review defines reusable independent assessment behaviour for **insight and risk management**.

The lead owns the current model/outcome and its net coherence. The reviewer provides a separate
challenge path intended to surface errors, gaps, assumptions, risks, alternatives, and useful
insight before important work is relied upon or locked in.

Independence, review lens, review intensity, blind framing, package construction, and convergence
are being reviewed from first principles before the prior Workflow review implementation is
re-admitted.

Detailed Review design remains current architecture work.

---

## §17 — Principal flow

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
Capability Package + Deployment Manifest
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

Tags, Scope, and Dependencies provide reusable runtime/build metadata and behaviour across this
flow rather than belonging to any one stage.

---

## §18 — Deliberately open

- Review component purpose/model/profile/package/iteration finalisation.
- Migration child design and Migration Build Standard details.
- Reconciliation of existing Standards and Tools child documents against this parent and the new
  Tags/Scope/Dependencies contracts.
- Remaining shared release/package/deployment version distinctions beyond the Core identity model.
- Detailed Capability Package / Deployment Manifest schema driven by Deployment requirements.
- Detailed Deployment design: configuration, composition, removal, partial failure, resumption,
  and platform-specific builders.
- WorkPackage Standard and Outcome model under AIDE Build.
- Detailed platform Build Standards for Claude, Codex, ChatGPT, and later platforms.
- Documentation Methodology reconciliation of generic header/footer metadata containers and the
  new Tags/Dependencies/Identity blocks.

---

**Depends on:** `Capabilities_Brief` v4, `Capabilities_Decisions` v10.

**References:** `Core_System_Design` v3, `Capabilities_Overview` v9,
`Capabilities_Tags_Design` v1, `Capabilities_Scope_Design` v1,
`Capabilities_Dependencies_Design` v1,
`Capabilities_Standards_Design` v3 (revision required),
`Capabilities_Tools_Design` v1 (revision required).

**Methodology:** v17
