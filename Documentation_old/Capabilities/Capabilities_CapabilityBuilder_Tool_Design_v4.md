# Capabilities Capability Builder Tool — Design

> **Version 4** (2026-09-03). Adds snapshot-relative Tag validation and keeps post-Build workflow state outside Package bytes.

## Purpose

Execute an authorised Capability Build WorkPackage using `AIDE_CapabilityBuild` and applicable
platform/Profile rules, returning every applicable required Build Target contribution in a complete
validated Registry-compatible Capability Package plus separate Outcome/post-Build evidence.

## Boundary

The Builder does not change Capability/Element meaning, choose Build Platforms/Profile membership,
invent applicability/degradation, infer Registry contracts, write post-Build request/results into
immutable package bytes, regenerate frozen Tags from newer upstream state, or increment semantic
releases because it was forced/re-run.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4, AIDE_Build@v8, AIDE_Tags@v3
References: Capabilities_CapabilityBuild_Design_v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
