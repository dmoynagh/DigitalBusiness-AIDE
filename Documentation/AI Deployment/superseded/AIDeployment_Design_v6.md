# AI Deployment — Design

> **Version 6** (2026-09-02). Closes exact Set releases, Deployment Outputs, Delivery Actions,
> Target Adapters, layered verification and the concrete AIDE Core deployment configuration.
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
outputs/actions/Targets are defined in `AIDeployment_AIDECore_Reference_v1`.

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

The current `AIDE_CapabilityBuild@v3` Capability Package is the first producer-specific `Deployable Package`. AI Deployment does not require Capabilities to re-open semantic Design or maintain a separate capability-only Deployment Manifest.

The package must expose the generic Registry acceptance envelope plus its Capability-specific composition, dependency/Migration and Build evidence. The post-Build **result** is not part of immutable package content; Registry publication returns its own receipt/state and Build reports that result separately.

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
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v8, AIDE_Dependencies@v3, AIDE_Tags@v2
References: AIDE_WorkPackage@v3, AIDE_CapabilityBuild@v3, AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v1, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v1, AIDE_DeploymentRegistryTool@v1, AIDeployment_OpenAI_Reference_v3
