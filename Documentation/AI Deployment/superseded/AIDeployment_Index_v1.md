# AI Deployment — Index

> **Version 1** (2026-08-30). Registers AI Deployment after promotion out of Capabilities.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic set-aware deployment of built artefacts into AI runtime surfaces.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v1 | Index | Current |
| `AIDeployment_Design` | v1 | Design | Current |
| `AIDeployment_Decisions` | v1 | Decisions | Current |
| `AIDeployment_OpenAI_Reference` | v1 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v1 | Standard | Current; identity `AIDE_Deployment@v1` |
| `AIDE_Deployment_Tool` | v1 | Tool | Current; identity `AIDE_DeploymentTool@v1` |

## Boundary

Capabilities produces capability-local package/build material and logical deployment intent.
Build produces target-compatible contributions. AI Deployment performs set-aware reconciliation,
delivery and runtime verification.

The dedicated GPT Project is an operational context boundary. Environment/platform configuration
remains the source of physical target facts and access references.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Capabilities_Design_v8, Build_Design_v1
