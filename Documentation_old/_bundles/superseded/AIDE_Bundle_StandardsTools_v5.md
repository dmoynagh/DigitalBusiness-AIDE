# AIDE Standards & Tools Bundle
> **Generated Bundle — do not edit directly.**
> **Version 5** (2026-08-31). Foundation-consolidation rebuild of the temporary common runtime
> bundle pending completion of the normal AIDE Build/AI Deployment route. It adopts the generic
> Core Index contract, Domain v2, Documentation Methodology v21, Project Design v2, Build v4,
> WorkPackage v2 and the current Working Practices document issue while retaining unchanged
> canonical Standards/Tools from Bundle v4.

This bundle contains canonical **Standards and Tools** only. It deliberately excludes internal
Brief/Design/Decisions/Index/Work/WIP documents and explanatory Guides. The canonical artefacts
remain owned by their source topics; this Bundle is a generated, non-authoritative consumption
artefact.

## Bundle manifest

- `AIDE_Bootstrap_Standard_v1.md` — sha256 `ff71a00d2eda`
- `AIDE_Build_Standard_v4.md` — sha256 `3a8386ef5c69`
- `AIDE_BuildCapability_Tool_v1.md` — sha256 `6986ef7c0a6e`
- `AIDE_Dependencies_Standard_v2.md` — sha256 `acd8d2f872f0`
- `AIDE_Deployment_Standard_v4.md` — sha256 `0e74bca74daa`
- `AIDE_Deployment_Tool_v4.md` — sha256 `542df4d9f2c6`
- `AIDE_DocumentationMethodology_Standard_v21.md` — sha256 `6629c6d004ff`
- `AIDE_Domain_Standard_v2.md` — sha256 `61a6d571a5c9`
- `AIDE_Index_Standard_v1.md` — sha256 `a85fc86937fa`
- `AIDE_Migration_Standard_v1.md` — sha256 `6cd6c3932476`
- `AIDE_Migration_Tool_v1.md` — sha256 `99705aaa2f9e`
- `AIDE_Principles_Standard_v1.md` — sha256 `7c5a0cb171f4`
- `AIDE_ProjectDesign_Standard_v2.md` — sha256 `c06d2ceef674`
- `AIDE_Review_Standard_v1.md` — sha256 `3d7292aa826c`
- `AIDE_Review_Tool_v1.md` — sha256 `5c116b6259ca`
- `AIDE_ReviewProfiles_Standard_v1.md` — sha256 `22ca6b64b427`
- `AIDE_Scope_Standard_v1.md` — sha256 `1bda6f1244df`
- `AIDE_StandardsProduction_Standard_v1.md` — sha256 `f8cfc520f6fa`
- `AIDE_StandardsUsage_Standard_v1.md` — sha256 `cf94060dbb0b`
- `AIDE_Tags_Standard_v1.md` — sha256 `ee2c8f46463b`
- `AIDE_WorkingPractices_Standard_v4.md` — sha256 `44d190928e29`
- `AIDE_WorkPackage_Standard_v2.md` — sha256 `aa6cd3c2d408`

---

<!-- BEGIN SOURCE: AIDE_Bootstrap_Standard_v1.md -->
# AIDE Bootstrap — Standard

> **Identity:** `AIDE_Bootstrap@v1`
> **Common name:** Bootstrap
> **Version 1** (2026-08-31). First canonical Bootstrap contract produced from
> `Core_Bootstrap_Design_v2`.
>
> **Default weight:** Requirement

## Purpose

Keep AIDE's platform-level activation instruction small and stable while allowing each environment
to select a changeable startup posture through a Bootstrap Profile and thin component Bootstrap
Contributions.

## Stable bootstrap contract

Use the strongest persistent instruction mechanism the platform provides.

The persistent bootstrap shall:

1. discover an applicable Bootstrap Profile where available;
2. establish/process the Profile before substantive work where reasonably possible;
3. process applicable available `{bootstrap}` Contributions;
4. continue normally where no Profile exists; and
5. avoid repeatedly reprocessing unchanged bootstrap state during the same session.

Do not embed a release-by-release list of AIDE components or reproduce detailed Standards/Tools in
the permanent platform instruction.

Do not claim stronger startup guarantees than the host platform provides.

## Bootstrap Profile

A Profile is an environment-specific startup map.

Each entry carries only:

```text
What
Why
Where
```

- **What** — identity/name of guidance, capability or material to bring into play.
- **Why** — concise reason or relevance condition.
- **Where** — locator/discovery information for the authoritative deployed material.

`Where` identifies how material can be resolved; it does not grant permission to execute/install
arbitrary content.

A Profile may use normal Dependencies metadata to declare required presence. Bootstrap does not
create separate dependency syntax.

One effective Profile applies by default. If multiple competing Profiles are applicable and no
governing composition rule exists, surface the conflict rather than inventing precedence.

No Profile is valid; continue without AIDE bootstrap activation.

## Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that requires best-effort early-session
discovery.

A Contribution shall be separate from the owner's full detailed material and remain short enough
to process without eagerly loading that material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/reason; and
- where detailed owner material can be resolved if needed.

The owner defines the contribution's substantive semantics. Bootstrap defines only
discovery/ordering.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

## Context economy

Bootstrap establishes awareness and genuinely early checks; it is not a universal eager include.

Load full Standards, Tools, Guides, migration histories and other detailed material only when the
current work needs them, unless the Profile deliberately identifies that material as startup
guidance.

## Dependencies and missing requirements

Use `AIDE_Dependencies` for requirement/presence/version semantics.

If startup processing reveals required material is missing:

- surface the missing requirement;
- do not silently weaken or erase the requirement;
- do not silently install/update/remove material; and
- hand remediation to the environment/deployment process that is authorised to change the host.

A startup presence check does not itself trigger a blanket migration/current-version sweep.

## Deployment boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- deployment-set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package acquisition; or
- deployment verification.

A future authorised deployment process may obtain a missing requirement from trusted configured
sources. This Standard does not define that acquisition mechanism.

## Startup tasks

No generic startup-task engine exists in v1.

Use Profile activation, thin owner Contributions and startup-required dependency checks. Add a
generic task mechanism only after a demonstrated early-session need cannot be represented by these
mechanisms cleanly.

## Subset-neutral operation

The same persistent bootstrap may activate, for example:

```text
General Working
  → Principles + Working Practices

AIDE Development
  → broader AIDE operating set
```

or operate with no Profile.

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
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies
References: Core_Bootstrap_Design_v2, Core_System_Design_v6
<!-- END SOURCE: AIDE_Bootstrap_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Build_Standard_v4.md -->
# AIDE Build — Standard

> **Identity:** `AIDE_Build@v4`
> **Common name:** Build
> **Version 4** (2026-08-31). Adds WorkRegister mapping/result traceability while preserving the v3 deployment-facing Build-output contract.
>
> **Default weight:** Requirement

---

## Purpose

Execute defined work through a WorkPackage, produce the required artefacts/state, validate the actual result, and return evidence without silently taking design authority.

## Applicability

Apply when an AI/environment is acting as the executor of a governed WorkPackage or equivalent explicitly defined Build task.

Build is behavioural. Coding agents, document/work agents and future execution environments may all implement this contract.

## Accept the handoff

Before consequential state change:

- resolve the WorkPackage and authoritative work-specific inputs;
- confirm Objective, Authorised Scope, Required Outputs and Acceptance are materially clear;
- load applicable Standards/Tools needed for the work;
- where WorkRegister mappings are supplied, resolve the mapped item IDs and covered portions; and
- return `NotReady`/Blocked if a substantive design gap prevents safe execution.

A WorkRegister mapping supplies traceability to a confirmed outstanding obligation; it does not
replace the WorkPackage's own Objective, Scope, Inputs, Outputs or Acceptance.

Do not use design-history material as permission to invent a result that the current handoff does not determine.

When the required output is a platform or consumption representation of governed capability material, resolve the current canonical Standard/Tool or other authoritative outcome as the semantic source. Do not use an older Bundle, generated package or deployed copy to determine current canonical meaning/version where a current authoritative source establishes otherwise.

## Plan proportionately

Establish a coherent execution sequence proportionate to the work. Trivial work need not generate ceremonial plan artefacts.

Apply configured/governing Review before execution where required or recommended.

## Execute within authority

Resolve ordinary implementation detail autonomously where it remains within scope and does not alter objective, acceptance, major architecture/policy or reserved decisions.

If execution exposes a design-level problem, stop/contain affected work and return the issue rather than adding compensating machinery without authority.

If canonical/authoritative semantics are insufficient to produce a correct derived representation, return the defect to the owning Design/capability. Do not repair it by inventing capability meaning during Build.

## Build derived representations

Where authorised, Build may render, transform, assemble or package authoritative material into target-compatible forms such as skills, plugin contributions, instruction representations, Bundle members, merged Bundles, platform-specific files or other supported representations.

For such output:

- preserve the semantics of the authoritative source;
- build only the explicitly authorised subset/composition rather than assuming the full AIDE system;
- preserve distinct upstream roles and boundaries even when a platform rendering places several artefacts in one physical package;
- do not copy full Standards/Tools into thin contributions merely for packaging convenience; and
- record the authoritative source identity/version set used sufficiently for reproducibility and provenance.

A derived representation is a consumption/build artefact, not an authoritative replacement for its sources.

## Prepare deployment-facing Build output

When the Build output is intended for AI Deployment, expose these semantic handoff facts directly or through the applicable representation/package contract:

```yaml
BuildOutputHandoff:
  SourceProvenance: <authoritative/canonical source identities and versions>
  BuildOutput:
    Identity: <identity of the concrete built artefact/package>
    Integrity: <representation-appropriate integrity evidence>
  CompositionPosture: MemberContribution | AssembledConsumptionArtefact
```

Equivalent clear representation is valid; this Standard does not require one universal manifest format.

`MemberContribution` means the supplied item is already semantically produced by Build and may be mechanically included, arranged or assembled with other built members by AI Deployment as part of target reconciliation. Mechanical assembly must not redefine the member's semantics.

`AssembledConsumptionArtefact` means Build has already produced the authorised semantic/member composition. AI Deployment may deliver/reconcile that artefact but must not treat its contents as authority to semantically rebuild or change that composition. If the semantic/member composition must change, produce another Build output.

The Build output identity/integrity must be sufficient for the concrete result to be distinguished from another build or substituted/changed payload using the mechanism appropriate to that representation or package.

## Validate the result

Test actual outputs/state against the WorkPackage Acceptance and applicable Standards. Validation evidence should be sufficient to support the returned status.

For a derived representation, validation includes confirming that the selected authoritative sources and their material semantics are represented correctly for the target form. Where a deployment-facing handoff is required, also validate that the Build output identity/integrity and composition posture describe the actual produced output.

Apply result Review where required/recommended.

## Return outcome

Return an `AIDE_WorkPackage@v2` Outcome with truthful status, work performed, outputs, validation, deviations, remaining work, out-of-scope findings and design feedback. Where the WorkPackage mapped WorkRegister obligations, return a result/evidence/remaining-work entry for each mapped obligation or covered portion. Build reports this evidence; the owning/directing process reconciles and closes the WorkRegister.

`Complete` means the defined acceptance is satisfied, not merely that execution ended.

For deployment-facing built material, include or reference the required `BuildOutputHandoff` facts so downstream Deployment does not need to infer provenance, concrete build identity or composition authority from payload structure.

## Failure and resumption

Use `Partial`, `Blocked` or `Failed` distinctly. Preserve safe successful work where appropriate and state the actual resulting state. Re-running should resume or reproduce intentionally and avoid duplicate side effects where practicable.

## Platform and Deployment boundary

Target-platform commands, plugin/skill structures, repositories, toolchains and environment mechanics belong in platform Build Standards/Tools/configuration. They may vary without changing this contract.

Build may produce a platform-compatible artefact, representation or package. Successful Build does **not** mean that artefact is installed, deployed, reconciled with a target environment or verified as runtime-usable.

AI Deployment owns target-state reconciliation, delivery/install/update/remove actions and target/runtime verification. It may mechanically assemble outputs declared `MemberContribution`; it does not semantically reconstruct an `AssembledConsumptionArtefact`. Build must not report Deployment states unless they were separately established under the governing Deployment operation.

```yaml
MigrationSummary:
  CurrentVersion: v4
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
```

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_Design_v4, AIDE_Review@v1
References: AIDE_WorkPackage@v2, AIDE_Deployment@v4, AIDE_StandardsProduction@v1
<!-- END SOURCE: AIDE_Build_Standard_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_BuildCapability_Tool_v1.md -->
# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v1`
> **Common name:** Build Capability
> **Version 1** (2026-08-30). Canonical design-side Tool for producing Standards/Tools from
> confirmed Capability Design.

---

## Purpose

Turn confirmed Capability Design into complete canonical Standard and/or Tool outcomes without
inventing new capability meaning and without crossing into platform Build or Deployment.

## Logical actions

```yaml
Tool:
  Identity: AIDE_BuildCapabilityTool@v1
  CommonName: Build Capability
  PrimaryInvocation: build-capability
  LogicalActions: [Build, Validate, Status]
```

## Trigger and inputs

Run when confirmed Capability Design is ready to produce/rebuild canonical outcomes, or when the
user/Lead asks whether that Design is production-ready.

Resolve the Design, its declared Standard/Tool outputs, formal identity/common name, intended
capability release version, applicable production contracts/shared Standards, previous release and
transition history where relevant, and current authority to produce the outcomes.

Do not infer a substantive design choice or semantic release version where the authoritative state
is ambiguous.

## Build

1. Read confirmed Capability Design and its declared outputs. Do not use Decisions as downstream
   production input.
2. Resolve each output kind, identity, and intended capability release version.
3. For each Standard, apply `AIDE_StandardsProduction@v1`.
4. For each Tool, produce the platform-independent Tool contract: identity/logical actions,
   trigger/Scope, purpose, inputs, preconditions, procedure, bounded decisions/escalation,
   outputs/effects, reporting, failure handling, and idempotency/resumption.
5. Preserve confirmed Scope, Dependencies, Migration, and Review semantics; do not restate their
   shared mechanisms inconsistently.
6. Exclude generic target-platform implementation. Include only capability-specific platform
   addenda explicitly confirmed by Design.
7. Validate each output and the sibling output set for completeness and contradiction.
8. Produce the canonical output set, or return a precise `DesignIncomplete`/production-defect result
   rather than repairing the Design by invention.

## Validate

Perform Build's readiness/completeness checks without replacing outputs. Return Ready/NotReady and
the smallest actionable set of missing/ambiguous inputs, shared-contract defects, or cross-output
contradictions.

## Status

Report target Design, declared outputs, resolved identities/releases, current canonical outcomes
where available, readiness, and next action.

## Boundary

Successful output is:

```text
canonical Standard / Tool outcome(s)
```

Build Capability stops there. Effective Build Config, WorkPackage, platform Build Standards/Tools,
Platform Contributions, Capability Package/Deployment Manifest, and Deployment are later stages.

## Failure and idempotency

- Missing design determination → stop and identify the unresolved point.
- Unresolved identity/release → ask/escalate; do not invent.
- Canonical/shared-contract contradiction → fail visibly.
- Re-running unchanged confirmed Design for the same release produces substantively equivalent
  canonical outcomes and does not create a new release solely because generation was repeated.

Normal reporting states outcomes produced/validated, identities/releases, and anything requiring
attention.

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

**Depends on:** `Capabilities_BuildCapability_Tool_Design_v1`, `AIDE_StandardsProduction@v1`,
`Capabilities_Tools_Design_v2`.

