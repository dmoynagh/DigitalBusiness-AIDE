# AI Deployment Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 7** (2026-09-03). Review D R1 remediation: fixed Set membership, required-presence preservation, frozen Tags, Registry v2 and target-relative satisfaction.

This Binder is a current-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `AIDeployment_Index_v7.md` — sha256 `ce020032ec38`
- `AIDeployment_Design_v7.md` — sha256 `bf3b9df89b3e`
- `AIDeployment_Decisions_v7.md` — sha256 `07f77cfeaa9d`
- `AIDeployment_Registry_Design_v2.md` — sha256 `583e1bfcac0a`
- `AIDeployment_SetRelease_Design_v2.md` — sha256 `e4ce359c712d`
- `AIDeployment_TargetAdapter_Design_v1.md` — sha256 `97e17c86f680`
- `AIDeployment_AIDECore_Reference_v2.md` — sha256 `79f0b445325a`
- `AIDeployment_OpenAI_Reference_v3.md` — sha256 `1b895fbe156d`
- `AIDE_Deployment_Standard_v7.md` — sha256 `6c8f9c248be0`
- `AIDE_Deployment_Tool_v7.md` — sha256 `99279f845278`
- `AIDE_DeploymentRegistry_Tool_v2.md` — sha256 `b3903fa3c162`

---

<!-- BEGIN SOURCE: AIDeployment_Index_v7.md -->
# AI Deployment — Index

> **Version 7** (2026-09-03). Registers Review D R1 remediation and the new AIDE documentation repository path.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

## Project identity

**Topic/workstream:** AI Deployment  
**Repository:** `DigitalBusiness-AIDE`  
**Project container / master folder:** `Documentation/AI Deployment/`  
**Purpose:** Generic Registry-backed, set-aware, policy-aware deployment of validated built artefacts into AI runtime surfaces.

## Contents

- **AI Deployment** — desired-state selection, target reconciliation/delivery and runtime verification.  
  `{standard: AIDE_Deployment@v7}`
- **Deployment Registry** — validated Deployable Package registration, immutable package-instance lifecycle and Release Batches.  
  `{tool: AIDE_DeploymentRegistryTool@v2}`
- **Set Release** — exact resolution, immutable `<Set>@vN` releases and final Deployment Outputs.
- **Target Adapter** — Delivery Actions, platform/channel mechanics, layered verification and per-Target state.
- **AIDE Core Deployment** — concrete `AIDE_Core` Set/output/action/Target reference configuration.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v7 | Index | Current |
| `AIDeployment_Design` | v7 | Design | Current |
| `AIDeployment_Decisions` | v7 | Decisions | Current |
| `AIDeployment_Registry_Design` | v2 | Design | Current |
| `AIDeployment_SetRelease_Design` | v2 | Design | Current |
| `AIDeployment_TargetAdapter_Design` | v1 | Design | Current |
| `AIDeployment_AIDECore_Reference` | v2 | Reference/configuration | Current |
| `AIDeployment_OpenAI_Reference` | v3 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v7 | Standard | Current; identity `AIDE_Deployment@v7` |
| `AIDE_Deployment_Tool` | v7 | Tool | Current; identity `AIDE_DeploymentTool@v7` |
| `AIDE_DeploymentRegistry_Tool` | v2 | Tool | Current; identity `AIDE_DeploymentRegistryTool@v2` |

## Binder boundary

`AIDeployment_Binder_v7` is the current generated top-level consumption Binder. Live state remains
separate.

## Current boundary

Producer/domain owns deployable artefact semantics and PackageKind-specific Build/package content. Build/specialised producer Build produces validated packages and supplies source/build provenance, concrete PackageId/integrity and Build-owned composition posture.

AI Deployment owns the **Deployment Registry** contract and lifecycle. `Deployable Package` is the generic Registry unit; `Capability Package` is the first specialised kind. Registered PackageIds are immutable; Current/Available/Deprecated/Withdrawn/Release Batch state is Registry-owned metadata.

Deployment Set membership does not erase upstream required presence. Deployment may mechanically assemble eligible `MemberContribution` outputs, treats an `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary, and owns policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Environment/platform configuration remains the source of physical Registry/Target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

## Current design status

The generic design required for the confirmed AIDE Core outcome is closed: fixed desired membership
resolves through eligible Registry supply into one immutable `AIDE_Core@vN`, four final Outputs, configured Delivery
Actions, independently reconcilable Targets and layered runtime verification. Remaining provider
uncertainties are empirical adapter facts, not missing generic architecture.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7, AIDE_Build@v8
References: AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v2, AIDE_DeploymentRegistryTool@v2, AIDE_CapabilityBuild@v4, AIDE_Dependencies@v3, AIDE_Tags@v3
<!-- END SOURCE: AIDeployment_Index_v7.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Design_v7.md -->
# AI Deployment — Design

> **Version 7** (2026-09-03). Closes Set membership authority, Target-relative required presence and frozen-Tag consumption.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

---

## Layer 1 — intent / system view

### Purpose

Make built deployable material available in the intended AI runtime surfaces, reconcile changes/removals and required-presence mismatches, and verify the **actual usable deployed state**.

### Premises

- Deployment starts after producer-specific design and successful validated Build.
- Deployment consumes validated **Deployable Packages** from the Deployment Registry; it does not reopen the producer's Design or perform a second semantic Build.
- `Capability Package` is the first specialised Deployable Package kind; other package kinds may be added later without changing generic Registry/Deployment semantics.
- Observed deployed state and older Bundles/packages are reconciliation evidence, not substitute semantic production sources.
- A Deployment Set states desired target composition; it does not redefine semantic requirements declared by its members or their dependencies.
- A shared representation does not imply a shared distribution route or runtime.
- Logical target, runtime surface, representation, distribution channel, physical destination, source locator, target-change policy and observed deployment state are separate facts.
- Possessing access credentials or knowing where material can be found does not by itself authorise target mutation.
- Deployment verification means runtime-appropriate evidence, not merely “the file/install exists.”

### Boundary

Producer/domain owns the logical artefact, its semantic requirements and any producer-specific package contract.

Dependencies owns dependency/required-presence semantics. Deployment consumes those facts when they materially affect target validity; it does not redefine them through Deployment Set membership.

Build owns semantic rendering/transformation from current authoritative/canonical sources into concrete Build outputs/packages. The Build output contract supplies authoritative/canonical source identity/version provenance, concrete Build-output/package identity and integrity evidence, and a Build-owned `CompositionPosture` of `MemberContribution` or `AssembledConsumptionArtefact`. Specialised producer Build may define a richer package contract such as `AIDE_CapabilityBuild`.

AI Deployment owns the **Deployment Registry** contract and Registry lifecycle, desired Set selection, set-aware **mechanical target assembly** of already built material where a Target requires it, destination/channel resolution, policy-aware publication/install/update/remove, resumption, mismatch reporting and verification. It consumes rather than invents Build composition posture: `MemberContribution` may participate in Deployment-owned mechanical assembly; `AssembledConsumptionArtefact` is atomic at its semantic/member-composition boundary and must be replaced by another Build output when that internal composition changes. Deployment does not independently render canonical semantics into a new target representation.

Environment/platform configuration supplies physical target facts, access and channel details, and the effective policy/authority under which the target may be changed.

Bootstrap may discover startup material and surface missing required presence. It does not install, update, remove, reconcile or verify deployed state.

### Flow

```text
producer canonical outcome(s)
      ↓
Build / specialised producer Build
      ↓
validated Deployable Package
      + PackageId / integrity / source-build provenance
      + deployment-facing built outputs and CompositionPosture
      + owner-specific dependency / Migration / extension metadata
      ↓
AIDE_DeploymentRegistryTool
      ↓
Deployment Registry
      ↓
Registry event / manual invocation
      ↓
resolve Deployment Set + target config/policy
      ↓
resolve semantic required-presence facts
      ↓
assemble/validate candidate Deployment Outputs
      ↓
changed exact resolution? issue immutable Set@vN
      ↓
execute configured Delivery Actions through Target Adapters
      ↓
publish/install/update/remove/refresh
      ↓
verify actual target/runtime state
      ↓
Deployment Result + Deployment State
```

---

## Layer 2 — model


### Deployable Package

A **Deployable Package** is the generic validated Build package accepted into the Deployment Registry as deployment supply. `Capability Package` is the first specialised Package kind.

Keep stable Logical Package Identity separate from concrete `PackageId`. A new Build can create another PackageId for the same logical package without implying a new semantic release. Package instances are immutable after successful registration; Registry lifecycle/current state is maintained separately.

The package contract exposes enough producer-owned information to identify the exact built result and use it without semantic inference, including integrity/provenance, deployment-facing outputs, Build-owned composition posture, and owner-specific dependency/Migration/extension information where applicable.

### Deployment Registry

The **Deployment Registry** is the authoritative source of validated built supply available to AI Deployment. Its physical implementation may be a folder, Git repository, package store, service or another configured mechanism.

The Registry owns:

- package registration/acceptance state;
- Logical Package Identity → Current Package relation;
- `Available | Deprecated | Withdrawn` lifecycle state;
- Release Batch staging/release state; and
- semantic Registry events used by configured Deployment Triggers.

The Registry does not mutate package bytes to represent lifecycle state and does not itself deploy anything to runtime targets. Detailed contract: `AIDeployment_Registry_Design_v2`.

### Release Batch

A **Release Batch** groups package registrations/lifecycle changes that must become visible to automatic downstream resolution together. Packages may be validated/staged while the Batch is Open; explicit Release makes the staged Registry changes visible together and emits one release event.

This is an atomic **Registry visibility** boundary, not a promise of atomic deployment across heterogeneous runtime Targets.

### Deployment Trigger

A **Deployment Trigger** maps Registry changes or explicit/manual invocation to re-evaluation of one or more Deployment Set Definitions. A trigger means the desired concrete Set may have changed; it does not require blind re-delivery. If resolution is unchanged, no target action is needed.

### Deployment Set

A named logical **desired composition**. It groups the producer members that should be realised together for one or more configured targets.

For fixed composition, the Set Definition owns an explicit required/desired member list and a
separate supply selector resolves eligible Registry packages for those members. A missing package
blocks the candidate; selector results never silently redefine membership. A genuinely dynamic Set
may declare selector-defined variable membership, but must do so explicitly.

The Set is semantic/logical. It does not itself mean plugin, bundle, repository, account or path.

Set membership is not the owner of a member's semantic dependencies or required-presence rules. Omitting a required dependency from a Set does not make that dependency optional. A Set is therefore not a replacement dependency graph or an automatic dependency-closure mechanism.

### Deployment Set Release

An immutable exact resolved Set result identified as `<Set>@vN`. It records the Set Definition
revision, exact PackageIds/build outputs/integrity, Output Definition revisions, final Output
identities/integrity and a resolution digest. The Set's mutable `DesiredRelease` pointer identifies
the release intended for Targets without claiming those Targets are already current.

There is no generic downstream Deployment Package. `Deployable Package` remains Registry supply;
`Deployment Output` is the final set-level consumable representation.

### Deployment Output

One final representation assembled under a Deployment Output Definition from compatible built
inputs. Required Outputs are validated together before a Set release is issued. Every Output carries
an intrinsic runtime-visible Set release marker and resolution digest. A generated plugin status
member may expose that provenance without becoming another Capability.

### Deployment Target

One concrete runtime/surface realisation of a Deployment Set. A Target resolves at least:

- platform/family;
- runtime/surface;
- representation;
- distribution channel;
- physical destination/account/workspace where applicable;
- effective target-change policy/authority;
- refresh/session-pickup behaviour where relevant; and
- verification requirements.

One logical Deployment Set may therefore have several Targets even inside one provider family.

One Deployment Output may feed several Targets. For example, one Claude plugin output may reconcile
independently to Claude account and Claude Code installation/runtime Targets.

### Delivery Action and Target Adapter

A **Delivery Action** is an idempotent configured operation that moves one or more Outputs toward
one or more Targets. A **Target Adapter** supplies the platform/channel-specific publish, install,
update, remove, pickup and verification mechanics behind the Target. Neither owns semantic content
or forms part of the immutable Set release.

### Representation

The target-compatible shape being deployed, for example a plugin, skill collection, project bundle, instruction file or another supported platform artefact.

### Build output composition posture

Build supplies one composition posture for each deployment-facing Build output:

- `MemberContribution` — a built target-compatible member/contribution that downstream Deployment may mechanically assemble with other built outputs where the Target representation requires it.
- `AssembledConsumptionArtefact` — a Build output whose semantic/member composition is already the authorised Build result. Deployment may place, publish, wrap or otherwise handle it mechanically as an atomic built input, but changing its internal semantic/member composition requires another Build output.

Composition posture is a Build-owned interface fact. Deployment consumes it and does not infer or override it from payload shape, filename, representation name or observed deployed state.

### Distribution channel

How that representation reaches the target: local marketplace, hosted directory/publication, project-file upload/sync, repository, account/workspace install, filesystem path, human-assisted replacement, or another supported route.

Representation and channel are independent dimensions. A manual channel does not create different deployment semantics from an automated channel.

### Deployment Policy

The effective environment/target rule that determines whether and under what conditions the deployment process may mutate a Target.

It may cover, as applicable:

- whether changes may be applied automatically;
- whether user/operator confirmation or external execution is required;
- constraints on install/update/remove actions; and
- whether future acquisition from a configured source/catalog is permitted.

AI Deployment defines how policy gates deployment behaviour. Environment/platform configuration owns the actual policy values and authority context.

Deployment Policy is not a new Core role. It is also distinct from credentials/access, a source locator, trust in a source, semantic requirement and the requested deployment action.

### Deployment Config

Resolves a Deployment Set to its Targets and physical mechanics. Config is environment data, not producer design intent.

Conceptual shape:

```yaml
DeploymentSets:
  <set-name>:
    Targets:
      - Platform: <family>
        Surface: <runtime/surface>
        Representation: <shape>
        Channel: <distribution route>
        Destination: <logical/physical destination reference>
        Policy: <target-change policy/authority reference or resolved policy>
        Refresh: <where required>
        Verification: <required checks/probes>
