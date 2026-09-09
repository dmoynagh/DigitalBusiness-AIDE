# AIDE Rebuild — Overview

Version 1. 2026-09-08.

---

## Purpose

AIDE makes the standards and behaviours that shape how AI works with you live in your sessions, on whatever surface is in use. Everything else in AIDE exists to produce, deliver and keep that content current.

---

## The model — what kind of thing AIDE is

AIDE is a set of components. Each component is a defined area of functionality with a declared purpose, scope and ownership. A component owns its own documents and decisions.

Some components produce capabilities — standards and tools that are delivered into the AI environment. A capability is a component whose purpose is providing a mechanism by which functionality is delivered to the AI environment. Producing capabilities is not a requirement; a component that exists solely to organise and govern a body of work is still a component.

There are two types of capability:

- A **standard** defines rules, expectations, guidance and context that shape decisions and behaviour while work is being done. It can include procedures, but those procedures are guidance within the operating context rather than a separately invoked operation.

- A **tool** encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It normally defines its inputs, preconditions, ordered procedure, decision points, escalation conditions, outputs, and failure behaviour.

Standards and tools are defined platform-neutral — the what — and transformed into platform-specific delivery. On Claude, that means a skill in a plugin.

A third kind of repeatable operation exists outside the AI session: a **utility** encapsulates a repeatable operation that acts on the corpus, environment or infrastructure from outside the session. It does not load into session context or shape in-session decisions. Examples: the binder-builder, the file-update packager, version-cleanup scripts. Utilities are not capabilities.

**Leanness is a governing principle.** Everything deployable — standards, tools, anything that loads into a session — is written as lean as possible without compromising its purpose or outcomes. The cost of length is baked into authoring from the start: the standards for building standards and building tools carry the discriminating guidance on how to write lean. A weight gate at deployment checks the combined load of a plugin and flags if the total is getting too big.

---

## The components

Twelve components, listed by the work they do.

### Foundations

**Principles** gives any AI the durable, portable reasoning and premises to think and act well, independent of platform or methodology. Portability is the defining test — if a candidate principle only makes sense inside AIDE, it is not a principle. Verification lives here as a premise: where possible, build in mechanical verification so claims and outcomes can be checked against inspectable evidence. The base premises about how the system behaves on the human side also live here.

**Working Practices** owns the conventions and behaviours for how an AI and user actually work together across surfaces — work in progress, handoffs, preservation of active state. The human working model — tiering, per-item confidence, the assumptions and gap-fill report, drift detection, definition-of-done at commission time — is a standard within Working Practices. The per-user override model is a future direction only; single user for now.

**Documentation Methodology** owns how documents are structured and created — the generic mechanics. Naming, document types, lifecycle, the master-versus-generated distinction, the doctype and block model, format, versioning, language rules. It is the grammar everything else is written in.

### The design-and-build path

**Project Design** produces the design specification. One scalable architecture from simple single-document to complex multi-document structures. It owns both ends of the design-build loop: the handoff to Build and the return and reconciliation. It defines its own block types (objectives, requirements, considerations) and document types.

**Build** takes the design specification and executes it — produces the outcome and reports what was done. It creates from the specification, thinking rather than transcribing, and owns how the code is structured. Build is likely an umbrella with different build paths depending on what is being produced — code projects, standards, tools — each potentially its own path.

### Capabilities

**Standards** makes sure standards are applied, honoured and kept current across the environment. As a capability, it owns what a standard is and how one is authored — including the authoring guidance that enforces leanness.

**Tools** owns what a tool is — the definition, shape and authoring guidance. Individual tools are owned by the component that needs them.

### Shared mechanisms

**Migration** owns the generic mechanism for keeping things current when something they depend on changes. It collates and distributes change actions (the migration record, accumulation, shipping the fix with the thing it serves) and executes them (the three-part task shape, atomic transitions, user prompt, stamp management). Detection is the one part that varies by consumer; each consumer defines its own. Documents against standards is the primary consumer, but it also covers skills, bootstraps, binder definitions, project knowledge, code project structure, and platform configuration.

