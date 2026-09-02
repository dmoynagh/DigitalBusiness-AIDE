# Capabilities Runtime Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.

This Binder is a GPT Project consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Capabilities_Tags_Design_v1.md` — sha256 `03dc70d882af`
- `AIDE_Tags_Standard_v1.md` — sha256 `ee2c8f46463b`
- `Capabilities_Scope_Design_v1.md` — sha256 `e15414243d99`
- `AIDE_Scope_Standard_v1.md` — sha256 `1bda6f1244df`
- `Capabilities_Dependencies_Design_v2.md` — sha256 `df71c09425b4`
- `AIDE_Dependencies_Standard_v2.md` — sha256 `acd8d2f872f0`
- `Capabilities_Migration_Brief_v1.md` — sha256 `62382e77005c`
- `Capabilities_Migration_Design_v1.md` — sha256 `1f2055b5d9cc`
- `AIDE_Migration_Standard_v1.md` — sha256 `6cd6c3932476`
- `Capabilities_Migration_Tool_Design_v1.md` — sha256 `682ca554e79a`
- `AIDE_Migration_Tool_v1.md` — sha256 `99705aaa2f9e`

---

<!-- BEGIN SOURCE: Capabilities_Tags_Design_v1.md -->
# Capabilities Tags — Design

> **Version 1** (2026-08-28). Establishes Tags as the general classification and query
> substrate for AIDE artefacts, including Tag Builder definitions, generated-tag ownership,
> compact document storage, and Boolean matching.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

---

## §1 — Purpose

Tags provides a general machine-usable classification system for AIDE artefacts.

It was identified while solving capability applicability, but it is not owned by Scope and is
not limited to capability matching. Any component may use Tags for deterministic classification,
selection, filtering, review selection, migration selection, build logic, reporting, search, or
other machine-facing behaviour.

The formal published Standard identity is **`AIDE_Tags`**. `Tags` is the common name used in
ordinary prose.

---

## §2 — Core model

```text
semantic owner
  defines source meaning and relationships
        ↓
owning process/Standard
  resolves and denormalises source values
        ↓
Tag Builder
  detects applicability and reads the artefact in hand
        ↓
flat generated tags
        ↓
Tags storage
        ↓
Boolean query
```

The governing principle is:

> **Semantic complexity is resolved by the owner. Tags works on explicit information already
> present on the artefact in hand.**

Tags does not walk inheritance chains, reopen source Standards, or reconstruct semantic
relationships at query time.

---

## §3 — Tag Builder

A **Tag Builder** defines how information available on an artefact is converted into tags.

A Tag Builder may be defined in any Standard that owns the semantics from which those tags are
derived. The owning Standard embeds a structured YAML block conforming to the `AIDE_Tags`
contract.

Example:

```yaml
AIDE_TagBuilder:
  Id: DocType
  Owner: AIDE_DocumentationMethodology

  AppliesWhen:
    Description: >
      Run when the document contains the canonical DocType metadata
      defined by Documentation Methodology.

  Source:
    Description: >
      Read DocType and InheritedDocTypes as defined by that Standard.

  Generate:
    Description: >
      Generate one tag for DocType and one for every InheritedDocType.
      Render each value using the builder's declared output convention.

  OutputOwnership:
    Prefix: "doctype-"
```

`AppliesWhen`, `Source`, and `Generate` are instructions owned by the builder. `AIDE_Tags` does
not need to understand whether the builder reads YAML, headings, filenames, metadata blocks, or
another source representation.

A valid builder declares at minimum:

- a unique builder identity;
- its semantic owner;
- how it determines applicability;
- how it locates/reads its source information;
- how it generates its current tags;
- how its generated output can be identified for cleanup.

---

## §4 — Builder discovery and execution

A Tags build pass discovers `AIDE_TagBuilder` definitions in the Standards available to the
current execution context.

No separate authoritative builder registry is maintained. Embedded definitions are the source;
the discovered builder set is derived.

Execution is:

```text
discover available Tag Builders
        ↓
run each against the artefact in hand
        ↓
builder decides applicable / not applicable
        ↓
applicable builder reads its source
        ↓
builder removes stale output it owns
        ↓
builder writes its current output
```

Each builder owns the full lifecycle of its generated tags. It must leave manual tags and output
owned by other builders untouched.

Builders are idempotent: running the same builder against an unchanged artefact produces the same
tag state.

If a builder determines that it applies but cannot derive its output correctly, it fails visibly
rather than silently leaving or producing misleading partial tags.

---

## §5 — Generated-tag ownership

Generated tags must be identifiable by their builder so stale output can be removed safely.

A builder may use either:

1. **Owned prefix** — the builder owns all tags beginning with a declared prefix.
2. **Owned group** — the builder owns a declared `{key}:[...]` group in the Tags storage line.

Examples:

```text
Tags: doctype-design, doctype-platformdesign, release-ready
```

with builder ownership:

```yaml
OutputOwnership:
  Prefix: "doctype-"
```

or:

```text
Tags: release-ready, doctype:[design, platformdesign]
```

with:

```yaml
OutputOwnership:
  Group: "doctype"
