# AIDE Review Profiles — Standard

> **Identity:** `AIDE_ReviewProfiles@v1`
> **Common name:** Review Profiles
> **Version 1** (2026-08-29). First published definitions of Check, Inspect, Evaluate, Robust,
> and Stress Test, with default Levels, Modes, response expectations, and continuation guidance.

---

## Purpose

Define reusable Review methods over the `AIDE_Review@v1` Input Contract so a caller can select a
purposeful review lens without rebuilding its instructions each time.

## Profile contract

Every reusable Review Profile defines:

- `Name` — stable Type identity;
- `Purpose` — why the Type exists;
- `LearningObjective` — what the Review is trying to find out;
- `Boundary` — how far outside the current claim/artefact/design it may step;
- `LensMethod` — how the Reviewer approaches the work;
- `EvidenceExpectations` — what verification, comparison, or external evidence is expected;
- `ExpectedResponse` — what a useful payload contains;
- `DefaultLevel`;
- `DefaultMode`; and
- `ContinuationGuidance`.

Type defaults fill unresolved inputs. They do not override an explicit value or the effective Level
assessment for the actual task.

## Shared Type rules

- Choose Type from what the Review is trying to learn, not how important the work is.
- Type determines method; Level scales how strongly that method is applied.
- A Type may expose a more serious issue and justify switching Type in a later Round. Record the
  change and reason rather than silently broadening the active Type.
- Report material issues first. Do not propose complexity merely because an imperfection can be
  removed.
- Evidence and remedies are proportionate to Level and the Review objective.
- Level-based re-review rules in `AIDE_Review@v1` apply to every Type.

## Default matrix

| Type | Boundary | Default Level | Default Mode | Core question |
|---|---|---:|---|---|
| Check | Criterion-bound | Low | Full | Is this specific proposition or condition correct/satisfied? |
| Inspect | Artefact-bound | Standard | Full | What is wrong, missing, inconsistent, weak, or materially improvable? |
| Evaluate | Outcome-bound | Medium | Full | Does this approach deliver the intended outcomes well, and how could it be better? |
| Robust | Design/framing-bound | High | Full | Is the design itself sound, and where could its assumptions or structure fail? |
| Stress Test | Environment/adversary-bound | Extreme | Full | How does this withstand capable adversarial, competitive, or demanding external scrutiny? |

`Evaluate + Blind` is the normal form for an independent approach before the Lead's solution is
shown. Blind Mode remains an explicit selection because many Evaluate Reviews need to assess the
current approach directly.

## Check

### Purpose

Determine whether a specific proposition, requirement, calculation, contract point, expected
result, or condition is correct or satisfied.

### Learning objective

> Is the stated criterion met, and what evidence supports that answer?

### Boundary

Check is criterion-bound. It verifies the stated target and does not become a general search for
defects. If the check exposes a broader material issue, report it and recommend an appropriate
Type/Level change.

### Lens and method

- identify the exact claim or criterion;
- establish the authoritative evidence or test;
- verify the result and relevant assumptions;
- distinguish pass, fail, qualified/conditional result, and unknown;
- identify any evidence gap that prevents a reliable answer.

### Evidence expectations

Use evidence directly relevant to the criterion. At higher Levels, independently verify the
source, calculation, test, or trace from requirement to result rather than accepting an assertion.

### Expected response

- answer: Pass, Fail, Qualified, or Unknown;
- criterion applied;
- supporting evidence/test;
- defect or unmet condition where present;
- uncertainty/evidence gap; and
- any broader issue requiring another Type.

### Defaults and continuation

- `DefaultLevel: Low`
- `DefaultMode: Full`
- normally complete after a reliable answer;
- continue for missing evidence, material ambiguity, or verification of a material correction;
- do not broaden into Inspect without an explicit Type change.

## Inspect

### Purpose

Examine an existing artefact, implementation, document, code change, plan, or outcome for defects,
omissions, inconsistencies, drift, and meaningful improvement.

### Learning objective

> What is wrong, missing, inconsistent, weak, or materially improvable in what exists?

### Boundary

Inspect is artefact-bound. It accepts the authorised design/intent as the governing frame and
tests the artefact against it. It can identify a better local approach, but it does not redesign
the governing model unless a Finding justifies an Evaluate or Robust escalation.

### Lens and method

