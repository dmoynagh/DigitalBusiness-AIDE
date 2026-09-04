# Capabilities Core Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 3** (2026-09-01). Applies Review C R1 remediation across the parent architecture and registers the remediated peer capability releases pending focused R2 verification.

This Binder is a project-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `Capabilities_Index_v17.md` — sha256 `ebe440c6e35a`
- `Capabilities_Brief_v9.md` — sha256 `ca436a6e3142`
- `Capabilities_Overview_v15.md` — sha256 `e362d24edbcc`
- `Capabilities_Design_v10.md` — sha256 `6f0b9cc78584`
- `Capabilities_Decisions_v16.md` — sha256 `dbff23758e54`

---

<!-- BEGIN SOURCE: Capabilities_Index_v17.md -->
# Capabilities — Index

> **Version 17** (2026-09-01). Registers the Review C R1 remediated capability set, including Tools Production v1 and current Dependencies/Migration/Tags/Scope/Review/Messaging releases, pending focused R2 verification.

`{scope: "AIDE/Capabilities", type: DocumentationTopic}`

## Contents

- **Capabilities** — reusable infrastructure for AI-facing Standards, Tools and supporting
  capability mechanisms.
  - **Standards** — canonical Standard production/usage contracts.
  - **Tools** — canonical Tool production/usage contracts.
  - **Tags** — metadata classification/query semantics.
  - **Scope** — applicability semantics.
  - **Dependencies** — dependency/conformance semantics.
  - **Migration** — transition/checkpoint semantics and Migration Tool.
  - **Review** — independent assessment semantics, profiles and Review Tool.
  - **Messaging** — AI-MESSAGE envelope/schema, message/thread identity, receipt/reconciliation,
    source/provenance, persistence semantics and messaging workflow/Tool.

## Documentation

### Top-level topic and subtopics

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Capabilities | AIDE | `Capabilities` | independent | expanded |
| Standards | Capabilities | `Capabilities_Standards` | inherits | expanded |
| Tools | Capabilities | `Capabilities_Tools` | inherits | expanded |
| Tags | Capabilities | `Capabilities_Tags` | inherits | expanded |
| Scope | Capabilities | `Capabilities_Scope` | inherits | expanded |
| Dependencies | Capabilities | `Capabilities_Dependencies` | inherits | expanded |
| Migration | Capabilities | `Capabilities_Migration` | inherits | expanded |
| Migration Tool | Migration | `Capabilities_Migration_Tool` | inherits | expanded |
| Build Capability Tool | Capabilities | `Capabilities_BuildCapability_Tool` | inherits | expanded |
| Review | Capabilities | `Capabilities_Review` | inherits | expanded |
| Review Tool | Review | `Capabilities_Review_Tool` | inherits | expanded |
| Messaging | Capabilities | `Capabilities_Messaging` | inherits | expanded |
| Messaging Tool | Messaging | `Capabilities_Messaging_Tool` | inherits | expanded |

WorkPackage belongs under `AIDE/Build/WorkPackage`.

### Document register — stable/current knowledge

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Capabilities_Index` | v16 | Index | established | Current |
| `Capabilities_Brief` | v9 | Brief | established | Current |
| `Capabilities_Design` | v10 | Design | established | Current |
| `Capabilities_Decisions` | v16 | Decisions | established | Current |
| `Capabilities_Overview` | v15 | Overview | established | Current architecture surface |
| `Capabilities_DocMethReviewItems` | v4 | DocMethReviewItems | custom | Current retained source; no longer active work state |
| `Capabilities_Tags_Design` | v2 | Design | established | Current |
| `AIDE_Tags_Standard` | v2 | Standard | custom | Current; identity `AIDE_Tags@v2` |
| `Capabilities_Scope_Design` | v2 | Design | established | Current |
| `AIDE_Scope_Standard` | v2 | Standard | custom | Current; identity `AIDE_Scope@v2` |
| `Capabilities_Dependencies_Design` | v3 | Design | established | Current |
| `AIDE_Dependencies_Standard` | v3 | Standard | custom | Current; identity `AIDE_Dependencies@v3` |
| `Capabilities_Migration_Brief` | v2 | Brief | established | Current |
| `Capabilities_Migration_Design` | v2 | Design | established | Current |
| `AIDE_Migration_Standard` | v2 | Standard | custom | Current; identity `AIDE_Migration@v2` |
| `Capabilities_Migration_Tool_Design` | v2 | Design | established | Current Tool source |
| `AIDE_Migration_Tool` | v2 | Tool | custom | Current; identity `AIDE_MigrationTool@v2` |
| `Capabilities_Review_Design` | v3 | Design | established | Current |
| `Capabilities_Review_Decisions` | v3 | Decisions | established | Current |
| `AIDE_Review_Standard` | v3 | Standard | custom | Current; identity `AIDE_Review@v3` |
| `AIDE_ReviewProfiles_Standard` | v2 | Standard | custom | Current; identity `AIDE_ReviewProfiles@v2` |
| `Capabilities_Review_Tool_Design` | v3 | Design | established | Current Tool source |
| `AIDE_Review_Tool` | v3 | Tool | custom | Current; identity `AIDE_ReviewTool@v3` |
| `Capabilities_Messaging_Brief` | v2 | Brief | established | Current |
| `Capabilities_Messaging_Design` | v2 | Design | established | Current |
| `Capabilities_Messaging_Decisions` | v2 | Decisions | established | Current |
| `AIDE_Messaging_Standard` | v2 | Standard | custom | Current; identity `AIDE_Messaging@v2` |
| `Capabilities_Messaging_Tool_Design` | v1 | Design | established | Current Tool source |
| `AIDE_Messaging_Tool` | v1 | Tool | custom | Current; identity `AIDE_MessagingTool@v1` |
| `Capabilities_Standards_Brief` | v2 | Brief | established | Current |
| `Capabilities_Standards_Design` | v5 | Design | established | Current |
| `AIDE_StandardsProduction_Standard` | v2 | Standard | custom | Current; identity `AIDE_StandardsProduction@v2` |
| `AIDE_StandardsUsage_Standard` | v1 | Standard | custom | Current; identity `AIDE_StandardsUsage@v1` |
| `Capabilities_Tools_Brief` | v3 | Brief | established | Current |
| `Capabilities_Tools_Design` | v3 | Design | established | Current |
| `AIDE_ToolsProduction_Standard` | v1 | Standard | custom | Current; identity `AIDE_ToolsProduction@v1` |
| `Capabilities_BuildCapability_Tool_Design` | v2 | Design | established | Current Tool source |
| `AIDE_BuildCapability_Tool` | v2 | Tool | custom | Current; identity `AIDE_BuildCapabilityTool@v2` |

### Live state — load separately

The stable Binder does not carry high-churn live state. Current versions are established from the
available files rather than repeated here.

- `Capabilities_WorkRegister` — confirmed outstanding work; currently includes peer architecture Review `WR17`.
- `Capabilities_OpenItems` — unresolved attention only.

The former `Capabilities_Messaging_WIP_v1` has been routed into authoritative Messaging masters and
is withdrawn from active state.

`Capabilities_Binder_Work.md` is no longer the normal consumption route for these registers under
v21; load the current live files directly when working on active state.

### Local configuration

#### Custom document types

| Type | Role | Holds | Lifecycle | Distribution |
|---|---|---|---|---|
| `DocMethReviewItems` | Review input | Consequences/questions for separate DocMeth review | Living until dispositioned | Internal |
| `Standard` | Outcome | Published AI-facing capability rules derived from Capability Design | Living/versioned by capability release | Consuming AI environments |
| `Tool` | Outcome | Published AI-facing invokable capability action derived from Tool Design/Capability Design | Living/versioned by capability release | Consuming AI environments |

Build Config inheritance/defaults remain environment/configuration detail. Generic Deployment
Config belongs to the AI Deployment workstream.

## Current priority

1. Complete focused Review C R2 verification of the remediated Capabilities architecture (`WR17`).
2. Resolve any material R2 finding before Review C closure.
3. Build lightweight platform-specific Bootstrap implementations where evidence warrants them.
4. Build/deploy the target-platform system through AIDE Build + AI Deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Index@v2, Capabilities_Design_v10
References: Capabilities_Overview_v15, Capabilities_Decisions_v16, Capabilities_Messaging_Design_v2, Capabilities_WorkRegister, Capabilities_OpenItems
<!-- END SOURCE: Capabilities_Index_v17.md -->

---

<!-- BEGIN SOURCE: Capabilities_Brief_v9.md -->
# Capabilities — Brief

> **Version 9** (2026-09-01). Applies Review C R1 architecture clarifications and records published Tools Production, reference-position semantics, tag freshness, correlation integrity and expected checkpoint lag.

---

## Purpose

Capabilities owns the reusable infrastructure by which AI-facing capabilities are defined,
classified, made applicable, connected to dependencies, transitioned across versions, built into
canonical outcomes, realised for platforms, packaged, deployed, and independently reviewed.

Everything exists to add practical AI-development capability or reduce a demonstrated risk.

## Required architecture

Eight peer components:

- **Standards** — Standard kind, weights, canonical production and generic usage.
- **Tools** — invokable action contract and logical commands.
- **Tags** — classification/build/query substrate.
- **Scope** — applicability using Tags plus AI context.
- **Dependencies** — dependency identity/presence/order, conformance and version-gap state.
- **Migration** — Required/OnUpdate/None transition authoring, discovery, ordering and execution.
- **Review** — purposeful independent assessment for insight, integrity, decisions and risk.
- **Messaging** — platform-neutral AI-MESSAGE semantics, correlation, receipt integrity and
  cross-context communication workflow.

AIDE Build owns WorkPackage and generic platform execution/handoff.

## Production and handoff

```text
Capability Design
      ↓
Build Capability Tool
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage

BUILD SIDE
canonical capability + WorkPackage + platform Build knowledge
      ↓
Platform contribution(s)
      ↓
Capability Package + Deployment Manifest
      ↓
Deployment
```

`AIDE_BuildCapabilityTool` is the canonical design-side producer for this step. It applies the published
Standards/Tools production contracts and fails back to the work owner rather than inventing missing
Design. Canonical outcomes contain complete capability meaning plus only capability-specific
platform addenda. Generic skill/plugin/bundle/command implementation belongs Build side.

## Shared contracts

### Tags and Scope

Semantic owners generate explicit tags through owner-defined Tag Builders. Scope consumes exact
Boolean tag queries plus optional AI-interpreted Context Scope. Missing Scope layers are
unrestricted; explicit disabled means never applies.

### Dependencies

Resolve identity first and version second. `!` means required on relevant use; `!!` additionally
requests best-effort startup presence checking. `X@vN` records the last saved/proven consumer
conformance checkpoint and creates no execution order; behind-current checkpoints are normal until a
qualifying save proves newer conformance. `X@!vN` is a hard present exact-version constraint.
Dependency declaration order supplies default processing precedence only where processing order is
actually required. `References:` carries no currency/conformance obligation; current executable
capability references are normally versionless unless they intentionally target a specific release.

### Migration

Every migratable capability release positively declares `Required`, `OnUpdate`, or `None`.
Required is checked before affected use; OnUpdate waits for the next modification/save.
`MigrationSummary` supports cheap discovery; detailed history is loaded only when necessary.
Checkpoints advance only with saved proven artefact state. Migration is resumable and records
compact owner-labelled unresolved state through the document methodology's generic state mechanism.

## Version/release/package distinctions

Keep separate:

- DocMeth document version;
- canonical capability release version;
- consumer dependency conformance version;
- package build identity/integrity; and
- factual deployment state.

Package rebuilds do not create a new capability release version unless capability meaning changed.

## Package and Deployment Manifest

A Capability Package is the capability-local payload for one capability release. Its `PackageId`
and integrity data identify the concrete build.

The Deployment Manifest supplies logical placement/lifecycle intent only: package/capability
identity, Deployment Set/platform targets, package-local contribution selection, explicit
replace/remove intent where required, and integrity. Physical destinations belong Deployment
Config.

Deployment must not reopen Capability Design or infer intent from payload structure.

## AI Deployment boundary

Generic deployment is no longer owned by Capabilities.

Capabilities owns:

- canonical capability production;
- capability-local Platform Contributions produced through Build;
- Capability Package/build identity and integrity; and
- logical deployment intent sufficient for the deployment consumer.

`AIDE_Deployment@v1` owns generic Deployment Set/Target reconciliation, representation/channel/
surface resolution, composition, publication/install/update/remove and runtime verification.

OpenAI evidence has closed the immediate architecture gate: a local plugin/skill representation
cannot be assumed to provide one common ChatGPT + Codex runtime route. Surface, representation and
distribution channel are separate deployment facts.

## Review and Messaging boundary

Review owns the independent-assessment lifecycle and substantive Review request/response semantics.
Messaging owns AI-MESSAGE relay, message correlation, receipt/reconciliation and Messaging actions.
Environment/platform configuration still supplies current reviewer/model/route facts and concrete
route availability.

Messaging keeps ordinary exchanges in conversation, uses WIP/OpenItems only where persistence is
actually needed, and persists a Message document only when the body itself requires independent
retrieval. STATE evidence is only as strong as retained evidence; explicit Ack supplies positive
receipt proof when needed. Review/Round correlation remains authoritative for Review semantics and a
positive mismatch with Messaging transport correlation is quarantined. Documentation Methodology
supplies the generic governed-document mechanics.

## Success signals

- Build side does not need to reopen Capability Design.
- Shared components have one owner and are consumed rather than restated.
- Required/OnUpdate behaviour remains unambiguous and cheap to check.
- Version/package/deployment facts are not conflated.
- Deployment can act mechanically from Package + Manifest.
- Platform choices are established by evidence rather than assumptions.
- Messaging adds receipt integrity without requiring a permanent message/obligations archive.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Decisions_v16
References: Capabilities_Design_v10, Capabilities_Migration_Design_v2, Capabilities_Standards_Design_v5, Capabilities_Tools_Design_v3, Capabilities_Messaging_Design_v2
<!-- END SOURCE: Capabilities_Brief_v9.md -->

---

<!-- BEGIN SOURCE: Capabilities_Overview_v15.md -->
# Capabilities — Overview

> **Version 15** (2026-09-01). Applies Review C R1 semantic remediation and records the current production/reference/freshness/correlation model before focused R2 verification.

---

## Architecture at a glance

```text
Capabilities
├── Standards
├── Tools
├── Tags
├── Scope
├── Dependencies
├── Migration
├── Review
└── Messaging
```

- Standards → Standard kind, weights, canonical production/usage.
- Tools → invokable action contracts/logical actions.
- Tags → generated/manual classifications + Boolean query.
- Scope → applicability.
- Dependencies → identity/presence/order/conformance/version facts.
- Migration → declared transition checking/execution.
- Review → independent assessment lifecycle.
- Messaging → AI-MESSAGE envelope, correlation, receipt integrity and cross-context messaging.

## End-to-end flow

```text
DESIGN
Capability Design → Build Capability Tool → canonical capability → Build Config → WorkPackage

