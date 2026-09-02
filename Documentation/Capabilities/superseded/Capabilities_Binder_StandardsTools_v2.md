# Capabilities StandardsTools Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 2** (2026-09-01). Carries Review C R2 runtime-consumer remediation through Standards Usage v2 while preserving the Tools Production architecture.

This Binder is a project-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Capabilities_Standards_Brief_v2.md` — sha256 `0e273a5170ae`
- `Capabilities_Standards_Design_v6.md` — sha256 `3bcf1be6e3df`
- `AIDE_StandardsProduction_Standard_v2.md` — sha256 `2d179e8f6edd`
- `AIDE_StandardsUsage_Standard_v2.md` — sha256 `4573304f05cf`
- `Capabilities_Tools_Brief_v3.md` — sha256 `45bb3d87b105`
- `Capabilities_Tools_Design_v3.md` — sha256 `b0659fcc867d`
- `AIDE_ToolsProduction_Standard_v1.md` — sha256 `c77ee2e1a330`
- `Capabilities_BuildCapability_Tool_Design_v2.md` — sha256 `e0beef1d5f87`
- `AIDE_BuildCapability_Tool_v2.md` — sha256 `923989b429ce`

---

<!-- BEGIN SOURCE: Capabilities_Standards_Brief_v2.md -->
# Capabilities Standards — Brief

> **Version 2** (2026-08-29). Reconciles Standards with the current Capabilities parent model and
> removes stale ownership of Scope, Tags, Migration, Deployment, and platform realisation.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## Purpose

Standards owns the reusable model for what an AI-facing Standard is, how its rules are structured
and weighted, how a canonical Standard is produced from confirmed design, and how sessions operate
under applicable Standards.

Individual domains own the substance of the Standards they produce.

## Outputs

Standards defines and ultimately publishes two generic outcomes:

- **Standards Production Standard** — authoring/structure/weight/canonical-production rules.
- **Standards Usage Standard** — discovery, interpretation, conflict/deviation, and operation under
  applicable Standards.

A domain may also produce an optional human Guide from the same design where useful.

## Required relationships

A canonical Standard:

- declares applicability through `AIDE_Scope`;
- declares dependencies through `AIDE_Dependencies`;
- declares version transition intent under `AIDE_Migration`;
- may contribute Tag/Dependency Builders where it owns the source semantics;
- uses Review where independent assessment adds value; and
- carries only capability-specific platform addenda. Generic platform implementation belongs Build
  side.

## Boundaries

Standards does not own Tags, Scope, Dependencies, Migration, Deployment, Review, WorkPackage, or
platform skill/plugin/bundle mechanics.

A Standard may describe a procedure but does not define a named invokable action; that is a Tool.

## Success signals

- A Standard author can produce one clear canonical Standard without inventing shared mechanisms.
- An extracted/chunked rule still carries its obligation weight and enough context to be used
  correctly.
- Platform builders can realise the same canonical Standard without reopening Capability Design.
- Runtime consumers can combine applicable Standards and surface genuine conflict/deviation rather
  than silently resolving it.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Standards_Design_v4`.

**References:** `Capabilities_Brief_v5`, `AIDE_Scope@v1`, `AIDE_Dependencies@v2`,
`AIDE_Migration@v1`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Standards_Brief_v2.md -->

---

<!-- BEGIN SOURCE: Capabilities_Standards_Design_v6.md -->
# Capabilities Standards — Design

> **Version 6** (2026-09-01). Carries Review C runtime tag-freshness and behind-current-checkpoint semantics into the Standards Usage source contract.

---

## §1 — Scope

Standards defines the Standard capability kind: role, rule/weight structure, canonical production,
and generic usage behaviour. It does not own individual domain Standards or shared mechanisms that
now have peer components.

## §2 — Role and purpose

A Standard provides guides, rules, advice and support focused on adding value and facilitating
effective work. Enforcement may be one of its roles but is never its primary lens; requirements are
framed through the consequence/value of meeting them.

A Standard shapes decisions and behaviour over a context. A named invokable action is a Tool.

## §3 — Weight system

Four weights remain:

- **Requirement** — must be met for the stated outcome/consumer to work; not open to ordinary
  judgment.
- **Expectation** — default position; departure is allowed but must be declared visibly.
- **Guidance** — default/best practice; departure is allowed and its consequences are owned.
- **Context** — information/reasoning with no obligation.

Every weighted unit states enough reason/consequence to preserve facilitation rather than bare
authority.

## §4 — Weight attachment and chunkability

Weight is a semantic property of addressable/chunkable Standard content.

- optional document default;
- every addressable section/unit carries its effective weight;
- statement-level override only where genuinely different.

