Tools — Decisions | decisions | Tools_Decisions@v1 | 2026-09-11

## D1 — Tools is a methodological component, same pattern as Standards and Infrastructure

Tools defines how to create its type. Individual tool instances live with their consuming component. This was settled in the overview as the common pattern for all three capability-type components and confirmed in the structure session. The alternative — Tools holding all tools — was rejected because it violates the what-knows-most-about-it ownership principle.

## D2 — The invocability test is the governing boundary, owned by Tools

The standard-tool boundary was originally settled as D24 in the old corpus. The test — "if you would say 'run X,' X is a tool; if you would say 'follow the approach in Y,' that is a standard" — survived the rebuild because it is the cleanest available distinction. It says nothing about how the action is carried out, only whether it is invoked or consulted.

Ownership is placed in Tools rather than Standards because the ambiguous cases land here. Someone wondering "is this a standard or a tool?" is almost always holding something that looks invokable, so they are in Tools' territory. The standards side already describes what a standard is clearly enough that the "follow" case is self-evident; it is the "run" case that needs the discriminating guidance.

Standards carries a one-line information-strength pointer to the test rather than restating it. One authority, not two.

## D3 — Seven authoring concerns, not a template

The tool definition listed eight elements a tool "normally" defines. This was an indicative sketch from the terminology-setting session, not a deliberated design. Evaluation against the tool's purpose — encapsulating a repeatable action — produced seven concerns that earn their place, with adjustments:

- **Reporting folded into outputs and effects.** A report is an output. Every existing utility's log and on-screen report is an output of running the tool. Reporting does not need its own category.
- **Failure behaviour and idempotency separated.** The original list combined these into one slot, but they are different concerns. Failure behaviour is what happens when something goes wrong — universal and always relevant. Idempotency is a property of the tool — whether it is safe to run again — better declared alongside the tool's purpose than authored as a procedural section.

The same principle as Standards applies: these are concerns the author must address, not a structure to fill in. A simple tool might have no meaningful escalation conditions; a complex one might need something this list does not name. The author decides how to meet the terms.

## D4 — Tools are AI-performed capabilities

The old WIP carried the qualifier "NOT limited to executable code — migration is a tool and it's an AI task." This was dropped because it introduced confusion by blurring the line between tools and utilities. A tool is a capability; capabilities load into the AI session; the AI performs the procedure. That is the definition, and it does not need a qualifier saying what it is not.

The framework already has clean separation: tools load into the session and the AI executes them; utilities run outside the session and act on the corpus or infrastructure. The qualifier was trying to say tools are not just scripts, but it achieved this by muddying a boundary that was already drawn.

Dropping it also simplifies the authoring guidance. There is one execution context — AI in-session — not two to accommodate. The seven authoring concerns work cleanly for AI-performed procedures.

## D5 — The staging clause governs standard-to-tool transition

A standard may describe a procedure that ought to be a tool but is not yet built. This is legitimate staging, not a defect. When the tool is built, the standard's procedure section is replaced by a pointer to the tool, making the tool the single source.

The staging clause exists because building a tool is more work than describing a procedure in a standard, and the work should not be blocked while the tool is being built. The direction of travel is always toward the tool — a staged procedure is a known debt, not a permanent arrangement.

The clause also protects the invocability test from being treated as rigid: a standard carrying a temporary procedure does not violate the test provided the intent is to replace it. The test governs the steady state, not the transition.

## D6 — The sibling-outputs model governs tool-standard coexistence

A single design can produce both standards and tools. The design describes the behaviour; each output delivers the part of that behaviour appropriate to its type — guidance into a standard, invokable actions into tools. Both derive from the design, not from each other, so they cannot disagree.

This is expected to be common. A component or feature specified in a design may need guidance on how the work is approached (a standard) and a specific invokable action within that work (a tool). The design is the single source; the outputs are its delivery.

The model also prevents the synchronisation problem the invocability test was designed to avoid. Two sibling outputs from one design are coordinated by the design. Two independent documents covering the same behaviour — one as a standard, one as a tool — would drift.

## D7 — The standards authoring rules apply to tools

The five authoring rules (carry test, leanness, discriminating guidance, strength assignment, self-containment) are not Standards-specific — they are properties of any capability that loads into a session and costs context space. A tool that fails the carry test wastes context. A tool that is not self-contained requires its design to be loaded alongside it. The rules apply.

Tools does not restate them. The tool authoring standard consumes them by reference to the standards authoring methodology.

## D8 — Trigger description and segmentation rules are capability-wide

The 130-character trigger budget, front-loading of trigger words, segmentation along dependency lines, and self-containment of each sub-unit were agreed as part of the standards authoring standard v3. They are platform constraints, not standard-specific constraints. A tool deployed as a skill faces the same budget on the same platforms.

Tools applies these rules identically. They are not restated — the tool authoring standard references them as capability-wide rules.

## D9 — One primary output: the tool authoring standard

The tool authoring standard covers design, authoring, and deployment of tools. It parallels the standards authoring standard in scope and shape.

A separate consumption standard — how to invoke and work with tools once deployed — is not assumed. A well-authored tool is self-evident to invoke: the trigger description tells the consumer when to use it, the inputs tell them what to provide, and the procedure tells them what will happen. Good authoring makes consumption fall out naturally.

---

Version note: v1 — initial decisions from the tools design session, 2026-09-11.
