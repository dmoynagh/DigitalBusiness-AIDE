# Build Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.

## Binder manifest

- `Build_Index_v1.md` — sha256 `0738486e768e`
- `Build_Design_v1.md` — sha256 `b6dbbefd2cc4`
- `Build_Decisions_v1.md` — sha256 `f6dc433ad3b8`
- `Build_WorkPackage_Design_v1.md` — sha256 `588a4e3a2d52`
- `AIDE_Build_Standard_v1.md` — sha256 `2ae0223e6b78`
- `AIDE_WorkPackage_Standard_v1.md` — sha256 `bc84412585a7`

---

<!-- BEGIN SOURCE: Build_Index_v1.md -->
# Build — Index

> **Version 1** (2026-08-30). Registers the initial generic Build and WorkPackage corpus.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

## Project identity

**Topic:** Build  
**Project container / master folder:** `AIDE/Build/`  
**Purpose:** Generic objective-driven execution of defined work.

## Topic declarations

| Name | Parent | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Build | AIDE | `Build` | independent | expanded |
| WorkPackage | Build | `Build_WorkPackage` | inherits | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Build_Index` | v1 | Index | Current |
| `Build_Design` | v1 | Design | Current |
| `Build_Decisions` | v1 | Decisions | Current |
| `Build_WorkPackage_Design` | v1 | Design | Current |
| `AIDE_Build_Standard` | v1 | Standard | Current; identity `AIDE_Build@v1` |
| `AIDE_WorkPackage_Standard` | v1 | Standard | Current; identity `AIDE_WorkPackage@v1` |

## Relationships

- Project Design defines work; WorkPackage is the principal governed handoff.
- Build returns evidence/outcomes; design-shaping issues return to Project Design.
- Platform-specific execution knowledge implements this behavioural contract without redefining it.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Core_System_Design_v4
References: ProjectDesign_Design_v1
<!-- END SOURCE: Build_Index_v1.md -->

---

<!-- BEGIN SOURCE: Build_Design_v1.md -->
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
<!-- END SOURCE: Build_Design_v1.md -->

---

<!-- BEGIN SOURCE: Build_Decisions_v1.md -->
# Build — Decisions

> **Version 1** (2026-08-30). Records the decisions establishing Build as generic execution/production behaviour and WorkPackage as its principal governed handoff.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## D1 — Retain Build and define it behaviourally

**Decision.** Retain **Build** as the AIDE area for objective-driven execution/creation. It is not defined as compilation, coding or any particular product.

**Reason.** The common behaviour is taking defined work and producing/validating artefacts. Current products are implementations of that behaviour rather than its definition.

## D2 — WorkPackage is the principal governed handoff into Build

**Decision.** Build consumes a WorkPackage containing work-specific intent, authority, inputs, outputs and acceptance; Build environments supply reusable implementation/platform knowledge.

**Reason.** This makes the handoff self-contained without copying generic execution knowledge into every project.

## D3 — Build has bounded implementation authority

**Decision.** Build may resolve ordinary implementation detail within authorised scope but returns objective, scope, acceptance, architecture or policy changes to the work owner/Project Design.

**Reason.** Execution needs autonomy to be efficient without silently becoming a second design authority.

## D4 — Build standards describe behaviour, not products

**Decision.** Codex, Claude Code, ChatGPT Work, Claude Co-work and future systems are Build environments/implementations. Generic Build Standards do not encode their product mechanics.

**Reason.** Behavioural contracts remain stable while products and platform capabilities change.

## D5 — Every executed WorkPackage returns evidence

**Decision.** Build returns an Outcome recording actual work, outputs, validation, deviations, unresolved issues and design feedback.

**Reason.** The director of work must be able to reconcile execution without reconstructing the Build session, and completion must mean more than artefact creation.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v1
References: ProjectDesign_Design_v1, Core_System_Design_v4
<!-- END SOURCE: Build_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Build_WorkPackage_Design_v1.md -->
# Build WorkPackage — Design

> **Version 1** (2026-08-30). Defines the generic Design-to-Build handoff, execution authority, acceptance and return contract required for operational AIDE Build work.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## §1 — Purpose

A WorkPackage is a bounded, executable unit of defined work handed to Build. It answers what Build is authorised to do, with what inputs, for what result, and how completion is established.

The WorkPackage is an outcome of Project Design/work direction and is not itself the place to rediscover the project's design.

## §2 — Required contract

Every executable WorkPackage resolves:

- **Objective** — the outcome the work is intended to achieve.
- **Authorised Scope** — what may be changed/created and important explicit exclusions.
- **Inputs** — work-specific authoritative artefacts/information required for execution.
- **Required Outputs** — artefacts/state the package must produce or change.
- **Acceptance** — observable conditions/evidence used to judge completion.
- **Constraints** — applicable limits, dependencies, environment/target requirements, or reserved decisions.
- **Review posture** — any required/recommended plan or result Review; otherwise the normal Build/Review defaults apply.
- **Return** — where/how the WorkPackage Outcome is to be delivered or recorded.

Optional context may be included where it materially helps execution, but the WorkPackage should not become a dump of design history.

## §3 — Self-containment boundary

A WorkPackage is complete when Build can understand the required result and authority without reopening Decisions or other design-history material.

Self-containment does **not** require copying generic platform/toolchain knowledge already available to the Build environment through applicable Standards, Tools or references.

If a material design choice is unresolved, the package is NotReady rather than granting Build authority to invent it.

## §4 — Review configuration

WorkPackage may configure Review separately for planning and completed execution using `AIDE_Review`:

```yaml
Review:
  Plan:
    Posture: Required | Recommended | Optional | None
    Type: <profile where specified>
    Level: <level where specified>
    Mode: <mode where specified>
  Result:
    Posture: Required | Recommended | Optional | None
    Type: <profile where specified>
    Level: <level where specified>
    Mode: <mode where specified>
