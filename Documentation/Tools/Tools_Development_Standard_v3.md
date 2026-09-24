> identity: Tools_Development_Standard@v3 | doctype: standard | updated: 2026-09-24 | uses: Capabilities_Development_Standard@v2, Standards_Development_Standard@v3

# Tools — Development Standard

How to design, author, review, build, and deploy an AIDE tool.

## What a tool is

Information. A tool encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content in project context. The AI performs the procedure the tool defines.

Information. Capabilities are defined platform-neutral and transformed into platform-specific delivery. A tool loads into the AI session; the AI is the executor. Services and utilities, by contrast, run as separate processes outside the session. The invocability test below draws the tool-versus-standard boundary; the execution-context property in the Capabilities Development Standard draws the in-session versus out-of-session boundary.

Information. A tool earns its context cost. Everything in it displaces something else the session could hold.

## Applicability

Information. This standard applies when designing, authoring, reviewing, building, or deploying an AIDE tool. It does not govern services, utilities, or the infrastructure mechanisms that package and deploy capabilities.

## The invocability test

The boundary between a tool and a standard is invocability. If you would say "run X," X is a tool. If you would say "follow the approach in Y," Y is a standard.

A standard may describe a procedure, but it may not define an invokable action. A named invokable thing must be a tool — only a tool carries the authoring discipline that keeps a named action honest. A standard that restates an invokable action creates two authorities on the same thing with no way to keep them in sync.

Information. The Standards Development Standard owns the complementary view of this boundary — what a standard is and does. This test owns the tool side.

## Authoring rules and acceptance test

The capability-wide authoring rules and the acceptance test defined in the Standards Development Standard apply to tools through this standard. Where those rules use standard-specific nouns, apply the equivalent tool concept — a rule or item includes an operational step or obligation carried by the tool.

The acceptance test for a tool: given only the tool, its declared dependencies, and the ambient framework context guaranteed to be present for the representative operation, can a fresh AI perform the representative operations the tool covers? If it cannot, the tool fails the self-containment rule and must not be published.

## Authoring concerns

Seven concerns a tool author must address. These are not a template — the author decides how to meet them, in whatever structure the content demands.

**Inputs.** What the tool needs in order to run.

**Preconditions.** What must be true before invoking the tool.

**Procedure.** The sequence of steps the AI performs when the tool is invoked. This is the tool.

**Decision points.** Where judgement is needed during execution — where the executor must choose between paths or assess a situation rather than follow a fixed sequence.

**Escalation conditions.** When to stop and hand back to the invoker. Different from a decision point: a decision point chooses between paths within the tool; an escalation condition exits the tool.

**Outputs and effects.** What the tool produces and what it changes. The invoker needs both — what they get back and what is different afterwards.

**Failure behaviour.** What happens when something goes wrong — how the tool reports failure, what state it leaves behind, and what the invoker should do next.

Recommended. Not every concern will be substantial for every tool. A simple tool might have no meaningful escalation conditions; a complex one might need something this list does not name. The concerns are what to think about, not what to fill in.

## Ask, infer, escalate

Recommended. The behavioural discipline for handling inputs, decision points, and escalation during execution:

- Infer and state where confidence is strong and cost of error is low.
- Ask once, preferably batched, for genuinely missing required inputs.
- Escalate genuine conflicts, authority decisions, or material uncertainty the tool does not own.

A tool must not silently fail for want of information that could reasonably have been requested.

## Idempotency

The author declares whether the tool is safe to run again, stated alongside its purpose. "This tool is idempotent" or "this tool is not safe to run twice" — the invoker needs this before deciding whether to re-run.

## The staging clause

Information. A standard may legitimately describe a procedure that ought to be a tool but is not yet built. That is a staging post, not a defect. When the tool is built, the standard's procedure section is replaced by a pointer to the tool, so the tool becomes the single source.

Information. This is the only case where a standard may describe an invokable procedure without violating the invocability test. The staging is temporary, and the direction of travel is always toward the tool.

## The sibling-outputs model

Information. A single design can produce standards, tools, and services as sibling outputs. The design describes the behaviour; each output delivers the part appropriate to its type — guidance into a standard, invokable actions into tools, out-of-session operations that sessions call into services. All derive from the design, not from each other, and must not disagree. If they do, the design is the authority and the inconsistent output is defective.

## Trigger description

Every tool carries a trigger description. The capability-wide trigger-description and segmentation rules in the Standards Development Standard apply identically to tools, including the 200-character budget, front-loading of trigger words, and segmentation along dependency lines.

## Applicability scope