Nearest declaration wins. Platform builders may render the semantic weight differently where the
target retrieval/chunking model needs another representation, but must not change its meaning.

## §5 — Outputs and audiences

Standards produces:

1. **Standards Production Standard** — for authors/builders of Standards.
2. **Standards Usage Standard** — for AI sessions operating under Standards.
3. Optional human **Guide** outcomes declared by individual capability designs.

The Standard is terse and complete; a Guide is explanatory. Both derive from the same Design and
may not disagree about substance.

## §6 — Canonical Standard contract

A canonical Standard contains only the capability meaning needed by consumers and Build, including
where applicable:

- formal identity/common name/release version;
- purpose and rules with effective weights;
- `AIDE_Scope` declarations;
- `AIDE_Dependencies` declarations;
- `AIDE_Migration` summary/transition declarations;
- owner-defined Tag/Dependency Builder definitions;
- Review expectations/profiles where the capability requires them; and
- capability-specific platform addenda.

Generic platform skill/plugin/bundle metadata does not belong in the canonical design contract.

## §7 — Production

```text
Capability Design
      ↓
Build Capability
      ↓
canonical Standard
      ↓
effective Build Config
      ↓
Build WorkPackage
```

Build Capability applies the Standards Production contract to confirmed design. The resulting
canonical Standard is the authoritative capability outcome passed to Build side. If Build side must
reopen the internal Capability Design to understand required capability behaviour, the canonical
outcome/WorkPackage is incomplete.

Platform realisation, contribution packaging, package/manifest construction, and Deployment belong
Build/Deployment side.

## §7a — Capability-reference validation

Canonical production distinguishes saved dependency checkpoints and reader References from current
executable capability instructions. Executable capability references are versionless by default. A
specific release is used only where the instruction deliberately depends on or targets that release;
production validates that the specificity is intentional and correct rather than mechanically
advancing it to the newest available release.

`References:` carries no currency or conformance obligation. Dependency checkpoint advancement
remains owned by `AIDE_Dependencies`/`AIDE_Migration`.

## §8 — Scope, Tags, and Dependencies

Standards consumes `AIDE_Scope`; it does not define another applicability language.

Standards may embed `AIDE_TagBuilder` or `AIDE_DependencyBuilder` blocks where that Standard owns the
semantics from which generated tags/dependencies are derived. Tags/Dependencies own builder
execution/storage/query contracts.

## §9 — Migration and release

Standards may change existing consumers. Each capability release therefore follows
`AIDE_Migration` and positively declares its version-level posture: Required, OnUpdate, or None.

The capability release version is distinct from the DocMeth version of the Design/Brief/source
documents used to author it. Package identity/build integrity and deployment state are also distinct
concepts under the parent contract.

## §10 — Review

Standards uses `AIDE_Review` rather than defining a local review mechanism. Production may select an
appropriate Review Profile for substantive integrity, weight justification, conflict, or other
capability-specific concerns.

Tone/facilitation quality is assessed through Review/judgment, not a mechanical publishing gate.

## §11 — Usage, conflict, and deviation

The Standards Usage outcome defines generic runtime behaviour. Before a Machine Scope result is
relied upon, the consumer honours the current-tag precondition supplied by `AIDE_Scope`/`AIDE_Tags`.
A dependency conformance checkpoint behind the available capability release is expected steady state
and is not by itself stale, missing, or an update trigger; applicable Required Migration remains the
affected-use gate.

The retained resolution principles are:

1. combine compatible Standards;
2. where genuine opposition exists, higher weight governs the point;
3. equal-weight genuine conflict is surfaced/escalated rather than silently resolved; and
4. direct human instruction may override a Standard, but the displaced Requirement/Expectation and
   consequence are surfaced/recorded as appropriate.

Scope determines whether the Standard is applicable before conflict resolution is considered.

## §12 — Ownership boundary

Standards owns Standard meaning, weight structure, canonical Standard production requirements, and
generic usage behaviour.

Peers own:

- Tags — classifications/builders/query;
- Scope — applicability;
- Dependencies — dependency/version state/order;
- Migration — transition semantics/execution;
- Review — independent assessment;
- Build — platform realisation/WorkPackage;
- Deployment — set-aware distribution/publication.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v11, Capabilities_Decisions_v16
References: Capabilities_Standards_Brief, Capabilities_Tools_Design, AIDE_Scope, AIDE_Dependencies, AIDE_Migration, AIDE_Review
<!-- END SOURCE: Capabilities_Standards_Design_v6.md -->

---

<!-- BEGIN SOURCE: AIDE_StandardsProduction_Standard_v2.md -->
# AIDE Standards Production — Standard

