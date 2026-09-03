# Capabilities — Index

> **Version 24** (2026-09-03). Registers Review D R1 remediation and the Inspect R2 baseline.

`{scope: "AIDE/Capabilities", type: DocumentationTopic}`

## Contents

- **Capabilities** — reusable AI-facing capability semantics and specialised Capability Build.
  - **Capability model** — Definition, Elements, production state and releases.
  - **Capability Build** — Build request, Builder and complete Package contract.
  - **Standards**, **Tools**, **Tags**, **Scope**, **Dependencies**, **Migration**, **Review**, **Messaging** — current peer Capabilities.

## Documentation

### Topic/subtopic ownership

| Subtopic | Required Definition | Canonical outcomes |
|---|---|---|
| Standards | `Capabilities_Standards_Definition_v4` | `AIDE_StandardsProduction@v4`, `AIDE_StandardsUsage@v2` |
| Tools | `Capabilities_Tools_Definition_v5` | `AIDE_ToolsProduction@v3`, `AIDE_UpdateCapabilityElementsTool@v1`, `AIDE_BuildCapabilityTool@v6`, `AIDE_CapabilityBuilderTool@v4` |
| Tags | `Capabilities_Tags_Definition_v3` | `AIDE_Tags@v3` |
| Scope | `Capabilities_Scope_Definition_v3` | `AIDE_Scope@v3` |
| Dependencies | `Capabilities_Dependencies_Definition_v3` | `AIDE_Dependencies@v3` |
| Migration | `Capabilities_Migration_Definition_v4` | `AIDE_Migration@v3`, `AIDE_MigrationTool@v3`, `AIDE_UpdateTool@v1` |
| Review | `Capabilities_Review_Definition_v4` | `AIDE_Review@v4`, `AIDE_ReviewProfiles@v2`, `AIDE_ReviewTool@v3` |
| Messaging | `Capabilities_Messaging_Definition_v3` | `AIDE_Messaging@v2`, `AIDE_MessagingTool@v2` |

### Parent/current architecture documents

| Document | Version | Type | Status |
|---|---:|---|---|
| `Capabilities_Index` | v24 | Index | Current |
| `Capabilities_Brief` | v14 | Brief | Current |
| `Capabilities_Overview` | v20 | Overview | Current human TLDR |
| `Capabilities_Design` | v15 | Design | Current |
| `Capabilities_Decisions` | v21 | Decisions | Current history |
| `Capabilities_Capability_Design` | v3 | Design | Current |
| `Capabilities_Capability_Decisions` | v2 | Decisions | Current |
| `AIDE_Capability_Standard` | v3 | Standard | `AIDE_Capability@v3` |
| `Capabilities_CapabilityBuild_Design` | v4 | Design | Current |
| `Capabilities_CapabilityBuild_Decisions` | v4 | Decisions | Current |
| `AIDE_CapabilityBuild_Standard` | v4 | Standard | `AIDE_CapabilityBuild@v4` |
| `Capabilities_BuildTargetProfile_Design` | v2 | Design | Current |
| `Capabilities_AIDECore_BuildTargetProfile` | v2 | Reference/Profile | Current `AIDE_Core` Profile |

### Binder boundaries

Capabilities deliberately uses a partitioned Binder set because of document volume/context limits:

| Binder | Boundary |
|---|---|
| `Capabilities_Binder_Core_v10` | parent architecture + Capability/Capability Build/Profile contracts |
| `Capabilities_Binder_StandardsTools_v7` | Standards/Tools Definitions, production contracts and current Capability production/build Tools |
| `Capabilities_Binder_Runtime_v5` | Tags/Scope/Dependencies/Migration Definitions and current outcomes |
| `Capabilities_Binder_Review_v7` | Review Definition and current Review corpus |
| `Capabilities_Binder_Messaging_v6` | Messaging Definition and current Messaging corpus |

`Capabilities_Binder_Set_Index_v5` is the lightweight generated map. The partitions collectively
cover the current stable corpus without a duplicate giant aggregate Binder. Curated Review material
is not a Binder.

### Live state

- `Capabilities_WIP` — current continuation; load separately.
- `Capabilities_WorkRegister` — current confirmed owed work; load separately.
- `Capabilities_OpenItems` — current unresolved attention; load separately.

### Review programme

Reviews A–C are complete at High. Restarted Review D R1 is complete and Lead-dispositioned. This
package supplies the remediated baseline for Inspect/High/Full R2 verification.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_CapabilityBuild@v4
References: Capabilities_WIP_v20, Capabilities_WorkRegister_v20, Capabilities_OpenItems_v16