```

Credentials/secrets are referenced through environment access mechanisms and are not embedded in a producer package/manifest or normal governed documentation. Access enables mechanics; it does not substitute for target-change policy.

### Deployment State

A mutable factual record of what has actually been observed/verified for one Target. It distinguishes:

- desired Set Release/output/integrity;
- publication release/evidence where applicable;
- platform-installed/attached release/evidence where applicable;
- runtime-observed release, content availability and session pickup where applicable;
- selected/installed Build-output or package identity, integrity relation and composition posture where exposed;
- member/capability identities and releases where exposed;
- representation/channel/surface;
- required-presence mismatches or blockers relevant to the Target;
- verification `Verified | Mismatch | Unverified`, evidence time and assurance
  `Enforced | Advisory`;
- runtime content availability; and
- session pickup state where the platform pins active sessions to an older build.

Installed state and active-session state may differ.

### Deployment Result

One reconciliation invocation result, not persistent state. Overall status is `Complete | Partial |
Blocked | Failed`, with per-Target action/result and resulting State. `Blocked` means a known
authority/prerequisite/manual/material condition prevented progress; `Failed` means an attempted
operation or validation failed.

---

## Major rules

### 1. Reconcile desired state rather than model separate semantic install/update/remove systems

The Deployment Set expresses what should exist. Deployment calculates target actions required to move verified target state toward that desired composition.

`Install`, `Update`, `Replace` and `Remove` are operational consequences of reconciliation, not four unrelated lifecycle models.

This removes the full-vs-incremental question from generic deployment semantics: a target adapter/assembler may mechanically rebuild the target assembly from the selected built inputs or patch it incrementally, provided it does not semantically re-render those inputs and the same desired state, provenance relation and verification result are produced.

### 2. Build production is upstream; Deployment is set-aware

Build produces deployment-facing outputs from current authoritative/canonical semantic sources and declares each output's `CompositionPosture`. A `MemberContribution` need not be independently deployable. An `AssembledConsumptionArtefact` is already the authorised Build result for its internal semantic/member composition.

Deployment selects the appropriate built outputs for the Deployment Set and Target. Where the Target representation requires set-level assembly, Deployment may combine `MemberContribution` outputs mechanically—for example by deterministic placement, concatenation, registration, wrapping or other representation-defined assembly that does not interpret or recreate their semantic meaning. An `AssembledConsumptionArtefact` may participate only as an atomic built input; Deployment does not decompose it or change its internal semantic/member composition.

If the required target-compatible semantic transformation or required replacement `AssembledConsumptionArtefact` is absent from the supplied Build outputs, Deployment reports a Build/material blocker rather than deriving the missing representation from Design history, canonical source text, an older Bundle/package or observed deployed content.

### 3. Deployment-time composition is deterministic mechanical assembly and conflicts fail visibly

For each Target, Deployment resolves all desired Build outputs together with their source/build provenance, identity/integrity and Build-declared composition posture. Where necessary, it mechanically assembles eligible `MemberContribution` outputs according to the target representation contract while treating each `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary. Assembly preserves semantics, provenance and member-level dependency/Migration/Scope/Tags or deterministic references to those facts; it does not create a new semantic rendering authority in Deployment or erase information needed downstream.

If built outputs claim incompatible ownership/identity/path/namespace, have incompatible composition postures for the required Target operation, or cannot coexist under the target representation, assembly fails for that Target. Deployment does not choose a winner silently, reinterpret posture or repair the conflict by rewriting member semantics.

### 4. No universal cross-target atomicity

Heterogeneous AI platforms do not provide a common transaction boundary. Generic Deployment therefore does not claim all-or-nothing atomicity across Targets.

The safe default is:

- validate/mechanically assemble before publication where possible;
- preserve previously verified state when failure occurs before target mutation;
- record each Target independently;
- stop dependent target actions when their prerequisites fail; and
- use platform rollback only when the target contract actually supports it.

A partially completed multi-target deployment returns `Partial`, never false `Complete`.

### 5. Resumption is target-state reconciliation

Re-running the same desired Set is idempotent where the target mechanics allow it. Already verified matching Targets require no semantic redeployment. Failed/unverified Targets are retried from the observed state.

A new Build output/package of the same semantic release can still require deployment because canonical/source identity, Build-output/package identity, composition posture and runtime pickup are separate facts. Deployment status never substitutes for those upstream Build facts.

### 6. Verification is layered and surface-specific

A Target is `Verified` only after the checks required by that Target have passed. Possible checks include:

1. package/artefact integrity;
2. destination publication/install acknowledgement;
3. directory/discovery visibility;
4. package/build version visibility;
5. member/capability identity visibility;
6. required dependency/presence checks relevant to target use;
7. MigrationSummary/cheap metadata visibility where expected;
8. runtime content probe;
9. implicit/explicit trigger behaviour where applicable; and
10. update/session pickup behaviour where the runtime may pin an old build.

UI presence or “enabled” state is not sufficient where executable runtime content is required.

### 7. Removal follows desired composition

When a member is no longer desired in a Set, Deployment removes it from the target composition. For `MemberContribution` outputs under Deployment-owned mechanical assembly, this may mean reassembling without that member. If the member is part of the internal semantic/member composition of an `AssembledConsumptionArtefact`, Deployment requires the appropriate replacement Build output rather than decomposing or semantically rebuilding it. Where the member is independently installed, removal may mean uninstall/removal.

Explicit producer `Remove`/`Replace` intent remains useful for identity transitions and retirement, but the stable semantic goal is the resulting desired Set.

### 8. Semantic requirements survive Deployment Set omission

The immutable Set release preserves required-presence facts that apply to desired members under the
owning dependency semantics. Before declaring a Target valid, Target reconciliation evaluates those
facts against that Target's observed state. Valid material already present outside Set membership
may satisfy a requirement; Set resolution does not claim Target-independent satisfaction.

If required material is already available in the Target outside the Set, the requirement may be satisfied without adding it to Set membership. If required material is absent, Deployment reports a target reconciliation mismatch/blocker.

Deployment does not erase the requirement, silently reinterpret it as optional, or silently expand Set membership to hide the defect.

### 9. Mutation is policy-gated

Deployment may calculate and report reconciliation actions without permission to perform them.

Before mutating a Target, it must resolve the effective Deployment Policy/authority. If policy does not permit the action, the Target remains mismatched and the result surfaces the blocked/manual/confirmation action required.

Credentials, filesystem access or a reachable API are evidence of technical capability, not sufficient evidence of policy permission.

### 10. Source, trust, permission and action remain separate

A locator answers where material may be resolved. Trust answers whether that source/material is acceptable. Deployment Policy answers whether acquisition or target mutation is permitted. Reconciliation determines what action would move the Target toward valid state.

Naming a source or exposing `WHERE` information does not imply permission to fetch, install or execute it.

### 11. Acquisition is an explicit future seam, not current Bootstrap behaviour

Current Deployment may require built/package material to be supplied or otherwise already resolvable through established environment mechanics. Absence of required deployable material is reported rather than triggering an implicit fetch.

The model permits a later acquisition step such as:

```text
required material missing
      ↓
resolve trusted source/catalog
      ↓
check Deployment Policy
      ↓
obtain package/material
      ↓
reconcile Target
      ↓
verify resulting state
```

That future mechanism must preserve source/trust/policy separation and does not move acquisition or installation into Bootstrap.

### 12. Deployable artefact kind does not change ownership

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other canonical/deployable artefacts may participate as Deployment Set members when Build provides the target-compatible Build output required by the Target and declares its composition posture. Deployment places/assembles those built forms according to that posture without collapsing their distinct semantic roles or inferring missing Bootstrap meaning.

Their deployment is then ordinary AI Deployment work. A Bootstrap artefact being deployed does not make Bootstrap the deployment owner.

### 13. Manual Bundle replacement is an implementation, not an architectural special case

The present ChatGPT project workflow can be modelled as:

```text
Representation: common Standards/Tools Bundle
Channel: manual project-file replacement/upload
Target: configured ChatGPT project context
Verification: project/runtime-appropriate presence/content checks
```

This remains a valid Target implementation while platform automation is unavailable. A future automated sync/install route may replace the manual channel without changing Deployment Set or reconciliation semantics.


### 14. Registry package instances are immutable; lifecycle is Registry state

A successfully registered `PackageId` identifies one concrete validated package instance. The Registry never rewrites that package to make it current, deprecated or withdrawn. A later Build produces a new PackageId; mutable Current/lifecycle state is stored separately.

`Deprecated` leaves the package available but discouraged. `Withdrawn` removes it from ordinary new/current resolution while retaining it for history/evidence and explicitly authorised recovery. Physical purge is separate retention maintenance and is not automatic in v1.

### 15. Coordinated publication uses explicit Release Batches

When several packages form one coordinated producer change, register them into one Open Release Batch and release them together. Do not infer completion solely from timing or package count. Batch release can validate an expected package list, changes Registry visibility together and triggers downstream re-evaluation once.

### 16. Package and built-output Tags are selectors, not semantic requirements

Deployment may use `AIDE_Tags` on the Package and individual built target/member outputs. Effective target/member selection tags are the union of Package and target/member tags. Tags may select/group supply but do not replace Dependencies, Scope, compatibility, Migration posture or Deployment Policy.

