# AI Deployment — Index

> **Version 4** (2026-08-31). Aligns AI Deployment with the Build v3 output contract, including
> explicit Build-owned composition posture.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic set-aware, policy-aware deployment of built artefacts into AI runtime surfaces.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v4 | Index | Current |
| `AIDeployment_Design` | v4 | Design | Current |
| `AIDeployment_Decisions` | v4 | Decisions | Current |
| `AIDeployment_OpenAI_Reference` | v2 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v4 | Standard | Current; identity `AIDE_Deployment@v4` |
| `AIDE_Deployment_Tool` | v4 | Tool | Current; identity `AIDE_DeploymentTool@v4` |

## Boundary

Producer/domain owns deployable artefact semantics and requirements. Dependencies owns dependency/required-presence semantics. Build performs semantic production from current authoritative inputs and supplies source provenance, Build-output/package identity and integrity, and a Build-owned `CompositionPosture` of `MemberContribution` or `AssembledConsumptionArtefact`. AI Deployment consumes that posture: it may mechanically assemble `MemberContribution` outputs, treats an `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary, and owns policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Deployment Set membership does not erase upstream required presence. Environment/platform configuration remains the source of physical target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Capabilities_Design_v8, Build_Design_v3, AIDE_Build@v3, AIDE_Dependencies@v2
