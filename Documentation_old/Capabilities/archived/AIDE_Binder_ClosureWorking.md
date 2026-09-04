# AIDE Closure Working Binder
> **Generated working Binder — 2026-08-30.** Consolidates the current closure work for Project Design, Build/WorkPackage, Platform Deployment, OpenAI evidence and Documentation Methodology reconciliation. Source files remain the editable units.

## Manifest

- `ProjectDesign_Decisions_v1.md` — sha256 `b4b4c718ba5e`
- `ProjectDesign_Design_v1.md` — sha256 `a542488f8ae3`
- `AIDE_ProjectDesign_Standard_v1.md` — sha256 `fb133958bea9`
- `Build_Decisions_v1.md` — sha256 `990df2d0523e`
- `Build_Design_v1.md` — sha256 `6996d0f981c1`
- `Build_WorkPackage_Design_v1.md` — sha256 `fcfeac0bccff`
- `AIDE_WorkPackage_Standard_v1.md` — sha256 `864067362a03`
- `AIDE_Build_Standard_v1.md` — sha256 `b0771872e453`
- `PlatformDeployment_Decisions_Working_v1.md` — sha256 `85dec5e36360`
- `PlatformDeployment_Working_v1.md` — sha256 `c8be238fc991`
- `Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING.md` — sha256 `e8c5be9b4620`
- `Capabilities_DeploymentPromotion_ChangePlan_Working_v1.md` — sha256 `182530ccdbc7`
- `DocumentationMethodology_Reconciliation_Working_v1.md` — sha256 `91a952d042e4`
- `AIDE_Closure_Working_v1.md` — sha256 `58c4df76cfa7`

---

<!-- BEGIN SOURCE: ProjectDesign_Decisions_v1.md -->
# Project Design — Decisions

> **Version 1** (2026-08-30). Records the decisions establishing Project Design as the generic design-side AIDE methodology and separating domain workflows from the reusable Project Design/Build contracts.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## D1 — Use Project Design rather than Design or Solution Design

**Decision.** The top-level methodology is named **Project Design**. `Design` remains a valid artefact/stage within it.

**Reason.** Bare `Design` is too overloaded, while `Solution Design` implies a narrower technical/software context. Project Design applies naturally to the intended range of substantial work.

## D2 — Project Design is domain-independent

**Decision.** Project Design defines reusable behaviour for determining substantial work, not a software-development lifecycle or product-specific process.

**Reason.** Software, documentation, capability, business and creative projects share the same core questions of intent, requirements, decisions, approach and outcomes.

## D3 — Domain production workflows remain domain-owned

**Decision.** Do not introduce a generic top-level Workflow owner for all production scenarios. A domain owns the workflow that composes Project Design, Build and other AIDE concerns for its type of work.

**Reason.** A universal workflow layer would have to understand every domain and would duplicate semantics already owned by Project Design and Build.

## D4 — Project Design and Build form an iterative loop

**Decision.** The generic handoff is Design Outcome → WorkPackage → Build → Build Outcome, with the outcome returning to Project Design where completion or a design issue must be reconciled.

**Reason.** Execution can reveal evidence or constraints that legitimately change the next design state without transferring design authority into Build.

## D5 — Layered overviews are a design-control mechanism

**Decision.** For substantial design, use a short intent/system layer and model layer as the primary checkpoint before detailed mechanics.

**Reason.** A compact complete view makes drift, boundary errors, missing concepts and unnecessary complexity easier to detect. Difficulty explaining the model simply is evidence to reconsider the model before expanding the specification.

---

**Depends on:** None.

**References:** `ProjectDesign_Design_v1`, `Build_Design_v1`.

**Methodology:** v17
<!-- END SOURCE: ProjectDesign_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Design_v1.md -->
# Project Design — Design

> **Version 1** (2026-08-30). Establishes Project Design as AIDE's generic methodology for defining substantial work before execution, independent of project domain or AI product.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## §1 — Purpose and boundary

Project Design defines **what is to be achieved, why, under what requirements and constraints, and what approach/outcome has been determined** before execution is handed to Build.

It is generic across software, documentation, capability development, business/process work, creative production, and other substantial projects.

Project Design owns the reusable design method. It does not own a domain's production workflow and does not execute the resulting work.

## §2 — Core model

```text
Intent / need
    ↓
Brief / requirements / constraints
    ↓
Decisions and model/approach
    ↓
Design Outcome
    ↓
WorkPackage where execution is required
    ↓
Build
    ↓
Build Outcome
    ↓
confirm completion OR resolve returned design issue
```

The loop may repeat. A Build Outcome can close the work or return evidence/questions that require Project Design to revise the defined outcome and issue further work.

## §3 — Principal concepts

### Intent and Brief

States the objective, need, scope, success conditions and important non-goals. The amount of ceremony is proportionate to the stakes; not every task requires a separate Brief document.

### Requirements and constraints

States what the outcome must satisfy. Requirements may be project-specific or consumed from applicable Standards. They remain distinct from implementation choices.

### Decisions

Records material design choices, credible rejected alternatives, reasoning and consequences. Decisions inform the current Design; downstream execution consumes the Design/defined outcome rather than reconstructing decisions history.

### Design

The authoritative current model/approach: what is now determined. It must contain every consideration that downstream work needs to honour.

