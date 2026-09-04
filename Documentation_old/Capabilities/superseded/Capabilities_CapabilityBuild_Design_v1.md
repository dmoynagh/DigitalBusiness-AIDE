
# Capabilities Capability Build — Design

> **Version 1** (2026-09-02). Defines specialised Capability Build, Build Capability orchestration and Capability Builder execution.

## Ownership

Capabilities owns specialised Capability Build semantics. Generic Build/WorkPackage remains the
execution framework. Core supplies generic Working Surface facts.

## Flow

```text
current Capability Definition + released Elements
  → Build Capability Tool (request/readiness/WorkPackage)
  → Capability Builder (Build-side execution)
  → complete Capability Package
  → nominated post-Build Tool
  → AI Deployment seam
```

## Package contract

For every selected `Build:true` platform, the Package exposes a complete logical output area. Build
may be incremental internally. Package metadata includes PackageId/integrity, Capability release and
Element composition, provenance, selected platforms, dependency/migration material required by
downstream consumers, Build evidence and post-Build request/result.

Force build may scope internal work to Capability/platform/Element/portion but never increments a
semantic release unless the semantic release rule was independently met.

## Open seam

The final Registry contract/name, publish/register Tool, Package-to-Registry interface, downstream
metadata and target/configuration mechanics await AI Deployment. This Design does not reinstate the
superseded prior fixed manifest schema.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Build@v6, AIDE_WorkPackage@v3
References: Capabilities_Design_v12
