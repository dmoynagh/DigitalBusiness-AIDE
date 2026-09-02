# Capabilities — Work Register

> **Version 8** (2026-08-28). Checkpoint after Tags, Scope and Dependencies were resolved.
> Moves Review to current priority, defers Deployment until the upstream contracts are stable,
> and records remaining reconciliation/package work.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

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

**Status:** Current priority — first-principles review in progress

Work from the top before re-admitting detailed mechanics:

1. purpose;
2. how Review creates value and reduces AI risk;
3. intended outcomes;
4. core model;
5. only then detailed mechanics.

Evidence to consider from the parked Workflow framework includes model-family independence,
blind review, Type × Level separation, attackable review packages, findings-not-fixes, and the
Json Equality evidence that changing lens can create more insight than repeating the same lens.

Do not automatically re-admit fixed round caps, provider/model mappings, Codex-specific preflight,
or historical commands without fresh justification.

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

## Current sequence

1. Review (`WR7`).
2. Migration (`WR3`).
3. Reconcile Standards (`WR1`).
4. Reconcile Tools (`WR2`).
5. Finish shared identity/version + Package/Manifest contracts (`WR8`, `WR9`).
6. Deployment (`WR4`).
7. Platform evidence/build/deployment standards (`WR10`) as required/parallel.
8. DocMeth review later (`WR12`).

WorkPackage remains the separate AIDE Build workstream (`WR11`).

---

**Depends on:** `Capabilities_Decisions` v10.

**References:** `Capabilities_Design` v4, `Capabilities_OpenItems` v10,
`Core_System_Design` v3.

**Methodology:** v17