### Design Outcome

The defined deliverable, contract or state that execution is intended to produce. It may be a canonical Standard/Tool, software behaviour, document set, asset specification, implementation contract, or another domain-defined outcome.

### Review

Independent Review is applied under `AIDE_Review` where required, configured, or materially valuable. Review informs the Lead; it does not take ownership of the design.

## §4 — Layered design control

For substantial design, the preferred primary checkpoint is a short two-layer overview before detailed specification.

**Layer 1 — Intent / system view**

- purpose and intended outcome;
- governing premises;
- ownership and explicit non-ownership;
- principal inputs/outputs; and
- relationship to surrounding architecture.

**Layer 2 — Model**

- principal concepts/entities;
- responsibilities and relationships;
- major lifecycle/flow; and
- important rules and distinctions.

Detailed schemas, metadata, mechanics and wording should expand a model already clear at these two layers. If the design cannot be explained simply at this level, first test whether the model is unclear or unnecessarily complicated.

## §5 — Domain-owned workflows

A production workflow belongs to the domain whose work it orchestrates.

A domain workflow may compose Project Design, Build, Review, capabilities and other AIDE services in any sequence the domain requires. It does not redefine their generic semantics.

Examples include a code-development workflow, capability-production workflow, documentation-production workflow, or branding-production workflow.

## §6 — Handoff to Build

Where execution is required, Project Design creates or authorises a WorkPackage conforming to `AIDE_WorkPackage`.

The handoff must define enough work-specific intent that Build does not need to reconstruct the design process to know the required result.

Generic execution/platform knowledge belongs to the Build environment and applicable Standards/Tools; it is not copied into every WorkPackage merely for self-containment.

## §7 — Return from Build

Build returns a WorkPackage Outcome stating what was done, what was produced, validation evidence, deviations, unresolved issues and any design question discovered during execution.

Project Design then:

- confirms/records completion where the defined outcome is satisfied;
- resolves a design issue and issues revised/further work; or
- explicitly accepts a residual difference/risk within the work owner's authority.

Execution evidence is input to Project Design state; it does not silently rewrite the Design.

## §8 — Simplicity and escalation

A sound conceptual model should normally permit a clean implementation. When downstream execution requires accumulating exceptions, compensating mechanisms or special cases, Project Design should consider whether ownership, boundaries, requirements or the model itself should be simplified before adding further machinery.

Routine reversible detail may be resolved during execution. Changes to objective, authorised scope, acceptance, major ownership or architecture return to Project Design.

---

**Depends on:** `DocumentationMethodology_Guide_v17`, `AIDE_Review@v1`.

**References:** `Build_Design_v1`, `AIDE_WorkPackage@v1`.

**Methodology:** v17
<!-- END SOURCE: ProjectDesign_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_ProjectDesign_Standard_v1.md -->
# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v1`
> **Common name:** Project Design
> **Version 1** (2026-08-30). Initial behavioural contract for defining substantial project work and handing defined execution to Build.
>
> **Default weight:** Expectation

---

## Purpose

Define substantial work coherently before execution: establish intent and requirements, determine the current model/approach, review proportionately, and hand execution to Build through a complete WorkPackage where needed.

## Apply proportionately

Use the amount of structure justified by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Establish the work

For work that needs design, establish enough of the following to remove material ambiguity:

- objective/need and intended outcome;
- authorised scope and non-goals;
- requirements and constraints;
- material assumptions/uncertainties;
- decisions and credible alternatives where consequential;
- the current design/model/approach; and
- defined deliverables or acceptance signals.

Do not allow detailed implementation to become the place where unresolved design is silently decided.

## Use a layered checkpoint for substantial design

Before descending into extensive mechanics, maintain a compact view of:

1. **Intent/system:** purpose, premises, ownership/boundaries, inputs/outputs and surrounding relationships.
2. **Model:** principal concepts, responsibilities, relationships, lifecycle/flow and major rules.

If this view is difficult to make clear, reassess the model before adding mechanisms.

## Record authoritative state

Design records the current confirmed position. Decisions record material reasoning and rejected alternatives. Downstream outcomes consume the confirmed Design/defined outcome, not Decisions history.