**References:** `AIDE_Scope@v1`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`.

**Type:** `Tool` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_BuildCapability_Tool_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Dependencies_Standard_v2.md -->
# AIDE Dependencies — Standard

> **Identity:** `AIDE_Dependencies@v2`
> **Common name:** Dependencies
> **Version 2** (2026-08-29). Adds significant declaration-order/default processing precedence and
> aligns saved conformance advancement with `AIDE_Migration@v1`.

---

## Purpose

Declare what an artefact relies on; resolve dependency identity; report presence/version state; and
preserve the last saved, proven conformance checkpoint.

## Storage

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

The governing document methodology supplies the metadata container. This Standard owns the
`Dependencies:` content contract.

## Presence and version grammar

```text
dependency      normal relationship
!dependency     required on relevant use/access
!!dependency    best-effort startup presence check + required thereafter
dependency@vN   last saved/proven conformance checkpoint
dependency@!vN  exact available version vN required
```

Markers compose.

Resolve identity name first, ignoring version; compare version after resolution. Multiple matches
fail visibly.

## Declaration order

Dependency order is significant. Earlier entries have higher **default processing precedence**
when an operation needs deterministic ordering, unless an explicit relationship or governing
operation supplies another order.

This is processing/foundational precedence, not requirement severity.

## Dependency Query

Return at least resolution, requirement level, conformance version, available version, version
relation/gap, exact-version result, and effective declaration order where needed.

Dependencies reports facts. Migration/current operations decide the consequence.

## Conformance checkpoint

A recorded version advances only when the dependent artefact is updated/saved in a state proven
through that version.

- availability alone never advances it;
- `None`/`NotApplicable` migration versions may count as traversed but are persisted only on the
  next artefact save;
- failed/deferred migration does not advance through the unresolved version;
- partial success advances only through the last saved proven version.

## Exact-version constraints

`abc@!v8` requires exactly v8 to be available. Dependencies reports whether the constraint passes.
The governing dependent Standard/document context defines how that constraint should be handled by
Migration or the current operation.

## Required/startup-required

`!` is checked on relevant use/access and missing identity is surfaced prominently.

`!!` additionally requests a best-effort startup **presence** check through the Core bootstrap
mechanism. It does not imply a general startup Migration scan.

## Dependency Builder

Standards may contribute `AIDE_DependencyBuilder` definitions. Builders own only their generated
Group/Prefix output, preserve meaningful order, are idempotent, and fail visibly when applicable
output cannot be derived correctly. Group keys remain invisible to non-owning consumers.

---

**Depends on:** `Capabilities_Dependencies_Design_v2`, `Core_System_Design` v3.

**References:** `AIDE_Migration@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Dependencies_Standard_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Standard_v4.md -->
# AIDE AI Deployment — Standard

> **Identity:** `AIDE_Deployment@v4`
> **Common name:** AI Deployment
> **Version 4** (2026-08-31). Aligns Deployment reconciliation with the Build v3 output
> contract and explicit Build-owned composition posture.
>
> **Default weight:** Requirement

## Purpose

Make built deployable material available in intended AI runtime surfaces, reconcile desired composition and applicable required presence with observed target state, and verify actual usable deployment.

## Core contract

Deployment consumes:

- current Build output(s) with Build-declared `CompositionPosture: MemberContribution | AssembledConsumptionArtefact`;
- authoritative/canonical source identity/version provenance and concrete Build-output/package identity and integrity evidence;
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
3. validate authoritative/canonical source provenance, Build-output/package identity, integrity evidence and Build-declared composition posture;
4. where the Target requires set-level assembly, mechanically assemble eligible `MemberContribution` outputs deterministically without semantically re-rendering them;
5. treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary; if that composition must change, require the corresponding replacement Build output;
6. fail visibly on missing posture-compatible Build output or incompatible ownership/path/identity/namespace/posture claims;
7. compare desired composition and required presence with observed deployed state;
8. surface any missing required material as a reconciliation mismatch/blocker rather than treating it as optional;
9. determine the necessary install/update/replace/remove actions;
10. apply only actions permitted by the effective Deployment Policy;
11. verify the resulting target/runtime state; and
12. persist/report Deployment Result and observed Deployment State.

A required dependency may already be satisfied by material present outside the Set. Deployment does not silently expand Set membership merely to hide a missing requirement.

Mechanical full reassembly versus incremental patching is target implementation detail only within the Build-declared composition posture. `MemberContribution` outputs may be mechanically reassembled or patched where the Target contract permits. Deployment must not decompose or alter the internal semantic/member composition of an `AssembledConsumptionArtefact`; a different internal composition requires another Build output. If a required semantic transformation or posture-compatible output is absent, Deployment blocks/returns that need upstream rather than producing it itself.

## Production and provenance boundary

Build is upstream of Deployment. It renders/transforms current authoritative/canonical semantics into concrete Build outputs and supplies source identity/version provenance, Build-output/package identity and integrity evidence, and one `CompositionPosture`: `MemberContribution` or `AssembledConsumptionArtefact`.

Deployment owns desired Set composition and target-state reconciliation. It consumes that posture rather than deriving another one. Any Deployment-time composition is mechanical assembly of eligible `MemberContribution` outputs required by the Target representation. An `AssembledConsumptionArtefact` remains atomic at its internal semantic/member-composition boundary. Deployment preserves supplied semantics and source/build provenance in either case.

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

Removal is the consequence of desired-state reconciliation. A Deployment-owned assembly of `MemberContribution` outputs may be reassembled without the removed member. If removal changes the internal semantic/member composition of an `AssembledConsumptionArtefact`, Deployment requires the corresponding replacement Build output. An independently installed member may be uninstalled. Removal is still subject to the effective Deployment Policy.

## Artefact neutrality and manual channels

Bootstrap Profiles, Bootstrap Contributions, Standards, Tools and other deployable artefacts use the same Deployment model when Build supplies the required target-compatible Build output and composition posture. Their semantic owner does not become the deployment owner, and Deployment does not collapse their semantic roles or infer missing Bootstrap meaning during assembly.

A manually replaced project Bundle is a valid representation/channel implementation where the platform lacks automation. Later automated sync/install can replace that channel without changing Deployment Set semantics.

## Boundaries

- Producer/domain owns logical artefact semantics and its declared requirements.
- `AIDE_Dependencies` owns dependency/required-presence semantics.
- Build owns semantic rendering/transformation into concrete Build outputs and owns their source provenance, Build-output/package identity/integrity and `CompositionPosture`.
- AI Deployment owns desired Set selection, posture-respecting mechanical target assembly of eligible `MemberContribution` outputs, atomic handling of `AssembledConsumptionArtefact` outputs, policy-aware delivery/reconciliation, mismatch reporting and verification.
- Environment/platform configuration owns physical target facts, access references and actual target-change policy/authority values.
- Bootstrap owns startup discovery/surfacing, not deployment action or verification.

```yaml
MigrationSummary:
  CurrentVersion: v4
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

```yaml
Transition:
  Version: v4
  Posture: None
```

No persisted consumer-state transformation is required to adopt v4.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v4, AIDE_Dependencies@v2
References: AIDE_Build@v3
<!-- END SOURCE: AIDE_Deployment_Standard_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_Deployment_Tool_v4.md -->
# AIDE AI Deployment — Tool

> **Identity:** `AIDE_DeploymentTool@v4`
> **Common name:** Deploy
> **Version 4** (2026-08-31). Consumes the Build v3 output contract and enforces
> `MemberContribution` / `AssembledConsumptionArtefact` posture during reconciliation.

## Logical actions

```yaml
Tool:
  Identity: AIDE_DeploymentTool@v4
  CommonName: Deploy
  PrimaryInvocation: deploy
  LogicalActions: [Reconcile, Verify, Status]
```

## Reconcile

1. Resolve the requested Deployment Set and selected/all configured Targets.
2. Resolve each Target's effective Deployment Policy/authority together with destination/channel facts.
3. Resolve desired members, authoritative/canonical source identity/version provenance, concrete Build-output/package identity and integrity, Build-declared `CompositionPosture`, and applicable required-presence facts.
4. Validate that each Build output is usable under its declared posture for the required Target operation.
5. If the Target requires a semantic transformation or posture-compatible Build output that has not been supplied/resolved, report a Build/material blocker; do not manufacture it from canonical source, Design history, an older Bundle/package or observed deployed content.
6. Read/resolve observed target state where possible.
7. Compare desired composition and applicable required presence with observed state.
8. If required material is absent, report a reconciliation mismatch/blocker; do not treat Set omission as removal of the requirement and do not silently expand Set membership.
9. Mechanically assemble eligible `MemberContribution` outputs where the Target representation requires set-level assembly, preserving supplied semantics and provenance. Treat each `AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary.
10. If desired reconciliation requires changing the internal semantic/member composition of an `AssembledConsumptionArtefact`, require the corresponding replacement Build output rather than decomposing or rebuilding it.
11. Determine the minimum target actions needed to reach valid desired state.
12. Apply only target mutations permitted by Deployment Policy; otherwise return the required confirmation/manual/external next action without mutating.
13. Run the Target's verification contract, including required-presence checks where relevant.
14. Record/report per-Target state and overall `Complete`, `Partial`, `Blocked` or `Failed`.

Do not infer producer intent or composition posture from payload structure, semantically rewrite supplied Build outputs, decompose an `AssembledConsumptionArtefact`, or silently choose between conflicting outputs. Observed target content is reconciliation evidence only, not a source for semantic production.

A source/catalog locator is not authority to fetch or install. Generic acquisition of missing packages/material is outside this Tool release unless an established environment mechanism explicitly supplies that operation under resolved trust and Deployment Policy.

## Verify

Run the configured verification contract without intentionally changing desired composition.
Report installed/published state separately from runtime-content availability, applicable required-presence state and active-session pickup where those can differ.

Verification does not remediate a mismatch unless Reconcile is separately authorised.

## Status

Report desired Set composition, configured Targets, effective policy posture where material, resolved source/build provenance, Build-output/package identity/integrity and composition posture where supplied, last observed/verified state, required-presence or missing/posture-incompatible Build-output mismatches, failed/unverified Targets and the next reconciliation action. Do not infer canonical/build provenance or composition posture from deployment status alone.

Where target mutation is not currently permitted, distinguish “action required” from technical deployment failure.

## Failure and idempotency

Re-running the same desired state reconciles from observed state. A matching verified Target needs no semantic redeployment. Failure on one Target does not falsely mark other successful Targets failed or the whole deployment Complete.

Policy-denied/unconfirmed actions must not be attempted merely because credentials or write access exist.

```yaml
MigrationSummary:
  CurrentVersion: v4
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

```yaml
Transition:
  Version: v4
  Posture: None
```

No persisted consumer-state transformation is required to adopt v4.

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Deployment@v4
References: AIDE_Build@v3, AIDE_Dependencies@v2
<!-- END SOURCE: AIDE_Deployment_Tool_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_DocumentationMethodology_Standard_v21.md -->
# AIDE Documentation Methodology — Standard

> **Identity:** `AIDE_DocumentationMethodology@v21`
> **Common name:** Documentation Methodology
> **Version 21**
> > **Published:** 2026-08-31
> > **Change:** Core Index ownership split; top-level-topic anchor; WIP/Working distinction; live-only registers; WorkRegister/WorkPackage reconciliation.
>
> **Default weight:** Expectation

## Purpose

Provide the canonical AI-facing contract for creating, naming, structuring, recording, versioning,
distributing and maintaining AIDE-governed document corpora while preserving active work safely
and keeping confirmed Design aligned with delivered outcomes.

This Standard is the normal runtime/deployable representation of Documentation Methodology.
`DocumentationMethodology_Guide_v21` is its fuller human-oriented companion.

## Ownership boundary

**Weight: Requirement**

Documentation Methodology owns governed document naming, document types and document-specific
lifecycle, lifecycle state/disposition semantics, top-level-topic/document organisation,
documentation-specific Index extensions, document metadata-container placement,
governed-history preservation, document distribution rules, asset/unmanaged recording, the
authoritative-master/generated-consumption boundary, and document output/version discipline.

Physical repository/storage layout, management-folder names, file movement, sweep/external-archive
cadence, Change Delivery staging and Binder placement/replacement workflow are operating concerns
owned by Working Practices or the applicable environment. Physical location does not define a
document's lifecycle state.

Do not absorb semantics owned elsewhere:

- Core owns formal Identity and generic `AIDE_Index@v1` Item/Item Type/Index behaviour.
- `AIDE_Domain` owns Domain resolution and which semantic Item Types may establish/stop Domain
  propagation.
- `AIDE_Tags` owns Tags content/build/query.
- `AIDE_Dependencies` owns dependency identity, presence, order, version and conformance checkpoints.
- `AIDE_Migration` owns transition discovery/execution/progress.
- `AIDE_Review` owns generic Review lifecycle.
- `AIDE_WorkPackage` / `AIDE_Build` own generic execution/return behaviour.
- Messaging owns Message envelope/schema/threading/receipt/transport behaviour and message-specific
  document semantics.
- Subject-matter owners own substantive document content and top-level-topic/subtopic choices.

Where this Standard hosts another owner's metadata/state, preserve that owner's semantics.

## Core corpus principles

**Weight: Expectation**

1. Keep one authoritative answer per question; reference rather than restate.
2. Route information by state and role: WIP preserves current volatile context; Working preserves
   substantial exploration; OpenItems tracks live unresolved attention; Brief defines; Design
   determines; Decisions records reasoning; WorkRegister tracks confirmed undelivered consequences;
   WorkPackage bounds execution; Outcome returns evidence; Index records structure/current corpus.
3. Treat filenames as legible locators and the applicable authoritative Index as the resolver.
4. Distribute only document types whose distribution contract permits it.
5. Keep human-readable documents as short as their function permits and conclusion-first.
6. A confirmed Design change with a downstream consequence is applied in the same pass or recorded
   in WorkRegister in enough detail to reconcile delivery later.
7. Version issued outputs/checkpoints, not drafting keystrokes.
8. Do not leave material confirmed state or valuable active thinking solely in volatile conversation
   where loss would materially impair continuation.
9. Prefer an existing mechanism over adding another one.

## Naming

**Weight: Requirement**

A chat project, master folder, workspace or similar shared context pool is a **container**. A
container may hold one or more **top-level topics**. The top-level topic, not the container, is the
normal semantic anchor for governed topic documentation and standing registers.

Normal governed Markdown filename:

```text
{TopLevelTopic}_{Subtopic...}_{DocType}[_{Key}]_v{N}.md
```

- Use the top-level-topic filename prefix first.
- Omit subtopic segments for top-level-topic-wide documents/registers.
- Resolve DocType from an established or locally declared custom type.
- Add a key only where the type/working pattern calls for one.
- Keep the version suffix last.
- Compound subtopic segments may express instantiation/subdivision and may nest.
- A filename is not the authoritative type/topic registry; the applicable Index is.
- Existing filenames already using the effective top-level-topic prefix do not require rename merely
  because older methodology called that first slot `Project`.

Cross-references may be deliberately:

```text
abc_Design_v5   # tied to that issued version
abc_Design      # resolves to current
```

Preserve the author's chosen form.

### Point-in-time keys

Use date-sequence `{YYYY-MM-DD}-{N}` where the type requires a dated instance.

- Review: date mandatory; optional single-segment label may follow the date-sequence.
- Working: no key normally; label/date only when the actual working pattern needs it.
- WIP: no key normally; use a subtopic/thread key where several parallel active contexts within one
  top-level topic need independent WIP series.
- WorkPackage: opening date mandatory; a separate WorkPackage Outcome uses the same key.
- Archive marker `_Archived_{date}` is inserted after DocType and before an existing key.

## Document role model

**Weight: Requirement**

```text
WIP
  current volatile persisted context

Working
  substantial exploratory/formative material

OpenItems
  live unresolved/pending/deferred/future attention

Brief / Requirements
        ↓
      Design  ← Decisions
        ↓
     outcomes

WorkRegister
  confirmed downstream consequences still undelivered
        ↓
   WorkPackage(s)
        ↓
      Outcome
        ↓
