# AIDE Scope — Standard

> **Identity:** `AIDE_Scope@v1`
> **Common name:** Scope
> **Version 1** (2026-08-28). First published applicability contract using Tags plus contextual
> AI judgment.

---

## Purpose

Define whether a Standard, Tool, rule, behaviour, or other referenceable capability applies in
the current context.

## Declaration

```yaml
Scope:
  Machine: design & !archived
  Context: >
    Apply when the work could affect governed documentation behaviour.
```

Either `Machine` or `Context` may be omitted.

To make an item explicitly non-applicable:

```yaml
Scope:
  Disabled: true
```

## Semantics

- Missing Machine Scope means no machine restriction.
- Missing Context Scope means no contextual restriction.
- If both are present, both must pass.
- If neither is present, the item is generally applicable.
- `Disabled: true` always returns not applicable.

## Evaluation

1. If disabled, return false.
2. If Machine Scope exists, evaluate it using `AIDE_Tags`; if false, return false.
3. If Context Scope exists, evaluate its natural-language condition against the current context;
   if false, return false.
4. Otherwise return true.

Scope returns applicability only. It does not execute the scoped behaviour.

## Machine Scope

Machine Scope is an `AIDE_Tags` Boolean query. Do not add a separate Scope expression language.

## Context Scope

Context Scope is descriptive applicability interpreted by the AI. Use it for semantic or
judgment-based conditions that would make the machine expression unnecessarily complex.

## Platform realisation

Concrete discovery and trigger mechanisms are platform Build concerns. Platform builders may use
Scope declarations to create effective target-platform metadata, but this Standard does not
define plugin, skill, repository, bundle, or platform-specific trigger mechanics.

---

**Depends on:** `AIDE_Tags@v1`, `Capabilities_Scope_Design` v1.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
