AIDE Documentation | WIP | AIDE_Documentation_WIP@v2 | 2026-09-12

## Active threads

### DocMeth rework — definition-contract gap

DocMeth design pass completed 2026-09-11 but cross-review identified a primary objective gap: the design describes the model (what a doctype is, what a block is) without specifying the grammar for defining instances (how you write a doctype definition, what properties a block-type definition must contain). The standard consequently cannot enable a consumer to define a new type from it alone.

**Direction:** reopen the design with a proper brief (inline). Address the definition-contract gap, the recognition marker content, and minimum format mapping for markdown. Reauthor the standard from the completed design. Cross-review again.

**Lesson applied:** every design pass must have a brief before design starts. Definition of done is the acceptance gate. The black-box acceptance test (can a fresh AI perform the operations from the standard alone?) is the concrete form of the definition of done for any standard.

**Cross-review required:** yes — both the reworked design and the reauthored standard. The gap was fundamental, not editorial.

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

## Completed — Working Practices

All items below delivered in WorkingPractices_Standard_v2 (cross-reviewed, 4 rounds, deployed 2026-09-17) and Assurance_Standard_v1 (human working model). Overview-first discipline, /more command, session-transition commands (renamed operational tools), capture-and-place, pending content rule, definition of done, work items, no-knowledge-lost — all in the WP standard. Tiering, confidence, assumptions, drift detection — in the Assurance standard.

---

## Pending — Infrastructure

### FUP manifest — `user_instructions` field clarification

The `user_instructions` field in the FUP manifest is only for tasks the user must do outside the AI platform — manual file system actions the deployer cannot reach (e.g. copy a file somewhere, delete a folder). All client-side instructions (download the FUP, run it, next tasks in the AI client) are presented in chat alongside the FUP, not in the manifest. Carry to the FUP design document as a clarification.

---

## Cross-review register

Tracks changes that need external AI review before acceptance. Items are added as work produces them and cleared when review is completed.

| Item | Reason | Status |
|---|---|---|
| DocMeth Design v3 + Standard v2 | Fundamental rework — definition-contract gap | Pending — rework not started |
| PD Standard update (design-approach + brief gate + operations/acceptance tests) | New gates that downstream work is built against | Pending — update not started |
| Principles premise strengthening | Foundational — changes propagate to all components | Pending — not started |

---

Version note: v2 — adds the `/more` command (Working Practices), and the FUP `user_instructions` clarification (Infrastructure). 2026-09-12.
