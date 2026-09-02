# AI Deployment Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.

## Binder manifest

- `AIDeployment_Index_v1.md` — sha256 `008e5de63ce7`
- `AIDeployment_Design_v1.md` — sha256 `5a6700deb844`
- `AIDeployment_Decisions_v1.md` — sha256 `70acec24a82d`
- `AIDeployment_OpenAI_Reference_v1.md` — sha256 `c5055e7c97a0`
- `AIDE_Deployment_Standard_v1.md` — sha256 `f35249ba5c63`
- `AIDE_Deployment_Tool_v1.md` — sha256 `661c64f55cb1`

---

<!-- BEGIN SOURCE: AIDeployment_Index_v1.md -->
# AI Deployment — Index

> **Version 1** (2026-08-30). Registers AI Deployment after promotion out of Capabilities.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic set-aware deployment of built artefacts into AI runtime surfaces.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v1 | Index | Current |
| `AIDeployment_Design` | v1 | Design | Current |
| `AIDeployment_Decisions` | v1 | Decisions | Current |
| `AIDeployment_OpenAI_Reference` | v1 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v1 | Standard | Current; identity `AIDE_Deployment@v1` |
| `AIDE_Deployment_Tool` | v1 | Tool | Current; identity `AIDE_DeploymentTool@v1` |

## Boundary

Capabilities produces capability-local package/build material and logical deployment intent.
Build produces target-compatible contributions. AI Deployment performs set-aware reconciliation,
delivery and runtime verification.

The dedicated GPT Project is an operational context boundary. Environment/platform configuration
remains the source of physical target facts and access references.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Capabilities_Design_v8, Build_Design_v1
<!-- END SOURCE: AIDeployment_Index_v1.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Design_v1.md -->
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
<!-- END SOURCE: AIDeployment_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Decisions_v1.md -->
# AI Deployment — Decisions

> **Version 1** (2026-08-30). Records the confirmed generic AI Deployment model and its promotion out of Capabilities.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

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

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v1
References: Capabilities_Design_v8, Core_System_Design_v4, AIDeployment_OpenAI_Reference_v1
<!-- END SOURCE: AIDeployment_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: AIDeployment_OpenAI_Reference_v1.md -->
# AI Deployment OpenAI — Reference

> **Version 1** (2026-08-30). Consolidates the empirical OpenAI deployment evidence used to
> establish the initial AI Deployment target model.

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
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v1
References: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING
<!-- END SOURCE: AIDeployment_OpenAI_Reference_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Standard_v1.md -->
# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v1`
> **Common name:** AI Deployment
> **Version 1** (2026-08-30). First published deployment contract for reconciling deployable
> artefacts into verified AI runtime targets.

## Purpose

Make built deployable material available in intended AI runtime surfaces, reconcile desired
composition with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes:

- built platform contribution(s) or assembled deployable material;
- producer package/build identity and integrity;
- logical deployment intent / Deployment Set membership; and
- environment-resolved target configuration.

Deployment does not reopen producer Design.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family;
- runtime/surface;
- representation;
- distribution channel;
- destination/account/workspace reference where applicable;
- refresh/session-pickup behaviour where relevant; and
- verification requirements.

Surface, representation and channel are independent facts.

## Reconciliation

For each Target:

1. resolve desired Set membership and target configuration;
2. validate package/contribution identity and integrity;
3. compose the target representation deterministically;
4. fail visibly on incompatible ownership/path/identity/namespace claims;
5. compare desired state with observed deployed state;
6. perform the necessary install/update/replace/remove actions;
7. verify the resulting target/runtime state; and
8. persist/report Deployment Result and observed Deployment State.

Full rebuild versus incremental patching is target implementation detail provided the same
desired state and verification contract are preserved.

## Failure and resumption

There is no generic all-or-nothing transaction across heterogeneous targets.

- Preserve previously verified state when failure occurs before mutation where possible.
- Record each Target independently.
- A multi-target deployment with mixed success is `Partial`.
- Re-running reconciles from observed state and avoids unnecessary semantic redeployment.
- Platform rollback is used only where the target actually supports it.

## Verification

UI presence, an enabled flag, or filesystem existence alone does not prove runtime availability.
Target-specific verification may include discovery, identity/version visibility, content probes,
trigger behaviour and new-session pickup.

## Removal

Removal is the consequence of desired-state reconciliation. An assembled representation may be
rebuilt without the removed member; an independently installed member may be uninstalled.

## Boundaries

- Producer/domain owns logical artefact semantics.
- Build owns target-compatible member/contribution production.
- AI Deployment owns set-aware composition, delivery/reconciliation and verification.
- Environment/platform configuration owns physical target facts and access references.

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
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v1, AIDE_Dependencies@v2
References: AIDE_Build@v1
<!-- END SOURCE: AIDE_Deployment_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Tool_v1.md -->
# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v1`
> **Common name:** Deploy
> **Version 1** (2026-08-30). Canonical Tool for target-state deployment reconciliation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v1
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve desired members, package/build identities and platform contributions.
3. Validate integrity and deterministic composability.
4. Read/resolve observed target state where possible.
5. Determine the minimum target actions needed to reach desired state.
6. Apply target actions through the available distribution channel.
7. Run the Target's verification contract.
8. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent from payload structure and do not silently choose between conflicting
contributions.

## Verify

Run the configured verification contract without intentionally changing desired composition.
Report installed/published state separately from runtime-content availability and active-session
pickup where those can differ.

## Status

Report desired Set composition, configured Targets, last observed/verified state, mismatches,
failed/unverified Targets and the next reconciliation action.

## Failure and idempotency

Re-running the same desired state reconciles from observed state. A matching verified Target needs
no semantic redeployment. Failure on one Target does not falsely mark other successful Targets
failed or the whole deployment Complete.

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
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Deployment@v1
References: AIDE_Build@v1
<!-- END SOURCE: AIDE_Deployment_Tool_v1.md -->

---
