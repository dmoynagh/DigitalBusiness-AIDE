# Core Index — Design

> **Version 1** (2026-08-31). Establishes Index as a generic Core-owned structural register and
> extension host, separate from Documentation Methodology's documentation-specific Index usage.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Index is the generic AIDE mechanism for maintaining an authoritative, human-readable view of
significant items within a defined boundary.

Core/Index owns:

- the meaning of an Index;
- Index scope/identity;
- hierarchical item registration;
- the generic Item and Item Type Definition contracts;
- physical `Folder` / `File` fallback classification;
- containment/delegation boundaries;
- owner-defined extension/property hosting;
- generic authority and update-preservation rules; and
- the compact runtime Item Type Registry projection.

Core/Index does **not** own:

- the internals of registered items;
- document lifecycle/type semantics;
- Domain-defining authority;
- native solution/project membership semantics;
- arbitrary owner-specific properties/sections; or
- a universal metadata/query/configuration language.

The defining authority boundary is:

> **An Index is authoritative for the items it registers within its scope and for the information
> it owns about those registrations. Registration does not make the Index authoritative for the
> registered item's internals.**

This Design produces:

```text
AIDE_Index@v1
```

## §2 — Level 1 model

An Index is:

> **an authoritative, hierarchical view of significant items within a defined boundary, together
> with information and optional specialised sections applicable to that boundary.**

The minimum model is deliberately small:

```text
Index
├── identity / scope
├── Contents
│   └── registered Items arranged by containment/location
└── optional owner-defined extension sections
```

The Contents view is not required to enumerate every physical file or folder. It registers items
whose existence/location/properties are useful to the Index's purpose and may stop at delegated or
self-describing boundaries.

## §3 — Scope and identity

Every Index states what it represents. Examples include:

- a repository;
- a folder/container;
- a documentation top-level topic/corpus;
- a top-level topic or branch;
- another owner-defined structural boundary.

The Index's identity/scope is not limited to AIDE documentation.

An Index may be colocated with what it represents, but physical filename/location is not its entire
semantic identity.

## §4 — Contents and Item

`Contents` is the generic structural view.

Items are arranged by **containment/location**, not grouped primarily by type.

A registered Item may expose, as applicable:

- display name / identity;
- locator/path, often implicit from the tree;
- semantic Item Type(s);
- concise human description;
- compact owner-defined properties/details; and
- a pointer/delegation to another self-describing boundary.

Type is metadata about an item, not the organising principle of the hierarchy.

Mixed item kinds may coexist in one Contents tree: folders, projects, files, documents, assets,
references, native structures or another significant item.

A project/container root locator is **not universally required**. A self-describing project folder
may be located by the parent Index and then resolve its own internal root/index from within that
folder.

## §5 — Item Type Definition

An **Item Type Definition** supplies a reusable semantic classification for Items.

The generic contract says only:

1. **how an item can be identified as the type**; and
2. **what becomes available/applicable once identified.**

Conceptual form:

```yaml
ItemType:
  Name: DocumentationTopic
  Identify: <declarative recognition evidence>
  Provides: <properties / semantic capabilities made available>
```

The type owner defines its recognition and provisions. The Index framework does not reinterpret
those semantics.

Recognition should prefer cheap, observable evidence such as:

- explicit declared identity/type;
- filename/extension/name pattern;
- structural marker;
- authoritative native relationship; or
- simple container-content evidence.

Do not turn Item Type Definition into arbitrary executable matching logic.

### Composability, not inheritance

An Item may satisfy more than one semantic Item Type.

For example, one physical directory might be both:

```text
Folder
DocumentationTopic
GitRepository
```

No Item Type inheritance/class hierarchy is defined in v1. Add one only if a demonstrated need
cannot be represented by independent composable types.

## §6 — Physical fallback

Physical form and semantic type are separate.

When no semantic Item Type applies:

```text
physical directory → Folder
physical file      → File
```

`Folder` and `File` are immediate Core fallback types. They do not imply richer semantics.

An Item may retain its physical classification while also satisfying one or more semantic types.

## §7 — Owner-defined properties and extension sections

