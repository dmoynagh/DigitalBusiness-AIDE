# Capabilities Standards — Brief

> **Version 4** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Standards.
>
> Created: 2026-08-27 | Last modified: 2026-09-02

---

## Purpose

Standards owns the reusable model for what an AI-facing Standard is, how its rules are structured
and weighted, how a canonical Standard is produced from confirmed design, and how sessions operate
under applicable Standards.

Individual domains own the substance of the Standards they produce.

## Outputs

Standards defines and ultimately publishes two generic outcomes:

- **Standards Production Standard** — authoring/structure/weight/canonical-production rules.
- **Standards Usage Standard** — discovery, interpretation, conflict/deviation, and operation under
  applicable Standards.

A domain may also produce an optional human Guide from the same design where useful.

## Required relationships

A canonical Standard:

- declares applicability through `AIDE_Scope`;
- declares dependencies through `AIDE_Dependencies`;
- declares version transition intent under `AIDE_Migration`;
- may contribute Tag/Dependency Builders where it owns the source semantics;
- uses Review where independent assessment adds value; and
- carries only capability-specific platform addenda. Generic platform implementation belongs Build
  side.

## Boundaries

Standards does not own Tags, Scope, Dependencies, Migration, Deployment, Review, WorkPackage, or
platform skill/plugin/bundle mechanics.

A Standard may describe a procedure but does not define a named invokable action; that is a Tool.

## Success signals

- A Standard author can produce one clear canonical Standard without inventing shared mechanisms.
- An extracted/chunked rule still carries its obligation weight and enough context to be used
  correctly.
- Platform builders can realise the same canonical Standard without reopening Capability Design.
- Runtime consumers can combine applicable Standards and surface genuine conflict/deviation rather
  than silently resolving it.
- A substantial Standard can be understood and navigated from a concise semantic Contents/Summary
  entry without duplicating or cluttering small/self-evident outcomes.


## Current Definition

`Capabilities_Standards_Definition_v3` is the required capability-level control document; production uses `AIDE_StandardsProduction@v4`.

---

**Depends on:** `Capabilities_Design_v14`, `Capabilities_Standards_Design_v8`.

**References:** `Capabilities_Brief_v11`, `AIDE_Scope@v2`, `AIDE_Dependencies@v3`,
`AIDE_Migration@v3`.

**Methodology:** v28
