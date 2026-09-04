# Capabilities Tools — Design

> **Version 1** (2026-08-27). First issuance. Establishes the model for how tools are defined,
> structured, and published. Scope model (§2) is shared with Standards and defined here as the
> canonical location; `Capabilities_Standards_Design` v2 §7 references it.
>
> This document is the current position, stated in present tense. For how positions were reached,
> see `Capabilities_Decisions` v3, `D18`–`D25`.
>
> Created: 2026-08-27 | Last modified: 2026-08-27

---

## §1 — Role and purpose of a tool

A standard shapes what a session decides; a tool removes the need to decide. A standard exists
where judgment is needed; a tool where judgment adds nothing.

A tool's value comes from four properties: determinism (same action, same way, every time),
encapsulation (knowledge lives once, not re-derived per session), cost (expensive reasoning
becomes cheap invocation), and completeness (no forgotten step, gates built into the action).

A tool is a machine-facing artefact. It is not designed for human readability — it is designed
to provide an effective implementation of an action or task on an AI platform.

---

## §2 — Scope model (shared with Standards)

How a standard or tool declares what it reaches, and how a session knows it applies here. This
model applies equally to standards and tools (`D18`, two-layer scope model).

### Mechanical scope

Machine-evaluable, no reasoning required. A hard filter based on tags.

Things carry tags — a domain, a document type, a platform, a session. A capability declares a
tag expression. Matching is set logic: any-of, all-of, none-of. Nothing more elaborate.

**Tag ownership.** Whoever applies a tag defines it. There is no central registry. Consumers
reference tags they've looked up from the source that applies them. Collisions and duplications
are possible and accepted — cheaper than maintaining a registry.

**Dependency.** A scope declaration referencing another domain's tags is a dependency on that
domain's vocabulary. Tag renames are breaking changes and migrate through versioning (`D19`).

**Mechanical scope is closed** — a finite set of tags and values that can be checked without
reasoning.

### Context scope

Descriptive, reasoned. Prose conditions, contexts, or situations that a session reads and
judges. Describes conditions to be evaluated, not descriptions to be interpreted: "applies when
the work crosses a topic boundary" rather than "this is about cross-topic work." Anything
assessable and measurable is valid.

**Context scope is open** — prose, not constrained.

### Composition and default

Mechanical scope gates whether the capability is even a candidate. Context scope decides whether
it applies to what's actually happening. Mechanical first because it's free.

**No declaration means applies nowhere.** A capability with no scope declaration does not
default to universal applicability.

**Reporting on context scope.** If a session decides a capability's context scope does not
apply, that judgment is worth surfacing. Quietly declining to apply a standard or tool is the
silent failure the corpus keeps running into.

### Relationship to AIDE

AIDE defines a scope marker (`AIDE_Domain_Design` v1 §10): a standard or tool declares its
applicability as either always-on or AIDE-scoped. The two-layer scope model here is the
mechanism behind that marker. Mechanical scope carries the AIDE/universal distinction as a tag;
context scope carries any further conditions.

---

## §3 — Tool document structure

A tool document contains, in this order:

### Identity and invocation

The name the tool is called by, and any aliases.

### Trigger

What causes the tool to fire — explicit invocation, and any conditions where a session should
reach for it unprompted. This is where the scope declaration from §2 attaches.

### Purpose

One line, dense with the terms someone would use when looking for this tool. A retrieval and
selection surface — not for humans, for the session deciding whether this is the right tool.

### Inputs

What the tool needs. For each input:

- Whether it is required, optional, or has a default.
- **Input resolution** — where the value may come from: supplied explicitly, derived from the
  environment or context, or asked for.
- **Confirmation posture** — how confident the tool must be before proceeding on a derived
  (not explicitly supplied) value:
  - **Proceed on inference** — derive it, state what was used, carry on. Appropriate where
    the inference is safe and the cost of being wrong is low.
  - **Confirm inference** — derive it, but check with the user before acting. Appropriate
    where being wrong is expensive or hard to undo.

The confirmation posture is an authoring decision, not a runtime guess. The tool's author knows
whether getting the target wrong means a wasted second or a clobbered file, and encodes it once.

