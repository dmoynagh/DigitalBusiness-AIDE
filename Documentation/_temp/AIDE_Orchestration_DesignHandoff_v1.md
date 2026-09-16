# AIDE Orchestration — Design Handoff Brief

For design shaping and model building in another AI session. Bring the result back to
the AIDE project chat for review and implementation.

Version 1. 2026-09-15.

---

## What AIDE is (context for an AI with no prior exposure)

AIDE is a methodology-driven framework that embeds standards and working practices into
AI-assisted software development sessions. It is built by Dave, a solo developer, mostly
through structured design sessions with Claude. AIDE itself has components — Core,
Principles, Standards, Project Design, Working Practices, Assurance, Messaging, Build,
Orchestration, and others — each with a design pass producing a Design document, a
Decisions log, and a lean Standard (the deployable artefact).

**Governing design principles, applied throughout AIDE and to this work:**

- **No apparatus a principle didn't ask for.** Build the smallest version that satisfies
  the principle. Elaborate only if volume or evidence justifies it.
- **Difficulty is evidence about the design, not about the implementation.** If something
  is getting hard to build, that's a signal to revisit the model, not to add cleverness.
- **General in shape, singular in first use.** Prove a mechanism end-to-end with one real
  case before generalising it to a category of cases.
- **Design produces the specification; build creates from it and owns how.** The
  design/build separation is fundamental to how AIDE works, including for itself.
- **Simple and well-conceived is a design goal, not a nicety.** Output markedly more
  elaborate than the intent above it is a warning sign.

This brief is itself an application of these principles to the Orchestration component.

---

## What Orchestration is for

**Objective.** Orchestration owns the transport and coordination mechanics that let work
move between surfaces — chat, Claude Code, and external AI platforms — with structured
evidence coming back. It is a Delivery-role component: it doesn't decide what work
happens (that's the consuming component's job), it moves the work and returns proof of
what happened.