BUILD
canonical capability + platform Build knowledge
  → Platform Contributions
  → Capability Package + logical deployment intent
  → AI Deployment
  → Deployment Set/Target reconciliation + verification
```

## Dependencies + Migration

```text
Dependencies: abc@v8
Available: abc@v12
       ↓
Dependency Query: v8 → v12
       ↓
MigrationSummary fast check
       ↓ if needed
per-version transition history
       ↓
Required before affected use
OnUpdate on next modification/save
None = no state change
```

- `!!` is startup presence checking, not a blanket startup migration scan.
- conformance checkpoints are non-ordering saved facts; dependency declaration order is default processing precedence only where processing order is needed;
- transition posture is version-level;
- Required-triggered save also reconciles pending applicable OnUpdate work through current;
- checkpoint is written only with saved proven artefact state;
- failure/defer preserves last successful checkpoint and writes compact owner-labelled temporary
  state;
- an unsatisfied exact-version constraint is a hard present block, not a conformance checkpoint or ordinary migration gap.

## Migration performance

```yaml
MigrationSummary:
  CurrentVersion: v20
  LatestRequiredVersion: v18
  LatestOnUpdateVersion: v19
  SupportedBaseline: v8
```

Detailed history loads only when the summary indicates possible work. Skill-based platform builds
should surface this summary in eagerly available skill/header metadata where possible.

## Version concepts

```text
DocMeth document version
≠ capability release version
≠ consumer conformance checkpoint
≠ package build identity
≠ deployment state
```

Package rebuilds use a new PackageId/digest as needed without falsely incrementing capability
release version. Consumer conformance checkpoints routinely lag current releases until a qualifying
save proves newer conformance; that is expected state rather than stale metadata.

## Package + Manifest

```text
Capability Package
  = payload/build instance for one capability release

Deployment Manifest
  = logical placement/lifecycle intent
```

Manifest minimally carries PackageId, capability identity/release, logical Deployment Set/platform,
contribution selection, explicit replace/remove intent where needed, and integrity. Physical
repository/plugin/path/account destination is Deployment Config.

## Standards and Tools

Standards and Tools now consume Tags/Scope/Dependencies/Migration/Review rather than embedding
those mechanisms. Generic platform realisation belongs Build side.

Tools may orchestrate bounded declared judgment; the repeatable Tool contract stays explicit and
genuine substantive authority remains external.

Published generic/canonical outcomes now include:

- `AIDE_StandardsProduction@v2`;
- `AIDE_StandardsUsage@v1`;
- `AIDE_ToolsProduction@v1`;
- `AIDE_ReviewTool@v3`;
- `AIDE_MigrationTool@v2`; and
- `AIDE_BuildCapabilityTool@v2`;
- `AIDE_Messaging@v2`; and
- `AIDE_MessagingTool@v1`.

`Build Capability` is the named design-side action that converts confirmed Design into canonical
Standard/Tool outcomes. It does not perform platform Build or Deployment.

## Messaging

```text
ordinary exchange                 → conversation
active state needing continuity   → WIP
durable outstanding obligation    → OpenItems
body needing independent retrieval → persisted Message
```

`AIDE_Messaging@v2` keeps message identity/threading/readability separate, retains best-effort
`=== STATE ===` receipt integrity, distinguishes receipt from fulfilment, and does not require the
former dedicated obligations register. STATE's value depends on retained evidence; use explicit Ack
where positive receipt proof matters. `AIDE_MessagingTool@v1` supplies Compose, Receive, Reply,
Forward, Promote, Acknowledge, QueryReceipt and Reconcile.

Review consumes Messaging for AI-MESSAGE relay/receipt semantics; Review v3 treats Review/Round payload correlation as authoritative for Review semantics and quarantines a positive mismatch with transport correlation. Profiles v2 keeps the same five Types with versionless Review references.

## AI Deployment handoff

Capabilities stops at capability-local package/build material plus logical deployment intent.

AI Deployment now owns:

- Deployment Set desired composition;
- target surface + representation + distribution channel;
- set-aware composition;
- install/update/remove reconciliation;
- partial failure/resumption; and
- runtime verification.

The previous hypothesis that one local OpenAI plugin/skill install could be the common private
ChatGPT + Codex route is closed as false for the tested path. Broader hosted/account/public routes
remain implementation evidence.

## Current sequence

1. Peer-review the major AIDE/Capabilities architecture slices with Claude, including Messaging.
2. Resolve accepted Review findings into current Design/Decisions/canonical outcomes.
3. Build lightweight platform-specific Bootstrap implementations where evidence warrants them.
4. Build target-platform contributions and hand deployment to AIDE Build + AI Deployment.
5. Run the planned final cross-system integration Review before broad deployment.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Brief_v9, Capabilities_Design_v10, Capabilities_Decisions_v16
References: Capabilities_Migration_Design_v2, Capabilities_Dependencies_Design_v3, Capabilities_WorkRegister, Capabilities_OpenItems, Capabilities_Messaging_Design_v2
<!-- END SOURCE: Capabilities_Overview_v15.md -->

---

<!-- BEGIN SOURCE: Capabilities_Design_v10.md -->
# Capabilities — Design

> **Version 10** (2026-09-01). Applies Review C R1 semantic remediation: reference-position rules, published Tool production, tag freshness, non-ordering checkpoints/exact pins, Review/Messaging correlation and STATE limitations.

---

## §1 — Scope

This is the parent architecture for reusable AI-facing capability infrastructure within AIDE. Child
components may add internal structure but may not silently take ownership assigned elsewhere here.

## §2 — Architecture

```text
Capabilities
├── Standards
├── Tools
├── Tags
├── Scope
├── Dependencies
├── Migration
├── Review
└── Messaging
```

AIDE Build owns WorkPackage and generic execution/handoff. Environment/platform architecture owns
runtime facts/settings. Documentation Methodology owns generic document structure/rendering.

### Principles

- one owner per mechanism;
- capability meaning before platform realisation;
- self-contained Design→Build handoff;
- generic platform implementation belongs Build side;
- Build is capability-local; generic set-aware Deployment is an external consumer;
- semantic complexity resolved before cheap runtime matching;
- declared transitions before inferred deltas; and
- platform evidence before platform assumptions become architecture.

## §3 — Capability production

```text
Capability Design
      ↓
Build Capability Tool
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage
```

The canonical outcome contains complete generic capability meaning, capability-specific platform
addenda, dependency/scope metadata, and release transition declarations where applicable.

`AIDE_BuildCapabilityTool` owns this repeatable production step. It applies the applicable
canonical production contracts, produces declared Standard/Tool siblings, and returns a precise
Design/production defect rather than making a new substantive design decision.

Build side should not need to reopen internal Capability Design to determine the required result.

## §4 — Build Config

Effective Build Config declares:

- target platforms/default supported set;
- side: Design, Build, or both (default both);
- one or more logical Deployment Sets.

It does not contain repositories, plugin layouts, paths, bundle filenames, or other generic
platform mechanics. Storage/inheritance details remain a later non-blocking configuration question.

## §5 — Build-side platform realisation

```text
canonical capability
 + Build Config
 + WorkPackage
 + platform Build Standards/Tools/references
        ↓
Platform Contribution(s)
```

A Platform Contribution is capability-local material for one platform/family. It may later be
composed with other packages by Deployment.

Current physical representations are evidence questions. A platform may use skills/plugins,
configuration, commands, repositories, bundles, or other mechanisms. Capability designs specify
only capability-specific deltas.

## §6 — Standards

Standards defines the Standard kind, weights, canonical Standard production, and generic usage
behaviour. Its published generic outcomes are `AIDE_StandardsProduction@v2` and
`AIDE_StandardsUsage@v1`.

Weights remain Requirement, Expectation, Guidance, Context. Standard content is facilitative and
consequence/value framed even where binding.

Standards consumes Tags, Scope, Dependencies, Migration and Review rather than restating them.
Detailed contract: `Capabilities_Standards_Design` v5.

## §7 — Tools

Tools defines repeatable invokable action contracts and logical actions. A Tool may orchestrate
bounded declared judgment through explicit inputs/decision/escalation rules but does not acquire
substantive authority it does not own.

Tools publishes `AIDE_ToolsProduction@v1` as the generic canonical Tool-production contract.
Build Capability consumes that published contract rather than copying the Tool structure or
requiring a downstream producer to reopen internal Tools Design.

Tools consumes Scope, Dependencies and Migration; Tools are not categorically excluded from release
transition handling. Platform invocation/rendering belongs Build side.

Detailed contract: `Capabilities_Tools_Design` v3.

## §8 — Tags

Tags owns Tag Builder declarations/discovery, generated ownership, compact storage, flattening,
exact Boolean query semantics and generic freshness. Semantic owners resolve inheritance/relationships
before generation. After source information that can change generated tags changes, builders run
before publishing/saving governed tag state; if freshness is uncertain, rebuild before tag-dependent
behaviour relies on it.

Detailed contract: `Capabilities_Tags_Design` v2 / `AIDE_Tags@v2`.

## §9 — Scope

Scope owns applicability only:

- Machine Scope = `AIDE_Tags` Boolean query;
- Context Scope = AI-interpreted natural-language condition;
- missing layer = unrestricted;
- disabled = never applicable.

Machine Scope relies on current tag state. Where generated-tag freshness is uncertain, refresh it
under `AIDE_Tags` before treating Machine Scope as deterministic input. Platform trigger/discovery
implementation belongs Build side.

Detailed contract: `Capabilities_Scope_Design` v2 / `AIDE_Scope@v2`.

## §10 — Dependencies

Dependencies owns dependency declaration, presence posture, identity/version factual state,
conformance checkpoints, Dependency Builders, and default dependency processing precedence.

```text
Dependencies: abc, !def@v4, !!ghi@!v7
```

- `!` required on relevant use/access;
- `!!` best-effort startup presence check plus required thereafter;
- `@vN` last saved/proven conformance checkpoint;
- `@!vN` hard exact available-version constraint.

A conformance checkpoint is backward-looking saved evidence and creates no resolution/execution
order; mutual checkpoints are not an operational dependency cycle. Declaration order supplies
default processing precedence only where the governing operation needs it for dependencies of the
artefact being processed; it does not sequence independent artefacts or peer Bootstrap Contributions.

Reference position matters: `References:` carries no currency/conformance obligation, while a
current executable in-body capability reference is operational guidance. Executable references are
normally versionless; a specific release is named only where deliberately required by that
instruction's contract.

An unsatisfied `@!vN` blocks affected use; it is not a conformance checkpoint or ordinary Migration
gap and another version may not silently substitute.

Detailed contract: `Capabilities_Dependencies_Design` v3 / `AIDE_Dependencies@v3`.

## §11 — Migration

Migration owns transition semantics and execution across dependency version gaps.

Every migratable capability release declares one version-level posture:

```text
Required | OnUpdate | None
```

Required is checked before affected use. OnUpdate waits until the next modification/save. If
Required causes an update, pending applicable OnUpdate work is reconciled in that same save and the
artefact normally advances through current as far as execution succeeds.

A compact `MigrationSummary` exposes current/latest Required/latest OnUpdate and optional supported
baseline for cheap discovery. Detailed history is loaded only when required. Skill-based builds
should surface the summary in eagerly available header/metadata where supported.

Checkpoints advance only with saved proven artefact state. Migration is stepwise durable; failure or
authorised deferral records compact owner-labelled temporary state through the generic document
state mechanism.

Exact-version constraints are checked as present dependency constraints rather than Migration gaps.
Migration reports/halts affected migration or use when the exact constraint is unsatisfied; changing
the pin is an explicit dependent-artefact change, not an inferred migration decision. Mutual
conformance checkpoints create no cross-artefact migration ordering.

Detailed contract: `Capabilities_Migration_Design` v2 / `AIDE_Migration@v2`,
`Capabilities_Migration_Tool_Design` v2, and canonical `AIDE_MigrationTool@v2`.

## §12 — Shared identity/version model

Formal identity remains the Core convention:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

Keep these meanings distinct:

1. **Document version** — DocMeth output version of source/design documentation.
2. **Capability release version** — formal published/referenceable capability contract version.
3. **Dependency conformance version** — consumer's last saved/proven checkpoint.
4. **Package identity** — concrete build instance of one release, distinguished by PackageId and
   integrity rather than another semantic release version.
5. **Deployment state** — factual record of what package/release is deployed to a target.

A changed capability release increments when released for distribution. Rebuilding unchanged
packaging does not change capability release version.

Consumer dependency checkpoints will routinely remain behind the current capability release until a
qualifying save proves newer conformance. That lag is expected steady state, not decay or an
automatic update trigger.

## §13 — Bootstrap

Core owns `{bootstrap}` and the best-effort session-start discovery instruction. Dependencies uses
it for `!!` startup presence checking. Other components may contribute bootstrap content only where
a real early-check requirement exists; Migration has no blanket startup scan.

## §14 — Capability Package

A Capability Package is the capability-local payload generated by Build for one capability release.
It carries:

- `PackageId` — identifies that build instance;
- formal capability identity/release version;
- package-local Platform Contribution identifiers/payload; and
- integrity information/digest sufficient to validate/distinguish the payload.

Rebuilding the same release may change PackageId/digest without changing capability release version.
The logical contract is not tied to ZIP or another container format.

## §15 — Deployment Manifest producer contract

The Deployment Manifest is logical placement/lifecycle intent accompanying one package:

```yaml
ManifestSchema: <contract identity/version>
PackageId: <package build identity>
Capability: <identity@release-version>
Targets:
  - DeploymentSet: <logical name>
    Platform: <logical platform/family>
    Contributions: [<package-local ids>]
    Replace: [<optional deployed member identities>]
    Remove: [<optional deployed member identities>]
