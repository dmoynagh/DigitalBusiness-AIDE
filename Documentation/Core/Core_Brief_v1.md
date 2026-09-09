# Core — Brief

Version 1. 2026-09-08.

---

## Purpose

Core is the root entry to AIDE. It describes what AIDE is, how it is structured, and the framework-wide requirements and concepts that govern all components. A reader starting here should be able to understand AIDE's shape and navigate to any component from it.

---

## What AIDE is

AIDE makes the standards and behaviours that shape how AI works with you live in your sessions, on whatever surface is in use. Everything else in AIDE exists to produce, deliver and keep that content current.

It is a methodology-driven framework for a solo developer working with AI. It gives AI sessions consistent behaviour, accumulated knowledge, and standards defined by the owner — not by platform defaults.

---

## Objectives

O1. Provide a single, maintained description of what AIDE is and how it works — the framework's own self-description.

O2. Define the component model: what a component is, what a capability is, and how components relate to each other.

O3. Hold the framework-wide requirements that govern all components and cannot be owned by any single one.

O4. Serve as the entry point — a reader (human or AI) arriving at AIDE for the first time navigates from here.

---

## Requirements

R1. **Facilitate, not constrain.** AIDE exists to facilitate and empower, not to constrain or be a source of friction. This is AIDE's own character — distinct from the universal principles, which hold outside AIDE. Every framework-wide decision is tested against it.

R2. **Component model.** Every component has a declared purpose, scope and ownership. A component owns its own documents and decisions. The component definition, the capability definition (standards and tools), and the utility definition all live here.

R3. **Platform neutrality.** Capabilities are defined platform-neutral — the what — and transformed into platform-specific delivery. On Claude, that means skills in a plugin.

R4. **Leanness.** What loads into a session must justify its weight. Leanness is a governing principle at the framework level; the Standards component owns the authoring guidance that enforces it.

R5. **Design is the default.** A design almost always exists behind a standard. Authoring straight to standard is the exception, not the rule.

R6. **No knowledge lost.** The framework captures and places everything of value. This is the fundamental rule.

R7. **Entry-point completeness.** Core's design document must contain a summary of every active component — its purpose and key boundaries — sufficient for navigation. The design specification of each component lives in its own folder.

---

## Considerations

C1. Core absorbs the "facilitate not constrain" position that was deferred pending a home. It is now settled here.

C2. Core replaces the previous definition ("hold whatever shared requirements have no natural home elsewhere"). The new purpose is deliberate and first-class, not residual.

C3. The relationship between Core and Principles needs to stay clean. Principles owns universal premises (portability test). Core owns AIDE-specific character and governance. "Facilitate not constrain" fails the portability test — it is about AIDE, not about all AI work — and therefore lives here, not in Principles.

C4. Some requirements above (leanness, design-is-the-default, no-knowledge-lost) are also expressed or implied elsewhere. Core holds the framework-wide statement; the owning component holds the mechanism. No duplication of mechanism.

C5. The three held candidates (Tags, Scope, Dependencies) and the deferred concerns (environment, platform, domains) remain open and are not resolved by this brief.

---

## Scope and boundaries

**In scope:**
- The framework's self-description and conceptual model
- Framework-wide requirements and considerations
- The component, capability and utility definitions
- The component map — purpose lines and navigation to each component's own material
- AIDE's character statement (facilitate not constrain)

**Out of scope:**
- Individual component designs — each component owns its own folder
- Principles — universal premises live there, governed by the portability test
- Documentation Methodology — the grammar of how documents are written
- The rebuild process itself — that is a project, not a permanent part of the framework

---

## Target outcome

A reader arriving at AIDE — whether a new AI session, a reviewing AI, or the human owner returning after time away — can read Core and understand: what AIDE is, what a component is, what the framework expects of every component, and where to find any specific component's design. Core is the map and the constitution.

---

## Definition of done

1. Core's design document describes the component model, capability and utility definitions, and framework-wide requirements
2. Core's design document contains a current summary of every active component with purpose and key boundaries
3. "Facilitate not constrain" is placed and stated with its rationale
4. The distinction from Principles (portability test) is explicit
5. A reader unfamiliar with AIDE can navigate from Core to any component
