# Capabilities Standards — Brief

> **Version 1** (2026-08-27). First issuance. Establishes the Standards subtopic within
> Capabilities, scoping what it owns and what it delegates.
>
> Created: 2026-08-27 | Last modified: 2026-08-27

---

## Purpose

The Standards subtopic owns how standards are defined, structured, produced, and published. It
does not own individual standards produced by other domains — those domains own their own
capability content; this subtopic provides the governing model they follow.

---

## What Standards produces

**The Standards Standard** — the standard governing standards production. This is its primary
output: the authoritative rules for how any standard is authored, weighted, structured, and
published.

**Guides** — an optional output, not produced by default. Whether a guide accompanies a given
standard is declared in that standard's brief. The default (no guide) is held in the Standards
Standard and is flippable later.

---

## Key mechanisms

**Standard blocks** — a first-class inclusion mechanism allowing other domains to contribute
sealed content into another domain's standard. A standardblock carries its own weights and
versions; the authoring domain owns the content, the publishing domain owns inclusion and
currency.

---

## Cross-topic dependency

Runtime rules for operating under standards — conflict resolution, deviation handling, how a
session honours weights — belong in the AIDE standard, not here. This subtopic contributes
content to the AIDE standard via a standard block containing the runtime conflict hierarchy,
deviation handling, and weight-honouring rules.

---

## What Standards does not own

- **Individual standards** produced by other domains — those domains own their content.
- **Runtime application of standards** — how a session resolves conflicts and handles deviation
  belongs in the AIDE standard.
- **Document types** — defined and managed by DocMeth.

---

**Depends on:** `Capabilities_Design` v1, `Capabilities_Standards_Design` v1.

**References:** `Capabilities_Brief` v1.

**Methodology:** v17
