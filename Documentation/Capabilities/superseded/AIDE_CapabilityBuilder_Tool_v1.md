
# AIDE Capability Builder — Tool

> **Identity:** `AIDE_CapabilityBuilderTool@v1`
> **Common name:** Capability Builder
> **Version 1** (2026-09-02). First Build-side specialised Capability executor.

## Procedure

1. Accept/validate the authorised WorkPackage under `AIDE_Build`.
2. Resolve current Definition, released Elements, selected Build Platforms and applicable rules.
3. Determine affected internal work; reuse/cache only with valid provenance and integrity.
4. Build every selected platform output to the complete external contract.
5. Assemble PackageId/integrity, composition, provenance, dependencies/migrations and evidence.
6. Validate the complete Package against WorkPackage Acceptance.
7. Invoke the nominated post-Build Tool if successful and report its result separately.
8. Return WorkPackage Outcome with actual Package/post-Build state.

Force build never increments semantic releases. Missing/unknown required platform or governing
capability state blocks rather than being assumed.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_CapabilityBuild@v1, AIDE_Build@v6, AIDE_WorkPackage@v3
References: Capabilities_CapabilityBuilder_Tool_Design_v1