Registry/Deployment consumes the immutable snapshot-relative Tags and producer freshness evidence
frozen by Build. It does not run producer-owned Tag Builders against later source state.

### 17. Issue Set releases only after all required Outputs validate

Calculate a candidate without consuming a version number. If all required members and Outputs are
present, mechanically assembled and valid, freeze the next `<Set>@vN` and advance DesiredRelease.
Otherwise retain the last issued Desired Release and report the candidate blocker/failure.

A different exact PackageId/build output can change the resolved Set even when Capability semantic
releases are unchanged. Destination, credentials, adapter/policy or verification-state changes do
not alone change Set content.

### 18. Automatic no-op and explicit retry are different

An automatic Registry event with unchanged exact resolution creates no release and performs no
delivery retry. Explicit/manual Reconcile may retry or re-verify incomplete Targets of the existing
Desired Release. Target/environment configuration changes reconcile that same release unless output
content changes.

### 19. Verification is output/publication/platform/runtime layered

Use the layers exposed by a Target. Installation/attachment proves platform state, not runtime use.
Runtime verification checks the intrinsic release marker and, where behaviour matters, a suitable
capability probe. Record whether evidence is Enforced outside model choice or Advisory because it
depends materially on model execution/reporting.

### 20. AIDE Core is the initial complete configuration

`AIDE_Core` is intentionally reused as Build Target Profile, Registry/member Tag and Deployment Set
identity, with each role remaining distinct. The Set resolves four Outputs—Claude plugin, Claude
bundle, ChatGPT bundle and OpenAI plugin—under one immutable `AIDE_Core@vN` release. Concrete
outputs/actions/Targets are defined in `AIDeployment_AIDECore_Reference_v2`.

---

## Ownership and project-container boundary

AI Deployment is no longer owned by Capabilities. Its dedicated master folder/GPT Project is
`AIDE/AI Deployment/`.

Architecturally it remains an environment/platform concern: it consumes target configuration,
credentials/access references, target-change policy, surface/channel facts and observed runtime state. The dedicated
project container is an operational context boundary, not evidence that deployment semantics
belong to Capabilities or to a producer domain.

Capabilities retains capability-specific production and PackageKind semantics. Post-Build request
is WorkPackage/Outcome workflow state, not package semantics. AI Deployment owns Deployment Set
selection/composition semantics.

## Producer-package compatibility

The current `AIDE_CapabilityBuild@v4` Capability Package is the first producer-specific `Deployable Package`. AI Deployment does not require Capabilities to re-open semantic Design or maintain a separate capability-only Deployment Manifest.

The package must expose the generic Registry acceptance envelope plus its Capability-specific
composition, dependency/Migration/Scope/Tags and Build evidence. Post-Build request and result are
not immutable package content; the WorkPackage supplies the request and Registry/Outcome returns
the result separately.

Where later package kinds need owner-specific metadata, use preserved/typed extension information rather than teaching generic Deployment the producer's semantics.

## Closed generic layer

Set Definitions/exact releases, Outputs, Delivery Actions, Target Adapters, State/Result and trigger
behaviour are now closed. Build Target Profiles/Definitions and surface/degradation production
remain upstream producer concerns; Deployment consumes their registered built results.

Detailed contracts: `AIDeployment_SetRelease_Design_v1` and
`AIDeployment_TargetAdapter_Design_v1`.

## Open empirical items — not architecture blockers

- exact supported ChatGPT reach of the OpenAI plugin in the configured account/workspace;
- which Claude installation currently governs the Desktop Code-tab runtime;
- broader provider adapter mechanics not yet tested;
- exact platform-specific composition rules for multi-member artefacts;
- platform-specific refresh/session pickup mechanics not yet observed;
- general trusted package/catalog acquisition infrastructure and its concrete source-trust model.

These populate target adapters/config or future acquisition support; they do not change the generic model unless evidence exposes a missing concept.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Build@v8, AIDE_Dependencies@v3, AIDE_Tags@v3
References: AIDE_WorkPackage@v3, AIDE_CapabilityBuild@v4, AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v2, AIDE_DeploymentRegistryTool@v2, AIDeployment_OpenAI_Reference_v3
<!-- END SOURCE: AIDeployment_Design_v7.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Decisions_v7.md -->
# AI Deployment — Decisions

> **Version 7** (2026-09-03). Records Review D R1 Set membership, required-presence, Tag and workflow remediation.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

---

## D1 — Target runtime/surface is separate from representation and channel

**Decision/recommendation.** Model runtime/surface, representation and distribution channel as distinct target facts.

**Reason.** OpenAI evidence demonstrated that the same local plugin representation was a valid Codex deployment, visible-but-not-executable in ChatGPT desktop Chat, and absent from ChatGPT web. Shared package shape did not imply shared deployment/runtime availability.

## D2 — Deployment Set is desired composition

**Decision/recommendation.** Treat a Deployment Set as a named desired composition rather than an append-only sequence of install/update/remove operations.

**Reason.** This collapses set lifecycle, replacement/removal and full-vs-incremental assembly into one reconciliation problem. Platform mechanics may rebuild or patch without changing semantics.

## D3 — Deployment Target is the unit of publication and verification

**Decision/recommendation.** One Set resolves to one or more Targets; each Target has its own surface, representation, channel, destination, refresh and verification contract.

**Reason.** Even a single provider family can require different routes for different surfaces.

## D4 — No generic cross-target transaction guarantee

**Decision/recommendation.** Do not claim universal atomic deployment/rollback across heterogeneous targets. Record per-target success and return Partial when the overall requested state is incomplete.

**Reason.** A generic transaction promise would be fictional on platforms that expose no rollback/transaction mechanism. Pre-publication validation and platform-specific rollback provide stronger truthful safety.

## D5 — Runtime verification is required where runtime use is the goal

**Decision/recommendation.** UI/install state is insufficient. Target verification includes a runtime content/use probe wherever the deployed object is meant to affect runtime behaviour.

**Reason.** ChatGPT desktop showed an installed/enabled plugin and updated package version while Chat runtime still could not access the skill body.

## D6 — Session state may differ from installed target state

**Decision/recommendation.** Record session pickup separately where a platform pins an active session to an older build.

**Reason.** Codex evidence showed an existing session remained on the old cache after reinstall while a new session used the updated build.

## D7 — Deployment is promoted out of Capabilities

**Decision.** Generic deployment is owned by the AI Deployment workstream, not by Capabilities.
Capabilities remains a producer of capability packages and logical deployment intent.

**Reason.** Deployment's intrinsic concerns are surface, representation, distribution channel,
destination/configuration, composition and verified runtime state. Those concerns apply to
deployable artefacts beyond capabilities.

## D8 — Dedicated project container does not collapse conceptual ownership

**Decision.** `AIDE/AI Deployment/` is the master folder and GPT Project for this workstream.
This is an operational context/container boundary. It does not make producer semantics part of
Deployment and does not require all environment concerns to share one GPT Project.

**Reason.** Project-context boundaries should optimise coherent working context; conceptual
ownership remains explicit in the design.

## D9 — Deployment Set membership does not redefine semantic requirements

**Decision.** A Deployment Set states desired composition only. Dependency/required-presence semantics remain owned by the producing artefact and `AIDE_Dependencies`.

**Reason.** Otherwise omission from a Set could silently convert an upstream requirement into an optional deployment choice. That would make deployment configuration an accidental semantic authority and hide configuration defects.

**Consequence.** Deployment checks applicable required presence against observed target state. A required item may be satisfied outside Set membership if it is actually available; if it is absent, the Target has a visible reconciliation mismatch/blocker.

## D10 — Use Deployment Policy rather than a Core Deployment Authority role

**Decision.** Add a target/environment **Deployment Policy** concept governing whether and under what conditions Deployment may mutate a Target. Do not add a generic Core `Deployment Authority` role.

**Reason.** Permission to modify a host belongs with the target/environment deployment context. A role would add ceremony without identifying the actual control point. Policy can represent automatic, confirmation-gated or externally executed changes without requiring one universal actor model.

**Consequence.** Access credentials and technical ability are not treated as permission. Deployment may report required actions even when policy prevents it from executing them.

## D11 — Locator, trust, policy and action remain separate

**Decision.** Keep source/location information separate from source trust, target-change policy and deployment action.

**Reason.** A Bootstrap Profile `WHERE` value or any other locator only answers where material can be resolved. Treating a locator as permission would allow discovery metadata to become an implicit install/execute authority.

## D12 — Future package acquisition remains an explicit Deployment seam

**Decision.** Preserve a future path for trusted source/catalog acquisition, but do not require or implement a generic acquisition mechanism now.

**Reason.** General package/catalog/source infrastructure is not yet sufficiently established. Premature fetch semantics would either couple Deployment to Bootstrap or hard-code platform-specific routes into the generic model.

**Consequence.** Missing material is currently surfaced/blocked unless established environment mechanics can provide it. A later acquisition step must check trust and Deployment Policy before obtaining or applying material.

## D13 — Bootstrap artefacts are ordinary deployables when built for a Target

**Decision.** Bootstrap Profiles and Bootstrap Contributions may be Deployment Set members under the same artefact-neutral deployment model as Standards, Tools and other deployables.

**Reason.** Deployability is a property of the produced target representation/contribution, not ownership of the semantic artefact. Special Bootstrap deployment semantics would duplicate Deployment responsibility.

## D14 — Manual Bundle replacement is a target-channel implementation

**Decision.** Treat the current common Standards/Tools Bundle plus manual ChatGPT project-file replacement as an interim Representation/Channel implementation, not as a separate architectural deployment model.

**Reason.** The existing Target abstraction already supports project bundles and upload/sync style channels. Automation can later replace the manual channel without changing desired-composition or reconciliation semantics.

## D15 — Deployment-time composition is mechanical assembly, not semantic Build

**Decision.** Preserve semantic production upstream in Build. AI Deployment may perform only the set-aware mechanical assembly needed to realise already built members/artefacts in a concrete Target.

**Reason.** Existing phrases such as “compose the target representation” and “rebuild fully” correctly described target reconciliation intent but could also be read as authority for Deployment to transform canonical semantics independently. That would create a second semantic renderer, blur Build provenance, and allow stale deployed material or Design history to become accidental production input.

**Consequence.** Build remains responsible for rendering/transforming current authoritative/canonical semantics into target-compatible contributions/packages and for any assembled consumption artefact that is itself a Build output. Deployment selects those outputs by Set/Target and may mechanically place, concatenate, register, wrap or otherwise assemble them where the Target contract requires it. If a required semantic transformation has not been built, Deployment reports a Build/material blocker rather than producing it itself.

## D16 — Deployment state cannot substitute for canonical/build provenance

**Decision.** Treat authoritative/canonical source identity and Build/package provenance as upstream facts consumed by Deployment; verified deployment state is a separate downstream fact.

**Reason.** A deployed Bundle/package can be current, stale, partially verified or platform-pinned independently of the semantic source and Build that produced it. Using deployment status or an older deployed representation as production authority would reverse the production flow and weaken reproducibility.

**Consequence.** Deployment may inspect existing target content to calculate reconciliation, but it does not use that content as the semantic source for rebuilding. Status and verification report deployed/runtime facts without claiming canonical or Build provenance that was not supplied/verified.

## D17 — Consume Build-owned composition posture explicitly

**Decision.** AI Deployment consumes the Build-owned `CompositionPosture` values `MemberContribution` and `AssembledConsumptionArtefact` as explicit deployment-facing facts. It does not infer or override posture from payload structure, filename, representation type or deployed state.

