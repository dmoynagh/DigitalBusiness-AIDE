# Build — Index

> **Version 4** (2026-08-31). Adopts Core Index and registers WorkRegister-aware WorkPackage
> execution/reconciliation.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

`{scope: "AIDE/Build", type: DocumentationTopic}`

## Contents

- **Build** — generic objective-driven execution of defined work.  
  `{standard: AIDE_Build@v4}`
- **WorkPackage** — bounded Design-to-Build handoff and Outcome return contract.  
  `{standard: AIDE_WorkPackage@v2}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Build | AIDE | `Build` | independent | expanded |
| WorkPackage | Build | `Build_WorkPackage` | inherits | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Build_Index` | v4 | Index | Current |
| `Build_Design` | v4 | Design | Current |
| `Build_Decisions` | v4 | Decisions | Current |
| `Build_WorkPackage_Design` | v2 | Design | Current |
| `AIDE_Build_Standard` | v4 | Standard | Current; identity `AIDE_Build@v4` |
| `AIDE_WorkPackage_Standard` | v2 | Standard | Current; identity `AIDE_WorkPackage@v2` |

### Relationships

- Project Design determines committed work and captures undelivered consequences in WorkRegister.
- WorkPackage may select a manageable subset of one or more WorkRegister obligations.
- Build returns Outcome evidence and per-source-obligation result information when mapped.
- The director/owning process reconciles WorkRegister; Build does not silently close it.
- Build remains upstream of AI Deployment for semantic representation/package production.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: ProjectDesign_Design_v2, AIDE_Deployment@v4
