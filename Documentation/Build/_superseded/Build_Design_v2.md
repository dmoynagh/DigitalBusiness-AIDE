> identity: Build_Design@v2 | doctype: design | updated: 2026-09-16

# Build — Design

## What Build is

Build is the transition to execution. It takes something defined — typically from design, but from any caller — and produces the outcome by creating and modifying files against a target. It then returns the result to whatever initiated the build for acceptance.

Build is a behavioural component: it defines conventions that are applied by following them, not machinery. The only concrete artefacts it produces as a component are the build mechanism, build standards, and the contract shape for build tasks and returns.

## The file-change principle

When files get created or modified, that is Build. This is a strong convention, not a blanket rule — it identifies the spine of build activity without claiming every file operation is formally a build.

The principle unifies what might otherwise appear as separate paths: applying a specification to a .NET codebase and persisting documentation changes are the same act against different targets — instruction crosses, agent discovers, edits, records, returns. What differs is the verification and convention layered on, not the act itself.

---

## The build mechanism

The build mechanism is the generic framework that applies to every build, regardless of target. It defines the relationship between the caller and the build, the authorities in play, and the completion model.

### The caller

Build returns to whatever initiated it — the **caller**. In many cases that is design, but it may be another build in a chain, or any other origin. Build neither knows nor cares what the caller is; it serves the request and returns.

The caller owns:

- **The instruction** — what the build should do. This sits on a spectrum from prescriptive ("change this exact line in this file") to intent-level ("apply this specification to the codebase"), where the agent owns discovery, planning and execution.
- **The decision scope** — the latitude and authority the build has to make its own calls. This ranges from "take care of it, don't come back to me" to "apply only these specific changes." The governing constraint: a build may make changes as needed within the granted scope, as long as it does not structurally change the fundamental design. Beyond that boundary, it returns to the caller.
- **Sign-off** — by default, a build does not sign off its own work; it returns to the caller for acceptance. But the caller may grant the build authority to self-accept. The default is the safe state; override must be explicit.

### The build package

The build package is the outbound handoff — what the caller sends to initiate a build. It is the matched counterpart of the build return: an open package with no return is an incomplete transaction.

#### Contents

A build package composes:

- **Instruction** — the caller's per-task ask, prescriptive to intent-level.
- **Decision scope** — the latitude and authority granted for this build.
- **Working target** — where the build may operate (when relevant to the target type).
- **Profile reference** — which build standards apply, as a named preset, inline definition, or both.
- **Definition of done** — the testable or assessable completion criteria for this task.
- **Intermediate exchange support** — whether the caller supports mid-execution questions and responses. Absent means not supported.
- **Transaction model** — commit, rollback and partial-completion expectations, where the caller wants to override the profile's default. Consumers fill the content; the invariant is that it must be something you can actually check against.

#### Sufficiency

The build package carries everything the build side needs to act without returning to the caller. Format-free, sufficiency required.

Sufficiency has a ceiling as well as a floor. The package does not re-supply generic knowledge the build environment already provides — execution-platform capabilities, the build standards already loaded via the profile, or standing conventions the target already knows. The package carries what is specific to this work.

#### Channel

The build package is **channel-agnostic** — it defines what crosses, not how it crosses. Orchestration is the most common channel for build work that dispatches to another AI platform, and the default where a build targets an AI agent. But direct chat, Messaging's envelope, and copy-paste are equally valid depending on context. The channel is the caller's choice.

### The return

Every build expects a return to the caller — transactional by default. The return reports against the definition of done supplied in the build package.

Fire-and-forget (no return expected) is allowed but must be explicitly declared by the caller at the point the package is created. The safe default is expected-return.

#### Return states

Five states, kept loose — the definition of done does the real work, not the enumeration:

- **Confirmed** — the definition of done is met.
- **Needs information** — build cannot proceed without input from the caller.
- **Raises an issue** — build has encountered something that needs caller attention.
- **Failed** — build could not complete. The return names the origin: caller-side (specification unclear, conflicting, unbuildable) or build-side (environment, tooling, execution failure). The response differs: a caller-side fault re-enters the caller's process; a build-side fault means retry or fix, nothing for the caller to rework.
- **Done with deviation** — build completed but the outcome differs from the specification. The caller decides whether to accept; accepting is a change that may produce fresh work.

