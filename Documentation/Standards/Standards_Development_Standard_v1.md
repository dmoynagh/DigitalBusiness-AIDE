> identity: Standards_Development_Standard@v1 | doctype: standard | updated: 2026-09-23 | uses: Capabilities_Development_Standard@v1, DocumentationMethodology_SchemaAuthoring_Standard@v1

# Standards — Development Standard

How to design, author, review, build, and deploy an AIDE standard — authoring rules, strength model, scope, trigger, and segmentation.

## What a standard is

Information. A standard defines rules, expectations, guidance and context that shape decisions and behaviour while work is being done. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content in project context. Everything behind it (the design, the decisions, the reference knowledge) stays outside the session.

Information. A standard earns its context cost. Everything in it displaces something else the session could hold.

Information. The invocability test in the Tools Development Standard draws the boundary between a standard and a tool. A standard shapes decisions and behaviour — you follow it. A named invokable action — something you would run — is a tool and belongs there.

## Applicability

Information. This standard applies when designing, authoring, building, or deploying a standard within the AIDE framework. It does not apply to standards authored for other development projects or methodologies.

## Two classes of standard

A standard's design approach is determined by its load pattern, not its subject.

**Task standards** load for a specific task — authoring a doctype, running a cross-review, defining a schema. The standard is contextually relevant to the work being done, and weight is acceptable because the cost is paid only in that context.

**Carried standards** govern broad behaviour that applies across most sessions — document identity, versioning, how documents work. They sit in memory and tax nearly every session. Leanness is non-negotiable for this class.

The class distinction affects design effort, not authoring rules. Both classes follow the same authoring rules below. But the design approach for a carried standard demands more — see "Designing a standard."

## Authoring rules

**The carry test.** Every item in a standard must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document. This is the single most important authoring rule.

**No consumer, no rule.** Every rule must have an operational consumer — something that acts on it at the moment of application. A rule with no consumer is governance without effect. If nothing would behave differently with the rule removed, the rule does not belong.

**Leanness.** Write the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard leaves the consumer confident about what to do without carrying anything they do not need.

**Discriminating guidance.** A rule that says "do X" without helping the consumer recognise when and how to apply it is governance without value. Frame requirements through the consequence or value of meeting them, not through bare authority — a rule the consumer cannot see the reason for reads as enforcement rather than guidance. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Every item carries a strength, selected by the author from the vocabulary below. The default strength is Required. Items that depart from the default carry their own strength explicitly — nearest declaration wins. This means: tag only the exceptions. Most items in a well-designed standard are Required and carry no explicit tag. Over-use of Recommended or Optional weakens the standard; over-use of Information turns it into a reference document.

**Self-containment.** A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but must not depend on it being loaded.

**Acceptance test.** Before accepting a standard, test: given only this standard, its declared dependencies, and the ambient framework context guaranteed to be present for the representative operation, can a fresh AI perform the representative operations covered by the applicability statement? If it cannot, the standard fails the self-containment rule and must not be published.

Information. Ambient framework context means framework capabilities the architecture guarantees will be present without a `uses` declaration — universal standards and independently triggered skills.

**Applicability scope.** Every standard declares the conditions under which it is applicable — what situation, activity, or context makes it relevant and of value. Scope is evaluated at application time, independent of how the standard was loaded. Frame scope through behaviour and relevance, not through a specific platform, package, or deployment target. A loaded standard whose scope does not match the current situation is not applied.

**Name your principles.** When a recurring concept drives multiple rules, pull it up to a named principle. Named principles are cheaper to carry than the repeated reasoning behind them, and they give consumers an anchor for understanding why related rules exist.

## Trigger description and segmentation

**Trigger description.** Every standard carries a trigger description as the first content after the header. The trigger description is authored once and serves both skill and bundle deployment — it is the basis for loading the standard where it is needed.

**Description budget.** The trigger description must fit within 130 characters — the tightest confirmed cross-platform trigger budget. Front-load trigger words so the most important terms survive truncation.

