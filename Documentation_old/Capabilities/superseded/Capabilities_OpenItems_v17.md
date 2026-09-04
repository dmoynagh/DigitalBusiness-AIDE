
# Capabilities — Open Items

> **Version 17** (2026-09-03). Carries the non-blocking Review D R2 Build-selection observation and four next-natural-revision clarifications.

## Q9 — Platform Definition resolution/defaults

**Status:** Open — detail, not a current blocker

Resolve inheritance/override rules for generic Platform facts/Profiles and Capability-specific
Platform Definition only when real multi-level evidence requires them. Current minimum remains
resolved factual `Supported`, designer-owned tri-state `Build`, and optional non-semantic Notes.

**Review D R2 carry (C5).** The architecture correctly blocks Capability Build until at least one
explicit `Build:true` resolves, but no current Capability presently asserts one and no current
contract names the operational owner/step that supplies that designer selection. Preserve this as
non-blocking operational work until the real build-selection workflow is exercised; do not invent a
new selection mechanism merely to close the observation.

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