- inspect the artefact itself rather than only its description;
- compare against authoritative requirements, intent, scope, interfaces, and expected outcomes;
- find defects, omissions, inconsistencies, weak implementation choices, and scope drift;
- consider straightforward alternatives where they materially improve the outcome;
- prioritise by materiality rather than volume.

### Evidence expectations

Use the artefact and its authoritative contract. At higher Levels, inspect supporting tests,
source material, dependency behaviour, execution evidence, and relevant adjacent effects.

### Expected response

- material Findings in priority order;
- affected location or element;
- evidence/reasoning and consequence;
- contract/intent comparison where applicable;
- uncertainty; and
- possible local improvement where useful.

### Defaults and continuation

- `DefaultLevel: Standard`
- `DefaultMode: Full`
- continue where material defects remain, accepted fixes materially change the artefact, or the
  current artefact cannot yet be tested reliably;
- recommend Evaluate/Robust when the defect appears to originate in the governing approach rather
  than the artefact.

## Evaluate

### Purpose

Assess whether a concept, design, decision, plan, or proposed approach delivers the intended
outcomes well and how it could be improved.

### Learning objective

> Does this approach meet the objective well, where does it fall short, and are there materially
> better alternatives?

### Boundary

Evaluate is outcome-bound. It may challenge important assumptions and compare credible
alternatives, but it begins from the premise that the proposed direction is a plausible design
worth assessing. It improves within or around that design; Robust may reject the design/framing
itself.

### Lens and method

- test fitness against objective, success criteria, constraints, and authorised scope;
- examine trade-offs, consequences, dependencies, and key assumptions;
- identify strengths, weaknesses, gaps, and avoidable complexity;
- compare credible alternatives where they could materially improve outcomes;
- avoid redesigning for marginal gains;
- distinguish decision input from a mandatory remedy.

### Evidence expectations

Use stated outcomes, constraints, evidence, and alternatives already considered. At higher Levels,
verify important assumptions and compare stronger external or internal approaches where available.

### Expected response

- overall assessment;
- material strengths and weaknesses;
- outcome/constraint fit;
- key trade-offs and consequences;
- credible alternatives and comparative advantage where relevant;
- recommendation or decision input;
- unresolved uncertainties.

### Defaults and continuation

- `DefaultLevel: Medium`
- `DefaultMode: Full`
- prefer `Blind` where the objective is an independent approach and exposure to the current
  solution would anchor the Reviewer;
- continue while materially different evidence, alternatives, or revised decisions are changing
  the assessment;
- complete when the Lead has sufficient decision-quality input for the Level, including an
  explicit residual uncertainty where necessary;
- change to Robust where the design/framing itself becomes the central question.

## Robust

### Purpose

Find material weaknesses normal inspection or evaluation may miss, including weaknesses caused by
the chosen design or framing itself.

### Learning objective

> Is this the right design, where can it fail or behave unexpectedly, and would a materially
> different design avoid the problem?

### Boundary

Robust is design/framing-bound. It may step back from the current design, challenge the problem
framing and foundational assumptions, and perform a blank-sheet comparison where consequence or
Findings justify it.

### Lens and method

- challenge foundational and operational assumptions;
- probe edge cases, unusual interactions, degraded states, and failure paths;
- look for hidden dependencies, second-order effects, and invalid safeguards;
- distinguish material failure modes from theoretical imperfections;
- step back and ask whether the problem is being solved in the wrong way;
- compare materially different designs when that exposes or avoids structural weakness;
- test whether added safeguards create disproportionate complexity.

### Evidence expectations

Inspect available evidence for assumptions, failure behaviour, interfaces, and safeguards. At
higher Levels, seek independent verification, precedents, or simulations where they materially
improve confidence. External threat/comparator research is not mandatory unless the objective
requires it; that is a defining Stress Test emphasis.

### Expected response

- material weaknesses/failure modes;
- trigger conditions and affected outcomes;
- evidence/reasoning and uncertainty;
- likely consequence and reach;
- challenged assumptions or framing;
- materially different design alternatives where justified;
- whether action appears proportionate; and
- residual risks or areas requiring judgment.

### Defaults and continuation

- `DefaultLevel: High`
- `DefaultMode: Full`
- use `Blind` where an independent blank-sheet framing is more valuable than direct critique;
- continue while material structural Findings, changed assumptions, or revised designs warrant
  further examination;
- substantive review-driven changes are normally returned under the High re-review posture;
- complete when material failure paths and design alternatives are adequately understood for the
  Level, not when every theoretical risk is removed.

## Stress Test

### Activation

