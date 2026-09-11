AIDE Documentation | WIP | AIDE_Documentation_WIP@v3 | 2026-09-12

## Active threads

### DocMeth — standards header migration

DocMeth definition contract accepted after three cross-review rounds (14 + 9 + 4 findings, all resolved). Design v6, Decisions v6, three standards at v4 (Schema, Authoring, Definitions). The grammar is settled and the standard set passes its own black-box acceptance test.

**Remaining action:** migrate the three standards' own headers from the legacy positional format to the accepted blockquote Declaration format. Mechanical — no grammar change. Carry to Migration.

**Cross-review required:** no — unless migration introduces a substantive grammar change.

**Lesson applied:** every design pass must have a brief before design starts. Definition of done is the acceptance gate. The black-box acceptance test (can a fresh AI perform the operations from the standard alone?) is the concrete form of the definition of done for any standard.

### DocMeth — schema review across components

All components owning doctypes or block types must define them using the accepted definition contract (PD-F2). Assessment produced (DocMeth_Schema_Review_v1). Rework is a separate task per component, each producing a schema standard. Recommended priority: DocMeth (done), then PD, Standards, Core, WP.

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

Add to the standard: a design almost always has a brief (standalone or inline). Design without a brief is the exception and requires explicit override. This strengthens the existing "brief is mandatory, always" position by making it an explicit gate rather than an implicit assumption.

**Cross-review required:** included in the PD standard update above — one review covers both.

### PD carries from DocMeth

Three carries from the DocMeth design to PD:

- **PD-F1 — Design two-part structure.** The design doctype has two recognised parts: the approach (tested by Check 1) and the detailed design (tested by Check 2).
- **PD-F2 — Doctype definitions needed.** All components owning doctypes must define them using the definition contract.
- **PD-F3 — Schema placement guidance.** PD's standard should reference DocMeth's schema placement guidance when advising components on their document sets.

**Cross-review required:** included in the PD standard update.

---

## Pending — Principles

### Three candidate premise strengthenings

From the design-approach work. These are not new premises — they would strengthen existing ones (same pattern as F12 found for the value claim). To be considered when Principles is next worked:

1. **Difficulty-as-evidence.** If something is becoming hard or elaborate, the model above it may need review. The recurrence signal (same accommodation across several elements) is especially general. May strengthen the existing model-before-machinery premise (P3).

2. **Do not build apparatus.** A clear principle is applied, not implemented through stages, phases, or machinery. May strengthen P3 or stand alongside it.

3. **Simple and well-conceived is the goal.** Output markedly more elaborate than the intent above it is a warning. May strengthen the existing layered-progression premise (P4).

**Action:** when Principles' standard is next authored, evaluate these against the existing nine premises. Decisions entries for strengthening, not new premises unless the existing ones genuinely don't carry them.

**Cross-review required:** yes, if any premises are strengthened — Principles is foundational and changes propagate.

---

## Pending — Standards

### Clarification block

The standard doctype has two parts: the standard itself (lean, stated rules) and clarification (reasoning, justification). Two blocks, joined when small, split by the split test when clarification would bloat the loaded standard. Carry from DocMeth.

---

## Pending — Core

### Component alias uniqueness

Component names and aliases must be unique within the framework. Aliases are used as type-reference prefixes in the dot-qualified naming grammar (`pd.brief`). Core Structure owns this rule.

---

## Pending — Working Practices

### Overview-first working behaviour

The discipline of staying at the overview level until it could drive excellent execution, probing rather than diving, is broader than design. It's a human-AI working behaviour that applies to research, planning, and any structured thinking. PD owns the design-specific application; WP owns the generic working behaviour when WP is built.

### `/more` command

AI-presented prompts (migration prompts, task summaries, session information) should be concise by default. The `/more` command expands the current prompt with additional detail. Belongs alongside the session-transition commands when those are designed.

### Items accumulated for WP from other passes

- Pending content rule ownership (flagged for revisit when WP is worked)
- Session-transition commands (full stop, checkpoint-and-continue, flush without closing)
- No-knowledge-lost rule and the three behaviours (session-close sweep, session-start check, periodic consolidation)
- Capture-and-place rules (the four methodology rules from the Core shaping session)
- Definition of done as a generic block (owned by WP, invariant: testable or assessable)
- Work item as the base workflow entity
- Human working model standard (tiering, confidence, assumptions report, drift detection)

---

## Pending — Infrastructure

### FUP manifest — `user_instructions` field clarification

The `user_instructions` field in the FUP manifest is only for tasks the user must do outside the AI platform — manual file system actions the deployer cannot reach (e.g. copy a file somewhere, delete a folder). All client-side instructions (download the FUP, run it, next tasks in the AI client) are presented in chat alongside the FUP, not in the manifest. Carry to the FUP design document as a clarification.

### FUP deployer — user_instructions display order

The `user_instructions` message should display after the deploy success statement, not before the deploy prompt. Currently displays before. Log for Code session.

---

## Cross-review register

Tracks changes that need external AI review before acceptance. Items are added as work produces them and cleared when review is completed.

| Item | Reason | Status |
|---|---|---|
| DocMeth definition contract (Design v6, Decisions v6, Schema/Authoring/Definitions Standards v4) | Definition-contract gap — fundamental rework | **Accepted** — three rounds, all findings resolved. Migration pending. |
| PD Standard update (design-approach + brief gate + operations/acceptance tests) | New gates that downstream work is built against | Pending — update not started |
| Principles premise strengthening | Foundational — changes propagate to all components | Pending — not started |

---

Version note: v3 — DocMeth cross-review accepted. PD carries (PD-F1/F2/F3), Standards clarification carry, Core alias uniqueness carry added. Schema review thread added. FUP deployer display-order task added. 2026-09-12.