Confirmed material must be written according to the governing Documentation Methodology rather than left only in conversation.

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v1`.

The package must make the required result, authority, work-specific inputs and acceptance clear. Do not embed generic execution-platform knowledge that is already supplied by the Build environment.

## Handle Build return

On Build Outcome:

- close/record completion when acceptance is satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

Build may resolve implementation detail within authority; it does not silently change objectives, major scope, acceptance or architecture.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

---

**Depends on:** `ProjectDesign_Design_v1`, `AIDE_Review@v1`.

**References:** `AIDE_Build@v1`, `AIDE_WorkPackage@v1`.

**Type definition:** `Standard` — outcome. Holds a published AI-facing behavioural contract derived from confirmed Design. Living/versioned by semantic release. Consuming AI environments.

**Methodology:** v17
<!-- END SOURCE: AIDE_ProjectDesign_Standard_v1.md -->

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

**Depends on:** None.

**References:** `Build_Design_v1`, `Build_WorkPackage_Design_v1`.

**Methodology:** v17
<!-- END SOURCE: Build_Decisions_v1.md -->

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

**Depends on:** `ProjectDesign_Design_v1`, `AIDE_Review@v1`.

**References:** `Build_WorkPackage_Design_v1`, `AIDE_WorkPackage@v1`.

**Methodology:** v17
<!-- END SOURCE: Build_Design_v1.md -->

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

**Depends on:** `ProjectDesign_Design_v1`, `Build_Design_v1`, `AIDE_Review@v1`.

**References:** `AIDE_WorkPackage@v1`, `DocumentationMethodology_Guide_v17`.

**Methodology:** v17
<!-- END SOURCE: Build_WorkPackage_Design_v1.md -->

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

**Depends on:** `Build_WorkPackage_Design_v1`, `AIDE_Review@v1`.

**References:** `AIDE_ProjectDesign@v1`, `AIDE_Build@v1`.

**Type definition:** `Standard` — outcome. Holds a published AI-facing behavioural contract derived from confirmed Design. Living/versioned by semantic release. Consuming AI environments.

**Methodology:** v17
<!-- END SOURCE: AIDE_WorkPackage_Standard_v1.md -->

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

**Depends on:** `Build_Design_v1`, `AIDE_WorkPackage@v1`.

**References:** `AIDE_ProjectDesign@v1`, `AIDE_Review@v1`.

**Type definition:** `Standard` — outcome. Holds a published AI-facing behavioural contract derived from confirmed Design. Living/versioned by semantic release. Consuming AI environments.

**Methodology:** v17
<!-- END SOURCE: AIDE_Build_Standard_v1.md -->

---

<!-- BEGIN SOURCE: PlatformDeployment_Decisions_Working_v1.md -->
# Platform Deployment — Decisions (Working)

> **Version 1** (2026-08-30). Records high-confidence Deployment design recommendations that can proceed independently of the still-pending top-level ownership/home decision.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## D1 — Target runtime/surface is separate from representation and channel

**Decision/recommendation.** Model runtime/surface, representation and distribution channel as distinct target facts.

**Reason.** OpenAI evidence demonstrated that the same local plugin representation was a valid Codex deployment, visible-but-not-executable in ChatGPT desktop Chat, and absent from ChatGPT web. Shared package shape did not imply shared deployment/runtime availability.

## D2 — Deployment Set is desired composition

**Decision/recommendation.** Treat a Deployment Set as a named desired composition rather than an append-only sequence of install/update/remove operations.

**Reason.** This collapses set lifecycle, replacement/removal and full-vs-incremental assembly into one reconciliation problem. Platform mechanics may rebuild or patch without changing semantics.

## D3 — Deployment Target is the unit of publication and verification

**Decision/recommendation.** One Set resolves to one or more Targets; each Target has its own surface, representation, channel, destination, refresh and verification contract.

**Reason.** Even a single provider family can require different routes for different surfaces.

## D4 — No generic cross-target transaction guarantee

**Decision/recommendation.** Do not claim universal atomic deployment/rollback across heterogeneous targets. Record per-target success and return Partial when the overall requested state is incomplete.

**Reason.** A generic transaction promise would be fictional on platforms that expose no rollback/transaction mechanism. Pre-publication validation and platform-specific rollback provide stronger truthful safety.

## D5 — Runtime verification is required where runtime use is the goal

**Decision/recommendation.** UI/install state is insufficient. Target verification includes a runtime content/use probe wherever the deployed object is meant to affect runtime behaviour.

**Reason.** ChatGPT desktop showed an installed/enabled plugin and updated package version while Chat runtime still could not access the skill body.

## D6 — Session state may differ from installed target state

**Decision/recommendation.** Record session pickup separately where a platform pins an active session to an older build.

**Reason.** Codex evidence showed an existing session remained on the old cache after reinstall while a new session used the updated build.

---

**Depends on:** `Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v2`.

**References:** `PlatformDeployment_Working_v1`.

**Methodology:** v17
<!-- END SOURCE: PlatformDeployment_Decisions_Working_v1.md -->

---

<!-- BEGIN SOURCE: PlatformDeployment_Working_v1.md -->
# Platform Deployment — Working

> **Version 1** (2026-08-30). Working design for the generic AI-platform Deployment contract. Ownership/home is intentionally pending the explicit architecture decision; the model is written generically so that decision does not need to be rediscovered.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## Layer 1 — intent / system view

### Purpose

Make built deployable material available in the intended AI runtime surfaces, reconcile changes/removals, and verify the **actual usable deployed state**.

### Premises

- Deployment starts after producer-specific design and Build.
- Deployment consumes declared package/manifest intent; it does not reopen the producer's Design.
- A shared representation does not imply a shared distribution route or runtime.
- Logical target, runtime surface, representation, distribution channel, physical destination and observed deployment state are separate facts.
- Deployment verification means runtime-appropriate evidence, not merely “the file/install exists.”

### Boundary

Producer/domain owns the logical artefact and any producer-specific package contract.

Build owns target-compatible **contributions** for the selected representation.

Platform Deployment owns set-aware composition, destination/channel resolution, publication/install/update/remove, resumption and verification.

Environment/platform configuration supplies physical target facts, access and channel details.

### Flow

```text
producer canonical outcome
      ↓
Build
      ↓
platform contribution(s)
      + producer Package/Manifest
      ↓
Platform Deployment
      ↓
