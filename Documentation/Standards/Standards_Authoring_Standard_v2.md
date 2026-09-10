Standards — Standard | standard | Standards_Authoring_Standard@v2 | 2026-09-11

## What a standard is

Information. A standard defines rules, expectations, guidance and context that shape decisions and behaviour while work is being done. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content in project context. Everything behind it (the design, the decisions, the reference knowledge) stays outside the session.

Information. A standard earns its context cost. Everything in it displaces something else the session could hold.

## Authoring rules

**The carry test.** Required. Every item in a standard must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document. This is the single most important authoring rule.

**Leanness.** Required. Write the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard leaves the consumer confident about what to do without carrying anything they do not need.

**Discriminating guidance.** Required. A rule that says "do X" without helping the consumer recognise when and how to apply it is governance without value. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Required. Every item carries a strength, selected by the author from the vocabulary below. Over-use of required produces rigidity; over-use of optional achieves nothing.

**Self-containment.** Required. A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but must not depend on it being loaded.

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

## Ownership

**Each standard lives with its owning component.** Required. Standards is a methodological component — it defines how to build a standard, not where standards live. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v2 — revised after cross-review. Removed cross-review obligation (Working Practices, not Standards). Removed invented strength-assignment defaults. Added strength to context-setting items. Added deployment boundary. Restored reference document-type distinction.
