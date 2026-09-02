# Build Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder version 5** (2026-09-01). Review B R1 clarification: deterministic-enough `Covers` mapping for deliberately split WorkRegister obligations.

## Binder manifest

- `Build_Index_v5.md` — sha256 `997b136e934e`
- `Build_Design_v5.md` — sha256 `442bf1f1d222`
- `Build_Decisions_v5.md` — sha256 `ee0c14c5deaa`
- `Build_WorkPackage_Design_v3.md` — sha256 `4dfc46fbca2f`
- `AIDE_Build_Standard_v5.md` — sha256 `6cf14a09d0f3`
- `AIDE_WorkPackage_Standard_v3.md` — sha256 `b07fe7d6cd5f`

---

<!-- BEGIN SOURCE: Build_Index_v5.md -->
# Build — Index

> **Version 5** (2026-09-01). Registers the Review B split-obligation coverage clarification while
> preserving WorkRegister ownership and WorkPackage/Outcome boundaries.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Build", type: DocumentationTopic}`

## Contents

- **Build** — generic objective-driven execution of defined work.  
  `{standard: AIDE_Build@v5}`
- **WorkPackage** — bounded Design-to-Build handoff and Outcome return contract.  
  `{standard: AIDE_WorkPackage@v3}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Build | AIDE | `Build` | independent | expanded |
| WorkPackage | Build | `Build_WorkPackage` | inherits | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `Build_Index` | v5 | Index | Current |
| `Build_Design` | v5 | Design | Current |
| `Build_Decisions` | v5 | Decisions | Current |
| `Build_WorkPackage_Design` | v3 | Design | Current |
| `AIDE_Build_Standard` | v5 | Standard | Current; identity `AIDE_Build@v5` |
| `AIDE_WorkPackage_Standard` | v3 | Standard | Current; identity `AIDE_WorkPackage@v3` |

### Relationships

- Project Design determines committed work and captures undelivered consequences in WorkRegister.
- WorkPackage may select a manageable subset of one or more WorkRegister obligations; deliberately split obligations require independently identifiable required changes and exact `Covers` mapping.
- Build returns Outcome evidence and per-source-obligation result information when mapped.
- The director/owning process reconciles WorkRegister; Build does not silently close it.
- Build remains upstream of AI Deployment for semantic representation/package production.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1
References: ProjectDesign_Design_v2, AIDE_Deployment@v4
<!-- END SOURCE: Build_Index_v5.md -->

---

<!-- BEGIN SOURCE: Build_Design_v5.md -->
# Build — Design

> **Version 5** (2026-09-01). Preserves the v4 Build/Deployment and WorkRegister ownership
> boundaries while clarifying deterministic-enough coverage for deliberately split WorkRegister obligations.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

## §1 — Purpose and boundary

Build is **objective-driven execution that takes defined work and produces required
artefacts/outcomes**.

It is not synonymous with software compilation or coding. A Build environment may create/modify
software, documents, datasets, websites, media/assets, packages, configuration or other
objective-driven outputs.

Build owns generic execution/handoff behaviour. It does not own the originating Design, the owning
top-level topic's WorkRegister, or target Deployment state.

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
   ↓
director reconciles source WorkRegister / Design
```

Build may be implemented by Codex, Claude Code, ChatGPT Work, Claude Co-work or other
execution-capable environments. The behavioural contract remains stable across products.

## §3 — WorkPackage and WorkRegister boundary

`AIDE_WorkPackage@v3` is the principal governed handoff into Build.

A WorkPackage supplies the work-specific definition and authority. The Build environment supplies
reusable execution knowledge, applicable Standards/Tools, platform mechanics and ordinary
implementation expertise.

Where a package is created from confirmed WorkRegister obligations, it carries the source item IDs
and the portion of each obligation included in that work chunk.

Where one source obligation is deliberately split across multiple WorkPackages, its required changes
must already be independently identifiable, normally as an owner-supplied enumerated/bulleted set.
Each package's `Covers` identifies exactly which required changes/portion it claims. Equivalent clear
prose is valid when unambiguous; structured sub-obligation identifiers are not required unless later
evidence establishes a need for them.

Build uses those mappings for traceability and result reporting only. WorkRegister remains owned by
the originating top-level topic/directing process. A WorkRegister row is not a substitute for a
self-contained executable WorkPackage.

