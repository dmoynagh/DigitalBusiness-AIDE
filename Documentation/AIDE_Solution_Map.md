# AIDE Solution Map

Snapshot of the AIDE framework: components in dependency order, documents under each.
Generated 2026-09-14 from Binder v42 and Documentation WIP v2.

Status key: ✅ complete · 🔧 rework needed · 📋 designed, not yet built · ⏳ not started

---

## 1. Principles ✅ (standard pending)

Durable, portable reasoning premises — independent of platform or methodology. Any AI can adopt these without adopting AIDE.

**Design and decisions**
- Principles_Design_v4.md
- Principles_Decisions_v4.md

**Pending:** standard not yet authored (was blocked on the Standards component, now unblocked). Three candidate premise strengthenings queued (difficulty-as-evidence, do-not-build-apparatus, simple-and-well-conceived). Cross-review required.

---

## 2. Core 📋

Shared framework-wide requirements, self-description, component model, and entry point. Deferred by design — resolved last.

**Standards**
- Core_Schema_Standard_v1.md (provisional)

**Design and decisions — AIDE Principles (Core-specific)**
- Core_AIDEPrinciples_Design_v1.md
- Core_AIDEPrinciples_Decisions_v1.md
- Core_Brief_v1.md

**Design and decisions — Structure**
- Core_Structure_Design_v1.md
- Core_Structure_Decisions_v1.md

**Working documents**
- Core_Working_v1.md
- Core_Design_Documentation_Working_v1.md
- Core_Tags_Working_v1.md

**Reference**
- Core_AIDEMap.md / Core_AIDEMap.yaml
- _index.md

---

## 3. Documentation Methodology 🔧

How documents are structured and created — the grammar. Owns doctypes, block types, declarations, lifecycle, format rules.

**Standards**
- DocumentationMethodology_Authoring_Standard_v4.md
- DocumentationMethodology_Definitions_Standard_v4.md
- DocumentationMethodology_Schema_Standard_v4.md

**Design, decisions, and brief**
- DocMeth_Brief_v1.md
- DocMeth_Design_v6.md
- DocMeth_Decisions_v6.md

**Working documents**
- DocMeth_Working_v8.md

**Reference**
- _index.md

**Rework needed:** cross-review found a definition-contract gap — design describes the model but doesn't specify the grammar for defining instances. Standard fails self-containment. Reopen design with inline brief, reauthor standard, cross-review again.

---

## 4. Standards ✅

How standards are authored, applied, honoured, and kept current. Owns the definition of a standard, authoring rules, strength model.

**Standards**
- Standards_Authoring_Standard_v5.md
- Standards_Consumption_Standard_v2.md

**Design and decisions**
- Standards_Design_v2.md
- Standards_Decisions_v2.md

**Working documents**
- Standards_Working_v1.md

**Reference**
- _index.md

---

## 5. Tools ✅

Encapsulate repeatable, named, invokable actions. Owns the definition of a tool; individual tools live with their consuming component.

**Standards**
- Tools_Authoring_Standard_v4.md

**Design and decisions**
- Tools_Design_v3.md
- Tools_Decisions_v4.md

**Reference**
- _index.md

---

## 6. Infrastructure ✅

Methodological infrastructure — CLI, deployment utilities, settings merge.

**Design and decisions — CLI**
- Infrastructure_CLI_Design_v1.md
- Infrastructure_CLI_Decisions_v1.md

**Working documents**
- Infrastructure_Working_v1.md

**Utilities**

*Binder Builder*
- BinderBuilder_Design_v10.md
- binder_builder_Documentation_settings.json
- README.md

*File Update Package (FUP)*
- FileUpdatePackage_Design_v1.md
- file_update_package_settings.json
- README.md

*Version Cleanup*
- VersionCleanup_Design_v3.md
- version_cleanup_settings.json
- README.md

**Reference**
- _index.md

---

## 7. Working Practices ⏳ (working docs only)

Conventions and behaviours for how an AI and user actually work together. Five parts: FileOps, WorkManagement, Capture, ContentDelivery, HumanAI.

**Working documents**
- WP_FileOps_Working_v1.md (FileOps/)
- WP_WorkManagement_Working_v1.md
- WP_Capture_Working_v1.md
- WP_ContentDelivery_Working_v1.md

**Reference**
- _index.md

**Not yet designed.** Accumulated items queued: pending-content rule, session-transition commands, no-knowledge-lost rule, capture-and-place rules, definition-of-done (generic block, WP-owned), work item, human working model standard, overview-first working behaviour, `/more` command.

