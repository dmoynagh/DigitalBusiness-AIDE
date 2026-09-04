# AIDE Capability Build — Standard

> **Identity:** `AIDE_CapabilityBuild@v4`
> **Common name:** Capability Build
> **Version 4** (2026-09-03). Makes the WorkPackage mapping, tag-freeze ordering and post-Build workflow boundary executable.

## Preconditions

- one current Capability Definition;
- released canonical Elements and non-conflicting current inputs;
- resolved Build Platforms with at least one explicit `Build:true`;
- one unambiguous effective Build Target Profile/Definition set;
- applicable generic and Capability-specific platform facts/rules;
- authorised WorkPackage under `AIDE_WorkPackage@v3`; and
- explicit post-Build Tool request or explicit none, carried as WorkPackage workflow authority.

## Capability Build WorkPackage mapping

Map specialised Capability Build facts into the unchanged generic `AIDE_WorkPackage@v3` contract:

- `Inputs` — current Capability Definition, exact released Elements/composition, selected Build
  Platforms, effective Build Target Profile/Definitions and resolved authoritative source snapshot;
- `RequiredOutputs` — every applicable required Build Target output plus one validated complete
  Capability Package;
- `Constraints` — target applicability/reach/conformance/degradation, required Tags, force scope
  (`absent` means no force), and the explicit post-Build Tool request/inputs or explicit none;
- `Acceptance` — target completeness, semantic preservation, freshness, integrity, provenance and
  package-contract validation; and
- `Return` — Package/Build evidence and separate post-Build/Registry receipt state.

The WorkPackage must be self-contained enough that Capability Builder does not reopen upstream
Design or choose unresolved Profile, platform, applicability or workflow policy.

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
- tag-freshness validation tied to the resolved immutable Build source snapshot.

The validated PackageId payload is immutable. Post-Build request/intent and actual Registry
receipt/result are not package content; they remain WorkPackage/Outcome workflow state.

Package format may vary by authorised platform contract. The external completeness/identity contract
does not. Forced/repeated build creates no Element/Capability release unless semantics changed.

## Post-Build

Invoke only the WorkPackage-nominated owner-defined Tool after validation. Registry publication
uses `AIDE_DeploymentRegistryTool@v2`, normally action `Register`, with configured Registry. A
single independent package may register directly. Once a coordinated multi-package change is
established, every participating registration must use the same Open Release Batch; Batch use is
not optional within that coordinated change. Report post-Build failure separately and preserve the
valid immutable Package for safe resumption.

Before Package freeze, run/validate every applicable Tag Builder against the resolved authoritative
Build source snapshot. Freeze the resulting Tags with source-snapshot provenance and compact Build
evidence. Registry, Deployment and runtime consumers use that immutable snapshot-relative Tag
state; they do not regenerate producer-owned Tags to chase newer source state.

```yaml
MigrationSummary:
  CurrentVersion: v4
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

Transition:
  Version: v4
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Build@v8, AIDE_WorkPackage@v3, AIDE_Dependencies@v3, AIDE_Migration@v3, AIDE_Tags@v3
References: Capabilities_CapabilityBuild_Design_v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_CapabilityBuilderTool@v4, AIDE_DeploymentRegistryTool@v2
