# AIDE Domain — Standard

> **Identity:** `AIDE_Domain@v3`
> **Common name:** Domain
> **Version 3** (2026-09-01). Completes the Domain recognition contract with an explicit
> Domain-owned approved recognition set, native Solution/Project minimum recognition, no generic
> Index root or separate Domain recognition registry, and complete Propagation Stop, explicit-root
> assertion and settings-host rules.
>
> **Default weight:** Requirement

## Purpose

Provide one consistent AIDE contract for identifying the named operating/governance context
relevant to a target, hosting independently owned Domain-context settings, and explicitly
clarifying/composing Domain roots when natural approved structure is insufficient.

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
implicit  — established from Domain-approved recognition and authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify approved recognised roots
```

Generic Item/Item Type semantics belong to `AIDE_Index@v2`. An Item Type owner defines the type's
identity, `Identify` and `Provides` semantics. **Only Core/Domain decides whether a recognised
semantic Item Type identity may establish or participate in Domain resolution.**

External Item Type owners cannot self-elevate to Domain capability. No Item Type owner, generic
Index, or registry entry can self-grant Domain authority.

## Approved Domain recognition set

The approved recognition set is authoritative Domain contract state and is versioned with this
Standard. Do not derive Domain eligibility from a type-owner flag or create a separate approval
register solely for this purpose.

The following table is the authoritative v3 approved recognition set:

| Recognition | Kind | Recognition owner | Domain authority owner |
|---|---|---|---|
| `DocumentationTopic` | semantic Item Type | Documentation Methodology | Core/Domain |
| `Solution` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `Project` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `AIDE_Domain` declaration entry | explicit Domain declaration | Core/Domain | Core/Domain |

A generic `Index` is **not** approved Domain recognition.

### `DocumentationTopic`

`DocumentationTopic` is the Documentation Methodology-owned semantic Item Type for one logical
**top-level documentation topic boundary**. Its governing Index document declares/describes that
logical boundary and supplies the recognition evidence; the Index file itself is not the semantic
boundary merely because it hosts the declaration.

Subtopics do not become independent `DocumentationTopic` Items merely because they have their own
Design/Decisions/Index state.

A documentation Index may therefore be the representation used to recognise a
`DocumentationTopic`, but generic Index existence never establishes a Domain.

### Native `Solution` recognition

For Domain purposes, recognise a Solution only from the minimum current native/platform evidence
needed to establish:

- the native Solution identity/signature; and
- authoritative project membership where membership affects Domain containment.

The native platform remains authoritative for Solution format, membership and internals. This
Standard does not define an AIDE Solution Item Type.

### Native `Project` recognition

For Domain purposes, recognise a Project only from the minimum current native/platform evidence
needed to establish:

- the native Project identity/signature; and
- authoritative membership in an enclosing recognised Solution where that relationship exists.

A Project that is a member of a Solution remains within that Solution's effective Domain under
normal propagation. A standalone recognised Project may establish an implicit Domain where no
stronger enclosing Domain applies.

The native platform remains authoritative for Project format, membership and internals. This
Standard does not define an AIDE Project Item Type.

### Explicit Domain declaration recognition

A valid Domain entry in `AIDE_Domain.yaml` is Domain-owned approved recognition. It may compose or
clarify approved roots but does not grant arbitrary nearby structures Domain capability.

A repository/worktree remains a discovery boundary, not an implicit Domain recognition.

## Natural containment

Under ordinary authoritative containment, a contained approved structure does not create a second
implicit Domain.

- a Project that is an authoritative member of a Solution remains in the Solution Domain; and
- a subordinate recognised documentation structure remains in its enclosing effective Domain while
  propagation continues.

The current rule is:

> Under ordinary authoritative containment, structural children do not create a second implicit
> Domain. A deliberate `Propagation: Stop` terminates that containment propagation; independent
> resolution below the stop may establish another Domain, but it is not modelled as a child Domain.

## Domain propagation stop

Use:

```yaml
Domain:
  Propagation: Stop
