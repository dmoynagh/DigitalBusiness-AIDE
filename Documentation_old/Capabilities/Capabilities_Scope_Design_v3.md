# Capabilities Scope — Design

> **Version 3** (2026-09-03). Clarifies snapshot-relative Machine Scope for immutable built/deployed artefacts.

---

## §1 — Purpose

Scope defines **when a Standard, Tool, behaviour, rule, or other referenceable capability
applies**.

It does not own taxonomy, tagging, deployment targeting, or concrete platform discovery
mechanics. Those are separate concerns.

The formal published Standard identity is **`AIDE_Scope`**. `Scope` is the common name.

---

## §2 — Two-layer model

```text
Machine Scope
  Boolean query over AIDE_Tags
        ↓
Context Scope
  natural-language condition interpreted by AI
        ↓
applicable / not applicable
```

Machine Scope provides cheap deterministic filtering. Context Scope handles meaning, intent,
nuance, and conditions that are better resolved from the current AI context than encoded in a
rule engine.

The design deliberately keeps the machine layer small. If applicability requires complex logic,
the first question is whether that condition belongs in Context Scope instead.

---

## §3 — Canonical declaration

A scoped item may declare either or both layers:

```yaml
Scope:
  Machine: design & !archived
  Context: >
    Apply when the work could affect governed documentation behaviour.
```

Machine-only:

```yaml
Scope:
  Machine: design & review-required
```

Context-only:

```yaml
Scope:
  Context: >
    Apply when the change requires independent review judgment.
```

Explicitly disabled:

```yaml
Scope:
  Disabled: true
```

The declaration may attach to a whole Standard or Tool, or to an individual rule/behaviour
inside one.

---

## §4 — Default semantics

An omitted Scope layer means **no restriction from that layer**.

- Machine Scope absent → unrestricted by Tags.
- Context Scope absent → unrestricted by contextual condition.
- Both present → both must pass.
- Neither present → generally applicable.
- `Disabled: true` → never applies.

Omission is not equivalent to disabled.

---

## §5 — Evaluation

Evaluation short-circuits from deterministic to contextual:

```text
Disabled?
  yes → false

Machine Scope present?
  yes → evaluate AIDE_Tags query
        false → false
        true  → continue

Context Scope present?
  yes → AI evaluates contextual condition
        false → false
        true  → continue

→ true
```

Machine Scope uses the query semantics defined by `AIDE_Tags`. Scope does not implement a second
tag matcher.

Context Scope is a natural-language condition, not an attempt to encode a full machine rule.

Scope returns applicability only. It does not execute the behaviour whose applicability it
assesses.

---

## §5a — Tag freshness precondition

Machine Scope is deterministic only over current `AIDE_Tags` state. If generated-tag freshness is
uncertain, refresh the applicable builders under `AIDE_Tags` before relying on the Machine result.
Scope does not own tag regeneration and does not treat stale tags as a second applicability state.

For immutable built/deployed material, evaluate the Tags frozen for the exact artefact snapshot.
Producer-side Build has already established their freshness relative to its authoritative source
snapshot. Scope does not mutate that artefact to follow later producer state.

## §6 — Relationship to triggering

Scope owns semantic applicability and the requirement that applicability can be made effective
for AI behaviour.

Concrete platform trigger, retrieval, discovery, skill, plugin, repository, bundle, or other
runtime rendering mechanics belong to Build-side platform Standards/Tools.

A platform implementation may use Scope declarations as input when producing trigger/discovery
metadata, but Scope does not contain generic platform implementation knowledge.

---

## §7 — Relationship to Tags

`AIDE_Tags` is the general classification substrate. Scope is one consumer.

```text
Tags
  creates/queryable classifications
        ↓
Scope Machine expression
        +
AI context condition
        ↓
applicability
```

Scope never generates tags and never assigns semantics to Tag groups.

---

## §8 — Ownership boundary

`AIDE_Scope` owns:

- Scope declaration shape;
- omission/default/disabled semantics;
- Machine + Context composition;
- evaluation order and short-circuit behaviour;
- the meaning of the applicability result.

`AIDE_Tags` owns machine tag generation/storage/querying.

The owning capability owns the actual Scope declaration for its behaviour.

Platform Build owns concrete trigger/discovery realisation.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v15, Capabilities_Decisions_v21, Capabilities_Tags_Design_v3
References: AIDE_Tags@v3