#### Return sufficiency

The return carries everything the caller needs to reconcile without going back to build. Sufficiency is symmetrical with handoff sufficiency.

Never bare. Every return carries what was actually done or what prevented it — accessible and comparable against the commitment.

Return detail is proportional to the task — a trivial task earns a brief return, a high-impact task earns fuller reporting. Where the work was reviewed, the return identifies that a review was performed and carries the result.

### Work scope

Build tasks commonly need a declared scope of work — what the build is allowed to operate on and its authorisation within that. For file-based targets this is expressed as a **working target**: the folder or subtree where the agent may create and modify, with the structural root above it carrying context (the documentation root, underscore folders, binders; or the solution root, project structure).

Work scope is not mandatory on every build — its presence depends on the context and the target. But it is common enough to warrant its own recognised structure, available as a convention that makes it easy for both sides. Branching and git instructions belong in this structure where relevant.

### Mid-execution communication

The build mechanism is not strictly one-shot. Real build execution may require communication between build and caller while the build is running — not just a terminal return at the end.

#### Intermediate exchanges

An intermediate exchange is a pause-and-resume within the build act: build pushes a question, a decision point, or information back to its caller, gets a response, and continues without terminating the build. This is distinct from the terminal return — the five return states remain completion states where build has stopped.

In interactive sessions (direct chat, same-session work), intermediate exchanges are just conversation — the AI asks, the human answers, work continues. In orchestrated or unattended sessions, the channel must support relaying the exchange, because the build executor has no UI — the caller provides the interaction surface.

In chained builds — build calling build — an intermediate exchange from the innermost build relays through each caller until it reaches a layer that can answer. Each layer in the chain relays; the model supports this without assuming chain depth.

The build package indicates whether the caller supports intermediate exchanges. Fire-and-forget builds cannot have them; some channels or callers may not support them. Where intermediate exchanges are not supported, build must either proceed within its granted decision scope or return terminally.

**Dependency on Orchestration:** intermediate exchanges are a real requirement on Orchestration's transport. Orchestration's design explicitly deferred stateful/multi-turn orchestration and a semantic intermediate-progress protocol. Build names the need here; Orchestration's design decides when and how to meet it.

#### Cancellation

The caller may send a **cancel request** to a running build — not just answers to intermediate exchanges. Cancellation is a caller-initiated instruction to stop work.

How a build handles cancellation depends on the transaction model in effect. A cancelled build that has already made changes must respond according to its transaction commitments — rolling back, committing what is complete, or leaving a partial state — and returns a terminal state (failed or done with deviation) with an account of what was done and what was not.

### Transaction model

Build work may succeed in full, fail entirely, or land somewhere in between. The transaction model governs what happens to work already done when a build fails, is cancelled, or encounters an issue partway through.

Three concerns:

- **Commit** — at what granularity does work become permanent? All at once when the build completes, or incrementally as each unit is done?
- **Rollback** — if the build fails or is cancelled, is completed work reversed? For code targets this may mean `git reset`; for documentation it may mean restoring files; for some work rollback is not possible.
- **Partial completion** — does work succeed in part or only in full? Can a build return "done with deviation" carrying partial results the caller can accept?

**Who decides:** the transaction model is declared by the **caller** (in the build package) or by the **build standards** (in the profile), or both — the caller's declaration overrides the profile's default where they conflict. This is a property of the handoff, not a fixed rule, because different targets and different tasks genuinely need different models: a code refactoring may need atomic all-or-nothing, while a documentation batch update may accept partial commits.

Where neither the caller nor the profile declares a transaction model, the default is **commit on completion** — work becomes permanent when the build returns confirmed, and a failed or cancelled build leaves no permanent changes. This is the safe default; override must be explicit.

---

## Build's behavioural obligations

