
# Capabilities — Open Items

> **Version 18** (2026-09-03). Records the first exercised AIDE_Core Build-platform selection while retaining the unresolved inheritance/override detail and other open items.

## Q9 — Platform Definition resolution/defaults

**Status:** Open — detail, not a current blocker

Resolve inheritance/override rules for generic Platform facts/Profiles and Capability-specific
Platform Definition only when real multi-level evidence requires them. Current minimum remains
resolved factual `Supported`, designer-owned tri-state `Build`, and optional non-semantic Notes.

**Review D R2 carry (C5) — exercised 2026-09-03.** The first real `AIDE_Core` production run supplied the missing operational selection through direct designer/user Build instruction: build every current `AIDE_Core` member for every required Profile target. For that request, Claude, ChatGPT and OpenAI resolved `Build:true` for the Profile representations they supply. This consumes the C5 observation for the exercised path without adding a new selection mechanism. The broader inheritance/override question in this item remains open until real multi-level evidence requires it.

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

## Q15 — Review D R2 next-natural-revision clarifications

**Status:** Open — drafting/placement cleanup, not Review D blockers

Carry these four Review D R2 clarifications without reopening Review D or treating them as design
defects:

- **R2-4 — Registry Tag evidence wording:** on the next natural `AIDeployment_Registry_Design`
  revision, express the Registry obligation as checking required producer snapshot/freshness
  evidence rather than generic "stale" Tags.
- **R2-5 — Tag-freeze placement:** on the next natural `AIDE_CapabilityBuild` revision, move the
  pre-freeze Tag validation rule out of the Post-Build heading to a pre-assembly/pre-freeze location.
- **R2-6 — RequiredReach feedback emission:** on the next natural AI Deployment verification
  revision, consider one explicit sentence returning authoritative/repeated contradictory reach
  evidence to the producer/Profile owner; the current recorded Target evidence is already sufficient
  for Review D closure.
- **R2-7 — Registry Tool purge wording:** on the next natural Registry Tool revision, replace the
  residual "not a v1 action" wording with version-neutral "not a Registry Tool action" wording.

Do not issue owner documents solely for these clarifications unless they become material to active
work.

---
Dependencies: !AIDE_DocumentationMethodology@v28
References: Capabilities_WorkRegister_v21, Core_Platform_Design_v1, Core_Knowledge_v1, Capabilities_Architecture_Review_2026-09-03-4_DesignToProduction_v1
