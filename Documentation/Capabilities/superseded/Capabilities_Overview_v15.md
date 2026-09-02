# Capabilities — Overview

> **Version 15** (2026-09-01). Applies Review C R1 semantic remediation and records the current production/reference/freshness/correlation model before focused R2 verification.

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
├── Review
└── Messaging
```

- Standards → Standard kind, weights, canonical production/usage.
- Tools → invokable action contracts/logical actions.
- Tags → generated/manual classifications + Boolean query.
- Scope → applicability.
- Dependencies → identity/presence/order/conformance/version facts.
- Migration → declared transition checking/execution.
- Review → independent assessment lifecycle.
- Messaging → AI-MESSAGE envelope, correlation, receipt integrity and cross-context messaging.

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
- conformance checkpoints are non-ordering saved facts; dependency declaration order is default processing precedence only where processing order is needed;
- transition posture is version-level;
- Required-triggered save also reconciles pending applicable OnUpdate work through current;
- checkpoint is written only with saved proven artefact state;
- failure/defer preserves last successful checkpoint and writes compact owner-labelled temporary
  state;
- an unsatisfied exact-version constraint is a hard present block, not a conformance checkpoint or ordinary migration gap.

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
release version. Consumer conformance checkpoints routinely lag current releases until a qualifying
save proves newer conformance; that is expected state rather than stale metadata.

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

- `AIDE_StandardsProduction@v2`;
- `AIDE_StandardsUsage@v1`;
- `AIDE_ToolsProduction@v1`;
- `AIDE_ReviewTool@v3`;
- `AIDE_MigrationTool@v2`; and
- `AIDE_BuildCapabilityTool@v2`;
- `AIDE_Messaging@v2`; and
- `AIDE_MessagingTool@v1`.

`Build Capability` is the named design-side action that converts confirmed Design into canonical
Standard/Tool outcomes. It does not perform platform Build or Deployment.

## Messaging

```text
ordinary exchange                 → conversation
active state needing continuity   → WIP
durable outstanding obligation    → OpenItems
body needing independent retrieval → persisted Message
```

`AIDE_Messaging@v2` keeps message identity/threading/readability separate, retains best-effort
`=== STATE ===` receipt integrity, distinguishes receipt from fulfilment, and does not require the
former dedicated obligations register. STATE's value depends on retained evidence; use explicit Ack
where positive receipt proof matters. `AIDE_MessagingTool@v1` supplies Compose, Receive, Reply,
Forward, Promote, Acknowledge, QueryReceipt and Reconcile.

Review consumes Messaging for AI-MESSAGE relay/receipt semantics; Review v3 treats Review/Round payload correlation as authoritative for Review semantics and quarantines a positive mismatch with transport correlation. Profiles v2 keeps the same five Types with versionless Review references.

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

1. Peer-review the major AIDE/Capabilities architecture slices with Claude, including Messaging.
2. Resolve accepted Review findings into current Design/Decisions/canonical outcomes.
3. Build lightweight platform-specific Bootstrap implementations where evidence warrants them.
4. Build target-platform contributions and hand deployment to AIDE Build + AI Deployment.
5. Run the planned final cross-system integration Review before broad deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Brief_v9, Capabilities_Design_v10, Capabilities_Decisions_v16
References: Capabilities_Migration_Design_v2, Capabilities_Dependencies_Design_v3, Capabilities_WorkRegister, Capabilities_OpenItems, Capabilities_Messaging_Design_v2