**Charter alignment.** This serves AIDE's cross-platform applicability objective (AIDE
works across platforms and surfaces), the trust and integrity objective (structured
verification makes work checkable, not just claimed), and the reduce-burden objective
(delegation to Code and to external AI reduces Dave's load as the framework matures).

**Two scopes, one shared shape:**

1. **Build delegation** (chat/Code → Claude Code) — an intent-level specification goes
   to Claude Code's agent loop, which owns file discovery, edit planning, and execution,
   and returns structured verification.
2. **Cross-platform review** (chat/Code → other AI platforms) — a review, search, or
   collaboration task goes to Codex, Gemini, or another platform, and a structured
   response comes back.

The core separation in both: **task creation is independent of transport.** The thing
that describes what needs doing (the work package) doesn't know or care how it travels.

---

## Tasks that would use Orchestration once built

- **FUP (File Update Package) delivery** — the current, entirely manual process of
  building a zip with a manifest and handing it to Code. This is the first validation
  scenario for the whole mechanism (see below).
- **Build delegation** — "apply this specification to the codebase" tasks that currently
  require Dave or chat to walk Code through file-by-file.
- **Cross-platform review** — getting a second AI's opinion on a design or a piece of
  code before committing to it, currently done by hand through Codex CLI.
- **Search/collaboration tasks** — open-ended requests to another platform that aren't
  quite review (e.g. "does this pattern exist elsewhere," "sanity-check this approach").
- **Risk-flagged external review** for heavyweight work — plan reviewed by an external
  AI, build reviewed by an external AI, completion document written. This is part of the
  heavyweight tier, not a separate mechanism.

---

## Architecture as scoped (before investigation)

This is the thinking from the original scoping session, before anything was tested.

### The work package — centre of gravity

The work package (possibly renamed "build package" to avoid collision with an existing
"work item" concept elsewhere in AIDE) is the bridge between design and build concerns.
It belongs to neither side. It must be:

- **Authorship-independent** — the same shape whether produced in chat or in Code. If
  Code authors a work package, it goes through the same doorway chat would use — the
  apparent redundancy is deliberate, it keeps the seam honest.
- **Transport-independent** — the same artefact can travel by copy-paste or by MCP.
  Location-independence follows from this: design work may happen in chat or in Code,
  so the artefact can't assume where it started.

The interface contract — what a work package contains and how it's structured — is the
single most important thing to get right.

### Two tiers of work package

- **Tier 1 — autonomous.** MCP delivers the instruction, Code executes, questions and
  responses come back to chat without Dave driving each step.
- **Tier 2 — heavyweight.** The work package is dropped as a file into the repo, Code
  picks it up, and Dave drives interactively in Code. Includes risk-flagged external
  review — plan reviewed externally, build reviewed externally, completion document
  written. The file-drop sidesteps the harder question of whether MCP can prime a live
  interactive Code session; the filesystem is the handoff.

### Verification

Verification travels at the same level as the instruction — evidence against the
specification comes back, not full file bodies dumped into chat. Code returns a
structured summary, a diff of changed regions, files touched, and objective check
results (compile, test, etc.). An objective gate on the Code side catches
misinterpretation before it reaches approval. If verification machinery starts getting
elaborate, that's a signal the specification wasn't precise enough — tighten the spec,
don't add checkers.

### Routing

Start with a crude threshold (more than a couple of files, or beyond some size, goes to
Code; the rest stays in chat). Adjust from experience — don't engineer a clever router
until a dumb one proves insufficient.

### Cross-platform review — statefulness

Most review work is stateless single request-response. All model calls are fundamentally
stateless anyway — "sessions" are client-side transcript replay. Since state is just a
replayed transcript, the orchestration layer could hold it itself if a given transport
lacks good resume support. Decision: **build stateless first, defer multi-turn until a
genuine need appears** — no penalty in deferring.

Each transport declares a capability profile: stateful or not, subscription or
token-billed, structured-output support or not. The scope picks a transport partly based
on what the task needs.

### Billing and auth (as originally assumed)

Dave is on Claude Max 5x and ChatGPT Plus. The target throughout is subscription/OAuth
auth, not API-key billing — this is personal use of his own subscriptions, not a product
distributed to others. `ANTHROPIC_API_KEY`, if set, silently overrides subscription
billing, so it must stay unset in the orchestration environment.

---

## What investigation found (tested against the scoping assumptions)

A prior session tasked Claude Code with investigating and prototyping the five open
questions the scoping session couldn't resolve on its own. Full findings are attached
separately; this is the digest.

| Area | Scoping assumption | Finding |
|---|---|---|
| 1. Agent SDK invocation | Intent-level delegation via an "Agent SDK wrapper" | **Confirmed and real.** `@anthropic-ai/claude-agent-sdk`'s `query()` function does exactly this — accepts a prompt, tool permissions, a working directory, and a JSON Schema for the final structured response. CLI equivalent (`claude -p --output-format json`) exists for non-JS callers. |
| 2. Subscription auth | OAuth against Max subscription, not API key | **Confirmed with a nuance.** Non-bare mode (the default) reads the logged-in session from the OS keychain automatically — no special config needed beyond staying logged in and keeping `ANTHROPIC_API_KEY` unset. Bare mode needs an API key. Usage draws from the same Max 5x quota as interactive sessions. |
| 3. Desktop Extension packaging | The deployment vehicle for automated build delegation | **Corrected, not confirmed.** Desktop Extensions (MCPB format) are passive MCP tool servers — chat can call tools they expose, but they cannot invoke Claude Code's agent loop or drive execution. Using one for the core transport would recreate the "chat still does the expensive work" problem the scoping session explicitly rejected. They have a legitimate secondary role (a "submit work package" convenience UI, status dashboards) but are not the orchestration mechanism itself. |
| 4. Cross-platform review transport | Codex and Gemini CLIs for non-interactive review | **Codex confirmed strong; Gemini path has moved.** Codex CLI (`codex exec`, `codex exec review`) has schema-constrained structured output, clean session resume, and confirmed ChatGPT Plus subscription auth. Gemini CLI **stopped serving consumer/subscription auth in June 2026** — Google consolidated under a new "Antigravity" brand and CLI (`agy`), which is early and has known permission bugs in headless mode. Gemini CLI still works with an API key, just not with the subscription auth the scoping session wanted. |
| 5. Work package contract | Authorship-independent, transport-independent artefact | **Draft schemas produced**, informed by what 1–4 showed is actually available (JSON Schema for both the Agent SDK's `outputFormat` and Codex's `--output-schema`). Tested conceptually against the FUP validation scenario. |

**Overall conclusion from the investigation:** the architecture is sound. The one real
correction is Desktop Extensions serving a different, smaller role than originally
scoped — everything else confirmed with implementation detail filled in.

### Key technical shape now known

**Build delegation (confirmed working pattern):**

```
Work package (task_type: build, tier: autonomous/heavyweight)
        │
        ▼
Agent SDK query({ prompt: intent, allowedTools, outputFormat: verificationSchema,
                   cwd: projectRoot, maxBudgetUsd, maxTurns })
        │
        ▼
Claude Code agent loop — owns file discovery, edit planning, execution
        │
        ▼
Verification response (schema-constrained): status, summary, files_changed,
checks, criteria_met, questions, blockers
```

**Cross-platform review (confirmed working for Codex, deferred for Gemini):**

```
Work package (task_type: review, routing.target: codex)
        │
        ▼
codex exec review "..." --json --output-schema schema.json --output-last-message out
        │
        ▼
Review response (parsed into the same verification schema shape)
```

**Draft work package schema** (fields, not full JSON Schema — see attached findings for
the complete version): `package_id`, `created`, `task_type` (build/review/search/
collaborate), `tier` (autonomous/heavyweight), `specification` (intent, context, scope),
`acceptance` (criteria, objective_checks), `routing` (transport, target, model,
budget_usd).

**Draft verification response schema:** `status` (success/partial/failed/blocked),
`summary`, `files_changed`, `checks`, `criteria_met`, `questions`, `blockers`.

The two schemas are designed to be the same shape whether the executor is Claude Code
(via `outputFormat`) or Codex (via `--output-schema`) — same contract, different
transport underneath.

---

## Open questions carried into this design pass

These are things the investigation surfaced but explicitly left for a design session to
resolve — this is the work being handed off.

**Where does the orchestration code live?** Three candidates surfaced: a standalone
Node.js/Python script that orchestrates from outside both chat and Code; a Claude Code
skill that reads work packages and invokes the SDK (Code invoking Code, recursively); or
a Desktop Extension MCP server that exposes orchestration tools to chat. Each has
different coupling and control tradeoffs. The investigation's own view: start with a
standalone script — simplest, most testable, least coupled — and evolve into a skill or
extension only if integration benefits justify it later. That's a recommendation, not a
decision.

**Intermediate status reporting.** The Agent SDK's `outputFormat` constrains only the
*final* response. During execution the agent produces a stream of assistant messages
(reasoning, tool calls, intermediate results) that aren't schema-constrained. Is
intermediate progress reporting needed for the autonomous tier, or is a single
verification response at the end sufficient?

**FUP deployer invocation strategy.** For the validation scenario specifically: should
the work package tell the agent to run the existing Python deployer tool
(`file_update_package.py`), or should it tell the agent to perform the deployment itself
(read the manifest, copy files, handle superseded versions)? The deployer is the proven
mechanism and has its own verification output, but it's currently interactive (holds a
window open, may prompt) — it would need a batch/non-interactive mode to be driven by an
agent. Recommendation from the investigation: add a `--batch` flag to the existing tool
rather than duplicate its logic in the agent.