These are obligations placed on Build by the framework — primarily carried from Project Design's commitment-and-return loop. They are Build's side of the contract.

### The escalation boundary

Build owns the *how*; the caller owns the *what and why*. The test is one question: does what build encountered change what is being delivered or why, or only how it gets delivered? How is build's call. What or why comes back to the caller.

**Build must be able to recognise it is holding a what/why question rather than a how question.** This is a carried obligation from Project Design — the escalation boundary only works if build can tell the difference.

**Tiebreak:** if build cannot tell which side it is on, it returns. An unnecessary return costs a message; silently absorbing a caller-side change costs the design's authority. The default is deliberately asymmetric.

### The cost-and-complexity flag

When the real cost or complexity materially exceeds what the caller's specification appeared to assume, build surfaces it before proceeding: *this is looking more extensive and complicated than it probably seemed from the design side — do you want to review, or are you happy to proceed?*

An obligation, not a threshold. No number — build's own judgement of "materially." The flag has a default of proceed: if the caller does not intervene, build continues. The loop keeps moving.

What is being protected is the value-versus-cost judgement, and that judgement is the caller's, because only the caller holds the why.

### Learnings routing

A learning about the caller's specification — about the design, its assumptions, or the domain — passes back to the caller. A learning about build technique — how to implement better, tooling improvements, execution patterns — stays in build.

This is a check, not new machinery: build's own learnings route correctly under the existing decisions and knowledge model. A learning about the design is a what/why question and follows the escalation boundary; a learning about technique is a how and stays.

### Design must not overreach into build

Even when design and build share a session, the transition point exists to stop the caller running, controlling or managing the build act. The caller specifies what; build owns how the code is structured, how discovery proceeds, and how execution is planned. This is the design-check skill's "design produces the specification; build creates from it and owns how the code is structured" stated as Build's own boundary.

---

## Build standards and profiles

### Build standards

The standing conventions for a build channel — instructions, guidance, methodology, rules, conventions, resources and considerations specific to a kind of build work. Build standards are composable: for a web-based .NET project, the .NET development build standard applies, then the web-based build standard layers over it. Each carries only the conventions specific to its scope; the build mechanism underneath carries the common obligations.

#### Authoring

Build standards are authored on the same Standards methodology as ordinary standards:

- Same schema, same document structure, same delivery mechanism (loaded into AI context as skills).
- Same eight authoring rules apply: carry test, no-consumer-no-rule, leanness, discriminating guidance, strength assignment, self-containment, applicability scope, name-your-principles.
- Same strength model: default-Required, with explicit override to Recommended, Optional, or Information.
- Subgrouped as **build standards** for delineation from ordinary standards — the term signals these carry build instruction, guidance and convention for a channel.

The governing test for what goes into a build standard is the same as for any standard: "is this needed at the moment of application?" — not "is this the definition of the thing." Discriminating guidance — the tell that separates correct build practice from its confusable neighbour — belongs in the standard even when it reads like elaboration.

#### Applicability

A build standard's applicability scope declares when it applies — which build channels, which target types, which contexts. The platform trigger mechanism activates it when the profile includes it; scope determines whether it applies to the work at hand once loaded. A build standard whose scope does not match should not run. Same pattern as ordinary standards and tools.

### Profiles

A **profile** is a structural container: it names and orders a set of build standards into a stack, and that is all it does. The substance lives in the build standards; the profile describes which ones apply and how they compose.

Profiles can be **named presets** — defined and saved for reuse ("documentation update", ".NET web project", "AIDE framework documentation update") — or **defined inline** on a specific build. The two combine: apply this named preset, and also these additional standards for this task.

Profiles compose on each other. An "AIDE framework documentation update" profile inherits the base "documentation update" profile and adds AIDE-specific conventions over the top. The delta stays small — only where AIDE genuinely differs from any documentation update.

---

## Build's contribution to assurance

Assurance sets goals, approaches, objectives and requirements/expectations for integrity across the framework. It operates on a spectrum: for some areas it provides methodology and guidance; for others, guidance and expectations alone. Build identifies where each integrity objective can be applied in Build's context and how it is applied there.