> **Identity:** `AIDE_StandardsProduction@v2`
> **Common name:** Standards Production
> **Version 2** (2026-09-01). Adds production-time capability-reference semantics from Review C while preserving the existing canonical Standard contract and weights.

---

## Purpose

Produce a canonical AI-facing Standard from confirmed Capability Design without introducing new
capability meaning during production.

This Standard governs the **canonical Standard outcome** only. Platform skill/plugin/bundle
realisation, packaging, WorkPackage execution, and Deployment are later concerns.

## Applicability

Apply when a confirmed Capability Design declares a Standard outcome or when an existing canonical
Standard is being rebuilt for a new capability release.

```yaml
Scope:
  Context: >
    Apply when producing or validating a canonical Standard from confirmed capability design.
```

## Required inputs

Resolve before production:

- the confirmed Capability Design and declared Standard output;
- formal capability identity and intended release version;
- applicable shared Standards, including Scope, Dependencies, Migration, and Review where used;
- any capability-specific platform addenda confirmed by the Design; and
- the previous canonical release/transition history where this is not the first release.

If capability meaning, release identity/version, or an authoritative input is materially ambiguous,
stop and return the gap to the work owner. Production does not fill design gaps by invention.

## Capability-reference semantics

During canonical production, distinguish reference roles rather than treating every version token as
a currency target:

- footer `Dependencies: X@vN` is a saved/proven conformance checkpoint owned by `AIDE_Dependencies`;
- footer `References:` is a reader/evidence pointer with no currency or conformance obligation; and
- a current executable in-body capability reference is an operational instruction.

Use a versionless identity for executable references by default. Name a specific capability release
only where the instruction deliberately depends on that release's contract or intentionally targets
it. Validate that any specific version is intentional and correct; do not mechanically advance every
body reference to the newest release.

## Canonical Standard contract

A canonical Standard contains only the capability meaning needed by its consumers and later Build.
Where applicable it carries:

- formal identity, common name, and capability release version;
- purpose and applicability;
- complete rules/guidance/context needed to operate under the capability;
- effective weight for every addressable/chunkable unit;
- `AIDE_Scope` declarations;
- `AIDE_Dependencies` declarations;
- `AIDE_Migration` summary and supported transition history;
- owner-defined Tag/Dependency Builder definitions;
- Review expectations/profile references where confirmed; and
- capability-specific platform addenda only.

Generic platform implementation metadata or mechanics do not belong in the canonical Standard.

## Weight production

Supported weights are:

```text
Requirement | Expectation | Guidance | Context
```

Every addressable unit must have an effective weight. Use the smallest clear representation:

1. an optional document default;
2. section/unit declaration where it differs or where no document default exists; and
3. statement/block override only where necessary.

Nearest declaration wins. A chunk with no effective weight is a production defect.

Weight meaning:

- `Requirement` — needed for the stated outcome/consumer to work; ordinary departure is not
  permitted.
- `Expectation` — default position; departure is allowed but must be made visible.
- `Guidance` — recommended/default practice; departure is allowed and its consequences are owned.
- `Context` — explanatory information with no obligation.

Requirements are expressed through consequence/value rather than bare authority.

## Production procedure

1. Read the confirmed Design and its declared outputs; do not use Decisions as an outcome input.
2. Resolve identity and intended capability release version.
3. Extract the complete confirmed Standard meaning, removing design-process reasoning that is not
   needed by consumers.
4. Preserve capability terminology and boundaries exactly; do not broaden ownership.
5. Apply the canonical Standard contract and effective weights.
6. Add shared Scope/Dependencies/Migration/Review declarations only where the Design requires them.
7. Carry forward supported transition history and update `MigrationSummary` for a later release.
8. Include only confirmed capability-specific platform addenda.
9. Validate completeness, internal coherence, dependency identities, transition continuity,
   capability-reference role/specificity, and chunk-level weight coverage.
10. Produce the canonical Standard and report any unresolved production defect rather than silently
    repairing the Design.

## First release and migration

A first release has no older consumer state to transform, but still declares positive transition
state so later tooling has an unambiguous history:

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

Later releases follow `AIDE_Migration` and retain the transition history required by the supported
baseline.

## Validation failures

Production fails visibly when, among other cases:

- Design does not determine required capability behaviour;
- declared output and Design disagree;
- identity/release version is unresolved;
- an addressable unit has no effective weight;
- Scope/Dependency/Migration declarations are contradictory or incomplete;
- a current executable capability reference is unintentionally stale or unjustifiably version-specific;
- a later release lacks required transition continuity; or
- platform-generic implementation has leaked into canonical capability meaning.