**Reason.** The Build v3 output contract closes the remaining interface ambiguity by stating whether an output is intended for downstream mechanical assembly or is already an authorised assembled consumption artefact. Reusing those Build-owned terms avoids a second Deployment classification scheme and keeps the semantic-production boundary enforceable.

**Consequence.** `MemberContribution` outputs may participate in Deployment-owned deterministic mechanical target assembly. `AssembledConsumptionArtefact` outputs are atomic at their internal semantic/member-composition boundary; Deployment may mechanically place/publish/wrap them, but a change to that internal composition requires a replacement Build output. Reconciliation resolves posture together with source provenance and Build-output/package identity/integrity and returns a Build/material blocker when the required posture-compatible output is unavailable.


## D18 — Deployment Registry is the authoritative built-supply boundary

**Decision.** Introduce **Deployment Registry** as the AI-Deployment-owned source of validated built packages available for downstream Deployment resolution. The physical implementation may be a folder, Git repository, package store, service or another conforming mechanism.

**Reason.** Build needs a stable post-Build destination that is more specific than an ordinary copy location but does not itself claim runtime Deployment state. The Registry closes the explicit seam left by Build v6 and the current Capability Build package contract.

**Consequence.** Generic Build may nominate the AI-Deployment-owned Registry Tool after successful validation. `AIDE_PublishBuildOutputTool` remains the ordinary location-copy Tool and does not claim Registry registration.

## D19 — Deployable Package is the generic Registry unit

**Decision.** Use **Deployable Package** as the generic Registry package concept. `Capability Package` remains the Capabilities-owned first specialised Package kind rather than being renamed.

**Reason.** AI Deployment should not be structurally limited to Capability Packages when other producer domains may later publish deployable packages. Retaining the producer-specific name preserves existing ownership while adding one generic umbrella.

## D20 — PackageId identifies an immutable concrete package instance

**Decision.** A registered `PackageId` is immutable. A stable Logical Package Identity groups successive package instances; the Registry maintains a separate mutable `Current Package` relation.

**Reason.** Rewriting one package in place weakens provenance, rollback, diff and reproducibility. Capability/Element semantic release is already distinct from PackageId, so another concrete Build can truthfully use a new PackageId without inventing a semantic release.

## D21 — Registry lifecycle is Available, Deprecated and Withdrawn

**Decision.** Registry-owned package lifecycle states are:

```text
Available
Deprecated
Withdrawn
```

`Deprecated` remains usable but discouraged and may identify a successor. `Withdrawn` is retained historically but excluded from ordinary new/current resolution. Physical purge is separate retention maintenance and is not automatic in v1.

**Reason.** Deprecation, withdrawal and byte deletion have different consequences. Collapsing them into “remove package” either destroys evidence or makes retirement too weak.

**Consequence.** Neither deprecation nor withdrawal directly mutates runtime targets. Any resulting runtime removal is determined later through normal desired-state reconciliation.

## D22 — Registry-owned state remains separate from immutable package metadata

**Decision.** Current/lifecycle/Release Batch/registration state is stored as Registry metadata and does not modify the package identified by PackageId.

**Reason.** Registry treatment changes independently from producer Build output. Mutating package bytes to record deprecation/current status would invalidate integrity and make the same PackageId mean different things over time.

## D23 — Registry actions are owned by one explicit Deployment Tool

**Decision.** Publish `AIDE_DeploymentRegistryTool@v1` with Register, Release Batch and lifecycle actions. Build may invoke it only as an explicit nominated post-Build Tool after successful package validation.

**Reason.** The destination/mechanism owner should own the action contract. Build v6 deliberately reserves AI Deployment Registry registration to an AI-Deployment-owned Tool.

**Consequence.** Registry action failure is reported separately and does not erase a successful Build package.

## D24 — Release Batch is the coordinated Registry visibility boundary

**Decision.** Use explicit **Release Batch** when several package publications/lifecycle changes must become visible to downstream automation together. Packages are staged while the Batch is Open; explicit Release validates and exposes the changes together.

**Reason.** Triggering Set reconciliation after every package in a coordinated multi-package Build can create waste and temporarily incoherent mixed old/new supply. Timing or package-count inference is not a reliable completion signal.

**Consequence.** Batch Release provides atomic Registry visibility only. It does not create a fictional cross-platform runtime transaction guarantee.

## D25 — Registry changes trigger re-evaluation, not unconditional redeployment

**Decision.** Registry semantic events may invoke configured Deployment Triggers for affected Deployment Set Definitions. The triggered process resolves/compares concrete desired state and takes no package/delivery action when that result has not materially changed.

**Reason.** Registry automation should be responsive but idempotent. A new registration can be irrelevant to a Set or reproduce the same resolved composition.

## D26 — Package and built-output Tags may drive Deployment selection

**Decision.** Allow `AIDE_Tags` at Deployable Package level and at individual built target/member level. For selection, a member's effective tags are the union of Package Tags and its own Tags.

**Reason.** Tags provide a reusable way to resolve eligible supply after a Set has established its
membership mode. For a fixed Set such as `AIDE_Core`, Tags do not replace the explicit desired
member list.

**Boundary.** Tags are classification/selection only. They do not replace Dependencies, Scope, Build-target compatibility, Migration posture or Deployment Policy.

## D27 — Post-Build result is not immutable package content

**Decision at v6.** A producer package could carry the nominated post-Build request/intent, while
the actual Registry post-Build result remained external.

**Superseded by D43.** Review D R1 showed that the request is workflow state too; neither request nor
result belongs in immutable Package bytes.

**Reason.** Registry registration occurs after successful package validation. Requiring its result inside the package would force mutation after the package's identity/integrity was established and conflicts with Build v6's explicit separation of production and post-Build result.

## D28 — Deployment Set Release is immutable desired-content truth

**Decision.** Resolve a Set Definition into an immutable `<Set>@vN` record containing exact
PackageIds/build outputs, Definition revisions, final Output identities/integrity and a resolution
digest. Keep a mutable `DesiredRelease` pointer separate from target state.

**Reason.** One shared release must identify the same exact content across all final
representations without implying that every Target is already installed or verified.

## D29 — No generic downstream Deployment Package

**Decision.** Retain Deployable Package for Registry supply and use Deployment Output for the final
set-level consumable. Do not add another generic package wrapper.

**Reason.** A second package concept would duplicate identity and blur upstream validated supply
with downstream set assembly.

## D30 — Issue only complete valid Set releases

**Decision.** Assign/freeze the next Set version only after every fixed required member has eligible
supply and every required Output resolves, assembles and validates. Preserve applicable required-
presence facts for per-Target evaluation. A failed candidate consumes no version and leaves the
previous Desired Release in place.

## D31 — Exact PackageId/output change may advance the Set release

**Decision.** A different selected PackageId or final Output content is a different exact resolved
Set even when semantic Capability releases are unchanged. Delivery destination, credentials,
adapter/policy or later target-state changes do not alone create a content release.

## D32 — One Output may feed several independently reconciled Targets

**Decision.** A Deployment Output is not one-to-one with Deployment Target. Target Adapter is the
platform/channel implementation behind each Target.

**Reason.** One Claude plugin output must support independent Claude account and Claude Code target
state; bundle publication and project/context attachment are also distinct target stages.

## D33 — Every final Output carries intrinsic Set provenance

**Decision.** Mechanically stamp Set release identity, Output identity/type and resolution digest
inside every final Output. Plugin assembly may add a generated provenance-only status member.

**Reason.** Platform-visible install version may be unavailable to running content or may differ
from active-session pickup. Runtime needs evidence from the deployed representation itself.

## D34 — State, Result and assurance remain distinct

**Decision.** Deployment State is mutable per-Target observed truth. Deployment Result records one
reconciliation invocation. State distinguishes desired, publication, installed/attached and
runtime-observed releases plus `Verified | Mismatch | Unverified`; verification assurance is
`Enforced | Advisory`.

## D35 — Automatic unchanged resolution is no-op; explicit Reconcile may retry

**Decision.** An automatic Registry event with unchanged exact resolution creates no release and no
delivery retry. Manual/explicit Reconcile may retry or re-verify incomplete Targets of the existing
Desired Release.

**Reason.** This preserves Registry event idempotency while allowing operational recovery.

## D36 — AIDE Core uses shared identity across distinct roles

**Decision.** Use `AIDE_Core` as Build Target Profile identity, package/member Tag and Deployment Set
identity without collapsing those concepts. The immutable exact Set release is `AIDE_Core@vN`.

## D37 — AIDE Core has four required Deployment Outputs

**Decision.** Resolve Claude plugin `aide-core-claude`, versioned Claude bundle, versioned ChatGPT
bundle and OpenAI plugin `aide-core-openai` together under one AIDE Core release. Bundle assembly
uses stable logical member ordering without semantic precedence.

## D38 — AIDE Core uses two shared publication actions

**Decision.** Initially publish both plugins to separate Claude/OpenAI areas of the single
`DigitalBusiness-AIDE-Marketplace` repository through one convenient Git action, and publish both
versioned bundles to
`C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation\_deploymentPackages` through one
local action that moves earlier current bundles to `_deploymentPackages\_superseded`.

**Boundary.** Shared publication is not atomic runtime installation. Bundle context placement may
remain manual and must not be reported as complete merely because the local file exists.

## D39 — OpenAI plugin required reach is Codex

**Decision.** Use GitHub/OpenAI marketplace distribution as the preferred route. Codex is required
reach; supported ChatGPT surfaces are additional intended reach. Keep workspace sync/install and
runtime verification separate from repository publication.

## D40 — Fixed Set composition and supply selection are separate

**Decision.** A fixed Deployment Set owns an explicit required/desired member list. Its supply
selector resolves eligible Registry packages for those members and cannot silently redefine
composition. A selector may define variable membership only when the Set explicitly declares a
dynamic membership mode.

## D41 — Required-presence satisfaction is per Target

**Decision.** Immutable Set releases preserve applicable required-presence facts. Target
reconciliation evaluates satisfaction against observed Target state, including valid material
already present outside Set membership. Set resolution does not freeze a Target-independent
satisfaction result.

## D42 — Deployment consumes frozen snapshot-relative Tags

**Decision.** Registry and Deployment preserve/use producer Build Tags and freshness evidence tied
to the immutable package source snapshot. They do not regenerate producer-owned Tags when newer
upstream source exists.

## D43 — Post-Build request and result are external workflow state

**Decision.** Build request/WorkPackage carries nominated post-Build action/inputs. Registry and
Outcome carry the actual result. Neither request nor result is intrinsic immutable package content.

## D44 — Mechanical assembly preserves required member facts

**Decision.** Final Outputs preserve member-level dependency/Migration/Scope/Tags and other required
downstream facts, directly or through deterministic provenance references. Mechanical composition
does not flatten away runtime/reconciliation requirements.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDeployment_Design_v7, AIDE_Build@v8
References: AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v2, AIDE_DeploymentRegistryTool@v2, AIDE_CapabilityBuild@v4, AIDE_Dependencies@v3, AIDE_Tags@v3, AIDeployment_OpenAI_Reference_v3
<!-- END SOURCE: AIDeployment_Decisions_v7.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Registry_Design_v2.md -->
# AI Deployment Registry — Design

> **Version 2** (2026-09-02). Reconciles Registry events and Release Batches to exact Deployment Set Release resolution.
>
> Created: 2026-09-02 | Last modified: 2026-09-02

## §1 — Purpose

Provide one stable source of validated built supply that AI Deployment can resolve without reopening
producer Design or treating an ordinary filesystem/repository copy as deployment state.

The Registry sits between successful producer Build and Deployment Set resolution:

