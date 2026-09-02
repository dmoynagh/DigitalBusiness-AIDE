# Core Domain — Design

> **Version 1** (2026-08-31). First blank-sheet issuance of the AIDE Domain model.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Domain defines the common AIDE concept used to identify the named operating/governance context
within which work is being performed.

A Domain gives AIDE one stable term for a boundary that may physically be represented by an Index,
solution, project, explicit Domain declaration, or another recognised structure added later.

Domain belongs under **AIDE Core** because Project Design, Build, Capabilities, AI Deployment,
Documentation Methodology and future AIDE concerns may all consume Domain context.

Core/Domain owns:

- the meaning of Domain;
- recognised Domain-defining structures and the minimum relationships needed to resolve them;
- implicit versus explicit Domain formation;
- Domain discovery and resolution;
- Domain naming/alias conventions needed for navigation and resolution;
- the Domain settings-host and Branch conventions; and
- deterministic ambiguity/failure behaviour.

Individual development/product Domains remain outside the AIDE system tree. They consume AIDE and
retain ownership of their own substantive work and domain-specific workflows.

### Blank-sheet status

This Design is a new model. Earlier `AIDE_Domain` design/decision documents were never implemented
and impose **no compatibility, migration, schema or behavioural requirements** on this Design.
Useful historical reasoning may be reconsidered independently, but no earlier mechanism is carried
forward merely because it existed.

### Declared output

This Design is intended to produce one canonical AI-facing Domain Standard:

```text
AIDE_Domain@v1
```

The canonical Standard should be deployable wherever AIDE may need Domain resolution, including
Design-side and Build-side environments. No dedicated Domain Tool is currently demonstrated.

---

## §2 — Level 1 model

A **Domain is a named AIDE operating/governance context**.

It exists to provide:

1. **one vocabulary for a contextual boundary** — AIDE can refer to "the Domain" whether the
   physical structure is an Index, solution, project or explicit declaration;
2. **a common Domain settings host** — independently owned settings can be stored in a predictable
   Domain-relative location without Domain taking ownership of their semantics; and
3. **explicit composition/clarification** — where existing structures do not themselves express the
   intended larger or different Domain.

A Domain is semantic, not inherently an artefact.

```text
Domain
├── implicit  — inferred from recognised authoritative structure
└── explicit  — declared when the natural interpretation is insufficient or wrong
```

AIDE operation does not require a Domain to exist. "No Domain context" is a legitimate state.

---

## §3 — Domain is contextual, not artefact-owned

An artefact normally does **not** declare its Domain.

Domain membership is resolved from the target artefact's or work target's authoritative structural
context when Domain information is required.

A document therefore does not normally need to know:

- the Domain's current name;
- whether a Domain exists; or
- how the Domain was resolved.

Do not resolve Domain merely because an artefact exists. Resolve it when the current operation
needs Domain context.

### Relative Domain references

Where the actual name is not part of the meaning, documents, Standards and Tools should refer to:

```text
the Domain
```

meaning the effective Domain resolved for the current target/context.

This is preferred to embedding the current Domain name and avoids unnecessary rename coupling.

Explicit Domain names are appropriate where identity itself matters, such as:

- navigation/conversation;
- explicit composition;
- cross-Domain reference;
- provenance where required; or
- an explicit Domain declaration.

---

## §4 — Domain identity, names and aliases

An implicit Domain takes its name/identity from the authoritative recognised structure that
establishes it.

Examples:

- an Index-backed Domain uses the Index's declared project/topic identity;
- a solution-backed Domain uses the solution's recognised identity;
- a standalone project-backed Domain uses the project's recognised identity.

Filename matching may be used as a discovery hint, but an available authoritative declared identity
wins.

Where rename continuity or alternate lookup names are needed, the Domain's authoritative metadata
representation may record previous names/aliases. These exist primarily for human/AI navigation,
reference resolution and continuity.

Do not require ordinary member artefacts to be rewritten merely because the Domain is renamed.

The exact alias field names and formal identity representation are Standard/schema details. They
must preserve Core's general formal-identity principles where formal referenceable identity is
required.

---

