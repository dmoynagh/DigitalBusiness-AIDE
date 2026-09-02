# AI Deployment — Design

> **Version 2** (2026-08-31). Clarifies required-presence reconciliation, target mutation policy,
> source/authority separation, Bootstrap artefact participation, and the interim manual Bundle route.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

---

## Layer 1 — intent / system view

### Purpose

Make built deployable material available in the intended AI runtime surfaces, reconcile changes/removals and required-presence mismatches, and verify the **actual usable deployed state**.

### Premises

- Deployment starts after producer-specific design and Build.
- Deployment consumes declared package/manifest intent; it does not reopen the producer's Design.
- A Deployment Set states desired target composition; it does not redefine semantic requirements declared by its members or their dependencies.
- A shared representation does not imply a shared distribution route or runtime.
- Logical target, runtime surface, representation, distribution channel, physical destination, source locator, target-change policy and observed deployment state are separate facts.
- Possessing access credentials or knowing where material can be found does not by itself authorise target mutation.
- Deployment verification means runtime-appropriate evidence, not merely “the file/install exists.”

### Boundary

Producer/domain owns the logical artefact, its semantic requirements and any producer-specific package contract.

Dependencies owns dependency/required-presence semantics. Deployment consumes those facts when they materially affect target validity; it does not redefine them through Deployment Set membership.

Build owns target-compatible **contributions** for the selected representation.

AI Deployment owns set-aware composition, destination/channel resolution, policy-aware publication/install/update/remove, resumption, mismatch reporting and verification.

Environment/platform configuration supplies physical target facts, access and channel details, and the effective policy/authority under which the target may be changed.

Bootstrap may discover startup material and surface missing required presence. It does not install, update, remove, reconcile or verify deployed state.

### Flow

```text
producer canonical outcome
      ↓
Build
      ↓
platform contribution(s)
      + producer Package/Manifest
      ↓
AI Deployment
      ↓
resolve Deployment Set + target config/policy
      ↓
resolve semantic required-presence facts
      ↓
compare desired + required state with observed target state
      ↓
compose desired target artefact/state
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
- installed/published package or assembled artefact identity;
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

This removes the full-vs-incremental question from generic semantics: a target adapter/composer may rebuild fully or patch incrementally, provided the same desired state and verification result are produced.

### 2. Build is capability/member-local; Deployment is set-aware

Build produces contributions for the individual producer/package. Deployment may combine contributions from many packages into a single target representation.

A Build contribution need not be independently deployable.

### 3. Composition is deterministic and conflicts fail visibly

For each Target, Deployment resolves all desired members and composes them according to the target representation contract.

If two contributions claim incompatible ownership/identity/path/namespace or cannot coexist under the target representation, composition fails for that Target. Deployment does not choose a winner silently.

### 4. No universal cross-target atomicity

Heterogeneous AI platforms do not provide a common transaction boundary. Generic Deployment therefore does not claim all-or-nothing atomicity across Targets.

The safe default is:

- validate/compose before publication where possible;
- preserve previously verified state when failure occurs before target mutation;
- record each Target independently;
- stop dependent target actions when their prerequisites fail; and
- use platform rollback only when the target contract actually supports it.

A partially completed multi-target deployment returns `Partial`, never false `Complete`.

### 5. Resumption is target-state reconciliation

Re-running the same desired Set is idempotent where the target mechanics allow it. Already verified matching Targets require no semantic redeployment. Failed/unverified Targets are retried from the observed state.

A new package build of the same semantic release can still require deployment because package/build identity and runtime pickup are separate facts.

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

When a member is no longer desired in a Set, Deployment removes it from the target composition. Where a target representation is assembled, this may mean rebuilding the assembled artefact without that member; where the member is independently installed, it may mean uninstall/removal.

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

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other canonical/deployable artefacts may participate as Deployment Set members when Build provides the target-compatible representation/contribution required by the Target.

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

---

## Ownership and project-container boundary

AI Deployment is no longer owned by Capabilities. Its dedicated master folder/GPT Project is
`AIDE/AI Deployment/`.

Architecturally it remains an environment/platform concern: it consumes target configuration,
credentials/access references, target-change policy, surface/channel facts and observed runtime state. The dedicated
project container is an operational context boundary, not evidence that deployment semantics
belong to Capabilities or to a producer domain.

Capabilities retains capability-specific production, Package and deployment-intent semantics.

## Producer-manifest compatibility

The current Capability Manifest can be consumed as producer-specific input. A generic Deployment implementation can normalise its `Capability` identity to an opaque Set member identity internally.

If ownership is promoted, the cleaner later schema is a generic `Artifact/Member` identity rather than a capability-named field; that producer-contract migration should be done once during the ownership move rather than by adding another permanent adapter layer.

## Open empirical items — not architecture blockers

- hosted/public/account-synchronised OpenAI plugin deployment into ChatGPT runtime;
- broader Claude and other provider channel specifics;
- exact platform-specific composition rules for multi-member artefacts;
- platform-specific refresh/session pickup mechanics not yet observed;
- general trusted package/catalog acquisition infrastructure and its concrete source-trust model.

These populate target adapters/config or future acquisition support; they do not change the generic model unless evidence exposes a missing concept.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Capabilities_Design_v8, Build_Design_v1
References: AIDE_WorkPackage@v1, AIDE_Dependencies@v2, AIDeployment_OpenAI_Reference_v2
