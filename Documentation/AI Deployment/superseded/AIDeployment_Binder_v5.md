# AI Deployment Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 5** (2026-09-02). Adds the Deployment Registry/Deployable Package boundary, immutable Registry lifecycle, Release Batches and the first AI-Deployment-owned Registry Tool.

This Binder is a current-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `AIDeployment_Index_v5.md` — sha256 `d3018d29e5b4`
- `AIDeployment_Design_v5.md` — sha256 `5a9bbfae734c`
- `AIDeployment_Decisions_v5.md` — sha256 `94d7ce0c6df7`
- `AIDeployment_Registry_Design_v1.md` — sha256 `e7d610036a86`
- `AIDeployment_OpenAI_Reference_v2.md` — sha256 `5f86468b1e99`
- `AIDE_Deployment_Standard_v5.md` — sha256 `e5f2237c81f4`
- `AIDE_Deployment_Tool_v5.md` — sha256 `359f85d984c3`
- `AIDE_DeploymentRegistry_Tool_v1.md` — sha256 `f8119d821b3a`

---

<!-- BEGIN SOURCE: AIDeployment_Index_v5.md -->
# AI Deployment — Index

> **Version 5** (2026-09-02). Adds the Deployment Registry/Deployable Package boundary and first Registry Tool while retaining the current Deployment Set/Target reconciliation model for later refinement.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic Registry-backed, set-aware, policy-aware deployment of validated built artefacts into AI runtime surfaces.

## Contents

- **AI Deployment** — desired-state selection, target reconciliation/delivery and runtime verification.  
  `{standard: AIDE_Deployment@v5}`
- **Deployment Registry** — validated Deployable Package registration, immutable package-instance lifecycle and Release Batches.  
  `{tool: AIDE_DeploymentRegistryTool@v1}`

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v5 | Index | Current |
| `AIDeployment_Design` | v5 | Design | Current |
| `AIDeployment_Decisions` | v5 | Decisions | Current |
| `AIDeployment_Registry_Design` | v1 | Design | Current |
| `AIDeployment_OpenAI_Reference` | v2 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v5 | Standard | Current; identity `AIDE_Deployment@v5` |
| `AIDE_Deployment_Tool` | v5 | Tool | Current; identity `AIDE_DeploymentTool@v5` |
| `AIDE_DeploymentRegistry_Tool` | v1 | Tool | Current; identity `AIDE_DeploymentRegistryTool@v1` |

## Current boundary

Producer/domain owns deployable artefact semantics and PackageKind-specific Build/package content. Build/specialised producer Build produces validated packages and supplies source/build provenance, concrete PackageId/integrity and Build-owned composition posture.

AI Deployment owns the **Deployment Registry** contract and lifecycle. `Deployable Package` is the generic Registry unit; `Capability Package` is the first specialised kind. Registered PackageIds are immutable; Current/Available/Deprecated/Withdrawn/Release Batch state is Registry-owned metadata.

