> identity: Core_AIDEMap@v2 | updated: 2026-09-15

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
│   ├── Principles — nine portable premises, any AI can adopt without adopting AIDE
│   ├── Standards — definition of a standard, authoring rules, leanness, strength model
│   ├── Tools — definition of a tool, authoring concerns, invocability test
│   ├── Assurance — trust conventions, human working model, verification, drift detection, learning capture
│   └── Improvement — pattern analysis of learnings queue, escalation decisions (identified, not yet scoped)
│
├── Work
│   ├── Working Practices (WP)
│   │   ├── Working State — WIP model, work items, work plan, pending content, development lifecycle
│   │   └── Content Delivery — binder concept, inclusion rules, context loading
│   ├── Project Design (PD) — design specification, design-build loop, work register
│   └── Build — execute the spec, report what was done, own code structure
│
├── Delivery
│   ├── Orchestration — transport, routing, work packages, verification, capability profiles
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

Version note: v2 — Assurance and Improvement added under Guidance; WP subtree updated to reflect WP_Design_v2 areas (Working State and Content Delivery replace the five pre-design-pass areas). 2026-09-15. Replaces v1.
