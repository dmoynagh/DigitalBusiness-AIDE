> identity: Core_AIDEMap@v3 | updated: 2026-09-17

# AIDE Map

Structural overview of the AIDE framework. Scan to see the whole shape; use for placement decisions. Updated when the component map changes.

```
AIDE
├── Foundation
│   ├── Core
│   │   ├── Structure — folders, paths, index, container labels, three-tier file model
│   │   └── AIDEPrinciples — facilitate-and-extend, opt-in, strength model, aliases
│   ├── Documentation Methodology (DocMeth) — doctypes, block types, declarations, definition contract
│   └── Messaging — envelope format, addressing, acknowledgment conventions
│
├── Guidance
│   ├── Capabilities — base development methodology for all capability types
│   ├── Principles — nine portable premises, any AI can adopt without adopting AIDE
│   ├── Standards — definition of a standard, authoring rules, leanness, strength model
│   ├── Tools — definition of a tool, authoring concerns, invocability test
│   ├── Services — definition of a service, authoring concerns, boundary tests
│   ├── Assurance — trust conventions, human working model, verification, drift detection, learning capture
│   └── Improvement — pattern analysis of learnings queue, escalation decisions (identified, not yet scoped)
│
├── Work
│   ├── Working Practices (WP)
│   │   ├── Working State — WIP model, work items, boards, pending content, development lifecycle
│   │   └── Content Delivery — binder concept, inclusion rules, context loading
│   ├── Project Design (PD) — design specification, design-build loop, work register
│   └── Build — execute the spec, report what was done, own code structure
│
├── Delivery
│   ├── Orchestration — dispatch correlation, invocation, target adapters, model-level resolution
│   ├── Migration — change detection, distribution, execution
│   ├── Deployment — build plugin, push to marketplace, weight gate
│   └── Infrastructure — CLI, deployment utilities, settings merge
│
├── Held
│   ├── Tags — awaiting a demonstrated consumer
│   └── Scope — awaiting runtime applicability need
│
└── Charter — founding rationale, objectives, development principles, decision test
```

---

Version note: v4 — Capabilities and Services added to Guidance role. Component count 15 → 17. Utilities identified but not yet created as a component. 2026-09-23. Replaces v3.
