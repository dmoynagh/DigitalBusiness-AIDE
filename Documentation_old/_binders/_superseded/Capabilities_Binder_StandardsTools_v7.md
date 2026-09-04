# Capabilities Binder StandardsTools

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 7** (2026-09-03). Review D R1 remediation: exact Definition checkpoints plus Capability Build/Builder mapping, frozen Tags and coordinated Registry batching.

This Binder is a current-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Capabilities_Standards_Definition_v4.md` — sha256 `8cbbbc2e9111`
- `Capabilities_Standards_Brief_v4.md` — sha256 `4a43f2a0b63e`
- `Capabilities_Standards_Design_v8.md` — sha256 `fd0fae89fa5c`
- `AIDE_StandardsProduction_Standard_v4.md` — sha256 `4090e11d0227`
- `AIDE_StandardsUsage_Standard_v2.md` — sha256 `4573304f05cf`
- `Capabilities_Tools_Definition_v5.md` — sha256 `3ef600955615`
- `Capabilities_Tools_Brief_v7.md` — sha256 `4ab2dfe2bfac`
- `Capabilities_Tools_Design_v7.md` — sha256 `ce021626eee8`
- `AIDE_ToolsProduction_Standard_v3.md` — sha256 `120a4c6dd6b3`
- `Capabilities_UpdateCapabilityElements_Tool_Design_v1.md` — sha256 `081be58d64ec`
- `AIDE_UpdateCapabilityElements_Tool_v1.md` — sha256 `797490b55005`
- `Capabilities_BuildCapability_Tool_Design_v6.md` — sha256 `1b42d8f14330`
- `AIDE_BuildCapability_Tool_v6.md` — sha256 `6f68217e29f2`
- `Capabilities_CapabilityBuilder_Tool_Design_v4.md` — sha256 `2ce238a8e45f`
- `AIDE_CapabilityBuilder_Tool_v4.md` — sha256 `e0869878f0ab`

---

<!-- BEGIN SOURCE: Capabilities_Standards_Definition_v4.md -->
# Standards — Capability Definition

> **Version 4** (2026-09-03). Replaces prose production state with exact evaluated-input checkpoints.

## Identity, purpose and boundary

**Capability:** `Standards@v2`

Defines canonical Standard production and runtime usage contracts.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Standards.Production` | Standard | `AIDE_StandardsProduction@v4` | v2 |
| `Standards.Usage` | Standard | `AIDE_StandardsUsage@v2` | v1 |

## Capability Release History

```text
Standards@v1
  Standards.Production@v1 -> AIDE_StandardsProduction@v3
  Standards.Usage@v1 -> AIDE_StandardsUsage@v2

Standards@v2
  Standards.Production@v2 -> AIDE_StandardsProduction@v4
  Standards.Usage@v1 -> AIDE_StandardsUsage@v2
```

This baseline adopts already-current canonical outcomes into the new Capability/Element release
model; it does not pretend those outcomes were newly changed on 2026-09-02.

## Element Release History

- `Standards.Production@v1` — baseline adoption of `AIDE_StandardsProduction@v3`; no new semantic change asserted.
- `Standards.Usage@v1` — baseline adoption of `AIDE_StandardsUsage@v2`; no new semantic change asserted.
- `Standards.Production@v2` — defines value-based Contents/Summary production for substantial canonical Standards.

## Element Production

