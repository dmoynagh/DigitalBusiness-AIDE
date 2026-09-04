# Capabilities — Open Items

> **Version 15** (2026-08-31). Converts the register to live-only v21 semantics, removes resolved
> and rehomed history, and leaves only unresolved items whose future attention still matters to
> Capabilities.
>
> Created: 2026-08-27 | Last modified: 2026-08-31

## Q9 — Build Config inheritance/defaults

**Status:** Open — detail, not a current blocker

Confirmed fields remain platforms, side (default both), and Deployment Set(s). Resolve inheritance/
overrides when Environment/Deployment configuration is designed and evidence demonstrates the
need.

## Q12 — Environment settings home consumed by Review

**Status:** Open — external dependency

Resolve storage/inheritance for available AI families/models/capabilities/routes/fallbacks,
preferences and access/usage/cost constraints in the owning Environment/platform work. Review and
other Capabilities consumers should reference that state rather than owning it.

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: Capabilities_WorkRegister_v13, Capabilities_Design_v8