resolve Deployment Set + target config
      ↓
compose desired target artefact/state
      ↓
publish/install/update/remove
      ↓
verify actual target/runtime state
      ↓
Deployment Result + Deployment State
```

---

## Layer 2 — model

### Deployment Set

A named logical **desired composition**. It groups the producer members that should be realised together for one or more configured targets.

The Set is semantic/logical. It does not itself mean plugin, bundle, repository, account or path.

### Deployment Target

One concrete runtime/surface realisation of a Deployment Set. A Target resolves at least:

- platform/family;
- runtime/surface;
- representation;
- distribution channel;
- physical destination/account/workspace where applicable; and
- verification/refresh requirements.

One logical Deployment Set may therefore have several Targets even inside one provider family.

### Representation

The target-compatible shape being deployed, for example a plugin, skill collection, project bundle, instruction file or another supported platform artefact.

### Distribution channel

How that representation reaches the target: local marketplace, hosted directory/publication, project-file upload/sync, repository, account/workspace install, filesystem path, or another supported route.

Representation and channel are independent dimensions.

### Deployment Config

Resolves a Deployment Set to its Targets and physical mechanics. Config is environment data, not producer design intent.

Conceptual shape:

```yaml
DeploymentSets:
  <set-name>:
    Targets:
      - Platform: <family>
        Surface: <runtime/surface>
        Representation: <shape>
        Channel: <distribution route>
        Destination: <logical/physical destination reference>
        Refresh: <where required>
        Verification: <required checks/probes>
