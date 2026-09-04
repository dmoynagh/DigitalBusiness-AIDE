# Capabilities Dependencies — Design

> **Version 3** (2026-09-01). Resolves Review C reference-position, non-ordering checkpoint, exact-version and Bootstrap-precedence semantics without adding dependency categories.

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

Precedence is interpreted for dependencies of the artefact being processed. It does not sequence
independent artefacts or peer Bootstrap Contributions. A conformance checkpoint alone creates no
resolution/execution order. Migration consumes declaration order only when the governing migration
operation actually needs deterministic ordering among that artefact's independent dependency
chains.

## §6 — Version semantics

`abc@v8` means the dependent artefact was last successfully **saved and proven conformant** against
`abc` v8. It remains the same identity if v12 is available; Dependency Query reports the v8→v12
gap.

`abc@!v8` is a hard present constraint requiring exactly v8 to be available. If exact v8 is not
available, the dependency is unsatisfied and affected use requiring it is blocked; another version
may not silently substitute. The constraint is not a saved conformance checkpoint or ordinary
Migration version gap. Changing/removing the pin is an explicit dependent-artefact change that is
validated and saved normally.

Unversioned dependencies request no version comparison.

## §6a — Reference positions and current executable instructions

Version meaning follows syntactic role; one role does not inherit another's obligations:

| Position | Form | Meaning | Currency/conformance obligation |
|---|---|---|---|
| Footer `Dependencies:` | `X@vN` | last saved/proven conformance checkpoint of this dependent artefact | none until a qualifying save proves advancement |
| Footer `Dependencies:` | `X@!vN` | hard present exact-version constraint | exact version must be satisfiable for affected use |
| Footer `Dependencies:` | `X` | dependency relationship without version tracking | no version comparison |
| Footer `References:` | any | reader/evidence pointer | none |
| Current executable body | `X` or deliberate `X@vN` | operational instruction | versionless by default; a specific release must be intentional/correct |

A conformance checkpoint is backward-looking evidence about the dependent artefact. It creates no
resolution order, execution order or runtime requirement by itself. Mutual conformance checkpoints
are therefore not an operational dependency cycle. Presence markers and exact constraints carry
present requirement; declaration order carries processing precedence only where the governing
operation needs it.

Current executable capability references are not dependency checkpoints. Use a versionless identity
by default; name a specific release only where the instruction deliberately depends on or targets
that release's contract. `References:` has no currency, compatibility or conformance duty merely
because a version is written there.

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

References remain distinct from Dependencies. They are reader/evidence pointers and carry no
reassessment, currency or conformance semantics. Documentation Methodology owns their document
container/rendering; Dependencies owns the semantic distinction from dependency checkpoints and
current executable capability instructions.

## §12 — Ownership boundary

Dependencies owns declaration grammar, presence posture, order/default processing precedence,
identity-first resolution, conformance/exact-version state, Dependency Query, conformance
advancement, and Dependency Builder semantics.

Core owns Identity/bootstrap. Migration owns transition semantics and execution. Deployment owns
installation/distribution. Governing consumers may impose stronger operational policy.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v10, Capabilities_Decisions_v16
References: Capabilities_Migration_Design_v2, Core_System_Design
