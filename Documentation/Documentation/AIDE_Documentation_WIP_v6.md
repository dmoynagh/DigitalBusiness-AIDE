AIDE Documentation | WIP | AIDE_Documentation_WIP@v6 | 2026-09-14

## Active threads

### DocMeth — uses migration

The DocMeth clean-sheet rebuild (2026-09-14) replaced three v4 standards with three v1 standards under new identities. Standards that declared `uses` referencing the old identities need updating:

| Old identity | New identity |
|---|---|
| DocumentationMethodology_Schema_Standard@v4 | DocumentationMethodology_SchemaAuthoring_Standard@v1 |
| DocumentationMethodology_Definitions_Standard@v4 | DocumentationMethodology_SchemaDefinitions_Standard@v1 |
| DocumentationMethodology_Authoring_Standard@v4 | DocumentationMethodology_Standard@v1 (universal — remove from uses) |

Known affected standards: Standards_Authoring_Standard, PD_Schema_Standard, Core_Schema_Standard.

The main DocumentationMethodology_Standard is now universal and exempt from `uses`. Any standard that listed Authoring Standard v4 should remove that entry.

**Cross-review required:** no — mechanical identity update.

### DocMeth — schema review across components

All components owning doctypes or block types must define them using the accepted definition contract. The definition contract has been simplified in the rebuild (6 blocktype properties, 4 doctype properties). Assessment produced (DocMeth_Schema_Review_v1) — rework is a separate task per component.

Note: existing component schema standards (PD_Schema_Standard_v1, Core_Schema_Standard_v1) were authored against the old Schema Standard v4 property vocabulary. They should be reviewed against the simplified contract in DocumentationMethodology_SchemaAuthoring_Standard_v1 when next worked.

### DocMeth — binder rebuild

The DocMeth binder needs rebuilding with the new v1 standards replacing the old v4 standards, plus updated decisions (v7) and working (v9) documents.

---

## Pending — Project Design

### PD standard update — design-approach content

PD's standard (v3) was authored before the design-approach content was formally placed. The following need folding in when PD's standard is next updated:

- **Brief-required gate.** Brief required before any design starts, override must be explicit. Already settled methodology — making the override-only exception explicit in the standard.
- **Operations test.** For every significant objective, determine what a consumer must be able to do when the objective is met. Test whether the design specifies enough for that operation to be performed deterministically. If the consumer has to invent a convention, the design is incomplete.
- **Black-box acceptance test.** Before accepting a standard, test: given only this standard, can a fresh AI perform the representative operations covered by the applicability statement? If it cannot, the standard fails the self-containment rule and must not be published.
- **The layering model, context rule, overview role, derive-from-model** per the placement plan in the design-approach WIP.
- **Difficulty-as-evidence** in the commitment-and-return section.
- **Check 1 and Check 2** as application-time discriminating guidance.

**Deployment output:** the aide-design-check skill is regenerated from the updated PD standard. It stops being an independently authored interim document.

**Cross-review required:** yes — the PD standard update is substantive and adds new gates that downstream components are built against.

### PD standard update — brief rule

Add to the standard: a design almost always has a brief (standalone or inline). Design without a brief is the exception and requires explicit override.

**Cross-review required:** included in the PD standard update above.

### PD carries from DocMeth

Three carries from the DocMeth design to PD:

- **PD-F1 — Design two-part structure.** The design doctype has two recognised parts: the approach (tested by Check 1) and the detailed design (tested by Check 2).
- **PD-F2 — Doctype definitions needed.** All components owning doctypes must define them using the definition contract.
- **PD-F3 — Schema placement guidance.** PD's standard should reference DocMeth's schema placement guidance when advising components on their document sets.

**Cross-review required:** included in the PD standard update.

---

## Pending — Principles

### Three candidate premise strengthenings

From the design-approach work. These are not new premises — they would strengthen existing ones. To be considered when Principles is next worked:

1. **Difficulty-as-evidence.** If something is becoming hard or elaborate, the model above it may need review. May strengthen P3.
2. **Do not build apparatus.** A clear principle is applied, not implemented through stages, phases, or machinery. May strengthen P3 or stand alongside it.
3. **Simple and well-conceived is the goal.** Output markedly more elaborate than the intent above it is a warning. May strengthen P4.

**Cross-review required:** yes, if any premises are strengthened.

---

## Pending — Standards

### Standard design approach — two classes by load pattern — DONE