```text
validated Deployable Package
        ↓
AIDE_DeploymentRegistryTool
        ↓
Deployment Registry
        ↓
Deployment Set resolution / reconciliation
```

The Registry is an interface contract, not a required storage technology. A conforming Registry may
be implemented by a folder, Git repository, package store, service or another mechanism that can
preserve the required identities, bytes, metadata and lifecycle state.

## §2 — Deployable Package

A **Deployable Package** is the generic Registry unit: a validated Build-owned package accepted as
available supply for later Deployment.

`Capability Package` is the first specialised Package kind. Future producer domains may define
other Package kinds without changing generic Registry semantics provided they satisfy this contract.

Keep these identities distinct:

- **Logical Package Identity** — stable producer/package identity used to group successive builds;
- **PackageKind** — producer-defined package contract kind, for example `CapabilityPackage`; and
- **PackageId** — unique identity of one concrete validated Build package instance.

A forced/repeated Build may therefore create another `PackageId` for the same Logical Package
Identity without implying a new semantic capability release.

## §3 — Package acceptance contract

Before a package becomes Registry supply, resolve enough producer-owned information to identify and
use the concrete Build result without semantic inference.

Every accepted package shall expose directly or through its applicable package contract:

```text
PackageKind
Logical Package Identity
PackageId
integrity evidence
source/canonical provenance
Build/production contract provenance sufficient for the package kind
one or more deployment-facing built outputs/members where applicable
Build-owned CompositionPosture for each output where required
payload/file/area identity sufficient to resolve those outputs
Build validation evidence sufficient to establish that the submitted package is the validated result
```

Preserve package-kind-owned metadata needed downstream, including dependency, Migration, Bootstrap,
activation/registration or other owner-defined information where applicable. Generic Registry does
not reinterpret those semantics.

A package/target contract may additionally provide:

- package-level Tags;
- Build-target/member-level Tags;
- surface support, conformance, variation or degradation results;
- successor/replacement information owned by the producer; and
- namespaced extension metadata for specialised Deployment-time Standards/Tools.

Unknown optional extension metadata is preserved. A package that declares an extension mandatory
for correct Deployment is not eligible for an operation that cannot resolve the required handler.

The Registry does not require one universal physical package/manifest format. It requires the
semantic envelope above to be resolvable and unambiguous.

## §4 — Immutability and Current Package

A successfully registered package instance is immutable under its `PackageId`.

- Re-registering the same `PackageId` with the same verified payload/integrity is idempotent.
- Re-registering the same `PackageId` with different bytes, integrity or producer metadata is a
  conflict and fails visibly.
- A later Build of the same Logical Package Identity uses a new `PackageId`.

The Registry separately records a mutable **Current Package** relation for each Logical Package
Identity. `Current` means the package instance normally selected by floating/current resolution; it
is an authority relation, not a synonym for newest timestamp.

Package bytes and producer-owned immutable metadata do not change when Registry lifecycle/current
state changes.

## §5 — Registry-owned lifecycle state

Registry lifecycle state is maintained separately from package payload.

### Available

Normal Registry supply. An Available package may participate in ordinary resolution subject to the
Deployment Set, Build-target compatibility, Dependencies and other governing rules.

### Deprecated

The package remains available but is discouraged. Record a concise reason and successor/replacement
where known.

Deprecation alone does not uninstall or invalidate an already deployed package. Floating/current
resolution should prefer a suitable non-deprecated current replacement where one exists and surface
a warning when a deprecated package remains selected.

### Withdrawn

The package is retained as historical/evidential state but is not eligible for ordinary new/current
resolution. If it was Current, withdrawal must either move Current to a valid replacement in the
same Registry transaction or leave the Logical Package Identity without an ordinary Current package.

Withdrawal may cause a later Deployment Set resolution to change and therefore may lead to removal
through normal Deployment reconciliation. It does not itself mutate runtime targets.

A withdrawn package may be used for explicit authorised recovery/forensic purposes only under the
applicable policy; it is not silently reintroduced by floating resolution.

### Purge

Physical deletion is repository/retention maintenance, not normal package lifecycle. v1 defines no
automatic purge. Historical package instances are retained by default; a future retention contract
may add safe purge after demonstrated need.

## §6 — Tags

Deployable Packages and individual built target/member outputs may carry `AIDE_Tags` values.

For Deployment selection, the effective tag set of a target/member is the union of:

```text
Package Tags + target/member Tags
```

Use the existing `AIDE_Tags` exact Boolean query semantics where tag selection is used. Registry
publication shall not knowingly publish stale generated Tags when those Tags are part of governed
package state.

Tags are classification/selection data. They do not replace:

- semantic Dependencies or required presence;
- Scope;
- Build-target compatibility;
- Migration posture; or
- Deployment Policy.

## §7 — Release Batch

A **Release Batch** groups Registry publications that must become visible to downstream automatic
resolution together.

The minimum v1 model is:

```text
Open
  ↓ Release
Released

Open
  ↓ Abandon
Abandoned
```

While a Batch is Open:

- packages may be validated and staged;
- staged instances do not replace ordinary Current Package state; and
- batch-triggered Deployment automation does not run from each staged package.

`Release` validates the batch as a coherent Registry transaction, including any declared expected
package set, conflicts, integrity and lifecycle actions. Only after successful validation are the
staged Current/lifecycle changes made visible together.

Release therefore provides an **atomic Registry visibility boundary**. It does not claim atomic
publication or rollback across heterogeneous runtime Deployment Targets.

An expected package list is optional and acts as a release validation condition. Explicit Release,
not inferred package count alone, is the authoritative signal that the producer/director considers
the batch complete.

## §8 — Registry events and Deployment triggers

Registry state changes may emit semantic events such as:

```text
PackageCurrentChanged
PackageDeprecated
PackageWithdrawn
ReleaseBatchReleased
```

A **Deployment Trigger** may map relevant Registry events to re-evaluation of one or more Deployment
Set Definitions. Trigger configuration is separate from Registry storage and may be automatic or
manual.

A Registry event means “desired supply may have changed”, not “redeploy unconditionally”. The
receiving Deployment process resolves the affected Set and compares its exact selected PackageIds,
built outputs and final Deployment Output content with the current Desired Release. If unchanged,
an automatic Registry-triggered invocation is a true no-op: no new Set release and no delivery
retry. An explicit/manual Reconcile may still retry or re-verify incomplete Targets of the existing
Desired Release.

There is no generic downstream Deployment Package. Registry supply is a Deployable Package; the
resolved set-level consumables are Deployment Outputs under an immutable Deployment Set Release.

## §9 — Registry publication boundary

Registry registration is an AI-Deployment-owned post-Build action.

Generic Build may nominate `AIDE_DeploymentRegistryTool` after successful output validation. The
Registry Tool owns acceptance/registration semantics; generic `AIDE_PublishBuildOutputTool` remains
for ordinary filesystem/repository publication and does not claim Registry state.

A Registry action result is separate from the immutable producer package. A Registry publication
failure does not erase a successfully validated Build package and may be resumed/retried against the
same PackageId where safe.

## §10 — Package metadata versus Registry metadata

Keep producer/package and Registry state distinct.

**Immutable producer/package state** includes, as applicable:

```text
PackageKind
Logical Package Identity
PackageId
integrity
source/build provenance
built member/target outputs
CompositionPosture
package/member Tags
dependency/migration/extension information
Build validation evidence
producer-declared limitations/degradation information
```

**Registry-owned mutable state** includes:

```text
Current Package relation
Available / Deprecated / Withdrawn
reason/successor where applicable
Release Batch staging/release state
registration receipt/evidence
retention/purge state where later implemented
```

Changing Registry state must not rewrite an immutable package merely to keep the two views in one
file.

## §11 — Physical implementation and authority

Environment/platform configuration resolves the Registry locator, access mechanism, credentials,
retention implementation and transaction mechanics.

Technical write access does not by itself grant authority to Register, Release, Deprecate or
Withdraw. The Registry Tool must operate under the applicable work/Deployment authority.

The Registry is trusted built supply only to the extent established by its configured source,
producer provenance, integrity and governing policy. Registering a package does not itself grant
permission to deploy it to a runtime Target.

## §12 — Failure and idempotency

- invalid package contract/integrity → reject; do not create Current state;
- duplicate PackageId with identical verified content → idempotent success;
- duplicate PackageId with conflicting content → fail visibly;
- failed Register outside a Batch → preserve prior Current state;
- failed Batch Release → preserve prior visible Registry state and keep/return staged state for
  correction or abandonment;
- Deprecate/Withdraw repeated with the same intended state → idempotent;
- missing required package-kind extension handler → block the affected downstream operation rather
  than dropping the extension;
- Registry action failure never converts a valid producer Build into a failed Build result.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v8, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDeployment_Design_v6, AIDeployment_SetRelease_Design_v1, AIDE_CapabilityBuild@v3, AIDE_PublishBuildOutputTool@v1
<!-- END SOURCE: AIDeployment_Registry_Design_v2.md -->

---

<!-- BEGIN SOURCE: AIDeployment_SetRelease_Design_v2.md -->
# AI Deployment Set Release — Design

> **Version 2** (2026-09-03). Separates desired membership from supply selection and required-presence satisfaction.

## Set Definition and exact resolution

A **Deployment Set Definition** identifies desired logical composition and the rules used to resolve
eligible registered supply. Resolution selects exact immutable PackageIds and exact compatible
built outputs; it does not reopen producer Design or infer missing target representations.

A fixed-composition Set owns an explicit required/desired member list. Its supply selector chooses
eligible Registry supply for those members; it does not decide whether a member belongs. If a
required member has no eligible supply, candidate resolution blocks rather than silently shrinking
the Set. A deliberately dynamic Set may instead declare selector-defined variable membership, but
that mode must be explicit and must not be inferred from use of a selector.

A candidate is valid only when all required desired members have eligible supply and every required
Deployment Output can be resolved, mechanically assembled and validated. Applicable semantic
required-presence facts must be preserved and interpretable in the release/output; whether they are
satisfied is evaluated later for each concrete Target against observed state.

## Deployment Set Release

A **Deployment Set Release** is the immutable exact resolved content result:

```yaml
DeploymentSetRelease:
  Identity: <Set>@vN
  DefinitionRevision: <exact revision>
  ResolvedMembers: [<LogicalPackage, PackageId, BuildOutput, Integrity>]
  OutputDefinitions: [<identity and revision>]
  Outputs: [<identity and integrity>]
  ResolutionDigest: <digest>
```

`DesiredRelease` is the Set's mutable pointer to the release currently intended for Targets.
Previous releases remain immutable history. `Current` is not used for this pointer because Registry
Current Package state and successful target deployment are separate facts.

There is no generic downstream `Deployment Package`. Upstream Registry supply is a Deployable
Package; the final set-level consumable is a Deployment Output.

## Release creation

Resolve and validate a candidate before assigning the next issued version. A failed candidate does
not consume a Set release number and does not replace the last Desired Release.

A new release is required when exact selected PackageIds/build outputs, final output content, or a
Set/output Definition change alters the exact resolved result. Changed delivery destinations,
credentials, adapters, policy, refresh commands or later verification do not change Set content and
therefore do not alone create another Set release.

The platform-native version may map the AIDE release into a required syntax, but the canonical
identity remains `<Set>@vN`.

## Deployment Output Definitions

Each Definition selects compatible built contributions for one final representation and supplies
deterministic mechanical assembly/validation rules. `MemberContribution` outputs may be combined;
an `AssembledConsumptionArtefact` remains atomic at its Build-owned semantic composition boundary.

Mechanical assembly preserves member-level dependency/Migration/Scope/Tags and other required
downstream facts or a deterministic provenance reference to them. Assembly must not discard those
facts merely because several members share one final representation.