```yaml
ElementProduction:
  Standards.Production:
    EvaluatedInputs:
      Capabilities_Standards_Design: v8
      AIDE_DocumentationMethodology: v28
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v2
  Standards.Usage:
    EvaluatedInputs:
      Capabilities_Standards_Design: v8
      AIDE_DocumentationMethodology: v28
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Standards_Design_v8, AIDE_StandardsProduction@v4, AIDE_StandardsUsage@v2
<!-- END SOURCE: Capabilities_Standards_Definition_v4.md -->

---

<!-- BEGIN SOURCE: Capabilities_Standards_Brief_v4.md -->
# Capabilities Standards — Brief

> **Version 4** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Standards.
>
> Created: 2026-08-27 | Last modified: 2026-09-02

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
- A substantial Standard can be understood and navigated from a concise semantic Contents/Summary
  entry without duplicating or cluttering small/self-evident outcomes.


## Current Definition

`Capabilities_Standards_Definition_v3` is the required capability-level control document; production uses `AIDE_StandardsProduction@v4`.

---

**Depends on:** `Capabilities_Design_v14`, `Capabilities_Standards_Design_v8`.

**References:** `Capabilities_Brief_v11`, `AIDE_Scope@v2`, `AIDE_Dependencies@v3`,
`AIDE_Migration@v3`.

**Methodology:** v28
<!-- END SOURCE: Capabilities_Standards_Brief_v4.md -->

---

<!-- BEGIN SOURCE: Capabilities_Standards_Design_v8.md -->
# Capabilities Standards — Design

> **Version 8** (2026-09-02). Defines value-based Contents/Summary orientation for canonical Standards.

---

## Contents

- **Standard semantics** — role, weights, chunkability, audiences and canonical contract. §1–§6
- **Production and shared capabilities** — Element production, references, Scope/Tags/Dependencies, Migration and Review. §7–§10
- **Runtime use and ownership** — conflict/deviation behaviour, boundaries and release production. §11–§13
- **Document orientation** — Standard-specific Contents/Summary applicability and depth. §14

## Summary

Standards defines the platform-independent contract for AI-facing Standards: weighted, addressable
rules that guide decisions and behaviour while remaining facilitative rather than enforcement-first.
Canonical Standards carry only consumer meaning plus shared Scope, Dependencies, Migration and
other owner-defined capability declarations; generic platform rendering belongs to Build.

Standard production distinguishes document revision from semantic Element release. It reassesses
documented inputs, advances only the evaluated-input checkpoint when meaning is unchanged, and
releases a new canonical outcome only when the semantics change.

Substantial Standards use Documentation Methodology Contents/Summary where this improves human and
machine comprehension/navigation. The Summary explains the high-level operating model, principal
rules/behaviours and important boundaries; small or already-scannable Standards omit the sections
when they would add clutter.

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
Capability Definition + documented production inputs
      ↓
Update Capability Elements
      ↓
canonical Standard Element + evaluated-input checkpoint
```

Update Capability Elements applies `AIDE_StandardsProduction@v4`. If reassessment finds unchanged
meaning, only `LastEvaluated` advances. If meaning changes, the canonical Standard is validated and
the next Element release/history is confirmed. Capability Build/package/Deployment remain later.

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

Standards may change existing consumers. Each changed Standard Element release follows `AIDE_Migration` and declares Required, OnUpdate, or None. Element release is distinct from source document version, containing Capability release/composition, Package identity and deployment state.

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


## §13 — Capability Element production

Standards are Capability Elements. Production resolves the current Capability Definition and
Element Production state, separates document revision from semantic Element release, and advances
`LastEvaluated` without a release when reassessment finds unchanged meaning. The current published
contract is `AIDE_StandardsProduction@v4`.

## §14 — Standard document orientation

Canonical Standard production consumes the generic Contents/Summary contract from Documentation
Methodology.

For a substantial Standard, use Contents to map significant rule/model areas and use Summary to
communicate the high-level operating model, principal rules/behaviours and important boundaries.
The precise weighted sections remain authoritative. The Summary must not flatten qualifications or
create another normative layer.

Apply the value/readability test: omit either section for small, immediately scannable or specialised
representations where it would duplicate existing structure or introduce more clutter than value.
Platform Build may render equivalent navigation suited to its retrieval model without changing
canonical meaning.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v14, Capabilities_Decisions_v20
References: Capabilities_Standards_Brief_v4, Capabilities_Tools_Design_v7, AIDE_Scope, AIDE_Dependencies, AIDE_Migration, AIDE_Review
<!-- END SOURCE: Capabilities_Standards_Design_v8.md -->

---

<!-- BEGIN SOURCE: AIDE_StandardsProduction_Standard_v4.md -->
# AIDE Standards Production — Standard

> **Identity:** `AIDE_StandardsProduction@v4`
> **Common name:** Standards Production
> **Version 4** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Standards.

## Contents

- **Purpose and release rule** — inputs, Element reassessment and release/checkpoint distinction.
- **Canonical orientation** — when Standard Contents/Summary applies and what it carries.
- **Output** — validated canonical Standard plus production/release result.

## Summary

Produce or validate one canonical Standard Element from confirmed inputs without inventing meaning.
Reassessment may advance only `LastEvaluated`; semantic change produces a new Element release.
Substantial Standards receive useful Contents/Summary orientation where it improves comprehension
and navigation without duplicating the precise weighted rules.

