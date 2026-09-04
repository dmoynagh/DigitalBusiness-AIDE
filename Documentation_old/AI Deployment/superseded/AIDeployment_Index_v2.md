# AI Deployment — Index

> **Version 2** (2026-08-31). Registers the required-presence and target-policy reconciliation update.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic set-aware, policy-aware deployment of built artefacts into AI runtime surfaces.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v2 | Index | Current |
| `AIDeployment_Design` | v2 | Design | Current |
| `AIDeployment_Decisions` | v2 | Decisions | Current |
| `AIDeployment_OpenAI_Reference` | v2 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v2 | Standard | Current; identity `AIDE_Deployment@v2` |
| `AIDE_Deployment_Tool` | v2 | Tool | Current; identity `AIDE_DeploymentTool@v2` |

## Boundary

Producer/domain owns deployable artefact semantics and requirements. Dependencies owns dependency/required-presence semantics. Build produces target-compatible contributions. AI Deployment performs set-aware and policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Deployment Set membership does not erase upstream required presence. Environment/platform configuration remains the source of physical target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Capabilities_Design_v8, Build_Design_v1, AIDE_Dependencies@v2
