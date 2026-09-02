# Capabilities — Brief

> **Version 6** (2026-08-30). Closes the non-Deployment canonical-output gap by publishing the
> Standards Production/Usage Standards, canonical Review/Migration Tools, and the Build Capability
> Tool that makes canonical production an explicit invokable action.
>
> Created: 2026-08-27 | Last modified: 2026-08-30

---

## Purpose

Capabilities owns the reusable infrastructure by which AI-facing capabilities are defined,
classified, made applicable, connected to dependencies, transitioned across versions, built into
canonical outcomes, realised for platforms, packaged, deployed, and independently reviewed.

Everything exists to add practical AI-development capability or reduce a demonstrated risk.

## Required architecture

Eight peer components:

- **Standards** — Standard kind, weights, canonical production and generic usage.
- **Tools** — invokable action contract and logical commands.
- **Tags** — classification/build/query substrate.
- **Scope** — applicability using Tags plus AI context.
- **Dependencies** — dependency identity/presence/order, conformance and version-gap state.
- **Migration** — Required/OnUpdate/None transition authoring, discovery, ordering and execution.
- **Deployment** — consumes packages/manifests, composes Deployment Sets and publishes/distributes.
- **Review** — purposeful independent assessment for insight, integrity, decisions and risk.

AIDE Build owns WorkPackage and generic platform execution/handoff.

## Production and handoff

```text
Capability Design
      ↓
Build Capability Tool
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage

BUILD SIDE
canonical capability + WorkPackage + platform Build knowledge
      ↓
Platform contribution(s)
      ↓
Capability Package + Deployment Manifest
      ↓
Deployment
```

`AIDE_BuildCapabilityTool` is the canonical design-side producer for this step. It applies the
Standards/Tools production contracts and fails back to the work owner rather than inventing missing
Design. Canonical outcomes contain complete capability meaning plus only capability-specific
platform addenda. Generic skill/plugin/bundle/command implementation belongs Build side.

## Shared contracts

### Tags and Scope

Semantic owners generate explicit tags through owner-defined Tag Builders. Scope consumes exact
Boolean tag queries plus optional AI-interpreted Context Scope. Missing Scope layers are
unrestricted; explicit disabled means never applies.

### Dependencies

Resolve identity first and version second. `!` means required on relevant use; `!!` additionally
requests best-effort startup presence checking. A version records the last saved/proven consumer
conformance checkpoint. Dependency declaration order supplies default processing precedence.

### Migration

Every migratable capability release positively declares `Required`, `OnUpdate`, or `None`.
Required is checked before affected use; OnUpdate waits for the next modification/save.
`MigrationSummary` supports cheap discovery; detailed history is loaded only when necessary.
Checkpoints advance only with saved proven artefact state. Migration is resumable and records
compact owner-labelled unresolved state through the document methodology's generic state mechanism.

## Version/release/package distinctions

Keep separate:

- DocMeth document version;
- canonical capability release version;
- consumer dependency conformance version;
- package build identity/integrity; and
- factual deployment state.

Package rebuilds do not create a new capability release version unless capability meaning changed.

## Package and Deployment Manifest

A Capability Package is the capability-local payload for one capability release. Its `PackageId`
and integrity data identify the concrete build.

The Deployment Manifest supplies logical placement/lifecycle intent only: package/capability
identity, Deployment Set/platform targets, package-local contribution selection, explicit
replace/remove intent where required, and integrity. Physical destinations belong Deployment
Config.

Deployment must not reopen Capability Design or infer intent from payload structure.

## Deployment boundary

A Deployment Set remains a named logical destination/grouping. Its concrete platform representation
is resolved by Deployment Config and is deliberately not fixed in this Brief.

Current platform evidence—including whether OpenAI plugins containing skills can be the common
primary representation for ChatGPT and Codex—must be tested before Deployment locks physical
mappings. Bundles remain a possible representation/fallback rather than an architectural default.

## Review boundary

Review owns the independent-assessment lifecycle, not environment/model-route configuration or
communication transport. Those remain explicit shared external seams.

## Success signals

- Build side does not need to reopen Capability Design.
- Shared components have one owner and are consumed rather than restated.
- Required/OnUpdate behaviour remains unambiguous and cheap to check.
- Version/package/deployment facts are not conflated.
- Deployment can act mechanically from Package + Manifest.
- Platform choices are established by evidence rather than assumptions.

---

**Depends on:** `Capabilities_Decisions` v13.

**References:** `Capabilities_Design` v7, `Capabilities_Migration_Design` v1,
`Capabilities_Standards_Design` v4, `Capabilities_Tools_Design` v2.

**Methodology:** v17
