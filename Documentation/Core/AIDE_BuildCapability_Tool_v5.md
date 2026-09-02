
# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v5`
> **Common name:** Build Capability
> **Version 5** (2026-09-02). Resolves Build Target Profiles/Definitions and target applicability before authorising Build.

## Actions

`Request | ValidateReadiness | Authorise | Status`

## Procedure

1. Resolve the current Capability Definition, released Elements/composition and production currency.
2. Require resolved Build Platforms and at least one explicit `Build:true`.
3. Resolve one unambiguous effective Build Target Profile/Definition set, including governed Profile
   membership/request selection and any Capability-specific overrides.
4. Resolve applicability, required reach, conformance/degradation permission and output Tags for
   every selected target; block unsupported applicable requirements rather than dropping them.
5. Resolve applicable Capability Build/platform rules, Registry-compatible package acceptance and
   explicit post-Build intent. When Registry publication is requested, resolve
   `AIDE_DeploymentRegistryTool@v1` action `Register`, configured Registry and optional open Release Batch.
6. If an Element may be stale, return `UpdateElementsRequired`; do not produce it here.
7. Validate that the requested force scope, if any, cannot imply false semantic release changes.
8. Create/authorise the self-contained `AIDE_WorkPackage@v3` for Capability Builder, carrying the
   resolved Profile/Definition revisions and required target outputs.
9. Return WorkPackage identity, readiness, selected platforms/targets, post-Build request and
   blockers. Keep actual post-Build result outside the validated package.

## Required migration from v2

`AIDE_BuildCapabilityTool@v2` canonical production calls move to
`AIDE_UpdateCapabilityElementsTool@v1`. Only explicitly migrated orchestration calls use v3.

```yaml
MigrationSummary:
  CurrentVersion: v5
  LatestRequiredVersion: v3
  LatestOnUpdateVersion: none

Transition:
  Version: v3
  Posture: Required
  Action: Review every v2 invocation; move Element production to AIDE_UpdateCapabilityElementsTool@v1 and retain only Build-request orchestration here.

Transition:
  Version: v4
  Posture: None

Transition:
  Version: v5
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v2, AIDE_CapabilityBuild@v3, AIDE_WorkPackage@v3
References: Capabilities_BuildCapability_Tool_Design_v5, AIDE_UpdateCapabilityElementsTool@v1, Capabilities_BuildTargetProfile_Design_v1, AIDE_DeploymentRegistryTool@v1