**SDK credit pool status.** Max 5x reportedly includes a separate $100/month credit pool
for API-key-authenticated calls, distinct from the subscription quota. Not directly
verifiable from the investigation session — Dave needs to check
`console.anthropic.com` → Billing → Usage. Matters only if API-key-authenticated
invocations (CI pipelines, bare mode) are ever needed; subscription auth is unaffected
either way.

**Desktop Extension role, if any.** Given the correction above, is a Desktop Extension
worth building at all as a convenience layer (a "Submit Work Package" tool in chat for
the manual/copy-paste path), or does copy-paste alone cover that case adequately for
now? Investigation's recommendation: defer — build it only when the manual path becomes
frequent enough to justify the packaging overhead.

**Work package naming.** There's a pending rename elsewhere in AIDE from "work package"
to "build package" for the build-side design-to-build handoff artefact, to avoid
collision with an existing "work item" concept in Working Practices. The Orchestration
transport artefact is a different thing again — arguably neither "work package" nor
"build package" is quite right, since it's a transport envelope, not a build handoff.
Options raised: "task package," "dispatch." Needs settling before the schema hardens
further, or an explicit decision to leave it as "work package" for now.

**Distribution vs personal use.** The Agent SDK's subscription-auth policy note (from
Anthropic's docs) restricts third-party developers from offering `claude.ai` login or
rate limits to other people's products — this doesn't block personal use of one's own
subscription, which is what AIDE is. But if AIDE is ever distributed to other users (as
a product or template) rather than staying personal tooling, the orchestration layer
would need to accept per-user API keys from the start, even if Dave himself keeps using
subscription auth. Is distribution a real future consideration or is AIDE always
personal? This shapes whether auth is designed with a seam for it now or added later if
needed.

**Gemini/cross-platform breadth.** With Gemini CLI's consumer path gone and its
successor (Antigravity/`agy`) immature, is Codex-only sufficient for the first build of
cross-platform review, with other platforms added as their tooling matures? Or is there
a reason to invest in the Gemini API-key path (rather than subscription) now?

---

## What's being asked of this session

Design shaping and model building for the Orchestration component, informed by the
architecture above and grounded in what the investigation actually confirmed (not the
original assumptions where they diverge — see the Desktop Extension correction
especially).

Useful outputs to bring back:

- A resolved position on the open questions above, or a narrowed set of options with
  reasoning, where a clean resolution isn't possible without more input from Dave.
- A refined work package schema and verification response schema, if the draft ones
  need adjustment in light of the design thinking.
- A view on component boundaries — does anything here belong to a different AIDE
  component (Build, Messaging, Assurance) rather than Orchestration itself? AIDE is
  deliberately strict about component ownership.
- Anything that looks like it needs a different model entirely, rather than a
  refinement of this one — per AIDE's own principle, if something here is proving hard
  to fit, that's a signal worth surfacing, not smoothing over.

This session doesn't need AIDE's full documentation corpus or deployment conventions —
just the architecture, the findings, and the open questions above. Implementation
detail, formal standards authoring, and deployment happen back in the AIDE project.

---

## Attached separately

- `AIDE_Orchestration_Investigation_Findings.md` — the full investigation findings
  (technical detail, code examples, complete schemas, per-area evidence).
