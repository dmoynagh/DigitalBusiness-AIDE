
# AIDE Capability Build — Standard

> **Identity:** `AIDE_CapabilityBuild@v1`
> **Common name:** Capability Build
> **Version 1** (2026-09-02). First specialised Capability Build and complete Package contract.

## Preconditions

- one current Capability Definition;
- released canonical Elements and non-conflicting current inputs;
- resolved Build Platforms with at least one explicit `Build:true`;
- applicable generic and Capability-specific platform facts/rules;
- authorised WorkPackage under `AIDE_WorkPackage@v3`; and
- explicit post-Build Tool request or explicit none.

## Build rule

Use the Capability Builder under generic `AIDE_Build`. Preserve semantic meaning; do not reopen
Decisions or invent platform eligibility. Internally use full/incremental/cache/reuse strategies as
safe. Externally produce a complete output area for every selected platform.

## Capability Package

The successful Package includes:

- unique PackageId and integrity evidence;
- Capability identity/release and exact Element-release composition;
- source provenance and production/build contract versions;
- resolved selected platforms and one complete logical output area per selected platform;
- dependency and migration material required downstream;
- Build/validation evidence and force-build scope where used; and
- nominated post-Build request/result.

Package format may vary by authorised platform contract. The external completeness/identity contract
does not. Forced/repeated build creates no Element/Capability release unless semantics changed.

## Post-Build

Invoke only the nominated owner-defined Tool after validation. Registry publication requires the
future AI-Deployment-owned contract. Report post-Build failure separately and preserve the valid
Package for safe resumption.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_Build@v6, AIDE_WorkPackage@v3, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_CapabilityBuild_Design_v1, AIDE_CapabilityBuilderTool@v1
