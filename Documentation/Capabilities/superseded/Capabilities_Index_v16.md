# Capabilities — Index

> **Version 16** (2026-08-31). Registers Messaging as the eighth peer capability,
> Review v2's resolved Messaging dependency, the completed WR16 delivery, and the next peer-Review
> work item while withdrawing the Messaging WIP checkpoint.
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
  - **Messaging** — AI-MESSAGE envelope/schema, message/thread identity, receipt/reconciliation,
    source/provenance, persistence semantics and messaging workflow/Tool.

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
| Messaging | Capabilities | `Capabilities_Messaging` | inherits | expanded |
| Messaging Tool | Messaging | `Capabilities_Messaging_Tool` | inherits | expanded |

WorkPackage belongs under `AIDE/Build/WorkPackage`.

### Document register — stable/current knowledge

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Capabilities_Index` | v16 | Index | established | Current |
| `Capabilities_Brief` | v8 | Brief | established | Current |
| `Capabilities_Design` | v9 | Design | established | Current |
| `Capabilities_Decisions` | v15 | Decisions | established | Current |
| `Capabilities_Overview` | v14 | Overview | established | Current architecture surface |
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
| `Capabilities_Review_Design` | v2 | Design | established | Current |
| `Capabilities_Review_Decisions` | v2 | Decisions | established | Current |
| `AIDE_Review_Standard` | v2 | Standard | custom | Current; identity `AIDE_Review@v2` |
| `AIDE_ReviewProfiles_Standard` | v1 | Standard | custom | Current; identity `AIDE_ReviewProfiles@v1` |
| `Capabilities_Review_Tool_Design` | v2 | Design | established | Current Tool source |
| `AIDE_Review_Tool` | v2 | Tool | custom | Current; identity `AIDE_ReviewTool@v2` |
| `Capabilities_Messaging_Brief` | v1 | Brief | established | Current |
| `Capabilities_Messaging_Design` | v1 | Design | established | Current |
| `Capabilities_Messaging_Decisions` | v1 | Decisions | established | Current |
| `AIDE_Messaging_Standard` | v1 | Standard | custom | Current; identity `AIDE_Messaging@v1` |
| `Capabilities_Messaging_Tool_Design` | v1 | Design | established | Current Tool source |
| `AIDE_Messaging_Tool` | v1 | Tool | custom | Current; identity `AIDE_MessagingTool@v1` |
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

- `Capabilities_WorkRegister` — confirmed outstanding work; currently includes peer architecture Review `WR17`.
- `Capabilities_OpenItems` — unresolved attention only.

The former `Capabilities_Messaging_WIP_v1` has been routed into authoritative Messaging masters and
is withdrawn from active state.

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

1. Peer-review the major AIDE architecture slices, including Messaging (`WR17`).
2. Resolve accepted Review findings into the authoritative/canonical corpus.
3. Build lightweight platform-specific Bootstrap implementations where evidence warrants them.
4. Build/deploy the target-platform system through AIDE Build + AI Deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, Capabilities_Design_v9
References: Capabilities_Overview_v14, Capabilities_Decisions_v15, Capabilities_Messaging_Design_v1, Capabilities_WorkRegister, Capabilities_OpenItems
