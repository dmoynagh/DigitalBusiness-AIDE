
# Capabilities Capability Build — Design

> **Version 2** (2026-09-02). Reconciles Capability Package and post-Build handling to the current Deployment Registry contract.

## Ownership

Capabilities owns specialised Capability Build semantics. Generic Build/WorkPackage remains the
execution framework. Core supplies generic Working Surface facts.

## Flow

```text
current Capability Definition + released Elements
  → Build Capability Tool (request/readiness/WorkPackage)
  → Capability Builder (Build-side execution)
  → complete Capability Package
  → nominated post-Build Tool
  → AIDE_DeploymentRegistryTool Register when requested
  → Deployment Registry
```

## Package contract

For every selected `Build:true` platform, the Package exposes a complete logical output area. Build
may be incremental internally. Package metadata includes `PackageKind: CapabilityPackage`, stable Logical Package Identity, PackageId/integrity, Capability release and Element composition, source/production/Build provenance, complete selected built outputs with resolvable payload/member identity, Build-owned composition posture where applicable, dependency/migration material required downstream, Build evidence and nominated post-Build request/intent. It may also expose package/member Tags, surface support/conformance/variation/degradation results and namespaced owner-specific extensions needed downstream.

The validated PackageId payload is immutable. Actual post-Build Registry result/receipt is external state returned by `AIDE_DeploymentRegistryTool` and WorkPackage Outcome; it is not written back into the package.

Force build may scope internal work to Capability/platform/Element/portion but never increments a
semantic release unless the semantic release rule was independently met.

## Registry seam

AI Deployment v5 owns Deployment Registry and `AIDE_DeploymentRegistryTool@v1`. Capability Build may nominate action `Register` after successful validation, with configured Registry and optional open Release Batch. No separate capability-only Deployment Manifest is required. Detailed Build Target/Profile and Deployment Set/output/delivery mechanics remain later work and are not inferred from this contract.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Build@v7, AIDE_WorkPackage@v3
References: Capabilities_Design_v13, AIDE_Deployment@v5, AIDE_DeploymentRegistryTool@v1