Bundle assembly defaults to stable logical Capability/member identity ordering. Ordering is not
semantic precedence unless an owning upstream contract explicitly makes it so.

Every final output carries an intrinsic runtime-visible marker:

```text
AIDE Set Release: <Set>@vN
Output: <output identity/type>
Resolved Set Digest: <digest>
```

Plugin assembly may add a small generated status member solely to expose this provenance. It is not
a Capability and has no independent semantic release.

## Trigger behaviour

Relevant Registry events cause Set re-evaluation. For an automatic Registry event, unchanged exact
resolution is a true no-op: no new release and no delivery retry. An explicit/manual Reconcile may
retry or re-verify failed, blocked, mismatched or unverified Targets of the existing Desired Release.

An Open Release Batch keeps staged changes outside ordinary Current resolution. Batch Release makes
the coordinated Registry changes visible once and therefore causes one Set re-evaluation.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7
References: AIDeployment_Registry_Design_v2, AIDeployment_TargetAdapter_Design_v1
<!-- END SOURCE: AIDeployment_SetRelease_Design_v2.md -->

---

<!-- BEGIN SOURCE: AIDeployment_TargetAdapter_Design_v1.md -->
# AI Deployment Target Adapter — Design

> **Version 1** (2026-09-02). Defines Delivery Actions, Target Adapters, layered verification, Deployment State and invocation Result.

## Relationship

```text
Deployment Set Release
  → Deployment Output
  → one or more Deployment Targets
  → Target Adapter
  → publish / install / attach / refresh / remove
  → verify
  → Deployment State + Deployment Result
```

One output may feed several independently reconcilable Targets. A Target Adapter is the
platform/channel-specific implementation behind an existing Deployment Target, not a new top-level
deployment concept.

## Target Adapter contract

```yaml
TargetAdapter:
  Representation: <Plugin | Bundle | other>
  Channel: <GitMarketplace | LocalFile | ManualUpload | other>
  Destination: <environment-owned reference>
  Actions:
    Publish: <mechanism>
    InstallOrUpdate: <mechanism if available>
    Remove: <mechanism if available>
  Pickup: <immediate | refresh | reload | new-session | manual | unknown>
  Verification:
    Publication: [<checks>]
    PlatformState: [<checks>]
    RuntimeState: [<checks/probes>]
  Policy: <environment Deployment Policy>
```

Concrete layouts, commands, Git mechanics, UI actions, destinations and credentials remain adapter/
environment configuration rather than Capability semantics or generic Deployment rules.

## Delivery Action

A **Delivery Action** is an idempotent configured operation that moves one or more Deployment
Outputs toward one or more Targets. It identifies input Output, Adapter, Destination, invocation
mode, prerequisites and action-level verification. It owns no semantic content and is not part of
the immutable Set release.

Several outputs may share one convenient publication action, such as one repository commit, without
claiming atomic installation or activation across their later runtime Targets.

## Verification layers

Use the layers a Target actually exposes:

1. **Output** — frozen release, integrity, expected marker and valid assembly.
2. **Publication** — expected bytes/revision exist at the distribution destination.
3. **Platform** — expected release is installed, attached or resolved by the platform.
4. **Runtime** — the running surface observes the intrinsic release marker and, where needed,
   passes a behaviour probe.

Visibility or installation alone does not prove runtime execution. Published, installed/attached
and runtime-observed releases may differ.

Verification assurance is:

- `Enforced` when evidence is obtained independently of model choice/compliance; or
- `Advisory` when the model materially selects, executes or reports the check.

## Deployment State

State is mutable and per Target. Record, as applicable:

```yaml
DeploymentState:
  Target: <identity>
  Desired: <SetRelease, Output, Integrity>
  Publication: <observed release and evidence>
  Platform: <installed/attached release and evidence>
  Runtime: <observed release, availability and session pickup>
  Verification:
    Status: Verified | Mismatch | Unverified
    Assurance: Enforced | Advisory
    Evidence: <reference>
    EvidenceAt: <time>
  Mismatches: [<facts>]
  NextAction: [<actions>]
```

## Deployment Result

A Result records one reconciliation invocation rather than duplicating persistent State. Use:

- `Complete` — every requested Target is at the required verified desired state, including a
  verified no-op;
- `Partial` — some requested Targets are Complete and others remain blocked, failed or unverified;
- `Blocked` — a known authority, prerequisite, manual action or required-verification condition
  prevents progress; or
- `Failed` — an attempted operation or validation failed.

Report target-level `Applied | NoOp | ManualRequired | Failed` action facts and the resulting State.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v6
References: AIDeployment_SetRelease_Design_v1, AIDeployment_AIDECore_Reference_v1
<!-- END SOURCE: AIDeployment_TargetAdapter_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDeployment_AIDECore_Reference_v2.md -->
# AIDE Core Deployment — Reference Configuration

> **Version 2** (2026-09-03). Makes AIDE Core desired membership explicit and updates the bundle publication repository path.

## Shared identity

`AIDE_Core` is reused deliberately as three related but distinct identities:

| Layer | Meaning |
|---|---|
| Build Target Profile | reusable four-target Capability Build requirements |
| Registry/package tag | classification of eligible AIDE Core built contributions |
| Deployment Set | logical desired composition resolved from Registry supply |

The immutable exact Set release is `AIDE_Core@vN`.

## Deployment Set and Outputs

```yaml
DeploymentSetDefinition:
  Identity: AIDE_Core
  MembershipMode: Fixed
  RequiredMembers:
    - Standards
    - Tools
    - Tags
    - Scope
    - Dependencies
    - Migration
    - Review
    - Messaging
  SupplySelector:
    TagQuery: AIDE_Core
    PackageRelation: Current
  RequiredOutputDefinitions:
    - ClaudePlugin
    - ClaudeBundle
    - ChatGPTBundle
    - OpenAIPlugin
  ReleaseIdentity: AIDE_Core@vN
  CandidatePolicy: IssueOnlyAfterAllRequiredOutputsValidate

DeploymentOutputs:
  ClaudePlugin:
    Inputs: BuildTarget=ClaudePlugin
    Assembly: DeterministicMemberContributionAssembly
    Identity: aide-core-claude

  ClaudeBundle:
    Inputs: BuildTarget=ClaudeBundle
    Assembly: StableLogicalMemberOrder
    Identity: AIDE_Core_Claude_Bundle_vN.md

  ChatGPTBundle:
    Inputs: BuildTarget=ChatGPTBundle
    Assembly: StableLogicalMemberOrder
    Identity: AIDE_Core_ChatGPT_Bundle_vN.md

  OpenAIPlugin:
    Inputs: BuildTarget=OpenAIPlugin
    Assembly: DeterministicMemberContributionAssembly
    Identity: aide-core-openai
```

Every output carries `AIDE_Core@vN`, its output identity/type and the resolved-set digest. Plugin
outputs include the generated provenance-only `aide-core-status` member.

## Delivery Actions and destinations

```yaml
DeliveryActions:
  PublishAIDECoreMarketplace:
    Inputs: [ClaudePlugin, OpenAIPlugin]
    Channel: GitMarketplace
    Repository: DigitalBusiness-AIDE-Marketplace
    Areas:
      ClaudePlugin: claude/
      OpenAIPlugin: openai/
    Evidence: GitCommit

  PublishAIDECoreBundles:
    Inputs: [ClaudeBundle, ChatGPTBundle]
    Channel: LocalFile
    RepositoryRoot: 'C:\Users\david\dev\repos\DigitalBusiness-AIDE'
    Destination: 'C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation\_deploymentPackages'
    SupersededDestination: 'C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation\_deploymentPackages\_superseded'
    Rule: MoveEarlierCurrentBundlesThenPublishBothNewVersionedFiles
```

The shared Git commit/local operation is an implementation convenience and provenance point, not a
cross-runtime transaction guarantee.

## Target map

| Output | Deployment Target | Initial adapter/pickup posture |
|---|---|---|
| Claude Plugin | Claude account plugin | marketplace/account update; account-backed surfaces reconcile together where platform evidence supports it |
| Claude Plugin | Claude Code plugin | separate local marketplace/plugin update and reload/session pickup |
| Claude Bundle | local published bundle | automatic versioned file replacement/publication |
| Claude Bundle | configured Claude contexts | manual/platform-specific placement until a verified adapter exists |
| ChatGPT Bundle | local published bundle | automatic versioned file replacement/publication |
| ChatGPT Bundle | configured ChatGPT contexts | manual/upload/import until a verified adapter exists |
| OpenAI Plugin | GitHub/OpenAI marketplace publication | repository publication and marketplace sync/import |
| OpenAI Plugin | required Codex target | install/update then runtime marker/behaviour verification |
| OpenAI Plugin | supported ChatGPT target | additional reach only where that surface supports the plugin |

The Claude account and Claude Code installations are independently reconcilable even though they
consume one Claude plugin output. Which installation governs a particular Claude Desktop Code-tab
runtime remains an empirical adapter fact to re-probe; architecture does not assume it.

## Trigger configuration

Re-evaluate `AIDE_Core` on:

```text
PackageCurrentChanged
PackageDeprecated
PackageWithdrawn
ReleaseBatchReleased
Deployment Set/output Definition change
Target/environment configuration change
explicit/manual Reconcile
```

For Registry events, resolve first and no-op when exact state is unchanged. A target/environment
configuration change reconciles the existing Desired Release unless content changes. Manual
Reconcile may retry or re-verify incomplete Targets without issuing a new Set release.

## Verification baseline

Record Desired Release, publication state, installed/attached platform release, runtime-observed
release, verification status and assurance separately. A Target becomes fully verified only after
its required release-marker and behaviour checks pass. Manual placement/action is reported as
`ManualRequired`; local publication alone does not claim a project/chat context is using the bundle.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7, AIDE_CapabilityBuild@v4
References: Capabilities_AIDECore_BuildTargetProfile_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_OpenAI_Reference_v3
<!-- END SOURCE: AIDeployment_AIDECore_Reference_v2.md -->

---

<!-- BEGIN SOURCE: AIDeployment_OpenAI_Reference_v3.md -->
# AI Deployment OpenAI — Reference

> **Version 3** (2026-09-02). Adds the current GitHub marketplace distribution baseline while
> retaining the runtime-execution evidence boundary.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Established evidence

The tested local OpenAI plugin/skill route cannot be treated as one common private deployment
channel across ChatGPT Chat and Codex.

The evidence established:

- a representation being visible/installed in one surface does not prove its skill body is
  executable in another runtime;
- Codex local plugin/marketplace behaviour and ChatGPT Chat runtime availability are distinct;
- ChatGPT web discovery of a local plugin was not established by the local route;
- standalone/personal skill availability across Work, Chat and Codex also differed in testing;
- UI presence or install state is therefore weaker evidence than a runtime content probe; and
- deployment architecture must model **surface**, **representation** and **distribution channel**
  separately.

## Architectural conclusion

Do not use the previously proposed “one local OpenAI plugin install = common ChatGPT + Codex
deployment route” as architecture.

Keep hosted/public/account-synchronised routes as empirical target-adapter work. The generic
Deployment model does not need those results before it can operate.

## Current GitHub marketplace baseline

Current official OpenAI documentation checked on 2026-09-02 establishes that:

- workspace administrators can import plugin marketplaces from public or private GitHub
  repositories;
- a marketplace may be located in a repository subdirectory and may track the default branch, a
  named branch/tag or a fixed commit;
- native `.agents/plugins/marketplace.json`, Claude-compatible marketplace manifests and a
  standalone Claude plugin manifest are supported import formats;
