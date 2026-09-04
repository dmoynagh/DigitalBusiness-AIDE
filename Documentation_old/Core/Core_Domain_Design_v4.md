# Core Domain — Design

> **Version 4** (2026-09-01). Applies the final Review A Round 2 determinism corrections: makes
> Propagation Stop inclusive of the marked boundary and all content within/below it, and requires
> one unambiguous eligible authoritative settings host for an implicit Domain when settings are needed.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## §1 — Purpose and ownership

Domain defines the common AIDE concept used to identify the named operating/governance context
within which work is being performed.

A **Domain is a named AIDE operating/governance context**. It is contextual and semantic; it is not
inherently a file and is not an AIDE activation switch.

Core/Domain owns:

- the meaning and identity of Domain;
- the explicit, versioned approved recognition set used for Domain resolution;
- the minimum native Solution/Project recognition and containment/membership observations needed by
  Domain;
- implicit versus explicit Domain formation;
- target-based discovery, resolution and deterministic ambiguity/failure behaviour;
- Domain metadata/settings-host and `Branch` conventions;
- Domain propagation-stop semantics; and
- Domain eligibility decisions applied after semantic Item Type recognition.

Domain does **not** own the full semantics of an approved semantic Item Type or native platform
structure. Generic Index/Item/Item Type semantics belong to Core/Index; an Item Type owner remains
authoritative for its own `Identify` and `Provides` contract. Native platforms remain authoritative
for solution/project identity, membership and internal semantics.

Domain alone decides whether recognised evidence may establish or participate in Domain resolution.

This Design produces:

```text
AIDE_Domain@v4
```

## §2 — Level 1 model and authority seam

```text
target / focus
    ↓
recognise available approved evidence
    ├── semantic Item Type identity
    ├── Domain-owned minimum native recognition
    └── explicit AIDE_Domain declaration
    ↓
Domain-owned approved recognition test
    ↓
explicit declaration / containment / co-root / propagation evaluation
    ↓
effective Domain | No Domain | unresolved/error
```

Recognition and Domain authority are distinct:

```text
Item Type owner
  → identity + Identify + Provides

optional ItemTypeRegistry
  → Domain-neutral recognition/provision optimisation

Core/Domain
  → approved Domain recognition set
  → minimum native Solution/Project recognition
  → Domain resolution authority
```

An external Item Type owner cannot add a field to its type definition or a compiled registry and
thereby become a Domain root.

## §3 — Applicability

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

## §4 — Approved Domain recognition set

The approved recognition set is part of the Domain contract itself. It is explicit and versioned
with `AIDE_Domain`; it is not a second standalone registry.

The v4 set is:

| Recognition | Kind | Recognition owner | Domain authority owner |
|---|---|---|---|
| `DocumentationTopic` | semantic Item Type | Documentation Methodology | Core/Domain |
| `Solution` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `Project` | native structural recognition | Core/Domain observes minimum native signature/authoritative membership relationship; native platform remains semantic authority | Core/Domain |
| `AIDE_Domain` declaration entry | explicit Domain declaration | Core/Domain | Core/Domain |

A generic `Index` is **not** in the approved set.

### `DocumentationTopic`

`DocumentationTopic` is a Documentation Methodology-owned semantic Item Type representing one
logical top-level-topic documentation boundary. Its governing Index document declares/describes
that logical boundary and supplies the authoritative recognition evidence; the Markdown file is not
itself the semantic boundary merely because the declaration appears there.

Subtopics do not become independent `DocumentationTopic` Items merely because they have their own
Design/Decisions/Index state.

Domain may consume a recognised `DocumentationTopic` identity but only this Domain-owned approval
makes that semantic type Domain-eligible.

### Native `Solution`

Domain owns only the minimum observation needed to recognise a native Solution for Domain purposes:

- a current native/platform-recognised Solution identity/signature; and
- the authoritative project-membership relationship exposed by that native structure when
  membership matters to Domain resolution.

The native platform remains authoritative for solution format, identity details, membership and all
other solution semantics. Domain does not invent an AIDE Solution Item Type merely to use the
native structure.

### Native `Project`

Domain owns only the minimum observation needed to recognise a native Project for Domain purposes:

- a current native/platform-recognised Project identity/signature; and
- its authoritative membership relationship to a recognised enclosing Solution where such a
  relationship exists.

A Project that is an authoritative member of a Solution participates through that containment; a
standalone recognised Project may establish an implicit Domain when no stronger enclosing Domain
relationship applies.

The native platform remains authoritative for project format, internals and membership semantics.

### Explicit `AIDE_Domain` declaration

A valid Domain entry in `AIDE_Domain.yaml` is a Domain-owned explicit recognition. It composes or
clarifies recognised roots. The file/container is not itself evidence that every nearby item is in
the declared Domain; normal applicability and root validation still apply.

