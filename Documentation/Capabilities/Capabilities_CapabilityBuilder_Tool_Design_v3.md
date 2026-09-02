
# Capabilities Capability Builder Tool — Design

> **Version 3** (2026-09-02). Adds target-complete Build Target Profile execution and reporting.

## Purpose

Execute an authorised Capability Build WorkPackage using `AIDE_CapabilityBuild` and applicable
platform/Profile rules, returning every applicable required Build Target contribution in a complete
validated Registry-compatible Capability Package plus separate Outcome/post-Build evidence.

## Boundary

The Builder does not change Capability/Element meaning, choose Build Platforms/Profile membership,
invent applicability/degradation, infer Registry contracts, write Registry results back into
immutable package bytes, or increment semantic releases because it was forced/re-run.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_CapabilityBuild@v3, AIDE_Build@v8
References: Capabilities_CapabilityBuild_Design_v3, Capabilities_BuildTargetProfile_Design_v1, AIDE_DeploymentRegistryTool@v1
