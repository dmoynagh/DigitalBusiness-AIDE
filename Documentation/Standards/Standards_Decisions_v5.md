> identity: Standards_Decisions@v5 | doctype: decisions | updated: 2026-09-23

## D1 — Standards is a methodological component, same pattern as Infrastructure and Tools

Standards defines how to create its type. Individual instances live with their consuming component. This was settled in the overview as the common pattern for all three capability-type components and confirmed in the structure session. The alternative — Standards holding all standards — was rejected because it violates the what-knows-most-about-it ownership principle.

## D2 — Eight authoring rules plus one design rule, not a template

The authoring methodology is expressed as eight rules (carry test, no consumer no rule, leanness, discriminating guidance, strength assignment, self-containment, applicability scope, name your principles) rather than a prescribed template or structural specification. The author decides what a standard contains and how it is organised, provided it meets the terms.

A ninth rule — earn your place — operates on the design and solving model rather than on the authored standard, and is therefore a design rule, not an authoring rule. It is recorded in D20.

A template risks becoming apparatus — a structure to fill in rather than a set of outcomes to achieve. The rules tell an author what a good standard must do. Document structure belongs to Documentation Methodology; Standards defines what the content must achieve, not what it must look like.

## D3 — Four strength levels, default-Required, strength per item not per section

The strength model uses four levels: Required, Recommended, Optional, Information. The fourth level (Information) was added specifically for reference-origin content that needs to reach the platform for awareness without carrying a compliance expectation.

The default strength is Required. Items at Required carry no explicit tag — only items that depart from the default are tagged. This keeps the standard lean by eliminating repetitive strength markers from the majority of items. The principle is: tag only the exceptions.

Strength is a property of each item rather than a section organiser because a single standard will naturally mix levels — a section on authoring might contain two required rules, one recommended practice, and one piece of information context. Grouping by strength would break the logical flow of the guidance.

The vocabulary — the four words and their definitions — is standardised. This is the "rule weight markers" technique lifted from the Project Design binder sweep and given its home here, as flagged during that work.

## D4 — The carry test is the single authoring filter

"Is this needed at the moment of application" is the governing test for what goes into a standard. It was stated by Dave as a Standards-wide principle during the Project Design work and is the most important single rule in the authoring methodology.

The test sharpens the three-layer authoring model rather than contradicting it: discriminating guidance belongs in the standard even though it reads like elaboration, because placement and application judgements happen from whatever is memory-resident.

## D5 — Self-containment over cross-referencing

A standard must be understandable without its design document in the session. The alternative — a standard that assumes access to its design — would mean loading both documents to apply the guidance, doubling the context cost and defeating the purpose of the lean standard.

This does not prevent a standard from referencing its design for deeper reasoning. It prevents depending on the design being present.

## D6 — Two outputs: authoring and consumption

The authoring standard covers design, authoring, and deployment. The consumption standard covers conflict resolution, human override, and runtime operation under applicable standards.

The original design assumed a single output with the consumption standard deferred. The legacy binder review identified conflict resolution and human override as real operational concerns that earn their place now. Both are consumption concerns — they tell consumers how to operate under standards, not authors how to build them. This makes the consumption standard a confirmed output rather than a contingency.

The boundary between them is deliberate: the authoring standard's scope stops at deployment; the consumption standard's scope starts at application.

## D7 — Settled decisions binding on Standards but owned elsewhere

Three decisions constrain Standards without being redefined by it:

- **The carry test** was stated as a rebuild-wide governing principle, not by this component. Standards must embody it but does not own the principle.
- **The cross-review requirement** comes from the three-layer authoring model: every authored standard is reviewed by a separate AI before acceptance. The obligation exists because of Standards; the process is a Working Practices collaboration convention.
- **The weight gate at deployment** checks the combined load when capabilities are packaged into a plugin. Standards owns leanness at authoring time; Deployment owns the gate at packaging time.

## D8 — The Contents/Summary edge is Documentation Methodology's concern

The edge between Contents and Summary was flagged during the Project Design work as "a common issue" for standards authors. It is carried to Documentation Methodology because the edge definition is about document-structure blocks — what Contents maps versus what Summary establishes — which is grammar, not authoring methodology. Standards authors will encounter the problem, but the solution belongs to whoever owns the grammar of those blocks.

## D9 — Conflict resolution between standards

When multiple standards apply to the same work, compatible standards stack — they are combined, not chosen between. When two applicable items genuinely oppose each other on the same point, higher strength governs. Equal-strength genuine conflict is surfaced and escalated rather than silently resolved. Conflict is not manufactured from different concerns that can both be satisfied.

