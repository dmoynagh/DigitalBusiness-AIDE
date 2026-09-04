# AIDE Index — Standard

> **Identity:** `AIDE_Index@v2`
> **Common name:** Index
> **Version 2** (2026-09-01). Retains the generic Index/Item/Item Type contract while making the
> optional Item Type registry Domain-neutral and removing the separate Domain recognition registry
> concept.
>
> **Default weight:** Requirement

## Purpose

Provide one generic AIDE mechanism for maintaining an authoritative hierarchical view of
significant items within a defined boundary while allowing specialised owners to add their own
properties/registers without transferring semantic ownership.

## Index contract

An Index shall identify its scope and provide a hierarchical `Contents` view of the significant
Items it registers.

The Index is authoritative for:

- which items it registers within that scope;
- their Index-owned locator/containment facts; and
- Index-owned information attached to those registrations.

Registration does **not** make the Index authoritative for a registered item's internals.

`Contents` may intentionally omit insignificant physical items and may stop at a delegated or
self-describing boundary.

## Item

A registered Item may expose, as applicable:

```text
name / identity
locator / containment
semantic Item Type(s)
description
compact owner-defined properties
delegated/self-describing boundary pointer
```

Arrange Items primarily by containment/location. Type is metadata, not the primary hierarchy.

## Item Type Definition

An Item Type Definition has two semantic jobs:

1. identify whether an item satisfies the type; and
2. state what the type provides/enables when identified.

Use declarative observable recognition evidence. Prefer cheap evidence such as explicit identity,
name/extension, structural marker or authoritative native relationship before expensive content
inspection.

Do not use the generic Item Type contract as arbitrary executable classification logic.

An Item may satisfy several independent semantic Item Types. No generic type-inheritance hierarchy
exists in v2.

## Physical fallback

If no richer semantic type applies:

```text
physical directory → Folder
physical file      → File
```

Physical classification may coexist with semantic Item Types.

## Extension ownership

An owner may define Item properties or specialised Index sections/registers.

The contributing owner owns:

- field/section meaning;
- values/schema;
- validation;
- lifecycle; and
- update rules.

Index owns generic hosting/coexistence only.

An Index updater shall preserve properties/sections it does not own unless explicitly authorised to
reconcile them.

## Delegation

A parent Index may register and locate a self-describing child boundary without duplicating its
internal registry. The parent remains authoritative for the parent registration; the child/native
owner is authoritative internally.

## Canonical representation

Use Markdown as the canonical human/AI source representation.

Prefer:

- headings/lists for hierarchy;
- YAML flow mappings/sequences for compact structured Item properties; and
- tables for regular homogeneous extension sections.

Do not invent an AIDE-only mini-language where standard YAML flow syntax suffices.

HTML may be generated as presentation but is not canonical source in v2.

## Runtime Item Type Registry

A runtime/build environment may compile available current Item Type Definitions into one compact
`ItemTypeRegistry`.

The registry contains only the recognition/provision facts needed for Item Type recognition and
provision lookup. It is **Domain-neutral** and is derived optimisation state, not semantic or Domain
authority.

Use this order where practical:

1. explicit/cheap selectors;
2. structural/native relationship checks;
3. expensive inspection only if necessary;
4. lazy enrichment after classification; and
5. cached reuse for unchanged items where safe.

A compiled registry is optional. Direct evaluation of current authoritative Item Type Definitions
is a conforming fallback when a compiled registry is absent, stale or unsuitable.

If a compiled registry is persisted/built, preserve enough authoritative source identity/version
provenance to determine whether it remains current and to invalidate/rebuild it safely. This
Standard does not define a separate registry-build subsystem.

## Domain boundary

Generic Index existence does **not** establish a Domain.

`AIDE_Domain` alone owns the approved Domain recognition set. Domain may consume a semantic Item
Type identity recognised directly or through `ItemTypeRegistry`, then separately test that identity
for Domain eligibility.

No Item Type owner or `ItemTypeRegistry` entry may self-grant Domain authority through a
`DomainCapable`, `domainDefining`, `DomainContainer` or equivalent owner-controlled declaration.

Domain may additionally apply Domain-owned native recognisers that are not Item Types. No separate
Domain-specific compiled registry is required for semantic Item Type recognition.

## Deliberately absent

No v2 requirement exists for:

- type inheritance;
- universal metadata ontology;
- generic query language;
- explicit registration of every file/folder;
- mandatory root pointer for every project/container;
- automatic recursion into self-describing child boundaries;
- an owner-self-declared Domain-capable Item Type flag; or
- a separate Domain Recognition Registry artefact.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v22
References: Core_Index_Design_v2, Core_Domain_Design_v3
