
# Capabilities Build Capability Tool — Design

> **Version 4** (2026-09-02). Adds current Deployment Registry post-Build request resolution without changing the v3 orchestration role.

## Purpose

Check Capability Build readiness, establish the current Build request including any nominated Registry `Register` action, and produce/authorise the WorkPackage for Capability Builder execution.

## Breaking transition

v2 produced canonical Standards/Tools. That responsibility moves to Update Capability Elements.
v3 is not backwards-compatible by silent reinterpretation; existing invocations/configuration must
be reviewed and split/migrated.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_CapabilityBuild@v2, AIDE_WorkPackage@v3
References: AIDE_UpdateCapabilityElementsTool@v1, AIDE_CapabilityBuilderTool@v2, AIDE_DeploymentRegistryTool@v1
