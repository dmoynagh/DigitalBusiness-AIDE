
# Capabilities Capability Builder Tool — Design

> **Version 1** (2026-09-02). Defines the Build-side specialised Capability executor.

## Purpose

Execute an authorised Capability Build WorkPackage using `AIDE_CapabilityBuild` and applicable
platform rules, returning a complete validated Capability Package and Outcome evidence.

## Boundary

The Builder does not change Capability/Element meaning, choose Build Platforms, infer Registry
contracts or increment semantic releases because it was forced/re-run.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_CapabilityBuild@v1, AIDE_Build@v6
References: Capabilities_CapabilityBuild_Design_v1
