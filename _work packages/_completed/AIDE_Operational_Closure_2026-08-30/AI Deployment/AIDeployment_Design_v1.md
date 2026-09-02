# AI Deployment — Design

> **Version 1** (2026-08-30). First confirmed design for generic AI-platform Deployment, promoted out of Capabilities.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## Layer 1 — intent / system view

### Purpose

Make built deployable material available in the intended AI runtime surfaces, reconcile changes/removals, and verify the **actual usable deployed state**.

### Premises

- Deployment starts after producer-specific design and Build.
- Deployment consumes declared package/manifest intent; it does not reopen the producer's Design.
- A shared representation does not imply a shared distribution route or runtime.
- Logical target, runtime surface, representation, distribution channel, physical destination and observed deployment state are separate facts.
- Deployment verification means runtime-appropriate evidence, not merely “the file/install exists.”

### Boundary

Producer/domain owns the logical artefact and any producer-specific package contract.

Build owns target-compatible **contributions** for the selected representation.

AI Deployment owns set-aware composition, destination/channel resolution, publication/install/update/remove, resumption and verification.

Environment/platform configuration supplies physical target facts, access and channel details.

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
resolve Deployment Set + target config
      ↓
compose desired target artefact/state
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

### Deployment Target

One concrete runtime/surface realisation of a Deployment Set. A Target resolves at least:

- platform/family;
- runtime/surface;
- representation;
- distribution channel;
- physical destination/account/workspace where applicable; and
- verification/refresh requirements.

One logical Deployment Set may therefore have several Targets even inside one provider family.

### Representation

The target-compatible shape being deployed, for example a plugin, skill collection, project bundle, instruction file or another supported platform artefact.

### Distribution channel

How that representation reaches the target: local marketplace, hosted directory/publication, project-file upload/sync, repository, account/workspace install, filesystem path, or another supported route.

Representation and channel are independent dimensions.

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
        Refresh: <where required>
        Verification: <required checks/probes>
```

Credentials/secrets are referenced through environment access mechanisms and are not embedded in a producer package/manifest or normal governed documentation.

### Deployment State

A factual record of what has actually been verified for one Target. It distinguishes at least:

- desired Set composition/revision;
- installed/published package or assembled artefact identity;
- member/capability identities and releases where exposed;
- representation/channel/surface;
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
6. MigrationSummary/cheap metadata visibility where expected;
7. runtime content probe;
8. implicit/explicit trigger behaviour where applicable; and
9. update/session pickup behaviour where the runtime may pin an old build.

UI presence or “enabled” state is not sufficient where executable runtime content is required.

### 7. Removal follows desired composition

When a member is no longer desired in a Set, Deployment removes it from the target composition. Where a target representation is assembled, this may mean rebuilding the assembled artefact without that member; where the member is independently installed, it may mean uninstall/removal.

Explicit producer `Remove`/`Replace` intent remains useful for identity transitions and retirement, but the stable semantic goal is the resulting desired Set.

---

## Ownership and project-container boundary

AI Deployment is no longer owned by Capabilities. Its dedicated master folder/GPT Project is
`AIDE/AI Deployment/`.

Architecturally it remains an environment/platform concern: it consumes target configuration,
credentials/access references, surface/channel facts and observed runtime state. The dedicated
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
- platform-specific refresh/session pickup mechanics not yet observed.

These populate target adapters/config; they do not change the generic model unless evidence exposes a missing concept.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Capabilities_Design_v8, Build_Design_v1
References: AIDE_WorkPackage@v1, AIDeployment_OpenAI_Reference_v1
