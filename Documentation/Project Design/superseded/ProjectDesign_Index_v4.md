# Project Design — Index

> **Version 4** (2026-09-01). Pre-Round-2 preflight correction: registers the reissued
> Project Design v4 Design/Standard whose active Build handoff now targets `AIDE_WorkPackage@v3`;
> Review B R1 substantive semantics are unchanged.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Project Design", type: DocumentationTopic}`

## Contents

- **Project Design** — generic methodology for defining substantial work and reconciling committed
  Design with downstream delivery.  
  `{standard: AIDE_ProjectDesign@v4}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v4 | Index | Current |
| `ProjectDesign_Design` | v4 | Design | Current |
| `ProjectDesign_Decisions` | v3 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v4 | Standard | Current; identity `AIDE_ProjectDesign@v4` |

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
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: ProjectDesign_Design_v3, AIDE_ProjectDesign@v3, AIDE_WorkPackage@v2