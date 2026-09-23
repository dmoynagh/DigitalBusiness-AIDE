> identity: Capabilities_Decisions@v3 | doctype: decisions | updated: 2026-09-24

# Capabilities — Decisions

## D1 — Capability extended to all four types

The old model used "capability" for standards and tools only — in-session things loaded into the AI. Utilities were explicitly "NOT a capability." That distinction no longer holds. All four types extend the development environment, all are designed, built, and deployed, and all need a shared development methodology. The word covers the full set. The in-session/out-of-session distinction becomes a property within capability, not a boundary around the term.

This resolves the earlier overview statement "Capabilities is a category not a parent" — it is now a component with a purpose: owning the base development methodology the four types consume.

## D2 — Two properties distinguish the four types

Execution context (in-session vs out-of-session) and direction of service (serves sessions vs serves the corpus) are the two orthogonal properties. One property alone would conflate types — services and utilities both run out-of-session but serve different things. The two properties produce three distinct groups; Standards and Tools share the same cell (both in-session, both session-serving) and are separated by the invocability test owned by Tools. Each group's boundary tests are owned by the relevant type component, not by Capabilities.

## D3 — Five lifecycle phases, authoring conditional

*Status: revised by D9 (six phases — review added). The conditional author phase stands.*

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

This means each type's development standard declares `uses` on Build and Infrastructure where the dependency creates a change-management obligation. *Corrected by D11 — `uses` points at standards only, and neither Build nor Infrastructure currently publishes one.*

## D8 — Infrastructure's role acknowledged as evolving

Infrastructure currently holds both delivery machinery and individual utility instances. This design does not resolve Infrastructure's scope — it acknowledges the evolution. As the Utilities component takes over utility methodology, individual utilities may move to their owning components. Infrastructure's durable contribution is the delivery and operational machinery. The resolution comes from Infrastructure's own design pass, not from Capabilities.

---

Version note: v1-draft1 — initial decisions from the design session. D1–D8. 2026-09-23.

Version note: v1 — cross-review remediation. F1: D2 overclaim corrected. F7: D7 corrected — development standards declare `uses`, not designs. 2026-09-23. Replaces v1-draft1.

## D9 — Review is a lifecycle phase for every type

Review was implicit — "cross-review accepted" appeared only as a build precondition in the type standards, with no guidance on how. It is now an explicit phase between author (or design) and build, applying to all four types. Every type checks its specification before build: a developer self-check (the acceptance test for standards and tools) and cross-review by a separate AI directed to find defects against the design's definition of done. Out-of-session types additionally test the built deliverable against its design during build. The lifecycle becomes six phases, and the development-standard structure gains a review section (seven sections).

The alternative — leaving review to Working Practices alone — was rejected because a developer following a development standard needs to know that review is required, what it checks, and what to test against. Working Practices still owns the cross-review process; the development standards carry what a developer needs to perform it.

## D10 — Definition of done framed around the development cycle; the design must produce the standard

The definition of done for Capabilities and every type component is framed around what a developer can do: classify, design, author, review, build, deploy, and consume. Each type's design must hold everything its standard carries, plus reasoning and explanation, so the standard can be produced from the design alone (with declared dependencies). This applies Standards D24–D25 across the Capabilities model. A review found the Capabilities design missing the standard's applicability statement and acceptance test; both were added.

## D11 — `uses` declares standards only; Build and Infrastructure referenced in prose

D7 said development standards declare `uses` on Build and Infrastructure. That cannot be done: `uses` declares dependencies on standards, and neither Build (first standard deferred, Build D32) nor Infrastructure (the MCP delivery model is a reference document, not a standard — see Document Management D18) currently publishes one. No development standard has done it. Development standards therefore reference Build's and Infrastructure's documents in prose. When either publishes a standard that a development standard depends on, the `uses` declaration is added then.

## D12 — Direction of service does not imply lifecycle

The design described corpus-serving capabilities as acting on files "then exit". Services cross-review finding F9 removed the equivalent wording from Services because a persistent corpus-serving process (a watcher, an indexer) would be excluded for no type-level reason. The Capabilities taxonomy is corrected to match: direction of service is about what the work serves, not whether the process terminates.

---

Version note: v2 — D9 (review as a lifecycle phase), D10 (definition of done and design-produces-standard), D11 (D7 corrected — `uses` is standards-only), D12 (direction of service does not imply lifecycle), D13 (no `uses` on the Capabilities Development Standard). 2026-09-23. Replaces v1.

## D13 — The Capabilities Development Standard declares no `uses`

The standard previously declared `uses` on the Standards Authoring Standard, which has since been deleted — a stale dependency. Replacing it with the Standards Development Standard would create a cycle, because the Standards Development Standard uses this one. Nothing in the Capabilities Development Standard depends on the standards authoring rules at the moment of application: it defines the taxonomy, lifecycle and structure the type standards extend. It is therefore a foundation-tier standard with no declared dependencies. That it was itself authored under the Standards rules is a property of how it was made, not a dependency of its consumers.

## D14 — The base standard names the four type standards

A developer reading the Capabilities Development Standard could learn that each type has its own development standard but not which one or where it is — the acceptance test asks them to locate it. The base standard now carries a table mapping each capability type to its development standard's identity and file location. The table is a pointer in prose, not a `uses` declaration: the type standards depend on this base, and a reverse declaration would create the cycle D13 avoids. The cost is that the table must be updated when a type standard is versioned.

---

Version note: v3 — D3 marked as revised by D9. D14 (the base standard names the four type standards). 2026-09-24. Replaces v2.