reconcile WorkRegister
```

- **WIP** — high-churn, non-authoritative current-work checkpoint used so valuable thinking can
  survive chat/session/platform/context loss.
- **Working** — substantial exploratory/formative body worth preserving while it develops; it may
  predate a Brief/Design and may later feed several destinations.
- **OpenItems** — live durable attention still requiring thought/revisit/investigation/progression.
- **Brief** — objective, scope, requirements, success signals; optional by stakes.
- **Requirements** — standing cross-topic requirements when size warrants splitting from Brief.
- **Design** — confirmed current position; declares produced outcomes and external handlers.
- **Decisions** — reasoning/history informing future Design. It is not a downstream outcome input.
- **Review** — faithful point-in-time assessment record. Generic Review behaviour comes from
  `AIDE_Review`.
- **Guide** — distributable explanatory outcome.
- **Reference** — distributable lookup outcome.
- **Glossary** — distributable definitions.
- **Overview** — standing narrative/orientation outcome.
- **WorkRegister** — confirmed downstream work/consequences that remain undelivered.
- **WorkPackage** — document representation of a bounded unit of Build work; execution semantics are
  `AIDE_WorkPackage`.
- **WorkPackage_Outcome** — separate live return document where used; folds into WorkPackage on
  archival.
- **Message** — Messaging-owned transmission/message semantic type; this methodology supplies only
  generic governed-file integration when persisted.
- **Index** — generic structural registration under `AIDE_Index@v1` plus documentation-specific
  extensions defined here.
- **Asset / Unmanaged** — explicitly outside normal governed document-type behaviour.

An outcome must have an authoritative defining source. Decisions never substitutes for missing
Design content.

## Condensed and expanded topic documents

**Weight: Guidance**

A small subtopic may hold its internal Brief/Design/Decisions/Working material in one condensed
file. Use the highest-order confirmed content as its DocType.

Expand when retrieval, independent edit cadence, Working disposition, blind review, or explicit
instruction makes separation valuable.

Generic Index remains structural. Documentation-specific Document Register and top-level-topic
standing WorkRegister remain outside a condensed subtopic file. OpenItems may be top-level-topic
wide by default or delegated to a subtopic when volume/cadence warrants it. A Guide does not
condense into its Design because they have different roles/distribution.

## WIP

**Weight: Expectation**

Use WIP when active thinking/current work state must survive interruption, chat/session context
loss, platform switching or another likely context discontinuity and is not yet safely represented
elsewhere.

WIP may contain current position, reasoning not yet routed, draft fragments, candidate OpenItems or
WorkRegister consequences, source pointers and a clear resume point. Temporary duplication is
allowed because WIP is a continuity checkpoint, not an authoritative source.

Draft freely inside one editing context. When issuing/persisting a checkpoint for reuse, sync or
resumption, increment `_vN` so the filename visibly signals currency. A replaced issued checkpoint
becomes Superseded.

WIP is normally outside the stable Binder and normally withdrawn/disposed after its useful content
has been routed. Archive only where the WIP itself has unusual independent historical value.

## Working

**Weight: Expectation**

Working is substantial exploratory/formative material that is useful to preserve independently
while it develops. It is **not limited to Design in progress**: an idea, review fallout, research or
other substantial block may exist for some time before its eventual authoritative destination is
known.

Working may later feed Design, Decisions, Brief, Reference, proposal, Review response or several
owners. Do not leave Working as a competing source once material confirms elsewhere.

On completion, resolve disposition: **Archived** where the Working record itself has independent
historical/research value; otherwise **Superseded/withdrawn** where its substantive value is fully
represented in retained authoritative records. Physical handling belongs to Working
Practices/environment.

Normal stable Binders exclude Working by default; load it separately when active/exploratory state
is needed.

## Decisions

**Weight: Requirement**

Decisions preserves **synthesized substantive reasoning for a future Design reader**, not only the
final outcome. Preserve enough of the path to reconstruct why the confirmed position exists
without turning the record into a transcript. As applicable and proportionate, include the
trigger/requirement, problem found, alternatives genuinely considered, key distinctions/reasoning,
decision, and important consequences/trade-offs.

A Decisions event is owed when:

- the confirmed substantive Design position changes;
- a requirement is established or materially revised; or
- a rejected alternative could reasonably be re-derived and reconsidered later.

Purely editorial, formatting, metadata, migration, mechanical maintenance, or application of an
already-recorded decision does not by itself create a new Design decision. A genuinely trivial
alternative may be omitted; otherwise a rejected alternative receives at least a brief reason.
Proportionality controls depth, not whether a substantive event disappears from the record.

Produce a substantive Design change and its Decisions record in the same pass. Assemble the entry
from the reasoning actually developed while it is available; confirmed reasoning at material risk
of being left only in conversation overrides ordinary restraint on document output.

Existing entries are historical and are not retroactively rewritten. Later entries may supersede,
refine, reverse, constrain, or reinterpret an earlier decision while leaving the earlier record
intact.

Keep Decisions at Design granularity. An independently expanded child Design normally keeps its
substantive reasoning in a Decisions record at that same scope; a condensed topic may use a
Decisions section. Parent-level architectural reasoning remains parent-level.

Split Decisions history only when retrieval quality deteriorates or unrelated settled history
obscures the live record. Prefer closure/state-based volumes with pointers over arbitrary
chronological trimming. Do not delete or rewrite history merely to shorten the active file.

Decisions informs future Design and is **not** an input to downstream outcomes. If a consideration
is required for correct implementation or delivery, it must be represented in the current Design
or other authoritative downstream input.

## Review document integration

**Weight: Requirement**

A governed Review document is a faithful point-in-time assessment record.

Do not rewrite a finding's substantive text because it was later resolved/disputed. Record
resolution/status separately. Archive according to the document lifecycle once its findings meet
the archival condition.

Use `AIDE_Review@v1` for the assessment lifecycle itself; this Standard governs only the document
representation/lifecycle.

## Message document integration

**Weight: Requirement**

Messaging owns Message schema/fields, envelope/thread identity, revision, source marking,
receipt/reconciliation state, light/heavy promotion criteria and transport workflow.

Documentation Methodology does **not** duplicate that schema.

When Messaging promotes a Message to a governed file, apply the generic document behaviours owned
here—filename/version placement, Current/Superseded/Archived lifecycle, metadata-container hosting,
governed-history handling and distribution integration—except where the Messaging-owned Message
contract deliberately specifies a message-specific rule.

A light conversation-only message is not required to become a governed document.

## Index

**Weight: Requirement**

Use `AIDE_Index@v1` for generic Index/Item/Item Type semantics.

Documentation Methodology contributes documentation-specific Index sections/properties where
applicable:

- top-level-topic/subtopic declarations and documentation relationships;
- Document Register and current document version/type/lifecycle facts;
- local/custom document type definitions;
- document assets/unmanaged-file records;
- withdrawn/renamed/rehomed/dead-locator mappings; and
- documentation-local configuration.

### DocumentationTopic Item Type

`DocumentationTopic` is a Documentation Methodology-owned semantic Item Type representing one
self-describing **top-level documentation topic**. Identification relies on authoritative topic/Index
declarations rather than folder naming alone.

A parent/repository Index may register and describe a DocumentationTopic, locate it and stop at that
self-describing boundary. A physical container may hold one or several DocumentationTopics.

Defining the Item Type does not grant Domain authority. `AIDE_Domain` alone decides whether a type
is Domain-capable/domain-defining.

The documentation Index is authoritative for the documentation registration/configuration facts it
owns; registration does not make it authoritative for another Item's internals.

## OpenItems and WorkRegister

**Weight: Expectation**

### OpenItems

OpenItems is the durable **live attention register**: current, pending, deferred or future items
whose loss would matter and which still require thought, revisit, investigation or progression.

- Default one OpenItems register per **top-level topic**.
- Create/delegate a subtopic register only when use/volume/cadence materially warrants it.
- Keep entries concise enough to resume; use WIP/Working for substantial active material.
- When resolved, route any durable outcome appropriately and remove the item.
- Do not maintain a closed-items/tombstone archive inside OpenItems.

### WorkRegister

WorkRegister is the top-level-topic-wide live queue/ledger of **confirmed downstream consequences or
work not yet fully delivered**. It is the reconciliation layer between committed Design and
delivered reality, not merely a generic backlog.

Whenever confirmed Design changes, determine whether downstream code/build/document/production
outcomes must change. Every such consequence shall either be fully delivered in the same pass or be
recorded in WorkRegister.

Record enough detail to determine later whether the committed Design has actually been delivered,
including as applicable:

```text
ID
source/triggering Design change
committed change
specific required downstream changes
target outcomes/locations
current delivery state
WorkPackage/action mapping
returned result while still open
remaining work
```

One WorkPackage may cover some/all of several WorkRegister items; one WorkRegister item may be split
across several WorkPackages. Completed items are removed after reconciliation. Do not retain
completed rows as a second Decisions/Outcome history.

Default one WorkRegister per top-level topic. Delegate only where an independently useful subtopic
queue is justified by volume/cadence.

## Binder and live-state treatment

**Weight: Expectation**

A normal Binder is a stable/current knowledge consumption artefact, not a live work queue. Exclude
by default:

```text
WIP
Working
OpenItems
WorkRegister
```

Load these separately when resuming/managing active work. A specialised live-state Binder is valid
only when deliberately designed for that purpose.

Do not reintroduce the same churn through Index. Individual live-state versions may be omitted from
the stable Document Register; where discovery benefits, an Index may hold a compact version-agnostic
`Live state` series/locator entry (for example `Capabilities_Messaging_WIP`). The current checkpoint
version is established from the actually available/current file, not an old Index row. Reissuing a
new `_vN` in the same live series therefore does not itself require an Index/Binder issue. Reconcile
series creation/withdrawal at the next normal corpus/output checkpoint.

## Lifecycle, supersession and archival

**Weight: Requirement**

Lifecycle state is independent of storage representation:

- **Current** — the issued authoritative version/instance the corpus resolves for normal current use.
- **Superseded** — an older issued version, or a document displaced/withdrawn without reaching an
  archival terminal disposition of its own.
- **Archived** — a document whose type-specific lifecycle reaches an archival terminal disposition;
  the final archival record is frozen except through the type's permitted correction route.

A type may define completion, withdrawal, absorption or another terminal path that determines the
correct disposition. The `_Archived_{date}` filename marker remains the document-naming expression
for an archival disposition where that convention applies.

Generated Binders/Bundles are consumption artefacts assembled from authoritative sources; they are
not authoritative masters. Regenerate them from their source set rather than editing them as the
source of truth.

Do not discard governed history merely to simplify the active view. A living current-document
register need not list every lower Superseded version where version sequence already proves their
existence, but preserve explicit mapping for renamed/rehomed/withdrawn names and enough archived
history/locator information to keep the corpus truthful.

Physical storage may use repository folders, external archives, a document-management system,
platform-native history or another representation. The applicable Working Practices/environment
owns physical placement, movement, retention media and cleanup; those choices must not erase the
semantic state or required governed history.

## Metadata containers

**Weight: Requirement**

Document layout may contain:

```text
Title / version preamble
Header metadata
Temporary owner-labelled state
Body
Footer metadata
Internal section
```

Header metadata is immediately after title/version preamble. Temporary state follows header
metadata and precedes ordinary body content. Footer metadata follows body and precedes the Internal
section where present.

Known properties:

```text
Identity: ...
Tags: ...
Dependencies: ...
References: ...
Type: ...
```

This list is extensible.

- Identity semantics belong to Core.
- Tags semantics belong to `AIDE_Tags`.
- Dependencies semantics belong to `AIDE_Dependencies`.
- Migration state semantics belong to `AIDE_Migration`.
- References is a document citation relationship without conformance semantics.
- Custom-type pointer/rendering remains a Documentation Methodology concern.

Keep generated metadata/state compact.

## Internal section

**Weight: Guidance**

Use an Internal section for durable bookkeeping that helps later maintainers but is not part of
the document's distributed substantive body, such as delivery/correction notes, absorbed-document
pointers or other lifecycle trace information defined by this methodology.

Do not use Internal as a hidden second body for substantive rules.

## Distribution

**Weight: Requirement**

Distribution follows document type and project policy.

Internal working/decision/register material does not travel merely because it is useful context.
Published outcomes such as Guides/References/Standards may travel according to their contract.

A consuming project may adopt a distributed Guide/Reference as a resource without becoming its
owner.

## Assets

**Weight: Expectation**

An Asset is produced/held by the corpus but its filename is fixed by the consuming tool/system
rather than by this document naming convention.

Record enough ownership, path, purpose/currency/lifecycle information in the Index/assets register
to manage it truthfully.

Do not rename an Asset into the document naming convention merely for aesthetic consistency.
Use Reference instead only where the file is actually a governed lookup document whose filename
the corpus owns.

## Unmanaged files

**Weight: Expectation**

An unmanaged file is held by the container but deliberately not governed by this methodology.

Record it in the Index with management=`unmanaged`, filename and recorded date. Optional attributes
such as purpose, editable posture, versioned posture, source and lifecycle are recorded only when
established; unknown values are stated as not established rather than guessed.

A type-looking segment in an unmanaged filename does not confer governed type/version/lifecycle
behaviour.

Review/prompt cadence for unmanaged files is owned by the process/interface that manages the
container, not by this Standard.

## Claimed versus verified

**Weight: Requirement**

Do not compose plausible metadata, times, versions, paths, delivery facts or successor names where
the fact should be observed/read.

Distinguish:

- verified/read state;
- declared/claimed state; and
- unknown/unestablished state.

Where the system cannot verify a mandatory value, represent that limitation explicitly.

## Output and version discipline

**Weight: Requirement**

A file's `_vN` counts issued outputs/checkpoints, not internal editing operations.

- Draft freely before issue.
- After an issued/delivered document is changed and reissued, increment its document version.
- A rename alone is not a semantic content revision unless the governing lifecycle explicitly
  makes it one.
- Do not issue new versions/documents as ceremony.
- WIP is intentionally versioned when a persisted continuity checkpoint is issued so filename
  currency is visible across chat/project/platform contexts.
- Produce a substantive Design change and its Decisions record in the same pass; editorial or
  mechanical Design maintenance does not create a Decisions event by itself.
- For every confirmed Design change, identify downstream consequences. Apply them in the same pass
  or record the undelivered consequences in WorkRegister.
- At the end of a material work unit or key confirmation point, assess whether confirmed state or
  valuable active thinking is at risk of being left only in volatile conversation/context.
- Where state is materially at risk, preserve it using the least-heavy correct mechanism—often WIP
  for current context—then consolidate normal deliverable output at the appropriate checkpoint.

## WorkPackage document integration

**Weight: Requirement**

Generic WorkPackage authoring/execution/validation/return semantics come from
`AIDE_WorkPackage@v2` and `AIDE_Build@v4`.

This Standard owns document integration:

- the WorkPackage is a governed point-in-time document with opening-date key;
- a separate live WorkPackage Outcome uses the same key where produced;
- when a WorkPackage is sourced from WorkRegister, it identifies the covered item IDs and the
  authorised portion of each obligation;
- the Outcome reports result/evidence/remaining work for those mappings;
- the director/owning process reconciles the returned evidence against the WorkRegister and current
  Design—Build does not silently close the register;
- after reconciliation, a returned Outcome may be appended verbatim to the WorkPackage before
  archival where that lifecycle is used; and
- design-shaping issues returned by Build are resolved by Project Design rather than silently
  settled by document mechanics.

## Documentation Methodology conformance

**Weight: Requirement**

Current conformance is recorded through Dependencies:

```text
Dependencies: !AIDE_DocumentationMethodology@v21
```

The dependency version is the last saved/proven Documentation Methodology capability release
against which the document is conformant.

A newer methodology release does not itself rewrite all existing documents. Migration posture
determines when the checkpoint advances.

### Legacy v17 checkpoint bridge

For the **v17 → v18 transition only**:

If all of the following are true:

1. the document is a governed pre-v18 document;
2. it has no resolved `AIDE_DocumentationMethodology` dependency checkpoint; and
3. it contains an unambiguous legacy `Methodology: v17` declaration,

then Migration shall interpret that legacy declaration as the starting conformance checkpoint
`AIDE_DocumentationMethodology@v17`.

This interpretation:

- is a compatibility input to Migration only;
- does not change the document on read/use;
- does not create a modern dependency declaration until a qualifying save/update succeeds; and
- must fail visibly rather than guess if multiple/contradictory legacy methodology declarations
  exist.

### v18 transition

```yaml
MigrationSummary:
  CurrentVersion: v21
  LatestRequiredVersion: none
  LatestOnUpdateVersion: v18
  SupportedBaseline: v17

Transition:
  Version: v18
  Posture: OnUpdate
  Change: >
    Move document conformance to AIDE_Dependencies, adopt extensible metadata/state containers,
    and delegate generic WorkPackage execution semantics to AIDE_WorkPackage.
  Items:
    - Resolve the starting checkpoint using Dependencies or the legacy-v17 bridge.
    - Replace the legacy Methodology: v17 checkpoint with !AIDE_DocumentationMethodology@v18.
    - Convert legacy Depends on relationships that are true conformance dependencies to Dependencies: syntax.
    - Preserve References as citations where no conformance obligation exists.
    - Host Identity, Tags and temporary owner state under the v18 container placement rules where present.
    - Preserve unrelated content; do not rewrite merely to make the document look newer.
  Success: >
    The saved document uses v18 metadata placement where applicable, records a truthful
    AIDE_DocumentationMethodology@v18 dependency checkpoint, and has no contradictory legacy
    Methodology footer.

Transition:
  Version: v19
  Posture: None

Transition:
  Version: v20
  Posture: None

Transition:
  Version: v21
  Posture: None
```

Merely reading/using a v17 document does not trigger the v18 OnUpdate transition. v19, v20 and v21
require no additional artefact transformation; when Migration traverses through current during a
qualifying save, their None transitions may advance the saved checkpoint after the v18 success
condition is satisfied.

An operation specifically requiring a v18-only structure may require migration before that
operation proceeds.

## Build and deployment

**Weight: Context**

This Standard is the canonical deployable Documentation Methodology outcome.

Platform Build may render it as a skill, plugin contribution, bundle member, instructions or
another supported representation without changing semantics.

The common AIDE Standards/Tools Bundle is a valid assembled representation. The human Guide is not
required in every consuming project once this Standard is available there, though it may be added
when richer explanatory context is useful.

---
Dependencies: AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_Tags@v1, AIDE_WorkPackage@v2, AIDE_Build@v4
References: DocumentationMethodology_Design_v18, DocumentationMethodology_Guide_v21
<!-- END SOURCE: AIDE_DocumentationMethodology_Standard_v21.md -->

---

<!-- BEGIN SOURCE: AIDE_Domain_Standard_v2.md -->
# AIDE Domain — Standard

> **Identity:** `AIDE_Domain@v2`
> **Common name:** Domain
> **Version 2** (2026-08-31). Moves Domain recognition onto Domain-approved semantic Item Types, adds a thin recognition projection and a propagation-stop boundary while retaining the established v1 resolution/settings model.
>
> **Default weight:** Requirement

## Purpose

Provide one consistent AIDE contract for identifying the named operating/governance context
relevant to a target, hosting independently owned Domain-context settings, and explicitly
clarifying/composing Domain roots when natural recognised structure is insufficient.

A Domain is contextual and semantic; it is not inherently a file and is not an AIDE activation
switch.

## Applicability

Apply when an operation needs Domain context for a target, focus, setting lookup, navigation,
composition or another Domain-aware behaviour.

```yaml
Scope:
  Context: >
    Apply when the current operation needs to resolve, declare, name, navigate or consume Domain
    context or Domain-hosted settings for a target/focus.
