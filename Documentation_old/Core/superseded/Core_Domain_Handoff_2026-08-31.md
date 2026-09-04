# Core Domain — Handoff Brief

> Prepared 2026-08-31 for transfer from the AIDE Capabilities project conversation into the Core
> project.

## Purpose of the handoff

Domain design was completed in the Capabilities project because that is where the investigation
started, but the resulting architecture clearly places Domain under **Core**.

The attached/current handoff documents are:

- `Core_Domain_Design_v1.md`
- `Core_Domain_Decisions_v1.md`

Treat those as the confirmed current Domain design input.

The earlier `AIDE_Domain_*` corpus from 2026-08-27/28 was never implemented. It has no standing and
creates no compatibility or migration requirement. Do not reconcile the new design back toward the
old model merely to preserve it.

## Confirmed model

Domain is a named AIDE operating/governance context. It is contextual rather than artefact-owned.

A Domain may be:

- **implicit** — supplied by a recognised Index, solution or standalone project; or
- **explicit** — declared in `AIDE_Domain.yaml` where natural structural rules are incomplete,
  ambiguous or intentionally different.

The initial recognised Domain-capable structures are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

Domain owns only the minimum recognition/containment knowledge required to resolve these
consistently across AIDE surfaces.

### Natural hierarchy

- solution member projects remain in the solution Domain;
- child/delegated Indexes remain in the root Index Domain;
- structural children do not create child Domains;
- child-Domain semantics are deliberately not designed.

### Co-root defaults

- matching authoritative identities → one implicit Domain;
- different identities → separate implicit Domains;
- multiple standalone projects with no solution → separate Domains.

Example:

```text
Foo.sln + Foo_Index    → Foo Domain
Foo.sln + Womble_Index → Foo Domain + Womble Domain
```

When Index + solution/project represent the same Domain, the Index is the preferred AIDE Domain
metadata/settings host but does not own native project/solution semantics.

If the default structural interpretation is wrong, use `AIDE_Domain.yaml`.

### Explicit Domain file

One physical `AIDE_Domain.yaml` may contain multiple independent Domain entries:

```yaml
Domains:
  - ...
  - ...
```

Same-file placement creates no relationship between those Domains.

Explicit Domain declarations compose/clarify recognised roots rather than enumerate their internal
files.

### Domain settings

Domain defines only the settings host/location/format/coexistence convention.

Setting owners define the settings themselves, including schema, values, defaults, validation,
precedence and inheritance.

Settings can be attached to the whole Domain or a structural `Branch`:

```yaml
Branch: docs/api
Settings:
  SomeSetting1:
    ...
  SomeSetting2:
    ...
```

`Scope` is deliberately not used because `AIDE_Scope` already owns applicability semantics.

### Documents and Domain identity

Ordinary documents/files do not normally carry a Domain declaration or Domain name.

Resolve Domain only when an operation needs Domain context.

Use relative references such as "the Domain" where the actual identity is not semantically
important.

Renames/previous names/aliases belong in authoritative Domain metadata for navigation and reference
resolution rather than requiring member-document rewrites.

### Discovery

Domain resolution is target-based and searches local + enclosing structure upward.

Do not stop at the nearest marker. A local project/solution/Index is only a candidate implicit root
until enclosing authoritative context has been checked.

Upward discovery stops at an appropriate operational boundary such as:

- explicit supplied boundary;
- workspace/container root;
- repository/worktree root;
- Documents/Desktop;
- AppData/application-data root or equivalent;
- filesystem/mount root fallback.

Repository root is currently a discovery boundary, not automatically a Domain type.

### Important boundary

Domain membership and constituent registry membership are distinct.

A solution owns solution/project membership.
An Index/Documentation Methodology owns governed document registration/corpus mechanics.
Domain supplies the wider AIDE operating context.

AIDE-governed artefacts inside an unambiguous Domain may resolve to that Domain without Domain
taking over native or Index membership semantics.

### No Domain

No Domain context is valid. Domain is not an AIDE activation switch.

## Core work requested

In the Core project:

1. Read the current Core Binder / `Core_System_Design` and these two Domain documents.
2. Confirm Domain as a Core subtopic/system foundation.
3. Register `Core_Domain_Design_v1` and `Core_Domain_Decisions_v1` in the Core Index.
4. Update `Core_System_Design` and `Core_System_Decisions` only as needed to record the ownership and
   system relationship; do not duplicate the detailed Domain model there.
5. Preserve the current rule that development/product Domains consume AIDE and remain outside the
   AIDE system tree.
6. Treat `Core_Domain_Design_v1` as the source for a canonical `AIDE_Domain@v1` Standard.
7. Use the normal Build Capability/Standards Production path to produce that Standard when the Core
   corpus is reconciled.
8. Do not create a Domain Tool unless a real repeatable action demonstrates the need.
9. Do not design child-Domain inheritance, generic settings precedence, repository-as-Domain, or
   other deferred mechanisms without a demonstrated use case.
10. Regenerate/update the Core Binder after the Core master documents are issued.

## Design discipline

Use the confirmed Domain Design as current authoritative intent. If integration with current Core
reveals a genuine contradiction, surface the exact architecture decision rather than silently
changing Domain behaviour.

Prefer the smallest Core changes needed to establish ownership and publish the Domain Standard.
