# Capabilities — Index

> **Version 15** (2026-08-31). Adopts the generic Core Index framework, records the confirmed
> Messaging integration direction as queued work, and moves high-churn live state out of the stable
> Document Register under Documentation Methodology v21.
>
> Created: 2026-08-27 | Last modified: 2026-08-31

`{scope: "AIDE/Capabilities", type: DocumentationTopic}`

## Contents

- **Capabilities** — reusable infrastructure for AI-facing Standards, Tools and supporting
  capability mechanisms.
  - **Standards** — canonical Standard production/usage contracts.
  - **Tools** — canonical Tool production/usage contracts.
  - **Tags** — metadata classification/query semantics.
  - **Scope** — applicability semantics.
  - **Dependencies** — dependency/conformance semantics.
  - **Migration** — transition/checkpoint semantics and Migration Tool.
  - **Review** — independent assessment semantics, profiles and Review Tool.
  - **Messaging integration** — confirmed direction to move AI-MESSAGE ownership into an AIDE
    Messaging capability; authoritative Capabilities Design/Decisions integration is queued in
    `WR16` and is intentionally not pre-empted by this Foundation pass.  
    `{state: "confirmed direction; authoritative integration queued"}`

## Documentation

### Top-level topic and subtopics

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

### Document register — stable/current knowledge

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Capabilities_Index` | v15 | Index | established | Current |
| `Capabilities_Brief` | v7 | Brief | established | Current |
| `Capabilities_Design` | v8 | Design | established | Current |
| `Capabilities_Decisions` | v14 | Decisions | established | Current |
| `Capabilities_Overview` | v13 | Overview | established | Current architecture surface |
| `Capabilities_DocMethReviewItems` | v4 | DocMethReviewItems | custom | Current retained source; no longer active work state |
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

### Live state — load separately

The stable Binder does not carry high-churn live state. Current versions are established from the
available files rather than repeated here.

- `Capabilities_WorkRegister` — confirmed outstanding work; currently includes Messaging `WR16`.
- `Capabilities_OpenItems` — unresolved attention only.
- `Capabilities_Messaging_WIP` — current Messaging continuation checkpoint.

`Capabilities_Binder_Work.md` is no longer the normal consumption route for these registers under
v21; load the current live files directly when working on active state.

### Local configuration

#### Custom document types

| Type | Role | Holds | Lifecycle | Distribution |
|---|---|---|---|---|
| `DocMethReviewItems` | Review input | Consequences/questions for separate DocMeth review | Living until dispositioned | Internal |
| `Standard` | Outcome | Published AI-facing capability rules derived from Capability Design | Living/versioned by capability release | Consuming AI environments |
| `Tool` | Outcome | Published AI-facing invokable capability action derived from Tool Design/Capability Design | Living/versioned by capability release | Consuming AI environments |

Build Config inheritance/defaults remain environment/configuration detail. Generic Deployment
Config belongs to the AI Deployment workstream.

## Current priority

1. Reconcile and publish Messaging as an AIDE Capability (`WR16`).
2. Peer-review the major AIDE architecture slices, including Messaging.
3. Build platform-specific Bootstrap implementations.
4. Build/deploy the platform target system through AIDE Build + AI Deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, Capabilities_Design_v8
References: Capabilities_Overview_v13, Capabilities_Decisions_v14, Capabilities_Messaging_WIP, Capabilities_WorkRegister, Capabilities_OpenItems
