
# Capabilities — Index

> **Version 21** (2026-09-02). Reconciles Capability Package/post-Build Registry semantics to AI Deployment v5; Build Target/Profile redesign remains deferred.

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
| Standards | `Capabilities_Standards_Definition_v2` | `AIDE_StandardsProduction@v3`, `AIDE_StandardsUsage@v2` |
| Tools | `Capabilities_Tools_Definition_v2` | `AIDE_ToolsProduction@v2`, `AIDE_UpdateCapabilityElementsTool@v1`, `AIDE_BuildCapabilityTool@v4`, `AIDE_CapabilityBuilderTool@v2` |
| Tags | `Capabilities_Tags_Definition_v2` | `AIDE_Tags@v2` |
| Scope | `Capabilities_Scope_Definition_v2` | `AIDE_Scope@v2` |
| Dependencies | `Capabilities_Dependencies_Definition_v2` | `AIDE_Dependencies@v3` |
| Migration | `Capabilities_Migration_Definition_v2` | `AIDE_Migration@v2`, `AIDE_MigrationTool@v2` |
| Review | `Capabilities_Review_Definition_v2` | `AIDE_Review@v3`, `AIDE_ReviewProfiles@v2`, `AIDE_ReviewTool@v3` |
| Messaging | `Capabilities_Messaging_Definition_v2` | `AIDE_Messaging@v2`, `AIDE_MessagingTool@v2` |

### Parent/current architecture documents

| Document | Version | Type | Status |
|---|---:|---|---|
| `Capabilities_Index` | v21 | Index | Current |
| `Capabilities_Brief` | v12 | Brief | Current |
| `Capabilities_Overview` | v18 | Overview | Current human TLDR |
| `Capabilities_Design` | v13 | Design | Current |
| `Capabilities_Decisions` | v18 | Decisions | Current history |
| `Capabilities_Capability_Design` | v1 | Design | Current |
| `Capabilities_Capability_Decisions` | v1 | Decisions | Current |
| `AIDE_Capability_Standard` | v1 | Standard | `AIDE_Capability@v1` |
| `Capabilities_CapabilityBuild_Design` | v2 | Design | Current |
| `Capabilities_CapabilityBuild_Decisions` | v2 | Decisions | Current |
| `AIDE_CapabilityBuild_Standard` | v2 | Standard | `AIDE_CapabilityBuild@v2` |

### Binder boundaries

Capabilities deliberately uses a partitioned Binder set because of document volume/context limits:

| Binder | Boundary |
|---|---|
| `Capabilities_Binder_Core_v7` | parent architecture + Capability/Capability Build contracts |
| `Capabilities_Binder_StandardsTools_v4` | Standards/Tools Definitions, production contracts and Capability production/build Tools |
| `Capabilities_Binder_Runtime_v3` | Tags/Scope/Dependencies/Migration Definitions and current outcomes |
| `Capabilities_Binder_Review_v5` | Review Definition and current Review corpus |
| `Capabilities_Binder_Messaging_v5` | Messaging Definition and current Messaging corpus |

`Capabilities_Binder_Set_Index_v1` is the lightweight generated map. The partitions collectively
cover the current stable corpus without a duplicate giant aggregate Binder. Curated Review material
is not a Binder.

### Live state

- `Capabilities_WIP` — current continuation; load separately.
- `Capabilities_WorkRegister` — current confirmed owed work; load separately.
- `Capabilities_OpenItems` — current unresolved attention; load separately.
- `Capabilities_Working_CapabilityArchitectureRedesign` — series closed by this pass; move current v2 to Superseded after application.

### Review programme

Reviews A–C are complete at High. The Registry producer/deployment seam is reconciled. Review D remains **ON HOLD** while the active Build Target/Profile and remaining AI Deployment Set/output/delivery design is finalised. Review E remains later.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_CapabilityBuild@v2
References: Capabilities_WIP_v18, Capabilities_WorkRegister_v18, Capabilities_OpenItems_v16