```

The group key is only a stable ownership marker the builder recognises. It does not need to be
the builder name or owner identity.

Two active builders must not claim the same output ownership boundary unless a future Standard
explicitly defines shared ownership.

---

## §6 — Groups

Groups are **storage and ownership structure only**.

> **Groups are ignored everywhere except by the Tag Builder that owns them.**

For:

```text
Tags: release-ready, doctype:[design, platformdesign], review-required
```

all ordinary consumers see only the flat tag set:

```text
release-ready
design
platformdesign
review-required
```

Scope, Review, Migration, search, query tools, and AI reasoning do not give `doctype` any
special meaning.

If a consumer needs qualified semantics, the builder emits qualified tag values such as
`doctype-design`; group membership itself is never a query dimension.

---

## §7 — Tag storage

Where a governed Markdown document exposes tags, they are stored as one compact metadata line in
the document's footer metadata container:

```text
Tags: tag-a, tag_b, group:[tag-c, tag_d]
```

Documentation Methodology owns the document metadata containers and their physical placement.
`AIDE_Tags` owns the content and behaviour of the `Tags:` property it places there.

The line may wrap visually but remains one logical delimited property.

Tag values contain **no whitespace**. `-` is the preferred separator and `_` is also permitted.
Generated output should use stable canonical spelling so repeated builds do not create noisy
diffs.

Manual and generated tags may coexist on the same line.

---

## §8 — Query semantics

Tag matching operates on the **flat set of tag values**, with groups removed before evaluation.

The supported Boolean expression language is deliberately small:

```text
!   NOT
&   AND
|   OR
()  grouping
```

Examples:

```text
design
design & !archived
design | build
(design | build) & !archived
```

Operator precedence is `!`, then `&`, then `|`; parentheses override precedence.

A tag expression tests only the tags it names. Extra tags do not affect the result.

Example, for:

```text
Tags: design, womble, archived
```

```text
design & !archived
```

is false because `archived` is present. `womble` is irrelevant.

Queries use exact tag values. There are no wildcards, inheritance traversal, comparisons,
functions, or semantic interpretation in the query language.

---

## §9 — Freshness and ordering

Derived tags are disposable and regenerable from their source information.

Tag Builders should run:

- after a relevant artefact change;
- before relying on tags when freshness is uncertain;
- through an explicit rebuild/update operation when required.

Tags does not implement a general dependency or execution-order engine. If a builder needs
upstream derived information, the wider update/orchestration mechanism is responsible for making
that information current before the builder runs.

A builder works only on the artefact in hand. Missing required source information is surfaced by
the builder rather than resolved through runtime traversal of other artefacts.

---

## §10 — Ownership boundary

`AIDE_Tags` owns:

- the Tag Builder declaration contract;
- builder discovery/execution conventions;
- generated-output ownership rules;
- the `Tags:` storage grammar;
- flattening semantics;
- the Boolean query language;
- generic freshness/idempotency/failure expectations.

The Tag Builder owner owns:

- criterion/source meaning;
- semantic relationships and inheritance;
- detection and extraction logic;
- tag-generation logic;
- cleanup of output inside its declared ownership boundary.

Platform Build Standards may realise Tags differently where a target platform requires another
representation, but they must preserve the same tag semantics.

---

**Depends on:** `Capabilities_Design` v4, `Capabilities_Decisions` v10.

**References:** `Capabilities_Scope_Design` v1, `Capabilities_Dependencies_Design` v1,
`DocumentationMethodology_Guide` v17.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Tags_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Tags_Standard_v1.md -->
# AIDE Tags — Standard

> **Identity:** `AIDE_Tags@v1`
> **Common name:** Tags
> **Version 1** (2026-08-28). First published definition of the AIDE tag-building, storage, and
> query contract.

---

## Purpose

Provide a small, extensible tag system that lets Standards define Tag Builders, maintain derived
classification data on artefacts, and evaluate simple deterministic tag expressions.

## Tag Builder definition

A Standard may contribute a Tag Builder by embedding an `AIDE_TagBuilder` YAML block.

A builder must define:

- `Id` — unique builder identity in the available Standards set;
- `Owner` — semantic owner;
- `AppliesWhen` — how the builder decides whether it applies to the artefact in hand;
- `Source` — how it locates/reads its source information;
- `Generate` — how it derives the current tag values;
- `OutputOwnership` — exactly one owned `Prefix` or owned `Group` key.

Example:

```yaml
AIDE_TagBuilder:
  Id: DocType
  Owner: AIDE_DocumentationMethodology
  AppliesWhen:
    Description: Run when canonical DocType metadata is present.
  Source:
    Description: Read DocType and InheritedDocTypes as defined by DocMeth.
  Generate:
    Description: Generate one tag for each current value.
  OutputOwnership:
    Prefix: "doctype-"