Return the smallest actionable defect set to the work owner. Do not create policy during repair.

## Output

The output is one canonical Standard for the declared capability release, ready for the normal
Build-side platform realisation flow.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Standards_Design_v5, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Tools_Design_v3, AIDE_BuildCapabilityTool
<!-- END SOURCE: AIDE_StandardsProduction_Standard_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_StandardsUsage_Standard_v2.md -->
# AIDE Standards Usage — Standard

> **Identity:** `AIDE_StandardsUsage@v2`
> **Common name:** Standards Usage
> **Version 2** (2026-09-01). Carries current Machine Scope tag-freshness and expected dependency-checkpoint lag into the runtime Standards consumer contract.
>
> **Default weight:** Requirement

---

## Purpose

Operate under applicable AI-facing Standards consistently while preserving declared weights,
Scope, dependencies, migration requirements, human authority, and visible handling of genuine
conflict or deviation.

## Applicability

Apply whenever an AI session relies on one or more governed Standards to perform, assess, or advise
work.

```yaml
Scope:
  Context: >
    Apply when governed Standards are available and relevant to the current work or action.
```

## Establish the applicable set

1. Discover the Standards available to the current execution context.
2. Resolve their formal identities and dependency state where relevant.
3. Before affected use, honour any applicable Required Migration under `AIDE_Migration`.
4. Before relying on Machine Scope, satisfy the current-tag freshness precondition owned by `AIDE_Scope`/`AIDE_Tags`; then evaluate `AIDE_Scope`. An item that is not applicable contributes no rule to the current work.
5. Use only the material needed for the current work while preserving each retrieved unit's
   effective weight and necessary context.

Do not treat installation/presence alone as applicability.

## Interpret weights

- `Requirement` — satisfy it for the stated outcome/consumer; if it cannot be satisfied, surface
  the consequence and do not silently claim conformance.
- `Expectation` — follow by default; if departing, make the departure visible.
- `Guidance` — follow where it adds value; departure is allowed and the resulting consequences are
  owned.
- `Context` — use as information/reasoning; it creates no obligation by itself.

A lower-weight statement does not silently cancel a higher-weight statement on the same point.

## Combine Standards

Compatible applicable Standards stack. Do not choose one merely because several apply.

When two applicable statements genuinely oppose each other on the same point:

1. higher weight governs;
2. equal-weight conflict is surfaced/escalated rather than silently resolved; and
3. the conflict record identifies the competing Standards/statements and the work affected.

Do not manufacture conflict from different concerns that can both be satisfied.

## Human instruction and deviation

Direct human/work-owner instruction may override a Standard within that person's authority.
When it displaces a Requirement or Expectation:

- state the Standard position and material consequence;
- make the departure visible in the appropriate work record where durability matters; and
- continue under the authorised instruction unless another non-overridable external constraint
  applies.

Guidance may be departed from without approval, but material consequences remain the responsibility
of the work owner/Lead.

## Missing, stale, or unresolved Standard state

- Missing required dependency → surface under `AIDE_Dependencies` and follow the governing
  operation's blocking posture.
- A dependency conformance checkpoint behind the available release is expected steady state and is not by itself stale, missing, or an update trigger; applicable Required Migration before affected use remains the gate.
- Required Migration outstanding → reconcile before affected use.
- Unsupported migration baseline or ambiguous transition → stop affected use and escalate.
- Unresolvable Standard identity/version → do not guess which contract governs.
- Genuine equal-weight conflict → escalate rather than select silently.

## Runtime economy

Prefer cheap applicability/version checks before loading detailed Standard material. Use
`MigrationSummary`, Scope machine filters, Tags, and platform discovery metadata where available,
then load only the detailed content needed for the work.

Performance optimisation must not change Standard meaning or hide an applicable Requirement.

## Reporting

Normal operation need not narrate every Standard consulted. Surface what materially affects the
work: blocking requirements, meaningful expectations/deviations, conflicts, migration state, or a
Standard-driven consequence the user/work owner needs to know.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Standards_Design_v6, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: AIDE_StandardsProduction
<!-- END SOURCE: AIDE_StandardsUsage_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tools_Brief_v3.md -->
# Capabilities Tools — Brief

> **Version 3** (2026-09-01). Publishes the Tools-owned canonical production contract and removes the need for Tool producers to reopen internal Tools Design.

---

## Purpose

Tools owns the reusable model for invokable AI capability behaviour: how a Tool defines its
identity/actions, inputs, preconditions, procedure, bounded decisions, escalation, outputs,
reporting, failure handling, and idempotency.

