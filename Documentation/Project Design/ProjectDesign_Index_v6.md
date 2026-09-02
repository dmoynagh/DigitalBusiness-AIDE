# Project Design — Index

> **Version 6** (2026-09-02). Registers Project Design v6 and the Design Summary/Overview orientation model.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

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
| `ProjectDesign_Index` | v6 | Index | Current |
| `ProjectDesign_Design` | v6 | Design | Current |
| `ProjectDesign_Decisions` | v5 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v6 | Standard | Current; identity `AIDE_ProjectDesign@v6` |

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
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Index@v2
References: ProjectDesign_Design_v6, AIDE_ProjectDesign@v6, AIDE_WorkPackage@v3