## §5 — Recognised Domain-defining structures

The initial demonstrated Domain-capable structure types are:

```text
AIDE Index
solution
project
explicit AIDE Domain declaration
```

Domain owns enough recognition knowledge to resolve these consistently wherever the Domain Standard
is deployed.

It does not absorb their full semantics.

Examples:

- Domain needs to know that a solution authoritatively contains its member projects; it does not
  own build/compilation semantics.
- Domain needs to know that a root Index may have delegated/child Indexes; Documentation
  Methodology still owns Index/register behaviour.

Additional Domain-capable structure types are added only when a demonstrated use case warrants
them.

A repository/worktree is currently a recognised **discovery boundary**, not automatically a
Domain-defining structure.

---

## §6 — Natural containment and structural children

Recognised authoritative containment is preserved.

Example:

```text
Foo.sln
├── Foo.Api.csproj
├── Foo.Core.csproj
└── Foo.Tests.csproj
```

resolves as one `Foo` Domain where those projects are members of the solution.

Likewise:

```text
Capabilities_Index
├── Review_Index
└── Migration_Index
```

remains one `Capabilities` Domain where the child Indexes are delegated/contained by the root
Index.

### No implicit child Domains

A contained structure does **not** create another Domain merely because it could independently act
as a root.

Therefore:

- a project contained by a solution is not a child Domain;
- a delegated/child Index is not a child Domain;
- another recognised structure inside an effective Domain does not create a child Domain solely
  because it exists.

A child Domain would require an explicit Domain declaration.

Child-Domain semantics, including inheritance, settings propagation, nesting, precedence and
parent/child composition, are deliberately **not designed** until a real use case establishes the
need.

---

## §7 — Co-root structures and identity matching

Recognised Domain-capable structures sharing a physical root are evaluated by authoritative
identity and recognised relationships, not proximity alone.

### Matching identity

Where co-root recognised structures have the same authoritative identity, they form one implicit
Domain.

Example:

```text
Foo.sln
Foo_Index
```

where the Index declares project/topic identity `Foo`:

```text
→ Foo Domain
```

When a matching Index coexists with a solution/project:

- the Index is the preferred AIDE Domain metadata/settings host;
- the solution/project retains authority over its native structure and membership; and
- the Index does not become the owner of the solution/project.

This provides an AIDE-controlled overlay for settings and Domain metadata without requiring the
native project/solution format to carry AIDE-specific configuration.

### Different identity

Co-root recognised structures with different identities remain separate implicit Domains by
default.

```text
Foo.sln
Womble_Index
```

means:

```text
Foo Domain
Womble Domain
```

Likewise, multiple standalone project files in one folder with no enclosing solution are separate
implicit Domains by default.

```text
Foo.csproj
Bar.csproj
```

means:

```text
Foo Domain
Bar Domain
```

If the intended reality differs from these defaults, use an explicit Domain declaration.

---

## §8 — Domain membership versus native/corpus membership

Domain membership and a constituent structure's native membership are different questions.

A solution remains authoritative for which projects belong to it.

An Index remains authoritative for which documents are registered in its governed corpus and for
its document/topic/type configuration.

The Domain provides the wider AIDE operating boundary.

Therefore, AIDE-governed artefacts structurally contained within an **unambiguous** effective Domain
may resolve to that Domain even when they are not members of the native solution/project registry.

Example:

```text
Foo.sln
Foo_Architecture_Design_v3.md
Foo_WorkPackage_...
```

The AIDE documents may resolve to the `Foo` Domain while Documentation Methodology separately
determines how/where they are registered and governed as documents.

This distinction prevents Domain from duplicating Index or native project/solution membership
semantics.

### Shared physical containers

A physical folder may legitimately contain several Domains.

Where several Domains share a physical container, location alone is insufficient to assign an
otherwise ambiguous artefact. Domain resolution must use stronger evidence such as:

- authoritative identity;
- recognised native containment;
- Index relationship; or
- an explicit Domain declaration.

Do not guess from proximity.

---

## §9 — Explicit Domains

Use an explicit Domain declaration when the implicit structural interpretation is incomplete,
ambiguous or intentionally different.