A Tool removes the need to re-derive a repeatable action each time. It may orchestrate bounded
judgment explicitly defined by its contract, but does not silently take substantive authority that
belongs to the work owner or another capability.

## Output

Tools publishes `AIDE_ToolsProduction@v1`, the canonical production contract used by domains and
Build Capability to produce/validate individual canonical Tools from confirmed Tool/Capability
Design. Platform Build Standards/Tools turn logical actions into target-specific skills, commands,
UI actions, scripts, or other representations.

## Required relationships

A Tool:

- declares applicability through `AIDE_Scope`;
- may declare dependencies through `AIDE_Dependencies`;
- may carry `AIDE_Migration` transition declarations where its release changes durable consumer
  state/configuration/contract;
- defines logical actions independently of their platform rendering; and
- reports what it did, what changed, and what needs attention.

## Boundaries

Tools does not own Scope, Tags, Dependencies, Migration, Review, Deployment, WorkPackage, or generic
platform implementation.

A Standard may describe procedure; a named invokable action is a Tool.

## Success signals

- A Tool can be invoked without re-deriving its mechanism.
- Inputs and decision/escalation boundaries are explicit.
- Re-running behaviour is known.
- Platform implementations preserve one logical action contract despite different command/skill
  representations.
- Durable release transitions are handled through the shared Migration contract rather than a
  Tool-specific version mechanism.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v10, Capabilities_Tools_Design_v3
References: Capabilities_Brief_v9, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
<!-- END SOURCE: Capabilities_Tools_Brief_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tools_Design_v3.md -->
# Capabilities Tools — Design

> **Version 3** (2026-09-01). Publishes the existing Tool contract as AIDE_ToolsProduction@v1 and makes it the canonical design-side Tool-production owner.

---

## §1 — Role and purpose

A Tool encapsulates a repeatable invokable action so its mechanism and safety checks are not
re-derived every time it is used.

Its value remains determinism of the action contract, encapsulation, lower repeated reasoning cost,
and completeness.

A Tool may contain bounded judgment where its contract explicitly defines how to infer, ask,
select, continue, or escalate. Genuine substantive authority remains with the work owner or the
capability that owns that judgment.

### Published production contract

This Design produces `AIDE_ToolsProduction@v1`, the published generic contract for producing and
validating canonical Tools from confirmed Tool/Capability Design. The structure below remains the
Tools-owned semantic source; downstream producers consume the published contract rather than
copying this internal Design.

## §2 — Canonical Tool structure

A Tool Design defines, in this order where applicable:

### Identity and logical actions

Stable Tool identity/common name and the logical actions/commands it contributes. Platform names
and invocation syntax are later renderings.

### Trigger and Scope

Explicit invocation plus contextual circumstances where the Tool should be selected proactively.
Applicability is declared through `AIDE_Scope`, not a Tools-local model.

### Purpose

A dense selection/retrieval statement describing the action/outcome.

### Inputs

For each input: requirement/default, resolution sources, and confirmation posture.

### Preconditions

Facts that must hold before changing state.

### Procedure

Ordered operational steps.

### Decision points

Visible branches and the rule/authority that resolves them. Do not hide substantive decisions in
procedure prose.

### Escalation conditions

Conditions where the Tool must hand back rather than invent policy/authority.

### Outputs and effects

Produced artefacts, changed state, persistent records.

### Reporting

Minimal/summary/detailed/verbose narration as appropriate; failures/deviations always surface.
Narration verbosity does not reduce the persisted record.

### Failure handling and idempotency

Partial-completion semantics, resumability/retry behaviour, and explicit idempotency declaration.

## §3 — Ask, infer, escalate

- infer and state where confidence is strong and cost of error low;
- ask once, preferably batched, for genuinely missing required inputs;
- escalate genuine conflicts, authority decisions, or material uncertainty the Tool does not own.

Never fail for want of information that could reasonably have been requested.

## §4 — Standards boundary

A Standard shapes behaviour/decision context. A Tool exposes a named invokable action.

A Standard may describe a procedure until a Tool exists; once an authoritative Tool owns the
action, the Standard points to it rather than duplicating the executable mechanism.

One Capability Design may produce sibling Standards and Tools from the same confirmed meaning.

## §5 — Scope, dependencies and migration

Tools consumes the shared contracts:

- Scope → whether the Tool/action applies;
- Dependencies → identities/version state the Tool relies on;
- Migration → release transitions affecting durable consumer state/configuration/contract.

Tools are **not categorically excluded from Migration**. If a Tool release has no existing durable
consumer state to transition, it declares `None`; if a real transition exists, it uses the same
Required/OnUpdate/None model as Standards.

## §6 — Canonical production and platform realisation

