> identity: Standards_Design@v5 | doctype: design | updated: 2026-09-24

## Brief

**Purpose.** Define how a standard is designed, authored, built, and deployed within AIDE. Standards is a methodological component — it owns the methodology for building standards, not the standards themselves. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The authoring methodology, the strength model, the reference-to-standard pipeline, the relationship between a standard and its design, applicability scope, the build domain (skill packaging and deployment), and the runtime contract for operating under standards. Individual standards, document structure, and the cross-review process are out of scope.

**Target outcome.** Two deployed standards: the Standards Development Standard (how to design, author, build, and deploy a standard) and the Standards Consumption Standard (how to operate under applicable standards at runtime). The development standard supersedes the earlier authoring standard per the Capabilities Development Standard model.

**Definition of done.**

1. A developer can design a standard — the two classes, the two-model sequence, earn-your-place, and when a design is required.
2. A developer can author a conforming standard — the authoring rules, strength vocabulary, trigger description and segmentation, applicability scope, and schema definitions, with each requirement, recommendation and piece of guidance clearly marked.
3. A developer can review a standard — the acceptance test, the cross-review requirement, and what makes a standard acceptable.
4. A developer can build a standard — the skill file format, plugin placement, and build preconditions.
5. A developer can deploy a standard — the deployment path and the registration it needs.
6. Sessions can operate under applicable standards — applicability evaluation, combining, conflict resolution, and human override.
7. The development standard and the consumption standard can be produced entirely from this design.

**Linked build outcome.** Standards Development Standard, deployed as a skill in the `aide-dev` plugin. Standards Consumption Standard, deployed as a skill in the `aide` plugin.

## What a standard achieves

A standard shapes decisions and behaviour at the moment of application. It reaches the AI platform as a capability — either as a skill loaded on trigger, or as binder content loaded into project context. In both cases, the standard is what the session consumes. Everything behind it — the design, the decisions, the reference knowledge — stays outside the session.

That single fact drives the authoring model: a standard carries only what is needed at the moment of application, because everything in it costs context space and attention.

## Two classes of standard

A standard's design approach is determined by its load pattern, not its subject. The distinction affects how much design effort goes into the standard — specifically, how hard the author must work to achieve leanness.

**Task standards** load only when performing a specific task — authoring a doctype, running a cross-review, defining a schema. The standard is contextually relevant to the work being done, and weight is acceptable because the cost is paid only in that context. A task standard can be reasonably heavier because the overhead is proportionate to the work it supports.

**Carried standards** govern broad behaviour that applies across most sessions — document identity, versioning, how documents work. They sit in memory and tax nearly every session. Leanness is non-negotiable for this class.

Both classes follow the same authoring rules and both use the two-model design sequence. The class distinction affects the design effort invested in the solving model: a carried standard demands substantially greater model quality because persistent context cost makes leanness a primary constraint. A task standard still uses the sequence, but additional weight is tolerable because the cost is bounded to the task.

## What Standards owns

### The authoring methodology

How to decide what goes into a standard, how to write it, and how lean is lean enough. Eight rules govern authoring, plus the trigger description and segmentation requirements below:

**The carry test.** Every item must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document.

**No consumer, no rule.** Every rule must have an operational consumer — something that acts on it at the moment of application. A rule with no consumer is governance without effect. If nothing would behave differently with the rule removed, the rule does not belong.

**Leanness.** A standard earns its context cost. Every sentence displaces something else the session could hold. The target is the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard reads as a short document that leaves the consumer confident about what to do.

**Discriminating guidance.** A standard that says "do X" without helping the consumer recognise when and how is governance without value. Frame requirements through the consequence or value of meeting them, not through bare authority — a rule the consumer cannot see the reason for reads as enforcement rather than guidance. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Every item carries one of the four strength levels. The default strength is Required. Items that depart from the default carry their own strength explicitly; nearest declaration wins. This means: tag only the exceptions. Most items in a well-designed standard are Required and carry no explicit tag. Over-use of Recommended or Optional weakens the standard; over-use of Information turns it into a reference document.

**Self-containment.** A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but it must not depend on it. The consumer has the standard; the design is available but not loaded.

**Acceptance test.** Self-containment is verified by a concrete test before a standard is accepted: given only this standard, its declared dependencies, and the ambient framework context guaranteed to be present for the representative operation, can a fresh AI perform the representative operations covered by the applicability statement? If it cannot, the standard fails the self-containment rule and must not be published. Ambient framework context means framework capabilities the architecture guarantees will be present without a `uses` declaration — universal standards and independently triggered skills. "Guaranteed" is the operative word: the criterion is architectural guarantee, not scope overlap.

