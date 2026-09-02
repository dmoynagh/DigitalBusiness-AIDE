# Tools — Capability Definition

> **Version 3** (2026-09-02). Advances Build Capability and Capability Builder for Build Target Profile/Definition resolution.

## Identity, purpose and boundary

**Capability:** `Tools@v3`

Defines canonical Tool production plus the current Capability production/build Tools.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Tools.Production` | Standard | `AIDE_ToolsProduction@v2` | v1 |
| `Tools.UpdateCapabilityElements` | Tool | `AIDE_UpdateCapabilityElementsTool@v1` | v1 |
| `Tools.BuildCapability` | Tool | `AIDE_BuildCapabilityTool@v5` | v3 |
| `Tools.CapabilityBuilder` | Tool | `AIDE_CapabilityBuilderTool@v3` | v3 |

## Capability Release History

```text
Tools@v1
  Tools.Production@v1 -> AIDE_ToolsProduction@v2
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v1 -> AIDE_BuildCapabilityTool@v3
  Tools.CapabilityBuilder@v1 -> AIDE_CapabilityBuilderTool@v1

Tools@v2
  Tools.Production@v1 -> AIDE_ToolsProduction@v2
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v2 -> AIDE_BuildCapabilityTool@v4
  Tools.CapabilityBuilder@v2 -> AIDE_CapabilityBuilderTool@v2

Tools@v3
  Tools.Production@v1 -> AIDE_ToolsProduction@v2
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v3 -> AIDE_BuildCapabilityTool@v5
  Tools.CapabilityBuilder@v3 -> AIDE_CapabilityBuilderTool@v3
```

`Tools@v3` advances only the two Build-orchestration Elements for the confirmed Build Target/Profile
contract. Production and Update Capability Elements retain their existing Element releases.

## Element Release History

- `Tools.Production@v1` — baseline adoption of `AIDE_ToolsProduction@v2`; no new semantic change asserted.
- `Tools.UpdateCapabilityElements@v1` — baseline adoption of `AIDE_UpdateCapabilityElementsTool@v1`; no new semantic change asserted.
- `Tools.BuildCapability@v1` — baseline adoption of `AIDE_BuildCapabilityTool@v3`; no new semantic change asserted.
- `Tools.CapabilityBuilder@v1` — baseline adoption of `AIDE_CapabilityBuilderTool@v1`; no new semantic change asserted.
- `Tools.BuildCapability@v2` — resolves Registry publication to `AIDE_DeploymentRegistryTool@v1` and current `AIDE_CapabilityBuild@v2`.
- `Tools.CapabilityBuilder@v2` — emits the current immutable Capability Package Registry envelope and keeps post-Build result external.
- `Tools.BuildCapability@v3` — resolves effective Build Target Profiles/Definitions, applicability and target output obligations before WorkPackage authorisation.
- `Tools.CapabilityBuilder@v3` — produces complete applicable target contributions with exact Profile/Definition/output provenance.

## Element Production

| Element | Production inputs | LastEvaluated |
|---|---|---|
| `Tools.Production` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Tools.UpdateCapabilityElements` | Current sources/contracts identified by Definition references | 2026-09-02 baseline |
| `Tools.BuildCapability` | Current sources/contracts identified by Definition references | 2026-09-02 Build Target/Profile closure |
| `Tools.CapabilityBuilder` | Current sources/contracts identified by Definition references | 2026-09-02 Build Target/Profile closure |

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

## Post-Build intent

No Registry publication is inferred automatically. A Capability Build request may nominate `AIDE_DeploymentRegistryTool@v1` action `Register` with configured Registry and optional open Release Batch, or another applicable post-Build Tool/explicit none. Registry result remains external to the immutable package and Tool semantic releases.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Tools_Design_v6, AIDE_ToolsProduction@v2, AIDE_BuildCapabilityTool@v5, AIDE_CapabilityBuilderTool@v3, AIDE_DeploymentRegistryTool@v1
