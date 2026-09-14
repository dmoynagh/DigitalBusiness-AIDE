AIDE Documentation | WIP | AIDE_Documentation_WIP@v13 | 2026-09-15

## Active threads

### DocMeth — schema review across components

All components owning doctypes or block types must define them using the accepted definition contract. The definition contract has been simplified in the rebuild (6 blocktype properties, 4 doctype properties). Assessment produced (DocMeth_Schema_Review_v1) — rework is a separate task per component.

Note: PD_Schema_Standard_v1 was authored against the old Schema Standard v4 property vocabulary. It should be reviewed against the simplified contract in DocumentationMethodology_SchemaAuthoring_Standard_v1 when next worked. Core_Schema_Standard_v2 is provisional and will be reviewed when Core's design pass is done.

---

## Completed — Project Design

### PD standard update — design-approach content — DONE

PD Standard v4 deployed 2026-09-14. Design-approach content folded in: two-part design structure (PD-F1), approach completeness check and element quality check as application-time guidance, operations test, context rule and derive-from-model, difficulty-as-evidence in the commitment-and-return loop. Brief-required gate made explicit with override. Overview section strengthened. DocMeth definition-contract and schema-placement pointers added (PD-F2, PD-F3). aide-design-check skill regenerated from the updated standard.

Cross-reviewed — ten findings, all resolved. PD Design v3, Decisions v3, Standard v4 all accepted.

### PD standard update — brief rule — DONE

Included in PD Standard v4 above.

---

## Completed — Principles

### Principles premise strengthenings — DONE

Completed 2026-09-15. Three candidate premise strengthenings from the design-approach work, all resolved as strengthenings of existing premises per F12 pattern. Premise count stays at nine.

P3 (model before elaboration) strengthened: difficulty-as-evidence feedback signal and apparatus-avoidance failure mode (D10). P4 (keep the working set human-comprehensible) strengthened: proportionality signal (D11).

Cross-review: F1 remediated (false-exclusive removed from difficulty signal), F2 remediated (positive injunction → naming the form), F3 remediated (universal causation → warning signal). Deployed: Principles_Design v5, Principles_Decisions v5, Principles_Standard v2.

---

## Completed — Standards

### Clarification block — DONE

Carry from DocMeth resolved by existing definition. The Standards Authoring Standard (v8 schema definitions section) already defines the Clarification blocktype — purpose, recognition, and split test governance — and includes it as optional in the Standard doctype. Definition-contract compliant. No design work needed. 2026-09-15.

---

## Completed — Documentation Methodology

### DocMeth — binder rebuild — DONE

Three superseded draft standards removed from the binder. The naming convention changed between drafts (`DocMeth_` prefix) and published v1 standards (`DocumentationMethodology_` prefix), so version cleanup didn't catch them. Files moved to `_superseded/`, binder rebuilt v64 → v65. Commit `f040d4b`. 2026-09-15.

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

How standards depend on each other via declared `uses` relationships. Current as of binder v65.

```
Tier 0 — Foundation (no declared uses)
│
├── DocumentationMethodology_Standard_v1 ★    universal, exempt from uses
│
├── Principles_Standard_v2    no declared uses
│
├── DocumentationMethodology_SchemaAuthoring_Standard_v1    no declared uses
│   │
│   ├── DocumentationMethodology_SchemaDefinitions_Standard_v1 ★
│   │
│   ├── Core_Schema_Standard_v2 (provisional)
│   │
│   └── PD_Schema_Standard_v1
│       │
│       └── PD_Standard_v4
│
└── Standards_Authoring_Standard_v8 ★
    │
    │   Tier 1
    │
    ├── Standards_Consumption_Standard_v3
    │
    └── Tools_Authoring_Standard_v8
```

★ = universal or always-on dependency

---

## Completed items (this session)

### DocMeth — uses migration — DONE

All three affected standards updated to reference new DocMeth v1 identities. Standards_Authoring_Standard_v7, PD_Schema_Standard_v1, and Core_Schema_Standard_v2 all current.

### Standard design approach — two classes by load pattern — DONE

Captured in Standards_Design_v3, Standards_Decisions_v3 (D15–D19), and Standards_Authoring_Standard_v7 (authoring rules, design guidance, default-Required strength model, acceptance test). DocMeth clean-sheet rebuild is the worked example. Cross-reviewed and accepted.

### Standards review batch — DONE

Six standards reviewed against the full methodology (no-consumer-no-rule, earn-your-place, name-your-principles, operations test, acceptance test, task-vs-carried classification). Findings:

- **Tools Authoring Standard v4 → v7** (substantive): authoring rules reference updated from a named list of five to the full capability-wide set. Explicit incorporation contract, applicability section, acceptance test, noun-substitution rule, scope narrowed to deployment handoff, trigger made generic, sibling-outputs corrected. Three cross-review rounds, ten findings across rounds 1–2 all resolved, round 3 finding (acceptance-test ambient-context wording) accepted as a Standards carry. Tools Decisions v4 → v7, Tools Design v3 → v6 updated alongside.
- **Core Schema Standard v1 → v2** (minor): Tags block type removed per no-consumer-no-rule; `uses` updated.
- **Standards Consumption Standard v2 → v3** (minor): `uses` updated to Standards_Authoring_Standard@v7.
- **Principles Standard v1, PD Schema Standard v1, PD Standard v4**: clean — no changes needed.

### Standards acceptance-test ambient-context fix — DONE

Completed 2026-09-15. Acceptance test amended for ambient framework context (D21). Cross-review: two defects remediated (F1 definition added, F2 "guaranteed" replaces "available within scope"), one concern accepted (F3 Tools sync included). Deployed: Standards_Authoring_Standard v8, Standards_Decisions v4, Tools_Authoring_Standard v8.

---

## Cross-review register

| Item | Reason | Status |
|---|---|---|
| DocMeth clean-sheet rebuild (three v1 standards) | Full rework of DocMeth standards | **Accepted** — two rounds, all findings resolved. Published 2026-09-14 |
| Standards design approach update (Design v3, Decisions v3, Authoring Standard v7) | New design approach, three new authoring rules, strength model change, acceptance test | **Accepted** — two rounds, all findings resolved. Published 2026-09-14 |
| PD Standard update (Design v3, Decisions v3, Standard v4) | Design-approach content, new gates, brief rule | **Accepted** — ten findings, all resolved. Published 2026-09-14 |
| Tools Authoring Standard v7 (Design v6, Decisions v7) | Authoring rules reference, incorporation contract, scope | **Accepted** — three rounds (10 findings resolved, 1 carried to Standards). Published 2026-09-14 |
| Principles premise strengthenings (P3, P4) | Three candidate strengthenings from design-approach work (F12 pattern) | **Accepted** — F1 remediated (false-exclusive), F2 remediated (D10 wording), F3 remediated (D11 wording). Published 2026-09-15 |
| Standards acceptance-test wording (ambient context) | Framework-contract issue exposed by Tools cross-review | **Accepted** — F1 defect (definition), F2 defect (guaranteed wording), F3 concern (Tools sync) — all remediated. Published 2026-09-15 |

---

Version note: v13 — Clarification block carry closed (existing definition resolves it). DocMeth binder rebuilt v64 → v65 (three superseded draft standards removed, commit f040d4b). 2026-09-15. Replaces v12.