```

only on a recognised/registered Domain-aware structural boundary for which the Domain-owned
property can be resolved reliably.

Canonical meaning:

> The enclosing effective Domain does not propagate through the marked structural boundary.
> Resolution below the boundary continues independently as though that enclosing Domain were absent.
> Independent resolution may therefore yield `No Domain`, an unresolved/error result, or another
> Domain. If another Domain is found below the stop, this Standard defines no parent/child semantic
> relationship, inheritance, merge, settings propagation or precedence between the two.

Where an Index Item represents the significant crossed boundary, a parent Index registration may
host the Domain-owned Stop property. That registration does not transfer authority over the
boundary's internals.

v3 does not define a generic filesystem Stop marker or arbitrary unregistered-folder exclusion.

### Stop traversal

While walking upward from the target:

1. identify every crossed recognised structural boundary;
2. inspect applicable Domain-owned boundary configuration, including a parent Index registration
   where that registration is the authoritative host; and
3. if Stop applies, discard the enclosing Domain for content below the boundary and continue
   independent resolution.

Stop terminates propagation; it does not itself create a Domain.

## Co-root recognised structures

Evaluate approved recognised structures sharing a physical root by authoritative identity and
structural relationships, not proximity alone.

### Matching identity

Approved co-root structures with matching authoritative identities form one implicit Domain where
no stronger rule changes the result.

```text
Foo.sln + DocumentationTopic(Foo)  → one Foo Domain
```

### Different identity

Approved co-root structures with different identities remain separate implicit Domains by default.

```text
Foo.sln + DocumentationTopic(Womble)  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj               → Foo Domain + Bar Domain
```

A bare generic Index beside `Foo.sln` does not establish a separate Womble Domain. If the natural
interpretation is not intended, use `AIDE_Domain.yaml` rather than adding special-case inference.

## Domain membership boundary

Domain answers:

> What AIDE operating context does this target belong to?

It does not replace constituent membership systems.

- a native Solution remains authoritative for Solution/Project membership;
- an Index/Documentation Methodology remains authoritative for governed document registration and
  corpus mechanics; and
- Domain supplies the wider AIDE operating context.

An AIDE-governed artefact structurally contained within one unambiguous effective Domain may
resolve to that Domain even when it is not a native Solution/Project member. Where several Domains
share a physical container, location alone is insufficient to assign an otherwise ambiguous
artefact.

## Domain identity and references

An implicit Domain takes its current name/identity from the authoritative approved recognition that
establishes it. Use authoritative declared/native identity when available; filename matching is only
a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally
wrong—for example to compose several Solutions/Projects/DocumentationTopics, combine differently
named roots, or deliberately separate roots that would otherwise converge.

One physical location has at most one `AIDE_Domain.yaml` declaration container. The file may hold
multiple independent Domain entries:

```yaml
Schema: AIDE_Domain/v1
Domains:
  - Name: Product
    Aliases: [ProductOld]
    Roots:
      - Recognition: Solution
        Path: Product.sln
      - Recognition: DocumentationTopic
        Path: docs/Product_Index_vN.md
    Settings:
      SomeSetting: <owner-defined value>
    Branches:
      - Branch: docs/api
        Settings:
          SomeSetting: <owner-defined value>
```

### Declaration fields

- `Schema` — required declaration-container schema identity; current value is `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of approved recognised roots explicitly composed/clarified
  by the entry.
- `Recognition` — expected approved Domain recognition for the root. It is an assertion, not an
  authority grant.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

### Root-recognition validation

For each explicit root:

1. independently recognise the target through current authoritative semantic Item Type recognition
   or the applicable Domain-owned native recogniser;
2. compare the observed recognition with the declared expected `Recognition`;
3. fail visibly on mismatch; and
4. fail visibly on unknown/unapproved recognition.

The token itself never creates Domain capability. `Index` is not a valid value merely because the
path identifies an Index document.

If an existing representation retains the field name `Type`, it has exactly these assertion
semantics.

