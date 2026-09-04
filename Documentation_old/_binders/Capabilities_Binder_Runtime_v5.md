# Capabilities Binder Runtime

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 5** (2026-09-03). Review D R1 remediation: snapshot-relative generated Tags and Scope plus exact Definition production checkpoints.

This Binder is a current-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Capabilities_Tags_Definition_v3.md` — sha256 `9e77ffaff99c`
- `Capabilities_Tags_Design_v3.md` — sha256 `bd38e876d0de`
- `AIDE_Tags_Standard_v3.md` — sha256 `11513e843c1d`
- `Capabilities_Scope_Definition_v3.md` — sha256 `bb0e3e4f2a39`
- `Capabilities_Scope_Design_v3.md` — sha256 `777debeca7c9`
- `AIDE_Scope_Standard_v3.md` — sha256 `c071b671b00d`
- `Capabilities_Dependencies_Definition_v3.md` — sha256 `98c2241506c6`
- `Capabilities_Dependencies_Design_v3.md` — sha256 `ee8326b631be`
- `AIDE_Dependencies_Standard_v3.md` — sha256 `87e82ecc7474`
- `Capabilities_Migration_Definition_v4.md` — sha256 `c9b7a569e431`
- `Capabilities_Migration_Brief_v3.md` — sha256 `4d5ff596096a`
- `Capabilities_Migration_Design_v3.md` — sha256 `6ef41a19c93d`
- `AIDE_Migration_Standard_v3.md` — sha256 `30ac2b2b3517`
- `Capabilities_Migration_Tool_Design_v3.md` — sha256 `eba8bfd8ceb1`
- `AIDE_Migration_Tool_v3.md` — sha256 `78d8a7c2edee`
- `Capabilities_Update_Tool_Design_v1.md` — sha256 `3e710a4eb312`
- `AIDE_Update_Tool_v1.md` — sha256 `45b75a29d3f8`

---

<!-- BEGIN SOURCE: Capabilities_Tags_Definition_v3.md -->
# Tags — Capability Definition

> **Version 3** (2026-09-03). Releases snapshot-relative generated-tag freshness and exact production checkpoints.

## Identity, purpose and boundary

**Capability:** `Tags@v2`

Provides generated classification and Boolean query semantics.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Tags.Standard` | Standard | `AIDE_Tags@v3` | v2 |

## Capability Release History

```text
Tags@v1
  Tags.Standard@v1 -> AIDE_Tags@v2

Tags@v2
  Tags.Standard@v2 -> AIDE_Tags@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Tags.Standard@v1` — baseline adoption of `AIDE_Tags@v2`; no new semantic change asserted.
- `Tags.Standard@v2` — defines producer-freeze and immutable snapshot-relative freshness for downstream consumers.

## Element Production

```yaml
ElementProduction:
  Tags.Standard:
    EvaluatedInputs:
      Capabilities_Tags_Design: v3
      AIDE_CapabilityBuild: v4
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v2
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Tags_Design_v3, AIDE_Tags@v3, AIDE_CapabilityBuild@v4
<!-- END SOURCE: Capabilities_Tags_Definition_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tags_Design_v3.md -->
# Capabilities Tags — Design

> **Version 3** (2026-09-03). Makes immutable package/runtime freshness snapshot-relative at the producer Build boundary.

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

When source information capable of changing generated tags changes, applicable Tag Builders run
before the artefact is published/saved as current where those tags form part of governed state.
Before tag-dependent behaviour relies on generated tags whose freshness is uncertain, rerun the
applicable builders first. An explicit rebuild/update operation may be used at any time.

Tags owns this generic freshness requirement but does not implement a runtime polling service or a
general dependency/execution-order engine. The operation changing/publishing/relying on the artefact
is responsible for invoking the applicable builders at the required boundary. If a builder needs
upstream derived information, that operation must make the upstream source current before the
builder runs.

For an immutable Build package/output, the required boundary is before Package/output freeze:

```text
exact authoritative Build source snapshot
        ↓
applicable Tag Builders run or validate
        ↓
freshness + snapshot provenance recorded
        ↓
immutable Package/output frozen
        ↓
Registry / Set / runtime consume frozen tags
```

Those tags are current for that immutable snapshot. Later producer-source change does not make the
package internally stale or authorise downstream regeneration; it may instead show that the built
or deployed release is behind current producer state.

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
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v15, Capabilities_Decisions_v21
References: Capabilities_Scope_Design_v3, Capabilities_Dependencies_Design_v3
<!-- END SOURCE: Capabilities_Tags_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Tags_Standard_v3.md -->
# AIDE Tags — Standard

> **Identity:** `AIDE_Tags@v3`
> **Common name:** Tags
> **Version 3** (2026-09-03). Defines snapshot-relative freshness for immutable built/deployed artefacts.

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

When source information capable of changing generated tags changes, run applicable Tag Builders
before the artefact is published/saved as current where those tags form part of governed state.
Before tag-dependent behaviour relies on generated tags whose freshness is uncertain, rerun the
applicable builders first. An explicit rebuild may be used at any time.

For an immutable Build package/output, run or validate applicable builders against the exact
authoritative source snapshot before freeze and preserve compact freshness/source-snapshot evidence.
The resulting tags remain current for that immutable snapshot. Registry, Deployment and runtime
consumers use those frozen tags; they do not rerun producer-owned builders merely because newer
upstream source now exists. Newer source requiring different tags makes the producer/build/deployed
state behind current source and requires a new producer update/build path.

Tags owns this freshness rule but does not provide runtime polling or a generic orchestration
engine. The changing/publishing/relying operation invokes the builders and supplies current source
state; builders do not reconstruct semantic inheritance or upstream state themselves.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Tags_Design_v3
References: AIDE_Scope@v3, AIDE_CapabilityBuild@v4
<!-- END SOURCE: AIDE_Tags_Standard_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Scope_Definition_v3.md -->
# Scope — Capability Definition

> **Version 3** (2026-09-03). Releases snapshot-relative Machine Scope and exact production checkpoints.

## Identity, purpose and boundary

**Capability:** `Scope@v2`

Provides applicability semantics using current Tags and contextual judgment.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Scope.Standard` | Standard | `AIDE_Scope@v3` | v2 |

