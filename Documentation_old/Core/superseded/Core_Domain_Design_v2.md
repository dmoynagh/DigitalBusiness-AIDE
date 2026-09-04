# Core Domain — Design

> **Version 2** (2026-08-31). Reconciles the established Domain model with the generic Core
> Index/Item Type framework, restricts Domain-capable assignment to Core/Domain, adds a thin
> recognition projection and adds an explicit propagation-stop boundary without introducing child
> Domain inheritance/merge semantics.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Domain defines the common AIDE concept used to identify the named operating/governance context
within which work is being performed.

A **Domain is a named AIDE operating/governance context**. It is contextual and semantic; it is not
inherently a file and is not an AIDE activation switch.

Core/Domain owns:

- the meaning and identity of Domain;
- which semantic Item Types are approved as Domain-capable/Domain-defining;
- the Domain-relevant structural relationships required for resolution;
- implicit versus explicit Domain formation;
- target-based discovery, resolution and deterministic ambiguity/failure behaviour;
- Domain metadata/settings-host and `Branch` conventions;
- Domain propagation-stop semantics; and
- the thin Domain Recognition Registry projection used for efficient hot-path discovery.

Domain does **not** own the full semantics of an approved Item Type/native structure. Generic
Index/Item/Item Type semantics belong to Core/Index; the Item Type owner remains authoritative for
its recognition and provisions. Domain alone decides whether that type may establish or participate
in Domain resolution.

This Design produces:

```text
AIDE_Domain@v2
```

## §2 — Level 1 model and authority seam

```text
target / focus
    ↓
recognise available Items / semantic Item Types
    ↓
Domain-approved type evidence + structural relationships
    ↓
explicit declaration / containment / co-root evaluation
    ↓
Domain propagation boundary where present
    ↓
effective Domain | No Domain | unresolved/error
```

The previous architecture named `AIDE Index`, solution, project and explicit declaration directly
inside Domain. The v2 refinement separates **type recognition** from **Domain authority**:

```text
Item Type owner
  → what this item is / how it is recognised / what it provides

Core/Domain
  → whether this semantic type is eligible to establish/participate in a Domain
```

This prevents an arbitrary local Item Type or generic Index from silently creating a governance
boundary while preserving the existing natural Domain cases.

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

## §4 — Domain model

A **Domain is a named AIDE operating/governance context**.

A Domain may be:

```text
implicit  — established from a Domain-approved semantic Item Type / authoritative structure
explicit  — declared in AIDE_Domain.yaml to compose or clarify recognised roots
```

Generic Item/Item Type semantics belong to `AIDE_Index@v1`. A type owner defines what an Item Type
is, how it is identified and what it provides. **Only Core/Domain decides whether a semantic Item
Type is permitted to establish/participate in Domain resolution.**

An arbitrary Item Type cannot self-assign Domain authority, and a generic Index is not
Domain-defining merely because it exists.

Initial Domain recognition continues to cover the demonstrated structural roles represented by the
current system—documentation top-level topic/Index structures, native solution structures, native
project structures and explicit AIDE Domain declarations—but they are consumed through
Domain-approved semantic type/recognition entries rather than a rule that every Index/solution/
project-shaped thing automatically creates Domain authority.

A repository/worktree remains a discovery boundary, not an implicit Domain type.

## §5 — Natural containment

Authoritative structural containment prevents a contained Domain-capable item from establishing a
second implicit Domain.

- a project that is an authoritative member of a solution remains in the solution Domain;
- a delegated/self-describing documentation topic remains in its enclosing effective Domain unless
  propagation is explicitly stopped; and
- another Domain-capable Item inside an effective Domain does not create a child Domain merely
  because it could establish a root when isolated.

Structural children do not create child Domains implicitly. Child-Domain inheritance, settings
propagation, precedence and parent/child composition remain undefined in v2.

### Domain propagation stop

Domain may mark a structural boundary as **Propagation: Stop**. The effect is deliberately narrow:

> an enclosing Domain does not propagate through that boundary; content below it must resolve
> Domain independently.

This does **not** create a child Domain and does not define inheritance, merge or precedence.

Where the boundary is represented as an Index Item, use the Domain-owned contribution, for example:

```yaml
Domain:
  Propagation: Stop
```

Equivalent representation may be defined for another Domain-aware structure. The semantic meaning
belongs to Domain; Index merely hosts the property.

## §6 — Co-root recognised structures

Evaluate recognised structures sharing a physical root by authoritative identity and structural
relationships, not proximity alone.

### Matching identity

Co-root structures with matching authoritative identities form one implicit Domain.

```text
Foo.sln + Foo_Index  → Foo Domain
```

An available declared Index structural/topic identity is authoritative over filename-only matching.
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

## §7 — Domain membership boundary

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

## §8 — Domain identity and references

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