## §5 — Domain model

A Domain may be:

```text
implicit  — established from approved recognition and authoritative structural relationships
explicit  — declared in AIDE_Domain.yaml to compose or clarify approved recognised roots
```

A repository/worktree remains a discovery boundary, not an implicit Domain recognition.

An Index may host or declare information used by another approved recognition. In particular, a
documentation Index may declare a `DocumentationTopic`, or may host Domain-owned configuration for
an implicit Domain established by approved evidence. **Index existence alone never establishes
Domain context.**

## §6 — Natural containment and Propagation Stop

Under ordinary authoritative containment, a contained recognised structure remains in the
enclosing effective Domain rather than creating a second implicit Domain.

Examples:

- a Project that is an authoritative member of a Solution remains in the Solution Domain; and
- a subordinate documentation structure remains in the enclosing Domain unless propagation is
  deliberately stopped.

The current rule is:

> Under ordinary authoritative containment, structural children do not create a second implicit
> Domain. A deliberate `Propagation: Stop` removes the enclosing effective Domain from the marked
> boundary itself and all content within/below it. The marked boundary and its contained region
> then resolve independently, but any Domain found there is not modelled as a child Domain.

### Propagation Stop meaning

Canonical meaning:

> `Propagation: Stop` removes the enclosing effective Domain from the marked structural boundary
> itself and all content within/below it. The marked boundary and its contained region then resolve
> independently as though that enclosing Domain were absent. Independent resolution may therefore
> yield `No Domain context`, an unresolved/error result, or another Domain. If another Domain is
> found in the stopped region, the current model defines no parent/child semantic relationship,
> inheritance, merge, settings propagation or precedence between the two.

### Supported Stop representation in v4

v4 supports Stop only on a **recognised/registered Domain-aware structural boundary**.

Where represented by an Index Item, the parent Index may register the significant boundary for the
purpose of locating/describing it and hosting the Domain-owned property:

```yaml
Domain:
  Propagation: Stop
```

That registration does not transfer authority over the boundary's internals to the parent Index.

v4 does not add a generic filesystem marker file or arbitrary unregistered-folder exclusion.

### Stop traversal

When resolving upward from a target:

1. identify each crossed recognised structural boundary;
2. inspect the applicable Domain-owned boundary configuration, including a parent Index
   registration where that registration is the authoritative host for the Stop property; and
3. when Stop applies to a crossed boundary, discard the enclosing Domain for the marked boundary
   itself and all content within/below it, then continue independent Domain resolution for that
   stopped region.

Where a parent Index hosts the Stop property on a boundary registration, the parent Index is the
property host only. The registered boundary is the stopped boundary; the parent Index does not
become part of the stopped region merely by hosting the property.

A Stop is therefore a propagation rule/contextual reset, not a Domain-creation token.

## §7 — Co-root recognised structures

Evaluate approved recognised structures sharing a physical root by authoritative identity and
structural relationships, not proximity alone.

### Matching identity

Approved co-root structures with matching authoritative identities form one implicit Domain where
no stronger explicit/containment rule changes the result.

```text
Foo.sln + DocumentationTopic(Foo)  → one Foo Domain
```

The documentation boundary is recognised as `DocumentationTopic`; a bare generic Index does not
supply a second Domain root.

### Different identity

Approved co-root structures with different identities remain separate implicit Domains by default.

```text
Foo.sln + DocumentationTopic(Womble)  → Foo Domain + Womble Domain
Foo.csproj + Bar.csproj               → Foo Domain + Bar Domain
```

If the natural interpretation is not intended, use `AIDE_Domain.yaml` rather than adding
special-case inference.

## §8 — Domain membership boundary

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

## §9 — Domain identity and references

An implicit Domain takes its current name/identity from the authoritative approved recognition that
establishes it. Use authoritative declared/native identity when available; filename matching is only
a discovery hint.

Ordinary member artefacts do not normally store Domain identity. Resolve Domain only when an
operation needs it.

Where the specific name is not semantically significant, refer to **the Domain**, meaning the
effective Domain for the current target. Use explicit names for navigation, cross-Domain references,
composition, provenance or other cases where identity itself matters.

Domain metadata may record aliases, including previous names, for navigation and reference
continuity. Renaming a Domain does not itself require member-document rewrites.

## §10 — Explicit Domain declaration

Use `AIDE_Domain.yaml` when natural implicit rules are incomplete, ambiguous or intentionally wrong—for
example to compose several Solutions/Projects/DocumentationTopics, combine differently named roots,
or deliberately separate roots that would otherwise converge.

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

### Root recognition is an assertion

`Recognition` means **expected approved Domain recognition**.

