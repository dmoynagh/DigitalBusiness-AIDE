
# Capabilities — Overview

> **Version 17** (2026-09-02). Human-oriented TLDR of the reconciled Capability architecture.

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
  → AI Deployment seam (pending final registry contract)
```

Document version, Element release, Capability release, Package/build identity and deployment state
are different facts. A forced rebuild can create a new PackageId without a false semantic release.

## Current status

The producer architecture is reconciled. Review D remains on hold pending the active AI Deployment
return handoff and final seam reconciliation. This Overview is not the machine navigation surface;
use `Capabilities_Index_v20` and the Binder-set index.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_Design_v12, Capabilities_WorkRegister_v18, Capabilities_WIP_v18
