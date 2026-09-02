
# Capabilities — Open Items

> **Version 16** (2026-09-02). Reconciles live-only attention with the new Build Platforms model and adds bounded platform evidence/security follow-ups.

## Q9 — Platform Definition resolution/defaults

**Status:** Open — detail, not a current blocker

Resolve inheritance/override rules for generic Platform facts/Profiles and Capability-specific
Platform Definition only when real multi-level evidence requires them. Current minimum remains
resolved factual `Supported`, designer-owned tri-state `Build`, and optional non-semantic Notes.

## Q12 — Environment settings home consumed by Review

**Status:** Open — external dependency

Resolve storage/inheritance for available AI families/models/capabilities/routes/fallbacks,
preferences and access/usage/cost constraints in the owning Environment/platform work. Review and
other consumers reference rather than own that state.

## Q13 — Platform security and local filesystem authority

**Status:** Open — reserved future architecture discussion

Define platform security boundaries, intended working-scope confinement, local filesystem read/write
reach, permissions/rights and user/agent authority. Do not infer authority from technical capability.

## Q14 — Additional platform deployment-route evidence

**Status:** Open — bounded empirical testing

Re-test newer OpenAI/other-platform routes in controlled probes. Promote only proven runtime facts to
Core Platform/Knowledge; keep UI presence and documentation possibilities distinct from execution evidence.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_WorkRegister_v18, Core_Platform_Design_v1, Core_Knowledge_v1
