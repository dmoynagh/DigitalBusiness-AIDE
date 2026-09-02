# Capabilities Tools — Brief

> **Version 6** (2026-09-02). Advances Build Capability and Capability Builder for Build Target Profile execution.

---

## Purpose

Tools owns the reusable model for invokable AI capability behaviour: how a Tool defines its
identity/actions, inputs, preconditions, procedure, bounded decisions, escalation, outputs,
reporting, failure handling, and idempotency.

A Tool removes the need to re-derive a repeatable action each time. It may orchestrate bounded
judgment explicitly defined by its contract, but does not silently take substantive authority that
belongs to the work owner or another capability.

## Output

Tools publishes `AIDE_ToolsProduction@v2`, the canonical production contract used by domains and
Build Capability to produce/validate individual canonical Tools from confirmed Tool/Capability
Design. Platform Build Standards/Tools turn logical actions into target-specific skills, commands,
UI actions, scripts, or other representations.

## Required relationships

A Tool:

- declares applicability through `AIDE_Scope`;
- may declare dependencies through `AIDE_Dependencies`;
- may carry `AIDE_Migration` transition declarations where its release changes durable consumer
  state/configuration/contract;
- defines logical actions independently of their platform rendering; and
- reports what it did, what changed, and what needs attention.

## Boundaries

Tools does not own Scope, Tags, Dependencies, Migration, Review, Deployment, WorkPackage, or generic
platform implementation.

A Standard may describe procedure; a named invokable action is a Tool.

## Success signals

- A Tool can be invoked without re-deriving its mechanism.
- Inputs and decision/escalation boundaries are explicit.
- Re-running behaviour is known.
- Platform implementations preserve one logical action contract despite different command/skill
  representations.
- Durable release transitions are handled through the shared Migration contract rather than a
  Tool-specific version mechanism.


## Current Tool set

Element update, Build request orchestration and Build-side execution are separate current Tools
under `Capabilities_Tools_Definition_v3`; Registry publication remains an AI-Deployment-owned
post-Build action.

---
Dependencies: !AIDE_DocumentationMethodology@v27, Capabilities_Design_v14, Capabilities_Tools_Design_v6
References: Capabilities_Brief_v13, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
