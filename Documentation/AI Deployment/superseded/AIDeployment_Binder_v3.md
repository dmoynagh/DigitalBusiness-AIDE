# AI Deployment Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Version 3** (2026-08-31). Rebuilt after Build-production / Deployment mechanical-assembly boundary reconciliation.

## Binder manifest

- `AIDeployment_Index_v3.md` — sha256 `53ab2396909f`
- `AIDeployment_Design_v3.md` — sha256 `41ceaaabd5e7`
- `AIDeployment_Decisions_v3.md` — sha256 `21672cb9ba20`
- `AIDeployment_OpenAI_Reference_v2.md` — sha256 `5f86468b1e99`
- `AIDE_Deployment_Standard_v3.md` — sha256 `b344f14beb88`
- `AIDE_Deployment_Tool_v3.md` — sha256 `5d3c3ae17fec`

---

<!-- BEGIN SOURCE: AIDeployment_Index_v3.md -->
# AI Deployment — Index

> **Version 3** (2026-08-31). Registers the clarified Build-production / Deployment mechanical-assembly boundary.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic/workstream:** AI Deployment  
**Project container / master folder:** `AIDE/AI Deployment/`  
**Purpose:** Generic set-aware, policy-aware deployment of built artefacts into AI runtime surfaces.

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `AIDeployment_Index` | v3 | Index | Current |
| `AIDeployment_Design` | v3 | Design | Current |
| `AIDeployment_Decisions` | v3 | Decisions | Current |
| `AIDeployment_OpenAI_Reference` | v2 | Reference | Current empirical baseline |
| `AIDE_Deployment_Standard` | v3 | Standard | Current; identity `AIDE_Deployment@v3` |
| `AIDE_Deployment_Tool` | v3 | Tool | Current; identity `AIDE_DeploymentTool@v3` |

## Boundary

Producer/domain owns deployable artefact semantics and requirements. Dependencies owns dependency/required-presence semantics. Build performs semantic production of target-compatible contributions/packages from current authoritative inputs and may produce authorised assembled consumption artefacts. AI Deployment selects those built outputs for desired Sets, performs only target-required mechanical assembly, and owns policy-aware reconciliation, delivery, mismatch reporting and runtime verification.

Deployment Set membership does not erase upstream required presence. Environment/platform configuration remains the source of physical target facts, access references and effective target-change policy/authority values.

The dedicated GPT Project is an operational context boundary, not a semantic ownership boundary.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: Capabilities_Design_v8, Build_Design_v1, AIDE_Dependencies@v2
<!-- END SOURCE: AIDeployment_Index_v3.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Design_v3.md -->
# AI Deployment — Design

> **Version 3** (2026-08-31). Tightens the Build/Deployment production boundary so Deployment-time
> composition is explicitly mechanical target assembly of built material, with canonical/build provenance preserved.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

---

## Layer 1 — intent / system view

### Purpose

Make built deployable material available in the intended AI runtime surfaces, reconcile changes/removals and required-presence mismatches, and verify the **actual usable deployed state**.

### Premises

- Deployment starts after producer-specific design and Build.
- Deployment consumes current built outputs and declared package/manifest intent; it does not reopen the producer's Design or perform a second semantic Build.
- Observed deployed state and older Bundles/packages are reconciliation evidence, not substitute semantic production sources.
- A Deployment Set states desired target composition; it does not redefine semantic requirements declared by its members or their dependencies.
- A shared representation does not imply a shared distribution route or runtime.
- Logical target, runtime surface, representation, distribution channel, physical destination, source locator, target-change policy and observed deployment state are separate facts.
- Possessing access credentials or knowing where material can be found does not by itself authorise target mutation.
- Deployment verification means runtime-appropriate evidence, not merely “the file/install exists.”

### Boundary

Producer/domain owns the logical artefact, its semantic requirements and any producer-specific package contract.

Dependencies owns dependency/required-presence semantics. Deployment consumes those facts when they materially affect target validity; it does not redefine them through Deployment Set membership.