**Messaging** is a general-purpose transport component — a standard for creating and carrying messages that any component or logic can use to move something across a boundary. Cross-process, cross-session, cross-AI, cross-project. It owns the envelope and the delivery convention. It does not care who uses it or why.

### Collaboration

**External AI** owns how and when another AI is brought into your work. The former separate components — Review, Research, Parallel Solutioning and Consultation — are modes within it. Mode is the contract (what role the external AI plays); interaction pattern (one-shot, multi-round, conversational) is a separate axis. External AI consumes Messaging as its transport.

### Delivery

**Deployment** takes the publishable capabilities, builds them into a plugin, pushes it to the git marketplace, and the account reloads. Deploy as each component completes, so the framework is tested in use. This is also where the deployable-length weight gate lives, flagging if the combined load of a plugin is getting too big.

### Residual

**Core** is deferred by design and resolved last. It is defined by whatever shared requirements are left that no other component naturally owns. It holds the existing settled work on the Index, Domain and Bootstrap — those designs carry forward. Core's shape is not forced until everything else has declared what it needs.

---

## How the components wire together

Intent enters through Project Design, which produces a specification and hands it to Build. Build creates the outcome and returns it; Project Design reconciles.

Principles and Working Practices are loaded into every session and shape all of it. Documentation Methodology is the grammar everything is written in.

Standards and Tools define what capabilities are and how they are authored. Migration keeps documents and other consumers current when standards change. Messaging carries structured communication across any boundary.

External AI can be invoked at any point — review, research, parallel solutioning, consultation — consuming Messaging as its transport.

Deployment takes capabilities live. Core holds what has no other home.

---

## What every component consumes

Each component uses the shared constructs already settled in the rebuild:

- documents, decisions, knowledge and WIP (the doctype and block model)
- binders (the generated consumption artefact)
- versioning
- the work item and definition of done
- principles and working practices

These are the common grammar. A component does not re-derive them.

---

## The build sequence

Standards and Tools are worked first — they define what capabilities are and how they are authored, which is prerequisite to all other component output. Their standards also carry the leanness guidance.

Then a simple Deployment component, so capabilities can be shipped.

Then deploy-and-test as each subsequent component completes its design. The sequence after Deployment follows the per-component method in the rebuild guide: purpose and objectives; component overview; Check 1; design; Check 2; author the standard; deploy; old-material pass.

---

## Outside AIDE

Which binders exist and what they contain; project repositories and their lifecycles; platform behaviour, which is verified not assumed.

---

## Open items

These are recorded explicitly as unresolved. Each has a stated trigger for resolution.

**Component boundaries and structure.** What makes something a component, where the boundaries fall, and whether components can contain sub-components. At least Working Practices and Build show signs of wanting nesting. The three held candidates also feed into this discussion. Trigger: resolve before or during the Standards pass, because the definition of a component is foundational.

**Utilities and infrastructure placement.** Utilities are defined but where they and infrastructure sit organisationally in the framework is not settled — they are currently a tack-on. Trigger: resolve when a utility needs to be built or documented and there is nowhere to put it.

**The Capability-as-deployable-unit question.** The old model had an extensive Capability Definition contract — elements, releases, production checkpoints, build target profiles. In the simplified model, does anything still own what a capability looks like when packaged? Or is that just Deployment's concern? Trigger: resolve during the Standards or Deployment pass.

**Whether domains exist as a concept.** The old model said development domains consume AIDE; they are not components of it. Whether that concept carries forward has no demonstrated need yet. Trigger: resolve if and when the relationship between AIDE and consuming projects needs to be defined.

---

## Held and deferred

**Tags, Scope and Dependencies** are held, not resolved. They earned their place in the old model by removing duplication of similar behaviour across multiple components. They come back only if the new design shows the same duplication reappearing. Resolution is by demonstrated need during component design, not before.

**Environment and platform concerns** are deferred. The old Core design held runtime knowledge of surfaces, channels, models, access references and deployed state. Single platform for now; no requirement yet to track this. Trigger: multi-platform deployment or a need to track deployment state.