```

Omitted Type/Level/Mode values resolve through the governing Review defaults. WorkPackage does not define another Type/Level system.

A domain may use a higher-level tier to generate this explicit posture, but tier semantics are domain/workflow policy unless separately standardised.

## §5 — Execution contract

Build must:

1. validate that required WorkPackage inputs are available and mutually coherent;
2. identify any material ambiguity before consequential execution;
3. establish a proportionate execution plan;
4. perform required/recommended Review according to governing posture;
5. execute within authorised scope using applicable Standards/Tools;
6. validate the actual result against Acceptance;
7. perform result Review where required/recommended; and
8. return the Outcome truthfully.

Build may resolve implementation details inside the contract. It may not silently alter Objective, Authorised Scope, Acceptance or a reserved design decision.

## §6 — Out-of-scope discoveries

Useful issues discovered outside Authorised Scope are reported in the Outcome and not executed under the current WorkPackage unless the work owner explicitly re-scopes the package or creates separate work.

## §7 — WorkPackage Outcome

The Outcome records at least:

- terminal status: `Complete | Partial | Blocked | Failed`;
- summary of work actually performed;
- produced/changed artefacts or state;
- acceptance/validation evidence and failures;
- Reviews performed and material resulting dispositions where applicable;
- deviations/authorised exceptions;
- unresolved items and remaining work;
- out-of-scope findings; and
- design questions/follow-up required.

The Outcome may be held in the active WorkPackage and folded into it on archival under Documentation Methodology v17.

## §8 — Lifecycle

```text
Defined → Ready → Executing → Returned → Reconciled/Archived
```

- **Defined** — work is being authored; not yet executable.
- **Ready** — required contract is resolved and execution is authorised.
- **Executing** — Build owns active execution within scope.
- **Returned** — an Outcome has been produced.
- **Reconciled/Archived** — the director of work has consumed the Outcome; further work, if any, is a new/revised WorkPackage.

A blocked package may return without being complete. Re-authorisation after a design change produces a new executable state rather than silently pretending the original contract never changed.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v1, AIDE_Review@v1
References: ProjectDesign_Design_v1
<!-- END SOURCE: Build_WorkPackage_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Build_Standard_v1.md -->
# AIDE Build — Standard

> **Identity:** `AIDE_Build@v1`
> **Common name:** Build
> **Version 1** (2026-08-30). Initial platform-independent execution, validation and return contract.
>
> **Default weight:** Requirement

---

## Purpose

Execute defined work through a WorkPackage, produce the required artefacts/state, validate the actual result, and return evidence without silently taking design authority.

## Applicability

Apply when an AI/environment is acting as the executor of a governed WorkPackage or equivalent explicitly defined Build task.

Build is behavioural. Coding agents, document/work agents and future execution environments may all implement this contract.

## Accept the handoff

Before consequential state change:

- resolve the WorkPackage and authoritative work-specific inputs;
- confirm Objective, Authorised Scope, Required Outputs and Acceptance are materially clear;
- load applicable Standards/Tools needed for the work; and
- return `NotReady`/Blocked if a substantive design gap prevents safe execution.

Do not use design-history material as permission to invent a result that the current handoff does not determine.

## Plan proportionately

Establish a coherent execution sequence proportionate to the work. Trivial work need not generate ceremonial plan artefacts.

Apply configured/governing Review before execution where required or recommended.

## Execute within authority

Resolve ordinary implementation detail autonomously where it remains within scope and does not alter objective, acceptance, major architecture/policy or reserved decisions.

If execution exposes a design-level problem, stop/contain affected work and return the issue rather than adding compensating machinery without authority.

## Validate the result

Test actual outputs/state against the WorkPackage Acceptance and applicable Standards. Validation evidence should be sufficient to support the returned status.

Apply result Review where required/recommended.

## Return outcome

Return an `AIDE_WorkPackage@v1` Outcome with truthful status, work performed, outputs, validation, deviations, remaining work, out-of-scope findings and design feedback.

`Complete` means the defined acceptance is satisfied, not merely that execution ended.

## Failure and resumption

Use `Partial`, `Blocked` or `Failed` distinctly. Preserve safe successful work where appropriate and state the actual resulting state. Re-running should resume or reproduce intentionally and avoid duplicate side effects where practicable.

## Platform boundary

Target-platform commands, plugin/skill structures, repositories, toolchains and environment mechanics belong in platform Build Standards/Tools/configuration. They may vary without changing this contract.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v1, AIDE_Review@v1
References: AIDE_WorkPackage@v1
<!-- END SOURCE: AIDE_Build_Standard_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_WorkPackage_Standard_v1.md -->
# AIDE WorkPackage — Standard

> **Identity:** `AIDE_WorkPackage@v1`
> **Common name:** WorkPackage
> **Version 1** (2026-08-30). Initial generic Design-to-Build handoff and Build Outcome contract.
>
> **Default weight:** Requirement

---

## Purpose

Provide Build with one bounded executable contract that states the required result, authority, work-specific inputs and acceptance, and returns enough evidence for the director of work to reconcile execution.

## Required WorkPackage content

Resolve before execution:

```yaml
WorkPackage:
  Objective: <required result>
  AuthorisedScope: <allowed work and material exclusions>
  Inputs: <work-specific authoritative inputs>
  RequiredOutputs: <artefacts/state to produce or change>
  Acceptance: <observable completion/evidence conditions>
  Constraints: <applicable limits/dependencies/targets/reserved decisions>
  Review: <optional explicit plan/result Review posture>
  Return: <required outcome destination/record>