Build owns semantic rendering/transformation from current authoritative/canonical sources into target-compatible **contributions**, packages, and any assembled consumption artefact that is itself a Build output. Build outputs carry the provenance needed to identify the authoritative/canonical source and build/package identity.

AI Deployment owns desired Set selection, set-aware **mechanical target assembly** of already built material where a Target requires it, destination/channel resolution, policy-aware publication/install/update/remove, resumption, mismatch reporting and verification. Deployment does not independently render canonical semantics into a new target representation.

Environment/platform configuration supplies physical target facts, access and channel details, and the effective policy/authority under which the target may be changed.

Bootstrap may discover startup material and surface missing required presence. It does not install, update, remove, reconcile or verify deployed state.

### Flow

```text
producer canonical outcome
      ↓
Build
      ↓
platform contribution(s) / authorised assembled Build output
      + producer Package/Manifest + source/build provenance
      ↓
AI Deployment
      ↓
resolve Deployment Set + target config/policy
      ↓
resolve semantic required-presence facts
      ↓
compare desired + required state with observed target state
      ↓
mechanically assemble desired target artefact/state where required
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

This removes the full-vs-incremental question from generic deployment semantics: a target adapter/assembler may mechanically rebuild the target assembly from the selected built inputs or patch it incrementally, provided it does not semantically re-render those inputs and the same desired state, provenance relation and verification result are produced.

### 2. Build production is upstream; Deployment is set-aware

Build produces target-compatible contributions/packages from current authoritative/canonical semantic sources and may also produce an authorised assembled consumption artefact when that assembled representation is the Build output. A Build contribution need not be independently deployable.

Deployment selects the appropriate built members/artefacts for the Deployment Set and Target. Where the Target representation requires set-level assembly, Deployment may combine those already built inputs mechanically—for example by deterministic placement, concatenation, registration, wrapping or other representation-defined assembly that does not interpret or recreate their semantic meaning.

If the required target-compatible semantic transformation is absent from the supplied Build outputs, Deployment reports a Build/material blocker rather than deriving the missing representation from Design history, canonical source text, an older Bundle/package or observed deployed content.

### 3. Deployment-time composition is deterministic mechanical assembly and conflicts fail visibly

For each Target, Deployment resolves all desired built members/artefacts and, where necessary, mechanically assembles them according to the target representation contract. Assembly preserves member semantics and source/build provenance; it does not create a new semantic rendering authority in Deployment.

If two contributions claim incompatible ownership/identity/path/namespace or cannot coexist under the target representation, assembly fails for that Target. Deployment does not choose a winner silently or repair the conflict by rewriting member semantics.

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

A new package build of the same semantic release can still require deployment because canonical/source identity, package/build identity and runtime pickup are separate facts. Deployment status never substitutes for those upstream provenance facts.

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

When a member is no longer desired in a Set, Deployment removes it from the target composition. Where Deployment owns mechanical target assembly, this may mean reassembling the built inputs without that member; where the assembled representation is itself a Build output, Deployment requires the appropriate replacement Build output rather than semantically rebuilding it; where the member is independently installed, it may mean uninstall/removal.

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

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other canonical/deployable artefacts may participate as Deployment Set members when Build provides the target-compatible representation/contribution required by the Target. Deployment places/assembles those built forms without collapsing their distinct semantic roles or inferring missing Bootstrap meaning.

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
<!-- END SOURCE: AIDeployment_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDeployment_Decisions_v3.md -->
# AI Deployment — Decisions

> **Version 3** (2026-08-31). Adds the explicit Build-production / Deployment-assembly boundary
> and provenance rules following Build reconciliation.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

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

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v3
References: Capabilities_Design_v8, Core_System_Design_v4, AIDE_Dependencies@v2, AIDeployment_OpenAI_Reference_v2
<!-- END SOURCE: AIDeployment_Decisions_v3.md -->

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

<!-- BEGIN SOURCE: AIDE_Deployment_Standard_v3.md -->
# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v3`
> **Common name:** AI Deployment
> **Version 3** (2026-08-31). Clarifies that Deployment-time composition is mechanical assembly
> of built material and preserves upstream canonical/build provenance.
>
> **Default weight:** Requirement

