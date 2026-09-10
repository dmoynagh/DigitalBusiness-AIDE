Standards — Standard | standard | Standards_Authoring_Standard@v3 | 2026-09-11

## What a standard is

Information. A standard defines rules, expectations, guidance and context that shape decisions and behaviour while work is being done. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content in project context. Everything behind it (the design, the decisions, the reference knowledge) stays outside the session.

Information. A standard earns its context cost. Everything in it displaces something else the session could hold.

## Applicability

This standard applies when designing, authoring, or deploying a standard within the AIDE framework. It does not apply to standards authored for other development projects or methodologies.

## Authoring rules

**The carry test.** Required. Every item in a standard must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document. This is the single most important authoring rule.

**Leanness.** Required. Write the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard leaves the consumer confident about what to do without carrying anything they do not need.

**Discriminating guidance.** Required. A rule that says "do X" without helping the consumer recognise when and how to apply it is governance without value. Frame requirements through the consequence or value of meeting them, not through bare authority — a rule the consumer cannot see the reason for reads as enforcement rather than guidance. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Required. Every item carries a strength, selected by the author from the vocabulary below. A standard may declare a document-level default strength; items that differ from the default carry their own strength explicitly; nearest declaration wins. Over-use of required produces rigidity; over-use of optional achieves nothing.

**Self-containment.** Required. A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but must not depend on it being loaded.

**Applicability scope.** Required. Every standard declares the conditions under which it is applicable — what situation, activity, or context makes it relevant and of value. Scope is evaluated at application time, independent of how the standard was loaded. Frame scope through behaviour and relevance, not through a specific platform, package, or deployment target. A loaded standard whose scope does not match the current situation is not applied.

## Trigger description and segmentation

**Trigger description.** Required. Every standard carries a trigger description as the first content after the header. The trigger description is authored once and serves both skill and bundle deployment — it is the basis for loading the standard where it is needed.

**Description budget.** Required. The trigger description must fit within 130 characters — the tightest confirmed cross-platform trigger budget across platforms implementing the agent skills standard. Front-load trigger words so the most important terms survive truncation. The 130-character figure is the union minimum across Claude, Codex, GitHub Copilot, Cursor, Gemini CLI, and other adopters of the standard; revise when platform budgets change.

**Segmentation.** Required. The description budget is the size test for whether a standard should be split. If the trigger elements that define when the standard is needed will not fit within the budget, split into sub-standards rather than compressing the description into uselessness.

**Where to cut.** Required. Split along dependency lines so co-dependent guidance loads together. Each sub-standard must be self-contained — the self-containment authoring rule applies to each part independently.

## Strength vocabulary

Information. Four levels. These words and definitions are the standard vocabulary — use them consistently across all standards.

- **Required** — must comply. Departure is a defect.
- **Recommended** — should comply. Departure needs a reason, but the reason is the author's judgement, not an approval process.
- **Optional** — available for use. No compliance expectation.
- **Information** — awareness content. Exists so the consumer knows it, not so they act on it.

## Designing a standard

**Design is the default.** Recommended. A design almost always exists behind a standard. Authoring straight to standard is the exception — reserved for cases where the content is simple enough that a design would restate rather than elaborate.

**Author fresh.** Required. A standard is authored from its design, not by modifying a previous version of the standard. The design holds the reasoning and constraints; the standard holds the conclusion as guidance.

**No prescribed template.** Information. A standard has no fixed structure. The author decides what it contains and how it is organised, provided the authoring rules above are met.

## The reference-to-standard pipeline

Information. Reference documents are design-time knowledge. When reference knowledge needs to be present in the AI session, it is authored into a standard at information strength. The decision criterion is the carry test: does the consumer need to be aware of this knowledge at the moment of application? If yes, it earns a place. If it only informed the design, it stays in the design.

Information. Reference is a document type, not an output type. A reference informs the design process; a standard is the delivery mechanism. The distinction matters because it prevents reference from becoming a parallel output channel.

## Deployment

Information. Once a standard is authored and accepted, it is deployed as a capability — packaged by Infrastructure and delivered through the deployment pipeline. The author's responsibility ends at a complete, accepted standard. Packaging into a skill or plugin, and the weight gate that checks the combined load, are owned by Infrastructure and Deployment respectively.

Information. Triggering — how a standard gets loaded where it might be needed — is a delivery concern owned by Infrastructure, distinct from applicability scope which is owned by the standard itself.

## Ownership

**Each standard lives with its owning component.** Required. Standards is a methodological component — it defines how to build a standard, not where standards live. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v3 — adds applicability scope (new required rule), trigger description and segmentation (four required items), document-default weight (strength assignment), facilitative framing (discriminating guidance), trigger/scope distinction (deployment). Merges legacy binder review and voice session additions, 2026-09-11.