Index is an extensible host.

A semantic owner may define:

- properties on Items; and/or
- specialised Index sections/registers.

The owner defines the field names, meaning, permitted values, validation and lifecycle of its
contribution. Index owns only hosting/coexistence and generic structural rules.

Examples include:

- Documentation Methodology → Document Register, topic declarations, custom document types;
- Domain → Domain-owned Index properties/settings;
- Dependencies → dependency-related contribution where one is demonstrated;
- another standard → an Item Type or specialist register.

Specialised registers are added only when their independent use justifies them. The existence of
one projection does not require a generic multi-view/query mechanism.

## §8 — Delegation and self-describing boundaries

An Index may stop at an item that is independently self-describing.

A repository Index can therefore state that a documentation top-level topic exists, describe it
and locate it, then stop. That topic's governing Index/native structure becomes authoritative for
its internals.

Delegation means:

```text
parent Index
  authoritative for registration/location of child boundary
        ↓
child Index / self-describing structure
  authoritative for its own internal registrations
```

Do not duplicate the entire child registry in the parent merely because it is technically
reachable.

## §9 — Representation

The canonical human/AI Index representation is Markdown using:

- headings and lists for structural/hierarchical views;
- YAML flow mappings/sequences for compact structured properties; and
- tables only where an owner-defined section is sufficiently homogeneous/regular for a table to
  improve readability.

Example:

```markdown
- **Capabilities/** — Reusable AIDE capability infrastructure.  
  `DocumentationTopic`  
  `{topics: [Capabilities]}`
```

Use standard YAML flow syntax rather than inventing an AIDE-specific mini-language.

HTML may be generated for presentation, but is not the canonical Index source representation.

## §10 — Update/reconciliation ownership

Index updates are contribution-preserving.

An updater changes only information it owns or is explicitly authorised to reconcile. In
particular:

- discovery may update observed locator/existence facts;
- an Item Type owner may update its own type-derived properties;
- Domain may update Domain-owned properties;
- Documentation Methodology may update its Document Register; and
- human-authored descriptions remain untouched unless explicitly authored/updated.

Unknown owner properties/sections are preserved.

Do not regenerate the whole Index in a way that destroys authored descriptions or another owner's
contributions merely because one derived property changed.

## §11 — Runtime Item Type Registry

Full Index/Item Type source material is not required on every classification operation.

A runtime/build environment may compile loaded Item Type Definitions into a compact
`ItemTypeRegistry` containing only the recognition/provision facts needed for the current work.

Performance posture:

1. load/compile definitions once per relevant context;
2. evaluate cheap selectors first;
3. perform expensive inspection only when needed;
4. lazily load richer type information for enrichment;
5. cache unchanged resolution where safe; and
6. use immediate `Folder` / `File` fallback where no semantic type matches.

The registry is a derived optimisation, not the authoritative source of type semantics.

## §12 — Relationship to Domain

Generic Index existence does **not** automatically establish a Domain.

Core/Domain owns which semantic Item Types are Domain-defining/Domain-capable and may compile a
thin Domain Recognition Registry from those approved types.

This prevents any arbitrary Item Type owner from acquiring Domain authority by setting a flag on
its own definition.

Index may host Domain-owned properties without owning Domain semantics.

## §13 — Relationship to Documentation Methodology

Documentation Methodology consumes the generic Index framework for documentation corpora.

It retains ownership of documentation-specific concerns including:

- DocumentationTopic Item Type semantics;
- topic/document organisation;
- Document Register;
- custom document type registration;
- assets/unmanaged document-corpus records; and
- document lifecycle/current-version resolution.

Documentation Methodology no longer owns generic Index semantics.

## §14 — Deliberately absent from v1

Do not introduce without a demonstrated need:

- Item Type inheritance;
- universal metadata ontology;
- arbitrary executable type matching;
- generic item query language;
- mandatory explicit registration of every physical item;
- HTML as canonical Index source;
- mandatory project-root pointers; or
- automatic recursion through self-describing boundaries.

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: Core_Domain_Design_v2, DocumentationMethodology_Design_v18