It never grants Domain capability. For every root:

1. the resolver independently recognises the target using the current authoritative semantic Item
   Type definition or Domain-owned native recognition mechanism;
2. the observed recognition must match the declared expected `Recognition`;
3. mismatch fails visibly; and
4. an unknown/unapproved recognition fails visibly.

`Index` is not a valid root-recognition value merely because the path points at an Index document.
A documentation-backed root uses `DocumentationTopic` when that logical top-level-topic boundary is
actually recognised.

If a representation retains the older field name `Type`, it has exactly these expected-recognition
assertion semantics; it is not an authority token.

### Declaration fields

- `Schema` — required declaration-container schema identity; current value remains
  `AIDE_Domain/v1`.
- `Domains` — required non-empty sequence of independent Domain entries.
- `Name` — required authoritative current Domain name/identity for an explicit entry.
- `Aliases` — optional unique alternate/previous lookup names for that Domain.
- `Roots` — required non-empty sequence of approved recognised roots explicitly composed/clarified
  by the entry.
- `Recognition` — expected approved Domain recognition for the root; validated against observed
  recognition and never self-authorising.
- `Path` — locator of that recognised root. Relative paths resolve from the directory containing
  `AIDE_Domain.yaml`; other locator forms are valid only where the current environment can resolve
  them unambiguously.
- `Settings` — optional Domain-root setting-owner payloads.
- `Branches` — optional sequence of structural setting attachments.
- `Branch` — required Domain-relative structural path for one branch attachment.

Co-location of two Domain entries inside one file creates no relationship between them. A valid
explicit declaration may override the natural implicit grouping of its listed roots, but it does
not recreate or replace their internal registries or native membership rules.

## §11 — Branch and settings convention

Domain defines only the settings host, format and structural attachment convention. Each setting
owner defines its setting names/schema, meaning, values, defaults, validation, consumption,
precedence, inheritance and combination behaviour.

A Domain-root declaration uses `Settings` without a Branch. A structural attachment is represented
under `Branches` with one Domain-relative `Branch` and its `Settings` mapping.

Canonical Branch serialization uses `/` as the structural separator, has no leading `/`, and must
not escape the Domain through `..`. Absence of Branch means Domain-root attachment. Domain assigns
no generic precedence between root and Branch settings or between different Branches.

### Authoritative Domain settings host

If an explicit `AIDE_Domain.yaml` Domain entry governs/composes the effective Domain, **that Domain
entry is the sole authoritative Domain metadata/settings host for that Domain**.

An Index-hosted `Domain:` configuration for the same effective Domain is not merged with the
explicit entry. Duplicate/conflicting host state is an error requiring reconciliation.

For an applicable implicit Domain where no explicit Domain entry governs it, Index-hosted
Domain-owned configuration is valid only under this **unique-host eligibility** rule:

1. an Index is eligible only when it is the governing Index of an approved semantic recognised root
   that establishes or participates in that implicit Domain;
2. mere parent/repository registration or location of a recognised root does not make that parent
   Index a Domain settings host;
3. where Domain metadata/settings are needed, the eligible governing Indexes must yield exactly one
   unambiguous authoritative host for the implicit Domain; and
4. if no unique eligible Index host exists, use an explicit `AIDE_Domain.yaml` representation for
   the Domain metadata/settings rather than inventing precedence.

Under the current approved recognition set, the ordinary implicit documentation case is the
governing Index of the `DocumentationTopic`. A matching co-root Domain comprising a Solution plus
one `DocumentationTopic` may therefore have that one governing documentation Index as its clear
host. A native Solution/Project-only implicit Domain does not acquire an arbitrary Index host merely
because an Index registers it; use an explicit Domain representation when AIDE Domain
metadata/settings are required.

If multiple eligible Indexes expose or claim Domain-owned configuration for the same implicit
Domain, fail visibly and reconcile or introduce an explicit Domain. Do not merge, rank, choose by
discovery order, or create a generic settings precedence rule.

## §12 — Runtime recognition

Domain has no separately named Domain recognition registry.

Domain resolution may use:

- direct current semantic Item Type recognition;
- the optional generic Domain-neutral `ItemTypeRegistry` from `AIDE_Index@v2`;
- Domain-owned minimum native Solution/Project recognisers;
- explicit `AIDE_Domain.yaml` declaration parsing; and
- safe runtime caches.

For semantic Item Types, recognition establishes only the Item Type identity. Domain then compares
that identity against its own current approved recognition set. No semantic Item Type definition
can elevate itself to Domain authority.

Compiled/cached state is derived optimisation only. If current recognition/approval provenance
cannot be established, refresh/directly evaluate or fail visibly rather than granting authority
from stale derived state.

## §13 — Target-based discovery

