
# Capabilities — Design

> **Version 14** (2026-09-02). Closes Build Target Profile/Definition production and the AIDE Core Profile.

## §1 — Scope and peers

Capabilities owns reusable AI-facing Capability semantics and the specialised rules/Tools used to
produce and build them. Current peer capability areas remain Standards, Tools, Tags, Scope,
Dependencies, Migration, Review and Messaging.

Core owns generic Working Surface facts. Generic Build owns WorkPackage/execution/provenance/output
identity. AI Deployment owns its Registry, target/configuration mechanics and deployed state.

## §2 — Capability model

A Capability is a coherent functional component/area. Every Capability has exactly one current
Capability Definition. It composes typed Capability Elements; initial Element Types are Standard and
Tool, and extension requires an actual domain need.

The Definition may host compact Capability-level Purpose/Brief, Requirements, Dependencies, Release
History, Element Production, Platform Definition, Build Platforms, Build Target Profile selection/
producer overrides and post-Build intent. A governed Profile may alternatively own explicit member
selection. Detailed Element meaning stays in the Element's canonical outcome.

## §3 — Design and authorship

Design is knowledge, not a mandatory one-output pipeline. Zero, one or many Design contributions may
apply; contributions and Elements are many-to-many and may be documents or identified sections.
Direct authorship into the correct authoritative owner is valid. Reconcile material conflicts before
production/Build.

## §4 — Update Capability Elements

`AIDE_UpdateCapabilityElementsTool` produces, refreshes or validates canonical Elements where their
documented production model calls for derivation. Directly authored Elements need not invoke it.

Element Production tracks source/design contributions, applicable production contracts and mutable
`LastEvaluated` checkpoints. Input change triggers reassessment. Only a confirmed semantic Element
change creates the next Element release.

## §5 — Release and migration model

Keep distinct document version, Element release, Capability release/composition, Package/build
identity and deployment state. Release History records released state, not general reasoning.

Current Migration is mutable while an Element change is prepared. On successful release it becomes
the immutable migration entry for that Element release and is cleared. `AIDE_Migration` remains the
transition contract.

## §6 — Platform Definition and Build Platforms

Capability Definition records design-owned Platform Definition. Resolve it against current generic
platform facts/profiles into per-platform `Supported` fact and designer-owned tri-state `Build`.
New support never silently enables Build. `Supported:false` plus `Build:true` blocks.

Generic facts stay with Core; Capability-specific build rules stay with Capabilities.

## §7 — Build Target Profiles and Capability Build

Capabilities owns reusable Build Target Profiles/Definitions, `AIDE_CapabilityBuild`, any justified
platform-specific Capability Build Standard, Build Capability orchestration and the Build-side
Capability Builder. A Build Target states what output/contribution must be produced; it is not a
runtime/install Deployment Target. Generic Build remains the framework owner.

`AIDE_BuildCapabilityTool` establishes a Build request and creates/authorises the current
WorkPackage. This is an explicit breaking transition from v2: the former canonical-element
production action moves to `AIDE_UpdateCapabilityElementsTool@v1` and v2 calls are never silently
reinterpreted.

Capability Builder executes the WorkPackage using resolved Build Platforms and the effective Build
Target Profile/Definitions. Internally it may use incremental rebuild/cache/reuse; externally every
applicable required target output is complete. Explicit `NotApplicable`/permitted degradation facts
are producer-owned and carried downstream. Force build may target a subset internally but creates
no Element or Capability release unless semantics changed.

The current `AIDE_Core` Profile selects the eight peer Capabilities and requires four contribution
targets: `ClaudePlugin`, `ClaudeBundle`, `ChatGPTBundle` and `OpenAIPlugin`. Each contribution carries
the `AIDE_Core` Tag. Repository paths, delivery channels and runtime Targets are not Profile facts.

## §8 — Capability Package and Dependencies

Each Package carries PackageId/integrity, Capability release/composition, effective Profile/
Definition revisions, complete applicable target outputs, source provenance, dependency/migration
material, Build evidence and nominated post-Build intent. The Registry envelope exposes stable
Logical Package Identity, target/member identity/integrity, Build-owned composition posture,
effective Tags and reach/applicability/conformance/degradation facts needed downstream. Reuse
`AIDE_Dependencies`; production Sources are not semantic Dependencies.

The validated PackageId payload is immutable. Actual post-Build Registry receipt/result is external state returned through the Registry Tool and WorkPackage Outcome; it is never written back into the validated package bytes.

## §9 — Post-Build and AI Deployment seam

After successful validation, invoke the explicitly nominated post-Build Tool. Generic ordinary publication may use Build's Tool. Registry publication/registration uses `AIDE_DeploymentRegistryTool@v1`, normally `Register`, with the configured Registry and optional open Release Batch.

AI Deployment accepts Capability Package as the first specialised Deployable Package kind. No
separate capability-only Deployment Manifest is required. Registry Current/lifecycle/batch state
and actual post-Build result remain outside the immutable package. AI Deployment resolves
`AIDE_Core` package/member Tags into its exact Set release and owns final Deployment Outputs,
Delivery Actions, Target Adapters and deployed state.

## §10 — Evidence and missing capability behaviour

Capability Build consumes evidence-supported Working Surface facts. Multiple mechanisms may exist
per surface. Unknown is not support. Surface any materially required missing governing capability,
source or surface feature before claiming successful production/build.

## §11 — Review state

Reviews A–C remain complete at High. Review D remains on hold only until this coordinated change is
applied and a fresh baseline is assembled.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v2, AIDE_CapabilityBuild@v3, AIDE_Build@v8, AIDE_WorkPackage@v3
References: Capabilities_Decisions_v19, Capabilities_BuildTargetProfile_Design_v1, Capabilities_AIDECore_BuildTargetProfile_v1, Core_Platform_Design_v1, AIDE_Deployment@v6, AIDE_DeploymentRegistryTool@v1