## Purpose and inputs

Produce or validate one canonical Standard Element from the current Capability Definition,
documented production inputs and applicable Scope/Dependencies/Migration contracts without inventing
meaning. Resolve Element identity/release, canonical outcome identity, prior release/history, Current
Migration and current production inputs.

## Rule

An input/document version change makes the Element potentially stale. Reassess it. If canonical
meaning is unchanged, advance only the Element Production `LastEvaluated` checkpoint. If meaning
changes, produce/validate the outcome, convert Current Migration into the immutable release entry and
confirm the next Element release. Document version and Element release are not the same.

Keep capability-reference roles distinct: Dependencies are conformance checkpoints, References are
reader/evidence pointers, and executable body references are versionless by default unless a specific
contract release is intentional.

## Canonical orientation

Apply `AIDE_DocumentationMethodology` and the Standards DocType rule. For a substantial canonical
Standard, provide:

- Contents — a concise semantic map of significant model/rule areas and stable locations; and
- Summary — the high-level operating model, principal rules/behaviours and important boundaries.

The detailed weighted body remains authoritative. Omit or use an equivalent structure where the
outcome is small/self-evident or the sections would add clutter, duplication or reduce usability.

## Output

Return the canonical Standard outcome plus production result, evaluated-input checkpoint and any
confirmed Element-release/history update. Do not perform platform Build/package/Deployment.

```yaml
MigrationSummary:
  CurrentVersion: v4
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Standards_Design_v8, AIDE_UpdateCapabilityElementsTool@v1
<!-- END SOURCE: AIDE_StandardsProduction_Standard_v4.md -->

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

<!-- BEGIN SOURCE: Capabilities_Tools_Definition_v5.md -->
# Tools — Capability Definition

> **Version 5** (2026-09-03). Releases executable Capability Build remediation and exact production checkpoints.

## Identity, purpose and boundary

**Capability:** `Tools@v5`

Defines canonical Tool production plus the current Capability production/build Tools.

This Definition controls Capability-level composition and production state. Detailed Element
semantics remain in the canonical outcomes identified below.

## Capability Elements

| Element | Type | Canonical outcome | Element release |
|---|---|---|---:|
| `Tools.Production` | Standard | `AIDE_ToolsProduction@v3` | v2 |
| `Tools.UpdateCapabilityElements` | Tool | `AIDE_UpdateCapabilityElementsTool@v1` | v1 |
| `Tools.BuildCapability` | Tool | `AIDE_BuildCapabilityTool@v6` | v4 |
| `Tools.CapabilityBuilder` | Tool | `AIDE_CapabilityBuilderTool@v4` | v4 |

## Capability Release History

```text
Tools@v1
  Tools.Production@v1 -> AIDE_ToolsProduction@v2
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v1 -> AIDE_BuildCapabilityTool@v3
  Tools.CapabilityBuilder@v1 -> AIDE_CapabilityBuilderTool@v1

Tools@v2
  Tools.Production@v1 -> AIDE_ToolsProduction@v2
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v2 -> AIDE_BuildCapabilityTool@v4
  Tools.CapabilityBuilder@v2 -> AIDE_CapabilityBuilderTool@v2

Tools@v3
  Tools.Production@v1 -> AIDE_ToolsProduction@v2
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v3 -> AIDE_BuildCapabilityTool@v5
  Tools.CapabilityBuilder@v3 -> AIDE_CapabilityBuilderTool@v3

Tools@v4
  Tools.Production@v2 -> AIDE_ToolsProduction@v3
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v3 -> AIDE_BuildCapabilityTool@v5
  Tools.CapabilityBuilder@v3 -> AIDE_CapabilityBuilderTool@v3

Tools@v5
  Tools.Production@v2 -> AIDE_ToolsProduction@v3
  Tools.UpdateCapabilityElements@v1 -> AIDE_UpdateCapabilityElementsTool@v1
  Tools.BuildCapability@v4 -> AIDE_BuildCapabilityTool@v6
  Tools.CapabilityBuilder@v4 -> AIDE_CapabilityBuilderTool@v4
