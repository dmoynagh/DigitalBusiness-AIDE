# Tools — Capability Definition

> **Version 5** (2026-09-03). Releases executable Capability Build remediation and exact production checkpoints.

## Identity, purpose and boundary

**Capability:** `Tools@v5`

Defines canonical Tool production plus the current Capability production/build Tools.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Tools.Production` | Standard | `AIDE_ToolsProduction@v3` | v2 |
| `Tools.UpdateCapabilityElements` | Tool | `AIDE_UpdateCapabilityElementsTool@v1` | v1 |
| `Tools.BuildCapability` | Tool | `AIDE_BuildCapabilityTool@v6` | v4 |
| `Tools.CapabilityBuilder` | Tool | `AIDE_CapabilityBuilderTool@v4` | v4 |

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

Tools@v4
  Tools.Production@v2 -> AIDE_ToolsProduction@v3
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v3 -> AIDE_BuildCapabilityTool@v5
  Tools.CapabilityBuilder@v3 -> AIDE_CapabilityBuilderTool@v3

Tools@v5
  Tools.Production@v2 -> AIDE_ToolsProduction@v3
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v4 -> AIDE_BuildCapabilityTool@v6
  Tools.CapabilityBuilder@v4 -> AIDE_CapabilityBuilderTool@v4
```

`Tools@v4` advances only Tools.Production for the canonical Tool orientation contract. The other
Element releases remain unchanged.

## Element Release History

- `Tools.Production@v1` — baseline adoption of `AIDE_ToolsProduction@v2`; no new semantic change asserted.
- `Tools.Production@v2` — defines value-based Contents/Summary production for substantial canonical Tools.
- `Tools.UpdateCapabilityElements@v1` — baseline adoption of `AIDE_UpdateCapabilityElementsTool@v1`; no new semantic change asserted.
- `Tools.BuildCapability@v1` — baseline adoption of `AIDE_BuildCapabilityTool@v3`; no new semantic change asserted.
- `Tools.CapabilityBuilder@v1` — baseline adoption of `AIDE_CapabilityBuilderTool@v1`; no new semantic change asserted.
- `Tools.BuildCapability@v2` — resolves Registry publication to `AIDE_DeploymentRegistryTool@v1` and current `AIDE_CapabilityBuild@v2`.
- `Tools.CapabilityBuilder@v2` — emits the current immutable Capability Package Registry envelope and keeps post-Build result external.
- `Tools.BuildCapability@v3` — resolves effective Build Target Profiles/Definitions, applicability and target output obligations before WorkPackage authorisation.
- `Tools.CapabilityBuilder@v3` — produces complete applicable target contributions with exact Profile/Definition/output provenance.
- `Tools.BuildCapability@v4` — maps specialised facts deterministically into WorkPackage v3, fixes current-call migration wording and propagates coordinated Release Batch use.
- `Tools.CapabilityBuilder@v4` — validates snapshot-relative generated Tags before Package freeze and keeps post-Build workflow state outside Package bytes.

## Element Production

```yaml
ElementProduction:
  Tools.Production:
    EvaluatedInputs: {Capabilities_Tools_Design: v7, AIDE_DocumentationMethodology: v28}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v2
  Tools.UpdateCapabilityElements:
    EvaluatedInputs: {Capabilities_UpdateCapabilityElements_Tool_Design: v1, AIDE_Capability: v3}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
  Tools.BuildCapability:
    EvaluatedInputs: {Capabilities_BuildCapability_Tool_Design: v6, AIDE_CapabilityBuild: v4}
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v4
  Tools.CapabilityBuilder:
    EvaluatedInputs: {Capabilities_CapabilityBuilder_Tool_Design: v4, AIDE_CapabilityBuild: v4}
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v4
```

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

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Tools_Design_v7, AIDE_ToolsProduction@v3, AIDE_BuildCapabilityTool@v6, AIDE_CapabilityBuilderTool@v4
