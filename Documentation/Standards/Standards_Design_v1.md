Standards — Design | design | Standards_Design@v1 | 2026-09-10

## Brief

**Purpose.** Define how a standard is designed, authored, and deployed within AIDE. Standards is a methodological component — it owns the methodology for building standards, not the standards themselves. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The authoring methodology, the strength model, the reference-to-standard pipeline, and the relationship between a standard and its design. Individual standards, document structure, packaging, and the cross-review process are out of scope.

**Target outcome.** A deployed standards authoring standard that any component author uses when designing, authoring, and deploying a standard for their component.

## What a standard achieves

A standard shapes decisions and behaviour at the moment of application. It reaches the AI platform as a capability — either as a skill loaded on trigger, or as binder content loaded into project context. In both cases, the standard is what the session consumes. Everything behind it — the design, the decisions, the reference knowledge — stays outside the session.

That single fact drives the authoring model: a standard carries only what is needed at the moment of application, because everything in it costs context space and attention.

## What Standards owns

### The authoring methodology

How to decide what goes into a standard, how to write it, and how lean is lean enough. Five rules govern authoring:

**The carry test.** Every item must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document.

**Leanness.** A standard earns its context cost. Every sentence displaces something else the session could hold. The target is the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard reads as a short document that leaves the consumer confident about what to do.

**Discriminating guidance.** A standard that says "do X" without helping the consumer recognise when and how is governance without value. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Every item carries one of the four strength levels. The author decides what strength each item warrants. Over-use of required produces a standard that reads as rigid; over-use of optional produces one that achieves nothing.

**Self-containment.** A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but it must not depend on it. The consumer has the standard; the design is available but not loaded.

### The strength model

Four levels defining how strongly an item in a standard applies:

- **Required** — must comply. Departure is a defect.
- **Recommended** — should comply. Departure needs a reason, but the reason is the author's judgement, not an approval process.
- **Optional** — available for use. No compliance expectation.
- **Information** — awareness content. Exists so the consumer knows it, not so they act on it.

Strength is a property of each item, not a section heading, because a single standard will mix levels. The vocabulary — the four words and their definitions above — is standardised so consumers read strengths consistently across all standards.

### The reference-to-standard pipeline

A reference is a design-time document type recording knowledge and concepts. When reference knowledge needs to reach the AI platform, it is authored into a standard at information strength. The decision criterion is the same carry test: does this knowledge need to be present at the moment of application? If the consumer needs to be aware of it to make good decisions, it earns a place. If it only informed the design, it stays in the design.

Reference is a document type only, not an output type. The distinction matters: a reference informs the design process; a standard is the delivery mechanism.

### The relationship between a standard and its design

A design almost always exists behind a standard — authoring straight to standard is the exception. The standard is authored fresh from the design, never by modifying a previous standard version. The design holds the reasoning, the alternatives, the constraints. The standard holds only the conclusion, stated as guidance.

The standard does not carry reasoning into the session. If a consumer needs to understand why a rule exists, the design is available outside the session — but the standard does not depend on it being present.

## What Standards produces

One standard: the standards authoring standard. It is aimed at anyone building a component, telling them how to design, author, and deploy a standard for that component. It consumes its own rules — the first standard is self-describing.

The authoring standard covers design, authoring, and deployment of standards. Implementation and consumption guidance, if it ever earns its place, would live in a separate standard, not in this one.

## What the author decides

A standard has no prescribed template. The author decides what the standard contains and how it is structured, provided it meets the terms defined in the standards authoring standard. The five authoring rules tell the author what a good standard achieves; the author meets them however the content demands.

## Boundaries

Standards does **not** own:

- **The three-layer authoring model** — a project-level convention consumed by all components, not a Standards mechanism.
- **The cross-review process** — the obligation that every standard is reviewed by a separate AI before acceptance is a collaboration convention owned by Working Practices. Standards' output goes through it.
- **Document structure and block grammar** — Documentation Methodology owns how documents are composed.
- **Packaging and delivery** — how a standard becomes a skill or binder entry is owned by Infrastructure (packaging) and Deployment (the weight gate and the pipeline to the marketplace).
- **Any individual standard** — each lives with its owning component.

## Carries to other components

**To Documentation Methodology:** the Contents/Summary edge — Contents maps what is where to judge relevance, Summary gives what the document establishes. Their edges need to stay distinct. Flagged as a common issue for standards authors; the edge definition is document-structure grammar.

---

Version note: v1 — initial design from the standards design session, 2026-09-10.
