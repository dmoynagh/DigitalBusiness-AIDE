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
