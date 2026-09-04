# AIDE Index — Standard

> **Identity:** `AIDE_Index@v1`
> **Common name:** Index
> **Version 1** (2026-08-31). First canonical generic Index/Item Type contract.
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
exists in v1.

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

HTML may be generated as presentation but is not canonical source in v1.

## Runtime Item Type Registry

A runtime/build environment may compile available Item Type Definitions into a compact registry.

Use this order where practical:

1. explicit/cheap selectors;
2. structural/native relationship checks;
3. expensive inspection only if necessary;
4. lazy enrichment after classification; and
5. cached reuse for unchanged items where safe.

The compiled registry is derived optimisation state, not semantic authority.

## Domain boundary

Generic Index existence does **not** establish a Domain.

`AIDE_Domain` owns the approved Domain-defining/Domain-capable Item Type set and any thin Domain
Recognition Registry derived from it. An Item Type owner cannot grant itself Domain authority by
setting a local flag.

## Deliberately absent

No v1 requirement exists for:

- type inheritance;
- universal metadata ontology;
- generic query language;
- explicit registration of every file/folder;
- mandatory root pointer for every project/container; or
- automatic recursion into self-describing child boundaries.

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
Dependencies: !AIDE_DocumentationMethodology@v21
References: Core_Index_Design_v1, Core_Domain_Design_v2