Build must not require Design-history material merely to reconstruct the intended result. If the
WorkPackage/authoritative input is materially incomplete, return a design/input issue rather than
inventing policy.

## §4 — Build authority

Build may decide ordinary implementation details needed to achieve the defined outcome when:

- they remain within authorised scope;
- they do not change objective or acceptance;
- they do not transfer major ownership/responsibility; and
- the decision is not reserved by WorkPackage/applicable Standard.

Build returns rather than silently deciding changes to objective, major scope, acceptance,
architecture, policy or other substantive design authority.

## §5 — Planning and Review

Planning is proportionate. A separate elaborate plan is not mandatory for trivial work, but the
executor must establish a coherent sequence before consequential state change.

Where Review is required/recommended, use `AIDE_Review`; Build does not define another assessment
system.

## §6 — Execution and validation

Execution:

- uses applicable Standards/Tools;
- preserves defined authority/constraints;
- makes state changes deliberately and recoverably where practicable;
- surfaces failures/deviations rather than claiming completion; and
- records enough evidence to support validation and return.

Validation tests the actual result against WorkPackage Acceptance and relevant Standards.
Producing an artefact is not by itself proof the objective was satisfied.

## §7 — Outcome and WorkRegister result return

Every executed WorkPackage returns an Outcome sufficient for the director to understand:

- what was actually done;
- artefacts/state produced or changed;
- validation performed and results;
- deviations or authorised exceptions;
- unresolved/blocked work;
- out-of-scope findings; and
- any design question/follow-up required.

Where WorkRegister mappings were supplied, the Outcome additionally reports each mapped
obligation/covered portion and:

- result (`Complete | Partial | Blocked | Failed`);
- evidence relevant to that covered obligation; and
- remaining work where applicable.

Build reports evidence. It does **not** remove/close the owning WorkRegister row. The
director/top-level-topic owner reconciles the result against the full committed obligation and
current Design.

The Outcome is evidence, not a rewritten Design.

## §8 — Failure, partial completion and resumption

Build distinguishes Complete, Partial, Blocked and Failed. It does not erase safely completed work
merely to make a later failure appear atomic unless transaction-like rollback is explicitly
required.

Partial work is preserved only when safe/truthful; Outcome states actual state and what remains.
Re-running should resume/reproduce deliberately and avoid duplicate side effects where practicable.

## §9 — Canonical and derived representation

Where Build produces a platform or consumption representation of governed capability material, the
upstream canonical Standard/Tool or other authoritative outcome supplies semantic meaning.

Build may render, transform, assemble or package that meaning into a target-compatible form such as
a skill, plugin contribution, instruction representation, Bundle member, merged Bundle,
platform-specific file or other supported representation. The derived form must preserve
canonical semantics; Build does not reopen Decisions history to reconstruct/improve missing
capability meaning.

Derived representations are built from the **current authoritative inputs resolved for the work**.
An earlier Bundle, package, generated file or deployed copy is evidence about a previous derived
state, not authority for current canonical meaning/version when a current authoritative source
exists.

Build may produce any explicitly authorised subset/composition. It must not assume every AIDE
Standard is deployed only as part of full AIDE. Independently deployable Standards/future subsets
remain buildable unless their authoritative dependencies say otherwise.

Where upstream material defines distinct semantic roles, Build preserves those distinctions unless
an authorised representation combines them without changing meaning. Packaging convenience does
not collapse persistent bootstrap, Bootstrap Profile, thin Bootstrap Contribution and full
Standard/Tool into one semantic object.

For a generated/assembled representation, Build evidence identifies the authoritative source
identity/version set sufficiently for reproducibility and to avoid mistaking the derived artefact
for its source.

When Build output is intended for AI Deployment, the Build-to-Deployment handoff additionally
exposes, directly or through the applicable representation/package contract:

- **source provenance** — authoritative/canonical source identity/version set represented;
- **Build output identity and integrity** — enough evidence to identify the concrete Build result
  and detect substitution/change using an appropriate mechanism; and
- **composition posture** — `MemberContribution` or `AssembledConsumptionArtefact`.

Definitions:

- **MemberContribution** — target-compatible built member/contribution whose semantic content is
  already produced by Build and which Deployment may mechanically include/arrange/assemble with
  other built members without redefining semantics.
