# AI Deployment — Index

> **Version 8** (2026-09-03). Registers the Review D R2 Set Release pointer correction; canonical Deployment remains v7.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

## Project identity

**Topic/workstream:** AI Deployment  
**Repository:** `DigitalBusiness-AIDE`  
**Project container / master folder:** `Documentation/AI Deployment/`  
**Purpose:** Generic Registry-backed, set-aware, policy-aware deployment of validated built artefacts into AI runtime surfaces.

## Contents

- **AI Deployment** — desired-state selection, target reconciliation/delivery and runtime verification.  
  `{standard: AIDE_Deployment@v7}`
- **Deployment Registry** — validated Deployable Package registration, immutable package-instance lifecycle and Release Batches.  
  `{tool: AIDE_DeploymentRegistryTool@v2}`
- **Set Release** — exact resolution, immutable `<Set>@vN` releases and final Deployment Outputs.
- **Target Adapter** — Delivery Actions, platform/channel mechanics, layered verification and per-Target state.
- **AIDE Core Deployment** — concrete `AIDE_Core` Set/output/action/Target reference configuration.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v8 | Index | Current |
| `AIDeployment_Design` | v8 | Design | Current |
| `AIDeployment_Decisions` | v7 | Decisions | Current |
| `AIDeployment_Registry_Design` | v2 | Design | Current |
| `AIDeployment_SetRelease_Design` | v2 | Design | Current |
| `AIDeployment_TargetAdapter_Design` | v1 | Design | Current |
| `AIDeployment_AIDECore_Reference` | v2 | Reference/configuration | Current |
| `AIDeployment_OpenAI_Reference` | v3 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v7 | Standard | Current; identity `AIDE_Deployment@v7` |
| `AIDE_Deployment_Tool` | v7 | Tool | Current; identity `AIDE_DeploymentTool@v7` |
| `AIDE_DeploymentRegistry_Tool` | v2 | Tool | Current; identity `AIDE_DeploymentRegistryTool@v2` |

## Binder boundary

`AIDeployment_Binder_v8` is the current generated top-level consumption Binder. Live state remains
separate.

## Current boundary

Producer/domain owns deployable artefact semantics and PackageKind-specific Build/package content. Build/specialised producer Build produces validated packages and supplies source/build provenance, concrete PackageId/integrity and Build-owned composition posture.

AI Deployment owns the **Deployment Registry** contract and lifecycle. `Deployable Package` is the generic Registry unit; `Capability Package` is the first specialised kind. Registered PackageIds are immutable; Current/Available/Deprecated/Withdrawn/Release Batch state is Registry-owned metadata.

Deployment Set membership does not erase upstream required presence. Deployment may mechanically assemble eligible `MemberContribution` outputs, treats an `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary, and owns policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Environment/platform configuration remains the source of physical Registry/Target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

## Current design status

The generic design required for the confirmed AIDE Core outcome is closed: fixed desired membership
resolves through eligible Registry supply into one immutable `AIDE_Core@vN`, four final Outputs, configured Delivery
Actions, independently reconcilable Targets and layered runtime verification. Remaining provider
uncertainties are empirical adapter facts, not missing generic architecture.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7, AIDE_Build@v8
References: AIDeployment_Design_v8, AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v2, AIDE_DeploymentRegistryTool@v2, AIDE_CapabilityBuild@v4, AIDE_Dependencies@v3, AIDE_Tags@v3
