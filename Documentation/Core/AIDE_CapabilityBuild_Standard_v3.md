
# AIDE Capability Build — Standard

> **Identity:** `AIDE_CapabilityBuild@v3`
> **Common name:** Capability Build
> **Version 3** (2026-09-02). Adds Build Target Profile/Definition resolution and target-complete package output.

## Preconditions

- one current Capability Definition;
- released canonical Elements and non-conflicting current inputs;
- resolved Build Platforms with at least one explicit `Build:true`;
- one unambiguous effective Build Target Profile/Definition set;
- applicable generic and Capability-specific platform facts/rules;
- authorised WorkPackage under `AIDE_WorkPackage@v3`; and
- explicit post-Build Tool request or explicit none.

## Build rule

Use the Capability Builder under generic `AIDE_Build`. Preserve semantic meaning; do not reopen
Decisions or invent platform eligibility. Internally use full/incremental/cache/reuse strategies as
safe. Externally produce a complete output area for every selected platform and applicable required
Build Target Definition. `NotApplicable` and permitted degradation/variation require explicit
producer-owned facts; do not treat a missing applicable output as degradation.

## Capability Package

The successful Package is `PackageKind: CapabilityPackage` and includes:

- stable Logical Package Identity plus unique PackageId and integrity evidence;
- Capability identity/release and exact Element-release composition;
- source/canonical provenance and production/Build contract versions;
- resolved selected platforms and one complete logical output area per selected platform, with payload/member identity sufficient to resolve each built output;
- effective Build Target Profile/Definition identity and revision;
- one complete output/contribution for every applicable required target;
- Build Target identity, reach/applicability/conformance/degradation facts and effective Tags for each output;
- Build-owned `CompositionPosture` for deployment-facing outputs where applicable;
- dependency and Migration material required downstream;
- Build/validation evidence and force-build scope where used;
- package-level and built-target/member-level `AIDE_Tags` where configured;
- producer-declared surface support/conformance/variation/degradation information where applicable;
- namespaced owner-specific extension metadata needed downstream; and
- nominated post-Build request/intent.

The validated PackageId payload is immutable. Actual post-Build Registry receipt/result is not package content; report it separately through Registry state and WorkPackage Outcome.

Package format may vary by authorised platform contract. The external completeness/identity contract
does not. Forced/repeated build creates no Element/Capability release unless semantics changed.

## Post-Build

Invoke only the nominated owner-defined Tool after validation. Registry publication uses `AIDE_DeploymentRegistryTool@v1`, normally action `Register`, with configured Registry and optional open Release Batch. Report post-Build failure separately and preserve the valid immutable Package for safe resumption.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v2, AIDE_Build@v8, AIDE_WorkPackage@v3, AIDE_Dependencies@v3, AIDE_Migration@v2, AIDE_Tags@v2
References: Capabilities_CapabilityBuild_Design_v3, Capabilities_BuildTargetProfile_Design_v1, AIDE_CapabilityBuilderTool@v3, AIDE_DeploymentRegistryTool@v1
