Tools — Decisions | decisions | Tools_Decisions@v7 | 2026-09-14

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

A single design can produce both standards and tools. The design describes the behaviour; each output delivers the part of that behaviour appropriate to its type — guidance into a standard, invokable actions into tools. Both derive from the design, not from each other, and must not disagree. If they do, the design is the authority and the inconsistent output is defective.

This is expected to be common. A component or feature specified in a design may need guidance on how the work is approached (a standard) and a specific invokable action within that work (a tool). The design is the single source; the outputs are its delivery.

The model also prevents the synchronisation problem the invocability test was designed to avoid. Two sibling outputs from one design are coordinated by the design. Two independent documents covering the same behaviour — one as a standard, one as a tool — would drift.

## D7 — The standards authoring rules apply to tools

The authoring rules in the standards authoring standard are not Standards-specific — they are properties of any capability that loads into a session and costs context space. A tool that fails the carry test wastes context. A tool that is not self-contained requires its design to be loaded alongside it. A tool with rules that have no operational consumer is governance without effect. The rules apply.

Tools does not restate them. The tool authoring standard consumes them by reference to the standards authoring methodology, with a reading rule for standard-specific nouns.

## D8 — Trigger description and segmentation rules are capability-wide

The 130-character trigger budget, front-loading of trigger words, segmentation along dependency lines, and self-containment of each sub-unit were agreed as part of the standards authoring standard v3. They are platform constraints, not standard-specific constraints. A tool deployed as a skill faces the same budget on the same platforms.

Tools applies these rules identically. They are not restated — the tool authoring standard references them as capability-wide rules.

## D9 — One primary output: the tool authoring standard

The tool authoring standard covers design, authoring, and the deployment handoff for tools. It parallels the standards authoring standard in scope and shape.

A separate consumption standard — how to invoke and work with tools once deployed — is not assumed. A well-authored tool is self-evident to invoke: the trigger description tells the consumer when to use it, the inputs tell them what to provide, and the procedure tells them what will happen. Good authoring makes consumption fall out naturally.

The Standards session subsequently found that a consumption standard did earn its place for standards, because conflict resolution and human override are real operational concerns when multiple standards stack silently. The question was raised for tools. The deferral holds: tools are explicitly invoked, not silently applicable, so the conflict and override scenarios that drove the standards consumption standard do not yet materialise for tools. If they do, the consumption standard earns its place on the same evidence basis.

## D10 — Applicability scope is a required authoring rule

Carried from the Standards session finding. Trigger and scope are distinct concerns. The trigger description declares when the tool is relevant — the mechanism that acts on it depends on the delivery form (platform trigger for a skill, binder configuration for binder content). Scope determines whether the tool applies to the work at hand, evaluated once the tool is available in the session regardless of how it arrived. Scope is framed through behaviour and relevance rather than deployment target. A tool whose scope does not match should not run. The same reasoning that made this Required for standards applies to tools — same platform, same delivery model, same risk of an available capability running when it shouldn't.

## D11 — Ask/infer/escalate discipline

Carried from the old Tools Design §3, confirmed during the legacy binder review. The seven authoring concerns tell the author what to address; this discipline tells them how to handle inputs, decision points, and escalation during execution. It passes the carry test — a tool author needs it at the moment of authoring these concerns.

The discipline is framed as Recommended because it is guidance for execution, not a compliance obligation. A tool author who has a good reason to handle inputs differently may do so — the rule is that the behaviour should be deliberate, not that it must follow this exact pattern.

## D12 — Document-default strength simplifies clutter in larger tools

A tool can declare its document-level default strength the same way standards do (nearest-declaration-wins). This avoids tagging every item Required in a long tool. The mechanism is in the standards authoring standard; Tools applies it identically.

## D13 — First cross-review findings (F1–F8)

Carried from the first cross-review round:
- **F1 (utility definition scope):** clarified that the utility boundary definition is a complementary statement, not a full design — utility design belongs to the owning component.
- **F2 (invocability test scope):** confirmed the test draws a clean enough boundary at this scope; edge cases are handled by the staging clause.
- **F3 (authoring concerns not exhaustive):** the Recommended strength on the meta-note about concerns addresses this — the author can add what the list does not name.
- **F4 (failure behaviour vs error handling):** "failure behaviour" is the better term — it covers both what goes wrong and what the tool does about it, without implying a catch/throw mechanism.
- **F5 (escalation vs decision overlap):** the standard already distinguishes them — a decision point chooses between paths within the tool; an escalation condition exits the tool.
- **F6 (sibling-outputs model naming):** confirmed as clear enough. "Sibling outputs from one design" needs no further elaboration.
- **F7 (deployment terminology drifted):** corrected from "skill or plugin" to "skill or binder entry" to match the design.
- **F8 (applicability scope extra constraint):** the "framed through behaviour and relevance" qualifier added to the design and D10 so the standard has authority.