## Purpose

Make built deployable material available in intended AI runtime surfaces, reconcile desired composition and applicable required presence with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes:

- built platform contribution(s) or an authorised assembled Build output;
- producer canonical/source provenance, package/build identity and integrity;
- logical deployment intent / Deployment Set membership;
- applicable semantic required-presence facts owned by the producing artefact/dependency system; and
- environment-resolved target configuration and target-change policy.

Deployment does not reopen producer Design and does not redefine upstream requirements through Deployment Set membership.

## Deployment Set and Target

A **Deployment Set** is named logical desired composition. It states which producer members should be realised together; omission from the Set does not cancel a member's semantic dependency/required-presence requirement.

A **Deployment Target** is one concrete realisation of a Set and resolves:

- platform/family;
- runtime/surface;
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

Technical access, credentials or a reachable destination do not by themselves establish permission to modify the Target.

## Reconciliation

For each Target:

1. resolve desired Set membership, target configuration and effective Deployment Policy;
2. resolve applicable required-presence facts for intended target use;
3. validate canonical/source provenance, package/contribution identity and integrity;
4. where the Target requires set-level assembly, mechanically assemble the selected built material deterministically without semantically re-rendering it;
5. fail visibly on missing target-compatible Build output or incompatible ownership/path/identity/namespace claims;
6. compare desired composition and required presence with observed deployed state;
7. surface any missing required material as a reconciliation mismatch/blocker rather than treating it as optional;
8. determine the necessary install/update/replace/remove actions;
9. apply only actions permitted by the effective Deployment Policy;
10. verify the resulting target/runtime state; and
11. persist/report Deployment Result and observed Deployment State.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

Mechanical full reassembly versus incremental patching is target implementation detail provided the same selected built inputs, provenance relation, desired state, policy boundary and verification contract are preserved. If a semantic transformation is required but is not present in the Build outputs, Deployment blocks/returns that need upstream rather than producing the representation itself.

## Production and provenance boundary

Build is upstream of Deployment. It renders/transforms current authoritative/canonical semantics into target-compatible contributions/packages and may produce an assembled consumption artefact when that artefact is itself the authorised Build output.

Deployment owns desired Set composition and target-state reconciliation. Any Deployment-time composition is mechanical assembly of already built material required by the Target representation; it must preserve member semantics and supplied source/build provenance.

Observed deployed state, an older Bundle/package, runtime verification or successful deployment status may be used as reconciliation evidence but do not become semantic production authority or substitute for canonical/build provenance.

## Source and acquisition boundary

A source/catalog locator, trust in that source, permission to acquire/change a Target, and the deployment action itself are separate facts.

Naming or discovering a source does not authorise Deployment to fetch, install or execute it.

Generic package/source acquisition is not required by this release. If required deployable material is unavailable through established environment mechanics, report the missing material/blocker. A future acquisition mechanism may be inserted before reconciliation provided it independently resolves trusted source and Deployment Policy before obtaining or applying material.

## Failure and resumption

There is no generic all-or-nothing transaction across heterogeneous targets.

- Preserve previously verified state when failure occurs before mutation where possible.
- Record each Target independently.
- A multi-target deployment with mixed success is `Partial`.
- A Target that requires an unpermitted/manual action may be reported `Blocked` with the required next action rather than mutated.
- Re-running reconciles from observed state and avoids unnecessary semantic redeployment.
- Platform rollback is used only where the target actually supports it.

## Verification

UI presence, an enabled flag, or filesystem existence alone does not prove runtime availability.
Target-specific verification may include discovery, identity/version visibility, applicable required-presence checks, content probes, trigger behaviour and new-session pickup.

## Removal

Removal is the consequence of desired-state reconciliation. A Deployment-owned mechanical assembly may be reassembled without the removed built member; an assembled representation that is itself a Build output requires the corresponding replacement Build output; an independently installed member may be uninstalled. Removal is still subject to the effective Deployment Policy.

## Artefact neutrality and manual channels

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other deployable artefacts use the same Deployment model when Build supplies the required target-compatible contribution/representation. Their semantic owner does not become the deployment owner, and Deployment does not collapse their semantic roles or infer missing Bootstrap meaning during assembly.

