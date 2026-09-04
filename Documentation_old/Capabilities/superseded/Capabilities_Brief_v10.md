# Capabilities — Brief

> **Version 10** (2026-09-01). Applies Review C R2 reference-position cleanup to current owner/inventory prose while preserving the R1 architecture.

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
- **Review** — purposeful independent assessment for insight, integrity, decisions and risk.
- **Messaging** — platform-neutral AI-MESSAGE semantics, correlation, receipt integrity and
  cross-context communication workflow.

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

`AIDE_BuildCapabilityTool` is the canonical design-side producer for this step. It applies the published
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
requests best-effort startup presence checking. `X@vN` records the last saved/proven consumer
conformance checkpoint and creates no execution order; behind-current checkpoints are normal until a
qualifying save proves newer conformance. `X@!vN` is a hard present exact-version constraint.
Dependency declaration order supplies default processing precedence only where processing order is
actually required. `References:` carries no currency/conformance obligation; current executable
capability references are normally versionless unless they intentionally target a specific release.

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

## AI Deployment boundary

Generic deployment is no longer owned by Capabilities.

Capabilities owns:

- canonical capability production;
- capability-local Platform Contributions produced through Build;
- Capability Package/build identity and integrity; and
- logical deployment intent sufficient for the deployment consumer.

`AIDE_Deployment` owns generic Deployment Set/Target reconciliation, representation/channel/
surface resolution, composition, publication/install/update/remove and runtime verification.

OpenAI evidence has closed the immediate architecture gate: a local plugin/skill representation
cannot be assumed to provide one common ChatGPT + Codex runtime route. Surface, representation and
distribution channel are separate deployment facts.

## Review and Messaging boundary

Review owns the independent-assessment lifecycle and substantive Review request/response semantics.
Messaging owns AI-MESSAGE relay, message correlation, receipt/reconciliation and Messaging actions.
Environment/platform configuration still supplies current reviewer/model/route facts and concrete
route availability.

Messaging keeps ordinary exchanges in conversation, uses WIP/OpenItems only where persistence is
actually needed, and persists a Message document only when the body itself requires independent
retrieval. STATE evidence is only as strong as retained evidence; explicit Ack supplies positive
receipt proof when needed. Review/Round correlation remains authoritative for Review semantics and a
positive mismatch with Messaging transport correlation is quarantined. Documentation Methodology
supplies the generic governed-document mechanics.

## Success signals

- Build side does not need to reopen Capability Design.
- Shared components have one owner and are consumed rather than restated.
- Required/OnUpdate behaviour remains unambiguous and cheap to check.
- Version/package/deployment facts are not conflated.
- Deployment can act mechanically from Package + Manifest.
- Platform choices are established by evidence rather than assumptions.
- Messaging adds receipt integrity without requiring a permanent message/obligations archive.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Decisions_v16
References: Capabilities_Design, Capabilities_Migration_Design, Capabilities_Standards_Design, Capabilities_Tools_Design, Capabilities_Messaging_Design
