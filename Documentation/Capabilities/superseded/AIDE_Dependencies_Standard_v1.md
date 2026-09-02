# AIDE Dependencies — Standard

> **Identity:** `AIDE_Dependencies@v1`
> **Common name:** Dependencies
> **Version 1** (2026-08-28). First published dependency declaration, resolution, builder, and
> conformance-tracking contract.

---

## Purpose

Declare what an artefact relies on for correct schema, design, content, interpretation,
conformance, maintenance, or execution; resolve those identities; report availability/version
state; and preserve the last proven conformance checkpoint.

## Dependency storage

For governed Markdown documents:

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

The governing document methodology supplies the footer metadata container. This Standard owns the
`Dependencies:` content contract.

## Declaration grammar

```text
dependency              relationship
dependency@vN           conformed at vN
!dependency             required; check on relevant use and raise loudly if missing
!!dependency            best-effort session-start check; also required on later use
dependency@!vN          exact available version vN required
```

Markers compose, for example `!!abc@!v8`.

## Identity resolution

Resolve by identity name **without using the version as part of identity equality**.

An artefact may expose:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first identity is primary. Any listed identity may resolve a dependency. If multiple
artefacts match the same identity, fail visibly rather than guessing.

After identity resolution, compare versions where the dependency declared one.

## Version meaning

`abc@v8` means the dependent artefact was last successfully conformed against `abc` v8.

If `abc@v12` is available, identity/presence resolves and the query reports a newer available
version plus the `v8 → v12` gap. The dependency is not treated as missing.

`abc@!v8` requires the resolved identity to expose exactly v8.

A dependency version advances only after all applicable migration/update/conformance work through
the recorded target has succeeded. A newer installed version alone never advances the footer.

## Dependency Query

For each dependency, return at least:

- resolved / not resolved;
- requirement level;
- declared conformance version where present;
- available version where present;
- version relation: same / newer / older / unknown / not-applicable;
- version gap where relevant;
- exact-version requirement result.

Dependencies reports state. Migration or the current operation decides what a version gap or
missing dependency requires beyond the mandatory loud reporting of `!` / `!!`.

## Required presence

`!dependency` must be checked when the artefact is accessed or used for a relevant operation. A
missing identity is raised prominently.

`!!dependency` should additionally be checked at session start wherever the platform permits.
This is best effort on chat platforms. If startup discovery fails, normal `!` behaviour remains
the fallback on first relevant use.

## Dependency Builder

A Standard may contribute an `AIDE_DependencyBuilder` YAML block defining:

- `Id`;
- `Owner`;
- `AppliesWhen`;
- `Source`;
- `Generate`;
- `OutputOwnership` as an owned `Group` or suitable identity `Prefix`.

Builders are discovered from the Standards available in the execution context. Each builder
maintains only the dependencies it owns, removes its stale output, and leaves manual/other-builder
declarations untouched.

Groups are ownership structure only. All non-owning consumers ignore group keys and see their
contents as normal dependency entries.

Builders must be idempotent and fail visibly when applicable output cannot be derived correctly.

## Bootstrap

This Standard may contribute a `{bootstrap}` instruction for `!!` checks. The marker and the rule
to discover/process bootstrap instructions are defined by the AIDE system bootstrap layer, not by
Dependencies.

---

**Depends on:** `Capabilities_Dependencies_Design` v1, `Core_System_Design` v3.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
