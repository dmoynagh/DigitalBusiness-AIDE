Working Practices | brief | WP_Brief@v1 | 2026-09-15

# Working Practices — Brief

## Purpose

Define the operational conventions, behaviours, and working methods that govern how work is conducted — across any phase, any surface, and any kind of work.

Working Practices is the umbrella for action and behaviour. Phase-specific methods (the design method, the build method) are owned by their phase component; WP owns what they all consume. WP may grow into a container with child components as the design reveals natural divisions.

## Objectives

**O1. Universal conventions.** Establish the working conventions that apply regardless of phase or surface — session management, file handling, content delivery. The test: if it changes when you switch from design to build, it isn't WP's.

**O2. Capture-and-place.** The AI is responsible for organising and allocating everything of value from a session to its correct home — design documents, decisions, knowledge, open items, working documents, or WIP. Nothing of value gets lost; everything has a home. The AI recommends where it's confident, asks where it's not, and summarises allocations so wrong calls get caught.

**O3. Work lifecycle.** Define how work is tracked, progresses, and completes — work items, their fates, pending content, definition of done. A defined model, scalable in implementation.

**O4. Assurance collaboration.** Working Practices provides the operational substrate that the Assurance component's conventions run on. WP defines how work is conducted; Assurance defines the conventions that build trust and ensure outcomes are visible. Both evolve as the collaboration learns.

**O5. Reduce human burden.** The AI carries the operational load — capture, sweep, consolidation, allocation. The human directs; the framework does the bookkeeping. Directly serves charter objective O6.

## Scope

WP owns generic operating behaviour and live state — the middle placement band. The test: if it doesn't change when you switch from design to build, it's probably WP's.

The current five-part structure (FileOps, WorkManagement, Capture, ContentDelivery, HumanAI) was input; the design pass reshaped it. Human-AI Collaboration became the Assurance component. Capture and Organisation dissolved upward to WP component level. WorkManagement merged into Working State. The design determines what remains.

## Boundaries

**WP does not own:**

- The design method — Project Design
- How code is structured — Build
- Document structure, the definition contract, the split test as a rule — Documentation Methodology
- The component model, ownership rules, framework-wide requirements (no-knowledge-lost, definition-of-done, assurance) — Core
- Universal reasoning premises — Principles
- The work register — Project Design (fills a design-specific temporal gap)
- Trust and outcome conventions, the human working model, verification behaviours, drift detection — Assurance
- Framework governance rules including P6 — Core

**WP owns:**

- Capture-and-place as the primary operational mechanism
- Workflow commands (the concept, definition methodology, reference guide)
- WIP model and conventions
- Work items, work plan, open items, pending content
- The development lifecycle concept (phases and modes)
- Process document types (working document, report, resource)
- File operation conventions (parked for review)
- The binder concept (why and how, not the doctype)
- The overview-first working discipline (generic — consumed by Assurance and PD)

## Definition of done

- The model is stated — what WP contains and how its parts relate.
- Each settled item from the accumulated pile is placed, deferred, or retired with reasoning.
- Doctypes and block types defined with owners.
- Design document and decisions document authored.
- Standard authored, cross-reviewed, and live in a session.
- Old-material pass complete (WP1–WP13 reconciled).

---

Version note: v1 — initial brief from the WP design pass. 2026-09-15.
