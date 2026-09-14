---
name: orchestration
description: Orchestration scope — local MCP transport for build tasks (to Claude Code) and cross-platform review (to Codex/Gemini/others); scoped 2026-09-15
sources: [chat]
aliases: [orchestration, local MCP, build packages, work packages, cross-platform review, sonder]
---

## Status

- Scoping complete (voice session 2026-09-15), not yet built

## Packaging and deployment

- Claude Desktop Extensions (formerly .dxt, now MCPB) allow one-click install of local MCP servers — no manual config editing needed
- Desktop includes bundled runtime, secrets via OS keychain, Extensions tab in Settings

## Architecture — two orchestration scopes, one shared shape

### Core separation

- Task creation is separate from transport — creation side builds the instruction, transport delivers it
- Transport is dumb about what it carries — same pipe regardless of task type
- Two transports always available: copy-paste (manual) and MCP (automated when working)
- MCP transport checks availability and falls back; copy-paste is always the baseline

### The work package as the centre of gravity

- The work package (may rename to build package) is the bridge between design and build as concerns — belongs to neither side
- Work package must be authorship-independent — same shape whether authored in chat or in Code
- If Code authors a work package it should go through the same doorway chat would use — apparent redundancy keeps the seam honest
- The interface contract (what a work package contains and how it's structured) is the critical thing to define precisely
- Design work may happen in chat or in Code — the seam floats, so the artefact must be location-independent

### Scope 1 — Build (chat/Code → Claude Code)

- Intent-level delegation via Claude Agent SDK wrapper, not raw mcp serve — chat describes the change, Code's agent loop realises it
- Raw mcp serve rejected: chat would still do the expensive work (locating files, reasoning about edits), saving almost nothing
- Maps to existing design-build separation — chat produces the specification, Code owns how it's built

#### Two tiers of work package

- **Tier 1 — autonomous:** MCP delivers instruction, Code executes, questions/responses come back to chat
- **Tier 2 — heavyweight:** MCP places the work-package file in the repo folder, Code's scan command picks it up, Dave drives interactively in Code
- Heavyweight tier includes risk-flagged external review (plan reviewed by external AI, build reviewed by external AI, completion document written)
- File-drop for heavyweight tier sidesteps the question of whether MCP can prime a live interactive Code session — filesystem is the handoff

#### Verification

- Verification travels at the same level as the instruction — evidence against the specification, not full file bodies back into chat
- Code returns structured summary, diff of changed regions, files touched, objective check results
- Objective gate on the Code side (compile, tests, assertions) catches misinterpretation before it reaches approval
- If verification machinery gets elaborate, that's a signal the specification isn't precise enough — tighten the spec, don't add checkers

#### Routing heuristic

- Start with a crude threshold — e.g. more than a couple of files or beyond a certain size goes to Code, rest stays in chat
- Adjust from experience, don't engineer a clever router until a dumb one proves insufficient

### Scope 2 — Cross-platform review / collaboration (chat/Code → other AI platforms)

- Structurally identical to build scope — task creation separate from transport
- Task types include: review, search, collaborate, discussion — each shapes the artefact differently
- Current proven mechanism: Codex CLI from Claude Code, submitting prompts and getting responses, using OpenAI ChatGPT Plus subscription (not API tokens)
- Want to add Gemini and potentially others — one review scope, many transports, each with a declared capability profile

#### Statefulness

- Most review work is stateless single request-response today
- All model calls are fundamentally stateless — "sessions" are client-side transcript replay
- Codex CLI has clean non-interactive resume (codex exec resume), preserves transcript/plan/approvals, built for CI/pipelines
- Gemini CLI has session management and richer branching/undo but non-interactive resume path is newer and less settled
- Since state is just replayed transcript, orchestration layer could hold it itself if a transport lacks good resume
- Decision: build stateless first, defer multi-turn until a genuine need appears — no penalty in deferring

#### Transport capability profiles

- Each transport declares: stateful or not, subscription or token billing, structured output support
- Scope picks transport partly based on what the task needs — one-shot can go anywhere, multi-turn needs a stateful transport

## Billing and authentication

- Dave is on Max 5x plan
- Target: OAuth/auth-token authentication against Max subscription, NOT API key
- If ANTHROPIC_API_KEY is set it overrides subscription and bills pay-as-you-go — must be unset
- Environment precedence: cloud creds → ANTHROPIC_AUTH_TOKEN → ANTHROPIC_API_KEY
- Separate SDK credit pool (if/when active) is $100/month at API rates for Max 5x, does not roll over
- Subscription-auth route has been subject to on-again-off-again billing changes — verify against own account before committing
- For Codex CLI: uses ChatGPT Plus subscription via CLI, not API tokens
- For Gemini: TBD — same principle, use subscription not tokens

## Design principles applied

- No apparatus a principle didn't ask for — build the smallest version, elaborate only if volume justifies it
- General in shape, singular in first use — prove end-to-end with one case (FUP) before pouring other task types through
- If implementation is getting too hard or elaborate, the model needs a look, not more cleverness
- Measure what file work actually costs now before building — prove the premise before building the apparatus
