> identity: Build_Decisions@v6 | doctype: decisions | updated: 2026-09-17

# Build — Decisions

## Summary

Reasoning and resolutions from the Build design pass. Decisions D1–D12 from the voice session (2026-09-16); D13–D20 from the corpus-driven specification pass; D24–D32 from the legacy-review pass and open-question resolutions; D33–D34 from the cross-review remediation pass (2026-09-17).

---

## D1. The file-change principle as spine

When files get created or modified, that is Build. Adopted as a strong convention, not a blanket rule. This unifies what might otherwise fragment into separate paths — applying a specification to a .NET codebase and persisting documentation changes are the same act against different targets. The principle identifies the spine without claiming every file operation is formally a build.

## D2. One act, not separate paths

Build is one common act — instruction crosses, agent discovers, edits, records, returns — with target-specific conventions layered on via build standards. The alternative was four or more discrete build paths with separate methodologies. Rejected because the act is the same; what differs is the verification and convention, which belongs in build standards for each build domain. The common act is the build mechanism; the target contributes its specifics through build standards composed into a profile.

**Caution recorded:** this holds for current scope but may not fit all future build domains. The model should support extension without disproportionate cost now — "a hammer that can grow to be a sledgehammer."

## D3. Caller, not design

Build returns to whatever initiated it — the caller — not specifically to design. A build request can be spawned by another build in a chain. Design is just the most common originator. This generalises the model and matches Orchestration's language, where the caller owns the request and the meaning of the result.

Consequence: reconciliation is the caller's act, not inherently design's. When the caller is design, the caller closes the register. When the caller is another build, that build handles the outcome.

## D4. Default sign-off convention

By default, a build does not sign off its own work — it returns to the caller for acceptance. But the caller may grant authority to self-accept. This is a default convention, not a rule: the safe state holds when nothing is said, with the caller's grant able to lift it. Same pattern as the default-Required strength model in Standards.

## D5. Decision scope is caller-defined

The latitude and authority a build has is defined by the caller, not by Build. The caller sets how much decision scope the build has — from "take care of it, don't come back to me" to "apply only these specific changes." The governing backstop: a build may act within its granted scope as long as it does not structurally change the fundamental design. Beyond that, it returns.

This is the escalation boundary from Project Design's commitment-and-return loop, now stated from Build's side as a caller-granted scope rather than a Build-owned rule.

## D6. Build standards as the term

The composable documents carrying target-specific build conventions are called **build standards**. "Build instructions" was considered and rejected — it collides with the caller's per-task instruction, blurring the standing-reusable-how (standards) and the task-specific-what (instructions). Build standards are authored on the same Standards methodology and delivered the same way, but subgrouped for delineation.

## D7. Profile as structural container

A **profile** is a structural container that names and orders a set of build standards into a stack. It holds nothing of its own. Profiles can be named presets (saved for reuse) or defined inline, and the two combine. Profiles compose on each other — an "AIDE framework documentation update" inherits "documentation update" and adds the delta.

## D8. Working target as scope-of-work concept

The scope of work a build operates on is expressed as a **working target** — the folder, subtree or scope the agent is authorised to touch. Not mandatory on every build, but common enough to warrant its own recognised structure. Its shape depends on the build target: code has repos and projects; documentation has documentation roots and work folders. Branching and git instructions belong in this structure where relevant.

## D9. Documentation root replaces "doc repo"

The contained root of documentation for a project or area is a **documentation root** — a folder, not a repo. "Doc repo" conflated the file-management system with the documentation container within it. A repo can hold multiple documentation roots; the root is the right level to name.

## D10. Assurance boundary — goals and expectations, not just guidance

Assurance sets goals, approaches, objectives and requirements/expectations for integrity. It operates on a spectrum: for some areas it provides methodology and guidance; for others, guidance and expectations alone. Build identifies where each integrity objective can be applied in Build's context and how — for example, Assurance states that components should where realistically possible use verification to ensure what is asked is what is delivered; Build identifies where that applies (test results, schema checks, etc.) and implements it by behaviour.

Assurance also owns shared assurance components — the framework tasks queue (name pending) and learning patterns — which Build consumes where relevant.

**Carry note for Assurance:** consider whether verification and validation should be elevated to its own area within Assurance, with stated expectations on components — currently only a detective behaviour. Raised from this session.

## D11. Design-build separation resolved as a light convention

