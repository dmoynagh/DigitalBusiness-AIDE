> identity: Build_Brief@v4 | doctype: brief | updated: 2026-09-17

# Build — Brief

## Purpose

Build is the transition to execution. When something has been defined — in design or elsewhere — Build produces the outcome by creating and modifying files against a target, and returns the result to its caller for acceptance.

## Objectives

1. Provide a common build mechanism applicable across all build targets, from software development to documentation persistence to framework payload authoring.
2. Support composable, reusable build standards that carry target-specific conventions without restating them per task.
3. Define the contract between Build and its caller — what rides in a build request and what comes back — so that Orchestration can carry it as opaque payload.
4. Implement verification by behaviour as Build's own contribution to the assurance requirement.
5. Support a caller-defined spectrum of instruction specificity and decision scope, so the same mechanism serves prescriptive and intent-level work.

## Scope and boundaries

**In scope:**

- The build mechanism — caller, instruction, decision scope, sign-off, return.
- Build standards — composable documents carrying the how for a build domain, authored on the existing Standards methodology.
- Profiles — structural containers naming an ordered stack of build standards for a target.
- The build act — the common spine: instruction crosses, agent discovers, edits, records, returns.
- Build's contribution to the assurance requirement — implementing Assurance's goals by behaviour.
- The known build activities: software development (.NET focus initially), document persistence, framework payload outputs (authoring standards and tools into their accepted form), framework utility outputs.

**Out of scope:**

- Design specification (Project Design).
- Transport and dispatch to AI platforms (Orchestration — one channel Build can use, not the only one).
- Deployment channel and delivery plumbing (Infrastructure / Deployment).
- Verification and assurance conventions (Assurance — sets goals, approaches and expectations; Build identifies where they apply and implements by behaviour).
- Documentation folder structure (cross-cutting — leaning to design project, possibly global; Build consumes it).

**Linked build outcome:** Build's channel-agnostic contract (what a build package contains and what comes back) unblocks Orchestration's build-delegation use case (use case 2), which needs Build's payload shape to carry as opaque dispatch.

## Requirements

No requirements beyond those implied by the objectives. The design must support the full instruction-specificity spectrum (prescriptive to intent-level) and hold across the known build activities without target-specific assumptions in the mechanism itself.

## Definition of done

1. Build's purpose, model and boundaries are defined at overview level.
2. The build mechanism is specified — caller, instruction, decision scope, sign-off, return.
3. Build standards and profile composition are defined.
4. Build's contribution to the assurance requirement is stated.
5. The contract Orchestration consumes (the shape of a build task and a build return) is defined.
6. Terminology is locked.

## Considerations

- The build mechanism must hold for targets not yet defined. The model should support extension without disproportionate cost now.
- FUP is Build scope (document persistence). Whether Build absorbs FUP immediately or claims it as scope with a working mechanism is an open sequencing question.
- Build standards are authored on the same methodology as ordinary Standards but subgrouped as "build standards" for delineation. The exact relationship to the Standards component's authoring rules is a detail question for the design, not the brief.
- A note to carry to Assurance: consider whether verification and validation should be elevated to its own area within Assurance, with stated expectations on components — raised from this Build session.

## Charter alignment

Build sits under the Work role. It directly serves O1 (trust and integrity) through its verification-by-behaviour commitment — build conventions make execution verifiable and outcomes traceable. It contributes to O2 (a coordinated framework) by unifying build activities under one mechanism with composable standards rather than accumulating per-target ad-hoc approaches. It serves O3 (the delivery path for business practices) by carrying business conventions in reusable build standards delivered through the framework. It contributes to O6 (reduce burden on the human) by carrying conventions that the AI applies without restating them per task.

---

Version note: v2 — cross-review remediation. F1: Requirements section added. F2: Charter alignment corrected against Core_Charter_v1 (O2 and O3 were misattributed). 2026-09-17. Replaces v1.

Version note: v3 — cross-review round 2. F8: scope corrected to platform-neutral output (Build authors accepted standards/tools, Infrastructure transforms to delivery format). F14: remaining "build channel" → "build domain". 2026-09-17. Replaces v2.

Version note: v4 — cross-review round 3. F8: Objective 1 corrected — "framework output packaging" replaced with platform-neutral authoring language. 2026-09-17. Replaces v3.
