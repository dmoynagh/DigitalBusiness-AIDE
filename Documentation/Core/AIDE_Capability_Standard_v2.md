
# AIDE Capability — Standard

> **Identity:** `AIDE_Capability@v2`
> **Common name:** Capability
> **Version 2** (2026-09-02). Adds Build Target Profile selection and producer-owned target overrides.

## Requirements

1. Every Capability has exactly one current Capability Definition.
2. The Definition identifies Capability identity/release, purpose/boundary, Elements/composition,
   Dependencies, Platform Definition, Build Platforms, Element Production, Capability Release
   History, Build Target Profile/override facts and post-Build intent as applicable.
3. Each Element has identity, Element Type, canonical outcome and semantic Element release.
4. Initial Element Types are `Standard` and `Tool`; extension requires owner-defined semantics.
5. Design contributions and Elements may be many-to-many. Direct authoritative authorship is valid.
6. Materially conflicting current contributions block production/Build.
7. Element Production separates immutable release-source snapshots from mutable `LastEvaluated`
   input checkpoints.
8. Input change triggers reassessment; only confirmed semantic change creates an Element release.
9. Capability release changes when composition or substantive Capability-level Definition changes.
10. Document version, Element release, Capability release, PackageId and deployment state remain distinct.
11. Resolve one unambiguous effective Build Target Profile/Definition set before Capability Build.
12. Capability-specific target overrides are delta-only, producer-owned and must expose explicit
    `NotApplicable` or permitted degradation/variation facts rather than silently weakening Profile requirements.

## Migration and Release History

Use `AIDE_Migration`. Maintain Current Migration while preparing an Element change; on release,
convert it to the immutable Element-release migration entry and clear Current Migration. Capability
history may summarise but does not replace Element migration authority.

## Platform Definition, Build Platforms and Build Targets

Resolve generic platform facts into `Supported`; retain designer-owned tri-state `Build`. New
support is surfaced without silent selection. `Supported:false` plus `Build:true` blocks.

```yaml
BuildPlatforms:
  <Platform>:
    Supported: true|false
    Build: true|false|null
    Notes: optional non-semantic context
```

Use `Capabilities_BuildTargetProfile_Design_v1` for deployment-facing Build Target/Profile
semantics. A Profile may be selected by the Definition, its own governed membership, or an
authorised Build request. Build Target Profiles do not own repositories, install destinations,
runtime Targets or deployed state.

## Hosting

Follow Documentation Methodology section-host rules. Multiple permitted hosts never create multiple
editable authorities.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Capability_Design_v2, Capabilities_BuildTargetProfile_Design_v1
