# Capabilities — Index

> **Version 14** (2026-08-30). Promotes generic Deployment out of Capabilities, closes the
> OpenAI local shared-route evidence gate, and records Documentation Methodology v18 reconciliation.
> canonical Review/Migration Tools, Build Capability Tool Design/outcome, and the custom Tool outcome
> type. Deployment/platform evidence are now the remaining principal Capabilities work.
>
> Created: 2026-08-27 | Last modified: 2026-08-30

---

## §1 — Project identity

**Project:** AIDE — Capabilities

**Topic:** Capabilities

**Purpose:** Define reusable infrastructure by which AI-facing capabilities are designed, built
into canonical outcomes, tagged/classified, scoped, connected to dependencies, transitioned,
realised for platforms, packaged with logical deployment intent, and independently reviewed.

**Parent system:** AIDE

**Master folder:** `AIDE/Capabilities/`

**Methodology:** `DocumentationMethodology` v17

## §2 — Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Capabilities | AIDE | `Capabilities` | independent | expanded |
| Standards | Capabilities | `Capabilities_Standards` | inherits | expanded |
| Tools | Capabilities | `Capabilities_Tools` | inherits | expanded |
| Tags | Capabilities | `Capabilities_Tags` | inherits | expanded |
| Scope | Capabilities | `Capabilities_Scope` | inherits | expanded |
| Dependencies | Capabilities | `Capabilities_Dependencies` | inherits | expanded |
| Migration | Capabilities | `Capabilities_Migration` | inherits | expanded |
| Migration Tool | Migration | `Capabilities_Migration_Tool` | inherits | expanded |
| Build Capability Tool | Capabilities | `Capabilities_BuildCapability_Tool` | inherits | expanded |
| Review | Capabilities | `Capabilities_Review` | inherits | expanded |
| Review Tool | Review | `Capabilities_Review_Tool` | inherits | expanded |

WorkPackage belongs under `AIDE/Build/WorkPackage`.

## §3 — Local configuration

### Custom document types

| Type | Role | Holds | Lifecycle | Distribution |
|---|---|---|---|---|
| `DocMethReviewItems` | Review input | Consequences/questions for separate DocMeth review | Living until dispositioned | Internal |
| `Standard` | Outcome | Published AI-facing capability rules derived from Capability Design | Living/versioned by capability release | Consuming AI environments |
| `Tool` | Outcome | Published AI-facing invokable capability action derived from Tool Design/Capability Design | Living/versioned by capability release | Consuming AI environments |

### Other local configuration

Build Config inheritance/defaults remain environment/configuration detail. Generic Deployment
Config belongs to the AI Deployment workstream.

