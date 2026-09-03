# Capabilities — Overview

> **Version 20** (2026-09-03). Closes exact production checkpoints, Tag freeze ordering and post-Build workflow state.

## Current model

```text
Capability Definition
  ├─ purpose / requirements / dependencies
  ├─ Elements + production checkpoints
  ├─ Element + Capability release history
  ├─ Platform Definition → Build Platforms
  └─ effective Build Target Profile/Definitions

Update Capability Elements
  → semantic change only? release Element

Build Capability
  → map resolved facts + post-Build request into WorkPackage
  → Capability Builder
  → validate generated Tags against exact source snapshot
  → four AIDE_Core contributions per applicable member
  → freeze complete Capability Package + AIDE_Core Tags
  → WorkPackage-nominated post-Build Tool
  → AIDE_DeploymentRegistryTool Register / common Batch when required
  → Deployment Registry
```

Document version, Element release, Capability release, Package/build identity and deployment state
are different facts. A forced rebuild can create a new PackageId without a false semantic release.

## Current status

Review D R1 is complete and Lead-dispositioned. This coordinated pass remediates its accepted
production seams; an Inspect/High/Full R2 should verify the replacement baseline. This Overview is
not the machine navigation surface; use `Capabilities_Index_v24` and the Binder-set index.

---
Dependencies: !AIDE_DocumentationMethodology@v28
References: Capabilities_Design_v15, Capabilities_AIDECore_BuildTargetProfile_v2, Capabilities_WorkRegister_v20, Capabilities_WIP_v20
