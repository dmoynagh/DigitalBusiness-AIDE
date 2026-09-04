# Capabilities — Work Register

> **Version 9** (2026-08-29). Completes the Review component design/Standards/Tool specification,
> records its external environment and communication handoffs, and moves Migration to current
> priority.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## WR1 — Reconcile Standards child corpus

**Status:** Open — after Review/Migration contracts are stable

Rewrite `Capabilities_Standards_Brief` v1 and `Capabilities_Standards_Design` v3 against parent
Design v4.

Retain still-current Standard role, weights, facilitation framing, canonical production, and
Production/Usage output split.

Remove/revise stale Scope mechanics, local tag ownership, platform trigger rendering, Deployment
mechanics, and old migration assumptions. Consume `AIDE_Tags`, `AIDE_Scope`,
`AIDE_Dependencies`, and the final Migration/Review contracts instead of restating them.

---

## WR2 — Reconcile Tools child corpus

**Status:** Open — after Review/Migration contracts are stable

Rewrite `Capabilities_Tools_Brief` v1 and `Capabilities_Tools_Design` v1 against parent Design v4.

Retain Tool role, logical commands, interaction model, reporting, failure handling, and
idempotency. Remove the stale embedded Scope/tag model and consume the shared component Standards.

---

## WR3 — Migration component design and production standard

**Status:** Open — next after Review

Create/reconcile Migration Brief/Design/Standard around:

- Required Migration / On-Update / no-transition postures;
- transition declarations embedded in canonical Standards/Tools;
- Dependencies conformance checkpoints and version-gap input;
- Migration Build Standard and canonical migration information;
- platform/deployment adaptation;
- `/migrations-check`, `/migrations-apply`, `/update-doc`;
- ordering, success/failure, idempotency, escalation;
- optional use of the Core `{bootstrap}` primitive where early checking adds value.

---

## WR4 — Deployment component design

**Status:** Open — deliberately deferred until upstream contracts are stable

Complete Deployment from the confirmed **Capability Package + Deployment Manifest** boundary.

Define:

- Deployment Config;
- Deployment Set identity and membership;
- platform resolution of a Deployment Set;
- package/manifest validation;
- composition/assembly from multiple packages;
- replacement/removal;
- deployment state;
- partial failure;
- resumption and idempotency;
- Git/repository publication where applicable;
- platform-specific deployment builders;
- rejection of defective inputs.

Deployment is isolated enough to complete late and contains more untested/platform-specific work
than the known capability components.

---

## WR5 — Scope component review/design

**Status:** Completed at model/design level

Completed in `Capabilities_Scope_Design` v1 / `AIDE_Scope@v1`:

- Machine Scope = `AIDE_Tags` Boolean query;
- Context Scope = AI-interpreted natural-language condition;
- omission = unrestricted; explicit disabled = never applies;
- both present = both constrain;
- deterministic-first short-circuit evaluation;
- Scope returns applicability only;
- platform trigger/discovery implementation belongs Build side.

Remaining work is only downstream reconciliation/testing.

---

## WR6 — Dependencies component review/design

**Status:** Completed at model/design level

Completed in `Capabilities_Dependencies_Design` v1 / `AIDE_Dependencies@v1`:

- compact dependency declaration;
- normal / `!` required / `!!` startup-required posture;
- identity-first resolution and version comparison second;
- `@v` conformance checkpoint and `@!v` exact-version constraint;
- Dependency Query result contract;
- Dependency Builder model;
- conformance advancement only after successful migration/update;
- handoff of version gaps to Migration;
- bootstrap relationship for `!!`.

---

## WR7 — Review component design

**Status:** Completed at model/design/Standard/Tool-specification level

Completed in `Capabilities_Review_Design` v1, `Capabilities_Review_Decisions` v1,
`AIDE_Review@v1`, `AIDE_ReviewProfiles@v1`, and
`Capabilities_Review_Tool_Design` v1:

