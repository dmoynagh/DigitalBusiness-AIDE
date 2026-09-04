
# Capabilities Build Capability Tool — Design

> **Version 5** (2026-09-02). Adds effective Build Target Profile/Definition resolution to Capability Build orchestration.

## Purpose

Check Capability Build readiness, resolve the effective Build Target Profile/Definitions and any
nominated Registry `Register` action, then produce/authorise the WorkPackage for Capability Builder
execution.

## Breaking transition

v2 produced canonical Standards/Tools. That responsibility moves to Update Capability Elements.
v3 is not backwards-compatible by silent reinterpretation; existing invocations/configuration must
be reviewed and split/migrated.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_CapabilityBuild@v3, AIDE_WorkPackage@v3
References: AIDE_UpdateCapabilityElementsTool@v1, AIDE_CapabilityBuilderTool@v3, Capabilities_BuildTargetProfile_Design_v1, AIDE_DeploymentRegistryTool@v1