```

Do not resolve Domain merely because an artefact exists. One session may work across several
Domains or with material that has no Domain.

## Domain model

A **Domain is a named AIDE operating/governance context**.

A Domain may be:

```text
implicit  — established from a Domain-approved semantic Item Type / authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify recognised roots
```

Generic Item/Item Type semantics belong to `AIDE_Index@v1`. A type owner defines what an Item Type
is, how it is identified and what it provides. **Only Core/Domain decides whether a semantic Item
Type is permitted to establish/participate in Domain resolution.**

An arbitrary Item Type cannot self-assign Domain authority, and a generic Index is not
Domain-defining merely because it exists.

Initial Domain recognition continues to cover the demonstrated structural roles represented by the
current system—documentation top-level topic/Index structures, native solution structures, native
project structures and explicit AIDE Domain declarations—but they are consumed through
Domain-approved semantic type/recognition entries rather than a rule that every Index/solution/
project-shaped thing automatically creates Domain authority.

A repository/worktree remains a discovery boundary, not an implicit Domain type.

## Natural containment

Authoritative structural containment prevents a contained Domain-capable item from establishing a
second implicit Domain.

- a project that is an authoritative member of a solution remains in the solution Domain;
- a delegated/self-describing documentation topic remains in its enclosing effective Domain unless
  propagation is explicitly stopped; and
- another Domain-capable Item inside an effective Domain does not create a child Domain merely
  because it could establish a root when isolated.

Structural children do not create child Domains implicitly. Child-Domain inheritance, settings
propagation, precedence and parent/child composition remain undefined in v2.

### Domain propagation stop

Domain may mark a structural boundary as **Propagation: Stop**. The effect is deliberately narrow:

> an enclosing Domain does not propagate through that boundary; content below it must resolve
> Domain independently.

This does **not** create a child Domain and does not define inheritance, merge or precedence.

Where the boundary is represented as an Index Item, use the Domain-owned contribution, for example:

```yaml
Domain:
  Propagation: Stop
```

Equivalent representation may be defined for another Domain-aware structure. The semantic meaning
belongs to Domain; Index merely hosts the property.

## Co-root recognised structures

Evaluate recognised structures sharing a physical root by authoritative identity and structural
relationships, not proximity alone.

### Matching identity

Co-root structures with matching authoritative identities form one implicit Domain.

```text
Foo.sln + Foo_Index  → Foo Domain
```

An available declared Index structural/topic identity is authoritative over filename-only matching.
When a matching Index and solution/project represent one Domain, the Index is the preferred
AIDE-controlled Domain metadata/settings host. The native solution/project retains authority over
its own membership and semantics.

### Different identity

Co-root recognised structures with different identities remain separate implicit Domains by
default.

```text
Foo.sln + Womble_Index  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj → Foo Domain + Bar Domain
```

Multiple standalone projects in one folder with no enclosing solution are therefore separate
Domains. If this natural interpretation is not intended, use `AIDE_Domain.yaml` rather than adding
special-case inference.

## Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a solution remains authoritative for solution/project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native solution/project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## Domain identity and references

An implicit Domain takes its current name/identity from the authoritative recognised structure
that establishes it. Use authoritative declared/native identity when available; filename matching
is only a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names for navigation, cross-Domain
references, composition, provenance or other cases where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally
wrong—for example to compose several solutions/projects/Indexes, combine differently named roots,
or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Type: Solution
        Path: Product.sln
      - Type: Index
        Path: Product_Index_v1.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Declaration fields

- `Schema` — required declaration-container schema identity; v1 value is `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of recognised roots explicitly composed/clarified by the
  entry.
- `Type` — one of the v2 Domain-approved root roles represented by `Index`, `Solution`, or `Project` for each explicit root; the resolver maps that role to approved semantic recognition rather than granting authority from the token alone.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

The explicit Domain declaration itself is Domain-capable, but its `Roots` identify the recognised
structures whose natural interpretation it composes or clarifies. Co-location of two Domain entries
inside one file creates no relationship between them.

A valid explicit declaration may override the natural implicit grouping of its listed roots. It
does not recreate or replace their internal registries or native membership rules.

## Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

Preferred authoritative hosts are:

```text
Index-backed implicit Domain
→ root Index local configuration may host Domain metadata/settings

matching solution/project + Index
→ Index is the preferred AIDE Domain metadata/settings host

explicit Domain
→ the Domain entry in AIDE_Domain.yaml hosts Domain metadata/settings
```

Where a root Index hosts Domain metadata/settings, expose one Domain configuration mapping in the
Index's local configuration using the shared field meanings:

```yaml
Domain:
  Aliases: [PreviousName]
  Settings:
    SomeSetting: <owner-defined value>
  Branches:
    - Branch: docs/api
      Settings:
        SomeSetting: <owner-defined value>
```

`Aliases`, `Settings` and `Branches` are optional. The Domain name is inherited from the Index's
authoritative structural/topic identity and `Roots` are not repeated. Core/Index owns generic Index hosting/representation; Documentation Methodology owns any
documentation-specific Index sections. Domain owns the meaning of this Domain configuration payload.

For a solution/project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit `AIDE_Domain.yaml` representation rather than modifying the native format solely to carry
AIDE configuration.

## Domain Recognition Registry

Runtime Domain discovery should not load every Standard/Item Type definition for every path step.
A build/runtime environment may compile the Domain-approved type assignments into a thin
`DomainRecognitionRegistry` containing only the cheap signatures/relations required for Domain
discovery.

Rules:

- the registry is an optimisation/projection, not the source of Domain authority;
- Core/Domain approval remains authoritative;
- load/compile definitions once per relevant context;
- prefer explicit/native/name/extension/marker evidence before expensive content inspection;
- cache unchanged resolution where safe; and
- if a registry entry cannot be traced to a currently approved semantic type/recognition rule, fail
  or refresh rather than silently granting Domain authority.

## Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. A nearby project, solution or Index is provisional until applicable enclosing evidence has
been checked.

Do **not** use “nearest marker wins”. Physical ancestry is a discovery path, not proof of
composition.

### Discovery boundaries

Stop upward discovery at the nearest meaningful operational boundary available to the current
context, such as:

- an explicitly supplied discovery boundary;
- workspace/container root;
- repository/worktree root;
- user Documents root;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- another recognised user/application storage root; or
- filesystem/mount root as fallback.

A discovery boundary limits search only. A valid explicit Domain declaration may reference roots
beyond that boundary where the environment can resolve those references.

## Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing recognised Domain evidence within that boundary, including
   applicable `AIDE_Domain.yaml` declarations and authoritative containment/membership relations.
3. Resolve explicit Domain claims applicable to the target. A valid unambiguous explicit claim
   supplies the effective Domain and may clarify/override the natural grouping of its declared
   roots.
4. Before propagating an enclosing Domain through a structural boundary, apply any Domain-owned
   `Propagation: Stop` declaration. If propagation is stopped, disregard the enclosing Domain for
   content below that boundary and continue resolution independently; the stop does not itself
   create a Domain.
5. Otherwise apply authoritative containment: a contained Domain-capable structure inherits the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate co-root independent recognised roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining independent recognised root, return that
   implicit Domain.
8. If no Domain-capable structure applies, return `No Domain context`.
9. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
   return an unresolved/error result rather than merging, ranking or guessing.

## Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership without clearly
  expressing the intended override;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## Ownership boundaries

- **Core/Domain** owns this common context/resolution/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Core/Index** owns generic Index/Item/Item Type behaviour. **Documentation Methodology** owns documentation-specific Index extensions and the `DocumentationTopic` semantic type.
- **Project/solution systems** own native membership and project/build-system semantics.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## Deliberately absent from v2

The following are not defined by this Standard:

- implicit or generic child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository-as-Domain merely because a repository exists;
- a generic settings precedence/inheritance engine;
- a Domain-specific Tool;
- broad exclusion syntax to counteract normal defaults; or
- platform-specific parser machinery beyond what is required to observe the recognised structures.

If a demonstrated use case later requires one of these mechanisms, change Domain Design first and
produce a later Standard release through the normal capability-production path.

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
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, AIDE_Scope@v1, AIDE_Migration@v1, Core_Domain_Design_v2
References: Core_System_Design_v7, AIDE_Index@v1
<!-- END SOURCE: AIDE_Domain_Standard_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Index_Standard_v1.md -->
# AIDE Index — Standard

> **Identity:** `AIDE_Index@v1`
> **Common name:** Index
> **Version 1** (2026-08-31). First canonical generic Index/Item Type contract.
>
> **Default weight:** Requirement

## Purpose

Provide one generic AIDE mechanism for maintaining an authoritative hierarchical view of
significant items within a defined boundary while allowing specialised owners to add their own
properties/registers without transferring semantic ownership.

## Index contract

An Index shall identify its scope and provide a hierarchical `Contents` view of the significant
Items it registers.

The Index is authoritative for:

- which items it registers within that scope;
- their Index-owned locator/containment facts; and
- Index-owned information attached to those registrations.

Registration does **not** make the Index authoritative for a registered item's internals.

`Contents` may intentionally omit insignificant physical items and may stop at a delegated or
self-describing boundary.

## Item

A registered Item may expose, as applicable:

```text
name / identity
locator / containment
semantic Item Type(s)
description
compact owner-defined properties
delegated/self-describing boundary pointer
```

Arrange Items primarily by containment/location. Type is metadata, not the primary hierarchy.

## Item Type Definition

An Item Type Definition has two semantic jobs:

1. identify whether an item satisfies the type; and
2. state what the type provides/enables when identified.

Use declarative observable recognition evidence. Prefer cheap evidence such as explicit identity,
name/extension, structural marker or authoritative native relationship before expensive content
inspection.

Do not use the generic Item Type contract as arbitrary executable classification logic.

An Item may satisfy several independent semantic Item Types. No generic type-inheritance hierarchy
exists in v1.

## Physical fallback

If no richer semantic type applies:

```text
physical directory → Folder
physical file      → File
```

Physical classification may coexist with semantic Item Types.

## Extension ownership

An owner may define Item properties or specialised Index sections/registers.

The contributing owner owns:

- field/section meaning;
- values/schema;
- validation;
- lifecycle; and
- update rules.

Index owns generic hosting/coexistence only.

An Index updater shall preserve properties/sections it does not own unless explicitly authorised to
reconcile them.

## Delegation

A parent Index may register and locate a self-describing child boundary without duplicating its
internal registry. The parent remains authoritative for the parent registration; the child/native
owner is authoritative internally.

## Canonical representation

Use Markdown as the canonical human/AI source representation.

Prefer:

- headings/lists for hierarchy;
- YAML flow mappings/sequences for compact structured Item properties; and
- tables for regular homogeneous extension sections.

Do not invent an AIDE-only mini-language where standard YAML flow syntax suffices.

HTML may be generated as presentation but is not canonical source in v1.

## Runtime Item Type Registry

A runtime/build environment may compile available Item Type Definitions into a compact registry.

Use this order where practical:

1. explicit/cheap selectors;
2. structural/native relationship checks;
3. expensive inspection only if necessary;
4. lazy enrichment after classification; and
5. cached reuse for unchanged items where safe.

The compiled registry is derived optimisation state, not semantic authority.

## Domain boundary

Generic Index existence does **not** establish a Domain.

`AIDE_Domain` owns the approved Domain-defining/Domain-capable Item Type set and any thin Domain
Recognition Registry derived from it. An Item Type owner cannot grant itself Domain authority by
setting a local flag.

## Deliberately absent

No v1 requirement exists for:

- type inheritance;
- universal metadata ontology;
- generic query language;
- explicit registration of every file/folder;
- mandatory root pointer for every project/container; or
- automatic recursion into self-describing child boundaries.

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
Dependencies: !AIDE_DocumentationMethodology@v21
References: Core_Index_Design_v1, Core_Domain_Design_v2
<!-- END SOURCE: AIDE_Index_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Migration_Standard_v1.md -->
# AIDE Migration — Standard

> **Identity:** `AIDE_Migration@v1`
> **Common name:** Migration
> **Version 1** (2026-08-29). First published transition authoring, fast-check, execution,
> checkpoint, failure, and resumption contract.

---

## Purpose

Safely move a dependent artefact from its last proven dependency conformance checkpoint toward the
currently available dependency version using owner-declared transitions rather than inferred deltas.

## Transition posture

Every released migratable capability version declares exactly one posture:

```text
Required | OnUpdate | None
```

- `Required` — applicable work must complete before affected use.
- `OnUpdate` — old state remains usable; apply on the next modification/save.
- `None` — no state change is required for existing consumers.

Posture is version-level. Items inside one version do not mix postures.

## MigrationSummary

Expose a compact summary:

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8   # optional
```

Use the summary as a cheap negative/possible-work test. It does not replace detailed transition
history or Scope evaluation.

Where skill headers or equivalent metadata are eagerly loaded/discoverable, platform builds should
surface this summary there and load detailed transition instructions only when the summary indicates
possible work.

## Transition declaration

For each released version:

```yaml
Transition:
  Version: v18
  Posture: Required | OnUpdate | None
  Scope: <optional AIDE_Scope declaration>
  Change: <why existing consumers are affected>
  Items:
    - <ordered transition instruction>
  Success: <how completion is proven>
```

`None` may contain only version and posture.

Transition instructions must be explicit enough to produce the required state and establish
success. They may invoke existing Tools. Do not encode generic platform packaging/invocation
mechanics in the canonical transition.

## Required check

When an artefact is about to be relied upon for relevant use:

1. query its versioned dependencies;
2. compare each checkpoint with `LatestRequiredVersion`;
3. load detailed transition history only where Required work may exist;
4. evaluate Scope/current state; and
5. if applicable Required work remains, migrate before affected use continues.

There is no general Migration startup sweep. `!!` remains the Dependencies startup-presence
posture.

## OnUpdate

When an artefact is modified/saved, reconcile pending migration work through the current available
version.

OnUpdate does not block ordinary use. If Required work causes a save, apply pending applicable
OnUpdate work in that same update where possible.

## Ordering

- Discover relevant pending work before changing the artefact.
- Process dependencies in their declared order unless a more specific governing order applies.
- Process versions oldest to newest.
- Process items within one version in declared order.
- Re-evaluate applicability before each version.
- Stop on unresolved conflict rather than silently choosing.

## Checkpoint

The dependency conformance version is the last **saved, proven** checkpoint.

- Do not advance it because a newer version merely exists.
- Persist a new checkpoint only when the artefact itself is updated/saved.
- `None` and `NotApplicable` count as traversed for the next saved checkpoint.
- On partial success, persist only through the last successful version.

## Outcomes

`Completed` — applicable work succeeded.

`NotApplicable` — the dependency applies but the transition does not; treat the version as traversed
for the next saved checkpoint.

`Deferred` — applicable work was authoritatively postponed; do not advance through it; maintain a
Migration-owned temporary state entry and surface the consequence.

`Failed` — execution could not complete; discard partial changes from the failed version, preserve
prior successful work/checkpoints, maintain temporary state, and report noisily.

## Failure state

On defer/failure, write/update a compact owner-labelled state entry using the generic document-state
location/rendering supplied by the governing document methodology. Include enough information to
understand the current condition, and where known state what would make the migration succeed.
Remove the Migration-owned entry after a later successful update resolves it.

## Exact-version constraints

If a dependency uses an exact-version requirement, follow the migration treatment defined by the
applicable governing Standard/document rule. That rule may preserve the pin, move it, relax it, or
require follow-on actions.

If no governing rule determines the treatment, stop and escalate rather than infer.

## Supported baseline

Retain detailed history needed to migrate from the oldest supported conformance version to current.
If `SupportedBaseline` is declared, a consumer older than it is outside the normal migration path
and requires explicit recovery/upgrade handling.

## Failure and safety

- Missing required transition history → fail loudly.
- Dependency version regression → report; do not treat as forward migration.
- Dependency state changes mid-run → stop and resume after state stabilises.
- Concurrent artefact modification → do not overwrite newer work.
- Ambiguous/contradictory transition instruction → stop and identify the owning version.
- Re-running resumes from persisted successful checkpoints and must not duplicate completed work.

---

**Depends on:** `Capabilities_Migration_Design_v1`, `AIDE_Dependencies@v2`, `AIDE_Scope@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Migration_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Migration_Tool_v1.md -->
# AIDE Migration — Tool

