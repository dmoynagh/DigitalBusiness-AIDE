# Capabilities Standards — Design

> **Version 3** (2026-08-29). **§10 open items closed.** The "Audience per weight" and "Tone
> enforcement" bullets are removed from what this design deliberately leaves open — both are
> now resolved (`D39`, audience carried by scope; `D40`, tone enforcement belongs in review) and
> moved to "Resolved since v1." Rest of document unchanged from v2.
>
> This document is the current position, stated in present tense. For how positions were reached,
> see `Capabilities_Decisions` v6, `D10`–`D16`, `D18`–`D19`, `D26`–`D27`, `D39`–`D40`.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## §1 — Scope of this document

This design covers the model for how standards are structured, weighted, produced, and published.
It applies to every standard produced under the Capabilities model, regardless of the domain
that authors it.

**In scope:** the structure of a standard, the weight system governing its contents, the output
model (what a design produces), the scope model (how a standard declares what it reaches),
and conflict handling at build and publish time.

**Out of scope:** runtime application of standards — how a session resolves conflicts between
standards, honours weights during execution, and handles deviation. Those rules belong in a
separately published standard scoped to AIDE contexts, produced by this subtopic.

---

## §2 — Role and purpose of a standard

A standard exists to add value to the development process — not to enforce. It acts as a guide
offering suggestions and direction. It supplies context, perspective, and reasoning so an AI
session can exercise judgment rather than follow steps blindly.

A standard carries rules, but rules work by benefit — follow them to get the benefit; don't
follow them and you don't get it. Mandates are framed consequentially ("if it isn't in this
format, it can't be consumed by X") rather than authoritatively ("you must"). A standard carries
outcomes, targets, and criteria — what must be met for something to happen.

**The framing distinction is critical.** It is not that standards are mostly guidance and
occasionally enforce. A standard may legitimately be almost entirely mandatory — volume of
enforcement is not the point. The point is the framing, because framing changes the outcome.
When enforcement becomes the primary lens, standards drift draconian and controlling. The same
requirement, expressed as facilitation, lands better and is more likely to be followed. Same
outcome, two different approaches — the facilitating one works better.

Standards are the broader artefact; tools cover specific actions. A standard may describe a
procedure; it may not define an invokable action (`D24`, standard-tool boundary). Where a
standard describes a procedure that later becomes a tool, the standard's procedure section is
replaced by a pointer — the tool becomes the single source.

**Role statement.** A standard provides guides, rules, advice and support, focused on adding
value and facilitating effective work. Enforcement may be one of its roles but is never its
primary lens; it operates through facilitation, clarity and support.

---

## §3 — Weight system

Four tiers, collectively called "weight" — as in "what weight does this carry." Each addressable
unit likely to be chunked carries a weight marker.

### Requirement

Must be met, not open to judgment. Framed consequentially: it doesn't work or can't be used
otherwise.

*Example:* a tool definition must carry a specified information structure — without it, the
publisher cannot extract the definition.

### Expectation

The default position. Departure is permitted but must be declared — visibly, in the moment.
Stronger than advice, not absolute.

*Example:* keep documents brief, but not at the cost of clarity or completeness. A departure is
stated where it happens: "this section is deliberately extended because the reasoning requires
it."

### Guidance

A default or best practice. Departure is permitted; you own the consequences and management of
your alternative. No obligation to announce.

*Example:* use present tense in design documents. A session that uses past tense for a specific
section handles whatever confusion that creates, without needing to declare the departure.

### Context

Information, perspective, reasoning. No obligation at all. Exists so the session understands the
territory and exercises better judgment.

**Key delineation.** Expectation is about visibility — declare your deviation. Guidance is about
ownership — handle what you've taken on. Both permit departure but ask different things when you
do.

---

## §4 — Weight cascade

Three levels of application:

### Document level

Optional. Declared in the header block as the default for everything below. Useful for setting
the tone; redundant as a mechanism since every chunk states its own.

### Section / category level

Every addressable unit carries its own weight marker. Always stated, even where it matches the
document default. This matters for verbatim extraction — an extracted section that lost its
weight would be actively misleading.

### Statement level

Used only where a statement genuinely departs from its section's weight. Bracketed weight at the
start of the statement.

**Cascade rule.** Document default overridden by section, overridden by statement. Nearest
declaration wins. An unmarked chunk is a defect to fix.

**The chunkability test.** What constitutes an "addressable unit" is determined by chunkability:
if it can be retrieved, extracted, or read in isolation, it carries its own weight marker.

**Design versus rendering.** The design attaches a weight to each unit as a semantic fact. How
granularly that weight gets rendered into the published artefact is builder logic — declared in
the Standards Standard and free to vary per platform as experience shows what each actually
needs. This keeps the design stable while the rendering stays tunable; a rendering lesson does
not force a design revision.

---

## §5 — Weight justification

Every unit, including those marked Requirement, states its value and consequence. The weight says
how binding it is, not that it skips justifying itself.

This keeps the facilitation framing intact at the strongest tier. A Requirement that says "you
must" without saying why has abandoned the framing — the justification is what distinguishes a
consequentially framed rule from an authoritatively framed one.

---

## §6 — Output model

A design, optionally plus platform-specific design elements, produces:

### Standard

A standard per supported platform — terse, complete, nothing superfluous, weights explicit. The
machine/AI-focused artefact: brief, defined, accurate, containing nothing superfluous, ensuring
everything needed is included.

### Guide (optional)

