# Capabilities — Overview

> **Version 8** (2026-08-28). Architecture checkpoint after the capability-production,
> Build handoff, platform-realisation, migration-source, and Deployment Set refinements.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Architecture at a glance

```text
Capabilities
├── Standards
├── Tools
├── Scope
├── Dependencies
├── Migration
├── Deployment
└── Review
```

- Seven peer components remain.
- Standards and Tools define capability kinds and canonical production.
- Scope, Dependencies, Migration, Deployment, and Review provide shared behaviour.
- WorkPackage belongs to AIDE Build and is consumed by Capabilities.
- Generic platform implementation knowledge belongs Build side.

---

## End-to-end flow

```text
DESIGN SIDE

Capability Design
      ↓
Build Capability
      ↓
Canonical Standard / Tool
  ├── generic capability
  ├── optional platform addenda
  └── Required Migration / On-Update declarations
      ↓
effective Build Config
      ↓
Build WorkPackage

══════════════════ HANDOFF ══════════════════

BUILD SIDE

canonical capability
 + WorkPackage
 + platform Build Standards / Tools / references
      ↓
Platform contribution(s)
      ↓
Capability Package
      ↓
Deployment
      ↓
Deployment Set composition
      ↓
publish / distribute
      ↓
WorkPackage Outcome returned
```

### Core boundary

**Design side owns capability meaning. Build side owns platform realisation.**

If Build side needs to reopen the Capability Design to understand what this capability requires,
the WorkPackage/canonical outcome is incomplete.

If the Capability Design explains generic plugin, skill, Codex, repository, or ChatGPT bundle
mechanics, platform implementation knowledge has leaked back across the boundary.

---

## Canonical Standard / Tool

The canonical outcome is produced by `Build Capability`.

It contains:

- the complete generic capability definition;
- capability-specific platform addenda only where a platform genuinely differs;
- Required Migration and On-Update declarations for the capability/version.

No platform addendum means the generic capability applies unchanged.

The platform addendum says what is special about **this capability on that platform**. Build-side
platform Standards say how that platform implements capabilities generally.

---

## Build Config

Every buildable capability has an effective Build Config:

| Setting | Meaning | Default |
|---|---|---|
| Platforms | Target platforms to build | Current supported-platform set |
| Side | Design, Build, or both | Both |
| Deployment Set(s) | Named logical deployment destination(s) | Explicit/inherited per config model |

The config may be managed on Design side or Build side. The effective values must be resolved by
WorkPackage execution.

---

## Migration

```text
Standard / Tool transition declarations
        ↓
Migration Build Standard
        ↓
canonical migration information
        ↓
platform/deployment builders
        ↓
target-specific migration representation
```

- Required Migration and On-Update are distinct postures.
- Transition declarations live with the owning Standard/Tool.
- Separate source migration files are not required.
- Migration owns the model and execution; the capability owner authors the transition intent.
- `/migrations-check`, `/migrations-apply`, and `/update-doc` remain the logical runtime tools.

---

## Platform Build

Build side consumes:

```text
canonical capability
+ capability-specific platform addendum
+ Build Config
+ WorkPackage
+ platform Build Standards / Tools / references
```

and produces **Platform Contributions**.

Platform Contributions are capability-local. They may not be independently deployable because
Deployment may need to compose contributions from many packages into one platform artefact.

Examples of generic platform knowledge that belongs Build side:

- Claude skill/plugin structures;
- Codex capability/command structures;
- ChatGPT project-context/bundle construction;
- repository layouts and build/deployment files.

---

## Package

A Capability Package is the completed capability-local release unit passed to Deployment.

It carries, as required by the package contract:

- platform contributions;
- identity/version information;
- transition material;
- removals;
- manifest/integrity information.

ZIP is the preferred physical container where practical; Package is the logical contract.

**Package is the hard production/deployment boundary.**

---

## Deployment Set

A Deployment Set is a named logical grouping/destination.

```text
Deployment Set: workflow-core

Claude
  → plugin "workflow-core"

Codex
  → corresponding Codex capability collection

ChatGPT
  → merged project bundle
  → workflow_core_bundle.md
```

The capability says only:

```text
Deployment Set: workflow-core
```

Deployment configuration knows what `workflow-core` physically means on each platform.

### Set-aware composition

```text
Package A ─┐
Package B ─┼──► Deployment Set
Package C ─┘
               ├── Claude assembled plugin
               ├── Codex assembled collection
               └── ChatGPT workflow_core_bundle.md
```

Build is capability-local. Deployment is set-aware.

---

## Component ownership review

| Component | Owns | Key boundary |
|---|---|---|
| Standards | Standard meaning, weights, canonical Standard production/use model | Not generic platform adaptation |
| Tools | Tool behaviour, logical commands, canonical Tool production | Not concrete platform rendering |
| Scope | Applicability | Must be separated from Build Config/deployment targeting |
| Dependencies | Dependency meaning, conformance version, availability | Not install/deploy/transition |
| Migration | Transition semantics, production rules, execution model/tools | Owner writes transition intent |
| Deployment | Package consumption, Deployment Sets, composition, publication | Starts from completed package |
| Review | Reusable independent assessment/disposition | Lead owns final model |

---

## Outstanding architecture work

### Deployment

Complete:

- Deployment Config;
- Deployment Set resolution;
- package validation;
- set composition;
- replacement/removal;
- partial failure;
- resumption/idempotency;
- platform-specific deployment builders;
- repository/publication behaviour.

### WorkPackage

Now an AIDE Build topic. Define:

- WorkPackage Standard;
- required inputs and supplied artefacts;
- acceptance/validation;
- execution posture;
- WorkPackage Outcome;
- success/partial/fail reporting;
- feedback and fix/resumption loop.

### Scope

Revalidate the methodology and separate:

- runtime applicability;
- Design/Build side applicability;
- target platforms in Build Config;
- Deployment Set membership;
- retrieval/discovery/trigger realisation.

### Dependencies

Confirm the minimal dependency/conformance/availability contract and its interaction with
Migration and Build-side installed capabilities.

### Review

Finalise the generic model, profiles, record, disposition, and tooling.

### Shared contracts

Still open:

- identity/version contract;
- package/manifest contract.

---

## Architecture checkpoint

Before further child-document production, confirm:

- Is every capability-specific build input present in the canonical outcome/WorkPackage?
- Can Build side realise a platform without generic platform mechanics in the Capability Design?
- Can one package be deployed into a named Deployment Set without capability judgement?
- Can Deployment rebuild a set from its packages/configuration?
- Are Required Migration and On-Update impossible to confuse after extraction/adaptation?
- Does Scope remain applicability rather than becoming a second Build/Deployment config system?
- Does Dependencies stop at dependency state rather than growing into installation?

---

**Depends on:** `Capabilities_Brief` v3, `Capabilities_Design` v3,
`Capabilities_Decisions` v9.

**References:** `Core_System_Design` v2,
`Capabilities_Standards_Design` v3 (revision required),
`Capabilities_Tools_Design` v1 (revision required).

**Methodology:** v17