- **AssembledConsumptionArtefact** — authorised Build output whose internal semantic/member
  composition has already been assembled by Build. Deployment may deliver/reconcile it but a
  semantic/member-composition change requires another Build output.

These are required interface facts, not a mandatory universal manifest schema. An applicable
platform/package contract may encode them; otherwise Outcome/equivalent handoff evidence carries
them.

If authoritative input is insufficient to produce a correct representation, Build returns the
defect rather than inventing semantics during rendering.

## §10 — Platform implementation and AI Deployment boundary

Platform-specific commands, file layouts, skills/plugins, toolchains and environment mechanics
belong to platform Build knowledge/Tools, not this generic Design.

Build may produce a platform-compatible artefact/representation/package. **Production does not
establish installation, target reconciliation or runtime usability.**

AI Deployment owns target-state reconciliation, policy-aware delivery/install/update/remove and
verification. Deployment may mechanically assemble `MemberContribution` outputs and treats an
`AssembledConsumptionArtefact` as atomic at its internal semantic/member-composition boundary.

Build reports only the state it actually produced and validated within its scope.

## §11 — Intended outputs

```text
AIDE_Build@v5
AIDE_WorkPackage@v3
```

The v5/v3 transition posture is `None`: the release clarifies future split-obligation mapping
without requiring historical WorkPackage, Outcome or Build-output rewriting and without changing
WorkRegister ownership.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_WorkPackage@v3, AIDE_Review@v1
References: Build_WorkPackage_Design_v3, AIDE_Deployment@v4, AIDE_StandardsProduction@v1, ProjectDesign_Design_v2
<!-- END SOURCE: Build_Design_v5.md -->

---

<!-- BEGIN SOURCE: Build_Decisions_v5.md -->
# Build — Decisions

> **Version 5** (2026-09-01). Preserves the Build v4 boundaries and records the Review B
> clarification for deterministic-enough coverage of deliberately split WorkRegister obligations.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

## D1 — Retain Build and define it behaviourally

**Decision.** Retain **Build** as the AIDE area for objective-driven execution/creation. It is not
software compilation, coding or any particular product.

**Reason.** The common behaviour is taking defined work and producing/validating artefacts.

## D2 — WorkPackage is the principal governed handoff into Build

**Decision.** Build consumes a WorkPackage containing work-specific intent, authority, inputs,
outputs and acceptance; Build environments supply reusable implementation/platform knowledge.

## D3 — Build has bounded implementation authority

**Decision.** Build may resolve ordinary implementation detail within authorised scope but returns
objective, major scope, acceptance, architecture, policy or reserved design changes to the owner.

## D4 — Build standards describe behaviour, not products

**Decision.** Codex, Claude Code, ChatGPT Work, Claude Co-work and future systems are Build
environments/implementations. Generic Build Standards do not encode their product mechanics.

## D5 — Every executed WorkPackage returns evidence

**Decision.** Build returns an Outcome recording actual work, outputs, validation, deviations,
unresolved issues and design feedback.

## D6 — Canonical meaning remains upstream of platform/consumption representation

**Decision.** When Build renders or packages governed capability material, the current canonical
Standard/Tool or other authoritative outcome supplies semantics. Build does not reconstruct missing
meaning from Decisions history or from an older derived Bundle/package.

**Rejected alternative.** Patch an older Bundle/package forward as the production baseline.
Rejected because that would make a derived artefact authoritative by accident.

## D7 — Build preserves composability and semantic role boundaries

**Decision.** Build may produce explicitly authorised subsets/combinations without assuming one
fixed full-AIDE package. Distinct upstream semantic roles remain distinct unless an authorised
representation combines them without changing meaning.

## D8 — Build output is not Deployment state

**Decision.** Build may produce target-compatible artefacts/packages, but successful production does
not claim installation, target reconciliation or runtime availability. AI Deployment owns those
states.

## D9 — Deployment-facing Build output is identifiable and composition-typed

**Decision.** A Build output intended for AI Deployment exposes:

- authoritative source identity/version provenance;
- concrete Build-output/package identity and integrity evidence; and
- `CompositionPosture: MemberContribution | AssembledConsumptionArtefact`.

`MemberContribution` is semantically produced and may be mechanically assembled by Deployment.
`AssembledConsumptionArtefact` has Build-owned internal semantic/member composition; a composition
change requires another Build output.