```

Credentials/secrets are referenced through environment access mechanisms and are not embedded in a producer package/manifest or normal governed documentation.

### Deployment State

A factual record of what has actually been verified for one Target. It distinguishes at least:

- desired Set composition/revision;
- installed/published package or assembled artefact identity;
- member/capability identities and releases where exposed;
- representation/channel/surface;
- verification status and evidence time;
- runtime content availability; and
- session pickup state where the platform pins active sessions to an older build.

Installed state and active-session state may differ.

---

## Major rules

### 1. Reconcile desired state rather than model separate semantic install/update/remove systems

The Deployment Set expresses what should exist. Deployment calculates target actions required to move verified target state toward that desired composition.

`Install`, `Update`, `Replace` and `Remove` are operational consequences of reconciliation, not four unrelated lifecycle models.

This removes the full-vs-incremental question from generic semantics: a target adapter/composer may rebuild fully or patch incrementally, provided the same desired state and verification result are produced.

### 2. Build is capability/member-local; Deployment is set-aware

Build produces contributions for the individual producer/package. Deployment may combine contributions from many packages into a single target representation.

A Build contribution need not be independently deployable.

### 3. Composition is deterministic and conflicts fail visibly

For each Target, Deployment resolves all desired members and composes them according to the target representation contract.

If two contributions claim incompatible ownership/identity/path/namespace or cannot coexist under the target representation, composition fails for that Target. Deployment does not choose a winner silently.

### 4. No universal cross-target atomicity

Heterogeneous AI platforms do not provide a common transaction boundary. Generic Deployment therefore does not claim all-or-nothing atomicity across Targets.

The safe default is:

- validate/compose before publication where possible;
- preserve previously verified state when failure occurs before target mutation;
- record each Target independently;
- stop dependent target actions when their prerequisites fail; and
- use platform rollback only when the target contract actually supports it.

A partially completed multi-target deployment returns `Partial`, never false `Complete`.

### 5. Resumption is target-state reconciliation

Re-running the same desired Set is idempotent where the target mechanics allow it. Already verified matching Targets require no semantic redeployment. Failed/unverified Targets are retried from the observed state.

A new package build of the same semantic release can still require deployment because package/build identity and runtime pickup are separate facts.

### 6. Verification is layered and surface-specific

A Target is `Verified` only after the checks required by that Target have passed. Possible checks include:

1. package/artefact integrity;
2. destination publication/install acknowledgement;
3. directory/discovery visibility;
4. package/build version visibility;
5. member/capability identity visibility;
6. MigrationSummary/cheap metadata visibility where expected;
7. runtime content probe;
8. implicit/explicit trigger behaviour where applicable; and
9. update/session pickup behaviour where the runtime may pin an old build.

UI presence or “enabled” state is not sufficient where executable runtime content is required.

### 7. Removal follows desired composition

When a member is no longer desired in a Set, Deployment removes it from the target composition. Where a target representation is assembled, this may mean rebuilding the assembled artefact without that member; where the member is independently installed, it may mean uninstall/removal.

Explicit producer `Remove`/`Replace` intent remains useful for identity transitions and retirement, but the stable semantic goal is the resulting desired Set.

---

## Open ownership decision

**Recommended home:** `AIDE/Environment/Deployment` with common name **Platform Deployment** (or AI Platform Deployment in prose).

Reason: Deployment's intrinsic knowledge is runtime/surface/channel/destination/config/state. Capabilities is one producer and should retain capability-specific Package/Manifest and production workflow semantics without owning generic installation mechanics.

If Deployment remains temporarily under Capabilities, this Working model should still be used and its generic boundary preserved so later promotion is mechanical.

## Producer-manifest compatibility

The current Capability Manifest can be consumed as producer-specific input. A generic Deployment implementation can normalise its `Capability` identity to an opaque Set member identity internally.

If ownership is promoted, the cleaner later schema is a generic `Artifact/Member` identity rather than a capability-named field; that producer-contract migration should be done once during the ownership move rather than by adding another permanent adapter layer.

## Open empirical items — not architecture blockers

- hosted/public/account-synchronised OpenAI plugin deployment into ChatGPT runtime;
- broader Claude and other provider channel specifics;
- exact platform-specific composition rules for multi-member artefacts;
- platform-specific refresh/session pickup mechanics not yet observed.

These populate target adapters/config; they do not change the generic model unless evidence exposes a missing concept.

---

**Depends on:** `Capabilities_Design_v7`, `Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v2`.

**References:** `Build_Design_v1`, `AIDE_WorkPackage@v1`.

**Methodology:** v17
<!-- END SOURCE: PlatformDeployment_Working_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING.md -->
# Capabilities OpenAI Platform — Test Record

> **Version 3 WORKING** (2026-08-30 NZST). Consolidates the completed local-plugin evidence from v2 with the later standalone personal-skill surface tests. No further testing is required for tonight's architecture closure.
>
> This working record is intended to supersede v2 once incorporated into the Capabilities corpus/register.

---

## Objective

Establish enough empirical OpenAI surface behaviour to design Deployment without assuming that a shared skill/plugin representation implies shared installation, discovery or runtime availability.

Representative capability: `AIDE_Tags@v1`.

## Evidence retained from v2 — local marketplace plugin

The v2 controlled test established:

- the OpenAI plugin/skill representation validated successfully;
- Codex CLI discovered, installed, explicitly/implicitly executed, updated, removed and reinstalled the local marketplace plugin;
- Codex runtime exposed `AIDE_Tags@v1` and `MigrationSummary` from the skill description;
- an existing Codex session remained pinned to its prior plugin-cache build after reinstall while a new session picked up the updated build;
- ChatGPT Windows desktop displayed the locally installed plugin, publisher, capability identity and plugin build version, but Chat runtime could not load the skill body;
- ChatGPT web did not discover the locally installed marketplace/plugin on the same account; and
- UI/plugin-management state was therefore not proof of runtime capability availability.

### v2 hypothesis result

**Rejected:** one local marketplace/plugin installation is not a common end-to-end deployment route for Codex CLI, ChatGPT desktop Chat and ChatGPT web.

**Still possible but unproven:** one plugin-shaped source/representation may be usable through a future hosted/account-synchronised distribution route, but that would be a different channel and must be independently proven.

## Additional evidence — standalone personal skill

A separate personal standalone skill (`aide-tags-web-test`, capability identity `AIDE_Tags@v1`) was used to test whether standalone skill delivery supplied the missing common ChatGPT route.

Observed surface results:

| Surface | Result | Evidence treatment |
|---|---|---|
| ChatGPT web Work | Skill executed; implicit positive trigger and negative/non-trigger behaviour passed | Runtime evidence |
| ChatGPT desktop Cloud Work | Skill executed | Runtime evidence |
| ChatGPT web Chat | Installed standalone skill unavailable to Chat runtime | Runtime evidence |
| ChatGPT desktop Chat | Installed standalone skill unavailable to Chat runtime | Runtime evidence |
| Codex skill picker | Standalone personal skill was not discovered in the tested `$` skill picker | Discovery evidence |
| Local Work/filesystem-access test | Apparent access could be explained by direct filesystem inspection | Excluded as runtime-delivery evidence |

The changing StandaloneDeliveryProbe was used to distinguish current installed skill content from reconstructed/prior-context answers; exact probe values are not architecture inputs and are omitted here.

### Standalone-skill hypothesis result

**Rejected as a common private route:** the tested standalone personal skill is a real ChatGPT Work delivery mechanism but did not establish Chat-runtime or Codex delivery.

## Combined conclusions

1. **Representation, distribution channel and runtime surface are independent Deployment dimensions.**
2. A logical OpenAI Deployment Set may require multiple target realisations even inside one provider family.
3. Codex local marketplace plugin deployment is proven for the tested route.
4. ChatGPT Work personal standalone-skill delivery is proven for the tested Work surfaces.
5. ChatGPT Chat local/private runtime capability delivery remains unproven by both tested routes.
6. ChatGPT web must not be assumed to inherit local Codex/desktop plugin installation.
7. A project/context Binder remains the current known private/local fallback for Chat-style contexts where installed skill/plugin runtime delivery is unavailable.
8. Deployment verification must test the **runtime behaviour actually required**, not merely package visibility, enabled state or directory metadata.
9. Installed package state and active-session pickup may need separate state where sessions pin versions.
10. No evidence requires reopening the completed non-Deployment Capabilities model.

## Architecture gate

The OpenAI evidence is **complete enough for Deployment design**. Further OpenAI testing is optional follow-up for selecting a better hosted/account-synchronised Chat route, not a prerequisite to tonight's architecture closure.

## Remaining empirical work — follow-up only

- hosted/public/account-synchronised plugin route into ChatGPT Chat;
- multi-capability composition within a shared hosted representation;
- broader provider/platform routes where actual deployment is required.

---

**Type definition:** `TestRecord` — point-in-time empirical platform evidence. Supersedes earlier records when a later record explicitly carries their still-valid evidence. Internal.

**Depends on:** `AIDE_Tags@v1`, `AIDE_StandardsProduction@v1`, `AIDE_Migration@v1`.

**References:** `Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v2`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING.md -->

---

<!-- BEGIN SOURCE: Capabilities_DeploymentPromotion_ChangePlan_Working_v1.md -->
# Capabilities Deployment Promotion — Change Plan (Working)

> **Version 1** (2026-08-30). Mechanical corpus-change plan to apply if the recommended Platform Deployment ownership move is confirmed.

---

## Intent

Move generic Deployment ownership out of Capabilities without disturbing the completed capability-production architecture.

Capabilities remains responsible for producing canonical capabilities and capability-local Build/package intent. Platform Deployment becomes the owner of generic set-aware installation/publication/removal/verification into AI environments.

## Capabilities changes

### `Capabilities_Index` next version

- Remove Deployment as an owned child topic.
- Record Deployment as moved to the Environment/Platform Deployment workstream.
- Register the current OpenAI platform TestRecord as a local empirical evidence type/document if retained in this corpus.
- Keep `Standard`, `Tool` and `DocMethReviewItems` local custom types.

### `Capabilities_Brief` next version

Change eight peer components to seven:

```text
Standards
Tools
Tags
Scope
Dependencies
Migration
Review
```

Replace Deployment component ownership with an external interface:

```text
Capability Design
  → Build Capability
  → canonical capability
  → Build / Platform Contribution(s)
  → Capability Package + producer Deployment Manifest
  → AIDE Platform Deployment
