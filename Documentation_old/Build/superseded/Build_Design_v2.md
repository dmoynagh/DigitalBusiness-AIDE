# Build — Design

> **Version 2** (2026-08-31). Clarifies canonical-to-derived Build flow, composable platform representation, derived-artefact provenance, and the Build/AI Deployment boundary.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

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

## §9 — Canonical and derived representation

Where Build is producing a platform or consumption representation of governed capability material, the upstream canonical Standard/Tool or other authoritative outcome supplies the semantic meaning.

Build may render, transform, assemble or package that meaning into a target-compatible form such as a skill, plugin contribution, instruction representation, Bundle member, merged Bundle, platform-specific file or other supported representation. The derived form must preserve the authoritative semantics; Build does not reopen Decisions history to reconstruct or improve missing capability meaning.

Derived representations are built from the **current authoritative inputs resolved for the work**. An earlier Bundle, package, generated file or deployed copy is evidence about a previous derived state, not authority for determining the current canonical capability version when a current authoritative source establishes otherwise.

Build may produce any explicitly authorised subset or composition. It must not assume that every AIDE Standard is deployed only as part of the full AIDE system. Independently deployable Standards and future subsets remain independently buildable unless their own authoritative dependencies say otherwise.

Where upstream material defines distinct semantic roles, Build preserves those distinctions unless an authorised representation combines them without changing their meaning. Packaging convenience is not authority to collapse separate artefacts such as a persistent bootstrap, Bootstrap Profile, thin Bootstrap Contribution and full Standard/Tool into one semantic object.

For a generated or assembled representation, Build evidence should identify the authoritative source identity/version set used sufficiently to make the result reproducible and to avoid mistaking the derived artefact for its source.

If canonical or authoritative input is insufficient to produce a correct representation, Build returns the defect to the owning Design/capability rather than inventing semantics during rendering.

## §10 — Platform implementation and AI Deployment boundary

Platform-specific commands, file layouts, skills/plugins, toolchains and environment mechanics belong to platform Build knowledge or Tools, not to this generic Design. A platform implementation must preserve the same WorkPackage authority, execution, validation and return semantics.

Build may produce a platform-compatible artefact, representation, assembled consumption artefact or package when that is the authorised output. **Production of that output does not establish that it has been installed, reconciled into a target environment, or verified as usable there.**

AI Deployment owns target-state reconciliation, delivery/install/update/remove behaviour and verification of the resulting target/runtime state. Build reports only the state it actually produced and validated within its own authorised scope.

---
Dependencies: !AIDE_DocumentationMethodology@v18, ProjectDesign_Design_v1, AIDE_Review@v1
References: Build_WorkPackage_Design_v1, AIDE_WorkPackage@v1, AIDE_Deployment@v1, AIDE_StandardsProduction@v1
