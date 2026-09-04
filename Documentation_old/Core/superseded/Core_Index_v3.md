# Core — Index

> **Version 3** (2026-08-31). Registers Bootstrap as a Core system foundation and records
> Principles and Working Practices as top-level independently deployable AIDE guidance concerns.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic:** Core  
**Project container / master folder:** `AIDE/Core/`

Core holds the system-wide foundations and the reference view of the AIDE structure. Development
and product Domains remain consumers of AIDE rather than children of the Core corpus.

## Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Core | None | `Core` | independent | expanded |
| Domain | Core | `Core_Domain` | inherits | expanded |
| Bootstrap | Core | `Core_Bootstrap` | inherits | expanded |

## Local configuration

None.

## Document register

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Core_Index` | v3 | Index | established | Current |
| `Core_System_Design` | v6 | Design | established | Current |
| `Core_System_Decisions` | v5 | Decisions | established | Current |
| `Core_Domain_Design` | v1 | Design | established | Current |
| `Core_Domain_Decisions` | v1 | Decisions | established | Current |
| `AIDE_Domain_Standard` | v1 | Standard | established | Current |
| `Core_Bootstrap_Design` | v2 | Design | established | Current |
| `Core_Bootstrap_Decisions` | v2 | Decisions | established | Current |
| `AIDE_Bootstrap_Standard` | v1 | Standard | established | Current |

### Withdrawn, renamed or rehomed

None.

## Core subtopics

| Subtopic | Core role | Authoritative design | Canonical outcome |
|---|---|---|---|
| Domain | System-wide operating/governance-context foundation | `Core_Domain_Design_v1` | `AIDE_Domain@v1` |
| Bootstrap | Stable AIDE activation/startup foundation | `Core_Bootstrap_Design_v2` | `AIDE_Bootstrap@v1` |

Development/product Domains are consumers of AIDE and are not Core subtopics or components of the
AIDE system tree.

## Project-container map

| Canonical concern | Master folder / GPT Project |
|---|---|
| Core | `Core` |
| Principles | `Principles` |
| Working Practices | `Working Practices` |
| Project Design | `Design Project` |
| Build | `Build` |
| Capabilities | `Capabilities` |
| AI Deployment | `AI Deployment` |
| Documentation Methodology | `Document Methodology` |
| Generated common bundle | `bundles` |

Project-container boundaries are operational context boundaries; they do not have to mirror the
conceptual ownership tree one-for-one.

## Assets register

None.

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: Core_System_Design_v6, Core_Domain_Design_v1, Core_Bootstrap_Design_v2
