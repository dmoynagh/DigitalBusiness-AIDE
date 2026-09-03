# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v6`
> **Common name:** Build Capability
> **Version 6** (2026-09-03). Makes WorkPackage mapping and coordinated post-Build Registry authority explicit.

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
   explicit post-Build request. When Registry publication is requested, resolve
   `AIDE_DeploymentRegistryTool@v2` action `Register` and configured Registry. Direct registration
   is valid for an independent package; an established coordinated multi-package change requires
   the same Open Release Batch for every participating registration.
6. If an Element may be stale, return `UpdateElementsRequired`; do not produce it here.
7. Validate that the requested force scope, if any, cannot imply false semantic release changes.
8. Create/authorise the self-contained `AIDE_WorkPackage@v3` for Capability Builder:
   - Inputs carry Definition, released Elements, selected Build Platforms, exact source snapshot
     and effective Profile/Definitions;
   - RequiredOutputs carry all applicable required target outputs and the complete Package;
   - Constraints carry reach/applicability/conformance/degradation, required Tags, force scope and
     post-Build request/inputs or explicit none;
   - Acceptance carries freshness, target completeness, semantic preservation, provenance,
     integrity and package validation; and
   - Return requires Package/Build evidence plus separate post-Build/Registry state.
9. Return WorkPackage identity, readiness, selected platforms/targets, post-Build request and
   blockers. Keep actual post-Build result outside the validated package.

## Required migration from v2

`AIDE_BuildCapabilityTool@v2` canonical production calls move to
`AIDE_UpdateCapabilityElementsTool@v1`. Calls retaining Build-request orchestration use the current
`AIDE_BuildCapabilityTool` release; v3 names the Required transition checkpoint, not the release to
which current invocations are pinned.

```yaml
MigrationSummary:
  CurrentVersion: v6
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

Transition:
  Version: v6
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_CapabilityBuild@v4, AIDE_WorkPackage@v3
References: Capabilities_BuildCapability_Tool_Design_v6, AIDE_UpdateCapabilityElementsTool@v1, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
