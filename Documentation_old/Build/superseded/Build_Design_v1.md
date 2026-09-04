# Build — Design

> **Version 1** (2026-08-30). Establishes Build as AIDE's generic objective-driven execution methodology, independent of software compilation, coding product, or AI vendor.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## §1 — Purpose and boundary

Build is **objective-driven execution that takes defined work and produces required artefacts/outcomes**.

It is not synonymous with software compilation or coding. A Build environment may create/modify software, documents, datasets, websites, media/assets, packages, configuration or other objective-driven outputs.

Build owns the generic execution/handoff behaviour. It does not own the originating project's design and does not own each domain's production workflow.

## §2 — Core model

```text
WorkPackage
   ↓
accept / validate handoff
   ↓
plan proportionately
   ↓
review plan where required/useful
   ↓
execute within authorised scope
   ↓
validate against acceptance
   ↓
review result where required/useful
   ↓
WorkPackage Outcome
```

Build may be implemented by Codex, Claude Code, ChatGPT Work, Claude Co-work or other current/future execution-capable environments. The behavioural contract is stable even when platform mechanisms differ.

## §3 — WorkPackage boundary

`AIDE_WorkPackage` is the principal governed handoff into Build.

A WorkPackage supplies the work-specific definition and authority. The Build environment supplies reusable execution knowledge, applicable Standards/Tools, platform mechanics and ordinary implementation expertise.

Build must not require access to design-history material merely to reconstruct what result was intended. If the WorkPackage/authoritative input is incomplete on a material point, return a design/input issue rather than inventing the missing policy.

## §4 — Build authority

Build may decide ordinary implementation details needed to achieve the defined outcome when:

- they remain within authorised scope;
- they do not change the objective or acceptance contract;
- they do not transfer major ownership/responsibility; and
- the decision is not reserved by the WorkPackage or an applicable Standard.

Build returns rather than silently deciding changes to objective, major scope, acceptance, architecture, policy or other substantive design authority.

## §5 — Planning

Planning is proportionate. A separate elaborate plan is not mandatory for trivial execution, but the executor must establish a coherent intended sequence before consequential state change.

Where plan Review is required or recommended, Build applies the configured `AIDE_Review` Type/Level/Mode rather than defining another review model.

## §6 — Execution and validation

Execution:

- uses applicable Standards and Tools;
- preserves defined authority and constraints;
- makes state changes deliberately and recoverably where practicable;
- surfaces failures/deviations rather than claiming completion; and
- records enough evidence to support validation and return.

Validation tests the actual result against the WorkPackage acceptance contract and relevant governing Standards. Producing an artefact is not by itself evidence that the objective was satisfied.

## §7 — Outcome and return

Every executed WorkPackage returns an Outcome sufficient for the director of work to understand:

- what was actually done;
- artefacts/state produced or changed;
- validation performed and results;
- deviations or accepted exceptions;
- unresolved/blocked work;
- out-of-scope findings noticed but not acted on; and
- any design question/follow-up now required.

The outcome is evidence, not a rewritten Design.

## §8 — Failure, partial completion and resumption

Build distinguishes Complete, Partial, Blocked and Failed outcomes. It does not erase successfully completed work merely to make a later failure appear atomic unless the governing work explicitly requires transaction-like rollback.

Partial work is preserved only when safe and truthful; the Outcome states the resulting state and what remains. Re-running should resume or reproduce deliberately rather than duplicate side effects where idempotency is achievable.

## §9 — Platform implementation

Platform-specific build representations, commands, file layouts, skills/plugins, toolchains and environment mechanics belong to platform Build knowledge or Tools, not to this generic Design.

A platform implementation must preserve the same WorkPackage authority, execution, validation and return semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v18, ProjectDesign_Design_v1, AIDE_Review@v1
References: Build_WorkPackage_Design_v1, AIDE_WorkPackage@v1
