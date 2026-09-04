# Capabilities — Open Items

> **Version 10** (2026-08-28). Closes the Tags/Scope/Dependencies model questions, records the
> partially resolved identity/package contracts, and makes Review the current architecture item.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Q1 — Deployment Set contract

**Status:** Open — deferred until Deployment pass

Define final identity/name, membership, configuration relationship, composition/rebuild,
replacement/removal, and deployment-state semantics.

---

## Q2 — Deployment Config ownership and shape

**Status:** Open — deferred until Deployment pass

Define the environment/platform configuration resolving logical Deployment Sets to physical
repositories, plugins, collections, bundle paths, and publication destinations.

---

## Q3 — Deployment assembly behaviour

**Status:** Open — deferred until Deployment pass

Determine full rebuild vs incremental update per platform, atomicity, partial failure,
resumption, integrity, and any rollback posture.

---

## Q4 — Scope boundary

**Status:** Resolved

Resolved by `Capabilities_Scope_Design` v1 / `AIDE_Scope@v1`:

- Scope owns applicability only.
- Machine Scope is a Tags query.
- Context Scope is AI contextual judgment.
- Missing layers are unrestricted; disabled is explicit.
- Platform trigger/discovery implementation belongs Build side.

---

## Q5 — Dependencies contract

**Status:** Resolved

Resolved by `Capabilities_Dependencies_Design` v1 / `AIDE_Dependencies@v1`:
compact grammar, `!` / `!!`, identity-first resolution, conformance checkpoints, exact-version
syntax, Dependency Query, Dependency Builders, migration handoff, and conformance advancement.

---

## Q6 — Review purpose, model and integration

**Status:** Current

Work from first principles before detailed mechanics:

- clarify Review's purpose as independent insight and AI risk management;
- state how it adds value;
- define intended outcomes;
- define the core lead/reviewer/review-package model;
- then evaluate Type/Level, blind review, independence, checking level, convergence, findings and
  disposition, review records, internal/external execution, and tooling.

Use parked Workflow review experience as evidence, not as an automatic baseline.

---

## Q7 — Shared identity and version contract

**Status:** Partially resolved

Resolved in Core:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

- first identity primary;
- formal AIDE identities namespaced where externally referenceable;
- identity match ignores version;
- version is compared by the consuming mechanism.

Dependencies now defines dependency conformance-version semantics.

Still define remaining canonical capability/package/deployment version distinctions and how they
map into manifests/state without conflating them with document version.

---

## Q8 — Capability Package and Deployment Manifest contract

**Status:** Partially resolved

Confirmed boundary:

```text
Capability Package + Deployment Manifest → Deployment
```

Package is payload; Manifest is machine-readable deployment intent. Complete the minimal fields
from demonstrated Deployment needs rather than prebuilding a broad schema.

---

## Q9 — Build Config inheritance/defaults

**Status:** Open — detail, not current blocker

Confirmed fields remain platforms, side (default both), and Deployment Set(s). Determine later
whether values inherit from project/topic defaults and how overrides are represented.

---

## Q10 — WorkPackage integration

**Status:** Moved to AIDE Build

Capabilities consumes the generic WorkPackage Standard/Outcome once defined there.

---

## Q11 — Platform build/deployment evidence

**Status:** Open — empirical

For Claude, Codex, and ChatGPT determine capability representation, Build standards, Tags/Scope
realisation, Core bootstrap implementation, identity/version visibility, Deployment Set assembly,
and publication/update mechanics.

---

## Resolved by the v10 checkpoint

- Tags extracted as a first-class general classification/query component.
- Tag Builder discovery/execution and generated ownership by prefix/group.
- Groups are invisible outside their owning builder.
- Flat Boolean Tags query model (`!`, `&`, `|`, `()`).
- Scope Machine + Context model and permissive omission semantics.
- Dependencies compact grammar and query model.
- `@v` conformance checkpoint vs `@!v` exact-version requirement.
- `!` required vs `!!` best-effort startup-required dependency posture.
- Core formal identity list convention.
- Core `{bootstrap}` system primitive.
- Package payload separated from Deployment Manifest intent.

---

**Depends on:** `Capabilities_Decisions` v10.

**References:** `Capabilities_Design` v4, `Capabilities_WorkRegister` v8.

**Methodology:** v17