- new marketplaces use daily sync and `Sync now` requests an update;
- repository sync and workspace installation/access policy are separate; and
- removing a repository entry does not delete the imported workspace plugin—it becomes
  `No longer in source`, so runtime removal requires an explicit workspace/plugin action.

Accordingly, `DigitalBusiness-AIDE-Marketplace/openai` is the preferred initial distribution route
for `aide-core-openai`. Use the native OpenAI representation even though compatible import formats
exist; import compatibility does not prove equal runtime behaviour.

Codex is required reach for this output. ChatGPT is additional intended reach only where the
configured plan/workspace/role/surface supports it. A missing unsupported ChatGPT surface is not
automatically a degraded Build; failure in the configured required Codex target is.

## Evidence discipline

A reconstructed answer, prior reported probe value, project file read, or filesystem read is not
accepted as proof that a runtime executed the deployed capability. Verification should use a
fresh, target-appropriate runtime probe where execution availability is the claim.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDeployment_Design_v6
References: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING, Workflow_Platform_Working_2026-09-02-1_v1, https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex, https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github
<!-- END SOURCE: AIDeployment_OpenAI_Reference_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Standard_v7.md -->
# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v7`
> **Common name:** AI Deployment
> **Version 7** (2026-09-03). Makes Set membership authority, Target-relative required presence and frozen-Tag consumption explicit.
>
> **Default weight:** Requirement

## Purpose

Make validated built deployable material available for intended AI runtime surfaces, reconcile desired composition and applicable required presence with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes validated **Deployable Packages** from the configured **Deployment Registry**.

A Deployable Package supplies, directly or through its PackageKind contract:

- Logical Package Identity, unique concrete PackageId and integrity evidence;
- authoritative/canonical source and Build provenance sufficient to identify the produced result;
- deployment-facing built outputs/members and Build-owned `CompositionPosture: MemberContribution | AssembledConsumptionArtefact` where applicable;
- applicable producer-owned dependency/Migration and other required downstream metadata; and
- package-kind-specific validation evidence and extensions needed for correct Deployment.

`Capability Package` is the first specialised Deployable Package kind. Deployment does not reopen producer Design, reconstruct canonical semantics, or treat Registry/deployed state as semantic production authority.

## Deployment Registry

The Deployment Registry is the authoritative source of validated built supply available to Deployment. Its physical implementation may be a folder, Git repository, package store, service or another configured mechanism that preserves the required contract.

Registry package instances are immutable under `PackageId`. A stable Logical Package Identity may have successive PackageIds; Registry-owned `Current Package` state identifies the instance normally selected by current/floating resolution.

Registry-owned lifecycle state is separate from immutable package content:

```text
Available   — normal resolution eligibility
Deprecated  — remains available but discouraged; warn/prefer suitable replacement
Withdrawn   — retained historically but excluded from ordinary new/current resolution
```

Physical purge is retention maintenance and is not an automatic v6 Deployment lifecycle action.

Use `AIDE_DeploymentRegistryTool` for Register, Release Batch and Registry lifecycle actions. Generic ordinary Build publication does not establish Registry state.

## Tags

Deployable Packages and individual built target/member outputs may carry `AIDE_Tags` values.

For Deployment selection, the effective Tags for a built target/member are the union of Package
Tags and that target/member's Tags. Use `AIDE_Tags` Boolean query semantics. For immutable Registry
supply, consume the snapshot-relative Tags and producer Build evidence frozen before Package
validation; Deployment does not regenerate producer-owned Tags from newer source state.

Tags are classification/selection only. They do not replace semantic Dependencies, Scope, Build-target compatibility, Migration posture or Deployment Policy.

## Release Batch and triggers

A Release Batch may stage several package registrations/lifecycle changes until an explicit Release operation validates and exposes them together.

Batch Release is an atomic **Registry visibility** boundary only; it does not claim an all-or-nothing transaction across heterogeneous runtime Targets.

Registry events may cause configured Deployment Triggers to re-evaluate affected Deployment Set
Definitions. For an automatic Registry trigger, unchanged exact resolution means no new release and
no delivery retry. Explicit/manual Reconcile may retry or re-verify incomplete Targets of the
existing Desired Release.

Detailed Set selectors/output definitions/Delivery Actions remain governed by the current Deployment Set configuration and may be refined independently of this Registry contract.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition. For a fixed-composition Set, the
Definition owns an explicit required/desired member list and a separate supply selector resolves
eligible Registry instances for those members. Missing eligible supply blocks the candidate rather
than silently shrinking it. A deliberately dynamic Set may declare selector-defined variable
membership explicitly. Omission from any Set does not cancel semantic dependency/required-presence
requirements.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family and runtime/surface;
- representation;
- distribution channel;
- destination/account/workspace reference where applicable;
- effective target-change policy/authority;
- refresh/session-pickup behaviour where relevant; and
- verification requirements.

Surface, representation, channel and target-change policy are independent facts.

## Deployment Set Release and Outputs

Resolve a candidate from exact eligible PackageIds/build outputs while preserving all applicable
required-presence facts. Mechanically assemble and validate every required Deployment Output before issuing
the next immutable `<Set>@vN`. A failed candidate consumes no version and leaves the last
`DesiredRelease` in place.

The immutable release records its Set/Output Definition revisions, exact resolved members, Output
identities/integrity and resolution digest. A new exact PackageId/output or changed final Output
content may create a new Set release even when upstream semantic releases are unchanged. Target
destination, credentials, adapter/policy and verification-state changes do not alone change Set
content.

There is no generic downstream Deployment Package. Registry inputs are Deployable Packages; final
set-level consumables are Deployment Outputs.

Every final Output includes a runtime-visible Set release marker, Output identity/type and resolved-
set digest. Plugin assembly may add a generated provenance-only status member without creating a
Capability or semantic release.

The immutable Set release carries applicable required-presence facts but does not claim they are
satisfied independently of a Target. Target reconciliation evaluates satisfaction against that
Target's observed state, including valid material already present outside Set membership.

## Delivery Actions and Target Adapters

A Delivery Action is an idempotent configured operation that moves one or more Outputs toward one
or more Targets. A Target Adapter owns platform/channel-specific publish, install/update, remove,
pickup and verification mechanics behind a Target. One Output may feed several independently
reconciled Targets. Actions/adapters do not own semantic content and are not part of the Set release.

## Deployment Policy

Before mutating a Target, resolve the effective environment/target policy that determines whether and under what conditions the change may be applied.

Policy may permit automatic action, require confirmation/external execution, or otherwise constrain install/update/remove/acquisition behaviour. The exact policy values are environment configuration; this Standard owns only the rule that Deployment must honour them.

Technical access, credentials, Registry availability or a reachable destination do not by themselves establish permission to modify the Target.

## Reconciliation

For each requested Set/Target:

1. resolve the applicable Deployment Set Definition, its fixed or explicitly dynamic membership
   mode, selected Registry supply and configured Targets/Policies;
2. resolve exact PackageId/member/build-output identity and verify package/member integrity/provenance;
3. reject ordinary selection of Withdrawn packages and surface Deprecated selection where no suitable non-deprecated result replaces it;
4. preserve applicable semantic required-presence facts for later per-Target evaluation;
5. validate Build-declared composition posture and required package-kind extensions/handlers;
6. resolve all required Output Definitions and mechanically assemble eligible `MemberContribution` outputs deterministically without semantically re-rendering them;
7. treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary; if that composition must change, require the corresponding replacement Build output;
8. fail visibly on missing posture-compatible Build output, unresolved mandatory extension, or incompatible ownership/path/identity/namespace/posture claims;
9. assemble/validate all required candidate Outputs and compare exact resolution with DesiredRelease;
10. if changed and valid, freeze the next Set release; if invalid, retain the last Desired Release;
11. read/resolve observed target state where possible;
12. compare desired composition and applicable required presence with observed deployed state for
    each Target, allowing a requirement to be satisfied by valid material already present outside
    Set membership;
13. surface missing required material as a mismatch/blocker rather than making Set omission redefine the requirement;
14. determine and execute only the minimum policy-permitted Delivery Actions;
15. run layered Output/publication/platform/runtime verification; and
16. persist per-Target State and return one invocation Result.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

Mechanical assembly preserves member-level dependency/Migration/Scope/Tags and other required
downstream facts, directly or through deterministic provenance references. It does not flatten away
facts needed by target reconciliation or runtime use.

## Production and provenance boundary

Build/specialised producer Build is upstream of Deployment. It renders/transforms current authoritative semantics into concrete deployable outputs/packages and owns their source/build provenance, identity/integrity and composition posture.

Deployment Registry registration validates/preserves that output as supply; it does not make the Registry a semantic producer.

Deployment owns desired Set selection and target-state reconciliation. Any Deployment-time composition is mechanical assembly of eligible `MemberContribution` outputs required by the Target representation. An `AssembledConsumptionArtefact` remains atomic at its internal semantic/member-composition boundary.

Observed target content, an older package, a Registry lifecycle state or successful deployment status may be evidence for reconciliation but do not substitute for canonical/Build provenance.

## Package lifecycle versus runtime removal

Registry lifecycle and runtime lifecycle are separate.

- `Deprecated` does not itself remove deployed material.
- `Withdrawn` removes the package from ordinary new/current Registry resolution; any resulting change to desired Set composition is handled by normal Deployment reconciliation.
- runtime removal remains subject to Dependencies, composition posture, Target mechanics and Deployment Policy.

A Deployment-owned assembly of `MemberContribution` outputs may be reassembled without a no-longer-desired member. If removal changes the internal semantic/member composition of an `AssembledConsumptionArtefact`, Deployment requires the corresponding replacement Build output.

## Source and acquisition boundary

A Registry/source locator, trust in that source, package lifecycle, permission to acquire/change a Target and the deployment action itself are separate facts.

Generic acquisition of packages not already available through established Registry/environment mechanics remains outside this release. Missing required deployable supply is reported/blocked rather than silently fetched from an arbitrary location.

## Failure, resumption and atomicity

There is no generic all-or-nothing transaction across heterogeneous Deployment Targets.

- preserve previously verified target state when failure occurs before mutation where possible;
- record each Target independently;
- a multi-target deployment with mixed success is `Partial`;
- a policy-denied/manual action may return `Blocked` with the next action rather than mutating;
- re-running reconciles from observed state and avoids unnecessary redeployment; and
- platform rollback is used only where actually supported.

Release Batch atomicity applies only to visibility of coordinated Registry changes, not to later target mutations.

## Verification

UI presence, an enabled flag, Registry registration, repository publication or filesystem existence alone does not prove runtime availability.

Record desired release, publication release, installed/attached platform release and runtime-observed
release separately where exposed. Verification status is `Verified | Mismatch | Unverified`.
Assurance is `Enforced` when evidence is independent of model choice/compliance and `Advisory` when
the model materially selects, executes or reports the check.

Target-specific verification may include package/member integrity, publication/install acknowledgement, discovery, identity/version visibility, applicable required-presence checks, Migration/cheap metadata visibility, content probes, trigger behaviour and fresh-session pickup where relevant.

Producer-declared surface variation/degradation information informs what behaviour is expected on each surface; verification must not fail a surface merely for functionality explicitly declared irrelevant/unsupported there, but must fail when a required/full-conformance condition is not met.

## Artefact neutrality and manual channels

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other built deployable artefacts use the same Registry/Deployment model when their producer supplies a conforming Deployable Package/output. Their semantic owner does not become the deployment owner.

A manually replaced project Bundle is a valid representation/channel implementation where the platform lacks automation. Later automated sync/install can replace that channel without changing the Registry or desired-composition semantics.

## Boundaries