```text
Tool / Capability Design
   ↓
AIDE_ToolsProduction
   ↓
canonical Tool
   ↓
Build WorkPackage
   ↓
platform Build Standards/Tools
   ↓
platform contribution
```

`AIDE_BuildCapabilityTool` invokes `AIDE_ToolsProduction` when the confirmed Design declares a Tool
outcome; other authorised Tool producers may consume the same published contract directly. The
canonical Tool carries platform-independent action semantics plus capability-specific platform
addenda only. Generic skill/plugin/command-file/UI mechanics belong Build side.

## §7 — Version/release/package boundary

A Tool's formal capability release version is distinct from the DocMeth version of its Design.
Dependencies may track consumer conformance to the Tool capability version where relevant.

Package identity/integrity identifies a produced package of that release; Deployment state records
what package/release is installed. Neither is another Tool semantic version.

## §8 — Reporting preferences

The four narration levels remain minimal, summary, detailed, verbose, defaulting to summary where
no stronger environment/user preference is available. The long-term storage home for account/
environment preferences remains external architecture work; Tools only consumes the resolved
preference.

## §9 — Ownership boundary

Tools owns the generic Tool/action contract and canonical Tool semantics. Shared peer components own
Scope, Dependencies, Migration, Review, Deployment, and platform implementation/build knowledge.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v10, Capabilities_Decisions_v16
References: Capabilities_Tools_Brief_v3, Capabilities_Standards_Design_v5, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
<!-- END SOURCE: Capabilities_Tools_Design_v3.md -->

---

<!-- BEGIN SOURCE: AIDE_ToolsProduction_Standard_v1.md -->
# AIDE Tools Production — Standard

> **Identity:** `AIDE_ToolsProduction@v1`
> **Common name:** Tools Production
> **Version 1** (2026-09-01). First published Tools-owned contract for producing a canonical Tool
> from confirmed Tool/Capability Design.
>
> **Default weight:** Requirement

---

## Purpose

Produce a complete platform-independent canonical Tool from confirmed Tool/Capability Design without
inventing capability meaning during production or leaking generic platform implementation into the
canonical outcome.

## Applicability

Apply when confirmed Design declares a Tool outcome or when an existing canonical Tool is rebuilt
for a new capability release.

```yaml
Scope:
  Context: >
    Apply when producing or validating a canonical Tool from confirmed Tool/Capability Design.
```

## Required inputs

Resolve before production:

- confirmed Tool/Capability Design and declared Tool outcome;
- formal Tool identity, common name, logical actions and intended capability release version;
- applicable Scope, Dependencies and Migration contracts;
- capability-specific platform addenda confirmed by Design, if any;
- prior canonical release/transition history where this is not the first release; and
- current authority to produce or replace the outcome.

If substantive Tool behaviour, release identity/version or another authoritative input is materially
ambiguous, stop and return the gap to the work owner. Production does not repair Design by invention.

## Canonical Tool contract

A canonical Tool contains enough platform-independent information to implement the same logical
action contract on any supported platform:

1. stable identity/common name and logical actions;
2. trigger and `AIDE_Scope` applicability;
3. purpose;
4. inputs, defaults, resolution sources and confirmation posture;
5. preconditions;
6. ordered procedure;
7. explicit decision points and the rule/authority resolving them;
8. escalation conditions where the Tool must hand back rather than invent policy;
9. outputs/effects and persistent-state consequences;
10. reporting contract; and
11. failure, partial-completion, idempotency and resumption semantics.

A Tool may orchestrate bounded declared judgment. It does not acquire substantive authority absent
from its Design.

## Ask, infer and escalate

- infer where confidence is strong and cost of error is low;
- ask once, preferably batched, for genuinely missing required inputs; and
- escalate genuine conflicts, authority decisions or material uncertainty the Tool does not own.

Do not fail for information that can reasonably be requested, and do not convert a missing Design
decision into producer policy.

## Shared capability contracts

Use the shared owners rather than restating them:

- `AIDE_Scope` — applicability;
- `AIDE_Dependencies` — dependency/version/presence state;
- `AIDE_Migration` — release transitions affecting durable consumer state/configuration/contract.

Use versionless current executable capability identities by default. A specific version is valid
only where the instruction deliberately depends on or targets that release; validate such
specificity rather than mechanically advancing it.

## Production procedure

1. Read the confirmed Design and declared Tool outcome; Decisions are not downstream production
   input.
2. Resolve identity, common name, logical actions and intended release version.
3. Extract the complete confirmed Tool behaviour into the canonical Tool contract above.
4. Preserve capability terminology, ownership and authority boundaries exactly.
5. Add shared Scope/Dependencies/Migration declarations only as required by Design.
6. Carry supported transition history and update `MigrationSummary` for later releases.
7. Include only confirmed capability-specific platform addenda; exclude generic platform
   skill/plugin/command/UI mechanics.
