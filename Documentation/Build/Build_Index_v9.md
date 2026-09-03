# Build — Index

> **Version 9** (2026-09-03). Registers Build v9 post-Build workflow-state and Registry v2 alignment while retaining WorkPackage v3.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

`{scope: "AIDE/Build", type: DocumentationTopic}`

## Contents

- **Build** — generic objective-driven execution of defined work.  
  `{standard: AIDE_Build@v9}`
- **WorkPackage** — bounded Design-to-Build handoff and Outcome return contract.  
  `{standard: AIDE_WorkPackage@v3}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Build | AIDE | `Build` | independent | expanded |
| WorkPackage | Build | `Build_WorkPackage` | inherits | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Build_Index` | v9 | Index | Current |
| `Build_Design` | v9 | Design | Current |
| `Build_Decisions` | v9 | Decisions | Current |
| `Build_WorkPackage_Design` | v3 | Design | Current |
| `AIDE_Build_Standard` | v9 | Standard | Current; identity `AIDE_Build@v9` |
| `AIDE_WorkPackage_Standard` | v3 | Standard | Current; identity `AIDE_WorkPackage@v3` |
| `Build_PostBuild_Design` | v3 | Design | Current |
| `AIDE_PublishBuildOutput_Tool` | v1 | Tool | Current; identity `AIDE_PublishBuildOutputTool@v1` |

### Binder boundary

`Build_Binder_v9` is the current generated top-level Build Binder; live state is loaded separately.

### Relationships

- Project Design determines committed work and captures undelivered consequences in WorkRegister.
- WorkPackage may select a manageable subset of one or more WorkRegister obligations; deliberately split obligations require independently identifiable required changes and exact `Covers` mapping.
- Build returns Outcome evidence and per-source-obligation result information when mapped.
- The director/owning process reconciles WorkRegister; Build does not silently close it.
- Build remains upstream of AI Deployment for semantic representation/package production; validated Deployable Package registration uses `AIDE_DeploymentRegistryTool@v2` as an explicit post-Build action; its request/result remain workflow state outside immutable package bytes.
- A named Build Target identifies a producer output requirement, not a runtime/install Deployment
  Target; specialised producer contracts own Target Definitions/Profiles.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Index@v1
References: ProjectDesign_Design_v6, AIDE_Deployment@v7, AIDE_DeploymentRegistryTool@v2, AIDE_CapabilityBuild@v4
