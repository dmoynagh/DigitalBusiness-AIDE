# AI Deployment — Decisions

> **Version 6** (2026-09-02). Records exact Set releases, Outputs, Actions, Target Adapters, verification and AIDE Core configuration.
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

**Decision.** Assign/freeze the next Set version only after every required member and Output resolves,
assembles and validates. A failed candidate consumes no version and leaves the previous Desired
Release in place.

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
versioned bundles to `C:\Users\david\dev\repos\Documentation\DeployedBundles` through one local
action that moves earlier current bundles to `superseded`.

**Boundary.** Shared publication is not atomic runtime installation. Bundle context placement may
remain manual and must not be reported as complete merely because the local file exists.

## D39 — OpenAI plugin required reach is Codex

**Decision.** Use GitHub/OpenAI marketplace distribution as the preferred route. Codex is required
reach; supported ChatGPT surfaces are additional intended reach. Keep workspace sync/install and
runtime verification separate from repository publication.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDeployment_Design_v6, AIDE_Build@v8
References: AIDeployment_Registry_Design_v2, AIDeployment_SetRelease_Design_v1, AIDeployment_TargetAdapter_Design_v1, AIDeployment_AIDECore_Reference_v1, AIDE_DeploymentRegistryTool@v1, AIDE_CapabilityBuild@v3, AIDE_Dependencies@v3, AIDE_Tags@v2, AIDeployment_OpenAI_Reference_v3