**Reason.** Deployment must not infer semantic composition authority from file shape or payload
structure.

## D10 — WorkPackage can map manageable execution chunks to WorkRegister obligations

**Trigger / problem.** A confirmed Design consequence may be larger than one safe/manageable Build
unit, while one Build unit may efficiently deliver several related consequences. A one-to-one
WorkRegister/WorkPackage rule would distort either the obligation or the execution chunk.

**Decision.** `AIDE_WorkPackage@v2` permits a WorkPackage to identify some or all of one or more
WorkRegister items. One WorkRegister item may be delivered through several WorkPackages. The
mapping states the covered portion when the package does not satisfy the full obligation.

**Boundary.** WorkRegister mapping is traceability and reconciliation input. It does not replace the
WorkPackage's complete executable contract and does not grant Build authority to reinterpret Design
or the source obligation.

## D11 — Build returns mapped WorkRegister results but does not close the register

**Trigger / problem.** The directing/owning topic needs to know which part of each source obligation
was actually delivered, especially after Partial/Blocked returns. A generic Outcome summary alone
can force manual reconstruction.

**Decision.** Where the WorkPackage carries WorkRegister mappings, the Outcome reports a result for
each mapped obligation/portion, including evidence and remaining work where applicable.

The owning/directing process reconciles the source WorkRegister. Build does **not** remove or close
its rows.

**Reason.** Build owns execution evidence; the top-level topic owns the full committed consequence
and is the only place that can judge whether that obligation is fully discharged.

## D12 — Issue Build v4 and WorkPackage v2

**Decision.** Publish `AIDE_Build@v4` and `AIDE_WorkPackage@v2` with migration posture `None`.

**Reason.** The release strengthens future handoff/return traceability while preserving Build v3's
deployment-facing production contract. Historical WorkPackages do not require rewriting.

## D13 — Deliberately split obligations require independently identifiable coverage

**Trigger / problem.** Review B found that the existing many-to-many mapping permits one
WorkRegister obligation to be delivered through several WorkPackages but does not explicitly ensure
that each package's claimed portion can be distinguished deterministically enough for later
reconciliation.

**Decision.** Where one WorkRegister obligation is deliberately split across multiple WorkPackages,
the source obligation's required changes must be independently identifiable, normally as an
owner-supplied enumerated/bulleted set. Each WorkPackage `Covers` identifies the exact required
changes/portion it claims. Equivalent clear prose is valid when unambiguous.

Do not introduce structured sub-obligation identifiers merely to support the split unless later
evidence establishes that they are necessary.

**Boundary.** This clarification does not transfer WorkRegister authority to Build, replace the
self-contained WorkPackage contract, move Outcome evidence into WorkRegister, or change the existing
per-mapped-obligation Outcome result/evidence/remaining-work return.

## D14 — Issue Build v5 and WorkPackage v3

**Decision.** Publish `AIDE_Build@v5` and `AIDE_WorkPackage@v3` with migration posture `None`.

**Reason.** The release makes the accepted Review B mapping rule explicit while preserving the
existing ownership, handoff and Outcome reconciliation model. Historical WorkPackages and Outcomes
do not require rewriting.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_Design_v5
References: ProjectDesign_Design_v2, AIDE_Deployment@v4, AIDE_WorkPackage@v3
<!-- END SOURCE: Build_Decisions_v5.md -->

---

<!-- BEGIN SOURCE: Build_WorkPackage_Design_v3.md -->
# Build WorkPackage — Design

> **Version 3** (2026-09-01). Clarifies deterministic-enough `Covers` mapping when one source
> WorkRegister obligation is deliberately split across multiple WorkPackages.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

## §1 — Purpose

A WorkPackage is a bounded executable unit of defined work handed to Build. It states what Build is
authorised to do, with what inputs, for what result and how completion is established.

A WorkPackage may be created directly from defined work or may select some/all of one or more
WorkRegister obligations.

## §2 — Required contract

Every executable WorkPackage resolves:

- **Objective** — required result;
- **Authorised Scope** — what may be changed/created and explicit exclusions;
- **Inputs** — work-specific authoritative inputs;
- **Required Outputs** — artefacts/state to produce/change;
- **Acceptance** — observable completion/evidence conditions;
- **Constraints** — limits/dependencies/targets/reserved decisions;
- **Review posture** — explicit plan/result Review where applicable;
- **Return** — outcome destination/record; and
- **WorkRegister mapping** — when sourced from WorkRegister, the item IDs and covered obligation
  portion(s).