Domain resolution starts from the current target/focus, not from a session-global Domain.

Search local and enclosing structural context upward far enough to establish authoritative Domain
context. A nearby Project, Solution or documentation Index is provisional evidence until applicable
enclosing relationships and approved recognition have been checked.

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

## §14 — Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing approved Domain evidence, including applicable explicit Domain
   declarations, semantic Item Type recognition, native Solution/Project recognition and
   authoritative containment/membership relations.
3. While walking upward, identify every crossed recognised structural boundary and inspect its
   applicable Domain-owned boundary configuration. If `Propagation: Stop` applies, remove any
   enclosing Domain above that boundary from the marked boundary itself and all content within/below
   it, then continue independent resolution for that stopped region.
4. Resolve explicit Domain claims applicable to the target. Validate every declared root's expected
   `Recognition` against independently observed approved recognition. A valid unambiguous explicit
   claim supplies the effective Domain for its governed/composed roots.
5. Otherwise apply authoritative containment: a contained approved structure participates in the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate remaining independent approved co-roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining independent approved root, resolve that
   implicit Domain.
8. When the operation also requires Domain-owned metadata/settings for a resolved implicit Domain,
   identify eligible Index hosts only from governing Indexes of approved semantic recognised roots
   participating in that Domain. Exactly one eligible authoritative host may supply the
   configuration. Mere parent/repository registration is not eligibility. If no unique eligible
   host exists, return a visible unresolved/configuration result and use an explicit Domain
   representation for settings rather than merging, ranking or guessing.
9. If no approved recognition applies, return `No Domain context`.
10. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
    return an unresolved/error result rather than merging, ranking or guessing.

## §15 — Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- an explicit root's declared expected recognition does not match observed recognition;
- an explicit root uses an unknown/unapproved recognition;
- two explicit Domains claim the same effective target without a defined resolution;
- an explicit declaration and an Index expose duplicate/conflicting Domain metadata/settings for
  the same effective explicit Domain;
- multiple eligible governing Indexes expose or claim Domain-owned configuration for the same
  implicit Domain;
- Domain metadata/settings are required for an implicit Domain but no unique eligible governing
  Index host exists and no explicit Domain representation supplies the host;
- a parent/repository Index attempts to claim settings-host authority solely because it registers
  or locates a recognised root;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## §16 — Ownership boundaries

- **Core/Domain** owns this common context/resolution/approved-recognition/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Core/Index** owns generic Index/Item/Item Type behaviour and the optional Domain-neutral
  `ItemTypeRegistry`.
- **Documentation Methodology** owns documentation-specific Index extensions and the
  `DocumentationTopic` semantic Item Type.
- **Native project/solution systems** own native membership and project/solution internals; Domain
  observes only the minimum facts needed for resolution.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## §17 — Deliberately absent

The v4 architecture deliberately does not add:

- generic Index as a Domain recognition;
- owner-self-declared Domain-capable Item Type flags;
- a separate Domain Recognition Registry;
- invented AIDE Item Types for native Solution/Project solely to obtain Domain recognition;
- implicit/generic child-Domain inheritance, override or composition;
- parent/child Domain settings propagation;
- arbitrary nested Domain precedence;
- a generic settings precedence/inheritance engine;
- repository-as-Domain merely because a repository exists;
- a generic filesystem Propagation Stop marker or arbitrary unregistered-folder exclusion;
- a Domain-specific Tool; or
- broad platform parser machinery beyond minimum approved recognition observations.

If a demonstrated use case later requires one of these mechanisms, change Domain Design first and
produce a later Standard release through the normal capability-production path.

## §18 — Success signals

The model is successful when:

- Domain authority can be audited from the Domain-owned approved recognition set;
- an external Item Type cannot promote itself into a Domain root;
- generic Indexes may exist without creating Domain context;
- documentation roots use `DocumentationTopic` rather than bare Index recognition;
- native Solutions/Projects work without invented AIDE type owners;
- runtime recognition may be direct or use the generic Item Type projection without duplicating
  registry machinery;
- a Propagation Stop removes an enclosing Domain from the marked boundary itself and all content
  within/below it, allowing that stopped region to resolve independently without creating parent/child
  Domain semantics;
- explicit roots are validated assertions rather than authority grants;
- an explicit Domain has one authoritative Domain metadata/settings host;
- an implicit Domain that needs Domain-owned configuration has one unambiguous eligible governing
  Index host or uses an explicit Domain representation;
- generic parent/repository registration alone never grants implicit settings-host authority;
- ambiguity and competing host state fail visibly; and
- `No Domain context` remains a normal result.

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Index@v2
References: Core_Index_Design_v2, Core_Domain_Decisions_v4, DocumentationMethodology_Design_v19