## Capability Release History

```text
Scope@v1
  Scope.Standard@v1 -> AIDE_Scope@v2

Scope@v2
  Scope.Standard@v2 -> AIDE_Scope@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Scope.Standard@v1` — baseline adoption of `AIDE_Scope@v2`; no new semantic change asserted.
- `Scope.Standard@v2` — evaluates Machine Scope over the frozen Tags of an immutable artefact snapshot.

## Element Production

```yaml
ElementProduction:
  Scope.Standard:
    EvaluatedInputs:
      Capabilities_Scope_Design: v3
      AIDE_Tags: v3
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v2
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Scope_Design_v3, AIDE_Scope@v3, AIDE_Tags@v3
<!-- END SOURCE: Capabilities_Scope_Definition_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Scope_Design_v3.md -->
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
<!-- END SOURCE: Capabilities_Scope_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Scope_Standard_v3.md -->
# AIDE Scope — Standard

> **Identity:** `AIDE_Scope@v3`
> **Common name:** Scope
> **Version 3** (2026-09-03). Applies Machine Scope to the current Tags of the artefact snapshot being evaluated.

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

## Tag freshness

Machine Scope is deterministic only over current `AIDE_Tags` state. If generated-tag freshness is
uncertain, rerun the applicable Tag Builders under `AIDE_Tags` before relying on the Machine result.
Scope consumes that freshness rule; it does not own another regeneration mechanism.

For immutable built/deployed material, “current” means the Tags frozen for that exact artefact
snapshot after producer-side freshness validation. Machine Scope evaluates that snapshot; it does
not mutate the artefact or rerun producer-owned builders to chase later upstream source.

## Context Scope

Context Scope is descriptive applicability interpreted by the AI. Use it for semantic or
judgment-based conditions that would make the machine expression unnecessarily complex.

## Platform realisation

Concrete discovery and trigger mechanisms are platform Build concerns. Platform builders may use
Scope declarations to create effective target-platform metadata, but this Standard does not
define plugin, skill, repository, bundle, or platform-specific trigger mechanics.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Tags@v3, Capabilities_Scope_Design_v3
<!-- END SOURCE: AIDE_Scope_Standard_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Dependencies_Definition_v3.md -->
# Dependencies — Capability Definition

> **Version 3** (2026-09-03). Replaces prose production state with an exact evaluated-input checkpoint.

## Identity, purpose and boundary

**Capability:** `Dependencies@v1`

Provides dependency identity, importance, version and conformance-checkpoint semantics.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Dependencies.Standard` | Standard | `AIDE_Dependencies@v3` | v1 |

## Capability Release History

```text
Dependencies@v1
  Dependencies.Standard@v1 -> AIDE_Dependencies@v3
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Dependencies.Standard@v1` — baseline adoption of `AIDE_Dependencies@v3`; no new semantic change asserted.

## Element Production

```yaml
ElementProduction:
  Dependencies.Standard:
    EvaluatedInputs:
      Capabilities_Dependencies_Design: v3
      AIDE_DocumentationMethodology: v28
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Dependencies_Design_v3, AIDE_Dependencies@v3
<!-- END SOURCE: Capabilities_Dependencies_Definition_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Dependencies_Design_v3.md -->
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
<!-- END SOURCE: Capabilities_Dependencies_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Dependencies_Standard_v3.md -->
# AIDE Dependencies — Standard

> **Identity:** `AIDE_Dependencies@v3`
> **Common name:** Dependencies
> **Version 3** (2026-09-01). Defines position-dependent capability-reference semantics, non-ordering checkpoints, hard exact constraints and local declaration precedence.

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

This is processing/foundational precedence, not requirement severity. It applies to dependencies of
the artefact being processed and does not sequence independent artefacts or peer Bootstrap
Contributions. A conformance checkpoint by itself creates no processing order.

## Reference positions

Position determines the role of a capability version reference:

| Position | Meaning |
|---|---|
| `Dependencies: X@vN` | this artefact's last saved/proven conformance checkpoint against X |
| `Dependencies: X@!vN` | hard present exact-version constraint |
| `Dependencies: X` | dependency without version tracking |
| `References:` | reader/evidence pointer; no currency or conformance obligation |
| current executable body | operational instruction; versionless by default, specific release only when deliberately required |

A checkpoint is backward-looking saved evidence. It imposes no resolution/execution order and
mutual checkpoints are not an operational dependency cycle. Newer availability alone does not make
a behind-current checkpoint stale or defective.

Canonical production validates current executable capability references separately from dependency
checkpoint advancement.

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

`abc@!v8` requires exactly v8 to be available. If it is unavailable the dependency is unsatisfied
and affected use requiring it is blocked; another version may not silently substitute. The mismatch
is not a saved conformance gap or ordinary Migration trigger. Changing/removing the pin is an
explicit dependent-artefact change that is validated and saved normally.

## Required/startup-required

`!` is checked on relevant use/access and missing identity is surfaced prominently.

`!!` additionally requests a best-effort startup **presence** check through the Core bootstrap
mechanism. It does not imply a general startup Migration scan.

## Dependency Builder

Standards may contribute `AIDE_DependencyBuilder` definitions. Builders own only their generated
Group/Prefix output, preserve meaningful order, are idempotent, and fail visibly when applicable
output cannot be derived correctly. Group keys remain invisible to non-owning consumers.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Dependencies_Design_v3
References: AIDE_Migration@v2
<!-- END SOURCE: AIDE_Dependencies_Standard_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Definition_v4.md -->
# Migration — Capability Definition

> **Version 4** (2026-09-03). Replaces prose production state with exact evaluated-input checkpoints.

## Identity, purpose and boundary

**Capability:** `Migration@v2`

Provides transition declaration, discovery, execution and progress semantics.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Migration.Standard` | Standard | `AIDE_Migration@v3` | v2 |
| `Migration.Tool` | Tool | `AIDE_MigrationTool@v3` | v2 |
| `Migration.UpdateTool` | Tool | `AIDE_UpdateTool@v1` | v1 |

