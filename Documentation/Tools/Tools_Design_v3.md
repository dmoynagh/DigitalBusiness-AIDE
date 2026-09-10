Tools — Design | design | Tools_Design@v3 | 2026-09-11

## Brief

**Purpose.** Define what a tool is and how one is designed, authored, and deployed within AIDE. Tools is a methodological component — it owns the methodology for building tools, not the tools themselves. Each tool is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The tool definition and the boundaries that distinguish a tool from a standard and a utility; the invocability test; the authoring concerns, execution discipline, and declared properties a tool must address; the staging clause and the sibling-outputs model; applicability scope and trigger description; and the designing and authoring rules. Individual tools, document structure, packaging, and the cross-review process are out of scope.

**Target outcome.** A deployed tool authoring standard that any component author uses when designing, authoring, and deploying a tool for their component.

## What a tool is and does

A tool encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content loaded into project context. In both cases, the tool is what the session consumes. The AI performs the procedure the tool defines.

A tool is a capability. Capabilities are defined platform-neutral — the what — and transformed into platform-specific delivery. A tool loads into the AI session; the AI is the executor. This is what distinguishes a tool from a utility, which runs outside the session and acts on the corpus or infrastructure directly.

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

A single design can produce both standards and tools as sibling outputs. The design describes the behaviour; the standard carries the guidance; the tool carries the invokable action. Both derive from the same design and therefore cannot disagree. Neither authors the other's content.

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

Whether a tool is safe to run again is a property the author declares about the tool, not a section within it. "This tool is idempotent" or "this tool is not safe to run twice" sits naturally alongside the tool's purpose, as a characteristic of the tool rather than a step in its procedure. The declaration is not optional — the invoker needs it before deciding whether to re-run.

### Applicability scope

Every tool declares the conditions under which it applies — framed through behaviour and relevance, not deployment target. Trigger and scope are distinct concerns:

- The **trigger description** declares when the tool is relevant. The mechanism that acts on it depends on the delivery form — the platform uses it to fire loading for a skill; a binder configuration uses it to decide inclusion for binder content. In both cases, the trigger description is a selection input, not a loading mechanism itself.
- **Scope** determines whether the tool applies to the work at hand, evaluated once the tool is available in the session regardless of how it arrived. A tool whose scope does not match is not run.

### The trigger description

Every tool carries a trigger description — the same mechanism and the same rules as for standards. The trigger description and segmentation rules are capability-wide: the 130-character budget, the front-loading of trigger words, segmentation along dependency lines, and self-containment of each sub-unit all apply to tools identically.

### Document-default strength

A tool may declare a document-level default strength so the author only marks items that differ from the default. Nearest declaration wins. This reduces clutter in longer tools without changing the obligation that every item carries an effective strength.

## Designing and authoring a tool

**Design is the default.** A design almost always exists behind a tool. Authoring straight to a tool is the exception — reserved for cases where the action is simple enough that a design would restate rather than elaborate.

**Author fresh.** A tool is authored from its design, not by modifying a previous version of the tool. This is a capability-wide principle from the design layering model — each output is derived from the design that governs it, not from its own prior version.

**No prescribed template.** A tool has no fixed structure. The author decides what the tool contains and how it is structured, provided it addresses the authoring concerns and meets the authoring rules inherited from the standards authoring methodology — the carry test, leanness, discriminating guidance, strength assignment, and self-containment. These rules apply to any capability, not only to standards.

## Boundaries

Tools does **not** own:

- **The standards authoring rules** — the carry test, leanness, discriminating guidance, strength assignment, and self-containment are Standards-wide rules that bind all capability authoring. Tools consumes them.
- **The three-layer authoring model** — a project-level convention consumed by all components, not a Tools mechanism.
- **The cross-review process** — the obligation that every capability is reviewed by a separate AI before acceptance is a collaboration convention owned by Working Practices. Tools' output goes through it.
- **Document structure and block grammar** — Documentation Methodology owns how documents are composed.
- **Packaging and delivery** — how a tool becomes a skill or binder entry is owned by Infrastructure (packaging) and Deployment (the weight gate and the pipeline to the marketplace).
- **Any individual tool** — each lives with its owning component.

## Carries to other components

**To Standards:** an information-strength pointer in the standards authoring standard noting that the invocability test in the tool authoring standard draws the boundary between the two capability types.

---

Version note: v3 — reconciles Brief scope with actual design content (F9), reframes trigger/scope model to be delivery-form-neutral (F10), 2026-09-11.