Optional context may help execution, but the package should not become a dump of design history.

## §3 — WorkRegister mapping

Conceptual representation:

```yaml
WorkRegisterItems:
  - Id: WR12
    Covers: "Comparer implementation and tests"
  - Id: WR13
    Covers: "Documentation update"
```

Equivalent prose is valid.

Rules:

- one WorkPackage may cover multiple items;
- one item may appear in several WorkPackages where delivery is deliberately chunked;
- where one source obligation is deliberately split across multiple WorkPackages, the obligation's
  required changes must be independently identifiable before mapping, normally as an
  owner-supplied enumerated/bulleted set;
- each package's `Covers` must identify the exact required changes/portion of that obligation this
  package claims;
- equivalent clear prose is valid where the claimed portion is unambiguous;
- do not introduce structured sub-obligation identifiers merely to support the split unless later
  evidence establishes that they are needed; and
- the mapping is traceability/reconciliation input, not authority to reinterpret the WorkRegister
  or Design.

## §4 — Self-containment boundary

Build must be able to understand required result/authority without reopening Decisions history.

WorkRegister references do not substitute for a complete WorkPackage. Include the actual
work-specific Design/inputs needed for execution.

If a material design choice remains unresolved, the package is NotReady.

## §5 — Review configuration

WorkPackage may configure `AIDE_Review` independently for planning and result review. Omitted
fields resolve through governing defaults.

## §6 — Execution contract

Build shall:

1. validate required inputs/authority;
2. validate WorkRegister mappings where supplied, including unambiguous `Covers` for deliberately split obligations;
3. establish a proportionate plan;
4. perform required/recommended Review;
5. execute within scope;
6. validate against Acceptance;
7. perform result Review where applicable; and
8. return truthful Outcome evidence including mapped obligation results.

Build may decide ordinary implementation detail within contract but may not silently alter the
objective, major scope, acceptance or reserved Design decisions.

## §7 — WorkPackage Outcome

Return at least:

- terminal status `Complete | Partial | Blocked | Failed`;
- work actually performed;
- produced/changed artefacts/state;
- validation/acceptance evidence;
- Reviews and material dispositions;
- deviations/authorised exceptions;
- unresolved/remaining work;
- out-of-scope findings;
- design questions/follow-up; and
- **WorkRegisterResults** when the package carried WorkRegister mapping.

Conceptual result mapping:

```yaml
WorkRegisterResults:
  - Id: WR12
    Result: Complete
    Evidence: <what proves the covered obligation was delivered>
    Remaining: None
  - Id: WR13
    Result: Partial
    Evidence: <what was completed>
    Remaining: <what is still owed>
```

Build reports these results. The owning/directing process decides how they reconcile the source
WorkRegister.

## §8 — Lifecycle

```text
Defined → Ready → Executing → Returned → Reconciled/Archived
```

`Reconciled` includes consumption of Outcome and source WorkRegister reconciliation where mapping
exists.

A blocked/partial return does not erase safe successful work; the Outcome states actual resulting
state.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_Design_v5, AIDE_Review@v1
References: ProjectDesign_Design_v2, AIDE_DocumentationMethodology@v21
<!-- END SOURCE: Build_WorkPackage_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_Build_Standard_v5.md -->
# AIDE Build — Standard

> **Identity:** `AIDE_Build@v5`
> **Common name:** Build
> **Version 5** (2026-09-01). Clarifies split-obligation WorkRegister coverage while preserving the v4 Build/Deployment and ownership boundaries.
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
- load applicable Standards/Tools needed for the work;
- where WorkRegister mappings are supplied, resolve the mapped item IDs and covered portions;
- where one source obligation is deliberately split across multiple WorkPackages, confirm its required changes are independently identifiable and this package's `Covers` is unambiguous; and
- return `NotReady`/Blocked if a substantive design gap prevents safe execution.

