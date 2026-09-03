# AIDE Capability Builder — Tool

> **Identity:** `AIDE_CapabilityBuilderTool@v4`
> **Common name:** Capability Builder
> **Version 4** (2026-09-03). Validates snapshot-relative Tags and executes post-Build workflow without freezing it into Package bytes.

## Procedure

1. Accept/validate the authorised WorkPackage under `AIDE_Build`.
2. Resolve current Definition, released Elements, selected Build Platforms, effective Build Target
   Profile/Definitions and applicable rules.
3. Determine affected internal work; reuse/cache only with valid provenance and integrity.
4. Build every selected platform and applicable required target output to the complete external
   contract. Do not silently omit a target or invent `NotApplicable`/degradation.
5. Run/validate applicable Tag Builders against the exact authoritative source snapshot resolved
   by the WorkPackage; fail visibly if freshness cannot be established.
6. Assemble the complete `CapabilityPackage` Registry envelope: Logical Package Identity,
   PackageId/integrity, Capability/Element composition, source/production/Build provenance,
   Profile/Definition revisions, complete Build Target output/member identities and integrity,
   Build-owned composition posture, effective Tags, reach/applicability/conformance/degradation,
   dependencies/Migration, tag-freshness/source-snapshot evidence and namespaced extensions.
7. Validate the complete Package against WorkPackage Acceptance.
8. Freeze the validated PackageId payload; do not write post-Build request, Registry receipt or
   lifecycle state into it.
9. Invoke the WorkPackage-nominated post-Build Tool if successful. Registry publication uses
   `AIDE_DeploymentRegistryTool@v2`; direct registration is valid for an independent package, while
   an established coordinated change requires the common Open Release Batch.
10. Return WorkPackage Outcome with actual Package and separate post-Build/Registry receipt state.

Force build never increments semantic releases. Missing/unknown required platform or governing
capability state blocks rather than being assumed.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4, AIDE_Build@v8, AIDE_WorkPackage@v3, AIDE_Tags@v3
References: Capabilities_CapabilityBuilder_Tool_Design_v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