```

Capabilities retains the producer-side Package/Manifest fields necessary to identify the capability package and its intended logical Deployment Set targets until the generic deployment schema deliberately replaces/generalises them.

### `Capabilities_Design` next version

- Remove Deployment from §2 owned architecture.
- Keep Build Config target platforms/side/Deployment Sets as producer intent.
- Keep capability-local Platform Contribution and Package production.
- Replace current Deployment section with **Platform Deployment interface**.
- State explicitly that a Capability Package is one producer-specific package accepted by generic Platform Deployment.
- Preserve all identity/release/package distinctions.
- Update principal flow so Deployment is outside the Capabilities ownership box.

### `Capabilities_Overview` next version

- Show seven owned components plus external Platform Deployment.
- Replace “Deployment fixed vs open” with “Deployment handed off/moved” and point to the new owning corpus.
- Record OpenAI evidence outcome: local shared-plugin route rejected; surface/representation/channel separated; no further test is a design prerequisite.

### `Capabilities_Decisions` next version

Append decisions:

1. Deployment is broader than Capabilities and moves to Platform Deployment ownership.
2. Capabilities remains a producer of Capability Package + deployment intent.
3. OpenAI local shared-plugin-route hypothesis rejected by v2/v3 evidence.
4. Representation, channel and runtime surface are separate deployment facts.
5. No non-Deployment Capabilities architecture is reopened by the evidence.

### `Capabilities_WorkRegister` next version

- Mark WR4 moved to Platform Deployment workstream rather than open Capabilities design.
- Update WR10: OpenAI evidence prerequisite complete; broader platform evidence remains empirical follow-up owned jointly by Build/Platform Deployment as targets are implemented.
- Keep WR12 DocMeth reconciliation until applied.
- Keep WR14 Environment/shared communication handoff separate.

### `Capabilities_OpenItems` next version

- Q1–Q3 move to Platform Deployment.
- Q11: close the immediate OpenAI hypothesis/evidence gate; retain broader per-platform implementation evidence as follow-up outside the core Capabilities architecture.
- Q9 Build Config inheritance/config remains external detail, to be resolved with Environment/Deployment configuration.
- Q12/Q13 remain external seams.

### Binder regeneration

Regenerate at minimum:

- `Capabilities_Binder_Core.md`
- `Capabilities_Binder_Work.md`
- `Capabilities_Binder_Set_ReadMe.md` if the registered source set changes.

Other Capabilities binders need regeneration only if cross-reference/footer content is changed in their constituent master documents.

## Core change

`Core_System_Design` next version:

- rename top-level **Design** concept to **Project Design**;
- update topic description and documentation folder naming decision once physical migration is chosen;
- remove Deployment from Capabilities list;
- add Platform Deployment under Environment if the ownership recommendation is confirmed;
- retain “side” as a working context independent of topic ownership.

## What does not change

- Tags, Scope, Dependencies, Migration and Review semantics;
- Build Capability Tool boundary;
- capability semantic release/version model;
- dependency conformance checkpoints;
- package build identity/integrity distinction;
- producer handoff rule that Build must not reopen Capability Design;
- WorkPackage ownership under AIDE Build.

---

**Depends on:** `Capabilities_Design_v7`, `Core_System_Design_v3`.

**References:** `PlatformDeployment_Working_v1`, `Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v3_WORKING`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_DeploymentPromotion_ChangePlan_Working_v1.md -->

---

<!-- BEGIN SOURCE: DocumentationMethodology_Reconciliation_Working_v1.md -->
# Documentation Methodology Reconciliation — Working

> **Version 1** (2026-08-30). Dispositions the twelve Capabilities→DocMeth review inputs against Documentation Methodology v17 and the completed Core/Tags/Dependencies/Migration contracts. One architecture decision remains open: whether DocMeth conformance becomes a normal dependency.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## Layer 1 — target boundary

Documentation Methodology should return to its narrow intrinsic job:

> **document naming, structure, metadata-container placement, document types and lifecycle.**

Generic reusable semantics live with their AIDE owner:

```text
Core Identity       → identity meaning
Tags                → tag generation/storage/query semantics
Dependencies        → dependency identity/presence/version/conformance semantics
Migration           → version-gap transition semantics/execution
Review              → independent review lifecycle
DocMeth             → where/how document-owned containers and properties are rendered
```

The document remains human-readable first. Machine metadata and temporary state are compact and extensible rather than forcing DocMeth to enumerate every future capability.

## Layer 2 — document model

```text
Title
Header metadata container
Temporary state container (only when state exists)
Body
Footer metadata container
Internal section (where applicable)
```

### Header metadata container

Holds compact metadata that identifies/describes the document as a referenceable artefact. Core Identity is the first known consumer; future owners may add blocks/properties without changing DocMeth.

### Temporary state container

Optional, visible near the top because unresolved operational state can materially affect safe use/update. Each entry has a stable owner and human-readable title/message. DocMeth owns placement/coexistence only.

Recommended compact rendering:

```text
State: Migration [AIDE_Migration] — v11 failed while targeting v12: source metadata unavailable.
```

Multiple owners use separate lines. The owner may update/remove only its own state.

### Footer metadata container

Holds durable document relationship/classification properties contributed by DocMeth or other owners.

Known examples, not a closed list:

```text
Tags: design, doctype:[design]
Dependencies: !AIDE_DocumentationMethodology@v18, abc@v4
References: pqr_Reference_v8
Type: Playbook — custom. Defined in ThisProject_Index.
```

`Tags` semantics belong to `AIDE_Tags`; `Dependencies` semantics belong to `AIDE_Dependencies`; `References` and custom-type rendering remain document-methodology concerns.

---

## Review-item dispositions

### DR1 — dependency semantics / footer hosting

**Disposition: split.**

- DocMeth retains footer container placement, generic formatting and document-specific `References` rendering.
- `AIDE_Dependencies` owns dependency grammar, identity/version/conformance meaning, generated dependency ownership and gap state.
- `AIDE_Migration` owns transition consequences.

Remove v17 prose that independently defines dependency change-impact/version behaviour where the generic contracts now answer it. DocMeth may state the document-specific reason a dependency is useful, but does not re-specify the engine.

### DR2 — `Methodology` footer line

**Disposition: pending architecture decision; recommendation = move to generic Dependencies.**

Recommended v18 model:

```text
Dependencies: !AIDE_DocumentationMethodology@v18, ...
```

The version is the document's last saved/proven conformance checkpoint to the methodology capability. A newer available methodology is therefore a normal Dependency Query + Migration problem.

Consequences:

- remove the project-wide invariant that every document must migrate simultaneously;
- allow Required/OnUpdate/None transitions per methodology release;
- migrate documents safely as required/use/update dictates;
- eliminate the specialised `Methodology:` version-gap mechanism.

If this recommendation is declined, keep `Methodology:` explicitly specialised and state why it is exempt from the generic model.

### DR3 — local document types

**Disposition: retain.**

DocMeth manages established shared types and the mechanism for declaring custom/local types. Domains own semantics/lifecycle of their custom types. Recurrence across domains is evidence for later promotion, not automatic promotion.

### DR4 — package manifest/build record

**Disposition: retain outside DocMeth.**

Do not create shared document types merely because Capabilities/Deployment uses a manifest or build record. Promote only on demonstrated cross-domain document lifecycle need.

### DR5 — existing shared types/metadata

**Disposition: no new mechanism.**

Overview and created/last-modified behaviour already exist; reconcile wording only where later decisions supersede it.

### DR6 — generic behaviour audit

**Disposition: move/split by owner.**

- classification generation/matching → Tags;
- semantic applicability → Scope;
- dependency presence/version/conformance → Dependencies;
- version transition/update reconciliation → Migration;
- independent assessment lifecycle → Review.

DocMeth retains only document-specific semantics (types, lifecycle, naming, records and physical metadata/state hosting).

### DR7 — document update and Migration

**Disposition: consume `AIDE_Migration`.**

A document update is a qualifying update event. `/update-doc` or equivalent document-update tooling should:

1. resolve Dependencies;
2. run applicable Required and pending OnUpdate migration through the save target as far as safely successful;
3. perform the requested local edit/update; and
4. persist only a saved/proven checkpoint.

Do not restate Migration's ordering/failure/checkpoint rules in DocMeth.

A local edit is not permission to semantically rewrite the whole document beyond applicable declared transitions.

### DR8 — generic metadata containers

**Disposition: adopt.**

DocMeth v18 explicitly defines extensible header/footer metadata containers and generic hosting rules. Block/property owners define their own contents and semantics.

### DR9 — Tags footer property

**Disposition: host only.**

Place `Tags:` in footer metadata. Do not define builder/group/query semantics in DocMeth.

### DR10 — Identity header metadata

**Disposition: host only.**

Place Core `Identity:` metadata in the header container for referenceable governed artefacts that expose a formal identity. Filename and formal identity remain distinct concepts.

### DR11 — temporary document state

**Disposition: adopt generic state container.**

Place compact owner-labelled temporary state after header metadata and before normal body content so material unresolved state is visible without searching the footer.

Minimum entry contract:

- stable owner identity;
- human-readable title/name;
- concise current message.

Owner defines lifecycle/content and may replace/remove only its own entry.

### DR12 — compact machine content

**Disposition: adopt as an authoring/rendering principle.**

For human-readable documents, metadata, derived data and machine-generated operational state should be as compact as practicable while remaining unambiguous and machine-usable. Rich diagnostics belong in the active work/session/result record unless durable document context genuinely requires them.

---

## Minimal v18 migration shape if DR2 recommendation is approved

A document conforming to v17:

```text
---
Depends on: abc_Design_v5
References: pqr_Reference_v8
Methodology: v17
```

migrates conceptually to:

```text
---
Dependencies: !AIDE_DocumentationMethodology@v18, abc_Design@v5
References: pqr_Reference_v8
```

Exact rendering of document identities is resolved against the Core identity and Dependencies contracts; this example shows semantics rather than prescribing whether an existing source document exposes a formal alternate identity.

The v18 release itself should carry a Required or OnUpdate transition posture based on the actual compatibility implications. Because the footer schema and conformance mechanism change, the transition is likely **OnUpdate** for documents that remain safely readable under v17 and **Required** only for an operation that requires v18-only metadata/state semantics. One version cannot mix postures, so the release design must choose the posture at release level rather than mixing item-level urgency.

## Items safely deferred beyond v18

- promoting Capabilities-local `Standard`/`Tool` document types absent wider recurrence;
- a richer temporary-state schema until multiple owners demonstrate a need;
- specialised metadata registry beyond owner-labelled blocks/properties;
- tooling/UI cadence for unmanaged-file review.

---

**Depends on:** `DocumentationMethodology_Guide_v17`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`, `AIDE_Tags@v1`, `Core_System_Design_v3`.

