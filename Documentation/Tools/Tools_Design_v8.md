> identity: Tools_Design@v8 | doctype: design | updated: 2026-09-24

## Brief

**Purpose.** Define what a tool is and how one is designed, authored, built, and deployed within AIDE. Tools is a methodological component — it owns the methodology for building tools, not the tools themselves. Each tool is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The tool definition and the boundaries that distinguish a tool from a standard and a utility; the invocability test; the authoring concerns, execution discipline, and declared properties a tool must address; the staging clause and the sibling-outputs model; applicability scope and trigger description; the designing and authoring rules; and the build domain (skill packaging and deployment). Individual tools, document structure, and the cross-review process are out of scope.

**Target outcome.** A deployed Tools Development Standard that any component author uses when designing, authoring, building, and deploying a tool.

**Definition of done.**

1. A developer can tell whether something should be a tool — the invocability test, the staging clause, the sibling-outputs model, and the boundary with services and utilities.
2. A developer can design a tool — when a design is required and how tool design relates to the normal AIDE design approach.
3. A developer can author a conforming tool — the authoring concerns, the ask/infer/escalate discipline, declared idempotency, trigger and applicability scope, and how the capability-wide authoring rules apply, with each requirement, recommendation and piece of guidance clearly marked.
4. A developer can review a tool — the acceptance test for a tool and the cross-review requirement.
5. A developer can build a tool — the skill file, plugin placement, and build preconditions.
6. A developer can deploy a tool — the deployment path.
7. The consumer can invoke a deployed tool without separate consumption guidance.
8. The Tools Development Standard can be produced entirely from this design, together with its declared dependencies.

**Linked build outcome.** Tools Development Standard, deployed as a skill in the `aide-dev` plugin.

## What a tool is and does

A tool encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content loaded into project context. In both cases, the tool is what the session consumes. The AI performs the procedure the tool defines.

A tool is a capability. Capabilities are defined platform-neutral — the what — and transformed into platform-specific delivery. A tool loads into the AI session; the AI is the executor. This is what distinguishes a tool from the out-of-session capability types — services and utilities — where a separate process does the work. The execution-context property in the Capabilities Development Standard draws that boundary; the invocability test below draws the tool-versus-standard boundary.

A tool earns its context cost. Everything in it displaces something else the session could hold.

## The invocability test

The boundary between a tool and a standard is invocability. If you would say "run X," X is a tool. If you would say "follow the approach in Y," Y is a standard.

A standard shapes decisions and behaviour while work is being done — it is guidance you consult. A tool is a named thing you invoke to get a specific thing done — it is an action you run. A standard may describe a procedure, but it may not define an invokable action.

The reasoning: a named invokable thing must be a tool because only a tool carries the identity, structure, and authoring discipline that keeps a named action honest. A standard that restates an invokable action creates two authorities on the same thing, with no way to keep them in sync.

This test is the heart of the Tools component. It governs what is a tool and what is not.

## The staging clause

A standard may legitimately describe a procedure that ought to be a tool but is not yet built. That is a staging post, not a defect. The standard carries the procedure so the work can be done now; the intent is that a tool will replace it.

When the tool is built, the standard's procedure section is replaced by a pointer to the tool, so the tool becomes the single source. The standard no longer carries the procedure — it references the tool that does.

This is the only case where a standard may describe an invokable procedure without violating the invocability test. The staging is temporary, and the direction of travel is always toward the tool.

## The sibling-outputs model

A single design can produce standards, tools, and services as sibling outputs. The design describes the behaviour; each output delivers the part of that behaviour appropriate to its type — guidance into a standard, invokable actions into tools, out-of-session operations that sessions call into services. All derive from the same design and must not disagree. If they do, the design is the authority and the inconsistent output is defective. Neither authors the other's content.

This is common. A component or feature may need a standard to shape how the work is approached and a tool to perform a specific action within it. The design specifies the full behaviour; the outputs are whatever delivers it — one or more standards, one or more tools, or a mix. Each output is authored from the design, not from its sibling.

## What Tools owns

### The tool definition

What a tool is, what it does, and what distinguishes it from a standard and a utility. The definitions are stated above. Tools owns these definitions and the invocability test that draws the boundary.