A guide — discursive, rich, explanatory. The human-readable artefact. Not produced by default;
declared in the brief for the individual standard when wanted.

Both are generated from one design, so they cannot disagree about substance.

**Specification is dropped as a type.** The standard now holds the precise-and-binding ground
specification occupied, and a third type invites overlap nobody can adjudicate.

**Platform targeting.** Which platforms a standard targets defaults to the supported-platform
list held in the Standards Standard, overridable per standard down to a single platform —
declared in the standard's brief.

**Platform-specific design.** Whether a platform-specific design is needed is derivable from the
design itself.

**Sibling outputs.** A single design may emit one or more standards and one or more tools as
sibling outputs. All derive from the same design; none is authoring the other's content. Platform
variance in the output set — whether a platform needs two tools where another needs one — is a
platform design concern (`D24`, standard-tool boundary).

---

## §7 — Scope

How a standard declares what it reaches, and how a session knows a standard applies here. The
scope model is shared with tools (`D18`, two-layer scope model) and defined fully in
`Capabilities_Tools_Design` v1 §2. This section states the model as it applies to standards.

### Mechanical scope

Machine-evaluable, no reasoning required. A hard filter based on tags: platform, side (design
or build), file type, domain membership, document type, or any locally-owned tag. Either it
matches or it doesn't.

Tags are locally owned — whoever applies a tag defines it. There is no central registry.
Matching is set logic: any-of, all-of, none-of. A capability's scope declaration referencing
another domain's tags is a dependency on that domain's vocabulary; tag renames are breaking
changes and migrate through versioning.

### Context scope

Descriptive, reasoned. Prose conditions, contexts, or situations that a session reads and
judges. States conditions to be evaluated, not descriptions to be interpreted: "applies when
the work crosses a topic boundary" rather than "this is about cross-topic work."

Mechanical scope is closed (finite vocabulary of tags); context scope is open (prose, not
constrained).

### Composition and default

Mechanical scope gates whether the standard is even a candidate; context scope decides whether
it applies to what's actually happening. A standard with no scope declaration applies nowhere.

**Context scope and reporting.** If a session decides a standard's context scope does not apply,
that is a judgment worth surfacing — quietly declining to apply a standard is the silent failure
the corpus keeps running into.

---

## §8 — Conflict handling

Two levels:

### Build (internal coherence)

Does this assembled artefact — own design plus platform design — contradict itself? The
publisher checks. Contradictions are escalated rather than resolved.

### Publish (external coherence)

Does this artefact contradict what's already deployed in the target repository? The publisher
scans the repository it's pushing to and checks. Contradictions are escalated rather than
resolved.

### Resolution hierarchy

When conflict is encountered at runtime (note: the runtime rules themselves belong in the
separately published AIDE-scoped standard, but the hierarchy is defined here as the model):

1. **Append where possible** — standards add to each other.
2. **Higher weight wins** — Requirement over Expectation over Guidance over Context.
3. **Equal weight in genuine opposition** — escalate loudly, take direction. Do not resolve
   silently.

This hierarchy applies across authority sources generally, not only standard-versus-standard.

**Human instruction sits above a Requirement**, but not silently. The session states what the
Requirement was, what following it would have delivered, and what not following it costs — then
proceeds as directed. Where the Requirement is structural (machine-readability), the framing
changes because the fact does: "this won't be consumable by X" rather than "this is inadvisable."
The deviation is recorded where the work is recorded.

---

## §9 — Standards Standard and AIDE standard split

Two standards govern different concerns:

**The Standards Standard** governs producing a standard — authoring, weights, publishing,
versioning. It is this subtopic's primary output.

**A separately published standard, scoped to AIDE contexts,** governs operating under standards
at runtime — how a session resolves conflict, honours weights, handles deviation. This subtopic
produces it; it deploys alongside the Standards Standard (same plugin, same package) but is its
own artefact with its own scope declaration.

This replaces the earlier standard-block delivery mechanism (`D14`, superseded by `D26`). The
content is unchanged; the vehicle changes from embedded block to standalone standard. The AIDE
standard stays limited to what AIDE itself owns.

---

## §10 — What this design deliberately leaves open

- **How versioning works** — what triggers a version, what a version means. Pulled to `Q7`
  (versioning, currency, and drift) for examination under one lens with tools.
- **How publishing works** — authored content → deployed artefact.
- **How currency works** — how a consumer knows what they have is current. Part of `Q7`.

### Resolved since v1

- **How scope works** — resolved in §7 above (`D18`, `D19`).
- **Actions boundary** — resolved by `D24` (standard-tool boundary). A standard may describe a
  procedure; it may not define an invokable action.
- **How migration works** — migration applies to standards only (`D24` context — tools excluded
  as no case exists). Migration content and mechanism are part of `Q7`.
- **Audience per weight** — resolved by `D39` (audience carried by scope, no per-unit marker). A
  standard needing both AI and human audiences is likely two standards.
- **Tone enforcement** — resolved by `D40` (tone enforcement belongs in review). The Standards
  Standard's review profile checks weight justification (`§5` above); no mechanical publish gate.

---

**Depends on:** `Capabilities_Design` v1, `Capabilities_Decisions` v6 (`D10`–`D16`,
`D18`–`D19`, `D26`–`D27`, `D39`–`D40`).

**References:** `Capabilities_Standards_Brief` v1, `Capabilities_Tools_Design` v1,
`Capabilities_Brief` v1.

**Methodology:** v17