- Producer/domain owns logical artefact semantics and PackageKind-specific Build/package content.
- `AIDE_Dependencies` owns dependency/required-presence semantics.
- `AIDE_Migration` owns consumer transition semantics.
- `AIDE_Tags` owns tag content/build/query semantics; Deployment consumes Tags for selection where configured.
- Build owns semantic rendering/transformation, source/build provenance, output/package identity/integrity and composition posture.
- AI Deployment owns the Deployment Registry contract/lifecycle, desired Set selection, posture-respecting mechanical assembly, policy-aware target reconciliation/delivery, mismatch reporting and verification.
- Environment/platform configuration owns physical Registry/Target facts, access references and actual policy/authority values.
- Bootstrap owns startup discovery/surfacing, not Registry registration, deployment action or verification.

```yaml
MigrationSummary:
  CurrentVersion: v7
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

Transition:
  Version: v5
  Posture: None

Transition:
  Version: v6
  Posture: None

Transition:
  Version: v7
  Posture: None
```

No persisted consumer-state transformation is required to adopt v7. Existing fixed-composition Set
Definitions must declare their required members before relying on v7 fixed-membership resolution.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDeployment_Design_v7, AIDE_Build@v8, AIDE_Dependencies@v3, AIDE_Tags@v3
References: AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v2, AIDE_DeploymentRegistryTool@v2, AIDE_CapabilityBuild@v4
<!-- END SOURCE: AIDE_Deployment_Standard_v7.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Tool_v7.md -->
# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v7`
> **Common name:** Deploy
> **Version 7** (2026-09-03). Enforces Set membership authority, frozen-Tag use and per-Target required-presence evaluation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v7
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set Definition, its current Desired Release and selected/all configured Targets.
2. Resolve fixed required/desired members or explicitly dynamic selector-defined membership, then
   resolve exact eligible Current Deployable Package/member supply using the Set supply selector.
3. For a fixed Set, block when any required member lacks eligible supply; do not silently shrink the
   desired composition to the selector result.
4. Resolve exact PackageId/Build Target/member identities, integrity, Definition/Profile and
   source/Build provenance, Build-declared `CompositionPosture`, frozen snapshot-relative Tags,
   reach/applicability/conformance/degradation, required extensions and applicable required-presence facts.
5. Reject ordinary selection of Withdrawn package instances; surface Deprecated selected supply and its successor/replacement state where known.
6. Validate that each built output is usable under its declared posture for the required Target operation and that required extension handlers are available.
7. If a required semantic transformation/posture-compatible output has not been supplied in eligible Registry material, report a Build/material blocker; do not manufacture it from canonical source, Design history, older package, Registry metadata or observed deployed content.
8. Resolve every required Deployment Output Definition and mechanically assemble candidate Outputs
   from eligible `MemberContribution`s, treating `AssembledConsumptionArtefact`s as atomic.
9. Preserve member-level dependency/Migration/Scope/Tags facts or deterministic provenance
   references required downstream, then stamp candidate Outputs with Set release/output identity
   and resolution digest and validate all
   required Outputs together before issuing a release.
10. Compare exact provenance and final Output content with Desired Release. If changed and valid,
    assign/freeze the next `<Set>@vN`; if invalid, retain the last Desired Release. An automatic
    Registry invocation with unchanged resolution returns no release/delivery action.
11. For explicit/manual invocation, continue for Targets that are failed, blocked, mismatched or
    unverified even when the Desired Release is unchanged.
12. Read/resolve observed publication, platform-installed/attached and runtime state where possible.
13. Compare Desired Release and applicable required presence with each observed Target state,
    allowing valid external material to satisfy a requirement. Do not
    silently expand Set membership to hide a missing requirement.
14. Determine the minimum configured Delivery Actions needed and apply only policy-permitted target
    mutations; otherwise return the required manual/confirmation/external next action.
15. Verify Output, publication, platform resolution and runtime layers applicable to the Target,
    including the intrinsic release marker and behaviour probe where required.
16. Record desired/publication/platform/runtime releases, verification status/assurance and
    mismatches in per-Target Deployment State.
17. Return one Deployment Result with target action/state and overall `Complete | Partial | Blocked | Failed`.

Do not infer producer intent, package kind semantics or composition posture from payload structure. Registry/deployed state is reconciliation evidence only, not a source for semantic production.

A source/Registry locator is not authority to acquire/install. Generic acquisition of missing packages outside established Registry/environment mechanics remains outside this Tool release.

## Verify

Run the configured verification contract without intentionally changing desired composition.

Report Registry/package identity and lifecycle separately from Desired Release, publication,
installed/attached platform state, runtime-observed release/content, applicable required-presence,
declared degradation/variation and active-session pickup. Record `Enforced | Advisory` assurance.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report, as applicable:

- Deployment Set Definition revision, Desired Release and configured Targets;
- exact immutable Set release members, Output identities/integrity and resolution digest;
- resolved Registry and exact PackageIds/member identities;
- package lifecycle (`Available | Deprecated | Withdrawn`) and successor state where material;
- effective policy posture;
- source/build provenance, integrity and composition posture;
- package/member Tags used for selection;
- last observed publication, installed/attached platform and runtime target state;
- verification status, assurance, evidence and evidence time;
- required-presence, missing-package, required-extension or posture-incompatible mismatches;
- declared surface degradation/variation relevant to verification;
- failed/unverified Targets; and
- next reconciliation action.

Do not infer canonical/build provenance or composition posture from deployment status alone.

## Failure and idempotency

Re-running the same concrete desired state reconciles from observed state. A matching verified Target needs no semantic redeployment.

An automatic Registry event/trigger that resolves to the same exact Set release is a no-op for
release/delivery. An explicit Reconcile may retry/re-verify incomplete Targets of that release.

Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete. Policy-denied/unconfirmed actions must not be attempted merely because credentials/write access exist.

```yaml
MigrationSummary:
  CurrentVersion: v7
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

Transition:
  Version: v5
  Posture: None

Transition:
  Version: v6
  Posture: None

Transition:
  Version: v7
  Posture: None
```

No persisted consumer-state transformation is required to adopt v7.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7, AIDE_Dependencies@v3, AIDE_Tags@v3
References: AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v2, AIDE_DeploymentRegistryTool@v2, AIDE_Build@v8
<!-- END SOURCE: AIDE_Deployment_Tool_v7.md -->

---

<!-- BEGIN SOURCE: AIDE_DeploymentRegistry_Tool_v2.md -->
# AIDE Deployment Registry — Tool

> **Identity:** `AIDE_DeploymentRegistryTool@v2`
> **Common name:** Deployment Registry
> **Version 2** (2026-09-03). Aligns package validation with AI Deployment v7 and frozen snapshot-relative Tags.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentRegistryTool@v2
  CommonName: Deployment Registry
  PrimaryInvocation: deployment-registry
  LogicalActions: [Register, BeginBatch, ReleaseBatch, AbandonBatch, Deprecate, Withdraw, Status]
```

## Trigger and inputs

Use for publication/registration of a successfully validated Deployable Package into a configured
Deployment Registry or for Registry-owned package lifecycle/Release Batch actions.

Resolve as applicable:

- Registry identity/locator and authority;
- validated Deployable Package source, `PackageKind`, Logical Package Identity and `PackageId`;
- integrity and Build validation/provenance evidence;
- optional Release Batch identity;
- lifecycle reason/successor where Deprecate/Withdraw is requested; and
- expected package identities/validation conditions where a Batch declares them.

Do not infer a Registry destination merely from an ordinary Build output path.

## Register

1. Resolve the configured Registry and authority to change it.
2. Validate the package against `AIDE_Deployment@v7` and its PackageKind contract.
3. Verify PackageId/integrity and sufficient Build/source provenance.
4. Preserve owner-specific dependency, Migration, Scope, frozen snapshot-relative Tags,
   degradation/limitation and extension metadata plus producer freshness evidence without
   redefining their semantics or regenerating Tags.
5. If the same PackageId already exists with identical verified package state, return idempotent
   `Registered`/existing receipt.
6. If the same PackageId exists with conflicting state, fail visibly.
7. If a Release Batch is supplied, stage the package/lifecycle-current change under that open Batch
   without changing ordinary Current visibility.
8. Otherwise store the immutable package, update Current Package for the Logical Package Identity
   as authorised, emit the applicable Registry event and return the registration receipt/state.

Register does not deploy the package to a runtime Target.

## BeginBatch

1. Resolve Registry and authority.
2. Create one unique open Release Batch identity.
3. Record optional expected Logical Package Identities and other explicit release validation
   conditions.
4. Return the Batch identity/state.

Do not infer that an arbitrary series of registrations forms one Batch merely because they are close
in time.

## ReleaseBatch

1. Resolve the open Batch and all staged changes.
2. Validate all staged PackageIds/integrity and package contracts again where needed.
3. Validate any declared expected-package conditions and lifecycle/current-pointer transitions.
4. Fail without changing visible Current Registry state if the Batch is incomplete, conflicting or
   otherwise invalid.
5. Make the staged Registry Current/lifecycle changes visible as one Registry transaction using the
   strongest atomicity the Registry implementation supports; if exact atomic replacement cannot be
   guaranteed, preserve prior state on failure and report the limitation.
6. Mark the Batch Released.
7. Emit one `ReleaseBatchReleased` event plus any required compact changed-package facts for
   downstream Deployment Trigger evaluation.

ReleaseBatch creates no cross-runtime deployment transaction guarantee.

## AbandonBatch

Mark an Open Batch Abandoned and remove/ignore its staged Registry visibility changes. Do not delete
or invalidate the producer Build outputs merely because the Registry batch is abandoned.

## Deprecate

1. Resolve the exact package instance and Registry authority.
2. Mark it `Deprecated` in Registry-owned metadata.
3. Record concise reason and successor/replacement where established.
4. Preserve the immutable package payload and existing exact historical references.
5. Emit a Registry event so configured Deployment Triggers may re-evaluate affected Sets.

Deprecation does not itself remove material from runtime targets.

## Withdraw

1. Resolve the exact package instance and Registry authority.
2. Mark it `Withdrawn` and remove it from ordinary new/current resolution eligibility.
3. If it is Current, move Current to an authorised valid replacement in the same Registry
   transaction or leave the Logical Package Identity without an ordinary Current package.
4. Preserve the immutable package for historical/evidential or explicitly authorised recovery use.
5. Emit `PackageWithdrawn`/current-change state for Deployment Trigger evaluation.

Withdrawal does not directly uninstall runtime material; resulting removal is owned by normal
Deployment reconciliation.

## Status

Report, as requested:

- Registry identity and reachable/authority state where material;
- Logical Package Identity → Current Package relation;
- exact PackageId, PackageKind, integrity and lifecycle state;
- package/member Tags where supplied;
- open/released/abandoned Release Batch state;
- deprecation/withdrawal reason/successor;
- registration receipt/provenance; and
- unresolved validation/conflict conditions.

Do not claim target/runtime Deployment state from Registry state.

## Failure and idempotency

- invalid/unvalidated package → reject;
- identical re-registration → idempotent;
- PackageId collision with different content → fail visibly;
- failed Register/Release → preserve prior visible Registry state;
- repeated same-state Deprecate/Withdraw → idempotent;
- unavailable destination authority → `Blocked`, not technical `Failed` merely because credentials
  are absent/unusable;
- physical purge is not a v1 action.

A successful producer Build remains successful when Registry registration fails; report Registry
post-Build state separately and preserve the validated package for safe retry.

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
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7, AIDE_Build@v8, AIDE_Tags@v3
References: AIDeployment_Registry_Design_v2, AIDE_PublishBuildOutputTool@v1
<!-- END SOURCE: AIDE_DeploymentRegistry_Tool_v2.md -->