Captured in Standards_Design_v3 (two-class distinction and solving-model design sequence), Standards_Decisions_v3 (D15–D19), and Standards_Authoring_Standard_v6 (authoring rules, design guidance, default-Required strength model). DocMeth clean-sheet rebuild is the worked example.

**Cross-review required:** yes — substantive additions to the design and standard (new authoring rules, design approach, strength model change).

### Clarification block

The standard doctype has two parts: the standard itself (lean, stated rules) and clarification (reasoning, justification). Two blocks, joined when small, split by the split test when clarification would bloat the loaded standard. Carry from DocMeth.

---

## Pending — Core

### Component alias uniqueness

Component names and aliases must be unique within the framework. Aliases are used as type-reference prefixes in the dot-qualified naming grammar (`pd.brief`). Core Structure owns this rule.

---

## Pending — Working Practices

### Overview-first working behaviour

The discipline of staying at the overview level until it could drive excellent execution, probing rather than diving, is broader than design. PD owns the design-specific application; WP owns the generic working behaviour when WP is built.

### `/more` command

AI-presented prompts should be concise by default. The `/more` command expands the current prompt with additional detail. Belongs alongside the session-transition commands when those are designed.

### Items accumulated for WP from other passes

- Pending content rule ownership
- Session-transition commands (full stop, checkpoint-and-continue, flush without closing)
- No-knowledge-lost rule and the three behaviours
- Capture-and-place rules (the four methodology rules from the Core shaping session)
- Definition of done as a generic block (owned by WP, invariant: testable or assessable)
- Work item as the base workflow entity
- Human working model standard (tiering, confidence, assumptions report, drift detection)

---

## Pending — Infrastructure

### FUP manifest — `user_instructions` field clarification

The `user_instructions` field is only for tasks the user must do outside the AI platform. All client-side instructions are presented in chat alongside the FUP. Carry to the FUP design document.

### FUP deployer — user_instructions display order

The `user_instructions` message should display after the deploy success statement, not before the deploy prompt. Log for Code session.

---

## Pending — Submission queue (component ownership TBD)

### Frictionless capture path — work to AIDE development

AIDE needs a mechanism for submitting learnings, additions, changes and new functionality from work sessions into an AIDE development queue. The charter's frictionless capture principle governs the design.

**Concept.** Work side: single action on any surface, no triage required. AIDE development side: queue reviewed, triaged, worked through the normal design-build-deploy cycle.

**Preferred mechanism.** An MCP server callable from any AI surface, writing to a queue document in the AIDE git repo.

**Component ownership.** Not yet allocated. To be decided when design starts.

---

## Standards Dependency Map

How standards depend on each other via declared `uses` relationships. Updated for the DocMeth rebuild.

```
Tier 0 — Foundation (no declared uses)
│
├── DocumentationMethodology_Standard_v1 ★    universal, exempt from uses
│
├── DocumentationMethodology_SchemaAuthoring_Standard_v1    no declared uses
│   │
│   └── DocumentationMethodology_SchemaDefinitions_Standard_v1 ★
│
└── Standards_Authoring_Standard_v5 ★         pending uses update
    │
    │   Tier 1
    │
    ├── Standards_Consumption_Standard_v2
    │
    ├── Tools_Authoring_Standard_v4
    │
    ├── Core_Schema_Standard_v1 (provisional)  pending uses update
    │
    └── PD_Schema_Standard_v1                  pending uses update
        │
        └── PD_Standard_v3
```

★ = universal or always-on dependency

**Pending:** Standards_Authoring_Standard, PD_Schema_Standard, and Core_Schema_Standard need `uses` updated to reference new DocMeth identities.

---

## Cross-review register

| Item | Reason | Status |
|---|---|---|
| DocMeth clean-sheet rebuild (three v1 standards) | Full rework of DocMeth standards | **Accepted** — two rounds, all findings resolved. Published 2026-09-14 |
| Standards design approach update (Design v3, Decisions v3, Authoring Standard v6) | New design approach, three new authoring rules, strength model change | Pending — documents drafted, cross-review not started |
| PD Standard update (design-approach + brief gate + operations/acceptance tests) | New gates that downstream work is built against | Pending — update not started |
| Principles premise strengthening | Foundational — changes propagate to all components | Pending — not started |

---

Version note: v6 — Standards design approach implemented: Design v3, Decisions v3 (D15–D19), Authoring Standard v6. Pending item marked done, cross-review registered. 2026-09-14. Replaces v5.
