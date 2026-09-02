# Project Design — Index

> **Version 5** (2026-09-02). Registers Project Design v5 and the flexible Design contribution/section-host model.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

`{scope: "AIDE/Project Design", type: DocumentationTopic}`

## Contents

- **Project Design** — generic methodology for defining substantial work and reconciling committed
  Design with downstream delivery.  
  `{standard: AIDE_ProjectDesign@v5}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v4 | Index | Current |
| `ProjectDesign_Design` | v5 | Design | Current |
| `ProjectDesign_Decisions` | v4 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v5 | Standard | Current; identity `AIDE_ProjectDesign@v5` |

### Binder boundary

One top-level Project Design Binder; live WorkRegister remains separate.

### Live state

- `ProjectDesign_WorkRegister` — WorkRegister live series; load separately from the stable Binder
  when current outstanding delivery obligations need to be managed.

### Container

Current physical/master folder:

```text
AIDE/Project Design/
```

This folder has always used `Project Design`; earlier references to `AIDE/Design Project/` were
incorrect current documentation/configuration.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Index@v1
References: ProjectDesign_Design_v5, AIDE_ProjectDesign@v5, AIDE_WorkPackage@v3