```

## Build behaviour

A Tags build pass:

1. discovers all available `AIDE_TagBuilder` definitions;
2. gives each builder the artefact in hand;
3. lets the builder determine applicability;
4. lets an applicable builder generate its current tags and remove stale tags it owns;
5. leaves manual tags and other builders' output unchanged.

Builders must be idempotent. If a builder applies but cannot complete correctly, it reports the
failure visibly and does not silently leave misleading partial output.

## Ownership

A builder identifies generated tags by either:

- an owned tag prefix; or
- an owned group `{key}:[...]`.

The builder owns generation and cleanup only inside that boundary.

Groups are invisible to every consumer except their owning builder. All other consumers see only
the contained tag values.

## Storage

For a governed Markdown document, store tags as one compact footer metadata property:

```text
Tags: tag-a, tag_b, group:[tag-c, tag_d]
```

The metadata container and placement are supplied by the governing document methodology; this
Standard owns only the `Tags:` content contract.

Tag values contain no whitespace. Use `-` or `_` as separators. Manual and generated tags may
coexist.

## Query

Before matching, flatten groups to their contained tag values and ignore group keys.

Supported operators:

```text
!   NOT
&   AND
|   OR
()  grouping
```

Precedence: `!`, then `&`, then `|`.

Matching uses exact tag values. Extra tags do not affect a query unless named by it. Wildcards,
inference, inheritance traversal, comparisons, and functions are not part of the query language.

## Freshness

Run Tag Builders after relevant artefact change and before tag-dependent behaviour when tag
freshness is uncertain. An explicit rebuild may be used at any time.

The Tags system does not resolve semantic inheritance or orchestrate upstream processors. The
builder consumes the current artefact state supplied to it.

---

**Depends on:** `Capabilities_Tags_Design` v1.

**References:** `AIDE_Scope@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Tags_Standard_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_Scope_Design_v1.md -->
# Capabilities Scope — Design

> **Version 1** (2026-08-28). Recasts Scope as the thin applicability layer above Tags and AI
> contextual reasoning, separating applicability from tag generation, build targeting, and
> platform trigger implementation.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

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

**Depends on:** `Capabilities_Design` v4, `Capabilities_Decisions` v10,
`Capabilities_Tags_Design` v1.

**References:** `AIDE_Tags@v1`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Scope_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Scope_Standard_v1.md -->
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
<!-- END SOURCE: AIDE_Scope_Standard_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_Dependencies_Design_v2.md -->
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
<!-- END SOURCE: Capabilities_Dependencies_Design_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_Dependencies_Standard_v2.md -->
# AIDE Dependencies — Standard

> **Identity:** `AIDE_Dependencies@v2`
> **Common name:** Dependencies
> **Version 2** (2026-08-29). Adds significant declaration-order/default processing precedence and
> aligns saved conformance advancement with `AIDE_Migration@v1`.

---

## Purpose

Declare what an artefact relies on; resolve dependency identity; report presence/version state; and
preserve the last saved, proven conformance checkpoint.

## Storage

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

The governing document methodology supplies the metadata container. This Standard owns the
`Dependencies:` content contract.

## Presence and version grammar

```text
dependency      normal relationship
!dependency     required on relevant use/access
!!dependency    best-effort startup presence check + required thereafter
dependency@vN   last saved/proven conformance checkpoint
dependency@!vN  exact available version vN required
```

Markers compose.

Resolve identity name first, ignoring version; compare version after resolution. Multiple matches
fail visibly.

## Declaration order

Dependency order is significant. Earlier entries have higher **default processing precedence**
when an operation needs deterministic ordering, unless an explicit relationship or governing
operation supplies another order.

This is processing/foundational precedence, not requirement severity.

## Dependency Query

Return at least resolution, requirement level, conformance version, available version, version
relation/gap, exact-version result, and effective declaration order where needed.

Dependencies reports facts. Migration/current operations decide the consequence.

## Conformance checkpoint

A recorded version advances only when the dependent artefact is updated/saved in a state proven
through that version.

- availability alone never advances it;
- `None`/`NotApplicable` migration versions may count as traversed but are persisted only on the
  next artefact save;
- failed/deferred migration does not advance through the unresolved version;
- partial success advances only through the last saved proven version.

## Exact-version constraints

`abc@!v8` requires exactly v8 to be available. Dependencies reports whether the constraint passes.
The governing dependent Standard/document context defines how that constraint should be handled by
Migration or the current operation.

## Required/startup-required

`!` is checked on relevant use/access and missing identity is surfaced prominently.

`!!` additionally requests a best-effort startup **presence** check through the Core bootstrap
mechanism. It does not imply a general startup Migration scan.

## Dependency Builder

Standards may contribute `AIDE_DependencyBuilder` definitions. Builders own only their generated
Group/Prefix output, preserve meaningful order, are idempotent, and fail visibly when applicable
output cannot be derived correctly. Group keys remain invisible to non-owning consumers.

---

**Depends on:** `Capabilities_Dependencies_Design_v2`, `Core_System_Design` v3.

