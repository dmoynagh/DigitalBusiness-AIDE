# Build — Index

> **Version 3** (2026-08-31). Registers the deployment-facing Build output identity/integrity and composition-posture clarification.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

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
| `Build_Index` | v3 | Index | Current |
| `Build_Design` | v3 | Design | Current |
| `Build_Decisions` | v3 | Decisions | Current |
| `Build_WorkPackage_Design` | v1 | Design | Current |
| `AIDE_Build_Standard` | v3 | Standard | Current; identity `AIDE_Build@v3` |
| `AIDE_WorkPackage_Standard` | v1 | Standard | Current; identity `AIDE_WorkPackage@v1` |

## Relationships

- Project Design defines work; WorkPackage is the principal governed handoff.
- Build returns evidence/outcomes; design-shaping issues return to Project Design.
- Canonical Standards/Tools and other authoritative outcomes are upstream semantic sources for derived platform/consumption representations.
- Build may produce authorised subsets, platform representations, assembled consumption artefacts and packages without making them authoritative sources or claiming they are deployed.
- Deployment-facing Build outputs expose source provenance, concrete Build-output identity/integrity, and whether the output is a mechanically assemblable member/contribution or a Build-owned assembled consumption artefact.
- Platform-specific execution knowledge implements this behavioural contract without redefining it.
- AI Deployment owns target-state reconciliation and runtime verification after Build output exists.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: ProjectDesign_Design_v1, AIDE_Deployment@v1
