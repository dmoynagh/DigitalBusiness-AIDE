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