**References:** `AIDE_Migration@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Dependencies_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Brief_v1.md -->
# Capabilities Migration — Brief

> **Version 1** (2026-08-29). First issuance. Defines the purpose, outcomes, and boundaries of the
> Migration component against the established Dependencies conformance-checkpoint model.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## Purpose

Migration owns the reusable transition model by which an artefact that was last proven conformant
against one dependency version is safely brought forward when a newer version is available.

Migration exists so transition work is **declared by the owner of the changed capability rather
than inferred by comparing old and new artefacts**. It applies only the deltas that the owner has
explicitly stated are required for existing consumers.

## Required model

Every released capability version has one transition posture for existing consumers:

- **Required** — applicable existing artefacts must complete the transition before affected use.
- **OnUpdate** — existing artefacts remain usable; the transition is applied the next time the
  artefact is modified/saved.
- **None** — no state change is required for existing consumers.

Posture is version-level. A version does not mix Required and OnUpdate migration items.

Dependencies supplies the last proven conformance checkpoint and current available version.
Migration resolves the intervening version range and determines what transition work applies.

## Required behaviour

- Required Migration is checked when the dependent artefact is relied upon for relevant use.
- OnUpdate work is checked/applied when the artefact is modified or prepared for changed output.
- If Required work causes an update/save, pending applicable OnUpdate work is applied in that same
  update and the artefact is normally brought to the current available version.
- Persisted conformance checkpoints change only when the artefact itself is updated/saved.
- A transition that is positively evaluated as not applicable counts as traversed when the next
  saved checkpoint is written.
- Migration preserves completed progress, never records a failed step as complete, and remains
  resumable from the last successful checkpoint.

## Transition production

Transition declarations live with the canonical Standard or Tool version that caused them. The
canonical capability retains the supported transition history needed to migrate from its supported
baseline to the current release.

Migration publishes a compact `MigrationSummary` for cheap discovery. Detailed transition history
is loaded only when the summary shows there may be relevant work.

## Outputs

Migration produces:

- `AIDE_Migration@v1` — the stable authoring, build, checking, execution, and state contract; and
- a Migration Tool specification providing logical Check, Apply, Update, Status/Resume behaviour.

## Boundaries

Migration does not own:

- dependency identity or version-state resolution — Dependencies;
- applicability language — Scope;
- document placement/rendering for temporary operational state — Documentation Methodology;
- platform-specific skill/plugin/bundle representations — Build-side platform Standards/Tools;
- installation/distribution — Deployment; or
- semantic decisions about exact-version constraints where the governing dependent Standard must
  define how the constraint should be treated during migration.

## Success signals

- A consumer can determine cheaply whether Required work may exist before loading migration detail.
- Required work blocks only affected use, not unrelated work or session startup by default.
- OnUpdate work waits safely until modification.
- Transition execution is ordered, resumable, and truthful about partial success.
- The conformance checkpoint always represents the last state actually proven and saved.
- Platform implementations can optimise discovery without changing Migration semantics.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Dependencies_Design_v2`.

**References:** `AIDE_Dependencies@v2`, `AIDE_Scope@v1`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Migration_Brief_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Design_v1.md -->
# Capabilities Migration — Design

> **Version 1** (2026-08-29). First issuance. Establishes version-level Required/OnUpdate/None
> transitions, fast migration summaries, use/update triggers, ordered multi-dependency execution,
> truthful partial progress, temporary state, supported baselines, and exact-version handling.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## §1 — Purpose and ownership

Migration answers:

> Given an artefact last proven conformant against dependency version X and a newer version Y now
> available, what declared transition work applies, when must it occur, and how far can the saved
> conformance checkpoint safely advance?

Migration owns transition classification, declaration structure, summary/index semantics,
version-range resolution, ordering, execution posture, progress/failure/defer state, and the
logical Migration Tool actions.

The changed capability owner authors the actual transition intent. Dependencies supplies identity,
conformance checkpoint, available version, version relation, and exact-version facts. Scope supplies
applicability. Documentation Methodology supplies generic document state placement/rendering.

---

## §2 — Core model

```text
Dependent artefact
  dependency conformance checkpoint = vX
        +
Available dependency = vY
        ↓
Dependency Query
        ↓
MigrationSummary fast check
        ↓ when work may exist
supported transition history vX+1..vY
        ↓
Scope/applicability
        ↓
Required / OnUpdate / None
        ↓
ordered execution
        ↓
save successful state
        ↓
advance persisted checkpoint
```

Migration never infers transitions by diffing old and new capability text.

---

## §3 — Version-level transition posture

Each released capability version has exactly one posture for existing consumers:

- `Required` — applicable transition work must complete before affected use can continue.
- `OnUpdate` — old state remains usable; applicable work occurs on the next modification/save.
- `None` — no state change is required for existing consumers.

Posture belongs to the release version. Multiple migration items may exist within the release but
all share that posture.

A release with no transition effect positively declares `None`; absence is not used to imply no
transition.

---

## §4 — Transition declaration

Canonical shape:

```yaml
Transition:
  Version: v18
  Posture: Required | OnUpdate | None
  Scope: <optional AIDE_Scope declaration>
  Change: <why existing consumers are affected>
  Items:
    - <ordered transition instruction>
    - <ordered transition instruction>
  Success: <how successful completion is established>
```

`None` requires only version and posture.

A transition is written to produce the required new state, not to encode generic platform
mechanics. It must be sufficiently explicit for an AI to apply safely and determine success.
Where ambiguity or missing prerequisites prevent a safe result, execution stops rather than
inventing a substantive decision.

A transition may invoke an existing Tool where that Tool is the safest deterministic implementation
of part of the change. The transition remains responsible for its outcome and success condition.