Stress Test is user-activated only. An AI may recommend it and explain the expected value, but no
Standard, workflow, WorkPackage default, or autonomous risk trigger starts it without explicit
user direction.

### Purpose

Determine how well the subject withstands deliberate, intelligent, and sustained challenge,
including exploitation of weakness and comparison against strong external alternatives.

### Learning objective

> What could a capable adversary, competitor, hostile environment, demanding customer, auditor,
> or expert discover, exploit, outperform, or use against this?

### Boundary

Stress Test is environment/adversary-bound. It steps outside the current design to test the work
against hostile or demanding reality, known failures, credible threats, strong comparators, and
external scrutiny.

### Lens and method

- assume weaknesses will be actively sought rather than encountered accidentally;
- challenge foundational assumptions and combine weaknesses into realistic paths;
- identify plausible adversary/challenger objectives and capabilities;
- test technical, architectural, operational, commercial, process, and human surfaces selected by
  the Review objective;
- seek relevant known attacks, failures, precedents, solutions, benchmarks, and competitors;
- compare resilience against credible stronger approaches;
- distinguish theoretical possibilities from realistically exploitable/material weakness;
- identify where the subject is stronger as well as weaker;
- assess whether proposed mitigation is proportionate to the protected outcome.

### Optional Stress Test parameters

- `AdversaryOrChallenger`
- `AdversaryObjective`
- `SubjectScope`
- `ProtectedOutcomesOrAssets`
- `ChallengeSurfaces`
- `ComparatorSet`
- `Constraints`
- `AssumptionsToAttack`
- `EvidenceAccess`
- `MaterialityThreshold`

Resolve only the parameters relevant to the actual objective.

### Evidence expectations

Actively seek external examples, comparators, known failures, threat paths, benchmarks, or stronger
solutions where the Reviewer has the capability and the scope permits it. If required evidence
access is unavailable, state the limitation; do not present a speculative scan as an Extreme
Stress Test.

Research performed to support the Review remains evidence gathering inside this Review. A
standalone request to discover options or facts without the Review lifecycle belongs to Research,
not this Type.

### Expected response

- strongest material weaknesses first;
- realistic challenge/exploitation or outperformance scenarios;
- external examples/comparators and their relevance;
- consequence, likelihood/materiality, and uncertainty;
- performance of current safeguards/design against the challenge;
- comparative strengths as well as weaknesses;
- residual risks that cannot reasonably be eliminated;
- proportionate mitigation directions; and
- questions requiring user/Lead judgment.

### Defaults and continuation

- `DefaultLevel: Extreme`
- `DefaultMode: Full`
- continue while material challenge paths, combined weaknesses, comparator evidence, or material
  remediations remain insufficiently tested for Extreme confidence;
- re-review material remediations as part of the cycle;
- stop when major paths are adequately explored and dispositioned, further Findings are marginal
  or speculative, or the residual issue is an explicit strategic/risk judgment;
- never pursue complexity solely to eliminate a theoretical weakness.

## Type changes and combined objectives

Use one primary Type per Round so the request has a clear learning objective. Where a Review needs
multiple lenses:

- sequence them as separate Rounds or separate Reviews when each needs a distinct response;
- state the primary Type and a narrow secondary question where separation would add no value; or
- change Type after a Finding exposes a materially different question.

Record each Round's effective Type. Do not create hybrid names such as `Robust-Deep`; Level already
expresses intensity.

## Five-use-case defaults

| Use case | Normal starting profile | Common variation |
|---|---|---|
| Design exploration | Evaluate + Medium + Full | Blind for an independent approach; Robust when framing itself is uncertain. |
| Pre-confirmation design | Evaluate + Medium | Robust + High for foundational or hard-to-reverse design. |
| WorkPackage authoring | Check + Low or Inspect + Standard | Raise Level when incorrect scope/contract would have material downstream reach. |
| Build plan | Evaluate + Medium | Robust + High for consequential architecture or weak assumptions. |
| Post-execution | Inspect + Standard | Robust + High where implementation or design integrity requires broader challenge. |

These are starting defaults. Effective Level follows consequence, reach, reversibility, and
uncertainty; explicit work configuration or instruction may select another Type/Mode.

---

**Depends on:** `AIDE_Review_Standard_v1`, `Capabilities_Review_Design_v1`.

**References:** `Capabilities_Design_v5`, `Capabilities_Standards_Design_v3`.

**Type:** `Standard` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
