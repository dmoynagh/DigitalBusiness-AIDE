# Build — Index

> **Version 1** (2026-08-30). Registers the initial generic Build and WorkPackage corpus.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic:** Build  
**Project container / master folder:** `AIDE/Build/`  
**Purpose:** Generic objective-driven execution of defined work.

## Topic declarations

| Name | Parent | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Build | AIDE | `Build` | independent | expanded |
| WorkPackage | Build | `Build_WorkPackage` | inherits | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Build_Index` | v1 | Index | Current |
| `Build_Design` | v1 | Design | Current |
| `Build_Decisions` | v1 | Decisions | Current |
| `Build_WorkPackage_Design` | v1 | Design | Current |
| `AIDE_Build_Standard` | v1 | Standard | Current; identity `AIDE_Build@v1` |
| `AIDE_WorkPackage_Standard` | v1 | Standard | Current; identity `AIDE_WorkPackage@v1` |

## Relationships

- Project Design defines work; WorkPackage is the principal governed handoff.
- Build returns evidence/outcomes; design-shaping issues return to Project Design.
- Platform-specific execution knowledge implements this behavioural contract without redefining it.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: ProjectDesign_Design_v1
