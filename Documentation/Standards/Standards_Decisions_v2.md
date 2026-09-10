Standards — Decisions | decisions | Standards_Decisions@v2 | 2026-09-11

## D1 — Standards is a methodological component, same pattern as Infrastructure and Tools

Standards defines how to create its type. Individual instances live with their consuming component. This was settled in the overview as the common pattern for all three capability-type components and confirmed in the structure session. The alternative — Standards holding all standards — was rejected because it violates the what-knows-most-about-it ownership principle.

## D2 — Six authoring rules, not a template

The authoring methodology is expressed as six rules (carry test, leanness, discriminating guidance, strength assignment, self-containment, applicability scope) rather than a prescribed template or structural specification. The author decides what a standard contains and how it is organised, provided it meets the terms.

A template risks becoming apparatus — a structure to fill in rather than a set of outcomes to achieve. The six rules already tell an author what a good standard must do. Document structure belongs to Documentation Methodology; Standards defines what the content must achieve, not what it must look like.

## D3 — Four strength levels, strength per item not per section

The strength model uses four levels: required, recommended, optional, information. The fourth level (information) was added specifically for reference-origin content that needs to reach the platform for awareness without carrying a compliance expectation.

Strength is a property of each item rather than a section organiser because a single standard will naturally mix levels — a section on authoring might contain two required rules, one recommended practice, and one piece of information context. Grouping by strength would break the logical flow of the guidance.

A document-level default strength is permitted as a shorthand — the author declares it once and only marks items that differ. Nearest declaration wins. This reduces clutter without changing the per-item principle.

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

---

Version note: v2 — adds D9 through D14. D9-D12 from legacy binder review, D13-D14 from voice session. Updates D2 (five rules to six) and D6 (one output to two). 2026-09-11.
