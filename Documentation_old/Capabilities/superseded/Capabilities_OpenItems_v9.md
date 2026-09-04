# Capabilities — Open Items

> **Version 9** (2026-08-28). Reconciled after canonical capability production, Build Config,
> build-side platform adaptation, embedded transition declarations, and Deployment Set were
> confirmed.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Q1 — Deployment Set contract

**Status:** Open

Define the minimum generic Deployment Set contract:

- identity/name;
- membership;
- relationship to Build Config;
- relationship to platform Deployment Config;
- whether a set has its own version or only deployment state;
- composition/rebuild rules;
- replacement/removal semantics.

**Feeds into:** Deployment design.

---

## Q2 — Deployment Config ownership and shape

**Status:** Open

Define the configuration that resolves a logical Deployment Set to concrete platform targets,
for example repositories, plugin/collection names, bundle paths, and publication destinations.

Confirm which parts are stable environment configuration versus per-deployment instruction.

**Feeds into:** Deployment design.

---

## Q3 — Deployment assembly behaviour

**Status:** Open

For each platform, determine whether Deployment:

- rebuilds the complete Deployment Set from known package contributions;
- incrementally updates the existing deployed artefact;
- supports both.

Define atomicity, partial failure, rollback/resume, and integrity expectations.

**Feeds into:** Deployment design and package contract.

---

## Q4 — Scope boundary

**Status:** Open — review required

Confirm what remains in Scope after separating:

- Build Config platform targeting;
- side targeting;
- Deployment Set membership;
- platform build mechanics.

Determine whether platform retrieval/discovery/trigger realisation remains a Scope mechanism, a
platform Build concern, or a split contract.

---

## Q5 — Dependencies contract

**Status:** Open — review required

Confirm:

- dependency identity/version semantics;
- dependency/reference distinction;
- availability checks;
- conformance version advancement;
- interaction with Build-side installed capabilities;
- exact handoff from version gap to Migration.

Do not allow Dependencies to become an installation/deployment mechanism.

---

## Q6 — Review outcome and integration model

**Status:** Open

Define the reusable Review contract:

- review record/outcome;
- finding/evidence/risk/remedy structure;
- lead disposition;
- review profiles;
- iteration and closure;
- published Standard/Tool outputs, if any.

---

## Q7 — Shared identity and version contract

**Status:** Open

Define the minimum identity/version contract shared across:

- canonical capability;
- dependency declaration;
- migration transition range;
- package;
- deployment state/Deployment Set where needed.

Distinguish document version from capability/release version and dependency conformance version.
Do not assume semantic versioning.

---

## Q8 — Capability Package and manifest contract

**Status:** Open

Define the smallest capability-local package contract:

- package identity/version;
- platform contributions;
- transition material;
- removals;
- integrity;
- manifest;
- information Deployment needs to place the package into its Deployment Set(s).

ZIP is the preferred physical representation where practical, not the logical definition.

---

## Q9 — Build Config inheritance/defaults

**Status:** Open — detail, not parent blocker

Confirmed fields are:

- platforms, defaulting to the current supported-platform set;
- side, defaulting to both;
- Deployment Set(s).

Determine whether Deployment Set and platform values may inherit from topic/project defaults and
how overrides are represented.

---

## Q10 — WorkPackage integration

**Status:** Moved to AIDE Build

Define the generic WorkPackage Standard and WorkPackage Outcome under AIDE Build.

Capabilities needs only the capability-specific profile/input requirements once that generic
contract exists.

---

## Q11 — Platform build/deployment evidence

**Status:** Open — empirical

For Claude, Codex, and ChatGPT, determine and maintain:

- concrete capability representation;
- platform build standards;
- deployment-set assembly mechanism;
- identity/version visibility;
- trigger/discovery behaviour;
- publication/update mechanism.

These are Build/platform facts, not Capability Design facts.

---

## Resolved by the v9 architecture pass

- Mandatory separate `Design_Platform_{Name}` files — **not required**.
- Design-side platform outcome generation — **superseded by Build-side platform realisation**.
- Physical separate source migration files — **not required**; posture separation remains.
- WorkPackage as a Capabilities concern — **moved to AIDE Build**.
- Logical deployment grouping — **Deployment Set confirmed**.
- Build Config core fields — **platforms, side, Deployment Set(s) confirmed**.

---

**Depends on:** `Capabilities_Decisions` v9.

**References:** `Capabilities_Design` v3, `Capabilities_WorkRegister` v7.

**Methodology:** v17
