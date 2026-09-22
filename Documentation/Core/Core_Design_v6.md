> identity: Core_Design@v6 | doctype: design | updated: 2026-09-22

# Core — Design

## Summary

Core is the root entry to AIDE. It describes what AIDE is, defines the component model, states the requirements that govern every component, and maps the framework so that any reader — human or AI — can navigate from here to any part of it. Two design areas sit under Core: **Structure** (how documentation is organised) and **AIDEPrinciples** (AIDE-specific operating principles, strength model, aliases). Each has its own design and decisions documents.

---

## What AIDE is

AIDE makes the standards and behaviours that shape how AI works with you live in your sessions, on whatever surface is in use. Everything else in AIDE exists to produce, deliver and keep that content current.

It is a methodology-driven framework for a solo developer working with AI. It gives AI sessions consistent behaviour, accumulated knowledge, and standards defined by the owner — not by platform defaults.

The framework's founding rationale, objectives, and development principles are stated in the Core Charter — a development document that informs how AIDE is built, not how it is used. When an AIDE development decision is contested or unclear, the charter provides the reference point.

### Four roles

AIDE's components provide four kinds of value:

- **Foundation** — defines AIDE's own shape and the grammar everything is written in.
- **Guidance** — the premises, rules, standards and tools that shape how work is done.
- **Work** — how work progresses from intent through design and build to outcome.
- **Delivery** — how things move between boundaries, stay current, and reach sessions.

These are conceptual roles, not a hierarchy. A component contributes to a role based on the value it provides to the system. Some components contribute to more than one. The component map organises each component under its primary role. Where a component contributes to a second role, that is noted in its own design, not duplicated here.

---

## The component model

**Component.** A defined area of functionality with a declared purpose, scope, and ownership. It owns its own documents and decisions. It may produce capabilities but need not. It is the functional unit of AIDE, independent of where it physically lives.

**Capability.** An output that extends the development environment — a standard or a tool. The two capability kinds are defined by their respective components.

**Capabilities** is the organisational grouping that contains standards and tools. It is not a component. It earns no purpose line because every job it could claim is already owned by a component within it. If it later demonstrates a purpose of its own, it graduates under the demonstrated-need rule.

**Utility.** A third kind of output alongside standards and tools. A utility is infrastructure — a repeatable operational task (building a binder, deploying a file update package, cleaning up superseded versions). Utilities are not capabilities; they serve the framework's own operation rather than extending the development environment.

### Ownership rules

Six rules govern what lives where:

1. **Owner is whoever knows the most about it.** Ownership goes to the component with the deepest knowledge of the thing — block types, doctypes, workflow artefacts, boundary disputes.
2. **Documentation Methodology owns structure and mechanics, not content definitions.** It does not hold a registry of types belonging to other components. Only genuinely global types — used across many components where no single component knows the most — live there.
3. **Each component defines its own block types and doctypes.** Being written down as a document does not make something Documentation Methodology's business.
4. **A purpose line is a filter criterion, not a description.** Its job is to reject content. A good purpose line carries an outcome, a consumer, and a visible edge.
5. **Purpose and role first; everything must align to it.** If a piece of content cannot trace back to the component's purpose, it is scope creep.
6. **Information holder decides the boundary.** When a boundary question arises, the component that holds the information decides. This is a framework governance rule, not a working practice — it governs how components relate to each other.

### Component naming

Component names and aliases must be unique within the framework. Aliases are used as type-reference prefixes in the dot-qualified naming grammar. An alias resolves to exactly one component; where ambiguity exists, the full name is used. Aliases are declared in the component's index document.

---

## Framework-wide requirements

These bind all components. Each requirement is stated once here; the owning component holds the mechanism. No duplication of mechanism.