8. Validate completeness, cross-action coherence, dependency identities, transition continuity,
   capability-reference specificity and idempotency/resumption behaviour.
9. Produce the canonical Tool or return the smallest actionable production-defect set.

## Validation failures

Fail visibly when, among other cases:

- Design does not determine required Tool behaviour;
- identity/release/logical actions are unresolved;
- a required input/precondition/decision/escalation/output/failure behaviour is missing;
- Scope/Dependency/Migration declarations contradict the Design;
- a current executable capability reference is unintentionally stale or unjustifiably
  version-specific;
- a later release lacks required transition continuity; or
- generic platform implementation has leaked into canonical Tool meaning.

## Output

The output is one canonical Tool for the declared capability release, ready for normal Build-side
platform realisation without reopening internal Tool Design.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Tools_Design_v3, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: AIDE_BuildCapabilityTool, AIDE_StandardsProduction
<!-- END SOURCE: AIDE_ToolsProduction_Standard_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_BuildCapability_Tool_Design_v2.md -->
# Capabilities Build Capability Tool — Design

> **Version 2** (2026-09-01). Consumes the published AIDE_ToolsProduction contract for Tool outcomes and removes duplicated/internal Tool-production ownership.

---

## §1 — Purpose and output

This Design produces one canonical **Build Capability Tool**.

Its job is:

```text
confirmed Capability Design
        ↓
Build Capability Tool
        ↓
canonical Standard / Tool outcome(s)
```

The Tool makes the existing production step explicit and repeatable. It applies the production
contract appropriate to each declared capability outcome and validates that the result is a
complete canonical handoff.

## §2 — Boundary

Build Capability is a **design-side canonical-production Tool**.

It owns:

- resolving the Design's declared canonical outputs;
- applying the Standards Production contract for Standard outcomes;
- applying the published Tools Production contract for Tool outcomes;
- preserving confirmed shared Scope/Dependencies/Migration/Review semantics;
- validating identity/release/output completeness; and
- producing canonical outcomes or a precise production defect report.

It does not own:

- capability design decisions or repair of incomplete Design;
- Build Config selection;
- WorkPackage creation/execution;
- target-platform skill/plugin/bundle/command implementation;
- Platform Contributions;
- Capability Package or Deployment Manifest construction; or
- Deployment Set composition/publication.

Those remain later Build/Deployment responsibilities.

## §3 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_BuildCapabilityTool@v2
  CommonName: Build Capability
  PrimaryInvocation: build-capability
  LogicalActions:
    - Build
    - Validate
    - Status
```

Platform invocation syntax is a Build-side representation detail.

## §4 — Trigger

Run when confirmed Capability Design is ready to produce/rebuild one or more canonical Standard or
Tool outcomes, or when the user/Lead asks to validate whether the Design can produce those outcomes
without reopening design.

The Tool may recommend itself when an outcome is about to be manually authored from Design and the
repeatable production contract would reduce drift.

## §5 — Inputs

Required/resolved inputs:

- target Capability Design;
- declared output set and output kinds;
- formal identity/common name for each canonical output;
- intended capability release version for each output;
- applicable canonical production contracts/shared Standards;
- previous canonical release and supported transition history where rebuilding a release line; and
- current work authority for producing the outcomes.

Release version is semantic capability state, not a file/package counter. If the intended release
identity/version is genuinely unresolved, the Tool asks/escalates rather than invents one.

## §6 — Build procedure

1. Read the confirmed Design and its declared outputs. Decisions may inform future Design changes
   but are not production input.
2. Confirm each output has one supported canonical kind: Standard or Tool.
3. Resolve formal identity and intended capability release version.
4. For a Standard outcome, execute `AIDE_StandardsProduction` against the Design.
5. For a Tool outcome, execute `AIDE_ToolsProduction` against the confirmed Design.
6. Preserve shared `AIDE_Scope`, `AIDE_Dependencies`, `AIDE_Migration`, and Review semantics exactly
   where confirmed by the Design.
7. Ensure later platform implementation has not leaked into the canonical outcome except for
   capability-specific platform addenda explicitly confirmed by Design.
8. Validate each outcome independently and the sibling set for contradiction/omission.
9. Produce the complete canonical outcome set or return production defects to the work owner.

The Tool does not repair Design by making a new substantive decision. If a required canonical
behaviour is not determined, the result is `DesignIncomplete` with the unresolved point identified.

## §7 — Tool outcome validation

For a Tool outcome, `AIDE_ToolsProduction@v1` owns the canonical Tool contract and validation rules.
Build Capability validates that the published production contract was applied successfully and that
the sibling canonical outcome set is mutually coherent; it does not maintain another copy of the
Tool structure.

## §8 — Validate action

`Validate` performs the same input/output completeness checks without producing/replacing the
canonical outcomes. Report at least:

- Design and declared output set;
- identity/release resolution;
- applicable production contract per output;
- missing/ambiguous canonical information;
- shared-contract consistency;
- cross-output contradiction; and
- Ready / NotReady result.

## §9 — Status and reporting

`Status` reports the target Design, declared outputs, current canonical output versions where
available, validation state, and next required production action.

Normal Build reporting is concise: outcomes produced, identities/releases, validation result, and
anything requiring attention. A production defect is always surfaced regardless of narration
preference.

## §10 — Idempotency

Building the same confirmed Design for the same capability release with unchanged production
contracts should produce substantively equivalent canonical outcomes. Re-running must not create a
new capability release merely because generation is repeated.

Package identity and physical platform output do not exist at this stage.

## §11 — Handoff

Successful output is the canonical capability set. The next boundary is:

```text
canonical capability
   + effective Build Config
   + Build WorkPackage
   + platform Build knowledge
        ↓
