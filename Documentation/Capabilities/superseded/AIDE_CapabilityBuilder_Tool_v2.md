
# AIDE Capability Builder — Tool

> **Identity:** `AIDE_CapabilityBuilderTool@v2`
> **Common name:** Capability Builder
> **Version 2** (2026-09-02). Produces the current immutable Registry-compatible Capability Package and keeps Registry result external.

## Procedure

1. Accept/validate the authorised WorkPackage under `AIDE_Build`.
2. Resolve current Definition, released Elements, selected Build Platforms and applicable rules.
3. Determine affected internal work; reuse/cache only with valid provenance and integrity.
4. Build every selected platform output to the complete external contract.
5. Assemble the complete `CapabilityPackage` Registry envelope: Logical Package Identity, PackageId/integrity, Capability/Element composition, source/production/Build provenance, complete built output/member identities, Build-owned composition posture where applicable, dependencies/Migration, evidence, optional package/member Tags, surface variation/degradation and namespaced extensions.
6. Validate the complete Package against WorkPackage Acceptance.
7. Freeze the validated PackageId payload; do not write later Registry receipt/lifecycle state back into it.
8. Invoke the nominated post-Build Tool if successful; for Registry publication use `AIDE_DeploymentRegistryTool@v1` action `Register` with configured Registry and optional open Release Batch.
9. Return WorkPackage Outcome with actual Package and separate post-Build/Registry receipt state.

Force build never increments semantic releases. Missing/unknown required platform or governing
capability state blocks rather than being assumed.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_CapabilityBuild@v2, AIDE_Build@v7, AIDE_WorkPackage@v3, AIDE_Tags@v2
References: Capabilities_CapabilityBuilder_Tool_Design_v2, AIDE_DeploymentRegistryTool@v1
