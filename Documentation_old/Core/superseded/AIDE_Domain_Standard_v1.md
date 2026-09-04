# AIDE Domain — Standard

> **Identity:** `AIDE_Domain@v1`
> **Common name:** Domain
> **Version 1** (2026-08-31). First canonical Domain contract produced from the blank-sheet
> `Core_Domain_Design_v1`.
>
> **Default weight:** Requirement

## Purpose

Provide one consistent AIDE contract for identifying the named operating/governance context
relevant to a target, hosting independently owned Domain-context settings, and explicitly
clarifying/composing Domain roots when natural recognised structure is insufficient.

A Domain is contextual and semantic; it is not inherently a file and is not an AIDE activation
switch.

## Applicability

Apply when an operation needs Domain context for a target, focus, setting lookup, navigation,
composition or another Domain-aware behaviour.

```yaml
Scope:
  Context: >
    Apply when the current operation needs to resolve, declare, name, navigate or consume Domain
    context or Domain-hosted settings for a target/focus.
```

Do not resolve Domain merely because an artefact exists. One session may work across several
Domains or with material that has no Domain.

## Domain model

A **Domain is a named AIDE operating/governance context**.

A Domain may be:

```text
implicit  — established from recognised authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify recognised roots
```

The initial recognised Domain-capable structure types are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

Domain owns only the recognition and structural relationships needed for Domain resolution. The
recognised structure's owner retains its native semantics and membership rules.

A repository/worktree is a discovery boundary in v1, not an implicit Domain type.

## Natural containment

Authoritative structural containment prevents a contained recognised structure from establishing a
second implicit Domain.

- a project that is a member of a solution remains in the solution Domain;
- a delegated/child Index remains in its enclosing root Index Domain; and
- another recognised structure inside an effective Domain does not create a child Domain merely
  because it could act as a root when isolated.

Structural children never create child Domains implicitly. Child-Domain inheritance, settings
propagation, nesting, precedence and parent/child composition are undefined in v1. If a distinct
child Domain is required, use an explicit declaration and require the result to be unambiguous.

## Co-root recognised structures

Evaluate recognised structures sharing a physical root by authoritative identity and structural
relationships, not proximity alone.

### Matching identity

Co-root structures with matching authoritative identities form one implicit Domain.

```text
Foo.sln + Foo_Index  → Foo Domain
```

An available declared Index project/topic identity is authoritative over filename-only matching.
When a matching Index and solution/project represent one Domain, the Index is the preferred
AIDE-controlled Domain metadata/settings host. The native solution/project retains authority over
its own membership and semantics.

### Different identity

Co-root recognised structures with different identities remain separate implicit Domains by
default.

```text
Foo.sln + Womble_Index  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj → Foo Domain + Bar Domain
```

Multiple standalone projects in one folder with no enclosing solution are therefore separate
Domains. If this natural interpretation is not intended, use `AIDE_Domain.yaml` rather than adding
special-case inference.

## Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a solution remains authoritative for solution/project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native solution/project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## Domain identity and references

An implicit Domain takes its current name/identity from the authoritative recognised structure
that establishes it. Use authoritative declared/native identity when available; filename matching
is only a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names for navigation, cross-Domain
references, composition, provenance or other cases where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally
wrong—for example to compose several solutions/projects/Indexes, combine differently named roots,
or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Type: Solution
        Path: Product.sln
      - Type: Index
        Path: Product_Index_v1.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Declaration fields

- `Schema` — required declaration-container schema identity; v1 value is `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of recognised roots explicitly composed/clarified by the
  entry.
- `Type` — one of `Index`, `Solution`, or `Project` for each explicit root in v1.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

The explicit Domain declaration itself is Domain-capable, but its `Roots` identify the recognised
structures whose natural interpretation it composes or clarifies. Co-location of two Domain entries
inside one file creates no relationship between them.

A valid explicit declaration may override the natural implicit grouping of its listed roots. It
does not recreate or replace their internal registries or native membership rules.

## Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

Preferred authoritative hosts are:

```text
Index-backed implicit Domain
→ root Index local configuration may host Domain metadata/settings

matching solution/project + Index
→ Index is the preferred AIDE Domain metadata/settings host

explicit Domain
→ the Domain entry in AIDE_Domain.yaml hosts Domain metadata/settings
```

Where a root Index hosts Domain metadata/settings, expose one Domain configuration mapping in the
Index's local configuration using the shared field meanings:

```yaml
Domain:
  Aliases: [PreviousName]
  Settings:
    SomeSetting: <owner-defined value>
  Branches:
    - Branch: docs/api
      Settings:
        SomeSetting: <owner-defined value>
```

`Aliases`, `Settings` and `Branches` are optional. The Domain name is inherited from the Index's
authoritative project/topic identity and `Roots` are not repeated. Documentation Methodology owns
the Index's document/configuration rendering; Domain owns the meaning of this Domain configuration
payload.

For a solution/project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit `AIDE_Domain.yaml` representation rather than modifying the native format solely to carry
AIDE configuration.

## Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. A nearby project, solution or Index is provisional until applicable enclosing evidence has
been checked.

Do **not** use “nearest marker wins”. Physical ancestry is a discovery path, not proof of
composition.

### Discovery boundaries

Stop upward discovery at the nearest meaningful operational boundary available to the current
context, such as:

- an explicitly supplied discovery boundary;
- workspace/container root;
- repository/worktree root;
- user Documents root;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- another recognised user/application storage root; or
- filesystem/mount root as fallback.

A discovery boundary limits search only. A valid explicit Domain declaration may reference roots
beyond that boundary where the environment can resolve those references.

## Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing recognised Domain evidence within that boundary, including
   applicable `AIDE_Domain.yaml` declarations and authoritative containment/membership relations.
3. Resolve explicit Domain claims applicable to the target. A valid unambiguous explicit claim
   supplies the effective Domain and may clarify/override the natural grouping of its declared
   roots.
4. Otherwise apply authoritative containment: a contained project/Index/recognised structure
   inherits the enclosing effective Domain rather than creating another implicit Domain.
5. Evaluate co-root independent recognised roots: matching authoritative identities converge;
   different identities remain separate.
6. If the target belongs unambiguously to one remaining independent recognised root, return that
   implicit Domain.
7. If no Domain-capable structure applies, return `No Domain context`.
8. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
   return an unresolved/error result rather than merging, ranking or guessing.

## Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership without clearly
  expressing the intended override;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## Ownership boundaries

- **Core/Domain** owns this common context/resolution/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Documentation Methodology** owns Index/register/document corpus behaviour and document/config
  rendering.
- **Project/solution systems** own native membership and project/build-system semantics.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## Deliberately absent from v1

The following are not defined by this Standard:

- implicit or generic child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository-as-Domain merely because a repository exists;
- a generic settings precedence/inheritance engine;
- a Domain-specific Tool;
- broad exclusion syntax to counteract normal defaults; or
- platform-specific parser machinery beyond what is required to observe the recognised structures.

If a demonstrated use case later requires one of these mechanisms, change Domain Design first and
produce a later Standard release through the normal capability-production path.

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
Dependencies: !AIDE_DocumentationMethodology@v18, AIDE_Scope@v1, AIDE_Migration@v1, Core_Domain_Design_v1
References: Core_System_Design_v5