Assurance also owns shared assurance components — the framework tasks queue (name pending) and learning patterns — which Build consumes where relevant.

### Lifecycle weighting

At the overview and approach level, proactive conventions carry the most weight. At build, **detective conventions carry more weight** — the specification exists and the question is whether build honours it. This is Assurance's design decision on lifecycle weighting, consumed here.

### Verification behaviours Build implements

Build implements the following Assurance conventions by behaviour inside the build act:

**Conformance checking.** The build confirms that delivered work satisfies its governing specification — the definition of done, the instruction, the design it was handed. A build can contain only verified facts, show no drift during production, and still fail to satisfy the specification. This is the basic assurance closure loop: intended outcome compared against delivered outcome.

**Verification of inspectable facts.** Where a build result depends on records, environment state, or test output, the build verifies rather than asserts. Where it cannot verify, it identifies the uncertainty.

**Assumptions and gap-fill disclosure.** When the build fills a gap — infers intent, supplies a default, or completes something the specification left unstated — it discloses what it filled in and distinguishes it from what was specified. The purpose is to make the boundary between the caller's intent and the build's interpretation visible. Inline, proportional to significance.

**Confidence signalling.** Where build's degree of certainty about an outcome is relevant to the caller's decision — a material judgement, a contested interpretation — it signals confidence using the plain-English vocabulary (high/moderate/low/unknown). Signals are given when they matter, not on every assertion.

### Active identification

Build has a standing obligation to identify and recommend opportunities where assurance could be strengthened within its own domain — gaps in verification coverage, emerging failure patterns, or situations where no convention exists yet. Recommendations surface through capture-and-place in the build return or inline during work.

---

## Known build activities

These are the currently identified kinds of work Build covers. They are not fixed paths — each is the build mechanism applied to a target, with build standards carrying the target-specific conventions.

### 1. Software development

Applying confirmed design to .NET projects and solutions. The proven path with the most established methodology: work packages built from the register, dispatched to Claude Code, agent owns file discovery and edit planning, reviews run including external AI where needed, results recorded, outcome returned.

Scope expands to other software and development platforms later; .NET is the current focus. The legacy flow is a strong simplification and was shaped early in AI-development experience — it wants reshaping against current knowledge, not lifting as-is.

The .NET build standard (not yet authored) will carry: coding standards and practices, review requirements, test expectations, git conventions, and the specific verification behaviours appropriate to code targets.

### 2. Document persistence

Creating and modifying files in a documentation working target. The most frequent build activity currently performed — work happens in chat, Cowork, Code or wherever is chosen, and when it needs to be persisted, files in the documentation root need updating.

Currently done via FUP (File Update Package) from chat — a zip with files at their correct paths plus a deploy manifest, deployed by the `aide fup` tool. FUP is Build scope. The instruction can be prescriptive (make this specific line change) or instructive (modify to implement this change). Normally involves caller check and verification before commit.

The documentation-update build standard (not yet authored) will carry: conventions for writing into a documentation root, schema validity expectations, binder rebuild triggers, version cleanup, output-separation convention, and the working-target conventions for documentation targets.

### 3. Framework payload outputs

Building standards and tools into their endpoint form — skills — and into packages for deployment via the marketplace plugin channel. A design covering an area of feature or functionality may translate into one or more standards or one or more tools; the relationship is one-to-many.

### 4. Framework utility outputs

Building utilities (binder builder, FUP deployer, cleanup, MCP servers) into their endpoint form. Infrastructure owns the delivery mechanism; Build produces the outputs.

---

## Doctypes and block types

Build does not define new doctypes or block types. The build package and the build return are **mechanisms**, not fixed document types — following Project Design's settled decision to withdraw the work-package doctype in favour of a format-free transition point whose shape varies with context.

Build consumes the **definition of done** generic block (owned by Working Practices, testable-or-assessable invariant). Build fills its content within the build package and reports against it in the return.