**Segmentation.** The description budget is the size test for whether a standard should be split. If the trigger elements that define when the standard is needed will not fit within the budget, split into sub-standards rather than compressing the description into uselessness.

**Where to cut.** Split along dependency lines so co-dependent guidance loads together. Each sub-standard must be self-contained — the self-containment authoring rule applies to each part independently.

## Strength vocabulary

Information. Four levels. These words and definitions are the standard vocabulary — use them consistently across all standards.

- **Required** — must comply. Departure is a defect. This is the default strength; items at Required carry no explicit tag.
- **Recommended** — should comply. Departure needs a reason, but the reason is the author's judgement, not an approval process.
- **Optional** — available for use. No compliance expectation.
- **Information** — awareness content. Exists so the consumer knows it, not so they act on it.

## Designing a standard

**Design is the default.** Recommended. A design almost always exists behind a standard. Authoring straight to standard is the exception — reserved for cases where the content is simple enough that a design would restate rather than elaborate.

**Author fresh.** A standard is authored from its design, not by modifying a previous version of the standard. The design holds the reasoning and constraints; the standard holds the conclusion as guidance.

**No prescribed template.** Information. A standard has no fixed structure. The author decides what it contains and how it is organised, provided the authoring rules above are met.

**Two-model design sequence.** The design of a standard follows a two-model sequence:

1. **Intent model.** Define the objectives, requirements, and what the standard must achieve. This is the same intent-then-model front half as any other AIDE design work.
2. **Solving model.** Design a construct — a model, a grammar, a classification — that delivers those objectives. The solving model translates into the standard, which is the buildable output.

Information. This two-model sequence is an extension of the normal design flow, not a departure from it. The front half is identical to all AIDE design. The solving model is a model-before-build step: design a model smart enough to carry the objectives, then build the standard from it.

**Leanness through model quality.** For carried standards, leanness is not achieved by compressing a heavy standard. It is achieved by designing a solving model that is smart enough that explaining it is cheap but applying it produces most of the required outcomes. The effort goes into the intelligence of the model. The model does the work that documentation would otherwise have to do.

Information. The leanness of the resolved standard is a readout on how well the solving model fits the intent model. If the output is not lean, the solving model is not yet a good enough solution — the fix is back at model design, not at the documentation level.

**Earn your place.** Every element in the design must justify its presence. If a concept, a classification, a stage, or a mechanism does not contribute to the objectives in the intent model, it is removed regardless of how well-conceived it is in isolation.

## The reference-to-standard pipeline

Information. Reference documents are design-time knowledge. When reference knowledge needs to be present in the AI session, it is authored into a standard at information strength. The decision criterion is the carry test: does the consumer need to be aware of this knowledge at the moment of application? If yes, it earns a place. If it only informed the design, it stays in the design.

Information. Reference is a document type, not an output type. A reference informs the design process; a standard is the delivery mechanism. The distinction matters because it prevents reference from becoming a parallel output channel.

## Review

A standard is reviewed before it is accepted. Both checks are required.

**Acceptance test.** Run the acceptance test in the authoring rules. A standard that fails it is not published.

**Cross-review.** A separate AI reviews the standard with its design and decisions. Direct the reviewer to find defects — contradictions, gaps, overclaims, rules without consumers, content not traceable to the design — not to improve wording, and give the reviewer the design's definition of done to test against. Triage findings as defects, partly valid, or misreadings; remediate and record the outcome in the decisions. Run a further round when remediation introduces material the reviewer has not seen; corrections to reviewed material do not need one.

Information. The cross-review process is a Working Practices convention. A separate AI is used for independence — the authoring session shares the author's assumptions.

## Build

A standard is built by packaging it as a skill for plugin delivery. The authored standard document is the build specification.

### Preconditions

Cross-review accepted and acceptance test passed before build starts. These are authoring-phase completions, not build steps.

The brief's linked build outcome states the deployment target — which plugin the skill is built for. This is recorded during design so the builder knows where to place the skill without having to determine it.

