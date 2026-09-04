# Capabilities — Overview

> **Version 13** (2026-08-30). Reflects promotion of generic Deployment to the
> dedicated AI Deployment workstream and closure of the local shared-OpenAI-route evidence gate.
> Review/Migration Tools, and Build Capability Tool are published. Deployment and platform evidence
> are the remaining Capabilities architecture/build focus.
>
> Created: 2026-08-27 | Last modified: 2026-08-30

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
└── Review
```

- Standards → Standard kind, weights, canonical production/usage.
- Tools → invokable action contracts/logical actions.
- Tags → generated/manual classifications + Boolean query.
- Scope → applicability.
- Dependencies → identity/presence/order/conformance/version facts.
- Migration → declared transition checking/execution.
- Review → independent assessment lifecycle.

## End-to-end flow

```text
DESIGN
Capability Design → Build Capability Tool → canonical capability → Build Config → WorkPackage

BUILD
canonical capability + platform Build knowledge
  → Platform Contributions
  → Capability Package + logical deployment intent
  → AI Deployment
  → Deployment Set/Target reconciliation + verification
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

Published generic/canonical outcomes now include:

- `AIDE_StandardsProduction@v1`;
- `AIDE_StandardsUsage@v1`;
- `AIDE_ReviewTool@v1`;
- `AIDE_MigrationTool@v1`; and
- `AIDE_BuildCapabilityTool@v1`.

`Build Capability` is the named design-side action that converts confirmed Design into canonical
Standard/Tool outcomes. It does not perform platform Build or Deployment.

## AI Deployment handoff

Capabilities stops at capability-local package/build material plus logical deployment intent.

AI Deployment now owns:

- Deployment Set desired composition;
- target surface + representation + distribution channel;
- set-aware composition;
- install/update/remove reconciliation;
- partial failure/resumption; and
- runtime verification.

The previous hypothesis that one local OpenAI plugin/skill install could be the common private
ChatGPT + Codex route is closed as false for the tested path. Broader hosted/account/public routes
remain implementation evidence.

## Current sequence

1. Use Capabilities as a stable producer of canonical capability outcomes/packages.
2. Use Build for target-compatible contribution production.
3. Use `AIDE_Deployment@v1` / AI Deployment for physical target reconciliation.
4. Resolve Environment/shared inter-AI communication ownership separately.
5. Apply Documentation Methodology v18 OnUpdate as affected documents change.

---

**Depends on:** `Capabilities_Brief` v7, `Capabilities_Design` v8,
`Capabilities_Decisions` v14.

References: `Capabilities_Migration_Design` v1, `Capabilities_Dependencies_Design` v2,
`Capabilities_WorkRegister` v12, `Capabilities_OpenItems` v14.

Dependencies: !AIDE_DocumentationMethodology@v18