---

## §5 — MigrationSummary fast path

Every versioned migratable capability exposes a compact summary:

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8   # optional
```

The summary is an index, not migration evidence. It allows the normal case to avoid loading
transition detail.

### Use fast path

If the dependent checkpoint is at or beyond `LatestRequiredVersion`, no Required transition detail
needs to be loaded for ordinary use.

If it is older, load the relevant detailed history and evaluate applicability.

### Update fast path

When the artefact is modified, compare its checkpoint with the current version and
`LatestOnUpdateVersion`; load transition detail only where pending Required/OnUpdate work may exist.

### Platform optimisation

Where a platform eagerly loads/discovers skill headers or equivalent metadata, Build should surface
`MigrationSummary` there. Detailed transition instructions remain on-demand. Other platforms use
the strongest equivalent cheap-discovery representation.

This is a recommended implementation methodology, not a change to the platform-independent
Migration semantics.

---

## §6 — Required trigger

Required Migration is checked when an artefact is about to be **relied upon for relevant use**.
Merely existing, being listed, or being read as historical/background material does not by itself
force migration.

Execution is:

```text
relevant use
  ↓
Dependency Query
  ↓
checkpoint < LatestRequiredVersion?
  no → continue
  yes → inspect detailed transitions
  ↓
applicable Required transition outstanding?
  no → continue
  yes → migrate before affected use continues
```

There is no blanket Migration startup scan. `!!` remains Dependencies' startup presence check.
A future capability may explicitly justify startup migration checking, but it is not the default.

---

## §7 — OnUpdate trigger

OnUpdate is triggered when an artefact is edited, revised, regenerated, prepared for changed output,
or otherwise modified/saved.

It does not block ordinary use.

When a Required migration causes an update/save, that save is also the next qualifying update for
pending OnUpdate work. Migration therefore applies all applicable pending transition work through
the current available version as part of the same update where possible.

---

## §8 — Conformance checkpoint behaviour

The dependency checkpoint records the **last saved state proven conformant through that dependency
version**.

Rules:

- Never advance merely because a newer dependency version exists.
- Persist a new checkpoint only when the artefact itself is updated/saved.
- A `None` version or a transition found `NotApplicable` is successfully traversed for conformance
  purposes, but does not force a save merely to refresh metadata.
- When the artefact is next saved, the checkpoint may advance through all successfully traversed
  versions.
- If migration succeeds only through an intermediate version, persist that last successful
  checkpoint and resume later from there.

---

## §9 — Multi-dependency migration ordering

Before changing the artefact, Migration discovers the relevant pending migration work across its
versioned dependencies.

Default order follows the dependency declaration order defined by `AIDE_Dependencies`: earlier
dependencies have higher default processing precedence. A more specific explicit dependency or
governing operation may override that order.

Within one dependency, versions execute oldest to newest. Items inside a version execute in their
declared order.

Applicability is re-evaluated immediately before each version is applied because earlier successful
migrations may legitimately change current state.

If two migrations conflict and no governing rule resolves the conflict, stop rather than silently
choosing an execution result.

---

## §10 — Outcomes

A transition/version evaluation has these relevant outcomes:

### Completed

Applicable work completed and its success condition passed. The version is traversed.

### NotApplicable

The dependency applies to the artefact, but Scope/current state establishes that the transition does
not. The version is treated as successfully traversed and may be included in the next saved
checkpoint.

### Deferred

The transition applies but an authorised decision postpones it. The checkpoint does not advance
through the deferred version. Migration writes/updates its temporary operational state entry and
surfaces the consequence. Required affected use remains blocked unless the governing authority has
explicitly accepted an exception for that use.

### Failed

Execution was attempted but could not complete. Partial changes from the failed version are not
saved. Successful earlier versions remain durable. Migration writes/updates temporary operational
state and reports noisily.

---

## §11 — Partial success and temporary state

Migration is stepwise durable rather than globally all-or-nothing.

If migration succeeds through v10 and fails at v11:

- preserve the successful state through v10;
- save the dependent checkpoint at v10;
- do not save partial v11 changes;
- create/update a compact Migration-owned temporary state entry;
- state why it failed and, where known, what would make it succeed; and
- resume later from v10.

Migration owns the state entry's semantics and lifecycle. Documentation Methodology owns the generic
location and rendering for temporary document state. The expected generic human-facing shape is
compact and owner-labelled, for example:

```text
Migration failure [AIDE_Migration]
v11 failed while targeting v12: required source metadata is unavailable.
```

The Migration entry is removed when a later successful update resolves the condition.

---

## §12 — Exact-version constraints

Dependencies reports exact-version constraints such as `abc@!v8` and whether they are satisfied.
Migration still performs its transition role, but it does not invent what the pin means for that
dependent artefact.

Applicable governing Standards/document rules define the migration treatment, for example:

- migrate only up to the explicit version;
- migrate to current and make the new current version explicit;
- migrate to current and relax the declaration to normal conformance tracking; or
- run migration and then perform other owner-defined actions.

If no applicable governing rule resolves the treatment, Migration stops and escalates rather than
guessing.

---

## §13 — Supported migration baseline and history retention

The canonical capability retains transition history sufficient to migrate from the oldest supported
conformance version to the current release.

`SupportedBaseline` is optional. If omitted, all retained historical transition versions are
supported starting points.

Moving the supported baseline forward is a deliberate capability release decision. A consumer
older than the supported baseline receives an `UnsupportedBaseline` result and requires an explicit
recovery/upgrade procedure; Migration does not silently skip missing history.

Old transition detail may be removed from the normal runtime artefact only after it falls below the
supported baseline and the release still provides a clear unsupported-baseline path.

---

## §14 — Edge and failure conditions

- **Missing transition history:** stop noisily; never infer the missing delta.
- **Available dependency older than checkpoint:** report version regression/downgrade state;
  forward Migration does not resolve it.
- **Dependency disappears or changes during execution:** stop against the moving target, preserve
  completed work, and resume after factual dependency state is stable.
- **Concurrent artefact change:** do not overwrite newer work. Stop before saving conflicting
  migration output and record/report the unresolved state.
- **Ambiguous migration instruction:** stop and identify the owning capability/version.
- **Repeated run:** resume safely from persisted checkpoints and owner state; do not reapply
  successfully completed versions.

Caching a successful check inside one session is an optional platform optimisation. It is invalidated
when the artefact, dependency/version state, or explicit refresh changes.

---

## §15 — Outputs and external seams

This Design produces:

- `AIDE_Migration@v1`; and
- `Capabilities_Migration_Tool_Design_v1`.

Migration consumes:

- `AIDE_Dependencies` for dependency/version facts and default dependency order;
- `AIDE_Scope` for applicability;
- governing capability Standards for transition intent and exact-version treatment;
- Documentation Methodology for generic temporary document-state placement/rendering; and
- Build-side platform knowledge for summary/detail representation.

Deployment distributes built transition material but does not own its semantics.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Dependencies_Design_v2`.

