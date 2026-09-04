# Core Index — Decisions

> **Version 2** (2026-09-01). Preserves the v1 generic Index decision history and records the
> Review A reconciliation to one optional Domain-neutral Item Type recognition projection with
> direct authoritative recognition as the supported fallback.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## D1 — Index is a generic Core foundation

**Decision.** Index is a generic AIDE structural registration/information-hosting mechanism owned by
Core rather than a documentation-only construct.

**Reason.** Repository/catalogue navigation, documentation corpora, native structures and future
AIDE concerns need the same small concept without making Documentation Methodology the owner of all
structural registration.

## D2 — Index authority stops at the registration boundary

**Decision.** An Index is authoritative for which Items it registers within its scope and for
Index-owned facts about those registrations. Registration does not make the Index authoritative for
the registered Item's internals.

**Reason.** Structural discovery must not transfer authority from native/self-describing owners into
the registry that points at them.

## D3 — Registration is selective

**Decision.** `Contents` registers significant Items and is not required to enumerate every physical
file/folder.

**Reason.** A useful structural view should remain compact and purpose-driven rather than becoming a
filesystem mirror.

## D4 — Parent Indexes may delegate at self-describing boundaries

**Decision.** A parent Index need not recursively enumerate an independently self-describing child
container. It locates/describes the boundary and delegates internal discovery.

**Reason.** This keeps hot/high-level Indexes small and avoids duplicate registries.

## D5 — Item Type is the generic semantic classification mechanism

**Decision.** An Item Type Definition states only how the type is identified and what it provides
once identified.

**Reason.** This is sufficient to support semantic types such as `DocumentationTopic` or future
domain-specific structures without building a universal object model.

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

## D10 — Runtime type resolution may use a thin compiled registry

**Decision.** Item Type Definitions may be compiled into a compact runtime registry; cheap
recognition runs before expensive enrichment and unchanged results may be cached.

**Reason.** Frequently invoked classification should not require loading or scanning every full
Standard on every operation.

## D11 — Generic Index is not Domain-defining by default

**Decision.** Domain-defining status is assigned by Core/Domain to approved recognition, not by
generic Index existence or arbitrary type-owner declaration.

**Reason.** Domain formation changes system governance context and therefore requires restricted
system-level authority.

## D12 — Update operations preserve other owners' contributions

**Decision.** An updater changes only the fields/sections it owns or is authorised to reconcile.
Unknown owner contributions and human-authored descriptions are preserved.

**Reason.** A shared Index becomes unsafe if a generated update can erase unrelated semantic or
human information.

## D13 — Keep one generic Item Type recognition projection

**Decision.** The optional `ItemTypeRegistry` remains the single generic compiled Item Type
recognition projection. Do not create a second Domain-specific registry for the same semantic Item
recognitions.

**Reason.** Domain eligibility is an authority decision applied after recognition, not a second Item
Type recognition system.

**Consequence.** Domain may consume a semantic Item Type identity recognised directly or through
`ItemTypeRegistry`, then apply its own approved recognition set. Domain-owned native recognition is
separate because those structures are not required to be Item Types.

## D14 — Runtime registry does not carry self-granted Domain authority

**Decision.** An Item Type owner cannot make itself Domain-capable through its Item Type Definition
or through metadata in `ItemTypeRegistry`.

**Reason.** The registry is a Domain-neutral recognition/provision optimisation. Core/Domain alone
owns the approved recognition set that controls Domain authority.

**Consequence.** Fields such as `DomainCapable`, `domainDefining`, `DomainContainer` or an equivalent
owner-controlled grant are not part of the generic registry contract.

## D15 — Direct recognition is the supported fallback

**Decision.** A compiled `ItemTypeRegistry` is optional. A conforming implementation may evaluate
current authoritative Item Type Definitions directly.

**Reason.** Recognition correctness must not depend on a separately maintained compiled artefact.

**Consequence.** Persisted compiled forms are derived outputs and retain enough source provenance to
be invalidated/rebuilt safely. Core does not add a registry-build subsystem.

---
Dependencies: !AIDE_DocumentationMethodology@v22, Core_Index_Design_v2
References: Core_Domain_Decisions_v3, DocumentationMethodology_Decisions_v20