```

Equivalent clear prose/sections are valid; the semantic fields matter, not this physical rendering.

If a material field is unresolved and cannot safely be inferred from authoritative inputs, the WorkPackage is NotReady.

## Handoff rule

Build should not need Decisions/design-history material to reconstruct the required result. Include work-specific authoritative artefacts needed for execution; do not duplicate generic execution/platform knowledge already supplied by the Build environment.

## Build authority

Build may choose ordinary implementation detail within Authorised Scope. It must return rather than silently change Objective, major scope, Acceptance, architecture/policy, or a decision explicitly reserved to the work owner.

## Review

Where the WorkPackage specifies plan/result Review, execute it under `AIDE_Review`; do not invent a WorkPackage-specific review method.

An omitted Review field does not disable governing Review requirements supplied by another applicable Standard/workflow.

## Execution

1. Validate inputs and authority.
2. Establish a proportionate plan.
3. Complete applicable pre-execution Review.
4. Execute within scope.
5. Validate against Acceptance.
6. Complete applicable result Review.
7. Return a truthful Outcome.

Do not claim completion solely because an artefact was produced.

## Out-of-scope discovery

Report useful out-of-scope findings; do not action them under the current authority without explicit re-scope/new work.

## Outcome

Return:

```yaml
Outcome:
  Status: Complete | Partial | Blocked | Failed
  WorkPerformed: <summary>
  Outputs: <produced/changed artefacts or state>
  Validation: <acceptance evidence/results>
  Reviews: <where applicable>
  Deviations: <authorised exceptions/differences>
  Remaining: <unresolved/remaining work>
  OutOfScope: <reported findings>
  DesignFeedback: <questions/follow-up>
```

The persisted record may use concise document sections rather than YAML.

## Partial/failure behaviour

Preserve successful work only where the resulting state is safe and accurately reportable. Do not hide partial completion. A retry/resumption starts from the actual returned state and must avoid duplicate side effects where practical.

## Lifecycle

`Defined → Ready → Executing → Returned → Reconciled/Archived`.

Documentation Methodology owns the file naming/archive mechanics; this Standard owns the WorkPackage execution semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_WorkPackage_Design_v1, AIDE_Review@v1
References: AIDE_Build@v1, AIDE_ProjectDesign@v1
<!-- END SOURCE: AIDE_WorkPackage_Standard_v1.md -->

---