**References:** `Capabilities_Migration_Brief_v1`, `AIDE_Dependencies@v2`, `AIDE_Scope@v1`,
`Capabilities_DocMethReviewItems_v3`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Migration_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Migration_Standard_v1.md -->
# AIDE Migration — Standard

> **Identity:** `AIDE_Migration@v1`
> **Common name:** Migration
> **Version 1** (2026-08-29). First published transition authoring, fast-check, execution,
> checkpoint, failure, and resumption contract.

---

## Purpose

Safely move a dependent artefact from its last proven dependency conformance checkpoint toward the
currently available dependency version using owner-declared transitions rather than inferred deltas.

## Transition posture

Every released migratable capability version declares exactly one posture:

```text
Required | OnUpdate | None
```

- `Required` — applicable work must complete before affected use.
- `OnUpdate` — old state remains usable; apply on the next modification/save.
- `None` — no state change is required for existing consumers.

Posture is version-level. Items inside one version do not mix postures.

## MigrationSummary

Expose a compact summary:

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8   # optional
```

Use the summary as a cheap negative/possible-work test. It does not replace detailed transition
history or Scope evaluation.

Where skill headers or equivalent metadata are eagerly loaded/discoverable, platform builds should
surface this summary there and load detailed transition instructions only when the summary indicates
possible work.

## Transition declaration

For each released version:

```yaml
Transition:
  Version: v18
  Posture: Required | OnUpdate | None
  Scope: <optional AIDE_Scope declaration>
  Change: <why existing consumers are affected>
  Items:
    - <ordered transition instruction>
  Success: <how completion is proven>
