# Capabilities — Index

> **Version 23** (2026-09-02). Registers aggregate Update, document-orientation releases and the active Review D baseline.

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
| Standards | `Capabilities_Standards_Definition_v3` | `AIDE_StandardsProduction@v4`, `AIDE_StandardsUsage@v2` |
| Tools | `Capabilities_Tools_Definition_v4` | `AIDE_ToolsProduction@v3`, `AIDE_UpdateCapabilityElementsTool@v1`, `AIDE_BuildCapabilityTool@v5`, `AIDE_CapabilityBuilderTool@v3` |
| Tags | `Capabilities_Tags_Definition_v2` | `AIDE_Tags@v2` |
| Scope | `Capabilities_Scope_Definition_v2` | `AIDE_Scope@v2` |
| Dependencies | `Capabilities_Dependencies_Definition_v2` | `AIDE_Dependencies@v3` |
| Migration | `Capabilities_Migration_Definition_v3` | `AIDE_Migration@v3`, `AIDE_MigrationTool@v3`, `AIDE_UpdateTool@v1` |
| Review | `Capabilities_Review_Definition_v3` | `AIDE_Review@v4`, `AIDE_ReviewProfiles@v2`, `AIDE_ReviewTool@v3` |
| Messaging | `Capabilities_Messaging_Definition_v2` | `AIDE_Messaging@v2`, `AIDE_MessagingTool@v2` |

### Parent/current architecture documents

| Document | Version | Type | Status |
|---|---:|---|---|
| `Capabilities_Index` | v23 | Index | Current |
| `Capabilities_Brief` | v13 | Brief | Current |
| `Capabilities_Overview` | v19 | Overview | Current human TLDR |
| `Capabilities_Design` | v14 | Design | Current |
| `Capabilities_Decisions` | v20 | Decisions | Current history |
| `Capabilities_Capability_Design` | v2 | Design | Current |
| `Capabilities_Capability_Decisions` | v1 | Decisions | Current |
| `AIDE_Capability_Standard` | v2 | Standard | `AIDE_Capability@v2` |
| `Capabilities_CapabilityBuild_Design` | v3 | Design | Current |
| `Capabilities_CapabilityBuild_Decisions` | v3 | Decisions | Current |
| `AIDE_CapabilityBuild_Standard` | v3 | Standard | `AIDE_CapabilityBuild@v3` |
| `Capabilities_BuildTargetProfile_Design` | v1 | Design | Current |
| `Capabilities_AIDECore_BuildTargetProfile` | v1 | Reference/Profile | Current `AIDE_Core` Profile |

### Binder boundaries

Capabilities deliberately uses a partitioned Binder set because of document volume/context limits:

| Binder | Boundary |
|---|---|
| `Capabilities_Binder_Core_v9` | parent architecture + Capability/Capability Build/Profile contracts |
| `Capabilities_Binder_StandardsTools_v6` | Standards/Tools Definitions, production contracts and current Capability production/build Tools |
| `Capabilities_Binder_Runtime_v4` | Tags/Scope/Dependencies/Migration Definitions and current outcomes |
| `Capabilities_Binder_Review_v6` | Review Definition and current Review corpus |
| `Capabilities_Binder_Messaging_v5` | Messaging Definition and current Messaging corpus |

`Capabilities_Binder_Set_Index_v4` is the lightweight generated map. The partitions collectively
cover the current stable corpus without a duplicate giant aggregate Binder. Curated Review material
is not a Binder.

### Live state

- `Capabilities_WIP` — current continuation; load separately.
- `Capabilities_WorkRegister` — current confirmed owed work; load separately.
- `Capabilities_OpenItems` — current unresolved attention; load separately.

### Review programme

Reviews A–C are complete at High. The coordinated Build Target/Profile and AI Deployment design has
been applied and AI Deployment is complete. Review D has restarted from a fresh baseline; refresh
that baseline with this package before continuing its current Round work.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_CapabilityBuild@v3
References: Capabilities_WIP_v19, Capabilities_WorkRegister_v19, Capabilities_OpenItems_v16