Integrity: <digest/equivalent>
```

Physical destination/configuration is not a manifest field. Deployment Config resolves logical
set/platform to repository, plugin, collection, bundle, path, account/workspace destination, etc.

The schema may be extended during Deployment only where a demonstrated mechanical requirement
exists. Transition semantics remain in capability/payload unless Deployment proves it needs a
manifest-level fact.

## §16 — AI Deployment handoff

Generic Deployment has been promoted out of Capabilities.

Capabilities retains the producer boundary:

```text
canonical capability
  ↓ Build
Platform Contribution(s)
  ↓
Capability Package + logical deployment intent
  ↓
AI Deployment
```

The producer contract must remain sufficient for mechanical deployment without reopening
Capability Design. `AIDE_Deployment@v1` owns Deployment Sets/Targets, representation/channel/
surface resolution, set-aware composition, physical reconciliation, partial failure/resumption
and runtime verification.

OpenAI evidence establishes that representation, distribution channel and runtime surface are
separate target facts. A locally installed plugin/skill route that works for Codex cannot be
assumed to expose executable ChatGPT Chat runtime content.

## §17 — Review

Review owns the purposeful independent-assessment lifecycle, Type/Level/Mode/Reviewer dimensions,
request/round/finding/disposition/result semantics and scope control. Environment supplies current
model/reviewer/route facts. Messaging owns AI-MESSAGE relay, receipt/reconciliation and messaging
actions used for indirect/manual Review transport; direct-route mechanics remain platform Build/
environment implementation.

For Review exchanges carried through Messaging, Review/Round identity in the Review payload is
authoritative for Review lifecycle semantics while Messaging correlation is transport-level.
Positive disagreement between those layers is quarantined rather than guessed through.

Detailed contract: `Capabilities_Review_Design` v3, `AIDE_Review@v3`,
`AIDE_ReviewProfiles@v2`, `Capabilities_Review_Tool_Design` v3, and canonical
`AIDE_ReviewTool@v3`.

## §18 — Messaging

Messaging owns platform-neutral structured communication between AI contexts that may share only
relayed text. Its canonical envelope separates Thread, Message-ID, Version, reply correlation and
human-readable Topic/Timestamp, carries `Expects`, and uses best-effort `=== STATE ===` evidence to
raise the probability that missed relay/receipt is noticed.

Messaging distinguishes receipt from fulfilment: a holding reply can prove receipt while the
original substantive expectation remains open. State inference is asymmetric—positive unexpected
identifiers are mismatch signals; absence proves nothing. STATE's evidential strength depends on
retained evidence; a genuinely stateless context may provide no receipt evidence, so explicit Ack is
used where positive receipt proof materially matters.

Messaging does not require a permanent obligations register. Use conversation for normal exchange,
WIP for active continuation state, OpenItems for obligations that must outlive current work/context,
and a persisted Message only when its actual body needs independent retrieval. Documentation
Methodology supplies generic governed-document mechanics for a persisted Message.

The canonical outcomes are `AIDE_Messaging@v2` and `AIDE_MessagingTool@v1`. Platform skills,
commands, pasted-envelope triggers, direct-route integrations, clock/file APIs and UI behaviour are
Build concerns. No Messaging Bootstrap Contribution exists by default; add one only if target
evidence demonstrates a genuine early-discovery need.

Detailed contract: `Capabilities_Messaging_Design` v2,
`Capabilities_Messaging_Tool_Design` v1, `AIDE_Messaging@v2`, and `AIDE_MessagingTool@v1`.

## §19 — Principal flow

```text
DESIGN SIDE
Capability Design → Build Capability Tool → canonical capability → Build Config → WorkPackage

BUILD SIDE
WorkPackage + canonical capability + platform Build knowledge
  → Platform Contributions
  → Capability Package + Deployment Manifest
  → AI Deployment
  → Deployment Set/Target reconciliation + verification
  → WorkPackage Outcome
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Brief_v9, Capabilities_Decisions_v16
References: Capabilities_Standards_Design_v5, Capabilities_Tools_Design_v3, Capabilities_Dependencies_Design_v3, Capabilities_Migration_Design_v2, Capabilities_Review_Design_v3, Capabilities_Messaging_Design_v2, Capabilities_BuildCapability_Tool_Design_v2, Core_System_Design
<!-- END SOURCE: Capabilities_Design_v10.md -->

---

<!-- BEGIN SOURCE: Capabilities_Decisions_v16.md -->
# Capabilities — Decisions

> **Version 16** (2026-09-01). Records Review C R1 dispositions for capability-reference semantics, Tool production ownership, tag freshness, Review/Messaging correlation, STATE limits, and expected checkpoint lag.

---

## D1 — Baseline reset

**Decision.** Set the entire Workflow corpus aside. Re-admit elements only by explicit confirmed
decision. The confirmed baseline is: `Workflow_Capabilities_Design` v1,
`Workflow-D106`–`Workflow-D113` (the capability model decisions), `Workflow_Principles` v1,
`Workflow_DesignMethodology` v1. Everything else is available as reference but has no standing
until positively re-admitted.

**Reason.** The design had been going off track and over-complicated. Significant work in flight
was not consistent with the intended design direction. Same blank-sheet move as the original
capability model session, applied to the whole corpus.

---

## D2 — Adapter renamed to publisher

**Status: superseded as the parent production model by `D49`.** The historical mechanical and
loud-failure constraints remain useful to component builders and deployers, but “Publisher” is
no longer the organising concept for Capabilities.

**Decision.** The adapter concept from `Workflow-D108` (one per capability kind per platform,
mechanical, no judgement) is renamed to publisher. The tools are Publish Standard and Publish
Tool.

**Reason.** "Adapter" was provisional ("good name as any for the moment") and abstract.
"Publisher" says what the thing does and reads naturally in use: "use the Publish Standard tool
to publish your standard."

**Constraints carried forward.** All `Workflow-D108` constraints apply: mechanical, decides
artefact count and shape but never anything requiring judgement, verbatim extraction of section
openers, loud failure on gaps.

---

## D3 — Doc types are single-source DocMeth

**Status: superseded by `D53`.** Domains may define local document types; DocMeth owns shared
types and shared components.

**Decision.** Document types are defined and managed by DocMeth, which produces a standard
covering them. Other capability projects scope against those types but do not define new ones
independently.

**Reason.** Multiple independent definers create collision risk and precedence disputes. A new
type is an event worth a conversation (via cross-project messaging) rather than something
happening silently.

---

## D4 — Production chain is a broader convention

**Decision.** The production chain (Brief / Requirements / Considerations / Guiding Principles →
Decisions → Design → Outcome) is a standard convention broader than `Workflow-D109` (the
four-layer chain). Different items implement whichever sections apply. `Workflow-D109` is one
instance.

**Detail.** Parts are often rolled into one file for ease of management. Design is normally kept
separate from Brief/Requirements to allow blind review segmentation. Subtopics may not need a
Brief if covered by a parent.

---

## D5 — Overview document type

**Decision.** Overview is a new document type — an orientation document showing where things sit
and how they relate.

**Content rules.** Triggers not definitions. Roughly a line per point, bulleted, organised and
grouped into headings. Flowchart and org-style representation common. Carries core structure,
behaviours and rules for its scope. If a line needs a second line to make sense, it's the wrong
line.

**Scope.** Attaches to a topic or part of the tree, not one-to-one with a domain. Delegates like
an Index. Optional per case.

**Currency.** Rebuild prompted by either side as needed. Staleness acceptable but must be checked
before use as a source of trust. Last-modified date supports this.

**Working surface.** Used as a focal point for design and discussion. Decisions can originate
here but get pushed to their proper home in the same pass. Source wins on disagreement.

**Ownership.** Type defined by DocMeth. Individual instances authored by their owning domain.
Registered in the Index like any other document.

---

## D6 — Document metadata standard

**Decision.** All governed documents carry created and last-modified dates, updated in the same
pass as a version bump. This is a DocMeth convention applying to all document types.

**Reason.** Version numbers tell sequence but not when. Last-modified answers "can I trust this
right now." Essential for Overview currency checks but valuable across all document types.

---

## D7 — Capabilities topic produces standards and tools

**Status: superseded by `D43` and `D51`.** Standards and Tools remain capability-producing
components, but they now sit beside five shared components and Standards' two confirmed generic
outputs are stated explicitly.

**Decision.** The Capabilities domain produces:
- **Standards** — for standards and tools creation, build and publishing. Includes platform
  standards for per-platform tailoring. Other domains consume these.
- **Tools** — Publish Standard and Publish Tool. Other domains invoke these to deploy their
  standards and tools.

---

## D8 — Principles is a separate top-level topic

**Decision.** Principles is a cross-cutting concern applying to every project and scenario. It
is established as its own top-level topic, not a subtopic of Workflow or Capabilities. It will
produce a standard as an outcome.

**Reason.** Principles was parked in Workflow because that's where the conversation happened, not
because that's where it belongs. Its scope is universal.

---

## D9 — Role and purpose of a standard

**Decision.** A standard exists to add value and facilitate, not to enforce. Enforcement may be
one of its roles but is never its primary lens. The role statement: "A standard provides guides,
rules, advice and support, focused on adding value and facilitating effective work. Enforcement
may be one of its roles but is never its primary lens; it operates through facilitation, clarity
and support."

**Reason.** Framing matters: the same requirement expressed as facilitation lands better than
expressed as authority. When enforcement becomes the primary lens, standards drift draconian and
controlling. Same outcome, two different approaches — the facilitating one works better.

A standard carries rules, but rules work by benefit — follow them to get the benefit; don't
follow them and you don't get it. Mandates are framed consequentially ("if it isn't in this
format, it can't be consumed by X") rather than authoritatively ("you must").

The framing distinction is critical: it is not that standards are mostly guidance and
occasionally enforce. A standard may legitimately be almost entirely mandatory — volume of
enforcement is not the point. The point is the framing, because framing changes the outcome.

Standards are the broader artefact; tools cover specific actions. A standard may reference
actions; its scope is wider — standard operating practice, guides, and anything a session or
user should consider relative to the work in hand.

---

## D10 — Weight system

