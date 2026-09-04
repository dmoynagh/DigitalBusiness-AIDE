
# Capabilities — Overview

> **Version 18** (2026-09-02). Adds the closed Capability Package→Deployment Registry seam and immutable post-Build-result boundary.

## Current model

```text
Capability Definition
  ├─ purpose / requirements / dependencies
  ├─ Elements + production checkpoints
  ├─ Element + Capability release history
  ├─ Platform Definition → Build Platforms
  └─ post-Build intent

Update Capability Elements
  → semantic change only? release Element

Build Capability
  → authorise WorkPackage
  → Capability Builder
  → complete Capability Package
  → nominated post-Build Tool
  → AIDE_DeploymentRegistryTool Register when requested
  → Deployment Registry
```

Document version, Element release, Capability release, Package/build identity and deployment state
are different facts. A forced rebuild can create a new PackageId without a false semantic release.

## Current status

The producer architecture is reconciled. Review D remains on hold pending the active AI Deployment
return handoff and final seam reconciliation. This Overview is not the machine navigation surface;
use `Capabilities_Index_v20` and the Binder-set index.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_Design_v13, Capabilities_WorkRegister_v18, Capabilities_WIP_v18