> **Identity:** `AIDE_MigrationTool@v1`
> **Common name:** Migration
> **Version 1** (2026-08-30). Canonical platform-independent Migration Tool produced from
> `Capabilities_Migration_Tool_Design_v1`.

---

## Purpose

Check, apply, update, resume, and report migration of dependent artefacts under
`AIDE_Migration@v1`, preserving truthful saved conformance checkpoints and durable partial
progress.

## Logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v1
  CommonName: Migration
  PrimaryInvocation: migration
  LogicalActions: [Check, Apply, Update, Resume, Status]
```

Platform Build may render these actions as slash commands, skills, UI actions, or conversational
intents without changing their semantics.

## Trigger and inputs

Run when affected use requires a Required check, an artefact modification qualifies for OnUpdate,
a migration action is requested, unresolved Migration state is resumed, or another governing
Standard/Tool invokes Migration.

Resolve target artefact, dependencies and Dependency Query facts, applicable `MigrationSummary`,
detailed transitions when needed, current operation/authority, exact-version governing policy, and
existing Migration-owned state.

Infer safe low-cost facts; ask once for genuinely missing information; escalate substantive
ambiguity or authority conflict.

## Check

1. Query relevant versioned dependencies.
2. For use, compare checkpoints to `LatestRequiredVersion`.
3. For update, compare checkpoints to current/OnUpdate summary state.
4. Load detailed history only where the summary indicates possible work.
5. Evaluate supported baseline and Scope.
6. Return pending Required/OnUpdate work, traversable None/NotApplicable state, defer/failure state,
   and blocking conditions.
7. Make no artefact change.

## Apply

1. Resolve all relevant pending work before changing state.
2. Process dependencies by declared processing precedence unless specifically overridden.
3. Process versions oldest to newest and items in declared order.
4. Re-evaluate applicability before each version.
5. Apply items and verify each version's `Success` condition.
6. Preserve durable success stepwise.
7. When Required causes a save, continue through pending applicable OnUpdate/None versions to
   current where possible.
8. Save only proven state and advance checkpoints only through successfully traversed saved state.
9. Remove Migration-owned temporary state when resolved.

## Update

Perform the intended artefact modification together with all applicable Required and OnUpdate work
through current. Do not stop merely because Required work exists: the operation is already a
qualifying save event.

If work cannot complete, preserve only the last successful state/checkpoint and surface the
unresolved condition.

## Resume

Read persisted checkpoints/state, re-resolve current dependency facts, confirm earlier durable
success, and continue from the first unresolved version without replaying completed work.

## Status

Report artefact, dependency, checkpoint, available/current version, summary relation, pending
Required/OnUpdate work, supported-baseline result, clear/deferred/failed state, and next action.

## Failure and integrity

- Failed version: discard that version's partial changes; keep prior successful work/checkpoint;
  write/update compact Migration-owned state and report noisily.
- Deferred: preserve authorised deferral and consequence; do not advance through it.
- Concurrent artefact change: do not overwrite newer work.
- Moving dependency facts: stop and resume against stable state.
- Missing/ambiguous transition or exact-version treatment: stop and identify the unresolved owner
  decision rather than infer it.

Check/Status are read-only and idempotent. Apply/Update/Resume are resumable and must not duplicate
already completed version work.

## Reporting

Summary reporting states what was checked/applied, resulting checkpoints, and anything still
blocking or needing attention. Failure, defer, unsupported baseline, exact-version ambiguity, and
conflict always surface regardless of narration preference.

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

**Depends on:** `AIDE_Migration@v1`, `AIDE_Dependencies@v2`,
`Capabilities_Migration_Tool_Design_v1`.

**References:** `AIDE_Scope@v1`.

**Type:** `Tool` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Migration_Tool_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Principles_Standard_v1.md -->
# AIDE Principles — Standard

> **Identity:** `AIDE_Principles@v1`
> **Common name:** Principles
> **Version 1** (2026-08-31). First canonical Principles contract produced from
> `Principles_Design_v3`.
>
> **Default weight:** Expectation

## Purpose

Provide portable base reasoning and problem-solving guidance for AI-assisted work.

This Standard may be used as part of full AIDE or independently.

## Base guidance

### Value over compliance

Prefer rules and mechanisms that create/protect real value. Re-examine rules whose compliance cost
exceeds what they enable or protect.

### Purpose before mechanism

Establish what something is for before designing how it works. Do not solve an unclear model by
adding mechanism.

### Model before elaboration

State the current model before deep detail. Check later mechanisms against that model rather than
letting detail silently replace it.

### Keep the working set human-comprehensible

Keep the active conceptual set small enough for the human owner to understand and challenge.
Progress through intent/premises, model, then detail.

### Authoritative evidence over incidental inference

Prefer declarations and model-defined authoritative structural relationships over conclusions from
mere presence, proximity or naming coincidence.

Inference is valid where the governing model defines the evidence that supports it.

### Information holder decides the boundary

When ownership/routing is ambiguous, prefer the component/project/Domain that holds the information
required to decide correctly rather than territorial ownership.

### Observation over prediction

Design mechanisms primarily against demonstrated needs/failures. Leave room for likely future
capability without building unused machinery prematurely.

### Loud failure over quiet absorption

When authoritative completion is not possible, surface the unresolved condition clearly rather
than producing output that merely looks complete.

### Verified truth over plausible assertion

Where a fact should be observed/read and an authoritative source is reasonably available, read it.
If verification is unavailable, state the uncertainty instead of composing a plausible value.

### Confirmed state over assumed state

Do not treat proposed/generated/handed-off state as applied/deployed/verified state without evidence
from the authority or environment that can perform/observe the change.

## Guidance Profiles

This is base guidance.

An applicable organisation/group/team/user Guidance Profile may:

```text
Add
Refine
Override
```

named guidance using a small delta.

Unmentioned base guidance remains effective. Equal-specificity conflict fails visibly unless an
explicit ordering exists.

Do not create copied/forked complete Standards solely to customise the base.

Host/platform instructions and other higher-priority governing constraints remain outside this
profile model.

## Relationship to Working Practices

Principles states judgement premises. `AIDE_WorkingPractices` states concrete collaboration and
operating conventions that may implement these premises.

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
Dependencies: !AIDE_DocumentationMethodology@v19
References: Principles_Design_v3
<!-- END SOURCE: AIDE_Principles_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_ProjectDesign_Standard_v2.md -->
# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v2`
> **Common name:** Project Design
> **Version 2** (2026-08-31). Adds explicit downstream-consequence capture and WorkRegister-to-WorkPackage reconciliation while preserving the established Project Design model.
>
> **Default weight:** Expectation

---

## Purpose

Define substantial work coherently before execution: establish intent and requirements, determine the current model/approach, review proportionately, and hand execution to Build through a complete WorkPackage where needed.

## Apply proportionately

Use the amount of structure justified by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Establish the work

For work that needs design, establish enough of the following to remove material ambiguity:

- objective/need and intended outcome;
- authorised scope and non-goals;
- requirements and constraints;
- material assumptions/uncertainties;
- decisions and credible alternatives where consequential;
- the current design/model/approach; and
- defined deliverables or acceptance signals.

Do not allow detailed implementation to become the place where unresolved design is silently decided.

## Use a layered checkpoint for substantial design

Before descending into extensive mechanics, maintain a compact view of:

1. **Intent/system:** purpose, premises, ownership/boundaries, inputs/outputs and surrounding relationships.
2. **Model:** principal concepts, responsibilities, relationships, lifecycle/flow and major rules.

If this view is difficult to make clear, reassess the model before adding mechanisms.

## Record authoritative state

Design records the current confirmed position. Decisions record material reasoning and rejected alternatives. Downstream outcomes consume the confirmed Design/defined outcome, not Decisions history.

Confirmed material must be written according to the governing Documentation Methodology rather than left only in conversation.

## Track undelivered Design consequences

Whenever the confirmed Design changes, identify the downstream outcomes that must change for
delivered reality to remain aligned.

For each consequence:

```text
fully delivered in the same pass → no standing obligation remains
not fully delivered               → record in the owning top-level topic's WorkRegister
```

The WorkRegister entry must state the source Design change and required downstream code/build/
document/production changes in enough detail that later delivery can be reconciled. WorkRegister is
not a list of undecided ideas; it records already-confirmed work/consequences that remain owed.

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v2`.

A WorkPackage may be created directly from defined work or select manageable portions of one or
more WorkRegister obligations. Where it is sourced from WorkRegister, identify the source item IDs
and the portion of each obligation covered.

The package must make the required result, authority, work-specific inputs and acceptance clear.
WorkRegister references are traceability, not a substitute for a self-contained execution contract.
Do not embed generic execution-platform knowledge already supplied by the Build environment.

## Handle Build return

On Build Outcome:

- reconcile returned evidence against each mapped WorkRegister obligation where applicable;
- remove a WorkRegister item only when its full confirmed consequence is actually delivered;
- retain partial/blocked items with the returned result and remaining work;
- close/record completion when acceptance and the committed outcome are satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

Build may resolve implementation detail within authority; it does not silently change objectives,
major scope, acceptance or architecture and does not silently close the owning WorkRegister.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

---
Dependencies: !AIDE_DocumentationMethodology@v21, ProjectDesign_Design_v2, AIDE_Review@v1
References: AIDE_WorkPackage@v2
<!-- END SOURCE: AIDE_ProjectDesign_Standard_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Review_Standard_v1.md -->
# AIDE Review — Standard

> **Identity:** `AIDE_Review@v1`
> **Common name:** Review
> **Version 1** (2026-08-29). First published contract for purposeful independent assessment,
> proportionate assurance, lifecycle control, and disposition.

---

## Purpose

Provide a stable way to bring a meaningfully independent reasoning source into work, obtain
insight or challenge shaped to the actual objective, manage the exchange proportionately to risk,
and return a clear result without transferring ownership of the work to the Reviewer.

## Applicability

Apply this Standard whenever an activity is identified as a Review, whether initiated directly,
recommended by an AI, required or recommended by a governing Standard/workflow, configured by a
WorkPackage, or triggered by consequence/risk.

A mechanical self-check, document-format validation, or independent research task is not a Review
merely because it tests something. It uses this Standard only when it creates the Lead/Reviewer
assessment lifecycle defined here.

## Governing principles

- Review introduces a second reasoning path to improve substantive integrity, decisions, and risk
  management.
- The Lead owns the work and its final disposition. The Reviewer owns Findings.
- A Finding is evidence, not an instruction.
- Type, Level, Mode, and Reviewer are independent Review inputs.
- Review effort and stopping confidence are proportionate to Level.
- Review may discover beyond authorised scope; execution may not silently expand beyond it.
- Review owns the exchange and its state. Communication owns delivery.
- A separate Review document is optional; reconstructable Review evidence is not.
- Review stops at justified confidence or explicit judgment, not perfection.

## Roles

### Lead

The Lead owns the current work, states or validates the Review objective and authorised scope,
supplies an accurate account of the work, handles the response, owns Finding disposition, and
preserves the net coherence and simplicity of the resulting work.

### Reviewer

The Reviewer provides the separate reasoning path. It applies the effective Type, Level, and Mode;
reports material Findings with evidence/reasoning and uncertainty; and may offer possible remedies
without treating them as requirements.

### Role assignment

Roles are contextual. The AI/platform responsible for or initiating the current work is normally
the Lead. The environment resolver supplies a meaningfully independent default Reviewer and may be
overridden explicitly.

The same AI family is not permanently Lead or Reviewer. Roles can reverse across work, and actual
models may change between Rounds. Every Round records the actual Lead model and Reviewer model.

## Trigger contract

A Trigger provides:

- `Source` — user/Lead, AI recommendation, governing Standard/workflow/project rule, WorkPackage,
  or risk/consequence condition;
- `Basis` — why Review is warranted now;
- `Posture` — `Required`, `Recommended`, or `Optional`;
- `Subject`; and
- optional suggested `Type` and `Level`.

The trigger source owns its criteria. Review resolves and executes the resulting Review.

An AI should recommend Review where consequence, reach, difficulty of reversal, uncertainty,
novelty, weak evidence, or a valuable second perspective makes the expected benefit material.
Recommendation does not become requirement unless the governing source makes it one.

`Stress Test` may be recommended but starts only after explicit user direction.

## Review Input Contract

Before the first request is sent, resolve:

```yaml
ReviewInput:
  Trigger:
    Source: <identity>
    Basis: <reason>
    Posture: Required | Recommended | Optional
  Subject: <thing or question under review>
  Objective: <what the Review is trying to learn or determine>
  AuthorisedScope: <execution boundary>
  Type: Check | Inspect | Evaluate | Robust | Stress Test | <omitted when DirectProfile is used>
  DirectProfile: <optional purpose, learning objective, lens/method, response expectations>
  Level: Low | Standard | Medium | High | Extreme
  Mode: Full | Blind
  Reviewer:
    Identity: <review source>
    RequiredCapabilities: <where applicable>
  ReviewMaterial: <context, artefacts, evidence, constraints, assumptions, uncertainties>
  ResponseExpectations: <useful payload>
  ContinuationPosture: <Type and Level informed>
```

`DirectProfile` lets the caller supply the profile content for a one-off Review. It does not add a
sixth Type or create a new reusable Profile.

Values resolve in this order:

1. direct instruction for this Review;
2. trigger or work-item configuration;
3. selected Review Profile defaults;
4. shared Review operating defaults;
5. environment-local availability/defaults.

Defaults fill gaps and never silently override an explicit value. Surface a conflict between
authoritative sources rather than choosing one without notice. Ask only for input that cannot be
safely resolved from the work and available configuration.

## Type

Type defines why the Review is being performed, what it is trying to learn, the lens/method the
Reviewer applies, and the expected response.

The standard profiles are defined only in `AIDE_ReviewProfiles@v1`:

```text
Check → Inspect → Evaluate → Robust → Stress Test
```

This ordering describes increasing distance from the current claim/artefact/design, not increasing
thoroughness. Level controls intensity.

## Level

Level defines the assurance effort, capability, independence, evidence, iteration, and stopping
confidence justified by the work.

Assess Level over four factors:

- `Consequence` — severity if wrong;
- `Reach` — downstream breadth;
- `Reversibility` — cost/difficulty of correction; and
- `Uncertainty` — novelty, ambiguity, assumption load, and evidence weakness.

Use judgment, not a score. Do not average away one serious factor. Work size and complexity may
inform but do not determine Level.

| Level | Meaning | Review posture |
|---|---|---|
| Low | Low consequence; easy to reverse | Quick focused pass; surface obvious/material issues; stop early. |
| Standard | Normal consequence and uncertainty | Normal independent review with reasonable evidence checking and further Rounds where useful. |
| Medium | Material consequence, uncertainty, reach, or difficulty of reversal | Stronger capability; broader examination; challenge assumptions; normally re-review substantive change. |
| High | Significant consequence or systemic risk | Deep independent review; substantial evidence; high confidence threshold; persist while material issues remain. |
| Extreme | Exceptional or critical consequence | Best justified available capability; maximum practical independence/evidence; very high confidence threshold; rare. |

Higher Level increases strength, not Type. Actual model names and routes are environment data.

### Dynamic Level

Reassess Level when a material Finding changes the understood consequence, reach, reversibility,
or uncertainty. Escalate or de-escalate accordingly, record a short reason, and re-resolve
Reviewer/model/route for the next Round when needed.

A Level change affects subsequent behaviour and does not invalidate completed Rounds.

## Mode

Mode controls exposure to the Lead's existing solution or reasoning:

- `Full` — expose the current approach, reasoning, artefacts, and relevant context.
- `Blind` — withhold selected solution/reasoning content to reduce anchoring and elicit an
  independent approach.

Blind Mode does not withhold information needed to answer the objective accurately. Record what
was deliberately withheld.

## Reviewer resolution

Resolve Reviewer after Type, Level, Mode, and required evidence/capabilities are known, and before
final request packaging.

The Reviewer is a review source/family, not a permanently pinned model version. Environment data
supplies:

- available reviewer identities/families;
- actual models and capability tiers;
- evidence/file/repository/web capabilities;
- independence characteristics;
- routes from the current surface;
- availability, usage, access, and cost constraints; and
- fallbacks.

Review does not define where that environment data is stored.

## Review Request

Build the request to maximise the chance of an effective and accurate Review for the objective.
Include:

- Review and Round identity;
- Subject, Objective, and AuthorisedScope;
- effective Type purpose/lens and Level expectations;
- Mode and deliberate withholding;
- sufficient relevant ReviewMaterial;
- constraints, assumptions, uncertainties, and evidence;
- specific questions/instructions; and
- ResponseExpectations.

The request is accurate, sufficient, relevant, attackable, and non-persuasive. It exposes the work
without arguing the Lead's conclusion or including context merely because it exists.

## Routing and communication

Review hands an external communication capability:

```yaml
ReviewDelivery:
  CurrentSurface: <surface>
  Reviewer: <resolved reviewer>
  ReviewId: <identity>
  RoundId: <identity>
  Request: <complete review request>
