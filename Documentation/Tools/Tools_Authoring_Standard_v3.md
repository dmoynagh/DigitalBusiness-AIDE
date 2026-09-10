Tools — Standard | standard | Tools_Authoring_Standard@v3 | 2026-09-11

## What a tool is

Information. A tool encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content in project context. The AI performs the procedure the tool defines.

Information. Capabilities are defined platform-neutral and transformed into platform-specific delivery. A tool loads into the AI session; the AI is the executor. A utility, by contrast, runs outside the session and acts on the corpus or infrastructure directly. The invocability test below draws the tool-versus-standard boundary; this platform distinction draws the tool-versus-utility boundary.

Information. A tool earns its context cost. Everything in it displaces something else the session could hold.

## The invocability test

Required. The boundary between a tool and a standard is invocability. If you would say "run X," X is a tool. If you would say "follow the approach in Y," Y is a standard.

Required. A standard may describe a procedure, but it may not define an invokable action. A named invokable thing must be a tool — only a tool carries the authoring discipline that keeps a named action honest. A standard that restates an invokable action creates two authorities on the same thing with no way to keep them in sync.

Information. The standards authoring standard owns the complementary view of this boundary — what a standard is and does. This test owns the tool side.

## Authoring rules

Required. The five authoring rules in the standards authoring standard — the carry test, leanness, discriminating guidance, strength assignment, and self-containment — apply to all capabilities. A tool that fails the carry test wastes context. A tool that is not self-contained requires its design to be loaded alongside it. The rules are not restated here; they are consumed as capability-wide methodology.

## Authoring concerns

Required. Seven concerns a tool author must address. These are not a template — the author decides how to meet them, in whatever structure the content demands.

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

Required. A tool must not silently fail for want of information that could reasonably have been requested.

## Idempotency

Required. The author declares whether the tool is safe to run again, stated alongside its purpose. "This tool is idempotent" or "this tool is not safe to run twice" — the invoker needs this before deciding whether to re-run.

## The staging clause

Information. A standard may legitimately describe a procedure that ought to be a tool but is not yet built. That is a staging post, not a defect. When the tool is built, the standard's procedure section is replaced by a pointer to the tool, so the tool becomes the single source.

Information. This is the only case where a standard may describe an invokable procedure without violating the invocability test. The staging is temporary, and the direction of travel is always toward the tool.

## The sibling-outputs model

Information. A single design can produce both standards and tools as sibling outputs. The design describes the behaviour; the standard carries the guidance; the tool carries the invokable action. Both derive from the design, not from each other, so they cannot disagree. Neither authors the other's content.

Information. This is common. A component or feature specified in a design often needs guidance on how the work is approached and a specific invokable action within that work. The design is the single source; the outputs are its delivery — one or more standards, one or more tools, or a mix.

## Trigger description

Required. Every tool carries a trigger description. The trigger description and segmentation rules are capability-wide: the 130-character budget, front-loading of trigger words, segmentation along dependency lines, and self-containment of each sub-unit all apply to tools identically. These rules are defined in the standards authoring standard.

## Applicability scope

Required. Every tool declares the conditions under which it applies — framed through behaviour and relevance, not deployment target. Trigger and scope are distinct: the trigger gets the tool loaded into the session; the scope determines whether it applies to the work at hand. A loaded tool whose scope does not match is not run.

## Document-default strength

Information. A tool may declare a document-level default strength so the author only marks items that differ from the default. Nearest declaration wins. This reduces clutter in longer tools without changing the obligation that every item carries an effective strength.

## Designing a tool

**Design is the default.** Recommended. A design almost always exists behind a tool. Authoring straight to a tool is the exception — reserved for cases where the action is simple enough that a design would restate rather than elaborate.

**Author fresh.** Required. A tool is authored from its design, not by modifying a previous version of the tool. This is a capability-wide principle — each output is derived from the design that governs it, not from its own prior version.

**No prescribed template.** Information. A tool has no fixed structure. The author decides what it contains and how it is organised, provided the authoring concerns above are addressed and the capability-wide authoring rules are met.

## Deployment

Information. Once a tool is authored and accepted, it is deployed as a capability — packaged by Infrastructure and delivered through the deployment pipeline. The author's responsibility ends at a complete, accepted tool. Packaging into a skill or binder entry, and the weight gate that checks the combined load, are owned by Infrastructure and Deployment respectively.

## Ownership

**Each tool lives with its owning component.** Required. Tools is a methodological component — it defines how to build a tool, not where tools live. Each tool is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v3 — re-authored from Tools_Design_v2 addressing cross-review findings F1–F8: restores tool/utility distinction, corrects idempotency to Required, separates "never fail" as Required from Recommended discipline, aligns deployment terminology, removes trigger placement rule, adds applicability framing authority, 2026-09-11.