Deployment Set membership does not erase upstream required presence. Deployment may mechanically assemble eligible `MemberContribution` outputs, treats an `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary, and owns policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Environment/platform configuration remains the source of physical Registry/Target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

## Current design status

The Build→Registry seam is defined in v5. The next active design layer will finalise Deployment Set Definition selectors, exact resolved-set state, deployment output/package definitions, Delivery Actions and trigger-to-Set resolution. Those details are deliberately not frozen by the Registry change package.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v5, AIDE_Build@v6
References: AIDeployment_Registry_Design_v1, AIDE_DeploymentRegistryTool@v1, AIDE_CapabilityBuild@v1, AIDE_Dependencies@v3, AIDE_Tags@v2
<!-- END SOURCE: AIDeployment_Index_v5.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Design_v5.md -->
# AI Deployment — Design

> **Version 5** (2026-09-02). Adds the Deployment Registry as the explicit validated-built-supply boundary,
> defines Deployable Package lifecycle/Release Batches, and reconciles the design to Build v6 and the
> current Capability Package producer contract.
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
compare desired + required state with observed target state
      ↓
mechanically assemble eligible MemberContribution outputs where required
      ↓
policy permits target mutation?
      ↓
publish/install/update/remove
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

The Registry does not mutate package bytes to represent lifecycle state and does not itself deploy anything to runtime targets. Detailed contract: `AIDeployment_Registry_Design_v1`.

### Release Batch

A **Release Batch** groups package registrations/lifecycle changes that must become visible to automatic downstream resolution together. Packages may be validated/staged while the Batch is Open; explicit Release makes the staged Registry changes visible together and emits one release event.

This is an atomic **Registry visibility** boundary, not a promise of atomic deployment across heterogeneous runtime Targets.

### Deployment Trigger

A **Deployment Trigger** maps Registry changes or explicit/manual invocation to re-evaluation of one or more Deployment Set Definitions. A trigger means the desired concrete Set may have changed; it does not require blind re-delivery. If resolution is unchanged, no target action is needed.

### Deployment Set

A named logical **desired composition**. It groups the producer members that should be realised together for one or more configured targets.

The Set is semantic/logical. It does not itself mean plugin, bundle, repository, account or path.

Set membership is not the owner of a member's semantic dependencies or required-presence rules. Omitting a required dependency from a Set does not make that dependency optional. A Set is therefore not a replacement dependency graph or an automatic dependency-closure mechanism.

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

A factual record of what has actually been verified for one Target. It distinguishes at least:

- desired Set composition/revision;
- selected/installed Build-output or package identity, integrity relation and composition posture where exposed;
- member/capability identities and releases where exposed;
- representation/channel/surface;
- required-presence mismatches or blockers relevant to the Target;
- verification status and evidence time;
- runtime content availability; and
- session pickup state where the platform pins active sessions to an older build.

Installed state and active-session state may differ.

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

For each Target, Deployment resolves all desired Build outputs together with their source/build provenance, identity/integrity and Build-declared composition posture. Where necessary, it mechanically assembles eligible `MemberContribution` outputs according to the target representation contract while treating each `AssembledConsumptionArtefact` as atomic at its semantic/member-composition boundary. Assembly preserves semantics and provenance; it does not create a new semantic rendering authority in Deployment.

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

Before declaring a Target valid for intended use, Deployment resolves required-presence facts that apply to the desired members under the owning dependency semantics.

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

---

## Ownership and project-container boundary

AI Deployment is no longer owned by Capabilities. Its dedicated master folder/GPT Project is
`AIDE/AI Deployment/`.

Architecturally it remains an environment/platform concern: it consumes target configuration,
credentials/access references, target-change policy, surface/channel facts and observed runtime state. The dedicated
project container is an operational context boundary, not evidence that deployment semantics
belong to Capabilities or to a producer domain.

Capabilities retains capability-specific production, PackageKind semantics and any producer-owned post-Build intent. AI Deployment owns Deployment Set selection/composition semantics.

## Producer-package compatibility

The current `AIDE_CapabilityBuild@v1` Capability Package is the first producer-specific `Deployable Package`. AI Deployment does not require Capabilities to re-open semantic Design or maintain a separate capability-only Deployment Manifest.

The package must expose the generic Registry acceptance envelope plus its Capability-specific composition, dependency/Migration and Build evidence. The post-Build **result** is not part of immutable package content; Registry publication returns its own receipt/state and Build reports that result separately.

Where later package kinds need owner-specific metadata, use preserved/typed extension information rather than teaching generic Deployment the producer's semantics.

## Next design layer intentionally not closed by v5

Registry v1 closes the Build→Registry seam only. The following confirmed working concepts will be finalised in the next Deployment layer rather than over-specified here:

- Deployment Set Definition selectors and exact resolved-set revision/lock semantics;
- one or more deployment package/output definitions per Set;
- configured Delivery Actions and manual delivery invocation;
- detailed Registry-event → Set trigger matching; and
- target-specific package assembly/adapters.

Build Target Profiles/Definitions and surface/degradation production are upstream producer/platform concerns; Deployment consumes their built results but does not own that model.

## Open empirical items — not architecture blockers

- hosted/public/account-synchronised OpenAI plugin deployment into ChatGPT runtime;
- broader Claude and other provider channel specifics;
- exact platform-specific composition rules for multi-member artefacts;
- platform-specific refresh/session pickup mechanics not yet observed;
- general trusted package/catalog acquisition infrastructure and its concrete source-trust model.

These populate target adapters/config or future acquisition support; they do not change the generic model unless evidence exposes a missing concept.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v6, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDE_WorkPackage@v3, AIDE_CapabilityBuild@v1, AIDeployment_Registry_Design_v1, AIDE_DeploymentRegistryTool@v1, AIDeployment_OpenAI_Reference_v2
<!-- END SOURCE: AIDeployment_Design_v5.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Decisions_v5.md -->
# AI Deployment — Decisions

> **Version 5** (2026-09-02). Adds the Deployment Registry, generic Deployable Package, immutable package lifecycle and Release Batch decisions.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

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

**Reason.** Tags provide a simple reusable way to express groups such as `AIDE_Core` without embedding every producer identity in Deployment Set definitions.

**Boundary.** Tags are classification/selection only. They do not replace Dependencies, Scope, Build-target compatibility, Migration posture or Deployment Policy.

## D27 — Post-Build result is not immutable package content

**Decision.** A producer package may carry the nominated post-Build request/intent, but the actual Registry post-Build **result** is external state returned by the Registry action and Build Outcome; it is not written back into the immutable PackageId payload.

**Reason.** Registry registration occurs after successful package validation. Requiring its result inside the package would force mutation after the package's identity/integrity was established and conflicts with Build v6's explicit separation of production and post-Build result.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDeployment_Design_v5, AIDE_Build@v6
References: AIDeployment_Registry_Design_v1, AIDE_DeploymentRegistryTool@v1, AIDE_CapabilityBuild@v1, AIDE_Dependencies@v3, AIDE_Tags@v2, AIDeployment_OpenAI_Reference_v2
<!-- END SOURCE: AIDeployment_Decisions_v5.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Registry_Design_v1.md -->
# AI Deployment Registry — Design

> **Version 1** (2026-09-02). Defines the first AI-Deployment-owned Registry contract for
> validated Deployable Packages, immutable package instances, lifecycle state and Release Batches.
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
receiving Deployment process resolves the affected Set and compares the concrete result with its
prior resolved/deployed state. If nothing material changed, no Deployment Package/delivery action is
required.

Detailed Deployment Set selectors, resolved-set revisions, output definitions and Delivery Actions
remain the next design layer and are not fixed by this Registry Design.

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
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v6, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDeployment_Design_v5, AIDE_CapabilityBuild@v1, AIDE_PublishBuildOutputTool@v1
<!-- END SOURCE: AIDeployment_Registry_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDeployment_OpenAI_Reference_v2.md -->
# AI Deployment OpenAI — Reference

> **Version 2** (2026-08-31). Reissues the unchanged empirical OpenAI baseline against the current
> AI Deployment Design after the v2 boundary reconciliation.
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

## Evidence discipline

A reconstructed answer, prior reported probe value, project file read, or filesystem read is not
accepted as proof that a runtime executed the deployed capability. Verification should use a
fresh, target-appropriate runtime probe where execution availability is the claim.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v2
References: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING
<!-- END SOURCE: AIDeployment_OpenAI_Reference_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Standard_v5.md -->
# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v5`
> **Common name:** AI Deployment
> **Version 5** (2026-09-02). Adds the Deployment Registry/Deployable Package boundary,
> immutable Registry lifecycle and Release Batches while retaining v4 desired-state reconciliation.
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

