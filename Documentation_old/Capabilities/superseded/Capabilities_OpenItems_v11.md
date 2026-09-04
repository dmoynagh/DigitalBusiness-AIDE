# Capabilities — Open Items

> **Version 11** (2026-08-29). Closes the Review purpose/model/lifecycle/profile/tool question and
> records its two deliberately external environment and communication seams.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

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

**Status:** Resolved

Resolved by `Capabilities_Review_Design` v1, `Capabilities_Review_Decisions` v1,
`AIDE_Review@v1`, `AIDE_ReviewProfiles@v1`, and
`Capabilities_Review_Tool_Design` v1:

- independent Type / Level / Mode / Reviewer dimensions;
- Check / Inspect / Evaluate / Robust / user-activated Stress Test profiles;
- consequence/reach/reversibility/uncertainty Level assessment and dynamic change;
- Full/Blind request construction and purpose-shaped Review material;
- role reversal with actual Lead/Reviewer models recorded per Round;
- append-only Rounds, Findings versus Lead disposition, Level-based re-review, and no fixed cap;
- authorised-scope control, Review Result, and transient/durable persistence;
- Review Tool orchestration boundary; and
- environment configuration plus shared communication retained as external seams.

The five primary use cases are covered from design exploration through post-execution Review.

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

## Q12 — Environment settings home consumed by Review

**Status:** Open — external to Review; not a Review completion blocker

Determine where environment-specific facts are stored and resolved, including available AI
platforms/reviewer families, actual models and capability tiers, routes from Chat/Work/Codex,
fallbacks, local preferences, and access/usage/cost constraints.

Review consumes this factual resolver and does not own its storage or wider environment model.

---

## Q13 — Shared communication capability ownership

**Status:** Open — external to Review; coordinate with future Research work

Determine the permanent owner and general contract for direct inter-AI send/receive, correlated
response return, delivery state/failure, and indirect AI Message relay. Review consumes this
capability but does not own transport. Research is expected to reuse it while retaining its own
behaviour and lifecycle.

---

## Resolved by the v11 checkpoint

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
- Review purpose, Lead/Reviewer ownership, and independent assessment model.
- Type / Level / Mode / Reviewer separation.
- Five Review Profiles and their default Levels/Modes.
- Dynamic consequence-based Review Level and Level-driven re-review.
- Review Input, Request, Response, Round, Finding/Disposition, and Result contracts.
- Review authorised-scope and transient/durable persistence rules.
- Review Tool orchestration boundary and five primary use cases.

---

**Depends on:** `Capabilities_Decisions` v11.

**References:** `Capabilities_Design` v5, `Capabilities_WorkRegister` v9,
`Capabilities_Review_Design` v1, `Capabilities_Review_Decisions` v1.

**Methodology:** v17
