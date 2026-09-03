# Project Design — Index

> **Version 7** (2026-09-03). Registers the corrected v4/v5 release-lineage explanation; canonical Project Design remains v6.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

`{scope: "AIDE/Project Design", type: DocumentationTopic}`

## Contents

- **Project Design** — generic methodology for defining substantial work and reconciling committed
  Design with downstream delivery.  
  `{standard: AIDE_ProjectDesign@v6}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v7 | Index | Current |
| `ProjectDesign_Design` | v7 | Design | Current |
| `ProjectDesign_Decisions` | v5 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v6 | Standard | Current; identity `AIDE_ProjectDesign@v6` |

### Binder boundary

One top-level Project Design Binder; live WorkRegister remains separate.

### Live state

- `ProjectDesign_WorkRegister` — WorkRegister live series; load separately from the stable Binder
  when current outstanding delivery obligations need to be managed.

### Container

Current repository-relative master folder:

```text
Documentation/Project Design/
```

The active AIDE repository supplies the repository root. Repository-relative placement remains
authoritative if a local checkout path changes.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Index@v2
References: ProjectDesign_Design_v7, AIDE_ProjectDesign@v6, AIDE_WorkPackage@v3
