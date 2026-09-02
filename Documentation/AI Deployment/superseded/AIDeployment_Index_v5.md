# AI Deployment — Index

> **Version 5** (2026-09-02). Adds the Deployment Registry/Deployable Package boundary and first Registry Tool while retaining the current Deployment Set/Target reconciliation model for later refinement.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic Registry-backed, set-aware, policy-aware deployment of validated built artefacts into AI runtime surfaces.

## Contents

- **AI Deployment** — desired-state selection, target reconciliation/delivery and runtime verification.  
  `{standard: AIDE_Deployment@v5}`
- **Deployment Registry** — validated Deployable Package registration, immutable package-instance lifecycle and Release Batches.  
  `{tool: AIDE_DeploymentRegistryTool@v1}`

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v5 | Index | Current |
| `AIDeployment_Design` | v5 | Design | Current |
| `AIDeployment_Decisions` | v5 | Decisions | Current |
| `AIDeployment_Registry_Design` | v1 | Design | Current |
| `AIDeployment_OpenAI_Reference` | v2 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v5 | Standard | Current; identity `AIDE_Deployment@v5` |
| `AIDE_Deployment_Tool` | v5 | Tool | Current; identity `AIDE_DeploymentTool@v5` |
| `AIDE_DeploymentRegistry_Tool` | v1 | Tool | Current; identity `AIDE_DeploymentRegistryTool@v1` |

## Current boundary

Producer/domain owns deployable artefact semantics and PackageKind-specific Build/package content. Build/specialised producer Build produces validated packages and supplies source/build provenance, concrete PackageId/integrity and Build-owned composition posture.

AI Deployment owns the **Deployment Registry** contract and lifecycle. `Deployable Package` is the generic Registry unit; `Capability Package` is the first specialised kind. Registered PackageIds are immutable; Current/Available/Deprecated/Withdrawn/Release Batch state is Registry-owned metadata.

Deployment Set membership does not erase upstream required presence. Deployment may mechanically assemble eligible `MemberContribution` outputs, treats an `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary, and owns policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Environment/platform configuration remains the source of physical Registry/Target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

## Current design status

The Build→Registry seam is defined in v5. The next active design layer will finalise Deployment Set Definition selectors, exact resolved-set state, deployment output/package definitions, Delivery Actions and trigger-to-Set resolution. Those details are deliberately not frozen by the Registry change package.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v5, AIDE_Build@v6
References: AIDeployment_Registry_Design_v1, AIDE_DeploymentRegistryTool@v1, AIDE_CapabilityBuild@v1, AIDE_Dependencies@v3, AIDE_Tags@v2
