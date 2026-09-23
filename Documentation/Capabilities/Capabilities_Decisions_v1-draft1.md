> identity: Capabilities_Decisions@v1-draft1 | doctype: decisions | updated: 2026-09-23

# Capabilities — Decisions

## D1 — Capability extended to all four types

The old model used "capability" for standards and tools only — in-session things loaded into the AI. Utilities were explicitly "NOT a capability." That distinction no longer holds. All four types extend the development environment, all are designed, built, and deployed, and all need a shared development methodology. The word covers the full set. The in-session/out-of-session distinction becomes a property within capability, not a boundary around the term.

This resolves the earlier overview statement "Capabilities is a category not a parent" — it is now a component with a purpose: owning the base development methodology the four types consume.

## D2 — Two properties distinguish the four types

Execution context (in-session vs out-of-session) and direction of service (serves sessions vs serves the corpus) are the two orthogonal properties. One property alone would conflate types — services and utilities both run out-of-session but serve different things. The two properties produce three distinct groups; Standards and Tools share the same cell (both in-session, both session-serving) and are separated by the invocability test owned by Tools. Each group's boundary tests are owned by the relevant type component, not by Capabilities.

## D3 — Five lifecycle phases, authoring conditional

The five phases (design, author, build, deploy, consumption) apply to all four types, but authoring is conditional. Standards and tools produce an authored doc that serves as both specification and deployment payload. Services and utilities have no authored doc — the design doc is the specification.

The alternative — forcing an "author" phase on all four types by stretching the word to mean "finalise the design to spec quality" — was rejected because it muddies a real distinction. For standards and tools, authoring is a distinct creative act (producing a lean, carry-tested document from a richer design). For services and utilities, no such act exists. The design does more work instead.

## D4 — Build specifics owned by type components as build standards

Each type component owns build standards for its build domain, composed into profiles on top of Build's generic mechanism. This is Build's own model (build standards, build domains, profiles) — not a new concept. The capability development standards are where those build standards live.

The alternative — putting all build specifics in Build or in Infrastructure — was rejected because it violates what-knows-most-about-it. Build knows the mechanism; the type component knows how to build its type.

## D5 — Development standard supersedes authoring standard

For Standards and Tools, the development standard replaces the existing authoring standard with broader scope. The authoring content is embedded unchanged; build, deploy, and consumption sections are added. This is an expansion, not a rewrite — the settled authoring rules, concerns, and acceptance tests carry forward.

For Services and Utilities, the development standard is authored fresh — no prior standard to supersede.

## D6 — Capabilities is a component in the Guidance role

Capabilities earns component status by owning a methodology with four demonstrated consumers. It sits in the Guidance role alongside Standards, Tools, Services, and Utilities. It is the base; they extend it.

The alternative — putting this in Core — was rejected because Core owns structural concerns (what AIDE is, what a component is), not methodological concerns (how to develop capabilities). This is Guidance work.

## D7 — Relationship to Build and Infrastructure by consumption, not restatement

The development lifecycle references Build and Infrastructure without restating their content. Build owns the generic build mechanism and the build-standard/profile model. Infrastructure owns the delivery pipeline. Each type component states how it uses these — what enters build and what gets delivered — without duplicating the source.

This means each type's development standard declares `uses` on Build and Infrastructure where the dependency creates a change-management obligation.

## D8 — Infrastructure's role acknowledged as evolving

Infrastructure currently holds both delivery machinery and individual utility instances. This design does not resolve Infrastructure's scope — it acknowledges the evolution. As the Utilities component takes over utility methodology, individual utilities may move to their owning components. Infrastructure's durable contribution is the delivery and operational machinery. The resolution comes from Infrastructure's own design pass, not from Capabilities.

---

Version note: v1-draft1 — initial decisions from the design session. D1–D8. 2026-09-23.

Version note: v1 — cross-review remediation. F1: D2 overclaim corrected. F7: D7 corrected — development standards declare `uses`, not designs. 2026-09-23. Replaces v1-draft1.