Examples include:

- several solutions form one product Domain;
- several standalone projects form one Domain;
- a differently named Index and solution form one Domain;
- several solutions plus a documentation Index form one Domain; or
- structures that would otherwise match implicitly are deliberately separated.

An explicit Domain composes or clarifies recognised roots. It does not recreate their internal
registries.

### `AIDE_Domain.yaml`

Explicit Domain declarations use an AIDE-owned YAML representation named:

```text
AIDE_Domain.yaml
```

One physical location has one such declaration container.

The file is capable of holding multiple independent Domain declarations:

```yaml
Domains:
  - ...
  - ...
```

Each array element is a separate Domain declaration.

Two Domain entries being stored in the same file implies no parent/child, composition, inheritance
or other relationship between them.

This allows several explicit Domains to coexist at one physical location without inventing
multiple Domain filenames.

The canonical Standard/schema should define a small deterministic structured representation.
Domain declarations should contain only information Domain owns or hosts, such as:

- Domain identity/current name and aliases/previous names where needed;
- the recognised roots being explicitly composed/clarified; and
- Domain settings/Branch setting declarations.

Do not place Tags, Standards applicability, Build behaviour, Deployment behaviour, document
membership or native project membership into Domain simply because the declaration file is
available.

---

## §10 — Domain settings host

Domain does **not** define Domain settings.

It defines only the standard location, representation and coexistence conventions by which setting
owners may place settings in Domain context.

The owner of a setting defines:

- setting name/schema;
- allowed values;
- meaning;
- defaults;
- validation;
- consumption;
- precedence; and
- any inheritance/override/combination behaviour.

Domain must not become a generic configuration engine.

### Root settings

A setting declaration with no Branch is attached to the Domain root:

```yaml
Settings:
  SomeSetting:
    ...
```

### Branch settings

A setting declaration may be attached to a structural subtree using `Branch`:

```yaml
Branch: docs/api
Settings:
  SomeSetting1:
    ...
  SomeSetting2:
    ...
```

`Branch` means a Domain-relative structural location/subtree.

Domain defines the Branch attachment convention. It does not define what a setting owner does with
declarations found at different Branches.

Exact Branch path normalization/serialization is a Standard/schema detail and should remain small.

### Preferred hosts

Typical authoritative hosts are:

```text
Index-backed implicit Domain
→ root Index may host Domain settings

solution/project + matching Index
→ Index is preferred Domain metadata/settings host

explicit Domain
→ the Domain entry in AIDE_Domain.yaml hosts Domain settings
```

A solution/project-only Domain that needs Domain metadata/settings may introduce an explicit Domain
representation rather than modifying native project formats merely to carry AIDE configuration.

---

## §11 — Discovery is target-based and upward

Domain resolution begins from the current target or focus, not from a global session Domain.

One session may work with artefacts from different Domains.

Starting from a target artefact, project or focused folder, Domain discovery examines the local and
available enclosing structural context.

A local recognised structure is only a **candidate implicit Domain root** until discovery
establishes that it is not incorporated into an enclosing authoritative Domain.

Example:

```text
/Product
  Product.sln
  /src
    /Foo
      Foo.csproj
      /Handlers   ← current focus
```

If `Foo.csproj` is a member of `Product.sln`, the effective Domain is `Product`, not `Foo`.

Likewise, a solution must be checked for an applicable enclosing explicit Domain before it
establishes its own implicit Domain.

### Do not stop at the first marker

Upward discovery is not "nearest marker wins".

It collects enough available evidence to determine the effective authoritative Domain boundary.

Physical ancestry is a discovery path, not proof of composition.

---

## §12 — Discovery boundaries

Upward discovery must not scan indefinitely.

Search through the available enclosing path only as far as the nearest meaningful operational
discovery boundary appropriate to the current context.

Common boundaries include:

- an explicitly supplied search/discovery boundary;
- workspace/container root;
- repository/worktree root;
- user Documents root;
- Desktop where relevant;
- AppData/application-data root or equivalent;
- another recognised user/application storage root; and
- filesystem/mount root as the final fallback.

