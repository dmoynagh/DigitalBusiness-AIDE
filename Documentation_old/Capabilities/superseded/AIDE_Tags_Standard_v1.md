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