## §9 — Explicit Domain declaration

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
- `Type` — one of the v2 Domain-approved root roles represented by `Index`, `Solution`, or `Project` for each explicit root; the resolver maps that role to approved semantic recognition rather than granting authority from the token alone.
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

## §10 — Branch and settings convention

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
authoritative structural/topic identity and `Roots` are not repeated. Core/Index owns generic Index hosting/representation; Documentation Methodology owns any
documentation-specific Index sections. Domain owns the meaning of this Domain configuration payload.

For a solution/project-only implicit Domain that needs AIDE Domain metadata/settings, introduce an
explicit `AIDE_Domain.yaml` representation rather than modifying the native format solely to carry
AIDE configuration.

## §11 — Domain Recognition Registry

Runtime Domain discovery should not load every Standard/Item Type definition for every path step.
A build/runtime environment may compile the Domain-approved type assignments into a thin
`DomainRecognitionRegistry` containing only the cheap signatures/relations required for Domain
discovery.

Rules:

- the registry is an optimisation/projection, not the source of Domain authority;
- Core/Domain approval remains authoritative;
- load/compile definitions once per relevant context;
- prefer explicit/native/name/extension/marker evidence before expensive content inspection;
- cache unchanged resolution where safe; and
- if a registry entry cannot be traced to a currently approved semantic type/recognition rule, fail
  or refresh rather than silently granting Domain authority.

## §12 — Target-based discovery

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

## §13 — Resolution procedure

For the target/focus:

1. Establish the available discovery boundary.
2. Collect local and enclosing recognised Domain evidence within that boundary, including
   applicable `AIDE_Domain.yaml` declarations and authoritative containment/membership relations.
3. Resolve explicit Domain claims applicable to the target. A valid unambiguous explicit claim
   supplies the effective Domain and may clarify/override the natural grouping of its declared
   roots.
4. Before propagating an enclosing Domain through a structural boundary, apply any Domain-owned
   `Propagation: Stop` declaration. If propagation is stopped, disregard the enclosing Domain for
   content below that boundary and continue resolution independently; the stop does not itself
   create a Domain.
5. Otherwise apply authoritative containment: a contained Domain-capable structure inherits the
   enclosing effective Domain rather than creating another implicit Domain.
6. Evaluate co-root independent recognised roots: matching authoritative identities converge;
   different identities remain separate.
7. If the target belongs unambiguously to one remaining independent recognised root, return that
   implicit Domain.
8. If no Domain-capable structure applies, return `No Domain context`.
9. If authoritative claims are contradictory or the target cannot be assigned unambiguously,
   return an unresolved/error result rather than merging, ranking or guessing.

## §14 — Failure and ambiguity

Fail visibly rather than infer a Domain where, for example:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership without clearly
  expressing the intended override;
- several co-located Domains leave the target's Domain ambiguous; or
- a declared root cannot be resolved reliably.

Do not introduce generic precedence or merge rules to hide contradictory Domain claims.

`No Domain context` is not an error. It means Domain-scoped context/settings are unavailable; AIDE
Standards, Tools and governed documentation may still operate normally.

## §15 — Ownership boundaries

- **Core/Domain** owns this common context/resolution/settings-host contract.
- **Development/product Domains** remain outside the AIDE system tree and own their substantive work
  and the workflow composing AIDE services for that work.
- **Core/Index** owns generic Index/Item/Item Type behaviour. **Documentation Methodology** owns documentation-specific Index extensions and the `DocumentationTopic` semantic type.
- **Project/solution systems** own native membership and project/build-system semantics.
- **Setting owners** own all setting semantics, including any precedence or inheritance.
- **Capabilities** retain Tags, Scope, Dependencies, Migration, Review, Standards and Tools
  semantics; Domain does not select Standards or duplicate applicability mechanisms.
- **Environment / AI Deployment** retain platform/runtime facts and deployment behaviour. They may
  consume Domain-hosted settings without transferring their semantics to Domain.

## §16 — Deliberately absent

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

## §17 — Design constraints / deliberately deferred

The v2 architecture deliberately does not add child-Domain inheritance/override/merge,
parent/child settings propagation, arbitrary nested Domain precedence, repository-as-Domain merely
because a repository exists, a generic settings precedence engine, arbitrary self-declared
Domain-capable Item Types, or broad platform parser machinery beyond the recognition contracts
needed by approved types.

The propagation-stop feature is intentionally not a partial inheritance system: it only prevents an
enclosing Domain from flowing through a marked boundary.

## §18 — Success signals

The model is successful when the same observable structures resolve consistently across AIDE
surfaces; generic Indexes can exist without accidentally creating Domains; simple documentation
topics/solutions/projects still need no explicit Domain file where their approved structural type
is sufficient; explicit composition remains available where natural structure is wrong; Domain
recognition can be evaluated cheaply; and ambiguity fails visibly rather than being hidden by
precedence/merge inference.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: Core_Index_Design_v1, Core_Domain_Decisions_v2, DocumentationMethodology_Design_v18
