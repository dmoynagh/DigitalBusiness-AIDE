# Capabilities Build Capability Tool — Design

> **Version 6** (2026-09-03). Defines the exact Capability-to-WorkPackage mapping and coordinated Registry workflow.

## Purpose

Check Capability Build readiness, resolve the effective Build Target Profile/Definitions and any
nominated Registry `Register` action, then produce/authorise the WorkPackage for Capability Builder
execution.

The specialised facts map into generic `AIDE_WorkPackage@v3` as follows: Definition, released
Elements, Build Platforms, exact source snapshot and Profile/Definitions are Inputs; required
target outputs and Capability Package are RequiredOutputs; applicability/conformance/degradation,
Tags, force scope and post-Build request are Constraints; package validation is Acceptance; and
Package evidence plus separate post-Build result is Return.

## Breaking transition

v2 produced canonical Standards/Tools. That responsibility moves to Update Capability Elements.
The v3 Required transition is not backwards-compatible by silent reinterpretation; existing v2
invocations/configuration must be reviewed and split/migrated. Calls retaining Build orchestration
use the current Tool release, not historical v3 merely because v3 is the migration checkpoint.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4, AIDE_WorkPackage@v3
References: AIDE_UpdateCapabilityElementsTool@v1, AIDE_CapabilityBuilderTool@v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