**Applicability scope.** Every standard declares the conditions under which it is applicable — what situation, activity, or context makes it relevant and of value. Scope is evaluated at application time, independent of how the standard was loaded. Scope targets behaviour and relevance, not a specific platform, package, or deployment target. A loaded standard whose scope does not match the current situation is not applied.

**Name your principles.** When a recurring concept drives multiple rules, pull it up to a named principle. Named principles are cheaper to carry than the repeated reasoning behind them, and they give consumers an anchor for understanding why related rules exist.

### Trigger description and segmentation

Every standard carries a trigger description as the first content after the header. The trigger description is authored once and serves both skill and bundle deployment — it is the single artefact that determines how the standard is loaded across platforms.

The trigger description must fit within 200 characters. This is AIDE policy, not a specification limit, and it can be adjusted in the standard. The Agent Skills specification allows descriptions up to 1024 characters; AIDE sets a tighter budget for two reasons. It matches the tightest known surface cap — the claude.ai skill uploader accepts 200 characters. And it keeps descriptions short enough to survive the shared skill-listing budget, which platforms truncate when many skills are installed. Front-load trigger words so the most important terms survive truncation.

The description budget doubles as the segmentation test. If the trigger elements that define when a standard is needed will not fit within 200 characters, the standard should be split into sub-standards along dependency lines so co-dependent guidance loads together. Each sub-standard must be self-contained.

A carry to Deployment: the aggregate sum of skill trigger descriptions across all deployed standards must be checked against the platform's shared description budget. This is a second measure for Deployment's weight gate.

### The strength model

Four levels defining how strongly an item in a standard applies:

- **Required** — must comply. Departure is a defect. This is the default; items at Required carry no explicit tag.
- **Recommended** — should comply. Departure needs a reason, but the reason is the author's judgement, not an approval process.
- **Optional** — available for use. No compliance expectation.
- **Information** — awareness content. Exists so the consumer knows it, not so they act on it.

Strength is a property of each item, not a section heading, because a single standard will mix levels. The vocabulary — the four words and their definitions above — is standardised so consumers read strengths consistently across all standards.

### The reference-to-standard pipeline

A reference is a design-time document type recording knowledge and concepts. When reference knowledge needs to reach the AI platform, it is authored into a standard at information strength. The decision criterion is the same carry test: does this knowledge need to be present at the moment of application? If the consumer needs to be aware of it to make good decisions, it earns a place. If it only informed the design, it stays in the design.

Reference is a document type only, not an output type. The distinction matters: a reference informs the design process; a standard is the delivery mechanism.

### The relationship between a standard and its design

A design almost always exists behind a standard — authoring straight to standard is the exception. The standard is authored fresh from the design, never by modifying a previous standard version. The design holds the reasoning, the alternatives, the constraints. The standard holds only the conclusion, stated as guidance.

The standard does not carry design derivation into the session — the alternatives considered, the reasoning used to choose the solution, the historical discussion. Application-facing rationale — a named principle, a consequence, a clarification needed to apply the rule intelligently — may be carried when it passes the carry test. If a consumer needs deeper reasoning than the standard provides, the design is available outside the session — but the standard does not depend on it being present.

### Designing a standard — the two-model sequence

The design of a standard follows a two-model sequence that extends the normal AIDE design flow:

1. **Intent model.** The objectives, requirements, and what the standard must achieve. This is the same intent-then-model front half as any other AIDE design work.
2. **Solving model.** A construct — a model, a grammar, a classification — designed to deliver those objectives. The solving model translates into the standard, which is the buildable output.

The front half is identical to all AIDE design. The solving model is a model-before-build step: design a model smart enough to carry the objectives, then build the standard from it.

For carried standards, the solving model is where the critical design effort goes. Leanness is not achieved by compressing a heavy standard. It is achieved by designing a solving model that is smart enough that explaining it is cheap but applying it produces most of the required outcomes. The effort goes into the intelligence of the model. The model does the work that documentation would otherwise have to do.

The leanness of the resolved standard is a readout on how well the solving model fits the intent model. If the output is not lean, the solving model is not yet a good enough solution — the fix is back at model design, not at the documentation level.

**Earn your place.** Every element in the design must justify its presence against the objectives in the intent model. A concept, classification, stage, or mechanism that does not contribute to those objectives is removed regardless of how well-conceived it is in isolation.

### Trigger and scope

Triggering and applicability scope are distinct responsibilities. Triggering is a delivery concern — getting the standard loaded where it might be needed. Scope is the standard's own concern — declaring the conditions under which it is applicable once loaded. Every standard carries its own scope because what is loaded on any given platform cannot be guaranteed.

Scope targets behaviour and relevance — what needs to be true for the standard to be of value — not a specific platform, package, or deployment target. Triggering belongs to Infrastructure; scope belongs to the standard and is defined by its author.

