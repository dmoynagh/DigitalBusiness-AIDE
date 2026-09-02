# Core — Index

> **Version 7** (2026-09-02). Registers the Working Surface model and Core Knowledge store.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

`{scope: "AIDE/Core", type: DocumentationTopic}`

## Contents

- **Core** — AIDE system-wide foundations and reference architecture.
  - **Index** — generic hierarchical item registration and Item Type framework.  
    `{design: Core_Index_Design_v2, standard: AIDE_Index@v2}`
  - **Domain** — contextual operating/governance boundary resolution.  
    `{design: Core_Domain_Design_v4, standard: AIDE_Domain@v4}`
  - **Bootstrap** — stable startup activation seam and Profile/Contribution model.  
    `{design: Core_Bootstrap_Design_v3, standard: AIDE_Bootstrap@v2}`
  - **Platform / Working Surfaces** — evidence-led surface capability and mechanism facts.  
    `{design: Core_Platform_Design_v1, knowledge: Core_Knowledge_v1}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Core | None | `Core` | independent | expanded |
| Index | Core | `Core_Index` | inherits | expanded |
| Domain | Core | `Core_Domain` | inherits | expanded |
| Bootstrap | Core | `Core_Bootstrap` | inherits | expanded |
| Platform / Working Surfaces | Core | `Core_Platform` | inherits | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Core_Index` | v6 | Index | Current |
| `Core_System_Design` | v9 | Design | Current |
| `Core_System_Decisions` | v7 | Decisions | Current |
| `Core_Index_Design` | v2 | Design | Current |
| `Core_Index_Decisions` | v2 | Decisions | Current |
| `AIDE_Index_Standard` | v2 | Standard | Current; identity `AIDE_Index@v2` |
| `Core_Domain_Design` | v4 | Design | Current |
| `Core_Domain_Decisions` | v4 | Decisions | Current |
| `AIDE_Domain_Standard` | v4 | Standard | Current; identity `AIDE_Domain@v4` |
| `Core_Bootstrap_Design` | v3 | Design | Current |
| `Core_Bootstrap_Decisions` | v3 | Decisions | Current |
| `AIDE_Bootstrap_Standard` | v2 | Standard | Current; identity `AIDE_Bootstrap@v2` |
| `Core_Platform_Design` | v1 | Design | Current |
| `Core_Platform_Decisions` | v1 | Decisions | Current |
| `Core_Knowledge` | v1 | Knowledge | Current durable lateral evidence |

### Binder boundary

One top-level Core Binder containing the declared current Core documentation corpus.

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
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Index@v2
References: Core_System_Design_v10, Core_Index_Design_v2, Core_Domain_Design_v4, Core_Bootstrap_Design_v3
