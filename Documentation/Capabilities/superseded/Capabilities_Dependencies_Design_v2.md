# Capabilities Dependencies — Design

> **Version 2** (2026-08-29). Adds significant declaration order/default processing precedence and
> reconciles conformance advancement with the final Migration model. Other v1 semantics are
> retained.
>
> Created: 2026-08-28 | Last modified: 2026-08-29

---

## §1 — Purpose

A Dependency declares that an artefact relies on another identified artefact or capability for
some part of its correct schema, design, content, interpretation, conformance, maintenance, or
execution.

Dependencies answers:

```text
What do I rely on?
Can that identity be resolved now?
What version was I last conformed against?
What version is available?
Is there a version gap or exact-version mismatch?
```

Dependencies reports state. It does not install, deploy, migrate, or decide every operation's
blocking policy.

The formal published Standard identity is **`AIDE_Dependencies`**.

## §2 — Identity and version

A referenceable artefact may expose:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

Resolve identity name first, ignoring version. Compare version only after identity resolution.
Multiple matching artefacts fail visibly rather than being guessed through.

## §3 — Compact declaration

```text
Dependencies: abc, !def@v4, !!ghi@!v7, builder:[jkl@v2, !mno]
```

Forms:

```text
dependency
!dependency
!!dependency
dependency@vN
dependency@!vN
<markers compose>
owner:[dependency, ...]
```

Documentation Methodology owns the footer metadata container; Dependencies owns the property's
content/semantics.

## §4 — Presence levels

- normal — check when relevant;
- `!` required — check on relevant use/access and report missing identity prominently;
- `!!` startup-required — best-effort startup presence check plus normal required behaviour
  thereafter.

`!!` concerns startup **presence**, not blanket startup Migration/currency scanning.

## §5 — Declaration order and default processing precedence

Dependency declaration order is significant.

> Earlier dependencies have higher default processing precedence where an operation needs a
> deterministic order, unless an explicit dependency relationship or the governing operation
> defines another order.

This expresses foundational/processing precedence, not business importance or requirement level.
Grouped/generated entries preserve their effective declared order after flattening.

Migration consumes this rule when ordering independent dependency migration chains.

## §6 — Version semantics

`abc@v8` means the dependent artefact was last successfully **saved and proven conformant** against
`abc` v8. It remains the same identity if v12 is available; Dependency Query reports the v8→v12
gap.

`abc@!v8` requires exactly v8 to be available. Exact-version mismatch is factual state; the
applicable consumer/governing Standard defines what operational or migration treatment follows.

Unversioned dependencies request no version comparison.

## §7 — Dependency Query

Report per declaration:

- requested identity and resolved primary identity;
- resolved/not resolved;
- requirement level;
- declared conformance version;
- available version;
- version relation: same/newer/older/unknown/not-applicable;
- version gap;
- exact-version requirement/result; and
- declaration/default-processing position where ordering is relevant.

Dependencies does not decide what a version gap requires. Migration and the current operation
consume the result.

## §8 — Conformance advancement

A dependency checkpoint advances only when the dependent artefact is actually updated/saved with a
state proven through the target version.

- Newer availability alone never advances it.
- `None` and positively `NotApplicable` migration versions may be traversed without changing
  content, but their newer checkpoint is written only on the next artefact save.
- Required or OnUpdate work must complete successfully before the saved checkpoint moves through
  it.
- On partial migration success, advance only through the last successfully completed/traversed
  version that is represented by the saved artefact.
- Deferred/failed migration does not advance through the unresolved version.

## §9 — Dependency Builder

A Standard may embed an `AIDE_DependencyBuilder` defining `Id`, `Owner`, `AppliesWhen`, `Source`,
`Generate`, and builder-owned Group/Prefix output.

Discovery, idempotency, failure, generated-output cleanup, and invisible group semantics mirror
`AIDE_Tags`. Builders preserve meaningful generated dependency order.

## §10 — Bootstrap

`!!` checks use the Core `{bootstrap}` primitive. Dependencies may contribute the startup check;
Core owns the marker/discovery rule and platforms implement the strongest available mechanism.

## §11 — References

References remain distinct from Dependencies. They do not carry reassessment/conformance semantics.
Document rendering remains a Documentation Methodology concern pending its separate review.

## §12 — Ownership boundary

Dependencies owns declaration grammar, presence posture, order/default processing precedence,
identity-first resolution, conformance/exact-version state, Dependency Query, conformance
advancement, and Dependency Builder semantics.

Core owns Identity/bootstrap. Migration owns transition semantics and execution. Deployment owns
installation/distribution. Governing consumers may impose stronger operational policy.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Decisions_v12`, `Core_System_Design` v3.

**References:** `Capabilities_Migration_Design_v1`, `DocumentationMethodology_Guide` v17.

**Methodology:** v17