A manually replaced project Bundle is a valid representation/channel implementation where the platform lacks automation. Later automated sync/install can replace that channel without changing Deployment Set semantics.

## Boundaries

- Producer/domain owns logical artefact semantics and its declared requirements.
- `AIDE_Dependencies` owns dependency/required-presence semantics.
- Build owns semantic rendering/transformation into target-compatible member/contribution/package outputs and any assembled consumption artefact that is a Build output.
- AI Deployment owns desired Set selection, set-aware mechanical target assembly of those built outputs where required, policy-aware delivery/reconciliation, mismatch reporting and verification.
- Environment/platform configuration owns physical target facts, access references and actual target-change policy/authority values.
- Bootstrap owns startup discovery/surfacing, not deployment action or verification.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none
```

```yaml
Transition:
  Version: v1
  Posture: None
```

```yaml
Transition:
  Version: v2
  Posture: None
```

```yaml
Transition:
  Version: v3
  Posture: None
```

No persisted consumer-state transformation is required to adopt v3.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v3, AIDE_Dependencies@v2
References: AIDE_Build@v1
<!-- END SOURCE: AIDE_Deployment_Standard_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Tool_v3.md -->
# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v3`
> **Common name:** Deploy
> **Version 3** (2026-08-31). Clarifies mechanical target assembly, Build-output requirements and provenance handling.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v3
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve each Target's effective Deployment Policy/authority together with destination/channel facts.
3. Resolve desired members, canonical/source provenance, package/build identities, platform contributions/authorised assembled Build outputs and applicable required-presence facts.
4. Validate integrity and that any required Deployment-time composition can be performed as deterministic mechanical assembly of the supplied built material.
5. If the Target requires a semantic transformation or assembled Build output that has not been supplied/resolved, report a Build/material blocker; do not manufacture it from canonical source, Design history, an older Bundle/package or observed deployed content.
6. Read/resolve observed target state where possible.
7. Compare desired composition and applicable required presence with observed state.
8. If required material is absent, report a reconciliation mismatch/blocker; do not treat Set omission as removal of the requirement and do not silently expand Set membership.
9. Mechanically assemble the selected built material where the Target representation requires set-level assembly, preserving supplied member semantics and provenance.
10. Determine the minimum target actions needed to reach valid desired state.
11. Apply only target mutations permitted by Deployment Policy; otherwise return the required confirmation/manual/external next action without mutating.
12. Run the Target's verification contract, including required-presence checks where relevant.
13. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent from payload structure, semantically rewrite supplied contributions, or silently choose between conflicting contributions. Observed target content is reconciliation evidence only, not a source for semantic production.

A source/catalog locator is not authority to fetch or install. Generic acquisition of missing packages/material is outside this Tool release unless an established environment mechanism explicitly supplies that operation under resolved trust and Deployment Policy.

## Verify

Run the configured verification contract without intentionally changing desired composition.
Report installed/published state separately from runtime-content availability, applicable required-presence state and active-session pickup where those can differ.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report desired Set composition, configured Targets, effective policy posture where material, resolved source/build provenance where supplied, last observed/verified state, required-presence or missing-Build-output mismatches, failed/unverified Targets and the next reconciliation action. Do not infer canonical/build provenance from deployment status alone.

Where target mutation is not currently permitted, distinguish “action required” from technical deployment failure.

## Failure and idempotency

Re-running the same desired state reconciles from observed state. A matching verified Target needs no semantic redeployment. Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete.

Policy-denied/unconfirmed actions must not be attempted merely because credentials or write access exist.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none
```

```yaml
Transition:
  Version: v1
  Posture: None
```

```yaml
Transition:
  Version: v2
  Posture: None
```

```yaml
Transition:
  Version: v3
  Posture: None
```

No persisted consumer-state transformation is required to adopt v3.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Deployment@v3
References: AIDE_Build@v1, AIDE_Dependencies@v2
<!-- END SOURCE: AIDE_Deployment_Tool_v3.md -->
