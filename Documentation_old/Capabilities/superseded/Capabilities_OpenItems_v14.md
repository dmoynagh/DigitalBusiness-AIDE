# Capabilities — Open Items

> **Version 14** (2026-08-30). Moves Deployment questions to AI Deployment,
> closes the immediate OpenAI evidence gate, and leaves only external/configuration follow-up.
> non-Deployment capability output remains open; Deployment/platform evidence plus deliberately
> external Environment/communication and later DocMeth work remain.
>
> Created: 2026-08-27 | Last modified: 2026-08-30

---

## Q1 — Deployment Set contract

**Status:** Moved to AI Deployment

Owned by `AIDE_Deployment@v1`; retained here only as historical routing.

## Q2 — Deployment Config ownership and shape

**Status:** Moved to AI Deployment

Owned by `AIDE_Deployment@v1`; retained here only as historical routing.

## Q3 — Deployment assembly/failure behaviour

**Status:** Moved to AI Deployment

Owned by `AIDE_Deployment@v1`; retained here only as historical routing.

## Q4 — Scope boundary

**Status:** Resolved — `Capabilities_Scope_Design` v1 / `AIDE_Scope@v1`.

## Q5 — Dependencies contract

**Status:** Resolved — `Capabilities_Dependencies_Design` v2 / `AIDE_Dependencies@v2`.

v2 adds declaration-order processing precedence and final saved-checkpoint semantics.

## Q6 — Review purpose/model/integration

**Status:** Resolved — Review child corpus v1.

## Q7 — Shared identity and version contract

**Status:** Resolved for current architecture

Distinct concepts are:

- document version;
- capability release version;
- dependency conformance version;
- package build identity/integrity; and
- deployment state.

Deployment may define additional state fields but not another semantic capability version without a
demonstrated need.

## Q8 — Capability Package and Deployment Manifest contract

**Status:** Resolved at producer boundary

Package identifies the concrete build of one capability release. Manifest carries only logical
placement/lifecycle intent needed by Deployment: PackageId, capability identity/release, target
Deployment Set/platform, contribution selection, replace/remove intent where required, and
integrity. Physical destinations are Deployment Config.

Deployment may extend this contract only where its design demonstrates another required input.

## Q9 — Build Config inheritance/defaults

**Status:** Open — detail, not current blocker

Confirmed fields remain platforms, side (default both), and Deployment Set(s). Resolve inheritance/
overrides when Environment/Deployment configuration is designed.

## Q10 — WorkPackage integration

**Status:** Moved to AIDE Build.

## Q11 — Platform build/deployment evidence

**Status:** Immediate OpenAI architecture gate resolved; broader evidence is implementation follow-up

The tested local shared-plugin/skill route is rejected as a common ChatGPT + Codex runtime route.
Further hosted/account/public OpenAI routes plus Claude/other platform mechanics belong to target
implementation evidence in Build + AI Deployment.


## Q12 — Environment settings home consumed by Review

**Status:** Open — external to Review

Resolve storage/inheritance for available AI families/models/capabilities/routes/fallbacks,
preferences and access/usage/cost constraints.

## Q13 — Shared communication capability ownership

**Status:** Open — external to Review; coordinate with Research

Resolve permanent ownership of direct/indirect inter-AI send/return, correlation, delivery/failure
state and AI Message relay.

## Q14 — Migration model

**Status:** Resolved

`Capabilities_Migration_Design` v1 / `AIDE_Migration@v1` / Migration Tool Design v1 cover trigger,
posture, summary, transition history, ordering, checkpoints, partial failure/defer, exact-version
policy seam and supported baseline.

## Q15 — Build Capability action ownership and missing canonical outputs

**Status:** Resolved

`Build Capability` is `AIDE_BuildCapabilityTool@v1`, with internal
`Capabilities_BuildCapability_Tool_Design` v1. The previously declared Standards Production/Usage
outcomes and canonical Review/Migration Tool outcomes are also published. `Tool` is now a
Capabilities-local custom outcome type distinct from Tool Design.

---

**Depends on:** `Capabilities_Decisions` v14.

References: `Capabilities_Design` v8, `Capabilities_WorkRegister` v12.

Dependencies: !AIDE_DocumentationMethodology@v18