**Decision.** Four obligation tiers collectively called "weight" (as in "what weight does this
carry"): Requirement, Expectation, Guidance, Context. Each addressable unit likely to be chunked
carries a weight marker.

- **Requirement** — must be met, not open to judgment. Framed consequentially.
- **Expectation** — the default position. Departure permitted but must be declared visibly.
- **Guidance** — a default or best practice. Departure permitted; you own the consequences.
- **Context** — information, perspective, reasoning. No obligation.

**Key delineation.** Expectation is about visibility — declare your deviation. Guidance is about
ownership — handle what you've taken on. Both permit departure but ask different things when you
do.

---

## D11 — Weight cascade

**Decision.** Weights cascade downward through a document with nearest-declaration-wins:

- **Document level** — an optional default for the whole document. Applies to any chunk that
  does not carry its own weight.
- **Section level** — mandatory. Every section declares a weight. This is the level most readers
  encounter.
- **Statement level** — override only. A single statement or block within a section that carries
  a different weight from its section.

**Unmarked chunk is a defect.** If a chunk has no weight from any level, the standard has a gap.
The cascade makes this rare (document default covers most things) but does not eliminate it.

**Addressable unit test.** The trigger for needing a weight is chunkability — "could this chunk
be retrieved, referenced, or read in isolation?" If yes, it needs to know its own weight,
either inherited or explicit.

---

## D12 — Specification dropped as output type

**Decision.** The Specification document type is dropped. The Standard is terse, complete, and
carries weights. The Specification was sitting between the Standard and the Design with no clear
reason for existing.

**What it leaves behind.** The Standard now holds the ground the Specification was meant to
cover: precise, machine-referenced, weight-carrying. It doesn't need two formats to be both
terse and consultable.

---

## D13 — Guide as opt-in companion

**Decision.** The Guide is optional, declared in the standard's Brief when wanted. It is a
discursive, explanatory companion to the Standard — a "why and how" rather than a "what."

**Key constraint.** Both are generated from the same Design. If they disagree about substance,
the Design is the authority. The Guide never introduces new rules not in the Standard; the
Standard never references the Guide as a source of obligation.

---

## D14 — Standard blocks (superseded)

**Status: superseded by `D26`.**

---

## D15 — Conflict handling

**Decision.** Conflicts are detected and escalated at two points:

- **Build check** — internal coherence of the assembled artefact (the standard itself). Multiple
  standards arriving in the same package are checked against each other before they ship.
  Contradiction = escalate, never resolve quietly.
- **Publish check** — external coherence against the already-deployed set. The new standard is
  checked against what exists. Contradiction = escalate.

**Runtime conflict hierarchy** (when two standards apply to the same scope at the same time):
1. Append — compatible standards stack.
2. Same weight, contradiction — escalate loudly. Do not pick one silently.
3. Higher weight wins — if one is Requirement and the other Guidance on the same point, the
   Requirement takes it and the conflict is noted.
4. Human instruction beats Requirement — but the standard's position is stated and the deviation
   is recorded.

---

## D16 — Standards Standard / AIDE standard split (revised)

**Status: revised by `D27`, then superseded by `D51`.** The production/use split remains; the
runtime outcome is now the generic Standards Usage Standard owned by Standards, not an
AIDE-scoped standard.

**Decision.** The Standards Standard (governs production: authoring, structure, weights,
publishing) and the AIDE standard (governs runtime: conflict handling, deviation, weight
honouring) are separate artefacts.

**Reason.** Different audiences, different lifecycles. A change to how standards are authored
should not require every consumer to re-absorb the runtime rules.

---

## D17 — Distinct audiences

**Status: revised by `D51`.** The audience-separation principle remains. The runtime audience is
served by the generic Standards Usage Standard rather than an AIDE-scoped artefact.

**Decision.** The Standards Standard addresses the standard author. The AIDE-scoped runtime
standard addresses the AI session. The Guide addresses the human reader. Each artefact is
written for the audience that will use it.

**Reason.** A single artefact written for multiple audiences fails at serving any of them well.
An AI session needs terse, machine-referenced structure; a human reader needs discursive
explanation; an author needs a production checklist.

---

## D18 — Two-layer scope model

**Status: revised by `D60`–`D64`.** The two-layer applicability idea remains, but tag
generation/querying is extracted to Tags, platform trigger realisation belongs Build side, and
the no-declaration default is reversed.

**Decision.** Scope is evaluated in two layers, shared by standards and tools:

1. **Mechanical scope** — locally-owned tags, set logic (any-of, all-of, none-of). Hard filter,
   no reasoning. Evaluated first because it is free.
2. **Context scope** — assessable prose conditions. The session reads and judges. Evaluated
   second, only for candidates that pass the mechanical filter.

**No declaration = applies nowhere.** A standard or tool without a scope declaration has no
scope; it does not silently apply everywhere.

---

## D19 — Mechanical scope: tag ownership and breaking changes

**Status: superseded by `D60`–`D62`.** Tag ownership is now defined through Tag Builders,
including generated ownership by prefix or group; Tags is a first-class component rather than a
locally-owned Scope convention.

**Decision.** Tags in mechanical scope are locally owned by each consuming domain. The set logic
operates on those tags. Tag renames are breaking changes — they invalidate every scope
declaration that references the old name.

**Reason.** Tags are identifiers, and identifiers must be stable. A rename that propagates
silently creates scope that was never declared, or removes scope that was. The cost of a rename
must be visible so the decision can be made honestly.

---

## D20 — Tool role and purpose

**Status: retained and extended by `D52`.** Tool definitions now also include the logical
commands they contribute.

**Decision.** A tool exists where judgment adds nothing — where the same action, given the same
inputs, should produce the same result regardless of who runs it. A tool removes the need to
decide; a standard shapes what a session decides.

**Value proposition.** Four things: determinism (same inputs, same result), encapsulation (the
caller doesn't need to understand the mechanism), cost (cheaper than re-deriving the approach
each time), completeness (nothing is forgotten because the tool carries the full checklist).

---

## D21 — Reporting obligation for tools

**Decision.** A tool must be able to report what it did and why — not just that it succeeded.
Otherwise it buys determinism at the cost of understanding, which is a bad trade given the
empowerment premise (`Workflow-D106`).

**Verbosity levels.** Four levels, account-level user preference (not repo, not plugin — both
are shared): minimal, summary, detailed, verbose. Default is summary.

Summary is defined tightly: what was done, what changed, what needs attention. Not reasoning,
not intermediate steps, not a recap. If it runs past a few lines it isn't a summary.

**Verbosity governs narration, not the record.** The full account is written wherever work is
recorded, regardless of the verbosity setting. This makes "minimal" safe — the record is
complete even when the narration is suppressed.

**Overrides.** Session instruction overrides the account default in the moment (Guidance weight,
not absolute). Failures and deviations surface regardless of verbosity setting.

**Reason.** Summary as default because asking for more is natural; asking for less repeatedly is
grating. The narration/record split means the preference never costs information — it only
controls what gets said aloud.

---

## D22 — Ask, infer, or escalate

**Decision.** Three postures a tool takes when it needs information:

- **Infer confidently and say so** — where a strong assumption is available and the cost of
  being wrong is low.
- **Ask** — for a missing input the tool knows it needs. Ask once, well, gathering everything
  in one exchange. Serial interrogation is the other way tools become tedious.
- **Escalate** — a genuine judgment call. Two things conflict, or the right course depends on a
  view nobody has taken. Never resolve it.

**Standing rule.** Never fail for want of information you could have asked for. Failing because
the caller didn't phrase it perfectly is the punitive posture the model rejects.

**Batched by default.** When asking, present everything needed in one exchange. If the user
prefers to step through one by one, that is an interaction preference the session honours —
but the full list is still surfaced first so the user sees the shape of what's needed.

**Reason.** The three postures match how a competent colleague works: obvious things are assumed
and stated, missing things are asked for, and judgment calls are handed up. The batching default
exists because the alternative — serial questions — makes every invocation an interrogation.

---

## D23 — Weights do not apply to tools (parked)

**Status: parked, not rejected.** No current case for weight markers in tool documents. Revisit
only if real examples surface showing tool content where the reader genuinely needs to know its
obligation level.

**Original proposal.** Apply the weight system (`D10`) to tool documents with a different
distribution — more Requirement, less Guidance. Rejected on the grounds that the concept was
being bent to fit an item where the case for its place had not been made.

---

## D24 — Standard-tool boundary

**Decision.** A standard may describe a procedure. It may not define an invokable action. If
you would say "run X," X is a tool. If you would say "follow the approach in section Y," that
is a standard.

**Sibling outputs from one design.** A single design describes a body of behaviour. Its outputs
are whatever implements that behaviour — one or more standards, one or more tools, siblings from
a common source. Neither sibling is authoring the other's content; both derive from the same
design and therefore cannot disagree.

**Platform variance in the output set.** Whether a platform needs two tools where another needs
one, or no tool because the platform provides it natively, is a platform design concern. The
base design declares the behaviour and its outputs; the platform design declares any variance.

**Staging.** A standard may legitimately describe a procedure that should be a tool but isn't
yet. That is a staging post, not a defect. When the tool is built, the standard's procedure
section is replaced by a pointer — the tool becomes the single source.

**Resolves `Q4` (actions boundary, renumbered from v2's `Q3`).**

**Reason.** The test is invocability. A named invokable thing must be a tool because only a tool
carries the identity, versioning, and publishing machinery that keeps a named thing honest. A
standard restating an action creates two authorities on the same thing with no synchronisation.

---

## D25 — Tool document structure

**Status: retained and extended by `D52`.** Commands become an explicit part of the Tool design.

**Decision.** A tool document is a machine-facing artefact designed to provide an effective
implementation of an action on an AI platform. It contains:

- **Identity and invocation** — the name it's called by, and any aliases.
- **Trigger** — what causes it to fire: explicit invocation, and any conditions where a session
  should reach for it unprompted. Scope attaches here.
- **Purpose** — one line, dense with matching terms. A retrieval and selection surface.
- **Inputs** — what it needs, which are required, which are inferable and from where, defaults.
  Each input carries an input resolution declaration and a confirmation posture (see `D22`).
- **Preconditions** — what must be true before it runs. Checked and reported, not assumed.
- **Procedure** — the steps, ordered, unambiguous.
- **Decision points** — where the procedure branches, and what determines which branch.
  Separated from the procedure steps, not buried in them. A step that hides a decision is
  where tools go wrong.
- **Escalation conditions** — what causes it to stop and hand back rather than proceed.
- **Outputs and effects** — what it produces, what it changes, what persists.
- **Reporting** — what it says at each verbosity level, and what it always says regardless.
- **Failure handling** — what happens on partial completion, and whether it's safe to re-run.
- **Idempotency** — whether re-running is safe. Declared, not inferred.

**Reason.** Structured in the order a session needs the information: identity first (is this the
right tool?), then inputs (what does it need?), then procedure (what does it do?), then
consequences (what happened?). Decision points are separated because a tool's honesty depends on
its judgment calls being visible — same lesson as normative versus advisory content being
typographically identical in a standard.

---

## D26 — Standard blocks removed

**Supersedes `D14` (standard blocks).**

**Decision.** The standard block inclusion mechanism is removed. A design that needs to
contribute content to another domain's standard publishes a separate standard with its own
scope declaration instead. Deployment can still arrive together (same plugin, same package);
ownership boundaries stay clean and no embedding mechanism is needed.

**Reason.** Standard blocks existed to let the Capabilities Standards subtopic contribute
runtime rules into the AIDE standard. The AIDE architecture review identified the risk of AIDE
becoming a monolith through cumulative absorption of other domains' content. A separately
published standard, scoped to AIDE contexts, achieves the same deployment result without the
AIDE standard growing to accommodate content it does not own. The inclusion mechanism was
solving a problem created by assuming AIDE had to absorb the content.

---

## D27 — AIDE standard delivery revised

**Status: superseded by `D51`.** The separately published runtime outcome remains separate from
production rules, but it is the generic Standards Usage Standard and is not AIDE-scoped.

**Revises `D16` (Standards Standard / AIDE standard split).**

**Decision.** The split between the Standards Standard (production) and the AIDE standard
(runtime) stands. The delivery mechanism changes: the Capabilities Standards subtopic publishes
a separate standard containing the runtime conflict hierarchy, deviation handling, and
weight-honouring rules, scoped to AIDE contexts. It does not contribute via a standard block.

**Reason.** Follows from `D26` (standard blocks removed). The content and the split are
unchanged; only the vehicle changes. A separately published standard is cumulative — it adds to
the AIDE environment without the AIDE standard absorbing it.

---

## D28 — Migration is a capability-level service

**Status: retained and revised by `D43` and `D47`.** Migration is now an explicit top-level
component and covers both Required Migration and On-Update transition postures.

**Decision.** Migration — the mechanism by which changes to a standard are propagated to
artefacts built under it — is a service owned by Capabilities, not by the Standards subtopic.
Standards are the first consumer but not the owner. Any capability kind (standards, tools,
document structures) may use the migration mechanism.

**Reason.** Migration applies wherever a versioned artefact governs downstream work. Placing
it in Standards would force other consumers to depend on a peer subtopic rather than on the
shared infrastructure. Same reasoning as versioning being a comparison primitive rather than a
standards-specific concept.

---

## D29 — Required versus lazy change classification

**Status: superseded by `D47`.** “Lazy” is replaced by On-Update / `OnUpdate`, and the current
classification explicitly includes the no-transition case.

**Decision.** A change to a standard is classified as one of two types:

- **Required** — a structural or functional change that must be applied for downstream artefacts
  to remain valid. Compromises integrity or ability to function if not applied. Example: a
  change in index structure, data definition, or a field that a consuming tool reads.
- **Lazy** — an improvement that does not compromise function. Applied when the artefact is
  next edited or refreshed. Example: a phrasing improvement, a better context structure, an
  efficiency gain.

**The classification belongs on the change, not on the release.** A single release may contain
both required and lazy changes. The release's obligation is derived from whatever it contains —
a release with any required change obliges action; a release with only lazy changes does not.

**Positive declaration.** A release states whether it obliges anything, rather than consumers
inferring it from an absent migration section.

**Reason.** Most rule changes do not invalidate existing work. A model that treats every version
as potentially migrating carries migration machinery for the small minority of changes that
actually require it. The required/lazy distinction makes the cost proportional to the
consequence.

---

## D30 — Two-level trigger architecture

**Status: superseded by `D48`.** Required Migration retains a blocking check path; On-Update is
triggered by AI-recognised modification activity and has `/update-doc` as its explicit recovery
path. Platform-specific trigger mechanics move to Scope and platform designs.

**Decision.** Migration checks operate at two levels, each with its own trigger:

1. **Domain level, at session start** — required changes only. A fast comparison of the domain's
   recorded state against what is currently installed. Cheap-to-expensive gate order: has the
   version moved → does the release declare any required change → does this domain declare that
   standard → only then does anything get actioned. Most sessions stop at the first or second
   gate.

2. **Document level, at edit time** — lazy changes, with required as a catchall. The document
   itself records what version of the standard it was built against. The gap between that and
   the current version is the pending set. Required changes are checked too as a safety net for
   any domain-level miss.

**A document's declared version updates when it is issued, not when the domain migrates.** The
domain record and the document record serve different purposes and cannot share one entry.

**Authority boundary.** In the authoritative domain, a version gap is work to do. In a consuming
domain holding a copy, the same gap is information only: report it, never act on it, never
rewrite someone else's artefact.

**Reason.** Two levels because two different things are being protected. Domain-level catches
breaking changes fast. Document-level catches everything else at the point where the artefact
is already open for editing — the cheapest possible moment to apply a lazy change.

---

## D31 — Two-skill migration mechanism

**Status: superseded by `D48`.** `/migrations-check` and `/migrations-apply` remain for Required
Migration; `/update-doc` is added as the distinct On-Update reconciliation tool.

**Decision.** The migration mechanism on the chat side is two skills:

1. **`/migrations-check`** — reports what is pending. Iterates available skills matching the
   `{key}_pendingmigrations` naming convention, reads their version from YAML frontmatter,
   compares against the `AppliedMigrations` section in the domain's context file
   (`AIDE_Domain.yaml`, `Migrations.yaml`, or equivalent). Reports required and lazy changes
   pending. Does not act.

2. **`/migrations-apply`** — executes pending migrations end to end. Reads the pending list,
   reads the `migrations.md` files stored with each standard skill, applies changes in version
   order, outputs updated files for download. Updates the `AppliedMigrations` record if the
   `{key}_pendingmigrations` skill version differs from what was stored.

**No third skill.** An earlier design proposed a separate `/migrations-migrate` skill for
per-document work. This was flattened to avoid a three-hop chain whose reliability degrades
multiplicatively on the chat side. `/migrations-apply` reads migration files directly.

**Execution surface is the user's choice.** `/migrations-check` prompts the user to run
`/migrations-apply` in chat, Cowork, or Code — whichever suits the scope of work. The skill
carries everything any surface needs; no separate handoff prompt is required.

**Reason.** Two skills with one explicit human decision between them. `/migrations-check` is
diagnostic; `/migrations-apply` is destructive. The user decides whether and where to act.

---

## D32 — Plugin currency detection via naming convention

**Status: removed from parent architecture by `D45` and `D50`; retained as historical platform
design input.** Any naming convention or plugin enumeration technique must be assessed in the
relevant Scope/Migration platform design rather than imposed generically.

**Decision.** Each plugin that pushes migrations includes a skill named
`{key}_pendingmigrations`. This skill's YAML frontmatter carries a version number. The
`/migrations-check` skill enumerates available skills by pattern-matching this naming
convention.

**Pending-migrations version only moves on required migration.** The `{key}_pendingmigrations`
skill version is bumped only when a required migration lands in the plugin. A release containing
only lazy changes does not touch it. This keeps the domain-level trigger honest: version moved
means there is genuinely required work waiting.

**Why this works.** On the chat side, the `<available_skills>` block is visible at session start
with skill names and descriptions. The naming convention makes migration-bearing plugins
findable by pattern. Reading the YAML frontmatter gives the version. No platform API for plugin
enumeration is required.

**What it does not solve.** Plugin-level version (e.g. "3.0.0" shown in the UI) is not exposed
to a running skill. The mechanism works at skill level, not plugin level. This is a known
platform limitation, not a design gap — the skill-level version is within the author's control
and is sufficient for the comparison.

**Reason.** The platform does not expose plugin metadata to running skills. This convention
solves the enumeration problem using what is available today. If the platform later exposes
plugin-level metadata, the mechanism can migrate to the cheaper check.

---

## D33 — Migration content is owner-authored

**Status: retained and revised by `D47`.** The owner still authors transition content, but
Required Migration and On-Update instructions are separate artefacts or package members.

**Decision.** The standard owner writes the migration file. The migration mechanism
(`/migrations-apply`) is a dumb executor that reads and follows instructions — it carries no
knowledge of what any specific standard does or how it changes.

**Migration files** are stored alongside the standard skill as `migrations.md`. They contain
per-version-transition instructions, applied sequentially from the artefact's current declared
version to the current standard version. The standard owner determines what is required versus
lazy, what the migration applies to, and what steps are needed.

**A migrations standard** (to be produced) governs how migration files are written — structure,
sequencing, and enough about quality that the failure mode is "author couldn't publish" rather
than "author published something ambiguous."

**Reason.** Same pattern as the publish skill: the mechanism knows how to execute, the content
owner knows what to execute. This means `/migrations-apply` never needs updating when a new
standard adds migrations.

---

## D34 — Multiple independent triggers for reliability

**Status: retained as a reliability principle and revised by `D45` and `D48`.** Generic trigger
intent belongs in Migration; concrete discovery/trigger realisation and independence evidence
belong in Scope and the applicable platform design.

**Decision.** On the chat side, where no hook mechanism guarantees execution, reliability is
achieved through multiple independent triggers rather than a single guaranteed one.

**Trigger independence.** Triggers must fail independently to multiply rather than correlate.
Three skills that all depend on the same retrieval mechanism are one trigger wearing three hats.
Independence comes from spreading across different mechanisms: always-resident instruction,
skill body invocation, a step inside an already-invoked procedure.

**Planned trigger inventory.** The design will include a table listing each trigger point, the
mechanism that causes it to fire, and whether it is independent of the others. This makes the
independence claim inspectable rather than assumed.

**Always-on instruction line.** A line in the plugin's instructions-to-Claude (always-resident,
not retrieval-dependent) pointing to `/migrations-check`. This is the strongest available
trigger on the chat side and is the primary required-migration trigger. The line is a pointer
only — no logic — keeping the always-on budget small.

**Adjacent-skill chaining.** Skills that fire from different triggers (document save, date stamp,
version update) include a reference to check migrations. Each chain inherits the reliability of
its host — a chain from an always-on host is strong; a chain from a retrieval-dependent host
adds a hat but not independence.

**Reason.** Follows the arithmetic established in the Standards Brief (S1, three independent
triggers): three loose triggers at sixty percent each leave under seven percent chance of all
missing. But the arithmetic only holds if failures are independent, which is why the trigger
inventory exists.

---

## D35 — Five-stage capability production chain

**Status: superseded by `D49`.** The useful responsibilities survive as two ownership flows—
capability production and capability deployment—followed by host pickup as an external
consequence. The fixed five-stage chain is no longer the parent model.

**Decision.** Producing and deploying capability artefacts follows a five-stage chain:

1. **Build** — takes a design document and produces the artefacts it declares: tool documents,
   standard documents, and migration files. Also applies platform design to produce platform
   variants. Build is capability-specific — a different build command exists for different kinds
   of output (capability packages, work packages, etc.). The command is `build-capability`, not
   bare `build`, to avoid skill collision with other domains' build commands that may land in
   the same plugin.

2. **Package** — assembles the build outputs into a deployable capability package with a package
   manifest. The manifest is the contract between capability-specific production and generic
   deployment: it carries required-migration flags, the standard version each migration attaches
   to, platform applicability per file, and a removal list for deprecated skills. Package is
   capability-specific.

3. **Platform deployment package** — takes the capability package and produces a
   platform-specific deployment package. Plugin packaging is platform-dependent (Claude plugins
   are git-hosted; other platforms may differ). This stage resolves which files apply to the
   target platform and excludes the rest.

4. **Publish** — pushes the platform deployment package to the plugin repository. This is the
   only stage that touches a live plugin. It needs git access (for Claude), reads the manifest,
   updates the `{key}_pendingmigrations` skill version if the manifest declares a required
   migration, and pushes. If the manifest declares skill removals, publish removes them from
   the plugin.

5. **Plugin update** — the host platform picks up the published changes. For Claude, this is
   periodic sync (24–48 hours) or manual refresh. This stage is a platform responsibility,
   not an AI-workflow responsibility.

**Build naming.** `build-capability` as the command, not bare `build`. Build is a family of
commands across domains (capability packages, work packages, etc.) and multiple build commands
may land in the same plugin. Each command carries a scoped noun to prevent collision.

**Reason.** Five stages because each has a distinct owner, a distinct input/output, and a
distinct failure mode. Build and package are capability-specific. Platform deployment package
and publish are deployment-specific and platform-aware. Plugin update is a platform
responsibility. Separating them means you can build and inspect before committing to
distribution, and a failure at any stage does not leave downstream stages in an inconsistent
state.

---

## D36 — Capability versioning is deployment versioning

**Status: retained as design input; detailed contract reopened by `Q12` and local-type boundary
revised by `D53`.** The distinction between document version and produced artefact version
remains. Any build/deployment record begins as a local Capabilities artefact rather than an
automatically shared DocMeth type.

**Decision.** A capability version (the version of a standard or tool) is a deployment version,
not a document version. It serves a different purpose from DocMeth document versioning.

**Version increments on publish, not on build.** Build regenerates freely — the same version
number is reused across iterations until the artefact is deployed. Once deployed, the next build
automatically increments. The version number carries no semantics about the nature of the
change; required-versus-lazy is declared separately in the migrations file.

**Per-artefact, not per-design.** If a design emits two standards and only one changed, only the
changed standard increments. The unchanged artefact stays at its current version — no
unnecessary trigger fired, no false migration signal.

**Build record.** Build and deployment state is tracked in a machine-maintained document (a new
document type — build record or output record), not in the design file. The design is
human-authored; the build record is machine-maintained. Mixing them means every deployment bumps
a design version for no design reason. The build record holds: what was built, what version,
what's deployed, and when. Never hand-edited.

**Reason.** A capability artefact is an output from design, not a working document. You don't
modify a standard directly — you modify the design and regenerate. The version therefore tracks
"which deployment is live," not "which edit pass was this." Semantic versioning (major/minor)
was considered and rejected: a release can carry both required and lazy changes, so a number
encoding both would lie.

---

## D37 — Deployment is a subtopic of Capabilities

**Status: retained and revised by `D43` and `D49`.** Deployment is one of seven peer components
and begins at the completed package boundary.

**Decision.** Deployment — the stages from package onward (platform deployment package, publish,
and the interfaces they require) — is a subtopic of Capabilities. It is platform-agnostic at
its interface: it takes a deployment package and a manifest, resolves platform-specific
packaging, and pushes to whatever hosts the plugin.

**Generic service.** Deployment does not know or care what produced the package. Standards and
tools are the first consumers, but anything that produces a deployable package can use the
deployment service.

**Platform resolution.** The manifest declares platform applicability per file. Deployment
filters by platform and builds the platform-specific deployment package. For Claude, the target
is a git-hosted plugin. For other platforms, the target and mechanism may differ. Platform
variance lives in the deployment design, not in the capability-specific stages.

**Reason.** Same principle as migration (`D28`, migration as a capability-level service):
deployment is infrastructure, not a feature of any one capability kind. Placing it in Standards
or Tools would force other consumers to depend on a peer subtopic.

---

## D38 — Currency delegated to host environment

**Decision.** Currency — whether the locally installed version of a standard or tool is the
latest published version — is delegated to the host environment administrator, not managed by
the AI workflow.

**What this means.** The AI workflow does not build a currency-reporting layer. Git-hosted
plugins already sync periodically (24–48 hours for Claude) or can be manually refreshed. The
developer or environment administrator is responsible for ensuring deployments are picked up.

**What is not delegated.** Migration checking (`D30`, `D31`) remains in-workflow. Migration
answers "is there required work to do against what I have"; currency answers "do I have the
latest release." These are different questions. Migration is the AI's responsibility because
migration instructions live inside the workflow. Currency is the host's responsibility because
the sync mechanism lives outside the workflow.

**Reason.** Building a currency layer would duplicate what the platform does while depending on
the same mechanism, so it would not be independent. The migration mechanism already covers the
case where being behind actually costs something — a required migration. Being behind on lazy
changes has no consequence until the artefact is next edited, at which point the document-level
check picks it up.

**Resolves the remaining open portion of `Q7` (versioning, currency, and drift).**

---

## D39 — Audience carried by scope, no per-unit marker

**Status: retained; ownership revised by `D45`.** Scope owns the model that carries audience and
applicability.

**Decision.** A weighted unit's audience is determined by the standard's scope declaration. No
per-unit audience marker is needed. A standard that genuinely needs to address both AI and human
audiences in the same document is likely two standards that should be separated.

**Reason.** The scope model (`D18`/`D19`) already carries audience. Adding a per-unit marker
solves a problem scope has already solved at a higher level. Context-weighted explanatory
material aimed at a different audience than the standard's primary scope is already distinguished
by its weight — Context carries no obligation, so the audience difference is self-evident.

**Resolves `Q5` (audience per weight).**

---

## D40 — Tone enforcement belongs in review

**Status: retained; ownership revised by `D44`.** Standards may supply the relevant review
profile, while Review owns the reusable assessment and disposition model.

**Decision.** The Standards Standard's review profile includes a check that every weighted unit
states its value and consequence, per `§5` (weight justification, `Capabilities_Standards_Design`).
This is a review concern, not a publish gate. No mechanical enforcement.

**Reason.** The facilitation framing (`D9`, role and purpose of a standard) is load-bearing —
it's worth more than a design principle nobody checks. But justification quality is a judgment
call, not a structural property. A publish gate would devolve into checking whether a
justification string exists rather than whether the justification is meaningful. Review can
assess quality; a gate cannot.

**Resolves `Q6` (tone enforcement).**

---

## D41 — Platform-specific design not re-admitted

**Decision.** The platform-specific content in `Workflow_Capabilities_Design` v1 §10–§11 (plugin
architecture and platform corrections) is not re-admitted into the Capabilities design. The
design content is superseded by `D35`–`D38` (the five-stage production chain, versioning model,
Deployment subtopic, currency delegation). The platform corrections (Code tab sharing config with
CLI, MCP reachable via plugin, project knowledge RAG switching) are factual findings about the
Claude platform, not Capabilities architecture — they belong in Claude platform reference
material, not here.

**Reason.** Re-admitting content already replaced by better-reasoned decisions is layering on a
superseded premise. If a Capabilities platform design document is ever needed, it would be
authored fresh from the current design, not recovered from the old document.

**Resolves `Q2` (platform-specific design re-admission).**

---

## D42 — Five-stage chain re-runnability model

**Status: revised by `D49`.** Re-runnability remains a component-design requirement, but it must
be restated against the two current flows rather than the superseded fixed five-stage chain.

**Decision.** Stages 1–3 (build, package, platform deployment package) are idempotent by
construction — same inputs produce same outputs, re-run freely. Stage 4 (publish) is re-runnable
from the build record — the record tracks what was successfully pushed, and a re-run picks up
from there. No rollback mechanism. Stage 5 (plugin update) is delegated to the host platform
(`D38`) and out of scope.

**Reason.** Stages 1–3 take defined inputs and produce defined outputs with no external side
effects — idempotency is inherent, not engineered. Stage 4 touches a live plugin repo, so partial
failure is possible; the build record (`D36`) already provides the resumption state needed for
clean re-run. Rollback is overkill for a git-hosted plugin where a bad push is correctable by
another push. No new mechanism is needed beyond what `D36` already provides.

**Resolves `Q11` (five-stage chain re-runnability).**

---

## D43 — Seven top-level Capabilities components

**Status: superseded by `D60`.** Tags becomes an eighth peer component.

**Decision.** Capabilities has seven peer components: **Standards, Tools, Scope, Dependencies,
Migration, Deployment, and Review**.

Standards and Tools are capability-producing components. Scope, Dependencies, Migration,
Deployment, and Review provide independently useful shared behaviour consumed across capability
kinds and, where applicable, other domains.

**Reason.** The former parent model concentrated shared mechanisms inside Standards and Tools,
which duplicated ownership and made platform, transition, deployment, and review concerns appear
as features of the first consumer that needed them. Each of the five extracted concerns has a
distinct question, contract, and set of consumers.

---

## D44 — Review is a Capabilities component

**Status: retained and detailed by `D71`.**

**Decision.** Review is a first-class Capabilities component, not an AIDE- or Workflow-only
behaviour. It owns the reusable lead/reviewer assessment model, the distinction between findings
and remedies, and the disposition discipline for review outcomes.

The lead owns the current design or outcome and its net simplicity. Reviewer findings are
evidence, not requirements. Before adding a mechanism, the lead considers accepting the risk,
removing the need, or reshaping the model. Lead/reviewer assignment is task-specific rather than
permanently attached to a particular model.

**Reason.** Independent assessment and disciplined response are reusable across designs,
standards, tools, code, and other outcomes. AIDE is one consumer, not the natural owner.

---

## D45 — Scope owns applicability and platform trigger realisation

**Status: superseded by `D63` and revised by `D55`.** Scope retains applicability only. Tags
owns the machine classification/query substrate; concrete platform trigger/discovery rendering is
a Build-side platform concern.

**Decision.** Scope is a first-class component. It owns the shared mechanical/context
applicability model and the platform-specific rendering of trigger and discovery cues.

Capability authors declare where their capability applies. Scope defines how that declaration is
interpreted and how `Scope_Design_Platform_{Name}` turns it into effective metadata, descriptions,
or retrieval cues for a target platform.

**Reason.** Standards, Tools, and Migration all need applicability and triggering. Leaving the
mechanism in each component duplicates it and allows platform retrieval techniques to leak into
generic capability designs.

---

## D46 — Dependencies owns dependency and document-footer semantics

**Status: revised by `D65`–`D68` and `Core_System_Decisions` v2.** Dependency semantics remain
with Dependencies; document metadata containers are hosted generically by DocMeth, identity is a
system primitive, and compact declaration/query semantics are now defined.

**Decision.** Dependencies is a first-class component owning dependency identity, version
declaration, the semantic distinction between dependencies and references, runtime availability
checks, version-gap meaning, and the rules for advancing a dependency declaration.

The dependency line/region in a document footer is an expression of this generic dependency
model and moves from DocMeth to the Dependencies Standard. DocMeth may own the shared footer
component and its other metadata, but it consumes Dependencies for dependency semantics.

A declared dependency version records the version against which the dependent artefact was last
conformed or validated. It does not advance merely because a newer dependency becomes available.

**Reason.** Dependency behaviour is useful beyond documents and should not be owned by a
methodology simply because documents were its first carrier. A single generic owner lets
Migration act on the same version meaning across artefact kinds.

---

## D47 — Required Migration and On-Update are distinct transitions

**Status: retained semantically; physical source separation revised by `D58`.**

**Decision.** Migration supports three classifications for a dependency change:

- **Required Migration** — the old dependent state cannot safely continue for applicable work;
  transition is blocking.
- **On-Update transition** (`OnUpdate` in identifiers) — the old state remains usable, but
  declared steps are applied when the artefact is next modified.
- **No transition** — the change affects new work or requires no alteration to existing
  artefacts.

Required Migration and On-Update instructions are separate artefacts or unequivocally separate
package members. The owner of the changed dependency authors both kinds of transition content;
Migration owns format, ordering, checking, and execution posture.

**Supersedes:** `D29`; revises `D28` and `D33`.

**Reason.** A Standard alone does not reliably tell an AI which existing content to revisit on a
partial edit. Explicit On-Update deltas avoid reconstructing changes between versions, while
physical separation prevents an AI from inferring urgency from mixed transition prose.

---

## D48 — AI-oriented On-Update trigger and explicit command set

**Decision.** Automatic On-Update is triggered when an artefact with an older declared
dependency is being edited, revised, regenerated, reviewed for update, or prepared for changed
output. Merely opening or discussing it does not cause gratuitous rewriting.

Migration defines at least three explicit logical commands:

- `/migrations-check` — report pending Required Migrations;
- `/migrations-apply` — apply authorised Required Migrations;
- `/update-doc` — force On-Update reconciliation for one or more documents.

`/update-doc` is idempotent. It applies only pending On-Update transitions in version order,
advances dependency declarations only after successful application, and makes no substantive
change when the target is current. The no-op report states that no On-Update actions were
pending. If a Required Migration is encountered, `/update-doc` stops or defers the affected
target and reports the required path; it never treats blocking work as On-Update.

**Supersedes:** `D30` and `D31`; revises `D34`.

**Reason.** AI interpretation is the normal execution surface, so the generic trigger describes
the semantic update event rather than a fragile save hook. The explicit idempotent command is a
cheap verification and recovery path when automatic triggering is missed.

---

## D49 — Production and Deployment are separate ownership flows

**Status: retained at the package boundary; production flow revised by `D54`–`D57`.**

**Decision.** Capability production is:

```text
Design → build → package
```

Capability deployment is:

```text
package → platform preparation → distribute/publish
```

Host pickup/update is an external consequence by default. Standards and Tools own build and
package for their outcomes. Deployment accepts completed packages and owns the steps from
platform preparation through distribution/publication.

The parent architecture no longer uses Publisher as its organising concept or a fixed five-stage
chain. Mechanical transformation, loud failure, resumability, and idempotency remain constraints
for the detailed producer and Deployment designs where applicable.

**Supersedes:** `D2` as parent organising model and `D35`; revises `D37` and `D42`.

**Reason.** Production and deployment have different owners, inputs, and responsibilities. The
package is the clean contract boundary. Host synchronisation should not be modelled as an
AI-owned stage when the host controls it.

---

## D50 — Generic design produces a base outcome before platform divergence

**Status: superseded by `D54` and `D55`.**

**Decision.** The common platform pattern is:

```text
Generic Design → base outcome → apply Design_Platform_{Name} → platform outcome
```

`Design_Platform_{Name}` contains only divergence from the generic Design. It may add, constrain,
substitute, or mark behaviour unavailable, but may not silently contradict the generic intent.
If no divergence is required, the base outcome proceeds unchanged.

**Reason.** The convention applies to more than documents and avoids restating the whole design
for each platform. It keeps generic meaning stable while allowing platforms to realise that
meaning differently.

---

## D51 — Standards publishes generic Production and Usage standards

**Decision.** Standards publishes two standards under its own ownership:

- **Standards Production Standard** — how standards are defined, authored, structured, built,
  reviewed, and packaged.
- **Standards Usage Standard** — how sessions discover, interpret, combine, and operate under
  applicable standards, including weight, conflict, deviation, and unavailability behaviour.

Both are generic. The Usage Standard is not scoped to AIDE; AIDE is one consumer.

**Supersedes:** `D16` and `D27`; revises the audience application in `D17`.

**Reason.** Runtime behaviour is behaviour for using standards, not behaviour owned by AIDE.
Separating production and usage still preserves distinct audiences and lifecycles without
coupling the shared runtime contract to one domain.

---

## D52 — Tool definitions include contributed commands

**Status: retained; platform rendering ownership revised by `D55`.**

**Decision.** A Tool design defines the logical commands or invocations the tool contributes,
including command identity, purpose, and invocation semantics. A platform design may alter the
concrete rendering, name, or availability needed on that platform without changing the logical
behaviour.

**Revises:** `D20` and `D25`.

**Reason.** Commands are part of how a Tool is selected and invoked. Leaving them until
deployment separates the interface from the behaviour it exposes and invites platform variants
to invent incompatible contracts.

---

## D53 — Domains may define local document types; DocMeth owns shared types

**Decision.** A domain may define the document types required by the artefacts it creates. Those
types remain local while their meaning and lifecycle are domain-specific. DocMeth owns only
document types and document components that are genuinely shared across domains.

Potential DocMeth consequences discovered during this architecture pass are recorded separately
for a later DocMeth review. DocMeth is not redesigned in this pass.

**Supersedes:** `D3`.

**Reason.** Requiring every useful local type to enter DocMeth centralises domain design and
expands the methodology before reuse is demonstrated. Local definition preserves ownership;
cross-domain recurrence provides evidence for later promotion.

---

## D54 — Canonical capability production and Build WorkPackage handoff

**Decision.** Capability production on Design side follows:

```text
Capability Design
      ↓
Build Capability
      ↓
Canonical Standard / Tool
      ↓
effective Build Config
      ↓
Build WorkPackage
```

`Build Capability` consumes the confirmed Capability Design and produces the canonical Standard
and/or Tool. The canonical outcome carries the complete capability definition and everything
capability-specific that Build side needs.

The Build WorkPackage is the handoff into Build-side execution. Build side should not need to
reopen the internal Capability Design to determine the required result.

**Revises:** `D49`; supersedes the base/platform-outcome part of `D50`.

**Reason.** The earlier `Design → build → package` shorthand concealed two different concerns:
deriving the canonical capability from Design and physically realising that capability for a
platform. Keeping canonical production on Design side and platform realisation on Build side
aligns capability work with the same governed handoff used for code production.

---

## D55 — Platform adaptation belongs Build side; capability addenda carry only capability-specific intent

**Decision.** Generic knowledge of how a platform implements Standards or Tools belongs on Build
side in platform Standards, Tools, and reference material.

A Capability Design may contain platform-specific considerations only where that particular
capability has a meaningful platform-specific requirement. Those considerations are delta-only
and are carried into the canonical Standard/Tool as platform addenda. Absence of an addendum
means the generic capability applies unchanged.

The addendum expresses **what must be true for this capability on that platform**, not generic
mechanics such as skill, plugin, repository, command-file, or bundle structures.

Build-side platform builders combine the canonical capability and its addenda with what the Build
environment already knows about the target platform.

**Supersedes:** `D50`; revises platform-rendering language in `D45` and `D52`.

**Reason.** Capability design should not need to know implementation facts shared by every
capability on a platform. Keeping reusable platform mechanics Build side prevents repeated
platform knowledge from leaking into each Design while preserving genuine capability-specific
platform intent.

---

## D56 — Effective Build Config

**Decision.** Every buildable capability has an effective Build Config declaring:

- target platforms, or the current supported-platform default set;
- side applicability: Design, Build, or both, with **both** as the default;
- one or more named Deployment Sets.

The Build Config may be physically managed on Design side or Build side according to preference.
By WorkPackage execution it must resolve to one effective configuration.

Operational storage does not transfer authority over capability intent. A Build-side config
cannot silently redefine a design decision merely because it is stored there.

**Reason.** Capability meaning and production/deployment targeting are separate concerns. The
Build Config gives targeting and placement a small explicit home without putting repositories,
plugin layouts, bundle filenames, or other platform implementation detail into the Capability
Design.

---

## D57 — Deployment Set is the logical deployment destination

**Decision.** A Deployment Set is a named logical grouping/destination for capability packages.
A capability's Build Config declares the Deployment Set name; platform Deployment configuration
resolves that name to the concrete target representation.

Example:

```text
Deployment Set: workflow-core

Claude
  → plugin "workflow-core"

Codex
  → corresponding Codex capability collection

ChatGPT
  → merged project bundle
  → workflow_core_bundle.md
```

Build remains capability-local. Deployment is set-aware and may compose contributions from many
capability packages into one Deployment Set artefact.

For ChatGPT, the merged bundle is therefore a Deployment Set output, not an individual capability
package output.

**Reason.** The same logical capability grouping needs different physical representations on
different platforms. Naming the logical destination once keeps capability configuration stable
while allowing Deployment to implement each platform independently.

---

## D58 — Transition declarations live with the canonical Standard or Tool

**Decision.** Required Migration and On-Update declarations are authored in the canonical
Standard or Tool that owns the changed dependency. Their postures must remain unequivocally
distinguishable, but separate source migration files are not required.

The capability builder uses a **Migration Build Standard** to transform the authored declarations
into canonical migration information. Build-side platform and Deployment Set builders extract
and adapt that information into whatever representation their target requires.

Migration continues to own transition semantics, structure, ordering, execution posture, and
runtime tools. The capability owner continues to author the actual transition intent.

**Revises:** the physical-separation requirement in `D47` and the source-file model in `D33`.

**Reason.** Transition information is intrinsic to the lifecycle of the Standard or Tool version
that causes it. Keeping it with the capability prevents a second source from drifting, while the
build layers still produce platform-specific migration artefacts where needed.

---

## D59 — WorkPackage belongs to AIDE Build, not Capabilities

**Decision.** WorkPackage becomes a subtopic of the top-level AIDE Build topic and is developed
as its own Standard/methodology.

Capabilities consumes WorkPackage for design-side-to-build-side handoff. Capability execution
returns the standard WorkPackage Outcome containing the build result, including success,
partial success or failure, reasons, validation results, produced artefacts, deviations,
observations, and feedback needed to fix or continue the work.

**Reason.** WorkPackage is a generic execution mechanism used by capability builds and code
builds. Owning it inside Capabilities would force unrelated Build work to depend on a
capability-specific domain.


---

## D60 — Tags is an eighth peer component and a general classification substrate

**Status:** Superseded as the current component count by `D87` and `D92`; Tags remains a peer component.

**Decision.** Add **Tags** as an eighth peer Capabilities component. Tags provides a general
machine-usable classification and query substrate and is not limited to capability applicability.
Scope consumes Tags rather than owning the tag system.

Capabilities is therefore:

```text
Capabilities
├── Standards
├── Tools
├── Tags
├── Scope
├── Dependencies
├── Migration
├── Deployment
└── Review
```

**Reason.** The mechanism uncovered while designing Scope is fundamentally broader: Standards
can derive classifications from artefact information and any component can query those
classifications. Keeping it inside Scope would make a reusable taxonomy/query primitive appear to
exist only for behaviour matching.

---

## D61 — Tag Builders keep semantic complexity with the semantic owner

**Decision.** `AIDE_Tags` defines a Tag Builder contract. Any Standard may embed an
`AIDE_TagBuilder` YAML definition describing how to detect applicability, locate/read its source
information, generate current tags, and identify the output it owns.

The semantic owner resolves inheritance and other domain-specific relationships before the Tag
Builder consumes them. Tags and runtime matching do not traverse semantic inheritance chains or
reopen source Standards.

Tag Builders are discovered from the Standards available to the current execution context. Each
builder is responsible for generating and cleaning up only its own tags and must be idempotent.

**Reason.** Denormalising semantic complexity before runtime keeps the implementation reliable:
owners understand their own meaning; Tags can remain a small generic execution/storage/query
contract. Complex runtime inheritance chains are fragile, particularly in AI/chat execution.

---

## D62 — Generated tag ownership may use prefix or group; groups are otherwise invisible

**Decision.** A Tag Builder may identify generated output either by an owned prefix or by an
owned `{key}:[...]` group in the compact `Tags:` property. The key is only an ownership marker
recognised by the builder; it does not need to be the builder or owner name.

Groups have no semantics anywhere else. Every consumer except the owning builder sees a flat set
of tag values and ignores group keys. Manual tags may coexist with generated tags.

Tag matching uses a deliberately small Boolean language over exact flat tag values: `!` (NOT),
`&` (AND), `|` (OR), and parentheses. Extra tags are irrelevant unless the expression names them.
Tags contain no whitespace; `-` or `_` may separate words.

**Reason.** Prefixes are useful where qualification adds meaning; groups are useful where a
prefix would be counterproductive but generated ownership still needs to be recoverable. Making
groups private maintenance structure preserves one simple query model.

---

## D63 — Scope is the applicability layer above Tags and AI context

**Decision.** Scope is reduced to a thin applicability contract with two optional layers:

1. **Machine Scope** — an `AIDE_Tags` Boolean query.
2. **Context Scope** — a natural-language condition evaluated by the AI against the current
   context.

When both exist, both constrain applicability. Machine Scope evaluates first and can short-circuit
Context Scope. Scope returns applicable/not-applicable and does not execute the behaviour.

Scope may attach to a whole Standard or Tool or to an individual rule/behaviour.

Concrete platform retrieval, trigger, skill/plugin, repository, bundle, or other discovery
mechanics belong to Build-side platform Standards/Tools.

**Reason.** Flat tag matching is excellent for cheap deterministic filtering; AI context is one
of the strongest assets of the platform for semantic judgment. Encoding contextual nuance into a
large machine rule language would add complexity without adding value.

---

## D64 — Missing Scope means unrestricted; explicit disabled means never applies

**Decision.** Scope omission is permissive:

- Machine Scope absent → no machine restriction.
- Context Scope absent → no contextual restriction.
- Both absent → generally applicable.
- Both present → both must pass.
- `Disabled: true` → never applies.

This supersedes the earlier rule that no declaration means applies nowhere.

**Reason.** Absence naturally means no restriction on that dimension and avoids boilerplate for
broadly applicable behaviour. Intentionally inactive behaviour needs an explicit state rather
than overloading omission.

---

## D65 — Dependencies use compact declarations with normal, required, and startup-required levels

**Decision.** Dependencies use a compact metadata property, for example:

```text
Dependencies: abc, !def@v4, !!ghi@!v7, owner:[jkl@v2, !mno]
```

A Dependency means the artefact relies on another identified artefact or capability for some
part of its correct schema, design, content, interpretation, conformance, maintenance, or
execution.

Presence levels are:

- `abc` — normal dependency; check when relevant to the operation.
- `!abc` — required dependency; check on relevant access/use and raise missing state prominently.
- `!!abc` — best-effort session-start check and also a required dependency thereafter.

Other Standards/Tools may define stronger blocking behaviour when a required dependency is
missing; Dependencies' minimum contract is prominent reporting.

**Reason.** The syntax makes dependency importance visible without turning Dependencies into a
policy engine. `!!` captures foundational dependencies that should be checked as early as the
platform permits while acknowledging that chat startup behaviour cannot always be enforced.

---

## D66 — Dependency identity resolution is separate from version comparison

**Decision.** A dependency resolves by identity name first, ignoring version. Version is compared
after identity resolution. A referenceable artefact may expose multiple identities using the AIDE
system identity convention; the first is primary and later entries are aliases/other exposed
identities.

`abc@v8` records the dependent artefact's last proven conformance checkpoint against `abc` v8.
If `abc@v12` is available, identity/presence resolves successfully and the query reports the
`v8 → v12` gap. The newer version does not make the dependency missing.

`abc@!v8` means the available identity must expose exactly v8. The `!` before the dependency and
the `!` after `@` have separate positional meanings and may be combined.

**Reason.** Version is state about a resolved identity, not identity equality. Treating version
as part of the match would hide exactly the condition Migration needs to see: the correct
dependency exists but has moved beyond the dependent artefact's conformance checkpoint.

---

## D67 — Dependency Query reports factual state for downstream policy

**Decision.** `AIDE_Dependencies` defines a Dependency Query that reports, per declaration,
identity resolution, requirement level, declared conformance version, available version, version
relation, version gap, and exact-version result where applicable.

Dependencies reports the state but does not decide migration policy or every operation's
continue/stop decision. Migration and the current operation consume the result.

**Reason.** Downstream systems need to distinguish missing identity, matched/current, matched but
newer, matched but older, unknown version, and exact-version failure. Collapsing these into one
boolean would discard the information needed for safe action.

---

## D68 — Dependency Builders mirror Tag Builders and conformance markers advance only after work succeeds

**Decision.** Any Standard may embed an `AIDE_DependencyBuilder` definition. Discovery,
idempotency, generated-output ownership, and group/prefix cleanup follow the Tag Builder pattern.
Groups are maintenance structure only and are ignored by all consumers except the owning builder.

A dependency's recorded conformance version advances only after all applicable migration,
On-Update, or other conformance work through the recorded target has completed successfully. A
newer available dependency never advances the declaration by itself.

If a Required Migration at v10 is applied to an artefact recorded at v8, v10 becomes the proven
checkpoint. When later update/save work successfully completes all remaining applicable steps to
v12, the declaration advances to v12.

**Reason.** The footer must record evidence of completed conformance rather than the version that
happens to be installed. This makes it a durable checkpoint from which Migration can determine
which transition range still needs consideration.

---

## D69 — Dependency startup checks use the system bootstrap primitive

**Decision.** `!!` dependency checking uses the system-level `{bootstrap}` convention defined by
Core. Dependencies may contribute a bootstrap block that asks the environment to check
discoverable startup-required dependencies. The marker and the instruction to discover bootstrap
blocks are not owned by Dependencies.

**Reason.** Startup discovery is useful to more than Dependencies and depends on platform-wide
persistent instructions. Keeping the primitive in Core lets Dependencies state intent while
platform implementations use the strongest available mechanism without duplicating startup
logic.

---

## D70 — Deployment consumes a Capability Package plus Deployment Manifest

**Decision.** The hard producer-to-Deployment boundary is a **Capability Package plus a
Deployment Manifest**.

The Package is the capability-local payload. The Deployment Manifest is machine-readable
deployment intent/metadata needed to place and maintain that payload, including at least package
identity/version, Deployment Set membership, platform applicability where required, and
replacement/removal information demonstrated by Deployment needs.

Deployment Config remains environment/platform knowledge that resolves logical targets to
physical repositories, plugins, bundles, collections, paths, or other destinations.

Deployment must not reopen Capability Design to reconstruct deployment intent.

**Reason.** Treating all deployment intent as implicit package content forces Deployment to infer
placement and lifecycle semantics from payload structure. Separating payload from deployment
intent preserves a mechanical boundary while allowing the manifest schema to remain as small as
actual Deployment requirements permit.

---

## D71 — Review child contract and artefact split

**Status:** Communication-owner/open-seam portion superseded by `D93`; the Review lifecycle and artefact split remain current.

**Decision.** Review is finalised as the reusable independent-assessment component for substantive
integrity, better decisions, insight, and proportionate risk management. The Lead owns the work,
authorised scope, net coherence, and Finding disposition; the Reviewer supplies a meaningfully
separate reasoning path and owns Findings as evidence rather than instructions.

One Review resolves independent **Type, Level, Mode, and Reviewer** inputs:

- Type defines what is being learned and the review lens;
- Level defines assurance strength and may change dynamically as consequence, reach,
  reversibility, or uncertainty becomes clearer;
- Mode is Full or Blind exposure to the Lead's current solution/reasoning; and
- Reviewer identifies the independent source, with actual Lead and Reviewer models recorded for
  every Round.

The five reusable Types and defaults are Check/Low, Inspect/Standard, Evaluate/Medium,
Robust/High, and user-activated Stress Test/Extreme. A higher Level increases reviewer/model
capability, depth, evidence, independence, iteration, re-review expectation, and completion
confidence without changing the Type's question.

Review owns the Trigger/Input/Request/Response/Round/Result lifecycle, append-only Round evidence,
Finding/disposition separation, Level-driven re-review, continuation without a fixed Round cap,
transient/durable persistence, and the rule that Review may discover beyond scope while execution
cannot expand beyond authorised work.

The output split is:

- `Capabilities_Review_Design` — complete internal component design;
- `Capabilities_Review_Decisions` — detailed Review reasoning;
- `AIDE_Review@v1` — stable Review semantics and lifecycle;
- `AIDE_ReviewProfiles@v1` — Check, Inspect, Evaluate, Robust, and Stress Test methods/defaults;
  and
- `Capabilities_Review_Tool_Design` — platform-independent orchestration specification for the
  future canonical Review Tool.

Environment configuration supplies current reviewer/model/capability/route availability, and a
shared communication capability supplies direct or AI Message-based transport. Review consumes
both through explicit seams and does not own their storage or permanent architecture.

**Reason.** The confirmed model preserves the proven benefit of a second AI perspective without
embedding volatile model mappings, transport, or work authority into Review. Separate Type and
Level avoid multiplying review variants; dynamic consequence-based intensity handles small but
high-risk work; append-only Rounds preserve the actual exchange; and Lead disposition plus scope
control prevents useful Findings from becoming disproportionate complexity or unauthorised drift.
The separate Standard/Profile/Tool outputs let stable semantics, evolving methods, and execution
mechanics change at their appropriate rates.

Detailed decisions: `Capabilities_Review_Decisions` v1, `D1`–`D25`.



---

## D72 — Required Migration is use-gated; OnUpdate is update-gated

**Decision.** Required Migration is checked when a dependent artefact is about to be relied upon
for relevant use. If applicable Required work is outstanding, it is completed before that affected
use proceeds. OnUpdate work does not block ordinary use and is applied when the artefact is next
modified/saved.

There is no default blanket Migration scan at session startup. `!!` remains the Dependencies
startup-presence posture.

**Supersedes:** the part of `D48` that treated `/update-doc` as stopping/deferring merely because
Required Migration was encountered.

**Reason.** Required describes when an existing state stops being safe to rely on; OnUpdate
describes work that may wait for the next changed save. Untouched documents do not need eager
rewrite merely because a dependency changed.

---

## D73 — Migration posture is version-level and transition history is positive

**Decision.** Every migratable capability release positively declares exactly one posture for
existing consumers: `Required`, `OnUpdate`, or `None`. Multiple transition items within the same
release share that posture.

The canonical capability retains the supported per-release transition history needed to move a
consumer from its supported baseline to current. Migration does not infer deltas by comparing old
and new capability text.

**Revises:** `D47` and `D58` by finalising the declaration semantics while retaining canonical
co-location of transition intent.

**Reason.** A positive version ledger makes urgency unambiguous and gives an old consumer a safe,
ordered path without reconstructing historical differences.

---

## D74 — MigrationSummary is the cheap discovery contract

**Decision.** Versioned migratable capabilities expose a compact `MigrationSummary` containing at
least current version, latest Required version, latest OnUpdate version, and optionally the oldest
supported migration baseline.

The summary is a fast negative/possible-work test. Detailed transition history is loaded only when
the summary shows work may exist. On skill-based platforms, Build should surface the summary in
eagerly available skill/header metadata where that platform supports it.

**Reason.** Most uses should be able to prove “no Required migration can apply” without loading a
potentially long transition history. The semantic contract stays platform-independent while Build
uses the cheapest platform representation.

---

## D75 — A Required migration update reconciles through current; checkpoints are saved-state facts

**Decision.** When Required Migration forces an artefact update/save, that update also applies
pending applicable OnUpdate work and normally reconciles through the current available dependency
version as far as successful execution permits.

Persisted dependency conformance checkpoints change only when the artefact itself is updated/saved.
`None` and positively `NotApplicable` versions count as successfully traversed for the next saved
checkpoint but never force a metadata-only save.

**Supersedes:** the `D68` example that advanced only to the Required version while leaving later
OnUpdate work pending despite already performing a save.

**Reason.** Once a Required migration has caused the next save, deliberately leaving compatible
pending OnUpdate deltas behind creates extra state and work with no benefit. Checkpoints should
record saved proven state, not merely runtime observation.

---

## D76 — Migration is stepwise durable and records compact owner-labelled unresolved state

**Decision.** Migration preserves successful progress version by version. If a later version fails,
partial changes from the failed version are not saved; prior successful work remains durable and the
checkpoint records the last saved successful version.

Failed or authorised Deferred migration creates/updates a compact Migration-owned temporary state
entry containing the current condition and, where known, what would allow success. It is surfaced
noisily and removed when a later successful update resolves it.

Documentation Methodology owns the generic location/rendering for temporary document state, not
Migration-specific placement.

**Reason.** Resumable partial progress is more useful than global rollback, while owner-labelled
state prevents failed work from disappearing or another capability from deleting state it does not
own.

---

## D77 — Dependency declaration order defines default processing precedence

**Decision.** Dependency declaration order is significant. Earlier dependencies have higher
default processing precedence wherever an operation needs deterministic ordering, unless an
explicit relationship or the governing operation supplies a more specific order.

This means foundational/processing precedence, not business importance or presence severity.
Migration uses it as the default order for independent dependency migration chains.

**Reason.** The dependent artefact already has an ordered dependency list; using that order avoids
inventing another orchestration property while remaining overridable where a real dependency order
exists.

---

## D78 — Exact-version constraints are migrated under governing consumer policy

**Decision.** Dependencies continues to report exact-version constraints/failure. Migration still
performs transition execution, but an applicable governing dependent Standard/document rule tells
Migration how the pin affects the path and resulting declaration: stop at the pin, move the pin,
relax it to normal conformance, or perform follow-on actions.

If no governing rule determines the treatment, Migration stops and escalates rather than guessing.

**Reason.** The meaning of an exact pin is contextual to the consumer. Dependencies can detect it
and Migration can execute change, but neither can infer why the dependent author pinned that
version.

---

## D79 — Migration history has an explicit supported baseline when pruning is needed

**Decision.** A capability retains transition history from the oldest supported conformance
version to current. `SupportedBaseline` is optional; if absent, retained history is the supported
path. Moving the baseline forward is a deliberate capability release decision.

A consumer older than the supported baseline receives an unsupported-baseline result and requires
an explicit recovery/upgrade procedure. Migration never silently skips missing history.

**Reason.** This allows old transition detail to be pruned eventually without turning missing
history into guessed migration behaviour.

---

## D80 — A Tool encapsulates a repeatable action contract, including bounded declared judgment

**Decision.** The Tool role is refined: a Tool removes the need to re-derive a repeatable action
and its safety/interaction contract. It may contain bounded judgment explicitly defined by its
inputs, decision points, inference/confirmation rules and escalation conditions. Substantive
authority it does not own remains external.

**Revises:** the overly absolute reading of `D20` that “judgment adds nothing,” while retaining its
core determinism/encapsulation/cost/completeness value proposition.

**Reason.** Review and Migration Tools legitimately orchestrate bounded judgments without becoming
owners of the substantive work. What must stay deterministic is the Tool contract for handling
those judgments, not the absence of reasoning altogether.

---

## D81 — Document, capability release, conformance, package identity and deployment state are distinct

**Decision.** Keep the version/state concepts separate:

- **Document version** — Documentation Methodology output version of a governed source/design doc.
- **Capability release version** — version on the published/referenceable canonical capability
  identity (for example `AIDE_Migration@v1`); increments when changed capability meaning is released
  for distribution, not when source documents are merely edited or a package is rebuilt.
- **Dependency conformance version** — consumer-side last saved/proven checkpoint against that
  capability release.
- **Package identity** — identifies a particular built package instance of one capability release;
  it is not another semantic capability version.
- **Deployment state** — factual record of what package/release is deployed to a target; not a new
  capability version.

A capability release is common across its platform contributions; platform packaging differences do
not create different semantic capability versions.

**Revises/clarifies:** `D36`.

**Reason.** Each value answers a different question. Collapsing them creates false migrations,
spurious release bumps, or an inability to distinguish a rebuilt package from changed capability
meaning.

---

## D82 — Package rebuilds use package identity/integrity, not a second semantic package version

**Decision.** A Capability Package is a build instance of one capability release. It carries a
unique/stable-for-that-build `PackageId`, the capability identity/release version it contains, and
integrity information sufficient to distinguish/validate the actual payload.

Rebuilding unchanged capability meaning may produce a new `PackageId`/digest while retaining the
same capability release version. No independent monotonically increasing “package semantic version”
is introduced until a demonstrated need exists.

**Reason.** Packaging can change because of build/platform fixes without changing the capability
contract. A build identity/digest distinguishes packages without lying to Dependencies/Migration
about capability meaning.

---

## D83 — Deployment Manifest producer contract is minimal and logical

**Decision.** The producer-side Deployment Manifest contract contains only information Deployment
can justify needing before its own detailed design:

```yaml
ManifestSchema: <manifest contract identity/version>
PackageId: <package build identity>
Capability: <formal capability identity@release-version>
Targets:
  - DeploymentSet: <logical set name>
    Platform: <logical platform/family>
    Contributions: [<package-local contribution ids>]
    Replace: [<optional deployed member identities>]
    Remove: [<optional deployed member identities>]
Integrity: <package/payload digest or equivalent>
```

Physical repositories, plugin names, paths, bundle names, credentials, and publication mechanics
remain Deployment Config/environment data. Transition detail remains payload/capability semantics
unless a future Deployment requirement demonstrates a manifest-level field is necessary.

Deployment may extend the schema only when its design demonstrates another mechanical input is
required; it must not reconstruct capability intent from payload structure.

**Completes:** the producer-side portions of `D70`, `WR8`, and `WR9` while leaving Deployment Set
lifecycle/atomicity/resumption behaviour open for Deployment.

**Reason.** The boundary is now strong enough to hand off mechanically without predesigning
Deployment itself.

---

## D84 — Build Capability is a Tool

**Decision.** The named production step previously shown as `Build Capability` is formalised as the
canonical design-side Tool `AIDE_BuildCapabilityTool`. Its sole production boundary is:

```text
confirmed Capability Design
        ↓
Build Capability Tool
        ↓
canonical Standard / Tool outcome(s)
```

The Tool applies the applicable Standards/Tools production contracts, validates identity/release and
shared Scope/Dependencies/Migration/Review semantics, and returns incomplete Design to the work
owner rather than inventing capability meaning.

It does not own Build Config, WorkPackage execution, platform implementation, Platform
Contributions, Package/Manifest construction, or Deployment.

**Reason.** `Build Capability` is a named repeatable invokable action, which meets the existing Tool
boundary. Leaving it implicit would require the production mechanism to be re-derived each time and
would make the architecture contradict its own “run X → Tool” rule.

---

## D85 — Canonical Tool is a published custom outcome type distinct from Tool Design

**Decision.** Capabilities defines a local custom document type `Tool` for published/referenceable
AI-facing invokable capability outcomes. `..._Tool_Design` remains the internal Design that
determines the Tool; `AIDE_<name>_Tool_vN` is the canonical outcome consumed by AI environments and
later platform Build.

The first canonical Tool outcomes are `AIDE_ReviewTool@v1`, `AIDE_MigrationTool@v1`, and
`AIDE_BuildCapabilityTool@v1`.

**Reason.** A Tool Design is not itself the executable capability outcome. Making the distinction
explicit gives Tools the same Design→canonical-outcome separation already used by Standards and
prevents Build from treating internal design documents as deployable capability content.

---

## D86 — Standards generic outcomes are now canonical published Standards

**Decision.** The two generic outcomes already declared by Standards are published as
`AIDE_StandardsProduction@v1` and `AIDE_StandardsUsage@v1`.

Standards Production governs deterministic Design→canonical Standard production. Standards Usage
governs runtime applicability, weight interpretation, composition, conflict/deviation and
migration-aware use. Build Capability invokes the Production contract for Standard outcomes.

**Reason.** The architecture had declared these as outputs but had not emitted them. Publishing
them closes the gap between the Standards Design and the capability surface actually available to
AI environments.


## D87 — Generic Deployment is promoted out of Capabilities

**Decision.** Deployment of arbitrary built artefacts into AI runtime surfaces is no longer a
Capabilities peer component. Capabilities remains responsible for capability semantics,
canonical production, Build contribution requirements, Capability Package identity/integrity and
logical deployment intent.

**Reason.** Deployment's intrinsic concerns are surface, representation, distribution channel,
destination/configuration, set composition and verified runtime state. Those are broader than
Capabilities and can serve other deployable artefact types.

---

## D88 — AI Deployment consumes rather than reinterprets capability intent

**Decision.** `AIDE_Deployment@v1` consumes package/build material and logical deployment intent
mechanically. It must not reopen Capability Design or infer semantic intent from payload shape.

**Reason.** This preserves the established self-contained producer handoff boundary.

---

## D89 — Surface, representation and distribution channel are separate deployment facts

**Decision.** A deployment target records runtime/surface, representation and distribution channel
separately.

**Reason.** Empirical OpenAI testing showed that the same local plugin/skill representation could
be usable through one Codex route without providing ChatGPT Chat runtime access. A representation
name alone therefore does not identify a deployable target.

---

## D90 — The tested common local OpenAI route hypothesis is rejected

**Decision.** Do not use “one local OpenAI plugin/skill install = common private ChatGPT + Codex
deployment route” as architecture.

**Reason.** The tested local route did not provide equivalent runtime discovery/execution across
those surfaces. Hosted/public/account-synchronised routes remain empirical implementation options,
not assumptions.

---

## D91 — Documentation Methodology handoff is closed by v18

**Decision.** Capabilities' DocMeth review items are considered dispositioned by Documentation
Methodology v18: generic metadata hosting, Dependencies/Migration conformance, temporary state and
compact generated content are now consumed through their owning contracts.

**Reason.** The receiving methodology now has a complete owner split; keeping the review handoff
open would duplicate completed work.


---

## D92 — Messaging is the eighth peer Capabilities component

**Decision.** Messaging is a first-class peer alongside Standards, Tools, Tags, Scope,
Dependencies, Migration and Review. It owns AI-MESSAGE envelope/schema semantics, message/thread/
version identity, reply/forward/convergence behaviour, `Expects`, receipt/reconciliation, source
marking, message-specific persistence semantics and messaging logical actions/workflow.

Documentation Methodology owns only generic governed-document integration when a Message is
persisted. Platform-specific skills/plugins/commands/triggers/direct-route/clock/file mechanics are
Build concerns.

**Reason.** AI-MESSAGE is useful across Review and other cross-context work. Giving the reusable
mechanism one Capabilities owner avoids both the old Workflow ownership and a duplicate transport
implementation inside Review or Documentation Methodology.

---

## D93 — Review consumes Messaging; the shared communication-owner seam is closed

**Decision.** Review retains Review/Round/request/response lifecycle and substantive review
semantics. Messaging owns AI-MESSAGE relay, receipt/reconciliation and messaging actions used by
Review for cross-context/manual transport. Environment/platform configuration continues to supply
current reviewer/model/route facts and concrete route availability.

**Reason.** The earlier Review architecture correctly kept transport external but deliberately left
its permanent owner unresolved. Messaging now supplies that reusable owner without changing Review's
assessment lifecycle.

---

## D94 — Messaging persistence uses existing live-state mechanisms; no dedicated obligations register

**Decision.** Normal messages remain in conversation. Use WIP only when active Messaging state must
survive context discontinuity, OpenItems for an outstanding obligation that genuinely must outlive
current work/context, and a persisted Message only when its actual body needs independent retrieval.
`=== STATE ===` remains the receipt-integrity mechanism and may construct its best-effort working
set from visible conversation plus those durable sources.

A reply proves receipt where correlated but closes the source only when its material `Expects` has
been satisfied, withdrawn, superseded or otherwise explicitly resolved.

**Reason.** The old obligations register mixed receipt bookkeeping with durable work persistence.
DocMeth v21 already has purpose-specific state mechanisms; preserving a second permanent ledger
would add reconciliation burden without unique value. Receipt and fulfilment must remain separate
so holding replies continue to work correctly.

---

## D95 — Messaging has no default Bootstrap Contribution

**Decision.** The canonical Messaging capability is platform-neutral. Normal Tool/Scope discovery
should recognise the strong `=== AI-MESSAGE ===` marker. Create a thin Messaging Bootstrap
Contribution only if target-platform evidence later demonstrates that ordinary discovery cannot
reliably recognise the capability when needed.

**Reason.** Bootstrap is intentionally thin and early-session only. The current design has no
demonstrated startup requirement that justifies eagerly loading Messaging merely because the
capability exists.



---

## D96 — Reference position determines version meaning; executable references default versionless

**Decision.** A version token has meaning from its syntactic role rather than from version syntax
alone. `Dependencies: X@vN` is the dependent artefact's saved/proven conformance checkpoint;
`References:` is a reader/evidence pointer with no currency or conformance obligation; and a
current executable in-body capability reference is an operational instruction rather than a
checkpoint.

Current executable references use the versionless capability identity by default. A specific
release may be named where the instruction deliberately depends on that release's contract or
intentionally targets it. Canonical production validates that such specificity is intentional and
correct; it does not mechanically force every body reference to the newest release.

**Reason.** Reviews A and B exposed repeated confusion between truthful saved history and current
execution guidance. Position already carries the practical distinction, so a new dependency
relationship taxonomy would add machinery without behavioural value.

---

## D97 — Conformance checkpoints create no execution order or dependency cycle

**Decision.** A saved conformance checkpoint is backward-looking evidence about the dependent
artefact. It creates no resolution order, execution order or cross-artefact sequencing requirement.
Mutual checkpoints are therefore not an operational dependency cycle. Dependency declaration order
has force only where the governing operation actually needs deterministic processing order within
the artefact being processed.

**Reason.** This resolves the Review A Index/Documentation Methodology apparent-cycle carry without
adding functional/schema/conformance dependency categories.

---

## D98 — Exact-version syntax is a hard present constraint, not a migration checkpoint

**Decision.** `X@!vN` requires exact vN to be available for affected use. If it is unavailable the
dependency is unsatisfied and affected use is blocked; another version may not silently substitute.
The exact constraint is not a saved conformance checkpoint and its mismatch is not an ordinary
Migration version gap. Changing or removing a pin is an explicit dependent-artefact change that is
validated and saved normally.

**Reason.** The published grammar should have deterministic default behaviour without introducing a
second generic pin-policy system.

---

## D99 — Canonical Tool production is published as a Tools-owned contract

**Decision.** Tools publishes `AIDE_ToolsProduction` as the generic design-side contract for
producing canonical Tools. Build Capability consumes it by identity, just as Standard outcomes
consume `AIDE_StandardsProduction`, rather than copying the Tool structure contract into Build
Capability or requiring a published Tool consumer to reopen internal Tools Design.

**Reason.** The complete Tool contract already belongs to Tools. Publishing it removes duplicated
contract text and makes Tool authoring/validation available independently of Build Capability.

---

## D100 — Tags owns freshness semantics without a generic orchestration engine

**Decision.** Tags remains the owner of generic generated-tag freshness. After source information
capable of changing generated tags changes, applicable builders run before the artefact is
published/saved as current where those tags form part of governed state. If freshness is uncertain,
builders run before tag-dependent behaviour relies on the tags. No runtime polling or generic
processing engine is introduced.

**Reason.** Machine Scope needs deterministic current input, but that need can be met by regeneration
at change/reliance boundaries rather than a new orchestration component. Concrete platform/build
realisation remains Review D work.

---

## D101 — Review correlation is authoritative over transport correlation for Review semantics

**Decision.** Review/Round identity in the Review request/response payload is authoritative for
Review lifecycle semantics. Messaging Thread/Message-ID/In-Reply-To provides transport-level
correlation. Positive disagreement between the two is a quarantine condition; Review does not
choose one interpretation and disposition the response.

**Reason.** Review and Messaging intentionally own different correlation layers. A single mismatch
rule closes the manual-relay integrity gap without teaching Messaging about Review internals.

---

## D102 — STATE evidence strength depends on retained evidence

**Decision.** Messaging `STATE` remains best-effort and asymmetric. Its evidential value depends on
the conversation/WIP/OpenItems evidence actually retained. A genuinely stateless context may
truthfully provide no receipt evidence; where positive receipt proof materially matters, use
explicit Ack/Acknowledge rather than treating empty STATE as assurance.

**Reason.** This states the inherent limitation of the deliberately register-free model without
reintroducing a permanent messaging ledger.

---

## D103 — Behind-current dependency checkpoints are expected steady state

**Decision.** Consumer conformance checkpoints will routinely remain several capability releases
behind current. That is the designed steady state until a qualifying save proves newer conformance;
newer availability alone is not decay, a defect, or an update trigger.

**Reason.** Making the expected state explicit removes recurring pressure for currency sweeps while
preserving the distinction between release history and current execution guidance.

---

## D104 — Review Profiles may advance independently from Review

**Decision.** Review Profiles remains a separately versioned capability contract. Its current
executable references to the Review contract are versionless unless a particular Review release is
intentionally required. Review and Profiles do not need matching release numbers.

**Reason.** Independent release cadence is the intended identity model; the Review C defect was the
stale executable version wording, not the split itself.

---

## D105 — Review C does not add a shared Builder substrate

**Decision.** Dependency Builder continues to mirror/reuse the small generic conventions established
by Tag Builder without introducing a separate general Builder capability. Reconsider only if another
builder family creates demonstrated common behaviour worth owning independently.

**Reason.** Two consumers do not justify a generic processing framework, and current mirroring is
already the smaller factoring.

---

## D106 — Review C preserves the eight-peer architecture

**Decision.** The Review C R1 architecture remains eight peers: Standards, Tools, Tags, Scope,
Dependencies, Migration, Review and Messaging. No peer merge/removal or new peer mechanism is
introduced by the accepted findings.

**Reason.** Robust Review found targeted missing rules/ownership surfaces rather than a structural
architecture defect. The existing distinctions continue to earn their complexity.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v10
References: Capabilities_Messaging_Design_v2, Capabilities_Review_Design_v3, AIDE_Messaging, AIDE_Review
<!-- END SOURCE: Capabilities_Decisions_v16.md -->