```

`Tools@v4` advances only Tools.Production for the canonical Tool orientation contract. The other
Element releases remain unchanged.

## Element Release History

- `Tools.Production@v1` — baseline adoption of `AIDE_ToolsProduction@v2`; no new semantic change asserted.
- `Tools.Production@v2` — defines value-based Contents/Summary production for substantial canonical Tools.
- `Tools.UpdateCapabilityElements@v1` — baseline adoption of `AIDE_UpdateCapabilityElementsTool@v1`; no new semantic change asserted.
- `Tools.BuildCapability@v1` — baseline adoption of `AIDE_BuildCapabilityTool@v3`; no new semantic change asserted.
- `Tools.CapabilityBuilder@v1` — baseline adoption of `AIDE_CapabilityBuilderTool@v1`; no new semantic change asserted.
- `Tools.BuildCapability@v2` — resolves Registry publication to `AIDE_DeploymentRegistryTool@v1` and current `AIDE_CapabilityBuild@v2`.
- `Tools.CapabilityBuilder@v2` — emits the current immutable Capability Package Registry envelope and keeps post-Build result external.
- `Tools.BuildCapability@v3` — resolves effective Build Target Profiles/Definitions, applicability and target output obligations before WorkPackage authorisation.
- `Tools.CapabilityBuilder@v3` — produces complete applicable target contributions with exact Profile/Definition/output provenance.
- `Tools.BuildCapability@v4` — maps specialised facts deterministically into WorkPackage v3, fixes current-call migration wording and propagates coordinated Release Batch use.
- `Tools.CapabilityBuilder@v4` — validates snapshot-relative generated Tags before Package freeze and keeps post-Build workflow state outside Package bytes.

## Element Production

```yaml
ElementProduction:
  Tools.Production:
    EvaluatedInputs: {Capabilities_Tools_Design: v7, AIDE_DocumentationMethodology: v28}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v2
  Tools.UpdateCapabilityElements:
    EvaluatedInputs: {Capabilities_UpdateCapabilityElements_Tool_Design: v1, AIDE_Capability: v3}
    LastEvaluated: 2026-09-03
    Result: CurrentAtElementRelease-v1
  Tools.BuildCapability:
    EvaluatedInputs: {Capabilities_BuildCapability_Tool_Design: v6, AIDE_CapabilityBuild: v4}
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v4
  Tools.CapabilityBuilder:
    EvaluatedInputs: {Capabilities_CapabilityBuilder_Tool_Design: v4, AIDE_CapabilityBuild: v4}
    LastEvaluated: 2026-09-03
    Result: ReleasedElement-v4