Platform Contribution(s)
```

Build Capability stops before that boundary.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v10, AIDE_StandardsProduction@v2, AIDE_ToolsProduction@v1
References: AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
<!-- END SOURCE: Capabilities_BuildCapability_Tool_Design_v2.md -->

---

<!-- BEGIN SOURCE: AIDE_BuildCapability_Tool_v2.md -->
# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v2`
> **Common name:** Build Capability
> **Version 2** (2026-09-01). Consumes AIDE_ToolsProduction@v1 for canonical Tool outcomes and removes the duplicated Tool-production contract.

---

## Purpose

Turn confirmed Capability Design into complete canonical Standard and/or Tool outcomes without
inventing new capability meaning and without crossing into platform Build or Deployment.

## Logical actions

```yaml
Tool:
  Identity: AIDE_BuildCapabilityTool@v2
  CommonName: Build Capability
  PrimaryInvocation: build-capability
  LogicalActions: [Build, Validate, Status]
```

## Trigger and inputs

Run when confirmed Capability Design is ready to produce/rebuild canonical outcomes, or when the
user/Lead asks whether that Design is production-ready.

Resolve the Design, its declared Standard/Tool outputs, formal identity/common name, intended
capability release version, applicable production contracts/shared Standards, previous release and
transition history where relevant, and current authority to produce the outcomes.

Do not infer a substantive design choice or semantic release version where the authoritative state
is ambiguous.

## Build

1. Read confirmed Capability Design and its declared outputs. Do not use Decisions as downstream
   production input.
2. Resolve each output kind, identity, and intended capability release version.
3. For each Standard, apply `AIDE_StandardsProduction`.
4. For each Tool, apply `AIDE_ToolsProduction`.
5. Preserve confirmed Scope, Dependencies, Migration, and Review semantics; do not restate their
   shared mechanisms inconsistently.
6. Exclude generic target-platform implementation. Include only capability-specific platform
   addenda explicitly confirmed by Design.
7. Validate each output and the sibling output set for completeness and contradiction.
8. Produce the canonical output set, or return a precise `DesignIncomplete`/production-defect result
   rather than repairing the Design by invention.

## Validate

Perform Build's readiness/completeness checks without replacing outputs. Return Ready/NotReady and
the smallest actionable set of missing/ambiguous inputs, shared-contract defects, or cross-output
contradictions.

## Status

Report target Design, declared outputs, resolved identities/releases, current canonical outcomes
where available, readiness, and next action.

## Boundary

Successful output is:

```text
canonical Standard / Tool outcome(s)
```

Build Capability stops there. Effective Build Config, WorkPackage, platform Build Standards/Tools,
Platform Contributions, Capability Package/Deployment Manifest, and Deployment are later stages.

## Failure and idempotency

- Missing design determination → stop and identify the unresolved point.
- Unresolved identity/release → ask/escalate; do not invent.
- Canonical/shared-contract contradiction → fail visibly.
- Re-running unchanged confirmed Design for the same release produces substantively equivalent
  canonical outcomes and does not create a new release solely because generation was repeated.

Normal reporting states outcomes produced/validated, identities/releases, and anything requiring
attention.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_BuildCapability_Tool_Design_v2, AIDE_StandardsProduction@v2, AIDE_ToolsProduction@v1
References: AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
<!-- END SOURCE: AIDE_BuildCapability_Tool_v2.md -->