### Building a skill

The skill file is a markdown file with YAML frontmatter containing the standard's content. Format:

```
---
name: <skill-name>
description: "<trigger description>"
---

<!-- provenance: <source_standard_identity> | redistributed: <plugin> (<marketplace>), <date> -->

<standard content>
```

The `description` field IS the trigger description — the 130-character text that determines when the platform loads the skill. The `name` field is the skill's identifier within the plugin, matching the skill directory name.

The provenance comment records which standard document the skill was built from and when. This is a build record, not a `uses` declaration.

The standard content is copied from the accepted standard document. The document header (identity line, `uses` declarations) is omitted — those are document metadata, not session content. The version note is omitted — the provenance comment serves the same purpose for a built skill.

### Plugin placement

Standards are deployed in one of two plugins in the `digitalbusiness-aide` marketplace:

- **`aide`** — operational standards that apply during normal work (principles, working practices, assurance, consumption, docmeth, messaging, PD). These load when work is being done.
- **`aide-dev`** — development standards that apply when building AIDE itself (standards development, tools development, services development, capabilities development, schema authoring). These load when AIDE capabilities are being designed, authored, or built.

The skill directory is named `<skill-name>` within the plugin's `skills/` folder. The skill name should be short, descriptive, and match how the standard would be referred to in conversation.

### Deployment target

A standard is deployed as a skill. When a standard is added or updated, its skill is rebuilt and deployed to the target plugin.

## Deployment

The built skill is deployed through the marketplace plugin pipeline:

1. Place the skill file at `<plugin>/skills/<skill-name>/SKILL.md` in the deploy repo (`DigitalBusiness-AIDE-Deploy`).
2. Merge via PR — direct commits to `main` do not trigger plugin updates.
3. Refresh the marketplace clone: `claude plugin marketplace update <n>`.
4. Restart Claude Desktop.

Skills reach Chat via web UI account-level plugin registration (Settings → Plugins) and Code/Cowork via desktop app plugin registration (Settings → Plugins → Discover). Both registration paths are needed for full three-surface coverage.

Information. The full deployment methodology, known platform issues, and workarounds are documented in `Infrastructure_MCPDeliveryModel@v2`. The deployment steps above are the minimum a builder needs; the delivery model document has the complete picture.

## Consumption

The Standards Consumption Standard governs how AI sessions operate under applicable standards — evaluating applicability, combining compatible standards, resolving conflicts, and handling human overrides. This development standard does not restate that content.

Information. A well-authored standard makes consumption natural: clear applicability tells the consumer when to apply it, discriminating guidance tells them how, and the strength model tells them how firmly.

## Ownership

**Each standard lives with its owning component.** Standards is a methodological component — it defines how to build a standard, not where standards live. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

## Schema definitions

Information. Standards owns two types. The split test says to keep them here — two definitions, same change cadence as the authoring rules.

### Standard

- **Purpose:** Shape decisions and behaviour at the moment of application. Lean, memory-resident, applied alongside many others.
- **Included blocktypes:** Clarification (optional), Contents (optional), Summary (optional), Version note (optional).
- **Format constraint:** markdown.

Information. The authoring rules, strength vocabulary, trigger description, applicability scope, and deployment guidance are defined elsewhere in this standard. The consumption contract is defined in the Standards Consumption Standard.

### Clarification

- **Purpose:** Reasoning and justification supporting the standard's stated rules. The design-side "why" surfaced into the standard where it helps the consumer apply the rules.
- **Recognition:** by subheading — `Clarification`.

Information. Governed by the split test: stays in the standard when small, removed when it would bloat the loaded standard. When removed, the reasoning lives in the design document.

---

Version note: v1 — supersedes Standards_Authoring_Standard@v8. All authoring content embedded unchanged. Review section added (acceptance test and cross-review). Build section covers skill file format, plugin placement, and preconditions; deployment covers the marketplace path. Consumption references the Standards Consumption Standard. Produced from Standards_Design@v4. 2026-09-23.