The explicit Domain declaration itself is approved Domain recognition. Co-location of two Domain
entries in one file creates no relationship between them. A valid explicit declaration may change
the natural grouping of its listed roots but does not replace their internal registries or native
membership rules.

## Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

### Authoritative settings host

Where an explicit `AIDE_Domain.yaml` entry governs/composes the effective Domain:

- that Domain entry is the **sole authoritative Domain metadata/settings host** for that Domain;
- an Index-hosted `Domain:` configuration for the same effective Domain is not merged; and
- duplicate/conflicting Domain host state is an error requiring reconciliation.

Index-hosted Domain configuration remains valid for an applicable **implicit** Domain where no
explicit Domain entry governs it.

For a Solution/Project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit Domain representation rather than modifying the native format solely to carry AIDE
configuration.

## Runtime recognition

No separately named Domain recognition registry is part of the current architecture.

Domain resolution may use:

- direct current semantic Item Type recognition;
- the optional generic Domain-neutral `ItemTypeRegistry` from `AIDE_Index@v2`;
- Domain-owned native Solution/Project recognisers;
- explicit Domain declaration parsing; and
- safe runtime caches.

For a semantic Item Type, recognition produces its identity/provisions only. Domain must compare
that recognised identity against the current approved recognition set before treating it as
Domain-eligible.

No semantic Item Type definition or `ItemTypeRegistry` entry may elevate itself to Domain authority.
Compiled/cached state is derived optimisation only. If its current authoritative provenance cannot
be established, refresh/directly evaluate or fail visibly rather than granting Domain authority.

## Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. Do **not** use “nearest marker wins”. Physical ancestry is a discovery path, not proof of
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
2. Collect local and enclosing Domain evidence through approved semantic/native/explicit
   recognition and authoritative containment/membership relationships.
3. While walking upward, inspect every crossed recognised structural boundary for applicable
   Domain-owned `Propagation: Stop`. Where Stop applies, exclude enclosing Domain evidence above the
   boundary from content below it and continue independent resolution.
4. Resolve applicable explicit Domain claims and validate every root's expected `Recognition`
   against independently observed approved recognition. A valid unambiguous explicit claim supplies
   the effective Domain for its governed/composed roots.
5. Otherwise apply authoritative containment: a contained approved structure participates in the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate remaining independent approved co-roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining approved root, return that implicit Domain.
8. If no approved recognition applies, return `No Domain context`.
9. If authoritative claims are contradictory or assignment remains ambiguous, return an
   unresolved/error result rather than merging, ranking or guessing.

## Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- an explicit root's expected recognition mismatches observed recognition;
- an explicit root uses unknown/unapproved recognition;
- two explicit Domains claim the same effective target without defined resolution;
- an explicit Domain entry and Index expose duplicate/conflicting Domain host state for the same
  effective Domain;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## Ownership boundaries

- **Core/Domain** owns the approved-recognition, context/resolution and Domain settings-host
  contract.
- **Core/Index** owns generic Index/Item/Item Type behaviour and the optional Domain-neutral
  `ItemTypeRegistry`.
- **Documentation Methodology** owns documentation-specific Index extensions and
  `DocumentationTopic` semantics.
- **Native Solution/Project systems** own their identities, memberships and internals; Domain
  observes only the minimum facts required for resolution.
- **Setting owners** own all setting semantics, including precedence and inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not duplicate them.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour.

## Deliberately absent from v3

This Standard does not define:

- generic Index as a Domain recognition;
- owner-self-declared Domain-capable Item Type flags;
- a separate Domain Recognition Registry;
- invented AIDE Solution/Project Item Types solely for Domain;
- implicit/generic child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository-as-Domain merely because a repository exists;
- a generic settings precedence/inheritance engine;
- a generic filesystem Propagation Stop marker or arbitrary unregistered-folder exclusion;
- a Domain-specific Tool; or
- broad platform-specific parser machinery beyond minimum recognition observations.

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
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v2, AIDE_Scope@v1, AIDE_Migration@v1, Core_Domain_Design_v3
References: Core_System_Design_v8, Core_Index_Design_v2
