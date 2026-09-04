
# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v3`
> **Common name:** Build Capability
> **Version 3** (2026-09-02). Breaking role transition to Build request/readiness/WorkPackage orchestration.

## Actions

`Request | ValidateReadiness | Authorise | Status`

## Procedure

1. Resolve the current Capability Definition, released Elements/composition and production currency.
2. Require resolved Build Platforms and at least one explicit `Build:true`.
3. Resolve applicable Capability Build/platform rules, package acceptance and explicit post-Build intent.
4. If an Element may be stale, return `UpdateElementsRequired`; do not produce it here.
5. Validate that the requested force scope, if any, cannot imply false semantic release changes.
6. Create/authorise the self-contained `AIDE_WorkPackage@v3` for Capability Builder.
7. Return WorkPackage identity, readiness, selected platforms, post-Build request and blockers.

## Required migration from v2

`AIDE_BuildCapabilityTool@v2` canonical production calls move to
`AIDE_UpdateCapabilityElementsTool@v1`. Only explicitly migrated orchestration calls use v3.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: v3
  LatestOnUpdateVersion: none

Transition:
  Version: v3
  Posture: Required
  Action: Review every v2 invocation; move Element production to AIDE_UpdateCapabilityElementsTool@v1 and retain only Build-request orchestration here.
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_CapabilityBuild@v1, AIDE_WorkPackage@v3
References: Capabilities_BuildCapability_Tool_Design_v3, AIDE_UpdateCapabilityElementsTool@v1