Every tool declares the conditions under which it applies — framed through behaviour and relevance, not deployment target. Trigger and scope are distinct concerns. The trigger description declares when the tool is relevant and is used by whatever mechanism selects it — the platform for a skill, binder configuration for binder content. Scope determines whether the tool applies to the work at hand, evaluated once the tool is available in the session regardless of how it arrived. A tool whose scope does not match is not run.

## Document-default strength

Information. A tool may declare a document-level default strength so the author only marks items that differ from the default. Nearest declaration wins. This reduces clutter in longer tools without changing the obligation that every item carries an effective strength.

## Designing a tool

**Design is the default.** Recommended. A design almost always exists behind a tool. Authoring straight to a tool is the exception — reserved for cases where the action is simple enough that a design would restate rather than elaborate.

Information. Tool design follows the normal AIDE design approach, which is a framework-level capability owned by Project Design and available as ambient session context. This section provides the tool-specific guidance on top of it — the authoring concerns, the invocability test, and the deployment handoff are the tool-specific overlay.

**Author fresh.** A tool is authored from its design, not by modifying a previous version of the tool. This is a capability-wide principle — each output is derived from the design that governs it, not from its own prior version.

**No prescribed template.** Information. A tool has no fixed structure. The author decides what it contains and how it is organised, provided the authoring concerns above are addressed and the capability-wide authoring rules are met.

## Review

A tool is reviewed before it is accepted, using the review defined in the Standards Development Standard: the acceptance test for a tool (above) and cross-review by a separate AI. Nothing about review is tool-specific beyond the form of the acceptance test.

## Build

A tool is built by packaging it as a skill for plugin delivery. The authored tool document is the build specification.

### Preconditions

Cross-review accepted and acceptance test passed before build starts. These are authoring-phase completions, not build steps.

The linked build outcome on the brief of the design that produces the tool states the deployment target — which plugin the skill is built for.

### Building a skill

The skill file format is the same as for standards — a markdown file with YAML frontmatter:

```
---
name: <skill-name>
description: "<trigger description>"
---

<!-- provenance: <source_tool_identity> | redistributed: <plugin> (<marketplace>), <date> -->

<tool content>
```

The `description` field is the trigger description. The `name` field follows the same Agent Skills specification rules as for standards. The tool content is copied from the accepted tool document, omitting the document header and version note. The provenance comment records the source.

A tool and a standard produced as sibling outputs from the same design are built as separate skills — each with its own trigger description and skill file. They load independently.

### Plugin placement

Tools follow the same plugin placement as standards: `aide` for operational tools, `aide-dev` for development tools. The distinction is the same — does the tool apply during normal work, or during AIDE development?

### Testing a built skill

Before the deploy PR, run the checks in the Standards Development Standard's "Testing a built skill".

## Deployment

The deployment path is the same as for standards: PR to the deploy repo, merge, refresh marketplace clone, restart Desktop. Both web UI and desktop app registration paths are needed for coverage of all three Claude surfaces. See the Standards Development Standard for the full deployment steps, or `Infrastructure_MCPDeliveryModel@v2` for the complete picture.

Information. Platform support: Claude — Chat, Code, and Cowork — is supported. ChatGPT and Codex are pending; for ChatGPT, which does not load plugins, the route is curated standards binders, held as a future consideration. No adapters for other platforms are built.

## Consumption

Information. A well-authored tool is self-evident to invoke: the trigger description tells the consumer when to use it, the inputs tell them what to provide, and the procedure tells them what will happen. Good authoring makes consumption fall out naturally. No separate consumption standard is currently needed for tools — tools are explicitly invoked, not silently applicable, so the conflict and override scenarios that drove the Standards Consumption Standard do not materialise.

## Ownership

**Each tool lives with its owning component.** Tools is a methodological component — it defines how to build a tool, not where tools live. Each tool is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v1 — supersedes Tools_Authoring_Standard@v8. All authoring content embedded unchanged. Review, build, deployment, and consumption sections added. Sibling-outputs model extended to include services. Produced from Tools_Design@v7 with its declared dependencies. 2026-09-23.

Version note: v2 — applicability adds reviewing. Sibling outputs describe services as out-of-session operations that sessions call. Trigger budget 200 characters and skill `name` rules, inherited from the Standards Development Standard. Build precondition names the brief of the producing design. Platform-support statement added. Produced from Tools_Design@v8 with its declared dependencies. 2026-09-24. Replaces v1.

Version note: v3 — testing a built skill: one-line pointer to the checks in the Standards Development Standard. `uses` updated to Standards_Development_Standard@v3. Produced from Tools_Design@v8 with its declared dependencies. 2026-09-24. Replaces v2.
