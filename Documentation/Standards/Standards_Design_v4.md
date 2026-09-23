> identity: Standards_Design@v4 | doctype: design | updated: 2026-09-23

## Brief

**Purpose.** Define how a standard is designed, authored, and deployed within AIDE. Standards is a methodological component — it owns the methodology for building standards, not the standards themselves. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The authoring methodology, the strength model, the reference-to-standard pipeline, the relationship between a standard and its design, applicability scope, and the runtime contract for operating under standards. Individual standards, document structure, packaging, and the cross-review process are out of scope.

**Target outcome.** Two deployed standards: one for authoring (how to design, author, and deploy a standard) and one for consumption (how to operate under applicable standards at runtime).

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

**Applicability scope.** Every standard declares the conditions under which it is applicable — what situation, activity, or context makes it relevant and of value. Scope is evaluated at application time, independent of how the standard was loaded. Scope targets behaviour and relevance, not a specific platform, package, or deployment target. A loaded standard whose scope does not match the current situation is not applied.

**Name your principles.** When a recurring concept drives multiple rules, pull it up to a named principle. Named principles are cheaper to carry than the repeated reasoning behind them, and they give consumers an anchor for understanding why related rules exist.

### Trigger description and segmentation

Every standard carries a trigger description as the first content after the header. The trigger description is authored once and serves both skill and bundle deployment — it is the single artefact that determines how the standard is loaded across platforms.

The trigger description must fit within 130 characters — the tightest confirmed cross-platform trigger budget across platforms implementing the agent skills standard (agentskills.io). This figure is the union minimum across Claude, Codex, GitHub Copilot, Cursor, Gemini CLI, and other adopters. Front-load trigger words so the most important terms survive truncation.

The description budget doubles as the segmentation test. If the trigger elements that define when a standard is needed will not fit within 130 characters, the standard should be split into sub-standards along dependency lines so co-dependent guidance loads together. Each sub-standard must be self-contained.

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

When multiple standards apply to the same work, compatible standards stack — they are combined, not chosen between. When two applicable items genuinely oppose each other on the same point, higher strength governs. Equal-strength genuine conflict is surfaced and escalated rather than silently resolved. Conflict is not manufactured from different concerns that can both be satisfied.

### Human override

Direct human instruction may override a standard within that person's authority. When it displaces a required or recommended item, the AI states the standard's position and the material consequence of departure, makes the departure visible, and continues under the human's instruction.

## Building a standard

The Capabilities Development Standard defines build standards per capability type — the type-specific conventions for how that type of capability is built. Standards' build domain is the packaging of accepted standard documents into skills or binder content.

The build specification is the accepted standard document. Build produces three outputs:

**Skills.** Each standard is packaged as an individual skill file — a markdown file with YAML frontmatter (name and trigger description) containing the standard's content, placed in the appropriate marketplace plugin. Skills load on trigger when relevant.

**Framework standards binder.** A curated binder of all operational AIDE standards — the standards that apply during normal work (principles, working practices, assurance, consumption, documentation methodology, messaging, PD, and others as authored). This binder provides project-context access to the full set of framework standards without loading designs, decisions, or working documents.

**Development standards binder.** A curated binder of all AIDE development standards — the standards that apply when building AIDE itself (capabilities, standards, tools, services, utilities development standards, schema authoring, and others as authored). This binder provides project-context access to the full development methodology.

When a standard is added or updated, the relevant binder is rebuilt alongside the skill deployment.

The brief's linked build outcome states the deployment target — which plugin the skill is built for. This is recorded during design so the builder does not have to determine it. Two plugins serve different audiences: one for operational standards (applied during normal work), one for development standards (applied when building AIDE itself).

The practical skill file format, plugin structure, and deployment path are recorded in the Standards Development Standard — that is where the build knowledge lives. The design provides the reasoning; the standard carries the operational detail.

## What Standards produces

Two standards:

**The standards development standard** — aimed at anyone building a standard, covering the full lifecycle: design, authoring, build, and deployment. Supersedes the earlier authoring standard with broader scope — the settled authoring rules are embedded unchanged, with build and deployment guidance added.

**The standards consumption standard** — aimed at AI sessions operating under applicable standards. Covers conflict resolution, human override, applicability evaluation, and runtime operation under standards.

## What the author decides

A standard has no prescribed template. The author decides what the standard contains and how it is structured, provided it meets the terms defined in the standards authoring standard. The authoring rules tell the author what a good standard achieves; the author meets them however the content demands.

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

Version note: v4 — build section added (standards build domain, skill packaging, deployment-target requirement). "What Standards produces" updated to reflect development standard model. Boundaries updated for build domain ownership. 2026-09-23. Replaces v3.
