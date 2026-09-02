# Capabilities — Overview

> **Version 10** (2026-08-29). Review checkpoint: finalises the independent assessment model,
> five Review Profiles, lifecycle/records, orchestration Tool boundary, scope control, and
> environment/communication seams.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## Architecture at a glance

```text
Capabilities
├── Standards
├── Tools
├── Tags
├── Scope
├── Dependencies
├── Migration
├── Deployment
└── Review
```

- Eight peer components.
- Standards and Tools define capability kinds and canonical production.
- Tags provides the general classification/query substrate.
- Scope uses Tags plus AI context to decide applicability.
- Dependencies resolves required identities and conformance/version state.
- Migration owns transition semantics and execution.
- Deployment consumes package payload + deployment intent and realises Deployment Sets.
- Review provides reusable independent assessment for insight, substantive integrity, better
  decisions, and risk management.
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
Capability Package + Deployment Manifest
      ↓
Deployment
      ↓
Deployment Set composition
      ↓
publish / distribute
      ↓
WorkPackage Outcome returned
```

**Core boundary:** Design side owns capability meaning. Build side owns platform realisation. A
valid package/manifest boundary lets Deployment operate mechanically without reopening Capability
Design.

---

## Tags

```text
semantic owner
  resolves/denormalises source meaning
        ↓
AIDE_TagBuilder
        ↓
flat tags
        ↓
Boolean query
```

- Tag Builders are embedded YAML definitions in owning Standards.
- Builders discover source, generate tags, and clean up only their own output.
- Generated ownership may use a prefix or an owned group `{key}:[...]`.
- Groups are invisible everywhere except to the owning builder.
- Markdown storage is compact: `Tags: tag-a, group:[tag-b, tag-c]`.
- Tags contain no whitespace; `-` or `_` may separate words.
- Query operators: `!`, `&`, `|`, `()` over exact flat tag values.
- Runtime does not traverse inheritance or reopen semantic sources.

---

## Scope

```text
Machine Scope
  → AIDE_Tags Boolean query

Context Scope
  → natural-language condition interpreted by AI
```

- Both constrain applicability when both are present.
- Machine evaluates first and can short-circuit Context.
- Missing Machine or Context means no restriction from that layer.
- No Scope means generally applicable.
- `Disabled: true` means never applicable.
- Scope returns applicability; it does not execute the behaviour.
- Platform trigger/discovery realisation belongs Build side.

---

## Dependencies

Compact document form:

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

- `abc` — normal dependency.
- `!abc` — required; check on relevant use and raise missing state prominently.
- `!!abc` — best-effort startup check and required thereafter.
- `@vN` — last proven conformance checkpoint.
- `@!vN` — exact available version required.
- Identity resolves first; version is compared second.
- Newer available version still resolves and exposes the version gap to Migration.
- Dependency Builders mirror Tag Builders and may own generated groups/prefixes.
- Dependency version advances only after applicable migration/update work succeeds.

---

## Core system primitives consumed

### Formal identity

Internal topic/source names remain simple. Published/referenceable AIDE identities use the
`AIDE_` namespace where collision is plausible.

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

First identity is primary; later entries are alternate/exposed identities. Identity matching is
by name, with version comparison handled separately.

### Bootstrap

`{bootstrap}` is a system-level discoverability marker. A small stable system instruction is
deployed to each AI environment telling it to process available bootstrap blocks at session
start on a best-effort basis and on first discovery if startup visibility was unavailable.

Dependencies uses this for `!!` checking; the primitive is reusable by other components.

---

## Document metadata ownership

Target boundary for the later DocMeth reconciliation:

```text
Documentation Methodology
  → owns generic header/footer metadata containers and placement

Block owner
  → owns its block/property content and behaviour
```

DocMeth does not need to know Tags or Dependencies specifically. `AIDE_Tags` asks for a footer
metadata property; `AIDE_Dependencies` asks for another; Identity uses header metadata.

---

## Canonical Standard / Tool and Build Config

The canonical capability contains the complete generic capability definition plus only
capability-specific platform addenda and transition declarations.

Effective Build Config declares target platforms, side (default both), and Deployment Set(s).
Platform-specific implementation mechanics remain Build-side knowledge.

---

## Package and Deployment Manifest

```text
Capability Package
  = capability-local payload

Deployment Manifest
  = machine-readable deployment intent

Package + Manifest
        ↓
Deployment
```

The Manifest carries only what Deployment demonstrates it needs: package identity/version,
Deployment Set membership, platform applicability where required, removals/replacements, and
other integrity/resumption fields only where justified.

Deployment Config resolves logical targets to physical platform destinations.

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
```

- Required Migration, On-Update, and No transition remain distinct.
- Dependencies supplies the durable conformance checkpoint and version gap.
- `/migrations-check`, `/migrations-apply`, and `/update-doc` remain the logical runtime tools.

---

## Review

```text
Trigger
  ↓
Review Input Contract
  ↓
Type + Level + Mode + Reviewer
  ↓
purpose-shaped request
  ↓
external communication route
  ↓
correlated response / Lead disposition / re-review
  ↓
Review Result
```

- The Lead owns the work, authorised scope, net coherence, and disposition.
- The Reviewer owns Findings as evidence, not instructions.
- Types are Check, Inspect, Evaluate, Robust, and user-activated Stress Test.
- Default Levels are Low, Standard, Medium, High, and Extreme respectively.
- Level follows consequence, reach, reversibility, and uncertainty and may change during Review.
- Mode is Full or Blind; Blind reduces anchoring without withholding required information.
- Each append-only Round records the actual Lead and Reviewer models, request/material, unchanged
  response, outcome, disposition, changes, and continuation reason.
- Higher Levels increase evidence, independence, persistence, completion confidence, and re-review
  of substantive changes; there is no fixed Round cap.
- Review may discover beyond authorised scope, but current execution cannot expand to address it.
- Review evidence may live in a surrounding work record or a durable Documentation Methodology
  Review document according to consequence and value.
- Review owns exchange semantics/state. Environment configuration supplies current reviewer/model/
  route facts; shared communication supplies direct or AI Message-based transport.

Detailed contract: `Capabilities_Review_Design` v1, `AIDE_Review@v1`,
`AIDE_ReviewProfiles@v1`, and `Capabilities_Review_Tool_Design` v1.

---

## Current sequence

1. **Migration** — formal child design and production standard.
2. **Standards reconciliation.**
3. **Tools reconciliation.**
4. **Remaining identity/version + Package/Manifest contract details.**
5. **Deployment** — complete last-ish from the stable upstream boundary.
6. **Platform evidence/build/deployment standards** as needed/parallel.
7. **Review environment/communication ownership handoff** with the owning workstreams.
8. **Documentation Methodology review** later using the accumulated handoff items.

WorkPackage remains a separate AIDE Build workstream.

---

**Depends on:** `Capabilities_Brief` v4, `Capabilities_Design` v5,
`Capabilities_Decisions` v11.

**References:** `Core_System_Design` v3, `Capabilities_Tags_Design` v1,
`Capabilities_Scope_Design` v1, `Capabilities_Dependencies_Design` v1,
`Capabilities_Review_Design` v1, `AIDE_Review@v1`,
`AIDE_ReviewProfiles@v1`, `Capabilities_Review_Tool_Design` v1.

**Methodology:** v17