The build standard is a standard authored under the Standards methodology. The profile is a structural container; it does not require its own doctype.

---

## Terminology

| Term | Meaning |
|---|---|
| **Caller** | Whatever initiated the build — design, another build, or any other origin. Owns the instruction, decision scope and sign-off authority. |
| **Build package** | The outbound handoff: composes instruction, decision scope, working target, profile reference and definition of done. Channel-agnostic — defines what crosses, not how. |
| **Build mechanism** | The generic framework: caller, build package, sign-off, return. Applies to every build. |
| **Build standard** | A composable document carrying the how for a build channel. Authored on the Standards methodology, subgrouped as "build standards." |
| **Profile** | A structural container naming an ordered stack of build standards. Can be a named preset or defined inline. |
| **Working target** | The folder, subtree or scope the build is authorised to operate on. |
| **Documentation root** | The contained root of documentation for a project or area — a folder, not a repo. Replaces "doc repo." |
| **Instruction** | The caller's per-task ask — prescriptive to intent-level. |
| **Decision scope** | The caller-granted latitude and authority for the build to make its own calls. |

---

## Boundaries and edges

- **Project Design** — owns the design specification, the work register, and reconciliation when it is the caller. Build takes what design hands off and returns the outcome; it does not write to the register. Build never closes a register item.
- **Orchestration** — owns transport and dispatch to AI platforms. The most common channel for build work that dispatches to another platform, and the default where a build targets an AI agent — but one channel among several. Direct chat, copy-paste messages, and Messaging's envelope are equally valid depending on context. Build defines a channel-agnostic contract; Orchestration carries it as opaque payload when dispatch is the delivery method.
- **Assurance** — sets goals, approaches, objectives and requirements/expectations for integrity. Provides methodology and guidance for some areas, guidance and expectations for others. Build identifies where integrity objectives apply in its context and implements them by behaviour. Assurance also owns shared assurance components (framework tasks queue, learning patterns) that Build consumes.
- **Infrastructure** — owns the deployment channel (marketplace plugin delivery model), the aide CLI, and operational tooling. Build produces outputs; Infrastructure delivers them.
- **Working Practices** — owns the definition-of-done generic block, work items, capture-and-place, and the overview-first discipline. Build consumes all of these.
- **Documentation folder structure** — a cross-cutting concern consumed by Build, not owned by it. Leaning toward design project as the home; possibly more global. Build needs to locate the structural root and working target within it.

---

## Open items

1. **FUP absorption timing** — FUP is Build scope. Whether Build replaces FUP with a direct file-instruction approach or continues using FUP as a working mechanism is a sequencing decision, not a design question.
2. **Profile storage** — where do named profile presets live? Configuration file, AIDE folder, documentation root, or elsewhere? Needs a decision from the director.
3. **Build standard content** — the .NET build standard and the documentation-update build standard are identified but not authored. Their content is Dave's conventions to specify; the authoring methodology is settled.
4. **Autonomy tiering default for build** — Assurance defines three tiers (directed, trusted, autonomous). What tier does build normally operate at, and does it vary by profile? Needs a decision from the director.
5. **Assurance carry note** — consider whether verification and validation should be its own area within Assurance, with stated expectations on components. Raised from this session.
6. **Documentation folder structure ownership** — cross-cutting concern; leaning to design project, possibly global. Not Build's to resolve.
7. **Work-scope structure** — the recognised structure for declaring work scope, branching and git instructions. Deferred from the voice session; a recommendation will be made.

---

Version note: v2 — expanded from the overview-level v1 to detail design. Added: build package specification (contents, sufficiency, channel-agnostic), mid-execution communication (intermediate exchanges, caller cancellation, transaction model), behavioural obligations (escalation boundary, cost-and-complexity flag, learnings routing, design-must-not-overreach), build standards authoring rules, Assurance verification behaviours Build implements (conformance checking, verification of inspectable facts, assumptions disclosure, confidence signalling, active identification), doctypes-and-block-types determination, return specification (states, sufficiency, failure attribution), and Working Practices boundary. PD carries placed. 2026-09-16.