## Capability Release History

```text
Migration@v1
  Migration.Standard@v1 -> AIDE_Migration@v2
  Migration.Tool@v1 -> AIDE_MigrationTool@v2

Migration@v2
  Migration.Standard@v2 -> AIDE_Migration@v3
  Migration.Tool@v2 -> AIDE_MigrationTool@v3
  Migration.UpdateTool@v1 -> AIDE_UpdateTool@v1
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Migration.Standard@v1` — baseline adoption of `AIDE_Migration@v2`; no new semantic change asserted.
- `Migration.Tool@v1` — baseline adoption of `AIDE_MigrationTool@v2`; no new semantic change asserted.
- `Migration.Standard@v2` — clarifies aggregate-operation/per-artefact ownership and authoritative-corpus treatment in `AIDE_Migration@v3`.
- `Migration.Tool@v2` — narrows `AIDE_MigrationTool@v3` to one artefact per invocation within aggregate orchestration.
- `Migration.UpdateTool@v1` — introduces `AIDE_UpdateTool@v1` for aggregate target resolution, selection, orchestration and reporting.

## Element Production

```yaml
ElementProduction:
  Migration.Standard:
    EvaluatedInputs: {Capabilities_Migration_Design: v3, AIDE_DocumentationMethodology: v28}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v2
  Migration.Tool:
    EvaluatedInputs: {Capabilities_Migration_Tool_Design: v3, AIDE_Migration: v3}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v2
  Migration.UpdateTool:
    EvaluatedInputs: {Capabilities_Update_Tool_Design: v1, AIDE_Migration: v3}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Migration_Design_v3, AIDE_Migration@v3, AIDE_MigrationTool@v3, AIDE_UpdateTool@v1
<!-- END SOURCE: Capabilities_Migration_Definition_v4.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Brief_v3.md -->
# Capabilities Migration — Brief

> **Version 3** (2026-09-02). Adds aggregate Required-Migration and Update operations without changing per-artefact transition ownership.

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

- `AIDE_Migration@v3` — the stable authoring, build, checking, execution, and state contract;
- a per-artefact Migration Tool providing Check, Apply, Update, Status/Resume behaviour; and
- `AIDE_UpdateTool@v1` — aggregate target resolution, authoritative-corpus selection,
  orchestration and reporting across Domains, Documentation Topics or selected artefact sets.

Domain-wide Required Migration selects only artefacts with outstanding applicable Required work;
it does not sweep artefacts solely because OnUpdate work exists. An explicitly requested aggregate
Update is the qualifying update operation and reconciles applicable Required and OnUpdate work for
each selected authoritative artefact under normal per-artefact Migration rules.

## Boundaries

Migration does not own:

- dependency identity or version-state resolution — Dependencies;
- applicability language — Scope;
- document placement/rendering for temporary operational state — Documentation Methodology;
- platform-specific skill/plugin/bundle representations — Build-side platform Standards/Tools;
- installation/distribution — Deployment; or
- dependency exact-version satisfaction — Dependencies; an unsatisfied exact pin blocks affected
  use and is not an ordinary Migration version gap. Migration does not silently move or relax pins.

## Success signals

- A consumer can determine cheaply whether Required work may exist before loading migration detail.
- Required work blocks only affected use, not unrelated work or session startup by default.
- OnUpdate work waits safely until modification.
- Transition execution is ordered, resumable, and truthful about partial success.
- The conformance checkpoint always represents the last state actually proven and saved.
- Platform implementations can optimise discovery without changing Migration semantics.
- Aggregate operations never rewrite external-owner/consuming artefacts merely because they are
  reachable from a selected Domain; they report them unless explicitly selected with authority.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v14, Capabilities_Migration_Design_v3
References: AIDE_Dependencies@v3, AIDE_Scope@v2, AIDE_Domain, AIDE_UpdateTool@v1
<!-- END SOURCE: Capabilities_Migration_Brief_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Design_v3.md -->
# Capabilities Migration — Design

> **Version 3** (2026-09-02). Adds aggregate Update orchestration and authoritative-corpus rules while retaining per-artefact transition ownership.

---

## Contents

- **Purpose and transition model** — ownership, version-level postures and owner-authored declarations. §1–§4
- **Discovery and triggers** — MigrationSummary fast paths plus Required and OnUpdate activation. §5–§7
- **Execution state** — checkpoints, dependency ordering, outcomes and durable partial progress. §8–§11
- **Constraints and failure safety** — exact pins, supported baselines and edge conditions. §12–§14
- **External and aggregate seams** — produced outcomes, aggregate target operations and authority boundaries. §15–§16

## Summary

Migration moves one dependent artefact from its last saved, proven dependency conformance checkpoint
toward the currently available dependency version using explicit owner-authored transitions. Each
release declares one posture—Required, OnUpdate or None—and Migration evaluates applicability,
orders work, verifies success, preserves durable partial progress and advances a checkpoint only
through state actually proven and saved.

Required work blocks only affected reliance; OnUpdate work waits for a qualifying modification.
When Required work itself causes a save, normal per-artefact rules also reconcile applicable
OnUpdate work through current where possible. Exact-version constraint failure is a present
dependency block, not an inferred migration gap.

Aggregate selection is a separate orchestration responsibility. `AIDE_UpdateTool` resolves Domains,
session Domains, Documentation Topics, explicit artefacts or criteria-selected sets, limits mutation
to the selected authoritative corpus, invokes per-artefact Migration behaviour and reports the
whole result. Domain-wide Required Migration selects artefacts because Required work is outstanding;
aggregate Update intentionally qualifies each selected artefact for Required and OnUpdate
reconciliation. External-owner artefacts are report-only unless separately selected and authorised.

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

A saved conformance checkpoint does not create resolution/execution order. Mutual conformance
relationships between artefacts create no cross-artefact migration order. Declaration precedence
applies to dependencies of the artefact being processed only where the migration operation needs
deterministic ordering.


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

`AIDE_Dependencies` owns `X@!vN` as a hard present exact-version constraint. Migration does not treat
it as a saved conformance checkpoint or ordinary version gap.

Before affected migration/use, Dependency Query checks the constraint. If exact vN is unavailable:

- the dependency is unsatisfied;
- affected use/migration requiring it is blocked;
- another version may not silently substitute; and
- Migration reports the dependency block rather than inventing a transition or pin policy.

Changing/removing the pin is an explicit modification of the dependent artefact under its owning
work/Standard and is then saved/validated normally. A governing consumer may impose additional
handling but cannot silently treat an unsatisfied exact constraint as satisfied.

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

- `AIDE_Migration@v3`;
- `Capabilities_Migration_Tool_Design_v3`; and
- `Capabilities_Update_Tool_Design_v1`.

Migration consumes:

- `AIDE_Dependencies` for dependency/version facts and default dependency order;
- `AIDE_Scope` for applicability;
- governing capability Standards for transition intent and any additional exact-version handling beyond the Dependencies hard constraint;
- Documentation Methodology for generic temporary document-state placement/rendering; and
- Build-side platform knowledge for summary/detail representation.

Deployment distributes built transition material but does not own its semantics.

## §16 — Aggregate Update orchestration

The higher-level `AIDE_UpdateTool` owns aggregate target resolution, selection, orchestration and
reporting. It may target:

- one Domain;
- multiple explicitly named Domains;
- the Domains participating in the current session/Working Context;
- one Documentation Topic;
- explicitly identified artefacts; or
- a criteria-selected set within an authorised boundary.

Criteria may use facts supplied by their owners, including document/artefact type, identity,
dependency, Tags/Scope, migration posture/state or current-versus-checkpoint relation. Selection
does not invent Domain membership, semantic ownership or authority.

The selected mutation corpus contains only artefacts authoritative within the selected target and
current work authority. A consuming copy, external-owner source or reachable dependency outside
that corpus is reported rather than rewritten. It may be mutated only when it is itself explicitly
selected through an authoritative target and the operation has authority to change it. Selecting
several Domains means resolving each Domain's authoritative corpus; it does not create Domain
inheritance or merge semantics.

Two aggregate operations are distinct:

1. **Required Migration** — discover the selected authoritative corpus and invoke per-artefact
   Apply only for artefacts with outstanding applicable Required work. An artefact is not selected
   solely for OnUpdate work. Once a Required migration causes a save, the normal §7 per-artefact
   rule may reconcile its pending applicable OnUpdate/None versions through current.
2. **Update** — treat the explicit aggregate request as a qualifying update for every selected
   authoritative artefact and invoke per-artefact Update, reconciling all applicable outstanding
   Required and OnUpdate work through current where possible.

`AIDE_Migration` and `AIDE_MigrationTool` remain the owners/executors of transition resolution,
ordering, success, partial progress, failure/defer state and dependency-checkpoint advancement for
each artefact. The aggregate Tool does not redefine those semantics or claim checkpoint progress
from aggregate completion alone.

For common governed-document conformance, use the genuine
`AIDE_DocumentationMethodology` dependency. Do not introduce a synthetic universal `AIDE_Doc`
dependency solely to create an aggregate migration hook. Artefacts participate through their real
declared dependencies and the selected authoritative corpus.

Aggregate reporting identifies target resolution, authoritative selection, exclusions/skips,
per-artefact result and resulting checkpoint, plus all blockers, failures, deferrals and partial
completion. A failed artefact does not erase other already-proven successful artefact updates, but
the overall result remains partial until every selected obligation is truthfully accounted for.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v14, Capabilities_Decisions_v20, AIDE_Dependencies@v3, AIDE_Scope@v2
References: Capabilities_Migration_Brief_v3, AIDE_Domain, AIDE_UpdateTool@v1
<!-- END SOURCE: Capabilities_Migration_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Migration_Standard_v3.md -->
# AIDE Migration — Standard

> **Identity:** `AIDE_Migration@v3`
> **Common name:** Migration
> **Version 3** (2026-09-02). Defines the aggregate-operation seam and authoritative-corpus treatment while preserving per-artefact Migration semantics.

---

## Contents

- **Transition contract** — postures, summaries, owner declarations and affected-use/update triggers.
- **Execution integrity** — ordering, saved checkpoints, outcomes, failure state and resumability.
- **Dependency constraints** — exact-version blocks and supported-baseline handling.
- **Aggregate operation seam** — authoritative selection plus Required-Migration and Update behaviour.

## Summary

Migration applies owner-declared version transitions to one dependent artefact at a time. Required
work gates affected reliance; OnUpdate work waits for a qualifying save; None requires no consumer
transformation. Only verified saved state advances dependency conformance checkpoints, and partial
success remains durable and resumable.

`AIDE_UpdateTool` may orchestrate this behaviour over Domains, session Domains, Documentation
Topics, explicit artefacts or criteria-selected sets. It owns aggregate selection and reporting,
but each artefact remains governed by this Standard and `AIDE_MigrationTool`. Required-Migration
selection does not sweep OnUpdate-only artefacts; explicit aggregate Update reconciles Required and
OnUpdate work for every selected authoritative artefact.

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
- Process dependencies of the artefact being processed in their declared order unless a more specific
  governing order applies. A saved conformance checkpoint creates no ordering by itself; mutual
  conformance checkpoints between artefacts create no cross-artefact migration order.
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

`X@!vN` is a hard present dependency constraint owned by `AIDE_Dependencies`, not a saved
conformance checkpoint or ordinary Migration gap. If exact vN is unavailable, affected use or
migration requiring the dependency is blocked and another version may not silently substitute.
Migration reports the dependency block and does not move/relax the pin by inference. Changing the
pin is an explicit dependent-artefact modification.

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

## Aggregate operations and authority

`AIDE_UpdateTool` owns aggregate target resolution, authoritative-corpus selection, orchestration
and whole-operation reporting. Supported target forms are one Domain, multiple Domains, current
session Domains, a Documentation Topic, explicit artefacts and criteria-selected sets inside an
authorised boundary.

Mutation is limited to authoritative artefacts within the selected target and work authority.
External-owner/consuming artefacts encountered through reachability or dependency resolution are
reported and skipped unless independently selected through an authoritative target with authority
to modify them. Multi-Domain selection does not imply Domain inheritance or merging.

For aggregate **Required Migration**, select/invoke Apply only where applicable Required work is
outstanding. Do not select an artefact solely for OnUpdate work. If Required work causes a save,
normal per-artefact OnUpdate-through-current behaviour still applies.

For aggregate **Update**, the explicit request is a qualifying update for each selected authoritative
artefact. Invoke per-artefact Update and reconcile applicable Required and OnUpdate work through
current where possible.

The aggregate result never advances dependency checkpoints itself. Per-artefact Migration advances
only through proven saved state and reports Completed, NotApplicable, Deferred or Failed truthfully.
Preserve successful artefacts when another fails and report overall partial completion.

Governed documents participate through their genuine `AIDE_DocumentationMethodology` dependency.
Do not create or require a synthetic universal `AIDE_Doc` dependency solely as a migration hook.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Migration_Design_v3, AIDE_Dependencies@v3, AIDE_Scope@v2
References: AIDE_MigrationTool@v3, AIDE_UpdateTool@v1, AIDE_Domain
<!-- END SOURCE: AIDE_Migration_Standard_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Migration_Tool_Design_v3.md -->
# Capabilities Migration Tool — Design

> **Version 3** (2026-09-02). Narrows execution to one artefact per invocation under optional aggregate Update orchestration.

---

## Contents

- **Identity, trigger and inputs** — per-artefact Tool boundary and resolved execution facts. §1–§4
- **Actions** — Check, Apply, Update, Resume and Status behaviour. §5–§9
- **Integrity and reporting** — failures, idempotency, aggregate seam and returned result. §10–§13

## Summary

The Migration Tool executes `AIDE_Migration` for one target artefact. It checks pending transition
work, applies Required work before affected reliance, performs qualifying Update reconciliation,
resumes from durable checkpoints and reports exact outcomes without inferring missing transition or
authority decisions.

Aggregate selection belongs to `AIDE_UpdateTool`. That Tool may invoke this one repeatedly, but it
cannot redefine per-artefact ordering, success, failure/defer state or checkpoint advancement.

## §1 — Output and boundary

This Design produces one canonical **Migration Tool**. It orchestrates `AIDE_Migration@v3` against
Dependency Query results and one artefact in hand.

The Tool does not author transition intent, define dependency identity/version semantics, define
Scope, decide document-state placement, resolve aggregate target/corpus selection, or implement
platform-specific command/skill/plugin rendering.

## §2 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v3
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

- one target artefact;
- current dependency declarations;
- Dependency Query facts;
- applicable `MigrationSummary` and detailed transition history when needed;
- current operation (`Use`, `Update`, explicit `Check/Apply/Resume`);
- current work authority/scope;
- exact-version constraint result from `AIDE_Dependencies`; and
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

### Unsatisfied exact-version constraint

Treat the dependency as blocked for affected use. Do not run an ordinary migration gap or silently
substitute/move the pin; report the constraint and the explicit owner change required to alter it.

## §11 — Idempotency

Check and Status are read-only/idempotent. Update/Apply/Resume are resumable and must not duplicate
already completed version work. Re-running against an unchanged current artefact produces no
substantive migration change.

## §12 — Reporting

Summary reporting states what was checked/applied, the resulting checkpoint(s), and anything still
blocking or needing attention. Failures, deferrals, unsupported baselines, exact-version constraint failure,
and conflict always surface regardless of verbosity preference.

## §13 — Aggregate orchestration seam

`AIDE_UpdateTool` may resolve a larger authorised selection and invoke Check/Apply/Update/Resume for
each artefact. This Tool accepts the resolved single target and operation authority; it does not
expand the corpus, traverse external-owner dependencies for mutation or claim aggregate success.

Return a structured per-artefact result sufficient for the caller to report selected dependency
transitions, saved checkpoints, skips, blockers, failure/defer state and next action. The caller's
aggregate failure does not roll back already-proven durable success in this artefact, and failure in
this artefact does not authorise changes to another.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, Capabilities_Migration_Design_v3, AIDE_Dependencies@v3
References: Capabilities_Tools_Design_v7, AIDE_UpdateTool@v1
<!-- END SOURCE: Capabilities_Migration_Tool_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Migration_Tool_v3.md -->
# AIDE Migration — Tool

> **Identity:** `AIDE_MigrationTool@v3`
> **Common name:** Migration
> **Version 3** (2026-09-02). Executes one-artefact Migration under optional aggregate Update orchestration.

---

## Contents

- **Purpose, actions and inputs** — the per-artefact execution contract.
- **Check, Apply, Update, Resume and Status** — logical behaviours and checkpoint handling.
- **Integrity, reporting and aggregate seam** — failure safety, resumability and caller interaction.

## Summary

This Tool checks and executes `AIDE_Migration` for one target artefact, preserves only proven saved
progress, resumes without replaying completed work and reports every blocker or partial result.
Aggregate corpus selection is owned by `AIDE_UpdateTool`, which may invoke this Tool but cannot
alter its per-artefact transition or checkpoint semantics.

## Purpose

Check, apply, update, resume, and report migration of dependent artefacts under
`AIDE_Migration@v3`, preserving truthful saved conformance checkpoints and durable partial
progress.

## Logical actions

```yaml
Tool:
  Identity: AIDE_MigrationTool@v3
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