This approach was carried from the legacy system's usage standard, where it was proven in practice. It is delivered through the consumption standard, not the authoring standard, because it governs runtime behaviour rather than authoring.

## D10 — Human override of standards

Direct human instruction may override a standard within that person's authority. When it displaces a required or recommended item, the AI states the standard's position and the material consequence of departure, makes the departure visible, and continues under the human's instruction.

This is a three-step behavioural contract, not a mechanism. It aligns with the overview principle that the human is always in control. It is delivered through the consumption standard.

## D11 — Trigger and scope are distinct

Triggering is a delivery concern — getting the standard loaded where it might be needed. Scope is the standard's own concern — declaring the conditions under which it is applicable once loaded. Every standard carries its own scope because what is loaded on any given platform cannot be guaranteed.

Scope targets behaviour and relevance — what needs to be true for the standard to be of value — not a specific deployment target or package. This future-proofs for a scenario where AIDE capabilities are distributed as separate packages: framework development standards and usage standards might be packaged separately, but each standard still declares its own applicability regardless of which package delivered it.

Triggering belongs to Infrastructure; scope belongs to the standard and is defined by its author. Scope is a required authoring rule.

## D12 — Facilitative framing over bare authority

Requirements are framed through the consequence or value of meeting them, not through bare authority. This was a deliberate philosophical position in the legacy system and is absent from bare "do X" rules. It differs from discriminating guidance (which is about helping the consumer apply a rule) — facilitative framing is about helping the consumer understand why the rule matters. Both are necessary: discriminating guidance without facilitative framing produces usable but authoritarian standards; facilitative framing without discriminating guidance produces well-reasoned but unapplicable ones.

Implemented as an extension to the discriminating-guidance authoring rule rather than a separate rule, because the two concerns are closely related and splitting them would create two rules that are always applied together.

## D13 — Trigger description and segmentation

Every standard carries a trigger description as its first content after the header. This is authored once and serves both skill and bundle deployment — it is the single artefact that controls how the standard is discovered and loaded across platforms.

The 130-character budget is the tightest confirmed cross-platform trigger budget across platforms implementing the agent skills standard (agentskills.io), currently adopted by Claude, Codex, GitHub Copilot, Cursor, Gemini CLI, and 30+ others. The figure is a union minimum — the smallest confirmed budget across all adopting platforms. It should be revised when platform budgets change.

The budget also serves as the segmentation test. If the trigger elements won't fit in 130 characters, the standard is too broad for a single skill and should be split. Cutting along dependency lines ensures co-dependent guidance loads together. Each sub-standard must be self-contained — the self-containment authoring rule applies to each part independently.

## D14 — Carry to Deployment: aggregate description budget

Deployment's weight gate gains a second measure beyond total context weight: the aggregate sum of all skill trigger descriptions must fit within the platform's shared description budget. This is a packaging constraint — the total description space available to a plugin is shared across all skills it contains, so each trigger description's cost is not just its own 130-character fit but its contribution to the aggregate.

This decision is carried to Deployment, not implemented by Standards.

## D15 — Two classes of standard by load pattern

Standards fall into two classes: task standards and carried standards. The distinction is load pattern, not subject matter.

Task standards load for a specific task and can afford weight because the cost is contextually proportionate. Carried standards govern broad behaviour, sit in memory across most sessions, and must be lean because the overhead is paid everywhere.

Both classes follow the same authoring rules and both use the two-model design sequence. The class distinction affects how much design effort must go into the solving model. For task standards, leanness is still desirable but weight is tolerable because the cost is bounded to the task. For carried standards, leanness is non-negotiable and is the primary design constraint — the solving model must be smart enough that the resulting standard is lean.

The DocMeth clean-sheet rebuild (2026-09-14) is the worked example: the main DocumentationMethodology_Standard is a carried standard; the SchemaAuthoring_Standard is a task standard. The two demanded materially different design effort to achieve appropriate weight.

## D16 — Two-model design sequence

The design of a standard follows a two-model sequence: an intent model (objectives and requirements) and a solving model (a construct designed to deliver those objectives). The solving model translates into the standard.

This is an extension of the normal AIDE design flow, not a departure. The front half — intent then model — is the same as all AIDE design. The solving model is a model-before-build step. This preserves consistency with the broader framework while adding the extra beat that standard design requires.

For carried standards, the solving model is where the critical effort goes. Leanness is not achieved by compressing a heavy standard — it is achieved by designing a solving model smart enough that explaining it is cheap but applying it covers most of the requirements. The model does the work that documentation would otherwise have to do. If the resolved standard is not lean, the solving model is not yet a good enough solution to the intent, and the fix is back at model design.

