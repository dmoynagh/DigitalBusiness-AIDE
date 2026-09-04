# Capabilities Capability Build — Design

> **Version 4** (2026-09-03). Closes WorkPackage mapping, snapshot-relative Tag freshness and post-Build workflow state.

## Ownership

Capabilities owns specialised Capability Build semantics. Generic Build/WorkPackage remains the
execution framework. Core supplies generic Working Surface facts.

## Flow

```text
current Capability Definition + released Elements
  + effective Build Target Profile/Definitions
  → Build Capability Tool (request/readiness/WorkPackage)
  → Capability Builder (Build-side execution)
  → complete Capability Package
  → nominated post-Build Tool
  → AIDE_DeploymentRegistryTool Register when requested
  → Deployment Registry
```

## Package contract

For every selected `Build:true` platform and every applicable required Build Target Definition, the
Package exposes a complete logical output area/contribution. Build may be incremental internally.
Package metadata includes `PackageKind: CapabilityPackage`, stable Logical Package Identity,
PackageId/integrity, Capability release and Element composition, source/production/Build provenance,
effective Profile/Definition revisions, complete target outputs with resolvable payload/member
identity, Build-owned composition posture, effective Tags, reach/applicability/conformance/
degradation facts, dependency/migration material and Build evidence. Effective Tags are generated
or validated against the exact authoritative Build source snapshot before Package freeze and are
preserved with compact freshness/provenance evidence.

The validated PackageId payload is immutable. Post-Build request/intent and actual Registry
result/receipt are external WorkPackage/Outcome state; neither is written into the package.

## WorkPackage mapping

Capability Build maps current Definition/released Elements, selected platforms, exact source
snapshot and effective Profile/Definitions into `Inputs`; required target outputs plus the complete
Package into `RequiredOutputs`; applicability/conformance/degradation, required Tags, force scope
and post-Build request into `Constraints`; complete target/package validation into `Acceptance`;
and Package evidence plus separate post-Build state into `Return`.

Force build may scope internal work to Capability/platform/Element/portion but never increments a
semantic release unless the semantic release rule was independently met.

## Registry seam

AI Deployment owns the Registry and `AIDE_DeploymentRegistryTool`. The WorkPackage may nominate
`Register` after successful validation with configured Registry. A standalone package may register
directly; an established coordinated multi-package change must use one common Open Release Batch.
No separate capability-only Deployment Manifest is required. Capability Build owns Build Target
production; AI Deployment owns Deployment Set resolution, set-level output assembly, Delivery
Actions, Target Adapters and deployed state.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Build@v8, AIDE_WorkPackage@v3, AIDE_Tags@v3
References: Capabilities_Design_v15, Capabilities_BuildTargetProfile_Design_v2, AIDE_Deployment@v7, AIDE_DeploymentRegistryTool@v2
