# Capabilities StandardsTools Binder

> **Generated Binder — do not edit directly.** This file is a GPT Project consumption artefact, not an authoritative source document. Edit the individual master documents and regenerate the Binder.

Each source document below is included byte-for-byte unchanged between explicit source boundaries.

## Binder manifest

- `Capabilities_Standards_Brief_v2.md` — sha256 `0e273a5170ae`
- `Capabilities_Standards_Design_v4.md` — sha256 `e4f61f242744`
- `Capabilities_Tools_Brief_v2.md` — sha256 `76e7165a7267`
- `Capabilities_Tools_Design_v2.md` — sha256 `2f0e90d85908`

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

<!-- BEGIN SOURCE: Capabilities_Standards_Design_v4.md -->
# Capabilities Standards — Design

> **Version 4** (2026-08-29). Reconciles the Standards child design with the eight-component
> parent architecture, retaining the weight/facilitation model while consuming Tags, Scope,
> Dependencies, Migration, Review, Build, Package/Manifest, and Deployment boundaries.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

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

The Standards Usage outcome defines generic runtime behaviour. The retained resolution principles
are:

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

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Decisions_v12`.

**References:** `Capabilities_Standards_Brief_v2`, `Capabilities_Tools_Design_v2`,
`AIDE_Scope@v1`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`, `AIDE_Review@v1`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Standards_Design_v4.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tools_Brief_v2.md -->
# Capabilities Tools — Brief

> **Version 2** (2026-08-29). Reconciles Tools with the current Capabilities architecture,
> including shared Scope/Dependencies/Migration, logical commands, canonical production and
> Build-side platform rendering.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## Purpose

Tools owns the reusable model for invokable AI capability behaviour: how a Tool defines its
identity/actions, inputs, preconditions, procedure, bounded decisions, escalation, outputs,
reporting, failure handling, and idempotency.

A Tool removes the need to re-derive a repeatable action each time. It may orchestrate bounded
judgment explicitly defined by its contract, but does not silently take substantive authority that
belongs to the work owner or another capability.

## Output

The Tools child design defines the canonical Tool contract used by domains to produce individual
Tools. Platform Build Standards/Tools turn logical actions into target-specific skills, commands,
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

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Tools_Design_v2`.

**References:** `Capabilities_Brief_v5`, `AIDE_Scope@v1`, `AIDE_Dependencies@v2`,
`AIDE_Migration@v1`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Tools_Brief_v2.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tools_Design_v2.md -->
# Capabilities Tools — Design

> **Version 2** (2026-08-29). Reconciles Tools with shared Scope, Dependencies, Migration and
> Build-side platform realisation; retains the input/decision/reporting/idempotency model and
> permits bounded contract-defined judgment such as that used by the Review Tool.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## §1 — Role and purpose

A Tool encapsulates a repeatable invokable action so its mechanism and safety checks are not
re-derived every time it is used.

Its value remains determinism of the action contract, encapsulation, lower repeated reasoning cost,
and completeness.

A Tool may contain bounded judgment where its contract explicitly defines how to infer, ask,
select, continue, or escalate. Genuine substantive authority remains with the work owner or the
capability that owns that judgment.

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
Tool Design
   ↓
Build Capability
   ↓
canonical Tool
   ↓
Build WorkPackage
   ↓
platform Build Standards/Tools
   ↓
platform contribution
```

The canonical Tool carries platform-independent action semantics plus capability-specific platform
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

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Decisions_v12`.

**References:** `Capabilities_Tools_Brief_v2`, `Capabilities_Standards_Design_v4`,
`AIDE_Scope@v1`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`.

**Methodology:** v17
<!-- END SOURCE: Capabilities_Tools_Design_v2.md -->

---