```

Update the mutable checkpoint when sources/contracts are reassessed. An input-version change does
not by itself increment an Element release; immutable release-source snapshots stay in history when
later releases are produced.

## Current Migration

None. Authoritative existing outcome migrations remain under `AIDE_Migration`. A future Element
change carries Current Migration until release confirmation.

## Platform Definition and Build Platforms

The Capability is platform-neutral. Current generic Working Surface evidence must be resolved before
a Capability Build request. Newly supported platforms are surfaced and retain designer selection
`Build: null` until explicitly decided; unsupported plus `Build:true` is blocking.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Tools_Design_v7, AIDE_ToolsProduction@v3, AIDE_BuildCapabilityTool@v6, AIDE_CapabilityBuilderTool@v4
<!-- END SOURCE: Capabilities_Tools_Definition_v5.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tools_Brief_v7.md -->
# Capabilities Tools — Brief

> **Version 7** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Tools.

---

## Purpose

Tools owns the reusable model for invokable AI capability behaviour: how a Tool defines its
identity/actions, inputs, preconditions, procedure, bounded decisions, escalation, outputs,
reporting, failure handling, and idempotency.

A Tool removes the need to re-derive a repeatable action each time. It may orchestrate bounded
judgment explicitly defined by its contract, but does not silently take substantive authority that
belongs to the work owner or another capability.

## Output

Tools publishes `AIDE_ToolsProduction@v3`, the canonical production contract used by domains and
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
- A substantial Tool can be understood and navigated from a concise semantic Contents/Summary entry
  while small/self-evident Tools avoid redundant boilerplate.


## Current Tool set

Element update, Build request orchestration and Build-side execution are separate current Tools
under `Capabilities_Tools_Definition_v4`; Registry publication remains an AI-Deployment-owned
post-Build action.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v14, Capabilities_Tools_Design_v7
References: Capabilities_Brief_v13, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
<!-- END SOURCE: Capabilities_Tools_Brief_v7.md -->

---

<!-- BEGIN SOURCE: Capabilities_Tools_Design_v7.md -->
# Capabilities Tools — Design

> **Version 7** (2026-09-02). Defines value-based Contents/Summary orientation for canonical Tools.

---

## Contents

- **Tool semantics** — role, canonical structure and ask/infer/escalate discipline. §1–§3
- **Production boundaries** — Standards, Scope/Dependencies/Migration, canonical production and release identity. §4–§7
- **Operation and ownership** — reporting preferences, peer boundaries and current Tool family. §8–§10
- **Document orientation** — Tool-specific Contents/Summary applicability and depth. §11

## Summary

Tools defines repeatable invokable action contracts whose inputs, preconditions, procedure,
decisions, authority, effects, reporting and failure/idempotency behaviour do not need to be
re-derived on each use. Canonical Tool semantics are platform independent; concrete commands,
skills, UI actions and scripts belong to Build.

Tool production distinguishes document revision from semantic Element release and consumes shared
Scope, Dependencies and Migration rather than creating local substitutes. Substantial Tools use
Contents/Summary where valuable: the Summary communicates the intended outcome, overall flow, main
decision/effect points and important constraints; detailed action sections remain authoritative.

## §1 — Role and purpose

A Tool encapsulates a repeatable invokable action so its mechanism and safety checks are not
re-derived every time it is used.

Its value remains determinism of the action contract, encapsulation, lower repeated reasoning cost,
and completeness.

A Tool may contain bounded judgment where its contract explicitly defines how to infer, ask,
select, continue, or escalate. Genuine substantive authority remains with the work owner or the
capability that owns that judgment.

### Published production contract

This Design produces `AIDE_ToolsProduction@v3`, the published generic contract for producing and
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

`AIDE_UpdateCapabilityElementsTool` invokes `AIDE_ToolsProduction@v3` where documented production is required; directly authored Tool Elements and other authorised producers may consume the same contract. The
canonical Tool carries platform-independent action semantics plus capability-specific platform
addenda only. Generic skill/plugin/command-file/UI mechanics belong Build side.

## §7 — Version/release/package boundary

A Tool Element release is distinct from the DocMeth version of its sources and from the containing Capability release/composition. Package identity/integrity identifies a Build instance; Deployment state records what is installed. Neither is another Tool Element release.

## §8 — Reporting preferences

The four narration levels remain minimal, summary, detailed, verbose, defaulting to summary where
no stronger environment/user preference is available. The long-term storage home for account/
environment preferences remains external architecture work; Tools only consumes the resolved
preference.

## §9 — Ownership boundary

Tools owns the generic Tool/action contract and canonical Tool semantics. Shared peer components own
Scope, Dependencies, Migration, Review, Deployment, and platform implementation/build knowledge.


## §10 — Current production/build Tool family

- `AIDE_UpdateCapabilityElementsTool@v1` — design-side Element evaluation/production.
- `AIDE_BuildCapabilityTool@v5` — Build request/readiness/WorkPackage orchestration with effective Build Target Profile/Definition resolution.
- `AIDE_CapabilityBuilderTool@v3` — Build-side specialised executor producing complete applicable target contributions in the immutable Registry-compatible Capability Package.

`AIDE_BuildCapabilityTool@v2` remains historical and requires explicit migration; its production
role is not silently interpreted as v3. Tool Element production uses `AIDE_ToolsProduction@v3`.

## §11 — Tool document orientation

Canonical Tool production consumes the generic Contents/Summary contract from Documentation
Methodology.

For a substantial Tool, use Contents to map significant action/decision areas and use Summary to
communicate what the Tool accomplishes, its overall operating flow, main decision/effect points and
important constraints. Detailed inputs, preconditions, procedure, failure and idempotency sections
remain authoritative.

Apply the value/readability test. Omit either section for small/self-evident Tools or specialised
representations where an equivalent structure already serves the purpose or the sections would add
more clutter than navigation/comprehension value.

---
Dependencies: !AIDE_DocumentationMethodology@v28, Capabilities_Design_v14, Capabilities_Decisions_v20
References: Capabilities_Tools_Brief_v7, Capabilities_Standards_Design_v8, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
<!-- END SOURCE: Capabilities_Tools_Design_v7.md -->

---

<!-- BEGIN SOURCE: AIDE_ToolsProduction_Standard_v3.md -->
# AIDE Tools Production — Standard

> **Identity:** `AIDE_ToolsProduction@v3`
> **Common name:** Tools Production
> **Version 3** (2026-09-02). Adds value-based dual-audience Contents/Summary production for substantial Tools.

## Contents

- **Purpose and canonical contract** — complete platform-independent Tool semantics.
- **Release rule** — reassessment, LastEvaluated and semantic Element release behaviour.
- **Canonical orientation and output** — Contents/Summary applicability plus returned result.

## Summary

Produce or validate one complete canonical Tool Element from confirmed behaviour without inventing
authority or leaking platform mechanics. Reassessment may advance only `LastEvaluated`; changed
semantics produce a new Element release. Substantial Tools receive useful Contents/Summary
orientation where it improves comprehension and navigation.

## Purpose and inputs

Produce or validate one complete platform-independent canonical Tool Element from the current
Capability Definition, confirmed Tool behaviour and documented production inputs. Resolve Element
identity/release, logical actions, Scope, Dependencies, Migration, prior history and Current Migration.

## Canonical Tool contract

Specify stable outcome identity/common name; actions and triggers; inputs/defaults/preconditions;
ordered procedure and decision authority; escalation; outputs/effects; reporting; failure/partial/
idempotency/resumption semantics. Do not leak generic platform mechanics or infer new authority.

## Release rule

Reassess changed inputs. If Tool meaning is unchanged, update only `LastEvaluated`. If meaning
changes, validate the new canonical outcome, convert Current Migration and confirm the next Element
release. Document version, Element release and Capability release remain distinct.

## Canonical orientation

Apply `AIDE_DocumentationMethodology` and the Tools DocType rule. For a substantial canonical Tool,
provide:

- Contents — a concise map of significant action/decision areas and stable locations; and
- Summary — intended outcome, overall flow, principal decision/effect points and constraints.

Detailed inputs, procedure, failure and idempotency sections remain authoritative. Omit or use an
equivalent structure where the Tool is small/self-evident or the sections would add clutter,
duplication or reduce usability.

## Output

Return the canonical Tool plus production/checkpoint/release result. Platform Build/package/
Deployment remain later concerns.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v2, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v3
References: Capabilities_Tools_Design_v7, AIDE_UpdateCapabilityElementsTool@v1
<!-- END SOURCE: AIDE_ToolsProduction_Standard_v3.md -->

---

<!-- BEGIN SOURCE: Capabilities_UpdateCapabilityElements_Tool_Design_v1.md -->
# Capabilities Update Capability Elements Tool — Design

> **Version 1** (2026-09-02). Succeeds the canonical-element production role formerly carried by Build Capability v2.

## Purpose

Evaluate documented production inputs and produce/refresh/validate canonical Elements without
inventing meaning or creating false releases.

## Result rule

`input changed → reassess Element → semantic change?`

- no: advance `LastEvaluated`; retain Element release;
- yes: produce/validate the Element, convert Current Migration and confirm the next Element release;
- unresolved conflict/gap: return blocked/incomplete.

Directly authored Elements without derivation need not invoke this Tool.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_StandardsProduction@v3, AIDE_ToolsProduction@v2
References: Capabilities_Capability_Design_v1
<!-- END SOURCE: Capabilities_UpdateCapabilityElements_Tool_Design_v1.md -->

---

<!-- BEGIN SOURCE: AIDE_UpdateCapabilityElements_Tool_v1.md -->
# AIDE Update Capability Elements — Tool

> **Identity:** `AIDE_UpdateCapabilityElementsTool@v1`
> **Common name:** Update Capability Elements
> **Version 1** (2026-09-02). First design-side Element production/update Tool.

## Actions

`Evaluate | Update | Validate | Status`

## Procedure

1. Resolve the current Capability Definition, target Elements and documented Element Production inputs.
2. Compare each current input/version with its `LastEvaluated` checkpoint.
3. Reassess potentially stale Elements using the applicable production contract.
4. If meaning is unchanged, update only the evaluated checkpoint.
5. If meaning changes, update and validate the canonical Element, complete Current Migration and
   confirm the next Element release/history.
6. If current inputs conflict or are insufficient, return the smallest actionable defect; do not choose/invent.
7. Update the Capability release only if composition or substantive Capability-level Definition changed.

## Migration from Build Capability v2

Calls that used `AIDE_BuildCapabilityTool@v2` to produce canonical Standards/Tools migrate to this
Tool. Do not reinterpret an unreviewed v2 invocation as Build Capability v3.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_StandardsProduction@v3, AIDE_ToolsProduction@v2
References: Capabilities_UpdateCapabilityElements_Tool_Design_v1, AIDE_BuildCapabilityTool@v2
<!-- END SOURCE: AIDE_UpdateCapabilityElements_Tool_v1.md -->

---

<!-- BEGIN SOURCE: Capabilities_BuildCapability_Tool_Design_v6.md -->
# Capabilities Build Capability Tool — Design

> **Version 6** (2026-09-03). Defines the exact Capability-to-WorkPackage mapping and coordinated Registry workflow.

## Purpose

Check Capability Build readiness, resolve the effective Build Target Profile/Definitions and any
nominated Registry `Register` action, then produce/authorise the WorkPackage for Capability Builder
execution.

The specialised facts map into generic `AIDE_WorkPackage@v3` as follows: Definition, released
Elements, Build Platforms, exact source snapshot and Profile/Definitions are Inputs; required
target outputs and Capability Package are RequiredOutputs; applicability/conformance/degradation,
Tags, force scope and post-Build request are Constraints; package validation is Acceptance; and
Package evidence plus separate post-Build result is Return.

## Breaking transition

v2 produced canonical Standards/Tools. That responsibility moves to Update Capability Elements.
The v3 Required transition is not backwards-compatible by silent reinterpretation; existing v2
invocations/configuration must be reviewed and split/migrated. Calls retaining Build orchestration
use the current Tool release, not historical v3 merely because v3 is the migration checkpoint.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4, AIDE_WorkPackage@v3
References: AIDE_UpdateCapabilityElementsTool@v1, AIDE_CapabilityBuilderTool@v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
<!-- END SOURCE: Capabilities_BuildCapability_Tool_Design_v6.md -->

---

<!-- BEGIN SOURCE: AIDE_BuildCapability_Tool_v6.md -->
# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v6`
> **Common name:** Build Capability
> **Version 6** (2026-09-03). Makes WorkPackage mapping and coordinated post-Build Registry authority explicit.