### Conflict resolution

The Standards Consumption Standard applies whenever an AI session is operating under one or more AIDE standards. It does not govern designing, authoring, reviewing, building, or deploying standards — those are governed by the Standards Development Standard.

When multiple standards apply to the same work, compatible standards stack — they are combined, not chosen between, and each item is applied according to its declared strength. When two applicable items genuinely oppose each other on the same point, higher strength governs, in the order Required > Recommended > Optional > Information. Equal-strength genuine conflict is surfaced and escalated rather than silently resolved; when surfacing it, identify the competing standards, the opposing items, and the work affected. Conflict is not manufactured from different concerns that can both be satisfied — two standards addressing different aspects of the same work are not in conflict merely because both apply.

### Human override

Direct human instruction may override a standard within that person's authority. When it displaces a required or recommended item, the AI states the standard's position and the material consequence of departure, makes the departure visible, and continues under the human's instruction. A human override does not change the standard — it authorises departure for the current work; the standard remains as written for all other application.

### Reporting

Normal operation under standards does not narrate every standard consulted. Silent compliance is the expected state. What is surfaced is what materially affects the work: blocking requirements, meaningful departures, conflicts, or a standard-driven consequence the work owner needs to know. This is Recommended rather than Required because judging what is material is contextual — the rule sets the default, not a fixed threshold. The reason is attention cost: narrating every applied standard buries the few things the human actually needs to act on.

### Evaluating applicability

A loaded standard is not automatically applicable. Before applying a standard, its declared applicability scope is evaluated against the current situation; a standard whose scope does not match is not applied, regardless of how it was loaded. This is the consumption-side counterpart of the applicability-scope authoring rule.

## Applicability of the development standard

The Standards Development Standard applies when designing, authoring, reviewing, building, or deploying a standard within the AIDE framework. It does not apply to standards authored for other development projects or methodologies — those projects may adopt it, but AIDE does not govern them.

## Reviewing a standard

A standard is reviewed before it is accepted. Two checks, both required:

**Acceptance test.** The developer runs the acceptance test defined in the authoring methodology. A standard that fails it is not published — the fix is to the standard (or its declared dependencies), not to the test.

**Cross-review.** A separate AI reviews the standard together with its design and decisions. The reviewer is directed to find defects — contradictions, gaps, overclaims, rules without consumers, content that cannot be traced to the design — not to improve wording. The reviewer is given the design's definition of done to test against. Findings are triaged as defects, partly valid, or misreadings; remediation is applied and recorded in the decisions. A further round is needed when remediation introduces material the reviewer has not seen; corrections to what was already reviewed do not need one.

The reason for a separate AI is independence: the author's session shares the author's assumptions. The cross-review process itself is a Working Practices convention; this section records what a standards developer needs to perform it.

## Schema definitions

Standards owns two types. They stay in the development standard rather than a separate schema standard because there are only two definitions and they change at the same cadence as the authoring rules.

The definitions are written to Documentation Methodology's definition contract — the properties a doctype or blocktype definition carries, and what they mean. A reader needs that contract to interpret them, so the development standard declares `uses DocumentationMethodology_SchemaAuthoring_Standard@v1` (D26).

**Standard (doctype).** Purpose: shape decisions and behaviour at the moment of application — lean, memory-resident, applied alongside many others. Included blocktypes: Clarification, Contents, Summary, Version note — all optional. Format constraint: markdown.

**Clarification (blocktype).** Purpose: reasoning and justification supporting the standard's stated rules — the design-side "why" surfaced into the standard where it helps the consumer apply the rules. Recognition: by subheading `Clarification`. Governed by the split test: it stays in the standard when small and is removed when it would bloat the loaded standard, in which case the reasoning lives in the design.

## Building a standard

The Capabilities Development Standard defines build standards per capability type — the type-specific conventions for how that type of capability is built. Standards' build domain is the packaging of accepted standard documents into skills or binder content.

The build specification is the accepted standard document. The build target is a skill file — a markdown file with YAML frontmatter (name and trigger description) containing the standard's content, placed in the appropriate marketplace plugin.

When a standard is added or updated, its skill is rebuilt and deployed.

### The skill file

The skill file format:

```
---
name: <skill-name>
description: "<trigger description>"
---

<!-- provenance: <source_standard_identity> | redistributed: <plugin> (<marketplace>), <date> -->

<standard content>
```

The `description` field is the trigger description — the text, within the 200-character budget, that determines when the platform loads the skill. The provenance comment records which standard document the skill was built from and when.

The `name` field is the skill's identifier within the plugin. It follows the Agent Skills specification's rules, which platforms enforce when loading a skill:

- 1–64 characters;
- lowercase letters a–z, digits 0–9, and hyphens only;
- no leading, trailing, or consecutive hyphens;
- must match the skill's directory name.