## D17 — Default-Required strength assignment

The default strength is Required. Items at the default carry no explicit tag — only departures (Recommended, Optional, Information) are tagged. This was adopted during the DocMeth clean-sheet rebuild and replaced the previous approach where every item carried an explicit strength.

The rationale is leanness: most items in a well-designed standard are Required, so tagging each one adds repetitive weight without adding information. Tagging only exceptions makes the non-Required items visually distinct, which is more useful than uniform tagging.

## D18 — No consumer, no rule

Every rule must have an operational consumer — something that acts on it at the moment of application. A rule with no consumer is governance without effect. This was the test that removed lifecycle states (Current, Superseded, Archived) from the DocMeth rebuild: no operational consumer existed for those states, so they were cut despite being conceptually reasonable.

The test is distinct from the carry test. The carry test asks whether the item is needed at the moment of application; no-consumer asks whether anything would actually behave differently. An item can pass the carry test (it is about application-time concerns) but fail the consumer test (nothing acts on it).

## D19 — Name your principles

When a recurring concept drives multiple rules, pull it up to a named principle. Named principles are cheaper to carry than repeating the underlying reasoning at each point of use. They also give consumers an anchor — a concept they can recognise and apply across contexts rather than following individual rules mechanically.

This was observed during the DocMeth rebuild: the default-and-override pattern recurred across versioning, strength, and optionality, and was pulled up to a named principle rather than being restated each time.

## D20 — Earn your place is a design rule, not an authoring rule

Every element in the design must justify its presence against the objectives in the intent model. A concept, classification, stage, or mechanism that does not contribute to the objectives is removed regardless of how well-conceived it is in isolation.

This is a design rule operating on the solving model, not an authoring rule operating on the resolved standard. The distinction matters because the three filters operate at different points:

- **Earn your place** — does this element in the design/solving model contribute to the objectives in the intent model?
- **The carry test** — does this resulting item need to be present at the moment of application?
- **Leanness** — is the necessary carried guidance expressed without avoidable context cost?

Earn-your-place was initially enumerated among the authoring rules. Cross-review (2026-09-14) identified that the Authoring Standard v6 had already placed it correctly in the design section, and Design/Decisions should agree.

## D21 — Acceptance test amended for ambient framework context

The acceptance test previously said "given only this standard and its declared dependencies." This excluded framework-level context that is delivered ambient — universal standards exempt from `uses` declarations, and skills that fire on trigger within the standard's applicability scope.

The exclusion was unintentional. The self-containment rule ensures a standard works without its design document present — it was never meant to exclude framework infrastructure the standard legitimately operates within. The Tools cross-review (round 3) exposed the gap: a tool that relies on the design-approach skill would fail the literal test despite working correctly in AIDE's actual architecture.

The fix adds "and the ambient framework context guaranteed to be present for the representative operation" after "its declared dependencies." This covers universal standards, triggered skills, and any future delivery mechanism that provides framework-level context without per-document dependency declarations. "Guaranteed" is the operative word — the criterion is architectural guarantee, not scope overlap, preserving the distinction between applicability and triggering established in D11.

An Information-strength definition of "ambient framework context" was added to the standard adjacent to the acceptance test, per cross-review finding F1: the standard must define the category it introduces.

The Tools Authoring Standard restatement was synced in the same change to avoid a live inconsistency (cross-review finding F3).

---

Version note: v5 — adds D22 (curated standards binders as future consideration). Build domain decisions (deployment-target requirement, development standard model) recorded from the Capabilities development-standards work. 2026-09-23. Replaces v4.

## D22 — Curated standards binders — future consideration

Two curated binders — a framework standards binder (all operational standards) and a development standards binder (all development standards) — would provide project-context access to the full set of standards for platforms where plugins are not supported (currently ChatGPT). Output location: `DigitalBusiness-AIDE\Deployment Binders`. Not designed or built now — noted as a future consideration when the need is demonstrated. The binder builder's existing multi-binder support (settings files per binder) would handle the mechanics.

## D23 — Development standard supersedes authoring standard

The Capabilities Development Standard (D5) established that each type's development standard supersedes the existing authoring standard with broader scope. For Standards, this means the Standards Development Standard replaces Standards_Authoring_Standard_v8. The authoring content is embedded unchanged; build, deployment, and consumption sections are added. The old authoring standard is removed from the repo (git history preserves it). The Standards Consumption Standard's `uses` is updated to reference the development standard.
