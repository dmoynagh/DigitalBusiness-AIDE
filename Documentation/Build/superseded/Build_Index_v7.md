# Build — Index

> **Version 7** (2026-09-02). Reconciles Build post-Build Registry publication to the current AI Deployment Registry Tool.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

`{scope: "AIDE/Build", type: DocumentationTopic}`

## Contents

- **Build** — generic objective-driven execution of defined work.  
  `{standard: AIDE_Build@v6}`
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
| `Build_Index` | v7 | Index | Current |
| `Build_Design` | v7 | Design | Current |
| `Build_Decisions` | v7 | Decisions | Current |
| `Build_WorkPackage_Design` | v3 | Design | Current |
| `AIDE_Build_Standard` | v7 | Standard | Current; identity `AIDE_Build@v7` |
| `AIDE_WorkPackage_Standard` | v3 | Standard | Current; identity `AIDE_WorkPackage@v3` |
| `Build_PostBuild_Design` | v2 | Design | Current |
| `AIDE_PublishBuildOutput_Tool` | v1 | Tool | Current; identity `AIDE_PublishBuildOutputTool@v1` |

### Binder boundary

One top-level Build Binder; live state is loaded separately.

### Relationships

- Project Design determines committed work and captures undelivered consequences in WorkRegister.
- WorkPackage may select a manageable subset of one or more WorkRegister obligations; deliberately split obligations require independently identifiable required changes and exact `Covers` mapping.
- Build returns Outcome evidence and per-source-obligation result information when mapped.
- The director/owning process reconciles WorkRegister; Build does not silently close it.
- Build remains upstream of AI Deployment for semantic representation/package production; validated Deployable Package registration uses `AIDE_DeploymentRegistryTool@v1` as an explicit post-Build action.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Index@v1
References: ProjectDesign_Design_v2, AIDE_Deployment@v5, AIDE_DeploymentRegistryTool@v1