Physical purge is retention maintenance and is not an automatic v5 Deployment lifecycle action.

Use `AIDE_DeploymentRegistryTool` for Register, Release Batch and Registry lifecycle actions. Generic ordinary Build publication does not establish Registry state.

## Tags

Deployable Packages and individual built target/member outputs may carry `AIDE_Tags` values.

For Deployment selection, the effective Tags for a built target/member are the union of Package Tags and that target/member's Tags. Use `AIDE_Tags` Boolean query semantics; satisfy applicable freshness requirements before relying on generated Tags.

Tags are classification/selection only. They do not replace semantic Dependencies, Scope, Build-target compatibility, Migration posture or Deployment Policy.

## Release Batch and triggers

A Release Batch may stage several package registrations/lifecycle changes until an explicit Release operation validates and exposes them together.

Batch Release is an atomic **Registry visibility** boundary only; it does not claim an all-or-nothing transaction across heterogeneous runtime Targets.

Registry events may cause configured Deployment Triggers to re-evaluate affected Deployment Set Definitions. Re-evaluation is idempotent: if the concrete desired result is unchanged, no deployment package/delivery mutation is required.

Detailed Set selectors/output definitions/Delivery Actions remain governed by the current Deployment Set configuration and may be refined independently of this Registry contract.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition. It states which eligible built members should be realised together; omission from the Set does not cancel a member's semantic dependency/required-presence requirement.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family and runtime/surface;
- representation;
- distribution channel;
- destination/account/workspace reference where applicable;
- effective target-change policy/authority;
- refresh/session-pickup behaviour where relevant; and
- verification requirements.