**Facilitate and extend.** AIDE exists to facilitate and extend, not to create friction or restrict. Methodology frameworks historically impose compliance overhead that discourages adoption; AIDE takes the opposite position — its value comes from making good practice easier, not from enforcing it. This is AIDE's own character, originating from the shorthand "facilitate, not constrain." The AIDEPrinciples design area states the principle and its design pattern — functionality activates from data, not from compliance. Owned by Core, delivered through the AIDE Principles standard.

**Component model.** Every component has a declared purpose, scope and ownership. The component, capability and utility definitions live here. Owned by Core.

**Platform neutrality.** Capabilities are defined platform-neutral — the what. Transformation into platform-specific delivery is Deployment's concern.

**Leanness.** What loads into a session must justify its weight. The Standards component owns the authoring guidance that enforces it.

**Design is the default.** A design almost always exists behind a standard. Authoring straight to standard is the exception, not the rule. Project Design owns the design method.

**No knowledge lost.** The framework captures and places everything of value. Working Practices owns capture-and-place; this is the fundamental rule.

**Entry-point completeness.** Core's design document contains a summary of every active component — its purpose and key boundaries — sufficient for navigation. Each component's design specification lives in its own folder.

**Definition of done.** Every component and every piece of work defines when it is done. The invariant: the completion bar must be testable or assessable. Working Practices owns the block type definition — the mechanism consumers use. Consumers fill it with their own content.

**Assurance.** Every component contributes to assurance — justified confidence that the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur. The Assurance component owns the specific conventions and detection mechanisms; this requirement is the lens every component is designed through.

---

## The component map

Fifteen active components, organised by primary role. Each component's entry point is its index document (`_index.md`) in its own folder. The folder path follows the component name.

### Foundation

| Component | Purpose | Key boundaries |
|---|---|---|
| Core | AIDE's self-description, component model, framework-wide requirements, and entry-point map. | Not a catchall — deliberate and first-class. Owns Structure and AIDEPrinciples as design areas. |
| Documentation Methodology | Define how documents are structured and created — the generic mechanics. | Owns the grammar. Not a registry of types belonging to other components. |
| Messaging | Define the format, structure, and conventions for reliable communication across any boundary. | Owns the envelope and delivery conventions. Does not own the transport — messages travel by Orchestration or by manual copy-paste. |

### Guidance

| Component | Purpose | Key boundaries |
|---|---|---|
| Principles | Give any AI the durable, portable reasoning and premises to think and act well — independent of platform or methodology. | Portability is the defining test. Includes verification as a premise and the base human-side behavioural premises. |
| Standards | Make sure standards are applied, honoured and kept current across the environment. | Owns the definition of a standard and the authoring guidance including leanness. Does not define individual standards — those are owned by their consuming component. |
| Tools | Encapsulate a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. | Owns the definition of a tool. Does not own individual tools — those are owned by their consuming component. |
| Assurance | Build justified trust in AI-assisted work by defining and evolving the conventions, behaviours, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur. | Cross-cutting — every component contributes. Owns the human working model, verification behaviours, drift detection, anomalies channel, learning loop capture conventions. Does not own the substrate (WP), the premises (Principles), or the pattern analysis (Improvement). |
| Improvement | Iterative improvement of the framework and working practices from accumulated learning, regardless of source (human or AI). Identified but not yet scoped. | Owns the periodic pattern analysis of the learnings queue, escalation decisions, and the reviewer. Does not own the capture conventions (Assurance) or the scheduling mechanism (Orchestration). |

### Work

| Component | Purpose | Key boundaries |
|---|---|---|
| Working Practices | Define the operational conventions, behaviours, and working methods that govern how work is conducted — across any phase, any surface, and any kind of work. | Umbrella for action and behaviour. At component level: capture-and-place, operational tools, file delivery, overview-first discipline. Two areas: Working State (WIP, work items, boards, completion) and Content Delivery (binder, session content). Does not own trust conventions or the human working model — Assurance. |
| Project Design | Produce the design specification. | One scalable architecture. Owns both ends of the design-build loop. |
| Build | Take the design specification and execute it — produce the outcome, report what was done. | Does not design — receives the specification from its caller, most often Project Design but any caller including another build. Creates from the spec, thinking not transcribing. Likely an umbrella with different build paths. |