```

The communication capability owns route selection, send/return mechanics, packaging constraints,
delivery state, and failures.

For indirect/manual communication, use the existing AI Message format as the envelope. Supply the
user with destination, requested model/capability, instructions, a ready-to-copy message, and exact
return instructions. Use a Markdown file where the request is exceptionally large.

Do not embed platform-to-platform routes or transport implementation in Review.

## Response contract

Act on a response only after it is correlated to one Review and Round.

```yaml
ReviewResponse:
  ReviewId: <identity>
  RoundId: <identity>
  Reviewer: <actual reviewer identity>
  ActualModel: <actual model, if known>
  Status: Complete | Partial | ClarificationNeeded | Failed
  Payload: <Type-defined review response>
  ContinuationSignal: <optional material-value signal>
```

Preserve the response unchanged in the Round record. A partial or clarification-needed response
keeps the Review open. An uncorrelated response is held for clarification and is not dispositioned.

## Lifecycle and states

The stable Review states are:

```text
Initiated
Awaiting Response
Response Received
Continuing
Complete
Escalated
```

Normal flow:

```text
Initiated
  → request resolved and sent
Awaiting Response
  → correlated response returned
Response Received
  → Lead handles Findings and change
Continuing | Complete | Escalated
```

There is no hard Round limit. After every handled response, determine whether:

- another Round is likely to add material information;
- unresolved Findings remain material to the current Level;
- Review-driven changes require verification;
- sufficient confidence has been reached; or
- the remaining matter is a user/work-owner judgment.

Continue, complete, or escalate from that assessment. Do not continue merely because further
imperfections can be imagined.

## Round record

Rounds are append-only. Each Round records:

- Review/Round identity and number;
- actual Lead identity/model;
- actual Reviewer identity/model;
- effective Type, Level, and Mode;
- request and supplied material;
- route/transport reference where useful;
- response unchanged;
- Findings and Lead dispositions arising from the Round;
- changes made;
- outcome; and
- reason for continuing, completing, or escalating.

Later Rounds may refer to earlier Rounds but do not replace them.

## Findings and disposition

A Finding preserves:

- observation;
- materiality/why it matters;
- evidence or reasoning;
- uncertainty;
- likely consequence/risk; and
- optional remedy.

The Lead records one or more dispositions:

```text
Accept | Decline | Defer | Supersede | Investigate | Change | Escalate
```

The Finding remains unchanged. A remedy is advisory until adopted. The Lead records the resulting
change or reason for no change and the re-review decision.

## Re-review

Re-review evaluates the revised outcome and whether it resolves the Finding without introducing
new problems.

| Level | Re-review expectation |
|---|---|
| Low | Re-review when the Lead judges the change material. |
| Standard | Re-review material changes or significant Finding resolutions. |
| Medium | Normally re-review substantive changes in reviewed scope. |
| High | Return substantive Review-driven changes before completion. |
| Extreme | Re-review material remediations as part of the cycle; the resulting state normally must survive Review. |

Minor editorial/local change that does not materially alter what was assessed does not require a
new Round.

## Scope control

Review may identify an issue outside AuthorisedScope. Neither Lead nor Reviewer may implement it
under the current authority.

Mark the Finding `OutOfScope` and return:

- the Finding;
- why it matters;
- likely consequence/risk; and
- suggested direction where useful.

The director/work owner decides re-scope, separate work, defer, or decline. This rule applies
strictly to WorkPackages and directed work.

## Review Result

Every completed or escalated Review returns:

```yaml
ReviewResult:
  ReviewId: <identity>
  Subject: <subject>
  ScopeReviewed: <scope>
  Type: <named Type, or DirectProfile>
  FinalLevel: <level>
  Mode: <mode>
  ReviewersAndModels: <actual Round history summary>
  Outcome: Complete | Escalated | Unresolved
  MaterialFindings: <summary with dispositions>
  ChangesWithinScope: <summary>
  ReReviewStatus: <required/completed/not required/outstanding>
  OutOfScopeFindings: <summary>
  ResidualRisks: <accepted or unresolved differences>
  CompletionReason: <why Review stopped>
```

The Result tells the director of work what was reviewed, what mattered, what changed, what remains,
and what needs attention without requiring reconstruction of the exchange.

## Persistence

Every Review preserves the Review Result and enough Round evidence to reconstruct what happened.

Use the surrounding work record for routine/transient Review where it can preserve the required
semantics, including a WorkPackage Outcome.

Create a separate Documentation Methodology `Review` document where Review is substantive
design-side evidence, High/Extreme, materially multi-Round, carries significant unresolved or
out-of-scope Findings, is required as assurance evidence, or is explicitly requested.

A durable Review document follows the governing document methodology. It contains the Review
Result and the complete Rounds or stable references to them. Review does not create a competing
record type.

## Failure handling

- Preserve request, identity, and route state after delivery failure so the same Round can be
  retried or rerouted.
- Do not report delivery success as Review completion.
- Do not silently skip Required Review; record an authorised exception and accepted consequence.
- Do not mark a Finding resolved because a change was attempted.
- Do not infer permission to expand scope from a Finding.
- Surface unavailable independence/capability rather than claiming the selected Level was met.

## External seams

Review consumes but does not own:

- environment configuration for reviewer/model/route availability and local mappings; and
- a shared communication capability for direct delivery, indirect AI Message relay, and response
  return/correlation.

These seams remain explicit until their architecture owners and storage contracts are separately
confirmed.

---

**Depends on:** `Capabilities_Review_Design_v1`.

**References:** `AIDE_ReviewProfiles_Standard_v1`, `Capabilities_Design_v5`,
`Capabilities_Tools_Design_v1`, `DocumentationMethodology_Guide_v17`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Review_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Review_Tool_v1.md -->
# AIDE Review — Tool

> **Identity:** `AIDE_ReviewTool@v1`
> **Common name:** Review
> **Version 1** (2026-08-30). Canonical platform-independent Review Tool produced from
> `Capabilities_Review_Tool_Design_v1`.

---

## Purpose

Initiate, resolve, construct, route, record, continue, and conclude one proportionate independent
Review lifecycle while preserving Lead ownership, authorised scope, Round evidence, and the
external communication boundary.

## Logical actions

```yaml
Tool:
  Identity: AIDE_ReviewTool@v1
  CommonName: Review
  PrimaryInvocation: review
  LogicalActions: [Start, Receive, Continue, Status, Complete]
```

Platform Build may render these actions through commands, skills, UI actions, or conversational
intent without changing their semantics.

## Trigger and Scope

Run on explicit Review request, accepted AI recommendation, governing Review Trigger, WorkPackage
Review posture, qualifying consequence/risk trigger, or receipt of a correlated response for an
active Review.

The Tool may recommend Review when consequence, reach, reversibility, uncertainty, novelty, weak
evidence, or a valuable second reasoning path makes the expected benefit material. It must not
turn recommendation into requirement. Stress Test starts only on explicit user direction.

```yaml
Scope:
  Context: >
    Apply when a purposeful independent assessment exchange is requested, accepted, required,
    recommended for material value, or resumed from a correlated Review response.
```

## Start

1. Resolve the Review Trigger, Subject, Objective, Authorised Scope, Type/profile, Level, Mode,
   Reviewer requirements, material, response expectations, and continuation posture under
   `AIDE_Review@v1`.
2. Use direct instruction, work configuration, Review Profile defaults, shared defaults, then
   environment data in that precedence.
3. Infer strong low-risk facts and state them; batch questions for genuinely missing inputs;
   escalate authoritative conflicts.
4. Resolve a meaningfully independent Reviewer/model/route from the environment. If the requested
   Level cannot be met, surface the shortfall rather than claiming it was performed.
5. Shape sufficient relevant, attackable, non-persuasive material. In Blind Mode withhold only the
   anchoring content needed to achieve the objective.
6. Create Review/Round identity and the purpose-shaped Review Request.
7. Preserve the request/material list before handing it to the external communication capability.
8. Record route/delivery state and set the Review to `Awaiting Response`.

For an indirect route, use the shared AI Message mechanism and provide a copy-ready request plus
exact return instructions; Review does not implement transport itself.

## Receive

1. Correlate the returned response to exactly one Review and Round.
2. Preserve the response unchanged and record actual Reviewer/model.
3. Record response status: Complete, Partial, ClarificationNeeded, or Failed.
4. Hold an uncorrelated response for clarification; do not disposition it.
5. Surface material Findings to the Lead while preserving Reviewer ownership of Finding text.
6. Record Lead disposition, in-scope changes, re-review need, out-of-scope findings, and residual
   risk.

## Continue

After a usable response/change:

1. reassess consequence, reach, reversibility, and uncertainty;
2. record any Level change and reason;
3. re-resolve Reviewer/model/route if needed;
4. apply Level-specific re-review expectations;
5. continue only while another Round is likely to add material value; and
6. set `Continuing`, `Complete`, or `Escalated` without imposing a fixed Round cap.

Review discovery never silently expands authorised execution scope.

## Status

Return Review identity/state, Subject, current Type/Level/Mode, Reviewer/model/route where known,
Round count/current Round, response state, unresolved material Findings/dispositions, re-review
requirement, out-of-scope findings, and next action.

## Complete

Produce the `ReviewResult` required by `AIDE_Review@v1`: scope reviewed, effective Type/final Level/
Mode, actual Reviewer/model history, outcome, material Findings and Lead dispositions, changes,
re-review state, out-of-scope Findings, residual risks, and completion reason.

Store the result and reconstructable Round evidence in the surrounding work record for transient
Review or in a durable Documentation Methodology Review artefact where the persistence rule
requires it.

## Failure and integrity

- Required Review cannot be silently skipped; authorised exception and consequence are recorded.
- Delivery failure preserves request/route state for retry/reroute.
- Partial/clarification response keeps Review open.
- Transport success is not substantive Review completion.
- A Finding is not resolved merely because a fix was attempted.
- Reviewer/model change is explicit in the next Round.
- Re-running status/receive handling must not duplicate Round evidence or dispositions.

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

**Depends on:** `AIDE_Review@v1`, `AIDE_ReviewProfiles@v1`,
`Capabilities_Review_Tool_Design_v1`.

**References:** `AIDE_Scope@v1`.

**Type:** `Tool` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Review_Tool_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_ReviewProfiles_Standard_v1.md -->
# AIDE Review Profiles — Standard

> **Identity:** `AIDE_ReviewProfiles@v1`
> **Common name:** Review Profiles
> **Version 1** (2026-08-29). First published definitions of Check, Inspect, Evaluate, Robust,
> and Stress Test, with default Levels, Modes, response expectations, and continuation guidance.

---

## Purpose

Define reusable Review methods over the `AIDE_Review@v1` Input Contract so a caller can select a
purposeful review lens without rebuilding its instructions each time.

## Profile contract

Every reusable Review Profile defines:

- `Name` — stable Type identity;
- `Purpose` — why the Type exists;
- `LearningObjective` — what the Review is trying to find out;
- `Boundary` — how far outside the current claim/artefact/design it may step;
- `LensMethod` — how the Reviewer approaches the work;
- `EvidenceExpectations` — what verification, comparison, or external evidence is expected;
- `ExpectedResponse` — what a useful payload contains;
- `DefaultLevel`;
- `DefaultMode`; and
- `ContinuationGuidance`.

Type defaults fill unresolved inputs. They do not override an explicit value or the effective Level
assessment for the actual task.

## Shared Type rules

- Choose Type from what the Review is trying to learn, not how important the work is.
- Type determines method; Level scales how strongly that method is applied.
- A Type may expose a more serious issue and justify switching Type in a later Round. Record the
  change and reason rather than silently broadening the active Type.
- Report material issues first. Do not propose complexity merely because an imperfection can be
  removed.
- Evidence and remedies are proportionate to Level and the Review objective.
- Level-based re-review rules in `AIDE_Review@v1` apply to every Type.

## Default matrix

| Type | Boundary | Default Level | Default Mode | Core question |
|---|---|---:|---|---|
| Check | Criterion-bound | Low | Full | Is this specific proposition or condition correct/satisfied? |
| Inspect | Artefact-bound | Standard | Full | What is wrong, missing, inconsistent, weak, or materially improvable? |
| Evaluate | Outcome-bound | Medium | Full | Does this approach deliver the intended outcomes well, and how could it be better? |
| Robust | Design/framing-bound | High | Full | Is the design itself sound, and where could its assumptions or structure fail? |
| Stress Test | Environment/adversary-bound | Extreme | Full | How does this withstand capable adversarial, competitive, or demanding external scrutiny? |

`Evaluate + Blind` is the normal form for an independent approach before the Lead's solution is
shown. Blind Mode remains an explicit selection because many Evaluate Reviews need to assess the
current approach directly.

## Check

### Purpose

Determine whether a specific proposition, requirement, calculation, contract point, expected
result, or condition is correct or satisfied.

### Learning objective

> Is the stated criterion met, and what evidence supports that answer?

### Boundary

Check is criterion-bound. It verifies the stated target and does not become a general search for
defects. If the check exposes a broader material issue, report it and recommend an appropriate
Type/Level change.

### Lens and method

- identify the exact claim or criterion;
- establish the authoritative evidence or test;
- verify the result and relevant assumptions;
- distinguish pass, fail, qualified/conditional result, and unknown;
- identify any evidence gap that prevents a reliable answer.

### Evidence expectations

Use evidence directly relevant to the criterion. At higher Levels, independently verify the
source, calculation, test, or trace from requirement to result rather than accepting an assertion.

### Expected response

- answer: Pass, Fail, Qualified, or Unknown;
- criterion applied;
- supporting evidence/test;
- defect or unmet condition where present;
- uncertainty/evidence gap; and
- any broader issue requiring another Type.

### Defaults and continuation

- `DefaultLevel: Low`
- `DefaultMode: Full`
- normally complete after a reliable answer;
- continue for missing evidence, material ambiguity, or verification of a material correction;
- do not broaden into Inspect without an explicit Type change.

## Inspect

### Purpose

Examine an existing artefact, implementation, document, code change, plan, or outcome for defects,
omissions, inconsistencies, drift, and meaningful improvement.

### Learning objective

> What is wrong, missing, inconsistent, weak, or materially improvable in what exists?

### Boundary

Inspect is artefact-bound. It accepts the authorised design/intent as the governing frame and
tests the artefact against it. It can identify a better local approach, but it does not redesign
the governing model unless a Finding justifies an Evaluate or Robust escalation.

### Lens and method

- inspect the artefact itself rather than only its description;
- compare against authoritative requirements, intent, scope, interfaces, and expected outcomes;
- find defects, omissions, inconsistencies, weak implementation choices, and scope drift;
- consider straightforward alternatives where they materially improve the outcome;
- prioritise by materiality rather than volume.

### Evidence expectations

Use the artefact and its authoritative contract. At higher Levels, inspect supporting tests,
source material, dependency behaviour, execution evidence, and relevant adjacent effects.

### Expected response

- material Findings in priority order;
- affected location or element;
- evidence/reasoning and consequence;
- contract/intent comparison where applicable;
- uncertainty; and
- possible local improvement where useful.

### Defaults and continuation

- `DefaultLevel: Standard`
- `DefaultMode: Full`
- continue where material defects remain, accepted fixes materially change the artefact, or the
  current artefact cannot yet be tested reliably;
- recommend Evaluate/Robust when the defect appears to originate in the governing approach rather
  than the artefact.

## Evaluate

### Purpose

Assess whether a concept, design, decision, plan, or proposed approach delivers the intended
outcomes well and how it could be improved.

### Learning objective

> Does this approach meet the objective well, where does it fall short, and are there materially
> better alternatives?

### Boundary

Evaluate is outcome-bound. It may challenge important assumptions and compare credible
alternatives, but it begins from the premise that the proposed direction is a plausible design
worth assessing. It improves within or around that design; Robust may reject the design/framing
itself.

### Lens and method

- test fitness against objective, success criteria, constraints, and authorised scope;
- examine trade-offs, consequences, dependencies, and key assumptions;
- identify strengths, weaknesses, gaps, and avoidable complexity;
- compare credible alternatives where they could materially improve outcomes;
- avoid redesigning for marginal gains;
- distinguish decision input from a mandatory remedy.

### Evidence expectations

Use stated outcomes, constraints, evidence, and alternatives already considered. At higher Levels,
verify important assumptions and compare stronger external or internal approaches where available.

### Expected response

- overall assessment;
- material strengths and weaknesses;
- outcome/constraint fit;
- key trade-offs and consequences;
- credible alternatives and comparative advantage where relevant;
- recommendation or decision input;
- unresolved uncertainties.

### Defaults and continuation

- `DefaultLevel: Medium`
- `DefaultMode: Full`
- prefer `Blind` where the objective is an independent approach and exposure to the current
  solution would anchor the Reviewer;
- continue while materially different evidence, alternatives, or revised decisions are changing
  the assessment;
- complete when the Lead has sufficient decision-quality input for the Level, including an
  explicit residual uncertainty where necessary;
- change to Robust where the design/framing itself becomes the central question.

## Robust

### Purpose

Find material weaknesses normal inspection or evaluation may miss, including weaknesses caused by
the chosen design or framing itself.

### Learning objective

> Is this the right design, where can it fail or behave unexpectedly, and would a materially
> different design avoid the problem?

### Boundary

Robust is design/framing-bound. It may step back from the current design, challenge the problem
framing and foundational assumptions, and perform a blank-sheet comparison where consequence or
Findings justify it.

### Lens and method

- challenge foundational and operational assumptions;
- probe edge cases, unusual interactions, degraded states, and failure paths;
- look for hidden dependencies, second-order effects, and invalid safeguards;
- distinguish material failure modes from theoretical imperfections;
- step back and ask whether the problem is being solved in the wrong way;
- compare materially different designs when that exposes or avoids structural weakness;
- test whether added safeguards create disproportionate complexity.

### Evidence expectations

Inspect available evidence for assumptions, failure behaviour, interfaces, and safeguards. At
higher Levels, seek independent verification, precedents, or simulations where they materially
improve confidence. External threat/comparator research is not mandatory unless the objective
requires it; that is a defining Stress Test emphasis.

### Expected response

- material weaknesses/failure modes;
- trigger conditions and affected outcomes;
- evidence/reasoning and uncertainty;
- likely consequence and reach;
- challenged assumptions or framing;
- materially different design alternatives where justified;
- whether action appears proportionate; and
- residual risks or areas requiring judgment.

### Defaults and continuation

- `DefaultLevel: High`
- `DefaultMode: Full`
- use `Blind` where an independent blank-sheet framing is more valuable than direct critique;
- continue while material structural Findings, changed assumptions, or revised designs warrant
  further examination;
- substantive review-driven changes are normally returned under the High re-review posture;
- complete when material failure paths and design alternatives are adequately understood for the
  Level, not when every theoretical risk is removed.

## Stress Test

### Activation

Stress Test is user-activated only. An AI may recommend it and explain the expected value, but no
Standard, workflow, WorkPackage default, or autonomous risk trigger starts it without explicit
user direction.

### Purpose

Determine how well the subject withstands deliberate, intelligent, and sustained challenge,
including exploitation of weakness and comparison against strong external alternatives.

### Learning objective

> What could a capable adversary, competitor, hostile environment, demanding customer, auditor,
> or expert discover, exploit, outperform, or use against this?

### Boundary

Stress Test is environment/adversary-bound. It steps outside the current design to test the work
against hostile or demanding reality, known failures, credible threats, strong comparators, and
external scrutiny.

### Lens and method

- assume weaknesses will be actively sought rather than encountered accidentally;
- challenge foundational assumptions and combine weaknesses into realistic paths;
- identify plausible adversary/challenger objectives and capabilities;
- test technical, architectural, operational, commercial, process, and human surfaces selected by
  the Review objective;
- seek relevant known attacks, failures, precedents, solutions, benchmarks, and competitors;
- compare resilience against credible stronger approaches;
- distinguish theoretical possibilities from realistically exploitable/material weakness;
- identify where the subject is stronger as well as weaker;
- assess whether proposed mitigation is proportionate to the protected outcome.

### Optional Stress Test parameters

- `AdversaryOrChallenger`
- `AdversaryObjective`
- `SubjectScope`
- `ProtectedOutcomesOrAssets`
- `ChallengeSurfaces`
- `ComparatorSet`
- `Constraints`
- `AssumptionsToAttack`
- `EvidenceAccess`
- `MaterialityThreshold`

Resolve only the parameters relevant to the actual objective.

### Evidence expectations

Actively seek external examples, comparators, known failures, threat paths, benchmarks, or stronger
solutions where the Reviewer has the capability and the scope permits it. If required evidence
access is unavailable, state the limitation; do not present a speculative scan as an Extreme
Stress Test.

Research performed to support the Review remains evidence gathering inside this Review. A
standalone request to discover options or facts without the Review lifecycle belongs to Research,
not this Type.

### Expected response

- strongest material weaknesses first;
- realistic challenge/exploitation or outperformance scenarios;
- external examples/comparators and their relevance;
- consequence, likelihood/materiality, and uncertainty;
- performance of current safeguards/design against the challenge;
- comparative strengths as well as weaknesses;
- residual risks that cannot reasonably be eliminated;
- proportionate mitigation directions; and
- questions requiring user/Lead judgment.

### Defaults and continuation

- `DefaultLevel: Extreme`
- `DefaultMode: Full`
- continue while material challenge paths, combined weaknesses, comparator evidence, or material
  remediations remain insufficiently tested for Extreme confidence;
- re-review material remediations as part of the cycle;
- stop when major paths are adequately explored and dispositioned, further Findings are marginal
  or speculative, or the residual issue is an explicit strategic/risk judgment;
- never pursue complexity solely to eliminate a theoretical weakness.

## Type changes and combined objectives

Use one primary Type per Round so the request has a clear learning objective. Where a Review needs
multiple lenses:

- sequence them as separate Rounds or separate Reviews when each needs a distinct response;
- state the primary Type and a narrow secondary question where separation would add no value; or
- change Type after a Finding exposes a materially different question.

Record each Round's effective Type. Do not create hybrid names such as `Robust-Deep`; Level already
expresses intensity.

## Five-use-case defaults

| Use case | Normal starting profile | Common variation |
|---|---|---|
| Design exploration | Evaluate + Medium + Full | Blind for an independent approach; Robust when framing itself is uncertain. |
| Pre-confirmation design | Evaluate + Medium | Robust + High for foundational or hard-to-reverse design. |
| WorkPackage authoring | Check + Low or Inspect + Standard | Raise Level when incorrect scope/contract would have material downstream reach. |
| Build plan | Evaluate + Medium | Robust + High for consequential architecture or weak assumptions. |
| Post-execution | Inspect + Standard | Robust + High where implementation or design integrity requires broader challenge. |

These are starting defaults. Effective Level follows consequence, reach, reversibility, and
uncertainty; explicit work configuration or instruction may select another Type/Mode.

---

**Depends on:** `AIDE_Review_Standard_v1`, `Capabilities_Review_Design_v1`.

**References:** `Capabilities_Design_v5`, `Capabilities_Standards_Design_v3`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_ReviewProfiles_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Scope_Standard_v1.md -->
# AIDE Scope — Standard

> **Identity:** `AIDE_Scope@v1`
> **Common name:** Scope
> **Version 1** (2026-08-28). First published applicability contract using Tags plus contextual
> AI judgment.

---

## Purpose

Define whether a Standard, Tool, rule, behaviour, or other referenceable capability applies in
the current context.

## Declaration

```yaml
Scope:
  Machine: design & !archived
  Context: >
    Apply when the work could affect governed documentation behaviour.
