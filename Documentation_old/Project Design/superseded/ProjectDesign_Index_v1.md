# Project Design — Index

> **Version 1** (2026-08-30). Registers the initial Project Design corpus and canonical Standard.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic:** Project Design  
**Project container / master folder:** `AIDE/Design Project/`  
**Purpose:** Generic methodology for defining substantial work before execution.

## Topic declarations

| Name | Parent | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v1 | Index | Current |
| `ProjectDesign_Design` | v1 | Design | Current |
| `ProjectDesign_Decisions` | v1 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v1 | Standard | Current; identity `AIDE_ProjectDesign@v1` |

## Relationships

- Build consumes defined work through `AIDE_WorkPackage`.
- Domain-owned production workflows compose Project Design and Build.
- Documentation Methodology is a dedicated project/container because of its size and lifecycle, while remaining design-methodology material conceptually.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Build_Design_v1