```

`None` may contain only version and posture.

Transition instructions must be explicit enough to produce the required state and establish
success. They may invoke existing Tools. Do not encode generic platform packaging/invocation
mechanics in the canonical transition.

## Required check

When an artefact is about to be relied upon for relevant use:

1. query its versioned dependencies;
2. compare each checkpoint with `LatestRequiredVersion`;
3. load detailed transition history only where Required work may exist;
4. evaluate Scope/current state; and
5. if applicable Required work remains, migrate before affected use continues.

There is no general Migration startup sweep. `!!` remains the Dependencies startup-presence
posture.

## OnUpdate

When an artefact is modified/saved, reconcile pending migration work through the current available
version.

OnUpdate does not block ordinary use. If Required work causes a save, apply pending applicable
OnUpdate work in that same update where possible.

## Ordering

- Discover relevant pending work before changing the artefact.
- Process dependencies in their declared order unless a more specific governing order applies.
- Process versions oldest to newest.
- Process items within one version in declared order.
- Re-evaluate applicability before each version.
- Stop on unresolved conflict rather than silently choosing.

## Checkpoint

The dependency conformance version is the last **saved, proven** checkpoint.

- Do not advance it because a newer version merely exists.
- Persist a new checkpoint only when the artefact itself is updated/saved.
- `None` and `NotApplicable` count as traversed for the next saved checkpoint.
- On partial success, persist only through the last successful version.

## Outcomes

`Completed` — applicable work succeeded.

`NotApplicable` — the dependency applies but the transition does not; treat the version as traversed
for the next saved checkpoint.

`Deferred` — applicable work was authoritatively postponed; do not advance through it; maintain a
Migration-owned temporary state entry and surface the consequence.

`Failed` — execution could not complete; discard partial changes from the failed version, preserve
prior successful work/checkpoints, maintain temporary state, and report noisily.

## Failure state

On defer/failure, write/update a compact owner-labelled state entry using the generic document-state
location/rendering supplied by the governing document methodology. Include enough information to
understand the current condition, and where known state what would make the migration succeed.
Remove the Migration-owned entry after a later successful update resolves it.

## Exact-version constraints

If a dependency uses an exact-version requirement, follow the migration treatment defined by the
applicable governing Standard/document rule. That rule may preserve the pin, move it, relax it, or
require follow-on actions.

If no governing rule determines the treatment, stop and escalate rather than infer.

## Supported baseline

Retain detailed history needed to migrate from the oldest supported conformance version to current.
If `SupportedBaseline` is declared, a consumer older than it is outside the normal migration path
and requires explicit recovery/upgrade handling.

## Failure and safety

- Missing required transition history → fail loudly.
- Dependency version regression → report; do not treat as forward migration.
- Dependency state changes mid-run → stop and resume after state stabilises.
- Concurrent artefact modification → do not overwrite newer work.
- Ambiguous/contradictory transition instruction → stop and identify the owning version.
- Re-running resumes from persisted successful checkpoints and must not duplicate completed work.

---

**Depends on:** `Capabilities_Migration_Design_v1`, `AIDE_Dependencies@v2`, `AIDE_Scope@v1`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Migration_Standard_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Tool_Design_v1.md -->
# Capabilities Migration Tool — Design

> **Version 1** (2026-08-29). First issuance. Specifies the platform-independent Tool that checks,
> applies, resumes, and reports Migration under `AIDE_Migration@v1`.
>
> Created: 2026-08-29 | Last modified: 2026-08-29

---

## §1 — Output and boundary

This Design produces one canonical **Migration Tool**. It orchestrates `AIDE_Migration@v1` against
Dependency Query results and the artefact in hand.

The Tool does not author transition intent, define dependency identity/version semantics, define
Scope, decide document-state placement, or implement platform-specific command/skill/plugin
rendering.

## §2 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v1
  CommonName: Migration
  PrimaryInvocation: migration
  LogicalActions:
    - Check
    - Apply
    - Update
    - Resume
    - Status
```

Platform implementations may render these as `/migrations-check`, `/migrations-apply`,
`/update-doc`, subcommands, skills, UI actions, or conversational intents.

## §3 — Trigger

The Tool runs when:

- relevant use requires a Required Migration check;
- an artefact is being modified and OnUpdate reconciliation is due;
- the user/AI explicitly asks to check/apply/update/resume migration;
- an active Migration failure/defer state is resumed; or
- another governing Standard/Tool invokes Migration.

## §4 — Inputs

Required/resolved inputs include:

- target artefact(s);
- current dependency declarations;
- Dependency Query facts;
- applicable `MigrationSummary` and detailed transition history when needed;
- current operation (`Use`, `Update`, explicit `Check/Apply/Resume`);
- current work authority/scope;
- applicable governing rules for exact-version constraints; and
- existing Migration-owned temporary state where present.

Infer safe low-cost facts; ask once for genuinely missing information; escalate substantive
ambiguity or authority conflicts.

## §5 — Check

1. Query relevant versioned dependencies.
2. For use, compare checkpoint to `LatestRequiredVersion`.
3. For update, compare checkpoint to current/OnUpdate summary state.
4. Load detailed history only where the summary indicates possible work.
5. Evaluate supported baseline and Scope.
6. Return pending Required, OnUpdate, None/NotApplicable, deferred/failed state, and any blocking
   condition.
7. Make no artefact change.

## §6 — Apply

1. Resolve all relevant pending migration work.
2. Order dependencies by declared dependency precedence unless specifically overridden.
3. Process versions oldest to newest.
4. Before each version, re-evaluate applicability/current state.
5. Apply ordered items and verify `Success`.
6. Preserve each successfully completed version as durable progress when saving is appropriate.
7. On Required-triggered update, continue through pending applicable OnUpdate/None versions to the
   current available version where possible.
8. Save only proven successful state and update dependency checkpoints accordingly.
9. Remove resolved Migration-owned temporary state.

## §7 — Update

`Update` is the explicit/idempotent document reconciliation action (commonly rendered
`/update-doc`).

It performs the intended document modification/update together with all pending applicable
Required and OnUpdate transition work through current. It does **not** stop merely because a
Required transition exists; the update is already the qualifying change/save event.

If migration cannot complete, preserve only the last successful state/checkpoint and report the
unresolved condition.

## §8 — Resume

1. Read persisted checkpoints and Migration-owned state.
2. Re-resolve current dependency/version facts.
3. Confirm that prior successful work remains present.
4. Resume from the first unresolved version; do not replay completed versions.
5. Update/replace/remove Migration-owned temporary state according to the new result.

## §9 — Status

Report at least:

- artefact;
- dependency;
- stored checkpoint;
- available/current version;
- summary relation;
- pending Required/OnUpdate work;
- supported-baseline result;
- Migration state: clear/deferred/failed;
- next action needed.