### The authoring concerns

Seven concerns a tool author must address. These are not a template — the author decides how to meet them, in whatever structure the content demands. They describe what a complete tool covers, so an author knows what to think about.

**Inputs.** What the tool needs in order to run. Without this, every invocation re-derives what to provide.

**Preconditions.** What must be true before invoking the tool. Running a tool when conditions are not met wastes effort or causes damage.

**Procedure.** The encapsulated mechanism — the sequence of steps the AI performs when the tool is invoked. This is the tool.

**Decision points.** Where judgement is needed during execution. Where the executor needs to think rather than follow. Essential for tools where the AI must choose between paths or assess a situation mid-procedure.

**Escalation conditions.** When to stop and hand back. The boundary between the tool and its invoker — "this is no longer yours, return to the caller." Different from a decision point: a decision point chooses between paths within the tool; an escalation condition exits the tool.

**Outputs and effects.** What the tool produces and what it changes. The invoker needs to know both — what they get back and what is different afterwards.

**Failure behaviour.** What happens when something goes wrong. How the tool reports failure, what state it leaves behind, and what the invoker should do next.

### The ask/infer/escalate discipline

The behavioural discipline for how a tool handles inputs, decision points, and escalation during execution:

- Infer and state where confidence is strong and cost of error is low.
- Ask once, preferably batched, for genuinely missing required inputs.
- Escalate genuine conflicts, authority decisions, or material uncertainty the tool does not own.

A tool must not silently fail for want of information that could reasonably have been requested. That is not a behavioural preference — it is a defect in the tool.

### Idempotency as a declared property

Whether a tool is safe to run again is a property the author declares about the tool, not a section within it. "This tool is idempotent" or "this tool is not safe to run twice" — the invoker needs to know before deciding whether to re-run.

## Designing and authoring a tool

**Design is the default.** A design almost always exists behind a tool. Authoring straight to a tool is the exception — reserved for cases where the action is simple enough that a design would restate rather than elaborate.

**Author fresh.** A tool is authored from its design, not by modifying a previous version of the tool. This is a capability-wide principle from the design layering model — each output is derived from the design that governs it, not from its own prior version.

**No prescribed template.** A tool has no fixed structure. The author decides what the tool contains and how it is structured, provided it addresses the authoring concerns and meets the authoring rules defined in the Standards Development Standard. These rules apply to any capability, not only to standards.

## Applicability of the development standard

The Tools Development Standard applies when designing, authoring, reviewing, building, or deploying an AIDE tool. It does not govern services, utilities, or the infrastructure mechanisms that package and deploy capabilities.

## How the capability-wide rules apply to tools

The authoring rules in the Standards Development Standard are not Standards-specific — they are properties of any capability that loads into a session and costs context space. A tool that fails the carry test wastes context; one that is not self-contained needs its design loaded alongside it; one with steps nobody performs is governance without effect. The rules apply to tools through the Tools Development Standard, which incorporates them explicitly rather than asserting that the Standards Development Standard's own applicability is wider than it declares.

The rules and the acceptance test are incorporated by reference, not restated, and referenced generically rather than as a closed list — so additions to the rules reach tools without a Tools change. Where the rules use standard-specific nouns, the equivalent tool concept applies: a rule or item includes an operational step or obligation carried by the tool.

**Acceptance test for a tool.** Given only the tool, its declared dependencies, and the ambient framework context guaranteed to be present for the representative operation, can a fresh AI perform the representative operations the tool covers? If it cannot, the tool fails the self-containment rule and must not be published.

**Trigger description.** Every tool carries a trigger description. The trigger-description and segmentation rules in the Standards Development Standard apply identically — the 200-character budget, front-loading of trigger words, and segmentation along dependency lines are platform constraints, not standard-specific ones. A tool deployed as a skill faces the same budget on the same platforms.

**Applicability scope.** Every tool declares the conditions under which it applies, framed through behaviour and relevance rather than deployment target. Trigger and scope are distinct: the trigger description declares when the tool is relevant and is used by whatever mechanism selects it — the platform for a skill, binder configuration for binder content. Scope determines whether the tool applies to the work at hand, evaluated once the tool is available in the session regardless of how it arrived. A tool whose scope does not match is not run — the same risk as for standards, of an available capability running when it should not.