### Delivery

| Component | Purpose | Key boundaries |
|---|---|---|
| Orchestration | Coordinate invocation across AI execution targets — accept caller-owned work, resolve model selection through Core-owned Framework Resources, invoke target adapters, correlate dispatch with transport outcome, and return the response. | Owns the crossing: dispatch correlation, invocation, transport outcome, target adapters, model-level resolution. Does not own the task, verification policy, routing decision, or semantic meaning of the response. Likely an umbrella with areas or parts. |
| Migration | Keep things current when something they depend on changes — collate, distribute and execute change actions. | Does not detect changes — detection varies by consumer. The mechanism is generic. |
| Deployment | Get the publishable capabilities live in a session, on whatever surface is in use. | Does not define capabilities — receives them from their owning components. Simple pipeline: build, push, reload. |
| Infrastructure | Methodological infrastructure — CLI, deployment utilities, settings merge. | Serves the framework's own operation. Does not own design documents or standards. |

### Held — resolved by demonstrated need

| Candidate | Resolution trigger |
|---|---|
| Tags | Reappears if the design shows labelling duplication across components. |
| Scope | Reappears if runtime applicability needs a shared definition. |

### Deferred

| Concern | Trigger |
|---|---|
| Environment and platform | Multi-platform deployment or a need to track deployment state. |

---

## Design areas

**Structure** (prefix `Core_Structure_`). How AIDE documentation is physically organised. Physical folders are the structure; no logical overlay. Path authority lives in the document header. `_index.md` is a generic folder metadata file — not AIDE-specific, governed by Declaration opt-in like any other document — that identifies document sources for discovery when its role is Documentation Solution or Documentation Project. Role vocabulary provides shared vocabulary. The three-tier file model governs what the binder includes. One `_archived` folder at the documentation root holds files that are no longer active but worth keeping — retired references, completed reviews, outdated knowledge. The underscore prefix removes it from binder scope while keeping files in the repo and searchable. Git is the version history. The `_superseded` folder pattern is dropped — when a new version lands, the old version is deleted from the working tree. Rollback means checking out the previous version from git. Design and decisions documents exist. Produces the Core Structure Standard for deployment.

**AIDEPrinciples** (prefix `Core_AIDEPrinciples_`). The operating principles specific to AIDE as a framework — facilitate and extend, opt-in for benefit, the strength model, and aliases. Distinct from the Principles component, which owns universal portable premises governed by the portability test. Design and decisions documents exist. Produces a standard for deployment.

---

## Boundaries

**Core does not own:**

- Individual component designs — each component owns its own folder
- Universal premises — the Principles component, governed by the portability test
- The grammar of how documents are written — Documentation Methodology
- The design method — Project Design
- How standards are authored or enforced — Standards
- The rebuild process — a project, not a permanent part of the framework

**Core owns:**

- The charter
- The component model and its definitions
- The framework-wide requirements
- The component map
- The index doctype
- The four roles
- Structure and AIDEPrinciples as design areas
- Component alias uniqueness

---

Version note: v4 — Orchestration component map entry corrected to match accepted Orchestration_Design_v5 (D3/D29 proposed Core wording). WP component map entry boundaries updated to match WP_Design_v6 (umbrella structure confirmed, boards replace work plan per D21). 2026-09-17. Replaces v3.

Version note: v5 — Build component map entry generalised to any-caller per Build_Decisions_v8 D3 (cross-review carry F3). 2026-09-17. Replaces v4.

Version note: v6 — Structure design area description updated for the retirement of the Core Schema Standard (absorbed into Core_Structure_Standard@v1) and the "AIDE document" reframe: `_index.md` is generic folder metadata, and container labels are now role vocabulary. Notes that Structure now produces a standard for deployment. 2026-09-22. Replaces v5.