Surface, representation, channel and target-change policy are independent facts.

## Deployment Policy

Before mutating a Target, resolve the effective environment/target policy that determines whether and under what conditions the change may be applied.

Policy may permit automatic action, require confirmation/external execution, or otherwise constrain install/update/remove/acquisition behaviour. The exact policy values are environment configuration; this Standard owns only the rule that Deployment must honour them.

Technical access, credentials, Registry availability or a reachable destination do not by themselves establish permission to modify the Target.

## Reconciliation

For each requested Set/Target:

1. resolve the applicable Deployment Set, selected Registry supply and configured Target/Policy;
2. resolve exact PackageId/member/build-output identity and verify package/member integrity/provenance;
3. reject ordinary selection of Withdrawn packages and surface Deprecated selection where no suitable non-deprecated result replaces it;
4. resolve applicable semantic required-presence facts for intended target use;
5. validate Build-declared composition posture and required package-kind extensions/handlers;
6. where the Target requires set-level assembly, mechanically assemble eligible `MemberContribution` outputs deterministically without semantically re-rendering them;
7. treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary; if that composition must change, require the corresponding replacement Build output;
8. fail visibly on missing posture-compatible Build output, unresolved mandatory extension, or incompatible ownership/path/identity/namespace/posture claims;
9. read/resolve observed target state where possible;
10. compare desired composition and applicable required presence with observed deployed state;
11. surface missing required material as a mismatch/blocker rather than making Set omission redefine the requirement;
12. determine the minimum install/update/replace/remove actions needed;
13. apply only actions permitted by Deployment Policy;
14. run the Target verification contract; and
15. persist/report per-Target Deployment Result and observed Deployment State.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

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
  CurrentVersion: v5
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
```

No persisted consumer-state transformation is required to adopt v5.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDeployment_Design_v5, AIDE_Build@v6, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDeployment_Registry_Design_v1, AIDE_DeploymentRegistryTool@v1, AIDE_CapabilityBuild@v1
<!-- END SOURCE: AIDE_Deployment_Standard_v5.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Tool_v5.md -->
# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v5`
> **Common name:** Deploy
> **Version 5** (2026-09-02). Resolves deployable supply through the Deployment Registry while retaining v4 posture-aware reconciliation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v5
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve the configured Deployment Registry and the exact eligible Deployable Package/member supply required by the Set.
3. Resolve each Target's effective Deployment Policy/authority together with destination/channel facts.
4. Resolve exact PackageId/member identities, integrity, authoritative/canonical source/build provenance, Build-declared `CompositionPosture`, package/member Tags where selection uses them, required package-kind extensions, and applicable required-presence facts.
5. Reject ordinary selection of Withdrawn package instances; surface Deprecated selected supply and its successor/replacement state where known.
6. Validate that each built output is usable under its declared posture for the required Target operation and that required extension handlers are available.
7. If a required semantic transformation/posture-compatible output has not been supplied in eligible Registry material, report a Build/material blocker; do not manufacture it from canonical source, Design history, older package, Registry metadata or observed deployed content.
8. Read/resolve observed target state where possible.
9. Compare desired composition and applicable required presence with observed state.
10. If required material is absent, report a reconciliation mismatch/blocker; do not treat Set omission as removal of the requirement and do not silently expand Set membership.
11. Mechanically assemble eligible `MemberContribution` outputs where the Target representation requires set-level assembly, preserving supplied semantics/provenance. Treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary.
12. If desired reconciliation requires changing the internal semantic/member composition of an `AssembledConsumptionArtefact`, require the corresponding replacement Build output rather than decomposing/rebuilding it.
13. Determine the minimum target actions needed to reach valid desired state.
14. Apply only target mutations permitted by Deployment Policy; otherwise return the required confirmation/manual/external next action without mutating.
15. Run the Target verification contract, using producer-declared surface variation/degradation information to determine the expected applicable behaviour and including required-presence checks where relevant.
16. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent, package kind semantics or composition posture from payload structure. Registry/deployed state is reconciliation evidence only, not a source for semantic production.