```

Either `Machine` or `Context` may be omitted.

To make an item explicitly non-applicable:

```yaml
Scope:
  Disabled: true
```

## Semantics

- Missing Machine Scope means no machine restriction.
- Missing Context Scope means no contextual restriction.
- If both are present, both must pass.
- If neither is present, the item is generally applicable.
- `Disabled: true` always returns not applicable.

## Evaluation

1. If disabled, return false.
2. If Machine Scope exists, evaluate it using `AIDE_Tags`; if false, return false.
3. If Context Scope exists, evaluate its natural-language condition against the current context;
   if false, return false.
4. Otherwise return true.

Scope returns applicability only. It does not execute the scoped behaviour.

## Machine Scope

Machine Scope is an `AIDE_Tags` Boolean query. Do not add a separate Scope expression language.

## Context Scope

Context Scope is descriptive applicability interpreted by the AI. Use it for semantic or
judgment-based conditions that would make the machine expression unnecessarily complex.

## Platform realisation

Concrete discovery and trigger mechanisms are platform Build concerns. Platform builders may use
Scope declarations to create effective target-platform metadata, but this Standard does not
define plugin, skill, repository, bundle, or platform-specific trigger mechanics.

---

**Depends on:** `AIDE_Tags@v1`, `Capabilities_Scope_Design` v1.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Scope_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_StandardsProduction_Standard_v1.md -->
# AIDE Standards Production — Standard

> **Identity:** `AIDE_StandardsProduction@v1`
> **Common name:** Standards Production
> **Version 1** (2026-08-30). First published contract for producing a canonical Standard from
> confirmed capability design.
>
> **Default weight:** Requirement

---

## Purpose

Produce a canonical AI-facing Standard from confirmed Capability Design without introducing new
capability meaning during production.

This Standard governs the **canonical Standard outcome** only. Platform skill/plugin/bundle
realisation, packaging, WorkPackage execution, and Deployment are later concerns.

## Applicability

Apply when a confirmed Capability Design declares a Standard outcome or when an existing canonical
Standard is being rebuilt for a new capability release.

```yaml
Scope:
  Context: >
    Apply when producing or validating a canonical Standard from confirmed capability design.
```

## Required inputs

Resolve before production:

- the confirmed Capability Design and declared Standard output;
- formal capability identity and intended release version;
- applicable shared Standards, including Scope, Dependencies, Migration, and Review where used;
- any capability-specific platform addenda confirmed by the Design; and
- the previous canonical release/transition history where this is not the first release.

If capability meaning, release identity/version, or an authoritative input is materially ambiguous,
stop and return the gap to the work owner. Production does not fill design gaps by invention.

## Canonical Standard contract

A canonical Standard contains only the capability meaning needed by its consumers and later Build.
Where applicable it carries:

- formal identity, common name, and capability release version;
- purpose and applicability;
- complete rules/guidance/context needed to operate under the capability;
- effective weight for every addressable/chunkable unit;
- `AIDE_Scope` declarations;
- `AIDE_Dependencies` declarations;
- `AIDE_Migration` summary and supported transition history;
- owner-defined Tag/Dependency Builder definitions;
- Review expectations/profile references where confirmed; and
- capability-specific platform addenda only.

Generic platform implementation metadata or mechanics do not belong in the canonical Standard.

## Weight production

Supported weights are:

```text
Requirement | Expectation | Guidance | Context
```

Every addressable unit must have an effective weight. Use the smallest clear representation:

1. an optional document default;
2. section/unit declaration where it differs or where no document default exists; and
3. statement/block override only where necessary.

Nearest declaration wins. A chunk with no effective weight is a production defect.

Weight meaning:

- `Requirement` — needed for the stated outcome/consumer to work; ordinary departure is not
  permitted.
- `Expectation` — default position; departure is allowed but must be made visible.
- `Guidance` — recommended/default practice; departure is allowed and its consequences are owned.
- `Context` — explanatory information with no obligation.

Requirements are expressed through consequence/value rather than bare authority.

## Production procedure

1. Read the confirmed Design and its declared outputs; do not use Decisions as an outcome input.
2. Resolve identity and intended capability release version.
3. Extract the complete confirmed Standard meaning, removing design-process reasoning that is not
   needed by consumers.
4. Preserve capability terminology and boundaries exactly; do not broaden ownership.
5. Apply the canonical Standard contract and effective weights.
6. Add shared Scope/Dependencies/Migration/Review declarations only where the Design requires them.
7. Carry forward supported transition history and update `MigrationSummary` for a later release.
8. Include only confirmed capability-specific platform addenda.
9. Validate completeness, internal coherence, dependency identities, transition continuity, and
   chunk-level weight coverage.
10. Produce the canonical Standard and report any unresolved production defect rather than silently
    repairing the Design.

## First release and migration

A first release has no older consumer state to transform, but still declares positive transition
state so later tooling has an unambiguous history:

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

Later releases follow `AIDE_Migration` and retain the transition history required by the supported
baseline.

## Validation failures

Production fails visibly when, among other cases:

- Design does not determine required capability behaviour;
- declared output and Design disagree;
- identity/release version is unresolved;
- an addressable unit has no effective weight;
- Scope/Dependency/Migration declarations are contradictory or incomplete;
- a later release lacks required transition continuity; or
- platform-generic implementation has leaked into canonical capability meaning.

Return the smallest actionable defect set to the work owner. Do not create policy during repair.

## Output

The output is one canonical Standard for the declared capability release, ready for the normal
Build-side platform realisation flow.

---

**Depends on:** `Capabilities_Standards_Design_v4`, `AIDE_Scope@v1`,
`AIDE_Dependencies@v2`, `AIDE_Migration@v1`.

**References:** `Capabilities_Tools_Design_v2`, `AIDE_BuildCapabilityTool@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_StandardsProduction_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_StandardsUsage_Standard_v1.md -->
# AIDE Standards Usage — Standard

> **Identity:** `AIDE_StandardsUsage@v1`
> **Common name:** Standards Usage
> **Version 1** (2026-08-30). First published runtime contract for discovering, combining,
> interpreting, and operating under applicable Standards.
>
> **Default weight:** Requirement

---

## Purpose

Operate under applicable AI-facing Standards consistently while preserving declared weights,
Scope, dependencies, migration requirements, human authority, and visible handling of genuine
conflict or deviation.

## Applicability

Apply whenever an AI session relies on one or more governed Standards to perform, assess, or advise
work.

```yaml
Scope:
  Context: >
    Apply when governed Standards are available and relevant to the current work or action.
```

## Establish the applicable set

1. Discover the Standards available to the current execution context.
2. Resolve their formal identities and dependency state where relevant.
3. Before affected use, honour any applicable Required Migration under `AIDE_Migration`.
4. Evaluate `AIDE_Scope`; an item that is not applicable contributes no rule to the current work.
5. Use only the material needed for the current work while preserving each retrieved unit's
   effective weight and necessary context.

Do not treat installation/presence alone as applicability.

## Interpret weights

- `Requirement` — satisfy it for the stated outcome/consumer; if it cannot be satisfied, surface
  the consequence and do not silently claim conformance.
- `Expectation` — follow by default; if departing, make the departure visible.
- `Guidance` — follow where it adds value; departure is allowed and the resulting consequences are
  owned.
- `Context` — use as information/reasoning; it creates no obligation by itself.

A lower-weight statement does not silently cancel a higher-weight statement on the same point.

## Combine Standards

Compatible applicable Standards stack. Do not choose one merely because several apply.

When two applicable statements genuinely oppose each other on the same point:

1. higher weight governs;
2. equal-weight conflict is surfaced/escalated rather than silently resolved; and
3. the conflict record identifies the competing Standards/statements and the work affected.

Do not manufacture conflict from different concerns that can both be satisfied.

## Human instruction and deviation

Direct human/work-owner instruction may override a Standard within that person's authority.
When it displaces a Requirement or Expectation:

- state the Standard position and material consequence;
- make the departure visible in the appropriate work record where durability matters; and
- continue under the authorised instruction unless another non-overridable external constraint
  applies.

Guidance may be departed from without approval, but material consequences remain the responsibility
of the work owner/Lead.

## Missing, stale, or unresolved Standard state

- Missing required dependency → surface under `AIDE_Dependencies` and follow the governing
  operation's blocking posture.
- Required Migration outstanding → reconcile before affected use.
- Unsupported migration baseline or ambiguous transition → stop affected use and escalate.
- Unresolvable Standard identity/version → do not guess which contract governs.
- Genuine equal-weight conflict → escalate rather than select silently.

## Runtime economy

Prefer cheap applicability/version checks before loading detailed Standard material. Use
`MigrationSummary`, Scope machine filters, Tags, and platform discovery metadata where available,
then load only the detailed content needed for the work.

Performance optimisation must not change Standard meaning or hide an applicable Requirement.

## Reporting

Normal operation need not narrate every Standard consulted. Surface what materially affects the
work: blocking requirements, meaningful expectations/deviations, conflicts, migration state, or a
Standard-driven consequence the user/work owner needs to know.

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

**Depends on:** `Capabilities_Standards_Design_v4`, `AIDE_Scope@v1`,
`AIDE_Dependencies@v2`, `AIDE_Migration@v1`.

