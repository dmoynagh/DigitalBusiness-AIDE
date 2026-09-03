# Capabilities — Brief

> **Version 14** (2026-09-03). Closes Review D R1 production seams without adding new generic mechanisms.

## Purpose

Provide reusable AI-facing capabilities whose current semantic meaning, production state, releases,
platform-build intent and complete Build output can be determined without conflating documents,
semantic releases, package identity or deployment state.

## Required outcomes

- one current Capability Definition per Capability;
- typed Capability Elements with explicit semantic releases and release history;
- flexible Design contributions and direct authoritative authorship where appropriate;
- Update Capability Elements as the design-side production/update action;
- resolved designer-owned Build Platforms and effective Build Target Profile/Definitions;
- Capabilities-owned specialised Capability Build contracts and Capability Builder;
- every successful Capability Build produces a complete immutable-identity Capability Package with
  every applicable required target contribution and snapshot-relative Tag evidence; and
- an explicit post-Build Tool request carried in WorkPackage/Outcome workflow state, with Registry
  publication through `AIDE_DeploymentRegistryTool@v2` when nominated.

## Boundary

Generic Build owns WorkPackage/execution/provenance/output identity. Core owns generic Working Surface
facts. AI Deployment owns its registry, target/configuration mechanics and deployed state.

---
Dependencies: !AIDE_DocumentationMethodology@v28
References: Capabilities_Design_v15, AIDE_Capability@v3, AIDE_CapabilityBuild@v4, Capabilities_AIDECore_BuildTargetProfile_v2, AIDE_DeploymentRegistryTool@v2