The seed material's design-build separation principle — build outputs reside outside the design area — resolved as a general good-practice convention: keep documentation separate from build outputs, the same way you wouldn't nest code libraries under your documentation folder. This is a property of the target (documentation says "keep me separate"), not a Build rule. Hold lightly, state as convention, don't build machinery for it.

## D12. Documentation folder structure is cross-cutting

The documentation folder structure — roots, underscore folders, binder storage, work folders and their nesting — is a cross-cutting concern consumed by Build but not owned by it. Leaning toward design project as the home, but it may be more global, reaching equally across design, build, deployment and tooling. Build needs to locate the structural root and its working target within it; the structure is declared once, somewhere central.

---

## D13. Build package and build return are mechanisms, not doctypes

Following Project Design's settled decision to withdraw the work-package doctype. The build package and the build return are format-free transition artefacts whose shape varies with context — a one-line message for trivial work, a full structured package for complex work. Sufficiency is the requirement, not format.

This means Build defines no new doctypes or block types. It consumes the definition-of-done generic block (Working Practices) and the standards methodology for build standards.

**Why not fix the format:** build targets vary (code, documents, framework outputs), build channels vary (Orchestration dispatch, direct chat, Messaging), and the instruction spectrum runs from prescriptive to intent-level. A fixed format would constrain most of these combinations without adding value. The sufficiency test — does it carry everything the build side needs to act? — is format-independent and does not rot.

## D14. Build package contents derived from PD's handoff

The build package composes nine elements. Four — instruction, decision scope, profile reference, definition of done — are always relevant. The remaining five — working target, intermediate-exchange support, transaction model, review requirement and work-level declaration — are present where applicable. The first five were surfaced in the initial design session; intermediate exchanges (D21) and the transaction model (D23) were added as the design developed; review requirement and work-level declaration were added to make explicit what the review activation model (D26, D27) already implied the package must carry. They are Build's resolution of PD's sufficiency contract. PD specifies a format-free handoff with a sufficiency floor and ceiling; these nine elements are the semantic fields Build identifies as the content that satisfies that contract.