## §10 — Failure handling

### Version failure

Discard partial changes from the failed version, preserve prior successful work, persist the last
successful checkpoint when the artefact is saved, write/update compact Migration-owned state, and
report noisily with a suggested resolution where known.

### Deferred

Record authorised deferral and consequence in Migration-owned state; do not advance through the
deferred version.

### Concurrent change

Do not overwrite newer artefact state. Stop and report/reconcile.

### Moving dependency state

If resolved dependency/version facts change during execution, stop and resume against a stable
state.

### Missing/ambiguous transition

Stop and identify the owning capability/version; do not infer.

## §11 — Idempotency

Check and Status are read-only/idempotent. Update/Apply/Resume are resumable and must not duplicate
already completed version work. Re-running against an unchanged current artefact produces no
substantive migration change.

## §12 — Reporting

Summary reporting states what was checked/applied, the resulting checkpoint(s), and anything still
blocking or needing attention. Failures, deferrals, unsupported baselines, exact-version ambiguity,
and conflict always surface regardless of verbosity preference.

---

**Depends on:** `AIDE_Migration@v1`, `Capabilities_Migration_Design_v1`, `AIDE_Dependencies@v2`.

**References:** `Capabilities_Tools_Design_v2`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Migration_Tool_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Migration_Tool_v1.md -->
# AIDE Migration — Tool

> **Identity:** `AIDE_MigrationTool@v1`
> **Common name:** Migration
> **Version 1** (2026-08-30). Canonical platform-independent Migration Tool produced from
> `Capabilities_Migration_Tool_Design_v1`.

---

## Purpose

Check, apply, update, resume, and report migration of dependent artefacts under
`AIDE_Migration@v1`, preserving truthful saved conformance checkpoints and durable partial
progress.

## Logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v1
  CommonName: Migration
  PrimaryInvocation: migration
  LogicalActions: [Check, Apply, Update, Resume, Status]
```

Platform Build may render these actions as slash commands, skills, UI actions, or conversational
intents without changing their semantics.

## Trigger and inputs

Run when affected use requires a Required check, an artefact modification qualifies for OnUpdate,
a migration action is requested, unresolved Migration state is resumed, or another governing
Standard/Tool invokes Migration.

Resolve target artefact, dependencies and Dependency Query facts, applicable `MigrationSummary`,
detailed transitions when needed, current operation/authority, exact-version governing policy, and
existing Migration-owned state.

Infer safe low-cost facts; ask once for genuinely missing information; escalate substantive
ambiguity or authority conflict.

## Check

1. Query relevant versioned dependencies.
2. For use, compare checkpoints to `LatestRequiredVersion`.
3. For update, compare checkpoints to current/OnUpdate summary state.
4. Load detailed history only where the summary indicates possible work.
5. Evaluate supported baseline and Scope.
6. Return pending Required/OnUpdate work, traversable None/NotApplicable state, defer/failure state,
   and blocking conditions.
7. Make no artefact change.

## Apply

1. Resolve all relevant pending work before changing state.
2. Process dependencies by declared processing precedence unless specifically overridden.
3. Process versions oldest to newest and items in declared order.
4. Re-evaluate applicability before each version.
5. Apply items and verify each version's `Success` condition.
6. Preserve durable success stepwise.
7. When Required causes a save, continue through pending applicable OnUpdate/None versions to
   current where possible.
8. Save only proven state and advance checkpoints only through successfully traversed saved state.
9. Remove Migration-owned temporary state when resolved.

## Update

Perform the intended artefact modification together with all applicable Required and OnUpdate work
through current. Do not stop merely because Required work exists: the operation is already a
qualifying save event.

If work cannot complete, preserve only the last successful state/checkpoint and surface the
unresolved condition.

## Resume

Read persisted checkpoints/state, re-resolve current dependency facts, confirm earlier durable
success, and continue from the first unresolved version without replaying completed work.

## Status

Report artefact, dependency, checkpoint, available/current version, summary relation, pending
Required/OnUpdate work, supported-baseline result, clear/deferred/failed state, and next action.

## Failure and integrity

- Failed version: discard that version's partial changes; keep prior successful work/checkpoint;
  write/update compact Migration-owned state and report noisily.
- Deferred: preserve authorised deferral and consequence; do not advance through it.
- Concurrent artefact change: do not overwrite newer work.
- Moving dependency facts: stop and resume against stable state.
- Missing/ambiguous transition or exact-version treatment: stop and identify the unresolved owner
  decision rather than infer it.

Check/Status are read-only and idempotent. Apply/Update/Resume are resumable and must not duplicate
already completed version work.

## Reporting

Summary reporting states what was checked/applied, resulting checkpoints, and anything still
blocking or needing attention. Failure, defer, unsupported baseline, exact-version ambiguity, and
conflict always surface regardless of narration preference.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---

**Depends on:** `AIDE_Migration@v1`, `AIDE_Dependencies@v2`,
`Capabilities_Migration_Tool_Design_v1`.

**References:** `AIDE_Scope@v1`.

**Type:** `Tool` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
<!-- END SOURCE: AIDE_Migration_Tool_v1.md -->

---