Resolve one target artefact, dependencies and Dependency Query facts, applicable `MigrationSummary`,
detailed transitions when needed, current operation/authority, exact-version constraint result, and
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
- Missing/ambiguous transition: stop and identify the unresolved owner decision rather than infer it.
- Unsatisfied exact-version constraint: block affected use, report the required exact version, and do
  not substitute/move the pin through Migration.

Check/Status are read-only and idempotent. Apply/Update/Resume are resumable and must not duplicate
already completed version work.

## Reporting

Summary reporting states what was checked/applied, resulting checkpoints, and anything still
blocking or needing attention. Failure, defer, unsupported baseline, exact-version constraint failure, and
conflict always surface regardless of narration preference.

## Aggregate caller seam

`AIDE_UpdateTool` may invoke this Tool once per artefact after resolving an authorised aggregate
selection. Do not expand that resolved target, mutate reachable external-owner artefacts or report
aggregate completion. Return the target's selected transitions, saved checkpoints, skips, blockers,
failure/defer state and next action so the caller can compose a truthful whole-operation report.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, AIDE_Dependencies@v3, Capabilities_Migration_Tool_Design_v3
References: AIDE_Scope@v2, AIDE_UpdateTool@v1
<!-- END SOURCE: AIDE_Migration_Tool_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Update_Tool_Design_v1.md -->
# Capabilities Update Tool — Design