**References:** `AIDE_StandardsProduction@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_StandardsUsage_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Tags_Standard_v1.md -->
# AIDE Tags — Standard

> **Identity:** `AIDE_Tags@v1`
> **Common name:** Tags
> **Version 1** (2026-08-28). First published definition of the AIDE tag-building, storage, and
> query contract.

---

## Purpose

Provide a small, extensible tag system that lets Standards define Tag Builders, maintain derived
classification data on artefacts, and evaluate simple deterministic tag expressions.

## Tag Builder definition

A Standard may contribute a Tag Builder by embedding an `AIDE_TagBuilder` YAML block.

A builder must define:

- `Id` — unique builder identity in the available Standards set;
- `Owner` — semantic owner;
- `AppliesWhen` — how the builder decides whether it applies to the artefact in hand;
- `Source` — how it locates/reads its source information;
- `Generate` — how it derives the current tag values;
- `OutputOwnership` — exactly one owned `Prefix` or owned `Group` key.

Example:

```yaml
AIDE_TagBuilder:
  Id: DocType
  Owner: AIDE_DocumentationMethodology
  AppliesWhen:
    Description: Run when canonical DocType metadata is present.
  Source:
    Description: Read DocType and InheritedDocTypes as defined by DocMeth.
  Generate:
    Description: Generate one tag for each current value.
  OutputOwnership:
    Prefix: "doctype-"
```

## Build behaviour

A Tags build pass:

1. discovers all available `AIDE_TagBuilder` definitions;
2. gives each builder the artefact in hand;
3. lets the builder determine applicability;
4. lets an applicable builder generate its current tags and remove stale tags it owns;
5. leaves manual tags and other builders' output unchanged.

Builders must be idempotent. If a builder applies but cannot complete correctly, it reports the
failure visibly and does not silently leave misleading partial output.

## Ownership

A builder identifies generated tags by either:

- an owned tag prefix; or
- an owned group `{key}:[...]`.

The builder owns generation and cleanup only inside that boundary.

Groups are invisible to every consumer except their owning builder. All other consumers see only
the contained tag values.

## Storage

For a governed Markdown document, store tags as one compact footer metadata property:

```text
Tags: tag-a, tag_b, group:[tag-c, tag_d]
```

The metadata container and placement are supplied by the governing document methodology; this
Standard owns only the `Tags:` content contract.

Tag values contain no whitespace. Use `-` or `_` as separators. Manual and generated tags may
coexist.

## Query

Before matching, flatten groups to their contained tag values and ignore group keys.

Supported operators:

```text
!   NOT
&   AND
|   OR
()  grouping
```

Precedence: `!`, then `&`, then `|`.

Matching uses exact tag values. Extra tags do not affect a query unless named by it. Wildcards,
inference, inheritance traversal, comparisons, and functions are not part of the query language.

## Freshness

Run Tag Builders after relevant artefact change and before tag-dependent behaviour when tag
freshness is uncertain. An explicit rebuild may be used at any time.

The Tags system does not resolve semantic inheritance or orchestrate upstream processors. The
builder consumes the current artefact state supplied to it.

---

**Depends on:** `Capabilities_Tags_Design` v1.

**References:** `AIDE_Scope@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Tags_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_WorkingPractices_Standard_v4.md -->
# AIDE Working Practices — Standard

> **Identity:** `AIDE_WorkingPractices@v1`
> **Common name:** Working Practices
> **Version 4** (2026-08-31). Adds WIP continuity checkpoints, visible cross-platform context
> currency and top-level-topic-aware live-state handling while preserving the first distributable
> `AIDE_WorkingPractices@v1` capability identity.
>
> **Default weight:** Expectation

## Purpose

Provide portable base conventions for how an AI and user practically approach, communicate,
organise, complete and hand over work.

This Standard may be used as part of full AIDE or independently.

## WP1 — Change Delivery Package

For a material multi-file change, cross-project change set, corpus reconciliation or other output where
application steps are non-obvious, deliver one package containing:

- all files created/changed by the change set; and
- one concise application-instructions document.

The instructions identify, as applicable:

- add/replace action and destination;
- semantic lifecycle action plus the applicable physical handling convention;
- rename/move/ownership change;
- Binder/Bundle regeneration/replacement;
- project-context additions/removals/replacements;
- cross-project, source or deployment consequences;
- transfer-only artefacts;
- intentionally unchanged related items where omission could be mistaken for oversight;
- actions still requiring another process/authority; and
- unconfirmed state changes.

Do not force a package for a trivial one-file output whose application is obvious.

Creating the package does not mean its contents were applied.

Under the current AIDE repository convention, stage active Change Delivery ZIPs in
`Documentation/_changeDeliveryPackages/`; after application/review is complete, move them to
`Documentation/_changeDeliveryPackages/_completed/`.


## WP2 — Use the owning project's current baseline for cross-project master changes

Before issuing authoritative changes for another owning top-level topic/container, use that owner's current Binder
or current master sources when reasonably available.

Do not reconcile another project from a stale snapshot when a current coherent source is available.

If current state cannot be obtained, state the limitation rather than claiming current
reconciliation.

Never edit a generated Binder directly; edit masters and regenerate.

## WP3 — Gloss coded references

On first use, briefly explain opaque section/decision/question IDs or document/capability references
when their meaning is not already clear from immediate context.

## WP4 — Verify inspectable current/external facts

Where a statement depends on current records, files, installed state, environment state or another
inspectable authority, check the available source/tool first when reasonably possible.

If it cannot be verified, state the uncertainty. Do not compose a plausible value.

## WP5 — Distinguish generated intent from applied state

Do not silently conflate states such as:

```text
created → proposed → handed off → applied → installed/deployed → verified
```

Claim only the state that the available authority/tool/environment actually establishes.

## WP6 — Surface architecture-shaping choices

Handle routine, reversible and low-risk choices autonomously.

For a genuine architecture-shaping decision/material trade-off, provide:

```text
Decision
Recommendation
Why
Credible alternative
Consequence
```

proportionately.

## WP7 — Work in layers before detail

For complex work, establish compact intent/premises and the working model before deep elaboration.
Keep the active set human-comprehensible and expose partial conclusions early enough for steering.

## WP8 — Preserve durable handoff

When substantial confirmed work moves to another project/session/environment/owner, preserve the
authoritative sources/pointers, confirmed model/decisions and material reasoning, remaining work,
important deferred/non-goals, and application/integration instructions needed to continue safely.

Treat handoff summaries as transfer material unless explicitly adopted as authoritative masters.
Remove stale handoff summaries from ongoing context once their job is complete.

### Project Handoff

**Project Handoff** is the named cross-project form of durable handoff. **Handoff** may be used as
conversational shorthand when the destination/context is obvious.

> A Project Handoff is a concise transfer of material knowledge, reasoning, decisions, implications
> and authoritative source pointers from one AIDE project to another project that owns or should act
> on that information.

Use or suggest one when knowledge developed in the current project would materially help another
owning project **make, understand or implement its next decision**. Do not create one for routine
chatter or information already fully represented in authoritative sources. Proactively suggest a
Project Handoff when material work clearly creates a consequence owned by another project; produce
one when requested or when the agreed work calls for it.

Proportionately include:

- why the Handoff is being made and what destination action is expected;
- material reasoning/context and destination-relevant confirmed decisions;
- important alternatives, constraints, trade-offs, implications and consequences;
- unresolved/deferred items and important non-goals/boundaries;
- authoritative source artefacts/pointers; and
- what is proposed versus already confirmed.

Keep it concise transfer context, not a transcript or duplicate corpus.

The destination's **current Binder/masters are the baseline**. Reconcile the Handoff against them,
surface genuine conflict, incorporate useful content into the destination's own authoritative
Design/Decisions/outcomes, and normally remove the Handoff from active context once incorporated.
An older Handoff does not override newer destination state.

Discovering another project's consequence does not itself authorise remote master editing. The
normal flow is:

```text
originating project → Project Handoff → owning project → authoritative update
```

If cross-project master changes are separately authorised, WP2 applies before issuing them.

A **Project Handoff** transfers knowledge, reasoning, decisions and implications. A **Change
Delivery Package** transfers concrete created/changed files plus application instructions. They may
accompany each other, but neither substitutes for the other, and a knowledge-only Project Handoff
does not by itself require a Change Delivery Package.

## WP9 — Management-folder and historical-storage convention

Where filesystem/repository structure is used and the distinction is useful, prefix structural or
workflow-management folders with `_` so they are visually distinct from substantive content.

Current AIDE examples are:

```text
_superseded/
_archived/
_changeDeliveryPackages/
_completed/
```

A folder does not define semantic state. The relevant owner first determines whether an artefact is
Current, Superseded, Archived or otherwise disposed; Working Practices then applies the physical
handling convention.

Under the current repository convention, physically hold Superseded material in `_superseded/` and
Archived material in `_archived/` where those folders are used.

Historical material in `_superseded/`, `_archived/` and `_changeDeliveryPackages/_completed/` may
periodically move to longer-term storage outside the active repository to control repository size,
provided required history and traceability are preserved.

Use an equivalent management representation on platforms that do not use filesystem folders.

## WP10 — Version and place generated Binders for easy current-context use

Issue a generated project Binder as:

```text
<Project>_Binder_vN.md
```

Binder version counts issued Binder assemblies independently of project/capability/source-document
versions.

Keep the current Binder in the active/master project folder alongside Current masters. It remains a
generated, read-only consumption artefact; its manifest identifies the exact source versions and
integrity information. Authoritative changes are made to masters, then the Binder is regenerated.

A normal Binder contains stable/current knowledge. Under `AIDE_DocumentationMethodology@v21`, WIP,
Working, OpenItems and WorkRegister are normally loaded separately as live/high-churn state. A new
checkpoint in an existing live-state series does not by itself require Binder regeneration; Index
discovery may use a version-agnostic live-series pointer reconciled at normal output checkpoints.

When a newly issued Binder replaces the active Binder, the prior Binder becomes Superseded and may
be retained under `_superseded/` according to the current repository convention. Replace the loaded
project-context Binder with the new current Binder.


## WP11 — Batch file/document output at meaningful checkpoints

Do not output changed masters, Binders or Change Delivery Packages after every individual change by
default.

Accumulate confirmed changes during active work and issue one consolidated output pass at the end
of a significant work unit, work session or meaningful completion/integration checkpoint, or when
the user explicitly asks to run/output the pass.

Before autonomously producing a material file set or Change Delivery Package, ask whether the user
wants the accumulated changes output now or whether other pending work should be included. An
explicit request to output/update/build the files or package already counts as confirmation.

Where another project/chat response is reasonably expected, especially during Project Handoff
exchange, normally queue resulting changes until the exchange reaches a useful checkpoint rather
than regenerating files/packages on every round.

Never batch at material risk of losing confirmed information, creating significant ambiguity, or
materially affecting downstream work. Preserve at-risk state promptly using the least-churn
appropriate durable mechanism, then consolidate normal deliverable output later.

## WP12 — Persist active work before context loss would be costly

Do not allow valuable current thinking to depend solely on a volatile chat/session/platform context
once losing that context would materially impair continuation.

Use the least-heavy suitable mechanism:

```text
current volatile active context → WIP
substantial exploratory body    → Working
unresolved durable attention    → OpenItems
confirmed downstream obligation → WorkRegister
confirmed model/reasoning       → Design / Decisions
```

Useful WIP checkpoint triggers include ending a material work session, switching chats/projects/
platforms, moving to unrelated work likely to displace active context, completing a substantial
reasoning block not represented durably, impending context/cache reset, or explicit request for a
physical continuation checkpoint.

Do not checkpoint every message merely because WIP exists. Where the AI judges persistence is
materially useful, advise/create the checkpoint according to current authority rather than waiting
for the human to discover context loss.

## WP13 — Use visible WIP version currency when moving context

When a WIP checkpoint is intended for project/context replacement or inter-platform transfer, use
the current versioned filename and identify the version being transferred.

The practical question is:

> Is the WIP file I have loaded the current issued checkpoint?

Do not infer successful replacement/sync merely because a new file was generated. Verify the
loaded/available version where the platform permits.

## Guidance Profiles

This is base guidance.

Applicable organisation/group/team/user Guidance Profiles may Add, Refine or explicitly Override
named practices using small deltas.

Unmentioned base practices remain effective. Equal-specificity conflict fails visibly unless
explicitly ordered.

Do not fork/copy the complete base Standard merely to customise it.

Host/platform instructions and other higher-priority governing constraints remain outside this
profile model.

## Ownership boundary

Working Practices governs collaboration/operating behaviour and practical workflow handling, not
the semantics of specialised mechanisms it mentions.

Documentation Methodology owns document lifecycle meaning and WIP/Working/OpenItems/WorkRegister
semantics; Working Practices may own the physical handling convention used to realise that state. Use the specialised owner for Domain, Dependencies,
Migration, Review, Build or Deployment semantics.

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
Dependencies: !AIDE_DocumentationMethodology@v21
References: WorkingPractices_Design_v5, AIDE_Principles@v1
<!-- END SOURCE: AIDE_WorkingPractices_Standard_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_WorkPackage_Standard_v2.md -->
# AIDE WorkPackage — Standard

> **Identity:** `AIDE_WorkPackage@v2`
> **Common name:** WorkPackage
> **Version 2** (2026-08-31). Adds explicit WorkRegister source mapping and per-obligation result return for manageable delivery chunks.
>
> **Default weight:** Requirement

---

## Purpose

Provide Build with one bounded executable contract that states the required result, authority, work-specific inputs and acceptance, and returns enough evidence for the director of work to reconcile execution.

## Required WorkPackage content

Resolve before execution:

```yaml
WorkPackage:
  Objective: <required result>
  AuthorisedScope: <allowed work and material exclusions>
  Inputs: <work-specific authoritative inputs>
  RequiredOutputs: <artefacts/state to produce or change>
  Acceptance: <observable completion/evidence conditions>
  Constraints: <applicable limits/dependencies/targets/reserved decisions>
  Review: <optional explicit plan/result Review posture>
  Return: <required outcome destination/record>
  WorkRegisterItems: <optional source item IDs and covered portions>
```

Equivalent clear prose/sections are valid; the semantic fields matter, not this physical rendering.

If a material field is unresolved and cannot safely be inferred from authoritative inputs, the WorkPackage is NotReady.

## WorkRegister mapping

A WorkPackage may be created directly from defined work or may cover some/all of one or more
WorkRegister obligations. Where mapped, record each source item ID and the portion covered by this
package.

```yaml
WorkRegisterItems:
  - Id: WR12
    Covers: comparer implementation and tests
  - Id: WR13
    Covers: documentation update
```

One WorkRegister item may be delivered through several WorkPackages; one WorkPackage may cover
several items. Mapping is traceability and does not grant authority to reinterpret the source
Design/WorkRegister.

## Handoff rule

Build should not need Decisions/design-history material to reconstruct the required result. Include work-specific authoritative artefacts needed for execution; do not duplicate generic execution/platform knowledge already supplied by the Build environment.

## Build authority

Build may choose ordinary implementation detail within Authorised Scope. It must return rather than silently change Objective, major scope, Acceptance, architecture/policy, or a decision explicitly reserved to the work owner.

## Review

Where the WorkPackage specifies plan/result Review, execute it under `AIDE_Review`; do not invent a WorkPackage-specific review method.

An omitted Review field does not disable governing Review requirements supplied by another applicable Standard/workflow.

## Execution

1. Validate inputs and authority.
2. Establish a proportionate plan.
3. Complete applicable pre-execution Review.
4. Execute within scope.
5. Validate against Acceptance.
6. Complete applicable result Review.
7. Return a truthful Outcome.

Do not claim completion solely because an artefact was produced.

## Out-of-scope discovery

Report useful out-of-scope findings; do not action them under the current authority without explicit re-scope/new work.

## Outcome

Return:

```yaml
Outcome:
  Status: Complete | Partial | Blocked | Failed
  WorkPerformed: <summary>
  Outputs: <produced/changed artefacts or state>
  Validation: <acceptance evidence/results>
  Reviews: <where applicable>
  Deviations: <authorised exceptions/differences>
  Remaining: <unresolved/remaining work>
  OutOfScope: <reported findings>
  DesignFeedback: <questions/follow-up>
  WorkRegisterResults: <per mapped item/portion result, evidence and remaining work where applicable>
```

The persisted record may use concise document sections rather than YAML. For mapped WorkRegister work, report each item/covered portion as `Complete | Partial | Blocked | Failed`, with enough evidence and remaining-work detail for the owning/directing process to reconcile the source register. Build does not silently close the register.

## Partial/failure behaviour

Preserve successful work only where the resulting state is safe and accurately reportable. Do not hide partial completion. A retry/resumption starts from the actual returned state and must avoid duplicate side effects where practical.

## Lifecycle

`Defined → Ready → Executing → Returned → Reconciled/Archived`. `Reconciled` includes source WorkRegister reconciliation where mapping exists.

Documentation Methodology owns the file naming/archive mechanics; this Standard owns the WorkPackage execution semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_WorkPackage_Design_v2, AIDE_Review@v1
References: AIDE_Build@v4, AIDE_ProjectDesign@v2
<!-- END SOURCE: AIDE_WorkPackage_Standard_v2.md -->

---