A WorkRegister mapping supplies traceability to a confirmed outstanding obligation; it does not
replace the WorkPackage's own Objective, Scope, Inputs, Outputs or Acceptance. For a deliberately
split obligation, independently identifiable required changes are normally supplied by the owner as
an enumerated/bulleted set; equivalent clear prose is valid. Do not require synthetic structured
sub-obligation identifiers unless a later governing contract establishes them.

Do not use design-history material as permission to invent a result that the current handoff does not determine.

When the required output is a platform or consumption representation of governed capability material, resolve the current canonical Standard/Tool or other authoritative outcome as the semantic source. Do not use an older Bundle, generated package or deployed copy to determine current canonical meaning/version where a current authoritative source establishes otherwise.

## Plan proportionately

Establish a coherent execution sequence proportionate to the work. Trivial work need not generate ceremonial plan artefacts.

Apply configured/governing Review before execution where required or recommended.

## Execute within authority

Resolve ordinary implementation detail autonomously where it remains within scope and does not alter objective, acceptance, major architecture/policy or reserved decisions.

If execution exposes a design-level problem, stop/contain affected work and return the issue rather than adding compensating machinery without authority.

If canonical/authoritative semantics are insufficient to produce a correct derived representation, return the defect to the owning Design/capability. Do not repair it by inventing capability meaning during Build.

## Build derived representations

Where authorised, Build may render, transform, assemble or package authoritative material into target-compatible forms such as skills, plugin contributions, instruction representations, Bundle members, merged Bundles, platform-specific files or other supported representations.

For such output:

- preserve the semantics of the authoritative source;
- build only the explicitly authorised subset/composition rather than assuming the full AIDE system;
- preserve distinct upstream roles and boundaries even when a platform rendering places several artefacts in one physical package;
- do not copy full Standards/Tools into thin contributions merely for packaging convenience; and
- record the authoritative source identity/version set used sufficiently for reproducibility and provenance.

A derived representation is a consumption/build artefact, not an authoritative replacement for its sources.

## Prepare deployment-facing Build output

When the Build output is intended for AI Deployment, expose these semantic handoff facts directly or through the applicable representation/package contract:

```yaml
BuildOutputHandoff:
  SourceProvenance: <authoritative/canonical source identities and versions>
  BuildOutput:
    Identity: <identity of the concrete built artefact/package>
    Integrity: <representation-appropriate integrity evidence>
  CompositionPosture: MemberContribution | AssembledConsumptionArtefact
```

Equivalent clear representation is valid; this Standard does not require one universal manifest format.

`MemberContribution` means the supplied item is already semantically produced by Build and may be mechanically included, arranged or assembled with other built members by AI Deployment as part of target reconciliation. Mechanical assembly must not redefine the member's semantics.

`AssembledConsumptionArtefact` means Build has already produced the authorised semantic/member composition. AI Deployment may deliver/reconcile that artefact but must not treat its contents as authority to semantically rebuild or change that composition. If the semantic/member composition must change, produce another Build output.

The Build output identity/integrity must be sufficient for the concrete result to be distinguished from another build or substituted/changed payload using the mechanism appropriate to that representation or package.

## Validate the result

Test actual outputs/state against the WorkPackage Acceptance and applicable Standards. Validation evidence should be sufficient to support the returned status.

For a derived representation, validation includes confirming that the selected authoritative sources and their material semantics are represented correctly for the target form. Where a deployment-facing handoff is required, also validate that the Build output identity/integrity and composition posture describe the actual produced output.

Apply result Review where required/recommended.

## Return outcome

Return an `AIDE_WorkPackage@v3` Outcome with truthful status, work performed, outputs, validation, deviations, remaining work, out-of-scope findings and design feedback. Where the WorkPackage mapped WorkRegister obligations, return a result/evidence/remaining-work entry for each mapped obligation or covered portion. Build reports this evidence; the owning/directing process reconciles and closes the WorkRegister.

`Complete` means the defined acceptance is satisfied, not merely that execution ended.

For deployment-facing built material, include or reference the required `BuildOutputHandoff` facts so downstream Deployment does not need to infer provenance, concrete build identity or composition authority from payload structure.

## Failure and resumption

Use `Partial`, `Blocked` or `Failed` distinctly. Preserve safe successful work where appropriate and state the actual resulting state. Re-running should resume or reproduce intentionally and avoid duplicate side effects where practicable.

## Platform and Deployment boundary

