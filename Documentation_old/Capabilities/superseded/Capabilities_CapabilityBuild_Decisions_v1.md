
# Capabilities Capability Build — Decisions

> **Version 1** (2026-09-02). Records the specialised Build and Package decisions.

## D1 — Capability Build is Capabilities-owned specialisation

Generic Build supplies the framework; Capabilities supplies domain rules and executor.

## D2 — Package completeness is external

Incremental/cached/reused implementation is allowed internally; every successful selected-platform
output is complete externally.

## D3 — Force build changes Package identity, not semantic release

PackageId/integrity records a rebuilt instance without lying about Element/Capability meaning.

## D4 — Registry contract remains open

Active AI Deployment WIP owns the final register/publish seam. Preserve an explicit handoff, not an
invented schema.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_CapabilityBuild_Design_v1, Capabilities_Decisions_v17