The exact platform mechanism for identifying these boundaries may vary, but Domain semantics remain
the same.

A discovery boundary limits **searching**. It does not limit what an explicit Domain declaration may
reference if the Standard permits that reference.

For example, an explicitly declared Domain may compose roots from two repositories without
requiring ordinary upward discovery to search beyond each repository root.

---

## §13 — Resolution model

For a target/focus:

```text
target
  ↓
discover local + enclosing Domain evidence within discovery boundary
  ↓
applicable explicit Domain declaration?
  yes → use declared Domain
  no
  ↓
recognised authoritative containment?
  yes → inherit enclosing effective Domain
  no
  ↓
matching co-root recognised identities?
  yes → one implicit Domain
  no
  ↓
independent recognised root?
  yes → implicit Domain
  no
  ↓
no Domain context
```

The resolver uses semantic relationships, not directory proximity alone.

### Ambiguity and contradiction

Fail visibly rather than guess where:

- two explicit Domains claim the same effective target without defined child-Domain semantics;
- an explicit declaration contradicts authoritative structural identity/membership and does not
  clearly state the intended override;
- several co-located Domains leave an artefact's Domain ambiguous; or
- a referenced Domain/root cannot be resolved reliably.

No generic precedence/merge framework is introduced to hide conflicting Domain claims.

### No Domain

`No Domain context` is a normal result.

It means Domain-scoped context/settings are unavailable. It does **not** mean AIDE is disabled or
that an AIDE-governed document is invalid.

---

## §14 — Relationship to other AIDE concerns

### Core

Core owns Domain as a system-wide foundation and owns the wider formal identity convention.

### Project Design

Project Design may consume Domain context while defining work. Domain does not own the design
workflow; the development/product Domain retains ownership of how Project Design, Build and other
AIDE services are composed for its work.

### Build

Build may resolve Domain from repository/workspace/project/solution context when Domain information
is relevant. Domain behaviour is not redefined separately on Build side.

### Documentation Methodology

Documentation Methodology owns document naming, Index/register mechanics, corpus lifecycle and
document metadata hosting.

Domain may recognise a root Index as a Domain-defining structure and may use the Index as a Domain
settings host. That does not transfer Index semantics into Domain.

### Capabilities

Tags, Scope, Dependencies, Migration, Review, Standards and Tools retain their existing owners.
Domain does not select Standards or duplicate applicability/configuration mechanisms unless a
future demonstrated requirement creates a separate Domain-owned need.

### Environment / AI Deployment

Environment supplies current factual platform/runtime/access information. AI Deployment owns
deployment composition/reconciliation/verification. Domain may host owner-defined settings consumed
by these concerns, but does not own their semantics or operational state.

---

## §15 — Deliberately deferred

The following are not part of v1 Design until demonstrated by a real use case:

- child-Domain inheritance/override/composition;
- parent/child Domain settings behaviour;
- arbitrary nested Domain precedence;
- repository as an implicit Domain-defining structure merely because it is a repository;
- a generic settings precedence/inheritance engine;
- a Domain-specific Tool where the Standard alone is sufficient;
- broad exclusion syntax merely to counteract defaults that can instead be clarified explicitly;
- detailed platform parsers beyond the minimum needed to implement recognised structures; and
- Branch path complexity beyond demonstrated structural-location needs.

---

## §16 — Success signals

The model is successful when:

- the same target resolves to the same Domain across AIDE surfaces given the same observable
  structures;
- simple Index-, solution- and project-backed work needs no Domain file;
- same-name co-root structures naturally converge;
- different-name co-root structures remain separate unless explicitly composed;
- nested project/folder focus resolves to its real enclosing Domain rather than the nearest local
  marker;
- Domain settings have a predictable host without Domain owning their semantics;
- Domain renames do not require rewriting ordinary member documents;
- member artefacts normally carry no Domain metadata;
- existing Index/native membership mechanisms are not duplicated;
- ambiguity fails visibly; and
- the model remains useful with no child-Domain or generic configuration machinery.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: DocumentationMethodology_Design_v15, AIDE_ProjectDesign@v1