**Document-default strength.** A tool may declare a document-level default strength so the author marks only items that differ from it; nearest declaration wins. This reduces clutter in longer tools without changing the obligation that every item carries an effective strength.

## The design approach for tools

Tool design follows the normal AIDE design approach, a framework-level capability owned by Project Design and delivered as ambient session context through the design-check skill. It is not declared in `uses` because the reference delegates rather than pins — if PD's approach changes, "follows the normal design approach" remains correct. What Tools adds on top is the tool-specific overlay: the invocability test, the authoring concerns, and the build and deployment detail.

## Reviewing a tool

A tool is reviewed the same way as a standard, using the review defined in the Standards Development Standard: the acceptance test for a tool (above), and cross-review by a separate AI directed to find defects, with findings triaged, remediated, and recorded in the decisions. Nothing about review is tool-specific beyond the form of the acceptance test.

## Consumption

A well-authored tool is self-evident to invoke: the trigger description tells the consumer when to use it, the inputs tell them what to provide, and the procedure tells them what will happen. No separate consumption standard is needed for tools. The Standards Consumption Standard exists because standards stack silently and need conflict resolution and human override; tools are explicitly invoked, so those scenarios do not arise. If they do, a tools consumption standard earns its place on the same evidence basis.

## Building a tool

Tools' build domain follows the same model as Standards — the accepted tool document is the build specification, and the build target is a skill file placed in the appropriate marketplace plugin. The skill file format, plugin placement, and deployment path are the same as for standards. A tool and a standard produced as sibling outputs from the same design are built as separate skills, each with its own trigger description.

The linked build outcome on the brief of the design that produces the tool states the deployment target — which plugin the skill is built for. The skill `name` follows the same specification rules as for standards. The practical build detail is recorded in the Tools Development Standard; the reasoning is here.

The boundary between what Tools owns and what Infrastructure owns is the same as for Standards: Tools owns the build domain knowledge (what a tool skill looks like, what the build preconditions are), Infrastructure owns the packaging mechanism and delivery pipeline.

**Platform support.** The same as for standards: Claude — Chat, Code, and Cowork — is supported, and both registration paths are needed for coverage of all three Claude surfaces. ChatGPT and Codex are pending; for ChatGPT, the route is the curated standards binders held as a future consideration (Standards D22). No adapters for other platforms are built.

## Boundaries

Tools does **not** own:

- **The authoring rules** — the authoring rules defined in the Standards Development Standard are capability-wide rules that bind all capability authoring. Tools consumes them.
- **The three-layer authoring model** — a project-level convention consumed by all components, not a Tools mechanism.
- **The cross-review process** — the obligation that every capability is reviewed by a separate AI before acceptance is a collaboration convention owned by Working Practices. Tools' output goes through it.
- **Document structure and block grammar** — Documentation Methodology owns how documents are composed.
- **Packaging and delivery** — how a tool becomes a skill or binder entry is owned by Infrastructure (the packaging mechanism and delivery pipeline). Tools owns the build domain knowledge. The weight gate is a deployment concern.
- **Any individual tool** — each lives with its owning component.

## Carries to other components

**To Standards:** an information-strength pointer in the Standards Development Standard noting that the invocability test in the Tools Development Standard draws the boundary between the two capability types.

---

Version note: v7 — brief updated (purpose, scope, target outcome, definition of done) for the development standard model. Added: applicability of the development standard, how the capability-wide rules apply to tools (incorporation, noun substitution, acceptance test, trigger, scope, document-default strength), the design approach for tools, reviewing a tool, consumption, and the build section. Sibling outputs extended to services; boundary with services and utilities stated. The development standard can now be produced from this design with its declared dependencies. 2026-09-23. Replaces v6.

Version note: v8 — second cross-review remediation. Linked build outcome added to the brief; build preconditions name the brief of the producing design (F8). Applicability adds reviewing (F4). Sibling outputs: services described as out-of-session operations that sessions call, not persistent operations (F11). Inherited trigger budget now 200 characters, and skill `name` rules follow the standards build (F12, Standards D27). Platform-support statement added (F13). 2026-09-24. Replaces v7.
