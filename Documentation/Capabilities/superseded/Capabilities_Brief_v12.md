
# Capabilities — Brief

> **Version 12** (2026-09-02). Reconciles specialised Capability Build and immutable Capability Package output to the current Deployment Registry contract.

## Purpose

Provide reusable AI-facing capabilities whose current semantic meaning, production state, releases,
platform-build intent and complete Build output can be determined without conflating documents,
semantic releases, package identity or deployment state.

## Required outcomes

- one current Capability Definition per Capability;
- typed Capability Elements with explicit semantic releases and release history;
- flexible Design contributions and direct authoritative authorship where appropriate;
- Update Capability Elements as the design-side production/update action;
- resolved designer-owned Build Platforms;
- Capabilities-owned specialised Capability Build contracts and Capability Builder;
- every successful Capability Build produces a complete immutable-identity Capability Package; and
- an explicit post-Build Tool handoff, with Registry publication through `AIDE_DeploymentRegistryTool@v1` when nominated.

## Boundary

Generic Build owns WorkPackage/execution/provenance/output identity. Core owns generic Working Surface
facts. AI Deployment owns its registry, target/configuration mechanics and deployed state.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_Design_v13, AIDE_Capability@v1, AIDE_CapabilityBuild@v2, AIDE_DeploymentRegistryTool@v1