### Preconditions

What must be true before the tool runs. Checked and reported, not assumed.

### Procedure

The steps, ordered, unambiguous. This is the bulk of the document and the part that must be
exact.

### Decision points

Where the procedure branches, and what determines which branch. **Separated from the procedure
steps**, not buried in them. A step that hides a decision is where tools go wrong — the same
lesson as normative and advisory content being typographically identical in a standard. A tool's
honesty depends on its judgment calls being visible.

### Escalation conditions

What causes the tool to stop and hand back rather than proceed. Genuine judgment calls — two
things conflict, or the right course depends on a view nobody has taken. Never resolved by the
tool.

### Outputs and effects

What the tool produces, what it changes, what persists after it finishes.

### Reporting

What the tool says at each verbosity level, and what it always says regardless. Four verbosity
levels: minimal, summary, detailed, verbose. Default is summary — what was done, what changed,
what needs attention. Account-level user preference (`D21`, reporting obligation).

Verbosity governs narration, not the record. The full account is written wherever work is
recorded, regardless of verbosity. Failures and deviations surface regardless of setting.

### Failure handling

What happens on partial completion, and whether it is safe to re-run.

### Idempotency

Whether re-running is safe. Declared explicitly — a session needs this and cannot infer it.

---

## §4 — Interaction model

### Ask, infer, or escalate

Three postures when the tool needs information (`D22`):

- **Infer confidently and say so** — strong assumption available, low cost of being wrong.
- **Ask** — missing input the tool knows it needs. Ask once, well, gathering everything in one
  exchange. The full list is surfaced first so the user sees the shape of what's needed.
- **Escalate** — genuine judgment call. Hand back, do not resolve.

**Standing rule.** Never fail for want of information you could have asked for.

**Batched by default.** If the user prefers stepping through one by one, that is an interaction
preference the session honours. The default is batched because serial interrogation is the other
way tools become tedious. Interaction style (batched or sequential) is an account-level user
preference alongside verbosity (`Q8`, account preferences surface reach).

---

## §5 — Boundary with standards

A standard may describe a procedure. It may not define an invokable action. If you would say
"run X," X is a tool. If you would say "follow the approach in section Y," that is a standard
(`D24`, standard-tool boundary).

A single design describes a body of behaviour. Its outputs are whatever implements that
behaviour — one or more standards, one or more tools, siblings from a common source. Neither
sibling is authoring the other's content; both derive from the same design and therefore cannot
disagree.

A standard may legitimately describe a procedure that should be a tool but isn't yet. When the
tool is built, the standard's procedure section is replaced by a pointer.

---

## §6 — Weights

The weight system (`D10`) does not apply to tool documents. No current case exists for weight
markers in tool content. Parked, not rejected — revisit if real examples surface (`D23`).

---

## §7 — Migration

Migration applies to standards only. Tools are excluded — no current case exists. A tool is
transient: it does something, completes the task, and is done. Where a tool leaves durable
output, that output is governed by a standard which carries its own migration.

If a case for tool migration appears in future, the standards migration model can be applied
or adapted. The mechanism is available but not pre-built for tools.

---

## §8 — What this design deliberately leaves open

- **How versioning works for tools** — same mechanism as standards expected, but the asymmetry
  (no consumer-side declaration, version matters for reporting not compatibility) needs stating
  explicitly. Part of `Q7` (versioning, currency, and drift).
- **How publishing works for tools** — expected to be the same as standards with no differences
  worth stating. Not yet confirmed.
- **How currency works for tools** — the only check available is "what's installed versus what's
  published," since tools carry no consumer-side declaration to compare against. Part of `Q7`.
- **Account preferences model** — verbosity and interaction style identified; which surfaces
  they reach is unverified. See `Q8` (account preferences surface reach).

---

**Depends on:** `Capabilities_Design` v1, `Capabilities_Decisions` v3 (`D18`–`D25`).

**References:** `Capabilities_Tools_Brief` v1, `Capabilities_Standards_Design` v2 (shared
scope reference), `Capabilities_Brief` v1.

**Methodology:** v17