> **Version 1** (2026-09-02). Defines aggregate Required-Migration and Update orchestration across authorised AIDE targets.

---

## Contents

- **Purpose and identity** — aggregate orchestration boundary and logical actions. §1–§2
- **Targets and selection** — supported selectors, authority and authoritative-corpus rules. §3–§5
- **Operations** — Resolve, Check Required, Apply Required, Update and Status. §6–§10
- **Execution integrity** — ordering, idempotency, failures and reporting. §11–§14
- **Ownership boundaries** — genuine dependencies and external capability seams. §15

## Summary

The Update Tool applies AIDE migration/update behaviour to an explicitly selected collection rather
than requiring each artefact to be named and invoked manually. It can resolve one or several
Domains, the Domains active in the current session, a Documentation Topic, explicit artefacts or a
criteria-selected set.

The Tool owns aggregate target resolution, selection, orchestration and reporting. It mutates only
artefacts authoritative within the selected target and current work authority; consuming or
external-owner artefacts are reported rather than rewritten unless independently selected with
authority. It delegates every artefact's transition evaluation, application, failure state and
dependency-checkpoint advancement to `AIDE_Migration`/`AIDE_MigrationTool`.

Required Migration and Update are deliberately different aggregate operations. Required Migration
selects only artefacts with outstanding applicable Required work; OnUpdate-only artefacts are not
swept. Update is an explicit qualifying update for every selected authoritative artefact and
reconciles its applicable Required and OnUpdate work through current where possible.

