# Capabilities Standards — Brief

> **Version 3** (2026-09-02). Adds the Standards Capability Definition and Element-release production boundary.
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


## Current Definition

`Capabilities_Standards_Definition_v1` is the required capability-level control document; production uses `AIDE_StandardsProduction@v3`.

---

**Depends on:** `Capabilities_Design_v12`, `Capabilities_Standards_Design_v7`.

**References:** `Capabilities_Brief_v11`, `AIDE_Scope@v2`, `AIDE_Dependencies@v3`,
`AIDE_Migration@v2`.

**Methodology:** v27
