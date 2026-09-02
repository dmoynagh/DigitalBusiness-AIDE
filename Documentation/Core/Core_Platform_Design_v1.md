
# Core Platform / Working Surface — Design

> **Version 1** (2026-09-02). Establishes the evidence-led generic Working Surface fact model.

## Purpose

Provide reusable factual platform/surface information to Working Practices, Capability Build and AI
Deployment without hard-coding product roles or conflating support with deployed state.

## Minimal model

For a named surface, record only evidenced facts needed by a current consumer. Candidate dimensions
include file read/write, repository access, semantic/project retrieval, voice/mobile access, shell
execution, artefact editing, persistent instruction support, Skill/Plugin or equivalent support,
source/context limits and supported deployment mechanisms.

Each fact should carry a point-in-time evidence reference where volatility matters. `Unknown` is
valid. A surface may list multiple deployment mechanisms.

## Boundaries

- actual installed/deployed/current AIDE capability state is environment/deployment state;
- Capability-specific platform rules belong to the Capability owner;
- AI Deployment owns target/configuration and deployment-state mechanics;
- security, permissions and filesystem authority are not inferred from technical reach; and
- no universal large schema or canonical Standard is issued in this pass.

## Consumption rule

Consumers resolve the required fact at the time of use, surface missing/unknown material facts, and
do not substitute product reputation or an untested possibility for evidence.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Core_System_Design_v10, Core_Knowledge_v1