## §1 — Purpose and boundary

Repeated per-artefact Migration is insufficient when an operator needs to bring a coherent
authoritative corpus forward. This Tool provides the reusable aggregate action while preserving the
existing transition owner and checkpoint truth.

It does not define Domain membership, Documentation Topic structure, dependency/version facts,
transition semantics, applicability language, artefact authority or platform implementation.

## §2 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_UpdateTool@v1
  CommonName: Update
  PrimaryInvocation: update
  LogicalActions:
    - Resolve
    - CheckRequired
    - ApplyRequired
    - Update
    - Status
```

Platform builds may expose conversational intents, commands, skills, UI actions or automation while
preserving these semantics.

### Trigger

Run on explicit user/work-owner request or invocation by an authorised governing Standard/Tool.
Selecting `SessionDomains` does not create an automatic session-start migration sweep; it only
defines the target of an invoked aggregate operation. Any environment-specific scheduled/automatic
invocation must carry its own authority and must not change Migration's affected-use default.

## §3 — Target forms

The caller supplies exactly one aggregate target expression:

```yaml
Target:
  Kind: Domain | Domains | SessionDomains | DocumentationTopic | Artefacts | Criteria
  Value: <identity/list/query where required>
```

- `Domain` — one resolved AIDE Domain.
- `Domains` — an explicit ordered set of resolved AIDE Domains.
- `SessionDomains` — the Domains participating in the current Working Context/session.
- `DocumentationTopic` — the current authoritative corpus registered for one Documentation Topic.
- `Artefacts` — an explicit ordered set of artefact identities/locators.
- `Criteria` — a selection query inside an explicitly bounded authorised search corpus.

Several selected Domains remain separate Domains. Selection does not create Domain inheritance,
merging or a new parent Domain.

## §4 — Criteria and discovery facts

Criteria may consume owner-supplied facts such as:

- artefact/document type, identity or location;
- declared dependency or checkpoint relation;
- migration posture/state;
- Tags and Scope facts; and
- authoritative/current status within the bounded corpus.

Use the strongest available authoritative Index/Domain/Topic registers and direct corpus discovery.
Do not infer authority or membership merely because a file is reachable or mentions another item.
Unresolvable selection facts are reported; substantive ambiguity is not silently guessed.

## §5 — Authority and mutation corpus

Resolve the **selected authoritative corpus** before mutation.

An artefact is mutable only when:

1. it is inside the resolved target expression;
2. it is authoritative for that target rather than a consuming copy/reference;
3. the current work authority permits its modification; and
4. the requested operation applies to it.

External-owner artefacts and consuming copies encountered through dependencies, links or search are
report-only. They may be changed only through a separate explicit authoritative selection and
appropriate authority. Do not expand to dependency closure by default.

## §6 — Resolve

`Resolve` is read-only.

1. Resolve target identities/boundaries using their owning contracts.
2. Enumerate candidate artefacts.
3. classify authoritative, consuming/external, duplicate, excluded and unresolved candidates;
4. apply criteria where present; and
5. return the deterministic selected corpus and all exclusions/ambiguities.

## §7 — Check Required

`CheckRequired` is read-only.

For each selected authoritative artefact, invoke per-artefact Migration Check for relevant
dependencies and report whether applicable Required work is outstanding. Do not classify an
artefact as requiring action solely because OnUpdate work or a behind-current checkpoint exists.

## §8 — Apply Required

1. Resolve/freeze the selected authoritative corpus for this run.
2. Check each artefact under `AIDE_Migration`.
3. Invoke per-artefact Apply only for outstanding applicable Required work.
4. Preserve and report each proven saved result/checkpoint.
5. Do not select another artefact merely because it has OnUpdate-only work.

When Required work causes a save, that artefact follows normal Migration behaviour: pending
applicable OnUpdate/None versions may be traversed through current in the same save where possible.

## §9 — Update

`Update` is an explicitly authorised qualifying update for every artefact in the selected
authoritative corpus.

For each target, invoke per-artefact Migration Update so all applicable outstanding Required and
OnUpdate work is reconciled through current where possible. `None`/NotApplicable versions may be
included in the next proven saved checkpoint under normal Migration rules.

Do not invent a substantive content change merely to advance a checkpoint. The operation applies
declared transition work and saves only the truthful resulting artefact state.

## §10 — Status

Report current/resolved aggregate state without mutation, including prior partial/failure/defer
state where available and the next action needed.

## §11 — Aggregate ordering

Preserve explicit target order where supplied. Otherwise use the authoritative Index/corpus order
or a stable identity order and report it. This order is operational determinism, not semantic
cross-artefact dependency order.

Each artefact independently follows `AIDE_Migration` dependency/version/item ordering. Do not infer
a cross-artefact migration graph from mutual conformance checkpoints.

## §12 — Idempotency and concurrency

Resolve/CheckRequired/Status are read-only. Re-running ApplyRequired or Update against unchanged
successfully current artefacts produces no duplicate substantive effect.

Before saving an artefact, detect conflicting concurrent change under the per-artefact Tool. Do not
overwrite newer authority. Re-resolve only the affected artefact or stop the run where the target
boundary itself has changed materially.

## §13 — Failure and partial completion

Aggregate execution is stepwise rather than globally transactional. Preserve successful
per-artefact updates/checkpoints. For Failed, Deferred, UnsupportedBaseline, exact-version block,
authority failure or unresolved selection:

- preserve the exact per-artefact result/state;
- continue with independent targets where safe and authorised;
- do not mark the aggregate operation complete; and
- return overall `Partial` or `Failed` truthfully with the outstanding set.

Resume re-resolves current facts and does not replay already-proven work.

## §14 — Reporting

Report at least:

- requested target expression and logical action;
- resolved Domains/Topic/boundary and authority basis;
- selected authoritative artefacts;
- consuming/external, excluded, duplicate and unresolved candidates;
- per-artefact Check/Apply/Update result, changed state and resulting checkpoints;
- skipped/current/NotApplicable outcomes;
- blockers, failures, deferrals and partial completion; and
- aggregate status plus next action.

Narration may be compact, but the persisted/returned operation result must remain sufficient to
reconcile every selected target.

## §15 — Ownership and dependency boundaries

- `AIDE_Domain` owns Domain resolution/membership.
- Documentation Methodology/Index owns Documentation Topic corpus navigation.
- `AIDE_Tags`/`AIDE_Scope` own classification/applicability facts used by criteria.
- `AIDE_Dependencies` owns dependency identity/version/checkpoint facts.
- `AIDE_Migration`/`AIDE_MigrationTool` own all per-artefact transition and checkpoint semantics.
- Working Context supplies current session Domains and work authority.
- Platform Build owns concrete commands/skills/UI/automation.

Governed documents participate through their genuine `AIDE_DocumentationMethodology` dependency.
Do not introduce or require a synthetic universal `AIDE_Doc` dependency solely to make aggregate
update selection possible.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, AIDE_MigrationTool@v3, AIDE_Dependencies@v3, AIDE_Scope@v2
References: Capabilities_Migration_Design_v3, AIDE_Domain, AIDE_Index@v2, AIDE_Tags@v2
<!-- END SOURCE: Capabilities_Update_Tool_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Update_Tool_v1.md -->
# AIDE Update — Tool

> **Identity:** `AIDE_UpdateTool@v1`
> **Common name:** Update
> **Version 1** (2026-09-02). Introduces aggregate Required-Migration and Update orchestration over authorised AIDE targets.

---

## Contents

- **Target and authority** — supported aggregate selectors and authoritative-corpus boundary.
- **Actions** — Resolve, Check Required, Apply Required, Update and Status.
- **Execution integrity** — ordering, partial completion, idempotency and reporting.

## Summary

Use this Tool to apply migration/update behaviour across one or more Domains, current session
Domains, a Documentation Topic, explicit artefacts or a criteria-selected set. The Tool resolves
and reports the aggregate selection, but delegates each artefact's transition work and checkpoint
advancement to `AIDE_MigrationTool`.

Apply Required selects only artefacts with outstanding applicable Required work. Update is a
qualifying update for every selected authoritative artefact and reconciles its applicable Required
and OnUpdate work. Consuming/external-owner artefacts remain report-only unless separately selected
with authority.

## Logical actions

```yaml
Tool:
  Identity: AIDE_UpdateTool@v1
  CommonName: Update
  PrimaryInvocation: update
  LogicalActions: [Resolve, CheckRequired, ApplyRequired, Update, Status]