## §4 — Document register

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Capabilities_Index` | v14 | Index | established | Current |
| `Capabilities_Brief` | v7 | Brief | established | Current |
| `Capabilities_Design` | v8 | Design | established | Current |
| `Capabilities_Decisions` | v14 | Decisions | established | Current |
| `Capabilities_WorkRegister` | v12 | WorkRegister | established | Current |
| `Capabilities_OpenItems` | v14 | OpenItems | established | Current |
| `Capabilities_Overview` | v13 | Overview | established | Current architecture surface |
| `Capabilities_DocMethReviewItems` | v4 | DocMethReviewItems | custom | Current |
| `Capabilities_Tags_Design` | v1 | Design | established | Current |
| `AIDE_Tags_Standard` | v1 | Standard | custom | Current; identity `AIDE_Tags@v1` |
| `Capabilities_Scope_Design` | v1 | Design | established | Current |
| `AIDE_Scope_Standard` | v1 | Standard | custom | Current; identity `AIDE_Scope@v1` |
| `Capabilities_Dependencies_Design` | v2 | Design | established | Current |
| `AIDE_Dependencies_Standard` | v2 | Standard | custom | Current; identity `AIDE_Dependencies@v2` |
| `Capabilities_Migration_Brief` | v1 | Brief | established | Current |
| `Capabilities_Migration_Design` | v1 | Design | established | Current |
| `AIDE_Migration_Standard` | v1 | Standard | custom | Current; identity `AIDE_Migration@v1` |
| `Capabilities_Migration_Tool_Design` | v1 | Design | established | Current Tool source |
| `AIDE_Migration_Tool` | v1 | Tool | custom | Current; identity `AIDE_MigrationTool@v1` |
| `Capabilities_Review_Design` | v1 | Design | established | Current |
| `Capabilities_Review_Decisions` | v1 | Decisions | established | Current |
| `AIDE_Review_Standard` | v1 | Standard | custom | Current; identity `AIDE_Review@v1` |
| `AIDE_ReviewProfiles_Standard` | v1 | Standard | custom | Current; identity `AIDE_ReviewProfiles@v1` |
| `Capabilities_Review_Tool_Design` | v1 | Design | established | Current Tool source |
| `AIDE_Review_Tool` | v1 | Tool | custom | Current; identity `AIDE_ReviewTool@v1` |
| `Capabilities_Standards_Brief` | v2 | Brief | established | Current |
| `Capabilities_Standards_Design` | v4 | Design | established | Current |
| `AIDE_StandardsProduction_Standard` | v1 | Standard | custom | Current; identity `AIDE_StandardsProduction@v1` |
| `AIDE_StandardsUsage_Standard` | v1 | Standard | custom | Current; identity `AIDE_StandardsUsage@v1` |
| `Capabilities_Tools_Brief` | v2 | Brief | established | Current |
| `Capabilities_Tools_Design` | v2 | Design | established | Current |
| `Capabilities_BuildCapability_Tool_Design` | v1 | Design | established | Current Tool source |
| `AIDE_BuildCapability_Tool` | v1 | Tool | custom | Current; identity `AIDE_BuildCapabilityTool@v1` |

### Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `Capabilities_Index` v13 | v14 | Deployment promoted; evidence gate closed |
| `Capabilities_Brief` v6 | v7 | Deployment boundary promoted |
| `Capabilities_Design` v7 | v8 | Deployment removed from peer component list |
| `Capabilities_Decisions` v13 | v14 | Promotion/evidence/DocMeth decisions appended |
| `Capabilities_WorkRegister` v11 | v12 | Deployment work moved out |
| `Capabilities_OpenItems` v13 | v14 | Q1-Q3 moved; Q11 narrowed |
| `Capabilities_Overview` v12 | v13 | Current model refreshed |
| `Capabilities_DocMethReviewItems` v3 | v4 | Review items dispositioned by DocMeth v18 |
| `Capabilities_Brief` v5 | v6 | Canonical-production Tool/output closeout |
| `Capabilities_Design` v6 | v7 | Build Capability Tool + canonical output registration |
| `Capabilities_Decisions` v12 | v13 | Decisions D84–D86 appended |
| `Capabilities_WorkRegister` v10 | v11 | Non-Deployment canonical outputs completed |
| `Capabilities_OpenItems` v12 | v13 | Canonical output gap closed |
| `Capabilities_Overview` v11 | v12 | Current model refreshed |
| `Capabilities_Index` v12 | v13 | New outputs/custom Tool type registered |
| `Capabilities_Brief` v4 | v5 | Migration/version/package checkpoint |
| `Capabilities_Design` v5 | v6 | Migration + reconciliations + producer manifest contract |
| `Capabilities_Decisions` v11 | v12 | Decisions D72–D83 appended |
| `Capabilities_WorkRegister` v9 | v10 | Items 1–5 completed; Deployment next |
| `Capabilities_OpenItems` v11 | v12 | Migration/Q7/Q8 closed; platform evidence sharpened |
| `Capabilities_Overview` v10 | v11 | Current model refreshed |
| `Capabilities_Index` v11 | v12 | New/current child corpus registered |
| `Capabilities_DocMethReviewItems` v2 | v3 | Temporary state + compact metadata + Migration update seam |
| `Capabilities_Dependencies_Design` v1 | v2 | Dependency order/checkpoint reconciliation |
| `AIDE_Dependencies_Standard` v1 | v2 | Published dependency order/checkpoint contract |
| `Capabilities_Standards_Brief` v1 | v2 | Stale boundaries removed |
| `Capabilities_Standards_Design` v3 | v4 | Eight-component reconciliation |
| `Capabilities_Tools_Brief` v1 | v2 | Shared component boundaries/migration corrected |
| `Capabilities_Tools_Design` v1 | v2 | Shared Scope/Migration + bounded judgment reconciliation |

## §5 — Assets register

None.

## §6 — Current priority

1. Maintain capability semantics/production and producer-side Package + deployment-intent contracts.
2. Supply target-compatible contributions through AIDE Build.
3. Hand generic deployment/composition/verification to the AI Deployment workstream.
4. Resolve Environment/shared communication ownership with the relevant AIDE workstreams.
5. Treat broader per-platform evidence as implementation evidence, not a Capabilities architecture gate.

No core Capabilities architecture output remains open in this project.

## §7 — Relationships

- **AIDE/Core:** whole-system structure, formal identity, bootstrap primitive.
- **AIDE/Design:** design methodology; Documentation Methodology later consumes generic metadata/
  temporary-state seams.
- **AIDE/Build:** WorkPackage and generic build execution/return.
- **AI Deployment:** consumes capability packages/logical deployment intent and owns generic
  set-aware delivery/reconciliation/verification.
- **AIDE/Environment:** supplies platform/model/route/configuration/access facts.
- **Development domains:** consume AIDE but are outside the AIDE system topic tree.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Capabilities_Brief_v7, Capabilities_Design_v8, Capabilities_Decisions_v14
References: Capabilities_Overview_v13, Capabilities_OpenItems_v14, Capabilities_WorkRegister_v12, Capabilities_DocMethReviewItems_v4