**References:** `Capabilities_DocMethReviewItems_v3`.

**Methodology:** v17
<!-- END SOURCE: DocumentationMethodology_Reconciliation_Working_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_Closure_Working_v1.md -->
# AIDE Closure — Working

> **Version 1** (2026-08-30). Closure map for making the current AIDE architecture operational while separating architecture blockers from empirical and deferrable work.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## Critical path

1. Formalise Project Design and Build behavioural contracts and WorkPackage handoff.
2. Resolve generic Platform Deployment ownership/home; then design the minimal operational Deployment contract from existing Package + Manifest evidence.
3. Reconcile Documentation Methodology with generic metadata/Dependencies/Migration boundaries.
4. Update Core/Capabilities affected ownership and current-state registers.
5. Regenerate project Binders and run cross-corpus consistency/readiness check.

## AI can close autonomously

- Project Design model/Standard from confirmed briefs.
- Build model/Standard and WorkPackage/Outcome contract.
- Domain-owned workflow boundary.
- Incorporation of completed OpenAI v2 deployment evidence: local shared-plugin route rejected; representation/channel/surface separated.
- Capabilities register updates once Deployment ownership is confirmed.
- Binder generation and consistency checks.
- Minimal Deployment failure/idempotency/verification mechanics once ownership is fixed.