```

Run on explicit user/work-owner request or authorised governing Standard/Tool invocation.
`SessionDomains` is a target selector, not an automatic startup sweep. Platform automation requires
its own authority and does not change `AIDE_Migration` trigger semantics.

## Target

Accept exactly one:

```yaml
Target:
  Kind: Domain | Domains | SessionDomains | DocumentationTopic | Artefacts | Criteria
  Value: <identity/list/query where required>
```

Resolve membership and current authoritative artefacts through the applicable Domain,
Documentation Topic/Index and Working Context contracts. Multiple Domains remain separate;
selection does not create inheritance or merge semantics.

Criteria may use owner-supplied type, identity, dependency/checkpoint, Tags/Scope,
migration-state/posture and current/authoritative facts inside an explicitly bounded corpus.

## Authority

Mutate only artefacts that are both authoritative within the resolved target and within current
work authority. Report and skip consuming copies, external-owner sources, dependency-reachable
artefacts outside the target, unresolved authority and excluded candidates. Do not expand to
dependency closure or infer authority from filesystem reachability.

## Resolve

Read-only: return the deterministic candidate classification and selected authoritative corpus,
including every exclusion or ambiguity.

## Check Required

Read-only: invoke per-artefact Migration Check and report outstanding applicable Required work.
Behind-current or OnUpdate-only state does not by itself select an artefact for required action.

## Apply Required

Invoke per-artefact Apply only where Required work is outstanding. Do not sweep OnUpdate-only
artefacts. If Required work saves an artefact, allow normal per-artefact reconciliation through
pending applicable OnUpdate/None versions.

## Update

Treat the explicit request as a qualifying update for every selected authoritative artefact and
invoke per-artefact Update. Reconcile applicable Required and OnUpdate work through current where
possible. Do not invent substantive content merely to advance metadata; save only truthful proven
state.

## Status

Return current aggregate selection/progress, prior failure/defer state where available and next
actions without mutation.

## Ordering and integrity

Use explicit target order, otherwise authoritative corpus order or stable identity order, and
report it. This is operational order only. Each artefact retains `AIDE_Migration` dependency,
version and item order.

Resolve/CheckRequired/Status are read-only. ApplyRequired/Update are resumable and must not duplicate
proven work. Detect concurrent artefact changes and never overwrite newer authority.

## Partial completion

Preserve successful artefact updates/checkpoints when another target fails or defers. Continue with
independent targets where safe. Return `Partial`/`Failed` with every outstanding target; never claim
aggregate completion from partial per-artefact success.

## Reporting

Report target/action, resolved boundaries/authority, selected artefacts, exclusions and unresolved
candidates, per-artefact result/change/checkpoints, skipped/current/NotApplicable outcomes,
blockers/failures/deferrals and aggregate status/next action.

## Ownership boundary

This Tool owns only aggregate target resolution, selection, orchestration and reporting.
`AIDE_Migration`/`AIDE_MigrationTool` own each artefact's transition discovery, ordering, success,
failure/defer state, durable progress and dependency-checkpoint advancement.

Use genuine declared dependencies. Governed documents use `AIDE_DocumentationMethodology`; do not
create a synthetic universal `AIDE_Doc` dependency solely as an update/migration hook.

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
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, AIDE_MigrationTool@v3, AIDE_Dependencies@v3, AIDE_Scope@v2
References: Capabilities_Update_Tool_Design_v1, AIDE_Domain, AIDE_Index@v2, AIDE_Tags@v2
<!-- END SOURCE: AIDE_Update_Tool_v1.md -->
