# Core Index — Decisions

> **Version 1** (2026-08-31). Records the blank-sheet decisions establishing the generic AIDE
> Index and Item Type framework in Core.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Index is a generic Core mechanism

**Decision.** Move generic Index semantics to Core. Documentation Methodology remains a consumer
and extension owner for documentation-specific Index behaviour.

**Reason.** Repositories, projects, documents, native structures and future contexts all need the
same basic structural registration concept. Keeping generic Index inside Documentation Methodology
would make a broadly useful system primitive documentation-specific.

## D2 — Index is an authoritative hierarchical register, not a flat type catalogue

**Decision.** Index organises significant Items by containment/location and is authoritative for
its registrations and Index-owned information.

**Rejected alternative.** Use a flat table grouped by item type. Rejected because mixed structural
containers are naturally navigated hierarchically and type is metadata rather than the primary
location relationship.

## D3 — Registration does not transfer authority over item internals

**Decision.** Registering an item gives the Index authority only over the registration facts it
owns. The registered item/native owner remains authoritative for its internals.

**Reason.** Without this boundary, a repository Index could accidentally become authoritative over
project internals, solution membership or document semantics merely by listing them.

## D4 — Contents may stop at self-describing boundaries

**Decision.** A parent Index need not recursively enumerate an independently self-describing child
container. It locates/describes the boundary and delegates internal discovery.

**Reason.** This keeps hot/high-level Indexes small and avoids duplicate registries.

## D5 — Item Type is the generic semantic classification mechanism

**Decision.** An Item Type Definition states only how the type is identified and what it provides
once identified.

**Reason.** This is sufficient to support semantic types such as DocumentationTopic, solution or
future domain-specific structures without building a universal object model.

## D6 — Prefer composable types over inheritance

**Decision.** An Item may satisfy multiple semantic Item Types. No generic inheritance hierarchy is
introduced in v1.

**Reason.** Physical/semantic classifications overlap naturally and current use cases do not need
class hierarchy machinery.

## D7 — Folder and File are immediate fallbacks

**Decision.** A physical directory/file with no richer semantic classification resolves to
`Folder`/`File`.

**Reason.** The framework remains useful without requiring a formal type definition for every
physical item.

## D8 — Index hosts owner-defined extensions without absorbing their semantics

**Decision.** Semantic owners may define Item properties and specialised Index sections. Core Index
owns only generic hosting/coexistence.

**Reason.** This lets Documentation Methodology, Domain and future owners extend one structural
surface without turning Index into a generic configuration authority.

## D9 — Markdown + YAML flow is the canonical representation

**Decision.** Use Markdown hierarchy plus compact YAML flow mappings/sequences. Tables remain valid
for homogeneous owner-defined sections.

**Rejected alternative.** Canonical HTML. Rejected because it adds context/token bloat and depends
on renderer support without improving the machine-readable source contract.

## D10 — Runtime type resolution uses a thin compiled registry

**Decision.** Item Type Definitions may be compiled into a compact runtime registry; cheap
recognition runs before expensive enrichment and unchanged results may be cached.

**Reason.** Domain and other frequently invoked classification should not require loading or
scanning every full Standard on every operation.

## D11 — Generic Index is not Domain-defining by default

**Decision.** Domain-defining status is assigned by Core/Domain to approved semantic Item Types,
not by generic Index existence or arbitrary type-owner declaration.

**Reason.** Domain formation changes system governance context and therefore requires restricted
system-level authority.

## D12 — Update operations preserve other owners' contributions

**Decision.** An updater changes only the fields/sections it owns or is authorised to reconcile.
Unknown owner contributions and human-authored descriptions are preserved.

**Reason.** A shared Index becomes unsafe if a generated update can erase unrelated semantic or
human information.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Core_Index_Design_v1
References: Core_Domain_Decisions_v2, DocumentationMethodology_Decisions_v19
