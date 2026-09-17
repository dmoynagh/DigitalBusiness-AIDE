> identity: Build_Overview@v6 | doctype: overview | updated: 2026-09-17

# Build — Overview

A project-scale snapshot of Build. Statements, not explanation — each is a recall handle; detail lives in the design. Read this to place anything about Build without re-reading the documentation set.

## Purpose

Build is the transition to execution — taking defined work and producing the outcome by creating and modifying files against a target, then returning the result for acceptance. A behavioural component: it defines conventions applied by following them, not machinery.

## The model, in one paragraph

A caller sends a build package — instruction, decision scope, profile reference, definition of done, and (where applicable) working target, intermediate-exchange support, transaction model, review requirement and work-level declaration. Build executes within its granted scope, applying build standards composed into a profile for the target. Build returns the result — confirmed, needs information, raises an issue, failed, or done with deviation — with an account of what was done. The model scales from a single-line file operation to a multi-stage coordinated build without changing shape; only the density of the package and which conventions carried by the profile's build standards activate change.

## Key mechanisms

- **The build mechanism** — caller, package, execution, return. The generic framework applying to every build, regardless of target.
- **Build standards and profiles** — composable, target-specific conventions authored on the Standards methodology; a profile names and orders a stack of them.
- **The review activation model** — dual-sourced (caller and profile-composed build standards), work-level-driven. Pre- and post-execution review points, activated proportionally to consequence and complexity.
- **The proactive feedback obligation** — surfacing implications, disproportionate cost, and potential design-review situations, unprompted.

## Behavioural obligations

- **Escalation boundary** — build owns how; the caller owns what and why. Unclear which side it's on → return.
- **Cost-and-complexity flag** — surfaced when real cost materially exceeds the specification's apparent assumption. Default is proceed.
- **Proactive feedback** — implications, cost signals and design-review triggers surfaced unprompted, not just on request.
- **Learnings routing** — specification learnings return to the caller; technique learnings stay in build.
- **Design must not overreach into build** — the caller specifies what; build owns how, even sharing a session.

## Assurance conventions consumed

Conformance checking, verification of inspectable facts, assumptions and gap-fill disclosure, confidence signalling, and the standing active-identification obligation. Detective conventions carry the most weight at build — the specification exists; the question is whether build honours it.

**Default autonomy tier: Collaborative.** Build acts within its granted scope and returns for sign-off. A caller or the build standards in the profile may raise it to Autonomous, but only with explicit human authorisation — never granted by the profile itself.

## Boundaries

Build does not own:

- **Design specification** — Project Design.
- **Transport and dispatch** — Orchestration (the default channel for AI-agent dispatch, not the only one).
- **Deployment channel** — Infrastructure / Deployment.
- **Assurance methodology** — Assurance (Build implements its goals by behaviour).
- **Documentation folder structure** — cross-cutting, consumed not owned.

Review, collaboration and investigation are cross-cutting concerns Build consumes at its review points — it does not own their methodology.

## Known build activities

Software development (.NET), document persistence (FUP), framework payload outputs (standards and tools into their accepted form; Infrastructure transforms to delivery format, Deployment delivers), framework utility outputs.

## Open items

FUP absorption timing. Documentation folder structure ownership. Work-scope structure. Assurance V&V carry note.

## Document set

Brief v4, Design v8, Decisions v8 (D1–D34), Overview v6. The first build standard is deferred until the Build design has been exercised and its conventions are stable enough to standardise.

---

Version note: v2 — cross-review remediation. F4: build package elements updated to seven. F5: return states corrected to PD Standard's settled model. F14: "build domain" terminology, packaging boundary corrected. 2026-09-17. Replaces v1.

Version note: v3 — cross-review round 2. F4: package elements updated to nine. F8: framework payload output corrected to platform-neutral. F10: stale "until it has a consumer" replaced with sequencing rationale. 2026-09-17. Replaces v2.

Version note: v4 — cross-review round 3. F4: model paragraph updated — working target now conditional. 2026-09-17. Replaces v3.

Version note: v5 — cross-review round 4. F6 terminology: "caller and profile" corrected to "caller and profile-composed build standards." 2026-09-17. Replaces v4.

Version note: v6 — cross-review round 5. F15: autonomy and remaining shorthand corrected — profile references now structural-only throughout. 2026-09-17. Replaces v5.
