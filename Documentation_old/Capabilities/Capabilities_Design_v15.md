# Capabilities — Design

> **Version 15** (2026-09-03). Closes Review D R1 production checkpoints, WorkPackage mapping, Tag freeze and post-Build boundaries.

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
History, Element Production, Platform Definition, Build Platforms and Build Target Profile
selection/producer overrides. A governed Profile may alternatively own explicit member
selection. Detailed Element meaning stays in the Element's canonical outcome.

## §3 — Design and authorship

Design is knowledge, not a mandatory one-output pipeline. Zero, one or many Design contributions may
apply; contributions and Elements are many-to-many and may be documents or identified sections.
Direct authorship into the correct authoritative owner is valid. Reconcile material conflicts before
production/Build.

## §4 — Update Capability Elements

`AIDE_UpdateCapabilityElementsTool` produces, refreshes or validates canonical Elements where their
documented production model calls for derivation. Directly authored Elements need not invoke it.

Element Production tracks exact source/design contributions and applicable production contracts as
mutable evaluated-input checkpoints using version/revision or digest plus evaluation date/status.
Input change triggers reassessment. Only a confirmed semantic Element change creates the next
Element release.

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
reinterpreted. Calls retaining Build orchestration use the current Tool release; v3 is the Required
migration checkpoint, not a permanent current-call version.

Capability Builder executes the WorkPackage using resolved Build Platforms and the effective Build
Target Profile/Definitions. Internally it may use incremental rebuild/cache/reuse; externally every
applicable required target output is complete. Explicit `NotApplicable`/permitted degradation facts
are producer-owned and carried downstream. Force build may target a subset internally but creates
no Element or Capability release unless semantics changed.

Capability Build explicitly maps Definition/Elements/platform/Profile/source snapshot into
WorkPackage Inputs; required targets/Package into RequiredOutputs; conformance, Tags, force scope
and post-Build request into Constraints; validation into Acceptance; and Package plus separate
post-Build evidence into Return. Generic `AIDE_WorkPackage@v3` remains unchanged.

The current `AIDE_Core` Profile selects the eight peer Capabilities and requires four contribution
targets: `ClaudePlugin`, `ClaudeBundle`, `ChatGPTBundle` and `OpenAIPlugin`. Each contribution carries
the `AIDE_Core` Tag. Repository paths, delivery channels and runtime Targets are not Profile facts.

## §8 — Capability Package and Dependencies

Each Package carries PackageId/integrity, Capability release/composition, effective Profile/
Definition revisions, complete applicable target outputs, source provenance, dependency/migration
material, Build and snapshot-relative Tag evidence. The Registry envelope exposes stable
Logical Package Identity, target/member identity/integrity, Build-owned composition posture,
effective Tags and reach/applicability/conformance/degradation facts needed downstream. Reuse
`AIDE_Dependencies`; production Sources are not semantic Dependencies.

The validated PackageId payload is immutable. Post-Build request/intent and actual Registry
receipt/result are external WorkPackage/Outcome state; neither is written into the validated bytes.

## §9 — Post-Build and AI Deployment seam

After successful validation, invoke the WorkPackage-nominated post-Build Tool. Generic ordinary
publication may use Build's Tool. Registry publication uses `AIDE_DeploymentRegistryTool@v2`.
Independent packages may register directly; all packages in an established coordinated producer
change use the same Open Release Batch.

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

Reviews A–C remain complete at High. Review D R1 is complete and Lead-dispositioned; this pass
implements accepted remediation for Inspect/High/Full R2 verification.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_CapabilityBuild@v4, AIDE_Build@v8, AIDE_WorkPackage@v3, AIDE_Tags@v3
References: Capabilities_Decisions_v21, Capabilities_BuildTargetProfile_Design_v2, Capabilities_AIDECore_BuildTargetProfile_v2, Core_Platform_Design_v1, AIDE_Deployment@v7, AIDE_DeploymentRegistryTool@v2