## Actions

`Request | ValidateReadiness | Authorise | Status`

## Procedure

1. Resolve the current Capability Definition, released Elements/composition and production currency.
2. Require resolved Build Platforms and at least one explicit `Build:true`.
3. Resolve one unambiguous effective Build Target Profile/Definition set, including governed Profile
   membership/request selection and any Capability-specific overrides.
4. Resolve applicability, required reach, conformance/degradation permission and output Tags for
   every selected target; block unsupported applicable requirements rather than dropping them.
5. Resolve applicable Capability Build/platform rules, Registry-compatible package acceptance and
   explicit post-Build request. When Registry publication is requested, resolve
   `AIDE_DeploymentRegistryTool@v2` action `Register` and configured Registry. Direct registration
   is valid for an independent package; an established coordinated multi-package change requires
   the same Open Release Batch for every participating registration.
6. If an Element may be stale, return `UpdateElementsRequired`; do not produce it here.
7. Validate that the requested force scope, if any, cannot imply false semantic release changes.
8. Create/authorise the self-contained `AIDE_WorkPackage@v3` for Capability Builder:
   - Inputs carry Definition, released Elements, selected Build Platforms, exact source snapshot
     and effective Profile/Definitions;
   - RequiredOutputs carry all applicable required target outputs and the complete Package;
   - Constraints carry reach/applicability/conformance/degradation, required Tags, force scope and
     post-Build request/inputs or explicit none;
   - Acceptance carries freshness, target completeness, semantic preservation, provenance,
     integrity and package validation; and
   - Return requires Package/Build evidence plus separate post-Build/Registry state.
