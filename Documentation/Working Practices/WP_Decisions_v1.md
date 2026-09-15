> identity: WP_Decisions@v1 | doctype: decisions | updated: 2026-09-15

# Working Practices — Decisions

## Summary

Reasoning and resolutions from the Working Practices design pass. Sixteen decisions covering the extraction of Assurance as a new component, structural reorganisation of WP, component-level concern placement, and dispositions of accumulated items from other component passes.

---

## D1. Assurance extracted as a new top-level component

The Human-AI Collaboration area — human working model, tiering, confidence, verification behaviours, drift detection, anomalies channel, assumptions/gap-fill report — was originally planned as an area within WP. During the design pass it became clear this content directly delivers charter objective O1 (trust and integrity), which is the framework's primary reason for existing. Burying it as an area inside WP would subordinate the most important thing AIDE does.

Assurance is a cross-cutting concern — every element in the framework contributes to it. The brief-required gate, cross-review, operations test, acceptance test, strength model, capture-and-place, the design-check skill, definition of done, Principles P7/P8/P10 all contribute to assurance.

Resolved as both: a component in the Guidance role owning its specific mechanisms (human working model, detection conventions), and a framework-wide requirement in Core ("every component contributes to assurance"). Same pattern as no-knowledge-lost and definition-of-done.

Component count goes from 13 to 14. Justified against F8 (component count for a solo developer) because this component directly delivers the framework's primary objective.

Assurance gets its own design pass after WP's is complete.

## D2. Capture and Organisation dissolved

Capture and Organisation's core content — capture-and-place rules, session-end allocation — moved to WP component level as standing obligations that govern everything WP does. They are not inside any area because they are the operational discipline that all areas consume. The process document types (working document, report, resource) moved to Working State, where they sit alongside WIP and working documents as the containers content moves through.

No remaining purpose justified the area as a separate grouping.

## D3. Work Lifecycle merged into Working State

Work Lifecycle (work items, definition of done, pending content, development lifecycle phases/modes) and Working State (WIP, working documents, open items) were initially proposed as separate areas. The split was artificial — lifecycle and containers are two descriptions of the same flow. A work item's five fates route into Working State containers. The pending content rule is a WIP convention. Open items appear in both. The two areas could not stand alone.

Merged under Working State. The name covers both: the state of the work includes what exists and where it lives.

## D4. Definition of done elevated to Core framework-wide requirement

Definition of done started as a PD brief element, was elevated to "principle level" importance, then became a generic block type owned by WP. During this pass it was recognised as too important to be buried inside an area — it's a cross-cutting principle used across the whole framework. Tested against Principles (portability test: it passes, but it's a process discipline not a reasoning premise, and the F12 pattern resists adding to the nine premises) and Core (framework-wide requirement pattern: same shape as no-knowledge-lost — Core states the requirement and invariant, owning component provides the mechanism).

Resolved: Core states the framework-wide requirement. The invariant is testable-or-assessable. WP owns the block type definition — the mechanism consumers use. PD fills it in the brief, component passes fill it in their definitions of done, Build checks against it.

## D5. P6 moved to Core, not WP

P6 (information holder decides the boundary) was moved from Principles to WP during the Principles design pass as AIDE-context behaviour, not a universal premise. During this pass it was tested against WP's purpose and recognised as a framework governance rule — when a boundary question arises, the component that holds the information decides. That's a component model concern, not a working practice. Core Design already has five ownership rules; P6 is a sixth.

## D6. Guidance Profiles deferred

The Add/Refine/Override delta model is well designed but has no demonstrated consumer for a solo developer. No organisation, group, or team profile layers exist. The design is preserved in Principles' decisions (D4, D5); it returns if multi-user profiles demonstrate need. Follows the no-consumer-no-rule bar.

## D7. Overview-first working behaviour — WP owns generic, PD consumes

PD Standard v4 already has the design-specific application. The broader discipline — staying at the overview level until it could drive excellent execution — applies beyond design to any work where there's a temptation to dive before the shape is clear. WP states the generic behaviour. PD's standard consumes it for design without change.

## D8. Verification behaviours — Assurance, not WP

Verification behaviours (verify inspectable facts, distinguish generated intent from applied state — consuming Principles P7 and P10) were placed in the Human-AI Collaboration area. When that area became the Assurance component, verification moved with it as detective-side conventions. They are about trust and visibility of reality, not about how work is conducted.

## D9. WIP as a defined model with three roles

WIP evolved organically but its three roles are distinct and deliberately designed: homeless shelter (temporary, nothing stays by default), persisted working memory (continuity across sessions), and transactional staging (pending content for masters). These roles were discussed extensively in earlier sessions and confirmed during this pass. The model includes multiple WIPs, WIP tracking via the project index, and visibility requirements.

## D10. Work plan as a block type in WIP

The work plan addresses a practical need: visibility of what's currently decided and in progress, without reading through multiple long documents. Supports named workstreams for parallel work. Maintained by the AI as part of capture-and-place. Lives in WIP as high-churn content.

Not project management — a todo list that scales. Formalised enough to have a known name and shape, light enough to be a WIP section.

## D11. Workflow commands replace session-transition commands

Session-transition commands (full stop, checkpoint-and-continue, flush without closing) were the first examples of a broader concept: named, invokable actions that trigger operational behaviours. The concept generalised to workflow commands — WP owns what a workflow command is and how new ones are defined; individual commands are defined by whatever owns the behaviour they trigger. A reference guide is a deployment output.

## D12. Proactive knowledge preservation as a capture-and-place obligation

The AI's duty to protect against knowledge loss from session mechanics (compaction risk, context weight, platform switching) is not a separate concept — it is the proactive face of capture-and-place. The AI doesn't just capture at session end; it actively guards throughout and pushes back when content at risk.

## D13. Capture and Organisation's process document types to Working State

The three process document types (working document, report, resource) are containers used during the working process. They sit naturally in Working State alongside WIP, working documents, and open items. Their ownership is unchanged: WP owns these types because they serve the working process; Documentation Methodology owns the doctype mechanics.

## D14. FileOps parked for review

FileOps has confirmed content from the 2026-09-10 session but its coherence as an area is under review. Analysis showed it is part genuine working practice (file delivery rules), part duplication of Core Structure decisions (design/output separation), and part Infrastructure utility concerns that moved here by subject affinity (git commit behaviour, FUP move action, utility designs). Whether FileOps earns its place, dissolves, or is redefined is deferred for a focused review.

## D15. WIP tracking via the project index

A register of active WIP documents prevents orphaned or neglected content. The natural home is the project's index document — it already indexes what a scope contains. Not a new mechanism; an expansion of the index's existing role.

## D16. Assurance as a framework-wide requirement in Core

Every component contributes to assurance — it is a cross-cutting concern, not contained within one component. Resolved the same way as no-knowledge-lost: a framework-wide requirement stated in Core that every component's design is tested against. The Assurance component owns its specific mechanisms; the framework-wide requirement is the lens every component is designed through.

---

Version note: v1 — initial decisions from the WP design pass. 2026-09-15.