---

## 8. Project Design ✅

Produce design specifications. Owns both ends of the design-build loop: handoff, return, reconciliation, and the work register.

**Standards**
- ProjectDesign_Schema_Standard_v1.md
- ProjectDesign_Standard_v3.md

**Design and decisions**
- ProjectDesign_Design_v2.md
- ProjectDesign_Decisions_v2.md

**Reference**
- _index.md

**Pending:** standard update to fold in design-approach content (brief gate, operations test, black-box acceptance test, layering model, difficulty-as-evidence, Check 1/2). Cross-review required. aide-design-check skill regenerated from the updated standard.

---

## Components without documents yet

| Component | Role | Status |
|---|---|---|
| Build (5) | Take the design specification and execute it — produce the outcome, report what was done | ⏳ Not started |
| Migration (8) | Keep things current when dependencies change — collate, distribute, and execute change actions | ⏳ Not started |
| Messaging (9) | Carry a message across any boundary reliably, with a known envelope and delivery convention | ⏳ Not started |
| External AI (10) | Bring another AI into your work — five modes: review, research, parallel solutioning, consultation, delegation | ⏳ Not started |
| Deployment (11) | Get publishable capabilities live in a session. Simple pipeline: build, push, reload | ⏳ Not started |

---

## Standards Dependency Map

How standards depend on each other via declared `uses` relationships. Three universal standards (marked ★) are implicit dependencies of every standard and exempt from `uses` listings.

```
Tier 0 — Foundation (no declared uses)
│
├── DocMeth Authoring Standard v4 ★         no dependencies
│
└── DocMeth Schema Standard v4              no dependencies
    │
    ├─────────────────────────────────────────────────────────┐
    │                                                         │
Tier 1 — Depends on DocMeth Schema Standard                   │
    │                                                         │
    ├── Standards Authoring Standard v5 ★                     │
    │   │                                                     │
    │   │   Tier 2 — Depends on Tier 1                        │
    │   │                                                     │
    │   ├── Standards Consumption Standard v2                 │
    │   │                                                     │
    │   └── Tools Authoring Standard v4                       │
    │                                                         │
    ├── DocMeth Definitions Standard v4 ★                     │
    │                                                         │
    ├── Core Schema Standard v1 (provisional)                 │
    │                                                         │
    └── PD Schema Standard v1                                 │
        │                                                     │
        └── PD Standard v3  ──────────────────────────────────┘
```

**Pending standards** (not yet authored — will enter the graph when built):

| Standard | Component | Expected dependencies |
|---|---|---|
| AIDE Principles Standard | Principles | TBD |
| Principles Standard (generic) | Principles | TBD |
| WP standards | Working Practices | TBD — design not started |

**Key observations:**
- The Documentation Methodology Schema Standard is the single most depended-upon standard — four standards declare it directly, and everything downstream inherits it
- The DocMeth rework (definition-contract gap) sits at the root of the graph — changes here propagate widest
- The Standards Authoring Standard is the gateway for all component-specific authoring standards

---

## Cross-cutting — _rebuild folder

Working documents that govern the rebuild itself, not owned by a single component.

- AIDE_Component_PurposeLines_v2.md — one-line purpose and boundaries per component
- AIDE_Rebuild_Guide_v1.md — review of rebuild state with findings F1–F13
- AIDE_Rebuild_Overview_v1.md — the overview driving the rebuild
- AIDE_Rebuild_SettledDecisions_v1.md — cross-component decisions locked during the rebuild

**Project Design pending files** (staged for deployment)
- ProjectDesign_Decisions_Pending_v1.md
- ProjectDesign_Design_Pending_v1.md
- ProjectDesign_StandardInputs_Pending_v1.md
- ProjectDesign_WorkRegister_Pending_v1.md

## Active WIP files (not in binder)

- AIDE_Rebuild_WIP_v22.md — main working document (210KB, being split)
- AIDE_Documentation_WIP_v2.md — cross-component working state and cross-review register
- AIDE_DesignApproach_WIP_v1.md — design-approach placement plan across four components

---

## Cross-review register

| Item | Status |
|---|---|
| Documentation Methodology design v3 + standard v2 (definition-contract rework) | Pending — rework not started |
| Project Design standard update (design-approach + gates) | Pending — update not started |
| Principles premise strengthening | Pending — not started |

---

**Document count:** 59 files in binder · 3 WIP files outside · 5 components without documents
