
# Capabilities Capability Build — Design

> **Version 3** (2026-09-02). Adds reusable Build Target Profile resolution and complete target-contribution production.

## Ownership

Capabilities owns specialised Capability Build semantics. Generic Build/WorkPackage remains the
execution framework. Core supplies generic Working Surface facts.

## Flow

```text
current Capability Definition + released Elements
  + effective Build Target Profile/Definitions
  → Build Capability Tool (request/readiness/WorkPackage)
  → Capability Builder (Build-side execution)
  → complete Capability Package
  → nominated post-Build Tool
  → AIDE_DeploymentRegistryTool Register when requested
  → Deployment Registry
```

## Package contract

For every selected `Build:true` platform and every applicable required Build Target Definition, the
Package exposes a complete logical output area/contribution. Build may be incremental internally.
Package metadata includes `PackageKind: CapabilityPackage`, stable Logical Package Identity,
PackageId/integrity, Capability release and Element composition, source/production/Build provenance,
effective Profile/Definition revisions, complete target outputs with resolvable payload/member
identity, Build-owned composition posture, effective Tags, reach/applicability/conformance/
degradation facts, dependency/migration material, Build evidence and nominated post-Build intent.

The validated PackageId payload is immutable. Actual post-Build Registry result/receipt is external state returned by `AIDE_DeploymentRegistryTool` and WorkPackage Outcome; it is not written back into the package.

Force build may scope internal work to Capability/platform/Element/portion but never increments a
semantic release unless the semantic release rule was independently met.

## Registry seam

AI Deployment owns the Registry and `AIDE_DeploymentRegistryTool`. Capability Build may nominate
`Register` after successful validation, with configured Registry and optional open Release Batch.
No separate capability-only Deployment Manifest is required. Capability Build owns Build Target
production; AI Deployment owns Deployment Set resolution, set-level output assembly, Delivery
Actions, Target Adapters and deployed state.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v2, AIDE_Build@v8, AIDE_WorkPackage@v3
References: Capabilities_Design_v14, Capabilities_BuildTargetProfile_Design_v1, AIDE_Deployment@v6, AIDE_DeploymentRegistryTool@v1