The standard content is copied from the accepted standard document. The document header (identity line, `uses` declarations) is omitted — those are document metadata, not session content. The version note is omitted — the provenance comment serves the same purpose for a built skill.

### Plugin placement

Standards are deployed in one of two plugins in the `digitalbusiness-aide` marketplace:

- **`aide`** — operational standards that apply during normal work (principles, working practices, assurance, consumption, docmeth, messaging, PD).
- **`aide-dev`** — development standards that apply when building AIDE itself (standards development, tools development, services development, capabilities development, schema authoring).

The skill directory name follows the convention `<skill-name>` within the plugin's `skills/` folder. The skill name should be short, descriptive, and match how the standard would be referred to in conversation.

### Deployment path

The built skill is deployed through the marketplace plugin pipeline:

1. Place the skill file at `<plugin>/skills/<skill-name>/SKILL.md` in the deploy repo (`DigitalBusiness-AIDE-Deploy`).
2. Merge via PR — direct commits to `main` do not trigger plugin updates.
3. Refresh the marketplace clone: `claude plugin marketplace update <n>`.
4. Restart Claude Desktop.

Skills reach Chat via web UI account-level plugin registration and Code/Cowork via desktop app plugin registration. Both registration paths are needed for coverage of all three Claude surfaces. The full deployment methodology and known platform issues are documented in `Infrastructure_MCPDeliveryModel@v2`.

**Platform support.** Claude — Chat, Code, and Cowork — is supported. ChatGPT and Codex are pending. For ChatGPT, which does not load plugins, the route is the curated standards binders held as a future consideration (D22). No adapters for other platforms are built.

### Build preconditions

Cross-review accepted and acceptance test passed before build. The linked build outcome on the brief of the design that produces the standard states the deployment target — which plugin the skill is built for. This is recorded during design so the builder does not have to determine it.

## What Standards produces

Two standards:

**The standards development standard** — aimed at anyone building a standard, covering the full lifecycle: design, authoring, build, and deployment. Supersedes the earlier authoring standard with broader scope — the settled authoring rules are embedded unchanged, with build and deployment guidance added.

**The standards consumption standard** — aimed at AI sessions operating under applicable standards. Covers conflict resolution, human override, applicability evaluation, and runtime operation under standards.

## What the author decides

A standard has no prescribed template. The author decides what the standard contains and how it is structured, provided it meets the terms defined in the Standards Development Standard. The authoring rules tell the author what a good standard achieves; the author meets them however the content demands.

## Boundaries

Standards does **not** own:

- **The three-layer authoring model** — a project-level convention consumed by all components, not a Standards mechanism.
- **The cross-review process** — the obligation that every standard is reviewed by a separate AI before acceptance is a collaboration convention owned by Working Practices. Standards' output goes through it.
- **Document structure and block grammar** — Documentation Methodology owns how documents are composed.
- **Triggering and delivery** — how a standard is loaded (skill headers, binder inclusion, package distribution) is owned by Infrastructure.
- **Packaging and deployment** — how a standard becomes a skill or binder entry is owned by Infrastructure (the packaging mechanism and delivery pipeline). Standards owns the build domain knowledge — what the skill file looks like, which plugin a standard targets, and the build preconditions. The weight gate that checks the combined load is a deployment concern.
- **Any individual standard** — each lives with its owning component.

## Carries to other components

**To Documentation Methodology:** the Contents/Summary edge — Contents maps what is where to judge relevance, Summary gives what the document establishes. Their edges need to stay distinct. Flagged as a common issue for standards authors; the edge definition is document-structure grammar.

---

Version note: v4 — brief updated (purpose, scope, target outcome, definition of done) for the development standard model. Added: acceptance test with ambient-context definition, applicability of the development standard, reviewing a standard, schema definitions, and full build detail (skill file format, plugin placement, deployment path, preconditions). The development standard can now be produced entirely from this design. Consumption content completed (applicability of the consumption standard, precedence order, what to identify when surfacing conflict, override scope, reporting, evaluating applicability) so the consumption standard can also be produced from it. 2026-09-23. Replaces v3.

Version note: v5 — second cross-review remediation. Linked build outcome added to the brief (F8); build preconditions say the field is on the brief of the producing design. Consumption applicability now names the Standards Development Standard and all five development activities (F3); development-standard applicability adds reviewing (F4). The DocMeth dependency justified in schema definitions (F9, D26). Trigger description budget set to 200 characters as AIDE policy, and the specification's `name` rules added to the skill file (F12, D27). Platform-support statement added to deployment; "full three-surface coverage" now reads "coverage of all three Claude surfaces" (F13). 2026-09-24. Replaces v4.
