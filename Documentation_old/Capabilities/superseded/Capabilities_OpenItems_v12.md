# Capabilities — Open Items

> **Version 12** (2026-08-29). Closes Migration, Standards/Tools reconciliation, shared version
> distinctions and the producer-side Package/Manifest question. Deployment behaviour and platform
> evidence are now the principal open Capabilities work.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## Q1 — Deployment Set contract

**Status:** Open — Deployment pass

Define set lifecycle/state, membership/removal semantics, composition/rebuild and verification.

## Q2 — Deployment Config ownership and shape

**Status:** Open — Deployment pass

Define where logical Deployment Set/platform mappings live, inheritance/overrides, credentials/
access boundaries, and physical destination resolution.

## Q3 — Deployment assembly/failure behaviour

**Status:** Open — Deployment pass

Define full vs incremental assembly, conflicts, atomicity, partial failure, resumption, rollback
posture, integrity verification, and publication state.

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

**Status:** Open — empirical and now immediately useful

For Claude/OpenAI/ChatGPT/Codex establish representation, skill/plugin/header discovery,
MigrationSummary visibility, Scope/trigger/bootstrap realisation, composition, install/update/remove,
publication/pickup, and verification/state.

**OpenAI hypothesis to test, not architecture yet:** one OpenAI plugin containing skills may be a
common primary Deployment Set representation for ChatGPT and Codex, with a project bundle retained
as compatibility/bootstrap/fallback. Prove this using a representative Standard before Deployment
locks the mapping.

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

---

**Depends on:** `Capabilities_Decisions` v12.

**References:** `Capabilities_Design` v6, `Capabilities_WorkRegister` v10.

**Methodology:** v17
