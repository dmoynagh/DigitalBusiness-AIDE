# Core — Index

> **Version 5** (2026-09-01). Registers the Review A Round 1 Core substrate remediation:
> `AIDE_Index@v2`, `AIDE_Domain@v3`, `AIDE_Bootstrap@v2` and their coordinated current
> Design/Decisions, while leaving the operational container map unchanged.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Core", type: DocumentationTopic}`

## Contents

- **Core** — AIDE system-wide foundations and reference architecture.
  - **Index** — generic hierarchical item registration and Item Type framework.  
    `{design: Core_Index_Design_v2, standard: AIDE_Index@v2}`
  - **Domain** — contextual operating/governance boundary resolution.  
    `{design: Core_Domain_Design_v3, standard: AIDE_Domain@v3}`
  - **Bootstrap** — stable startup activation seam and Profile/Contribution model.  
    `{design: Core_Bootstrap_Design_v3, standard: AIDE_Bootstrap@v2}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Core | None | `Core` | independent | expanded |
| Index | Core | `Core_Index` | inherits | expanded |
| Domain | Core | `Core_Domain` | inherits | expanded |
| Bootstrap | Core | `Core_Bootstrap` | inherits | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Core_Index` | v5 | Index | Current |
| `Core_System_Design` | v8 | Design | Current |
| `Core_System_Decisions` | v7 | Decisions | Current |
| `Core_Index_Design` | v2 | Design | Current |
| `Core_Index_Decisions` | v2 | Decisions | Current |
| `AIDE_Index_Standard` | v2 | Standard | Current; identity `AIDE_Index@v2` |
| `Core_Domain_Design` | v3 | Design | Current |
| `Core_Domain_Decisions` | v3 | Decisions | Current |
| `AIDE_Domain_Standard` | v3 | Standard | Current; identity `AIDE_Domain@v3` |
| `Core_Bootstrap_Design` | v3 | Design | Current |
| `Core_Bootstrap_Decisions` | v3 | Decisions | Current |
| `AIDE_Bootstrap_Standard` | v2 | Standard | Current; identity `AIDE_Bootstrap@v2` |

### Current context/container map

Chat-project/master-folder/container boundaries are working/context boundaries. They may contain one or more top-level
topics and are not semantic ownership boundaries.

| Canonical concern | Current master folder/container |
|---|---|
| Core | `AIDE/Core/` |
| Principles | `AIDE/Principles/` |
| Working Practices | `AIDE/Working Practices/` |
| Project Design | `AIDE/Project Design/` |
| Build | `AIDE/Build/` |
| Capabilities | `AIDE/Capabilities/` |
| AI Deployment | `AIDE/AI Deployment/` |
| Documentation Methodology | `AIDE/Document Methodology/` |
| Generated common bundles | `Documentation/_bundles/` or current environment equivalent |

The canonical and physical name for Project Design is **Project Design**. Earlier current-document
references to `Design Project` were documentation/configuration errors, not a historical folder
rename.

### Local configuration

None.

### Assets

None.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v2
References: Core_System_Design_v8, Core_Index_Design_v2, Core_Domain_Design_v3, Core_Bootstrap_Design_v3