- purpose as independent insight, substantive integrity, better decisions, and risk management;
- Lead ownership and Reviewer Findings as evidence;
- Trigger and resolved Review Input Contract;
- independent Type / Level / Mode / Reviewer dimensions;
- Check / Inspect / Evaluate / Robust / user-activated Stress Test profiles and defaults;
- consequence/reach/reversibility/uncertainty Level assessment and dynamic change;
- purpose-shaped, attackable, non-persuasive request construction;
- direct/AI Message communication seam;
- correlated append-only Rounds with actual Lead/Reviewer models;
- Findings/dispositions, scope control, Level-based re-review, and proportionate completion;
- Review Result and transient/durable persistence; and
- five primary design-to-build use cases.

Remaining environment/communication ownership work is tracked separately in `WR14` and does not
reopen the Review model.

---

## WR8 — Shared identity/version contract

**Status:** Partially resolved

Core now establishes:

- namespaced formal AIDE identities with common names;
- compact `Identity: primary@v, alternate@v, ...` header metadata;
- first identity primary;
- identity matching by name, version comparison separate.

Dependencies now defines conformance-version semantics.

Still resolve the remaining distinctions needed by canonical capability release versions,
packages, Deployment Manifest, Deployment Set/deployment state, and transition ranges. Do not
create a new top-level component solely for these remaining details.

---

## WR9 — Package/manifest contract

**Status:** Partially resolved

Confirmed boundary:

```text
Capability Package + Deployment Manifest → Deployment
```

Package = payload. Deployment Manifest = machine-readable placement/lifecycle intent.

Complete the smallest schema demonstrated by Deployment needs, including identity/version,
Deployment Set membership, platform applicability, removals/replacements, integrity, transition
material, and resumption/deployment-state information only where required.

---

## WR10 — Platform evidence and build/deployment standards

**Status:** Open — empirical/platform work

For each supported platform, record capability representation, build-side adaptation, identity
visibility, scope/trigger realisation, bootstrap mechanism, publication/update mechanics, and
Deployment Set assembly.

Initial targets: Claude, Codex, ChatGPT.

---

## WR11 — WorkPackage handoff to AIDE Build

**Status:** Moved outside Capabilities

Create AIDE Build / WorkPackage design and Standard separately. Capabilities consumes its generic
handoff and Outcome contract.

---

## WR12 — Documentation Methodology review handoff

**Status:** Open — intentionally deferred

Use `Capabilities_DocMethReviewItems` v2 when the separate Documentation Methodology review begins.
Do not edit DocMeth piecemeal while Capabilities contracts are still being completed.

---

## WR13 — Tags component design and Standard

**Status:** Completed at model/design level

Created `Capabilities_Tags_Design` v1 / `AIDE_Tags@v1` covering Tag Builders, discovery,
generated ownership by prefix/group, group invisibility, compact `Tags:` storage, Boolean query,
idempotency/failure/freshness, and external execution-order responsibility.

---

## WR14 — Review external environment and communication handoff

**Status:** Open — parked outside Review; coordinate with Environment and future Research work

Resolve the architecture homes for:

- environment-specific reviewer/model/capability/route availability, fallbacks, preferences, and
  constraints; and
- shared direct/indirect inter-AI send/receive, correlation, failure state, and AI Message relay.

Review's consumer contracts are defined. This item must not move either mechanism into Review for
implementation convenience.

---

## Current sequence

1. Migration (`WR3`).
2. Reconcile Standards (`WR1`).
3. Reconcile Tools (`WR2`).
4. Finish shared identity/version + Package/Manifest contracts (`WR8`, `WR9`).
5. Deployment (`WR4`).
6. Platform evidence/build/deployment standards (`WR10`) as required/parallel.
7. Resolve the Review environment/communication handoff (`WR14`) with the owning workstreams.
8. DocMeth review later (`WR12`).

WorkPackage remains the separate AIDE Build workstream (`WR11`).

---

**Depends on:** `Capabilities_Decisions` v11.

**References:** `Capabilities_Design` v5, `Capabilities_OpenItems` v11,
`Capabilities_Review_Design` v1, `Capabilities_Review_Decisions` v1,
`Core_System_Design` v3.

**Methodology:** v17
