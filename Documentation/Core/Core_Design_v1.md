> identity: Core_Design@v1 | doctype: design | updated: 2026-09-15

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

These are conceptual roles, not a hierarchy. A component contributes to a role based on the value it provides to the system. Some components contribute to more than one.

---

## The component model

**Component.** A defined area of functionality with a declared purpose, scope, and ownership. It owns its own documents and decisions. It may produce capabilities but need not. It is the functional unit of AIDE, independent of where it physically lives.

**Capabilities** covers standards and tools — the output definitions that extend the development environment. Capabilities is an organisational grouping, not a component. It earns no purpose line because every job it could claim is already owned by a component within it. If it later demonstrates a purpose of its own, it graduates under the demonstrated-need rule.

**Utility.** A third kind of output alongside standards and tools. A utility is infrastructure — a repeatable operational task (building a binder, deploying a file update package, cleaning up superseded versions). Utilities are not capabilities; they serve the framework's own operation rather than extending the development environment.

### Ownership rules

Five rules govern what lives where:

1. **Owner is whoever knows the most about it.** Ownership goes to the component with the deepest knowledge of the thing — block types, doctypes, workflow artefacts, boundary disputes.
2. **Documentation Methodology owns structure and mechanics, not content definitions.** It does not hold a registry of types belonging to other components. Only genuinely global types — used across many components where no single component knows the most — live there.
3. **Each component defines its own block types and doctypes.** Being written down as a document does not make something Documentation Methodology's business.
4. **A purpose line is a filter criterion, not a description.** Its job is to reject content. A good purpose line carries an outcome, a consumer, and a visible edge.
5. **Purpose and role first; everything must align to it.** If a piece of content cannot trace back to the component's purpose, it is scope creep.

### Component naming

Component names and aliases must be unique within the framework. Aliases are used as type-reference prefixes in the dot-qualified naming grammar. An alias resolves to exactly one component; where ambiguity exists, the full name is used. Aliases are declared in the component's index document.

---

## Framework-wide requirements

These bind all components. Each requirement is stated once here; the owning component holds the mechanism. No duplication of mechanism.

**Facilitate, not constrain.** AIDE exists to facilitate and empower, not to constrain or be a source of friction. This is AIDE's own character. The AIDEPrinciples design area states the principle and its design pattern — functionality activates from data, not from compliance. Owned by Core, delivered through the AIDE Principles standard.

**Component model.** Every component has a declared purpose, scope and ownership. The component, capability and utility definitions live here. Owned by Core.

**Platform neutrality.** Capabilities are defined platform-neutral — the what. Transformation into platform-specific delivery is Deployment's concern.

**Leanness.** What loads into a session must justify its weight. The Standards component owns the authoring guidance that enforces it.

**Design is the default.** A design almost always exists behind a standard. Authoring straight to standard is the exception, not the rule. Project Design owns the design method.

**No knowledge lost.** The framework captures and places everything of value. Working Practices owns capture-and-place; this is the fundamental rule.

**Entry-point completeness.** Core's design document contains a summary of every active component — its purpose and key boundaries — sufficient for navigation. Each component's design specification lives in its own folder.

---

## The component map

Twelve active components, organised by role.

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
| Standards | Make sure standards are applied, honoured and kept current across the environment. | Owns the definition of a standard and the authoring guidance including leanness. |
| Tools | Encapsulate a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. | Owns the definition of a tool. Individual tools are owned by their consuming component. |

### Work

| Component | Purpose | Key boundaries |
|---|---|---|
| Working Practices | Own the conventions and behaviours for how an AI and user actually work together across surfaces. | Includes the human working model. May grow into a container with sub-components. |
| Project Design | Produce the design specification. | One scalable architecture. Owns both ends of the design-build loop. |
| Build | Take the design specification and execute it — produce the outcome, report what was done. | Creates from the spec, thinking not transcribing. Owns how code is structured. Likely an umbrella with different build paths. |

### Delivery

| Component | Purpose | Key boundaries |
|---|---|---|
| Orchestration | Coordinate work across AI surfaces and platforms — the channels, communication mechanics, and coordination logic that allow multiple AI components to work together. | Owns transport, routing, work package structure, verification, and capability profiles. Does not own the work modes that consume it. Likely an umbrella with areas or parts. |
| Migration | Keep things current when something they depend on changes — collate, distribute and execute change actions. | Detection varies by consumer; the mechanism is generic. |
| Deployment | Get the publishable capabilities live in a session, on whatever surface is in use. | Simple pipeline: build, push, reload. Includes the deployable-length weight gate. |
| Infrastructure | Methodological infrastructure — CLI, deployment utilities, settings merge. | Serves the framework's own operation. Design documents and utility outputs are separate. |

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

**Structure** (prefix `Core_Structure_`). How AIDE documentation is physically and logically organised. Physical folders are the structure; no logical overlay. Path authority lives in the document header. The index document (`_index.md`) is the identity and entry point for each scope. Container labels provide shared vocabulary. The three-tier file model governs what the binder includes. Design and decisions documents exist.

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

Version note: v1 — initial design from the Core design pass. 2026-09-15.