## D14 — Second cross-review findings (F9–F10)

F9: the design Brief's Scope sentence understated what the design actually owned. The v2 additions had expanded the design's content without updating the scope declaration. Fixed by reconciling the scope to describe the full design.

F10: the trigger/scope model incorrectly treated trigger-loading as the universal mechanism ("the trigger gets the tool loaded into the session"). This holds for skills but not for binder content, which is already in project context. The trigger description is reframed as a relevance declaration consumed by whatever selection mechanism applies — platform trigger for skills, binder configuration for binder content. Scope evaluates once the tool is available in the session, regardless of how it arrived. This makes the model true for both delivery forms established in the tool definition.

## D15 — Authoring rules reference updated from five to the full capability-wide set

The v4 standard named five specific authoring rules (carry test, leanness, discriminating guidance, strength assignment, self-containment) and referenced them as a closed list. The Standards Authoring Standard expanded from five to eight authoring rules in v6 (adding no-consumer-no-rule, applicability scope, name-your-principles) and added the acceptance test in v7.

D7's rationale — that these are properties of any capability, not Standards-specific — applies to the full set. The three additions are operationally significant for tool authoring: no-consumer-no-rule catches a tool with steps nobody performs; applicability scope was already independently addressed in D10; name-your-principles catches a tool that repeats reasoning without pulling it up. The acceptance test gives self-containment a concrete verification form.

The fix: the standard references the authoring rules generically rather than naming a closed list, with examples for discriminating guidance rather than an exhaustive enumeration.

## D16 — Fourth cross-review findings (F1–F8, v5 review)

Eight findings from the v5 cross-review. All accepted and remediated in v6.

- **F1 (incorporation conflict):** Tools asserted the rules were capability-wide; Standards declared itself applicable to standard authoring. Fixed by making the incorporation explicit — the rules apply to tools through this standard, not by asserting Standards' applicability is wider than it declares.
- **F2 (acceptance test not incorporated):** The v5 text said "the authoring rules apply" but the acceptance test sits alongside the rules, not within them. Fixed by explicitly naming both the authoring rules and the acceptance test.
- **F3 (no applicability declaration):** Tools v5 imported the applicability-scope rule and then failed it itself. Fixed by adding an applicability section.
- **F4 (design method insufficient):** The design section said design is required but didn't define a method. Fixed by clarifying tool design follows the normal AIDE design approach; this section provides the tool-specific overlay.
- **F5 (scope overclaim on publishing and versioning):** The opening description claimed "published and versioned" but neither is defined. Fixed by narrowing the description and renaming "Deployment" to "Deployment handoff" to match the actual scope.
- **F6 (noun substitution):** The source rules use standard-specific nouns. Fixed by adding a reading rule: where those rules use standard-specific nouns, apply the equivalent tool concept.
- **F7 (trigger partial list):** The trigger section named four specific sub-rules, reproducing the same maintenance risk the authoring-rules fix addressed. Fixed by making it a generic incorporation with "including" for examples.
- **F8 (sibling-outputs guarantee):** "Cannot disagree" overstated the model's guarantee. Fixed to "must not disagree" with the design as authority if they do.

## D17 — Round 2 cross-review findings (F1–F2, v6 review)

Two findings from the v6 cross-review. Both accepted and remediated in v7/v6.

- **F1 (design approach undeclared dependency):** The standard said "tool design follows the normal AIDE design approach" but the approach was neither contained nor declared in `uses`. The reviewer correctly noted the acceptance test fails. Resolution: the general design approach is a framework-level capability owned by Project Design, delivered as ambient session context (via the aide-design-check skill), not a document-to-document dependency. The `uses` field tracks change-management dependencies — if PD's approach changes, Tools' reference to "the normal AIDE design approach" remains correct because it delegates rather than pins. Made explicit in the standard with an Information line naming the owner and delivery mechanism.
- **F2 (Design brief scope not propagated):** The Design's Brief still said "deployed" where the standard, decisions, and detailed design all said "deployment handoff." Fixed by narrowing Purpose and Target outcome.

---

Version note: v7 — D17 added for round 2 cross-review remediation. 2026-09-14. Replaces v6.