A source/Registry locator is not authority to acquire/install. Generic acquisition of missing packages outside established Registry/environment mechanics remains outside this Tool release.

## Verify

Run the configured verification contract without intentionally changing desired composition.

Report Registry/package identity and lifecycle separately from destination publication/install state, runtime-content availability, applicable required-presence state, declared degradation/variation and active-session pickup where those can differ.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report, as applicable:

- desired Deployment Set composition and configured Targets;
- resolved Registry and exact PackageIds/member identities;
- package lifecycle (`Available | Deprecated | Withdrawn`) and successor state where material;
- effective policy posture;
- source/build provenance, integrity and composition posture;
- package/member Tags used for selection;
- last observed/verified target state;
- required-presence, missing-package, required-extension or posture-incompatible mismatches;
- declared surface degradation/variation relevant to verification;
- failed/unverified Targets; and
- next reconciliation action.

Do not infer canonical/build provenance or composition posture from deployment status alone.

## Failure and idempotency

Re-running the same concrete desired state reconciles from observed state. A matching verified Target needs no semantic redeployment.

A Registry event/trigger that resolves to the same concrete desired package/member set is a no-op for target mutation.

Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete. Policy-denied/unconfirmed actions must not be attempted merely because credentials/write access exist.

```yaml
MigrationSummary:
  CurrentVersion: v5
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
```

No persisted consumer-state transformation is required to adopt v5.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v5, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDE_DeploymentRegistryTool@v1, AIDE_Build@v6
<!-- END SOURCE: AIDE_Deployment_Tool_v5.md -->

---

<!-- BEGIN SOURCE: AIDE_DeploymentRegistry_Tool_v1.md -->
# AIDE Deployment Registry — Tool

> **Identity:** `AIDE_DeploymentRegistryTool@v1`
> **Common name:** Deployment Registry
> **Version 1** (2026-09-02). First AI-Deployment-owned package registration, lifecycle and Release Batch Tool.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentRegistryTool@v1
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
2. Validate the package against `AIDE_Deployment@v5` and its PackageKind contract.
3. Verify PackageId/integrity and sufficient Build/source provenance.
4. Preserve owner-specific dependency, Migration, Tags, degradation/limitation and extension
   metadata without redefining their semantics.
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
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v5, AIDE_Build@v6, AIDE_Tags@v2
References: AIDeployment_Registry_Design_v1, AIDE_PublishBuildOutputTool@v1
<!-- END SOURCE: AIDE_DeploymentRegistry_Tool_v1.md -->

---