9. Return WorkPackage identity, readiness, selected platforms/targets, post-Build request and
   blockers. Keep actual post-Build result outside the validated package.

## Required migration from v2

`AIDE_BuildCapabilityTool@v2` canonical production calls move to
`AIDE_UpdateCapabilityElementsTool@v1`. Calls retaining Build-request orchestration use the current
`AIDE_BuildCapabilityTool` release; v3 names the Required transition checkpoint, not the release to
which current invocations are pinned.

```yaml
MigrationSummary:
  CurrentVersion: v6
  LatestRequiredVersion: v3
  LatestOnUpdateVersion: none

Transition:
  Version: v3
  Posture: Required
  Action: Review every v2 invocation; move Element production to AIDE_UpdateCapabilityElementsTool@v1 and retain only Build-request orchestration here.

Transition:
  Version: v4
  Posture: None

Transition:
  Version: v5
  Posture: None

Transition:
  Version: v6
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Capability@v3, AIDE_CapabilityBuild@v4, AIDE_WorkPackage@v3
References: Capabilities_BuildCapability_Tool_Design_v6, AIDE_UpdateCapabilityElementsTool@v1, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
<!-- END SOURCE: AIDE_BuildCapability_Tool_v6.md -->

---

<!-- BEGIN SOURCE: Capabilities_CapabilityBuilder_Tool_Design_v4.md -->
# Capabilities Capability Builder Tool — Design

> **Version 4** (2026-09-03). Adds snapshot-relative Tag validation and keeps post-Build workflow state outside Package bytes.

## Purpose

Execute an authorised Capability Build WorkPackage using `AIDE_CapabilityBuild` and applicable
platform/Profile rules, returning every applicable required Build Target contribution in a complete
validated Registry-compatible Capability Package plus separate Outcome/post-Build evidence.

## Boundary

The Builder does not change Capability/Element meaning, choose Build Platforms/Profile membership,
invent applicability/degradation, infer Registry contracts, write post-Build request/results into
immutable package bytes, regenerate frozen Tags from newer upstream state, or increment semantic
releases because it was forced/re-run.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4, AIDE_Build@v8, AIDE_Tags@v3
References: Capabilities_CapabilityBuild_Design_v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
<!-- END SOURCE: Capabilities_CapabilityBuilder_Tool_Design_v4.md -->

---

<!-- BEGIN SOURCE: AIDE_CapabilityBuilder_Tool_v4.md -->
# AIDE Capability Builder — Tool

> **Identity:** `AIDE_CapabilityBuilderTool@v4`
> **Common name:** Capability Builder
> **Version 4** (2026-09-03). Validates snapshot-relative Tags and executes post-Build workflow without freezing it into Package bytes.

## Procedure

1. Accept/validate the authorised WorkPackage under `AIDE_Build`.
2. Resolve current Definition, released Elements, selected Build Platforms, effective Build Target
   Profile/Definitions and applicable rules.
3. Determine affected internal work; reuse/cache only with valid provenance and integrity.
4. Build every selected platform and applicable required target output to the complete external
   contract. Do not silently omit a target or invent `NotApplicable`/degradation.
5. Run/validate applicable Tag Builders against the exact authoritative source snapshot resolved
   by the WorkPackage; fail visibly if freshness cannot be established.
6. Assemble the complete `CapabilityPackage` Registry envelope: Logical Package Identity,
   PackageId/integrity, Capability/Element composition, source/production/Build provenance,
   Profile/Definition revisions, complete Build Target output/member identities and integrity,
   Build-owned composition posture, effective Tags, reach/applicability/conformance/degradation,
   dependencies/Migration, tag-freshness/source-snapshot evidence and namespaced extensions.
7. Validate the complete Package against WorkPackage Acceptance.
8. Freeze the validated PackageId payload; do not write post-Build request, Registry receipt or
   lifecycle state into it.
9. Invoke the WorkPackage-nominated post-Build Tool if successful. Registry publication uses
   `AIDE_DeploymentRegistryTool@v2`; direct registration is valid for an independent package, while
   an established coordinated change requires the common Open Release Batch.
10. Return WorkPackage Outcome with actual Package and separate post-Build/Registry receipt state.

Force build never increments semantic releases. Missing/unknown required platform or governing
capability state blocks rather than being assumed.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4, AIDE_Build@v8, AIDE_WorkPackage@v3, AIDE_Tags@v3
References: Capabilities_CapabilityBuilder_Tool_Design_v4, Capabilities_BuildTargetProfile_Design_v2, AIDE_DeploymentRegistryTool@v2
<!-- END SOURCE: AIDE_CapabilityBuilder_Tool_v4.md -->