Target-platform commands, plugin/skill structures, repositories, toolchains and environment mechanics belong in platform Build Standards/Tools/configuration. They may vary without changing this contract.

Build may produce a platform-compatible artefact, representation or package. Successful Build does **not** mean that artefact is installed, deployed, reconciled with a target environment or verified as runtime-usable.

AI Deployment owns target-state reconciliation, delivery/install/update/remove actions and target/runtime verification. It may mechanically assemble outputs declared `MemberContribution`; it does not semantically reconstruct an `AssembledConsumptionArtefact`. Build must not report Deployment states unless they were separately established under the governing Deployment operation.

```yaml
MigrationSummary:
  CurrentVersion: v5
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None

Transition:
  Version: v5
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_Design_v5, AIDE_Review@v1
References: AIDE_WorkPackage@v3, AIDE_Deployment@v4, AIDE_StandardsProduction@v1
<!-- END SOURCE: AIDE_Build_Standard_v5.md -->

---

<!-- BEGIN SOURCE: AIDE_WorkPackage_Standard_v3.md -->
# AIDE WorkPackage — Standard

> **Identity:** `AIDE_WorkPackage@v3`
> **Common name:** WorkPackage
> **Version 3** (2026-09-01). Clarifies deterministic-enough coverage when one WorkRegister obligation is deliberately split across multiple WorkPackages.
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
  WorkRegisterItems: <optional source item IDs and covered portions>
```

Equivalent clear prose/sections are valid; the semantic fields matter, not this physical rendering.

If a material field is unresolved and cannot safely be inferred from authoritative inputs, the WorkPackage is NotReady.

## WorkRegister mapping

A WorkPackage may be created directly from defined work or may cover some/all of one or more
WorkRegister obligations. Where mapped, record each source item ID and the portion covered by this
package.

```yaml
WorkRegisterItems:
  - Id: WR12
    Covers: comparer implementation and tests
  - Id: WR13
    Covers: documentation update
```

One WorkRegister item may be delivered through several WorkPackages; one WorkPackage may cover
several items.

Where one source obligation is deliberately split across multiple WorkPackages:

- the source obligation's required changes must be independently identifiable, normally as an
  owner-supplied enumerated/bulleted set;
- each WorkPackage `Covers` must identify the exact required changes/portion it claims;
- equivalent clear prose is valid when unambiguous; and
- do not introduce structured sub-obligation identifiers merely to support the split unless later
  evidence establishes that they are needed.

Mapping is traceability and does not grant authority to reinterpret the source Design/WorkRegister.

## Handoff rule

Build should not need Decisions/design-history material to reconstruct the required result. Include work-specific authoritative artefacts needed for execution; do not duplicate generic execution/platform knowledge already supplied by the Build environment.

## Build authority

Build may choose ordinary implementation detail within Authorised Scope. It must return rather than silently change Objective, major scope, Acceptance, architecture/policy, or a decision explicitly reserved to the work owner.

## Review

Where the WorkPackage specifies plan/result Review, execute it under `AIDE_Review`; do not invent a WorkPackage-specific review method.

An omitted Review field does not disable governing Review requirements supplied by another applicable Standard/workflow.

## Execution

1. Validate inputs, authority, and any supplied WorkRegister mapping; for a deliberately split source obligation, require independently identifiable required changes and unambiguous `Covers`.
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
  WorkRegisterResults: <per mapped item/portion result, evidence and remaining work where applicable>
```

The persisted record may use concise document sections rather than YAML. For mapped WorkRegister work, report each item/covered portion as `Complete | Partial | Blocked | Failed`, with enough evidence and remaining-work detail for the owning/directing process to reconcile the source register. Build does not silently close the register.

## Partial/failure behaviour

Preserve successful work only where the resulting state is safe and accurately reportable. Do not hide partial completion. A retry/resumption starts from the actual returned state and must avoid duplicate side effects where practical.

## Lifecycle

`Defined → Ready → Executing → Returned → Reconciled/Archived`. `Reconciled` includes source WorkRegister reconciliation where mapping exists.

Documentation Methodology owns the file naming/archive mechanics; this Standard owns the WorkPackage execution semantics.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_WorkPackage_Design_v3, AIDE_Review@v1
References: AIDE_Build@v5, AIDE_ProjectDesign@v2
<!-- END SOURCE: AIDE_WorkPackage_Standard_v3.md -->
