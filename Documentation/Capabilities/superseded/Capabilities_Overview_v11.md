# Capabilities — Overview

> **Version 11** (2026-08-29). Migration/reconciliation checkpoint: Migration, Standards, Tools,
> dependency ordering, version distinctions and producer Package/Manifest are settled; Deployment
> and platform evidence are next.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## Architecture at a glance

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

- Standards → Standard kind, weights, canonical production/usage.
- Tools → invokable action contracts/logical actions.
- Tags → generated/manual classifications + Boolean query.
- Scope → applicability.
- Dependencies → identity/presence/order/conformance/version facts.
- Migration → declared transition checking/execution.
- Deployment → Package/Manifest consumption and Deployment Set realisation.
- Review → independent assessment lifecycle.

## End-to-end flow

```text
DESIGN
Capability Design → Build Capability → canonical capability → Build Config → WorkPackage

BUILD
canonical capability + platform Build knowledge
  → Platform Contributions
  → Capability Package + Deployment Manifest
  → Deployment
  → Deployment Set composition/publication
```

## Dependencies + Migration

```text
Dependencies: abc@v8
Available: abc@v12
       ↓
Dependency Query: v8 → v12
       ↓
MigrationSummary fast check
       ↓ if needed
per-version transition history
       ↓
Required before affected use
OnUpdate on next modification/save
None = no state change
```

- `!!` is startup presence checking, not a blanket startup migration scan.
- dependency declaration order is default processing precedence;
- transition posture is version-level;
- Required-triggered save also reconciles pending applicable OnUpdate work through current;
- checkpoint is written only with saved proven artefact state;
- failure/defer preserves last successful checkpoint and writes compact owner-labelled temporary
  state;
- exact-version treatment comes from applicable governing consumer rules.

## Migration performance

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8
```

Detailed history loads only when the summary indicates possible work. Skill-based platform builds
should surface this summary in eagerly available skill/header metadata where possible.

## Version concepts

```text
DocMeth document version
≠ capability release version
≠ consumer conformance checkpoint
≠ package build identity
≠ deployment state
```

Package rebuilds use a new PackageId/digest as needed without falsely incrementing capability
release version.

## Package + Manifest

```text
Capability Package
  = payload/build instance for one capability release

Deployment Manifest
  = logical placement/lifecycle intent
```

Manifest minimally carries PackageId, capability identity/release, logical Deployment Set/platform,
contribution selection, explicit replace/remove intent where needed, and integrity. Physical
repository/plugin/path/account destination is Deployment Config.

## Standards and Tools

Standards and Tools now consume Tags/Scope/Dependencies/Migration/Review rather than embedding
those mechanisms. Generic platform realisation belongs Build side.

Tools may orchestrate bounded declared judgment; the repeatable Tool contract stays explicit and
genuine substantive authority remains external.

## Deployment: fixed vs open

Fixed:

- Package + Manifest boundary;
- logical Deployment Sets;
- capability-local Build / set-aware Deployment;
- composition, replacement/removal and publication belong Deployment.

Still open:

- set lifecycle/state;
- Deployment Config ownership/inheritance;
- full vs incremental assembly;
- conflicts/atomicity/partial failure/rollback/resume;
- publication and verification mechanics.

Platform mappings remain empirical. The proposed shared OpenAI plugin/skills representation for
ChatGPT + Codex must be proven with a real Standard before becoming the primary mapping.

## Current sequence

1. Run high-value platform evidence proof (OpenAI skill/plugin Standard test).
2. Design Deployment.
3. Complete platform Build/Deployment standards/evidence as required.
4. Resolve Environment/shared inter-AI communication ownership.
5. Review Documentation Methodology later using `Capabilities_DocMethReviewItems` v3.

---

**Depends on:** `Capabilities_Brief` v5, `Capabilities_Design` v6,
`Capabilities_Decisions` v12.

**References:** `Capabilities_Migration_Design` v1, `Capabilities_Dependencies_Design` v2,
`Capabilities_WorkRegister` v10, `Capabilities_OpenItems` v12.

**Methodology:** v17
