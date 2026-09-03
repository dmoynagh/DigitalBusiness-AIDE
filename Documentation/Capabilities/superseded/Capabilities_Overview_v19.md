
# Capabilities — Overview

> **Version 19** (2026-09-02). Adds the closed Build Target/Profile model and AIDE Core four-contribution Profile.

## Current model

```text
Capability Definition
  ├─ purpose / requirements / dependencies
  ├─ Elements + production checkpoints
  ├─ Element + Capability release history
  ├─ Platform Definition → Build Platforms
  ├─ effective Build Target Profile/Definitions
  └─ post-Build intent

Update Capability Elements
  → semantic change only? release Element

Build Capability
  → authorise WorkPackage
  → Capability Builder
  → four AIDE_Core contributions per applicable member
  → complete Capability Package + AIDE_Core Tags
  → nominated post-Build Tool
  → AIDE_DeploymentRegistryTool Register when requested
  → Deployment Registry
```

Document version, Element release, Capability release, Package/build identity and deployment state
are different facts. A forced rebuild can create a new PackageId without a false semantic release.

## Current status

The producer architecture and AI Deployment seam are reconciled. Review D may restart after this
coordinated change package is applied and its baseline is refreshed. This Overview is not the
machine navigation surface; use `Capabilities_Index_v22` and the Binder-set index.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_Design_v14, Capabilities_AIDECore_BuildTargetProfile_v1, Capabilities_WorkRegister_v18, Capabilities_WIP_v18
