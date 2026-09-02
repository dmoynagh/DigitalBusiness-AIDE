
# Capabilities Capability Build — Decisions

> **Version 2** (2026-09-02). Records the closed Registry package/post-Build seam.

## D1 — Capability Build is Capabilities-owned specialisation

Generic Build supplies the framework; Capabilities supplies domain rules and executor.

## D2 — Package completeness is external

Incremental/cached/reused implementation is allowed internally; every successful selected-platform
output is complete externally.

## D3 — Force build changes Package identity, not semantic release

PackageId/integrity records a rebuilt instance without lying about Element/Capability meaning.

## D4 — Registry contract is owned by AI Deployment v5

Capability Package is the first specialised Deployable Package. Registry publication uses `AIDE_DeploymentRegistryTool@v1`; no separate capability-only Deployment Manifest is required.

## D5 — Registry result remains outside immutable PackageId bytes

The validated Package may carry the nominated post-Build request/intent. Registry receipt/result and lifecycle state remain external in Registry/Outcome state so registration failure can be retried without rewriting the package.

## D6 — Registry envelope may preserve Tags, degradation and extensions

Package/member Tags, producer-declared surface support/conformance/variation/degradation and namespaced owner-specific extensions may be carried for downstream Deployment. Their detailed Build Target/Profile policy remains separate later design.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_CapabilityBuild_Design_v2, Capabilities_Decisions_v18, AIDE_DeploymentRegistryTool@v1
