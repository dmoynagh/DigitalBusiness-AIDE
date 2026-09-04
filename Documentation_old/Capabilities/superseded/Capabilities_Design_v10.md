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