The ceiling rule (from PD's Standard) applies equally: do not re-supply generic execution-platform knowledge the build environment already provides. The profile already carries the standing conventions; the package carries only what is specific to this task.

## D15. Orchestration is the default channel, not the only one

Build's contract is channel-agnostic. Orchestration is the most common channel and the default where a build dispatches to an AI agent on another platform. But direct chat (same-session builds), Messaging's envelope, and copy-paste are all legitimate channels depending on context. The build package defines what crosses; the channel carries it unchanged.

This keeps Build decoupled from Orchestration's transport concerns and avoids requiring Orchestration for same-session work that doesn't need it.

## D16. Build standards follow the Standards methodology

Build standards are authored on the same Standards methodology — same schema, same eight authoring rules, same strength model, delivered through the ordinary Standards delivery model — triggered skills, binder content, or project context. They are subgrouped as "build standards" for delineation, not forked into a separate authoring approach.

**Why not a separate methodology:** Standards already solved the authoring problem. The eight rules (carry test, no-consumer-no-rule, leanness, discriminating guidance, strength assignment, self-containment, applicability scope, name-your-principles) apply identically to build conventions. Forking would duplicate work and create divergence risk for no demonstrated benefit.

## D17. PD carries placed as behavioural obligations

Three obligations carried from Project Design's commitment-and-return loop are placed in Build's design as its own behavioural section:

1. **Escalation boundary recognition** — build must recognise when it holds a what/why question rather than a how question.
2. **Cost-and-complexity flag** — build must judge when cost materially exceeds the specification's apparent assumption and surface it.
3. **Learnings routing** — learnings about the specification pass back; learnings about build technique stay.

These were stated in PD as obligations placed on Build but not designed there. They are now designed here, stated from Build's side.

Additionally, "design must not overreach into build" is placed as a Build boundary: the caller specifies what, build owns how, even when they share a session.

## D18. Assurance conventions consumed by Build

Build implements four Assurance conventions by behaviour:

1. **Conformance checking** — delivered work compared against governing specification.
2. **Verification of inspectable facts** — verify rather than assert where checking is available.
3. **Assumptions and gap-fill disclosure** — disclose what build filled in vs what was specified.
4. **Confidence signalling** — signal confidence on material judgements using the plain-English vocabulary.

Plus the standing **active identification** obligation — Build identifies opportunities where assurance could be strengthened within its domain.

These are Build's contribution to the assurance requirement, implementing Assurance's goals by behaviour. The specific verification checks a build domain needs live in its build standards — so the .NET build standard might specify test coverage expectations, while the documentation-update build standard might specify schema validation. The mechanism (verify by behaviour) is common; the content varies by target.

## D19. Assurance lifecycle weighting consumed

Assurance's design decision (Assurance D10) states that at build, detective conventions carry more weight than proactive conventions — the specification exists and the question is whether build honours it. Build consumes this: its verification behaviours and conformance checking are the primary assurance concern during a build act, while proactive conventions (autonomy tiering, confidence signalling) remain active but carry less weight.

## D20. Build does not define new block types or doctypes

Build consumes the definition-of-done generic block (Working Practices, testable-or-assessable invariant) and fills its content. Build standards are standards (Standards methodology). Profiles are structural containers. The build package and build return are mechanisms, not doctypes (D13).

No new block types or doctypes needed. This is consistent with Build being a behavioural component — it defines conventions, not document structures.

## D21. Intermediate exchanges — mid-execution communication

Build is not strictly one-shot request-response. The build mechanism supports intermediate exchanges: a pause-and-resume within the build act where build pushes a question or decision point to its caller, gets a response, and continues. Distinct from the terminal return — the five return states remain completion states.

In interactive sessions this is just conversation. In orchestrated or unattended sessions the channel must relay the exchange because the build executor has no UI — the caller provides the interaction surface. In chained builds, exchanges relay through each caller until a layer can answer.

The build package indicates whether the caller supports intermediate exchanges. Where not supported, build must proceed within its decision scope or return terminally.

**Dependency recorded:** this is a real requirement on Orchestration's transport, connecting to its explicitly deferred "stateful/multi-turn orchestration" and intermediate-progress protocol items. Build names the need; Orchestration decides when and how.

## D22. Caller cancellation

The caller may send a cancel request to a running build — not just answers to intermediate exchanges. How cancellation is handled depends on the transaction model in effect (D23). A cancelled build returns a terminal state with an account of what was done and what was not.

## D23. Transaction model — commit, rollback, partial completion

Build work may succeed in full, fail entirely, or land in between. The transaction model governs what happens to work already done on failure, cancellation or mid-execution issues.

Three concerns: commit granularity (all-at-once or incremental), rollback capability (can completed work be reversed?), and partial completion (does work succeed in part or only in full?).

**Who decides:** the caller (in the build package) or the build standards (in the profile), or both — caller overrides profile where they conflict. Different targets genuinely need different models: code refactoring may need atomic all-or-nothing; documentation batch updates may accept partial commits.

**Default:** commit on completion — work becomes permanent when the build returns confirmed; a failed or cancelled build leaves no permanent changes. Safe default; override must be explicit.

The guarantee is conditional on target capability. Where a target does not support staging or rollback, the profile or build package must reflect that constraint — a guarantee stronger than the target can deliver is a misconfiguration, not a Build obligation. Build's obligation is to honour the declared model and to account accurately for what was committed.

---

## D24. Scalability is a governing property of Build

The build package spectrum runs from a single-line file operation to a multi-stage coordinated build with review gates and decision paths. The model — caller, package, execution, return — holds at both ends without changing shape. What changes is the density of the package contents and which profile conventions activate.

This is more than an observation on the package format. It is a governing property: any mechanism or convention added to Build must hold at both ends of the spectrum. A convention that requires full structure for a file rename has failed; one that cannot support review gates on a complex build has equally failed.

## D25. Proactive feedback obligation

Build has a proactive obligation to surface implications, cost signals, and potential design-review situations to the caller — not just when hitting the escalation boundary or answering intermediate questions (D21), but whenever build observes something the caller would want to know.

This is broader than the cost-and-complexity flag (D17), which is about cost materially exceeding the specification's apparent assumption for the current build. The feedback obligation covers design-level observations: patterns suggesting the design should be revisited, disproportionate cost between the work and what it serves, and implications the caller may not have seen.

The caller decides what to do with the feedback. Build's job is to surface it.

## D26. Review activation is dual-sourced

Review within a build is activated from two directions: the caller specifies review requirements in the build package, and standing policy in the build standards the profile composes requires review for the applicable build domain. Both apply. The build standards in the profile set the minimum floor; the caller can raise the review level but not lower it below what the profile's standards require.

This matches the profile composition model (D7/D8) and the decision-scope model (D5) — the build standards in the profile carry standing conventions, the caller adds per-task specifics.

## D27. Work level determines review activation

The consequence and complexity of the work — its work level — drives which review behaviours apply and at what depth. A trivial file rename gets no review; a structural change to the framework gets mandatory pre- and post-execution review.

The work level is sourced from three inputs: the caller's declaration (in the build package), the standing policy in the build standards the profile composes (for the domain), and build's own assessment (what it discovers about the work during planning and execution). The highest applicable level governs.

The concept of "work level" is not exclusive to Build — it applies equally to design, deployment, research and other areas. Build implements the cross-cutting concept within its own context.

## D28. Review, collaboration and investigation are cross-cutting concerns consumed by Build

These capabilities are defined elsewhere — Assurance, Working Practices, or their own areas — and consumed by Build with Build-specific application. Build does not own review methodology. Build provides the review points (pre-execution and post-execution) and activates the cross-cutting capability according to its own policies, the work level, and the profile.

The same capabilities apply to design, deployment, research and other areas. Build defines how and when they apply within build execution; the capabilities themselves are defined by their owning components.

## D29. Post-build is the tail of execution, not a separate phase

The old design (PostBuild_Design_v3) separated post-build publication from build execution as a distinct phase with its own design document. In the new model, this separation is dissolved. Post-build actions — publication, file delivery, output landing — are the tail end of the execution sequence, after validation. The transaction model (D23) governs what commits when.

Deployment registry registration is Deployment scope. Coordinated release batches are a coordination concern owned by Orchestration or Deployment. Build's job ends when the output lands at the working target and the return crosses to the caller.

## D30. Profile storage follows Core's ownership model

Named profile presets are defined by Build (shape and composition rules) and stored with the owning target area — the area with the most knowledge of that target. Combined and applied at runtime.

Build owns the mechanism; the target area owns the instance. A documentation-update profile lives under the documentation methodology area; an AIDE framework build profile lives under the AIDE area. This follows Core's ownership model: each component defines its own types, and the component with the most knowledge of a concern owns it. Build defines the profile concept and its semantics; owning components define their own build standards because they hold the domain knowledge. The split matches doctype and block-type ownership — the defining component carries the definition, not a central registry. This avoids Build becoming a dumping ground for every target domain's configuration.

## D31. Build's default autonomy tier is collaborative

Assurance defines three tiers — directed, collaborative, autonomous — with the Autonomous tier requiring human authorisation. Build's default is collaborative: build acts within its scope, returns for sign-off (matching the default sign-off convention, D4). A caller can explicitly grant autonomous authority when warranted, with the explicit authorisation Assurance requires.

Directed would be too restrictive for normal builds; autonomous would require explicit human authorisation every time. Collaborative is the natural match for Build's default convention of returning to the caller for acceptance.

## D32. Build standard authoring deferred — sequencing, not absence of consumer

Document persistence is the most frequent current build activity and is a real consumer of Build conventions. The deferral is sequencing: the framework's build conventions are still maturing (this design pass is the first to define them), and authoring a standard against a model that is itself being established risks premature codification. The first build standard should be authored once the Build design has been exercised and its conventions are stable enough to standardise. The expectation that the framework's own build work will be the first standard authored remains directionally correct as the most likely trigger.

---

## D33. Work-level interim vocabulary

Build requires an orderable work-level concept for review activation. Until the cross-cutting model is defined, Build uses a four-level qualitative scale — trivial, routine, significant, high-consequence — with the ordering implied by that sequence and a highest-governs resolution rule across caller, profile and build assessment. This is a working definition, not a claim on the cross-cutting model.

## D34. Scalability operational semantics

At the small end of the build spectrum, most package elements are implicit — defaulting from the profile, the domain or the nature of the task. The package contract is the same at both ends; only the density changes. This is a design test: any convention added to Build must hold at both ends of the spectrum.

---

Version note: v4 — cross-review remediation. D14: element count corrected to seven, PD provenance restated as Build's resolution of PD's sufficiency contract (F4, F12). D23: transaction guarantee made conditional on target capability (F7). D30: incorrect DocMeth analogy removed, restated under Core ownership model (F13). D32: rationale corrected from "no consumer" to sequencing (F10). D33: work-level interim vocabulary (F6). D34: scalability operational semantics (F11). "Build channel" → "build domain" where applicable (F14). 2026-09-17. Replaces v3.

Version note: v5 — cross-review round 2. D14: element count updated to nine (four optional). D16: delivery model corrected to delivery-neutral. D2, D18: "channel" → "build domain". 2026-09-17. Replaces v4.

Version note: v6 — cross-review round 3. D14: working target reclassified as conditional (F4). D26, D27: "profile policy" corrected to "build standards in the profile" (F6). 2026-09-17. Replaces v5.
