# AI Deployment — Decisions

> **Version 2** (2026-08-31). Adds decisions for semantic requirement preservation, target-change
> policy, source/authority separation, Bootstrap artefact deployment and interim manual Bundles.
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

---
Dependencies: !AIDE_DocumentationMethodology@v18, AIDeployment_Design_v2
References: Capabilities_Design_v8, Core_System_Design_v4, AIDE_Dependencies@v2, AIDeployment_OpenAI_Reference_v2