## Design decision required

### Deployment ownership/home

Recommendation: promote generic Deployment from Capabilities to Environment as Platform Deployment, with Capabilities retaining producer-specific package/manifest responsibility and its capability production workflow.

### Documentation Methodology conformance

Recommendation: replace specialised project-wide `Methodology: vN` conformance with generic Dependencies + Migration semantics in the next DocMeth release; retain DocMeth ownership only of metadata placement/rendering and document-specific lifecycle/naming.

## Empirical/user action required — not blocking tonight's architecture

- Prove any future hosted/public/account-synchronised OpenAI plugin route before using it as ChatGPT runtime deployment.
- Broader Claude/other platform install/update/remove evidence where a concrete deployment is required.
- Supply/authorise credentials/accounts/repositories/physical destinations when actual Deployment Config is instantiated.

## Safe to defer

- exhaustive platform matrix coverage;
- generic shared inter-AI communication owner;
- complete Environment settings architecture beyond the minimum facts required by Platform Deployment;
- sophisticated atomic multi-target rollback where no platform can supply it reliably;
- standardisation of higher-level WorkPackage tier policy until consequence-based criteria are confirmed;
- future Build subcategories absent demonstrated need.

## Tomorrow-operational threshold

The system is sufficiently operational when:

- Project Design and Build have clear behavioural Standards;
- WorkPackage can be authored/executed/returned consistently;
- Capabilities can produce canonical outputs and hand built packages to a defined Deployment boundary;
- the current known OpenAI routes are represented truthfully rather than assumed;
- DocMeth has one coherent metadata/dependency/migration model (or, if not yet released, an explicit compatibility rule for v17); and
- all unresolved non-blockers are visible in registers rather than implicit.

---

**Depends on:** `ProjectDesign_Design_v1`, `Build_Design_v1`, `Capabilities_Design_v7`, `DocumentationMethodology_Guide_v17`.

**References:** `Capabilities_OpenAIPlatform_TestRecord_2026-08-30_v2`.

**Methodology:** v17
<!-- END SOURCE: AIDE_Closure_Working_v1.md -->

---
