> identity: Build_Brief@v1 | doctype: brief | updated: 2026-09-16

# Build — Brief

## Purpose

Build is the transition to execution. When something has been defined — in design or elsewhere — Build produces the outcome by creating and modifying files against a target, and returns the result to its caller for acceptance.

## Objectives

1. Provide a common build mechanism applicable across all build targets, from software development to documentation persistence to framework output packaging.
2. Support composable, reusable build standards that carry target-specific conventions without restating them per task.
3. Define the contract between Build and its caller — what rides in a build request and what comes back — so that Orchestration can carry it as opaque payload.
4. Implement verification by behaviour as Build's own contribution to the assurance requirement.
5. Support a caller-defined spectrum of instruction specificity and decision scope, so the same mechanism serves prescriptive and intent-level work.

## Scope and boundaries

**In scope:**

- The build mechanism — caller, instruction, decision scope, sign-off, return.
- Build standards — composable documents carrying the how for a build channel, authored on the existing Standards methodology.
- Profiles — structural containers naming an ordered stack of build standards for a target.
- The build act — the common spine: instruction crosses, agent discovers, edits, records, returns.
- Build's contribution to the assurance requirement — implementing Assurance's goals by behaviour.
- The known build activities: software development (.NET focus initially), document persistence, framework payload outputs (standards and tools into skills and packages), framework utility outputs.

**Out of scope:**

- Design specification (Project Design).
- Transport and dispatch to AI platforms (Orchestration — one channel Build can use, not the only one).
- Deployment channel and delivery plumbing (Infrastructure / Deployment).
- Verification and assurance conventions (Assurance — sets goals, approaches and expectations; Build identifies where they apply and implements by behaviour).
- Documentation folder structure (cross-cutting — leaning to design project, possibly global; Build consumes it).

**Linked build outcome:** Build's channel-agnostic contract (what a build package contains and what comes back) unblocks Orchestration's build-delegation use case (use case 2), which needs Build's payload shape to carry as opaque dispatch.

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

Build sits under the Work role. It directly serves O2 (consistent, high-quality outcomes) by making execution repeatable and convention-driven rather than interpretive. It contributes to O1 (trust and integrity) through its verification-by-behaviour commitment, and to O3 (efficiency) by carrying conventions in reusable build standards rather than restating them per task.

---

Version note: v1 — produced from the Build design-pass voice session 2026-09-16. Overview-level brief; detail deferred to the design.
