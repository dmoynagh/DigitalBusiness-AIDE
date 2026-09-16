# AIDE Orchestration — Decisions v1 (DRAFT — for review)

Status: proposed alongside Design v1. Not deployed, not cross-reviewed.

---

**D1 — Dispatch replaces the universal Work Package as Orchestration's artefact.**
The investigation's proposed universal Work Package and mandatory Verification Response
would make Orchestration own task semantics, violating the component's ownership
boundary. A thin `dispatch` (target, workspace, model level, opaque payload) is the
Orchestration-level artefact instead. Caller-owned artefacts (Build packages, review
requests, Messaging envelopes) travel as the payload.

**D2 — Orchestration ownership narrowed.** Owns: dispatch, invocation, transport/channel
selection, target adapters, target-specific invocation mechanics, model-level
resolution, execution-endpoint interaction, correlation, transport/invocation failure,
returning results to the caller. Does not own: work-package/build-package structure,
task types, verification policy, acceptance criteria, review semantics, Build's return
semantics, generic response semantics, human/autonomy policy, or model-mapping content.

**D3 — Core's current wording needs correction.** Core presently assigns Orchestration
ownership of "work package structure, verification, and capability profiles." This
contradicts D2 and needs correcting in Core's own document, not silently absorbed by
Orchestration. Tracked here as a dependency on Core; proposed wording included in the
Design document for Core's design pass to adopt or amend.

**D4 — Transport outcome and task outcome are distinct fields.** `transport_status`
(e.g. `completed`) reports only that the invocation returned. It never implies the
requested task succeeded — that judgement stays with the owning component. Prevents a
completed-but-failed task being misread as done.

**D5 — `response_schema` is an adapter capability, not a mandatory contract.**
Schema-constrained output (Agent SDK `outputFormat`, Codex `--output-schema`) is real and
useful, confirmed by investigation. Orchestration may pass a caller-supplied schema
through to a target that supports it. It is never required as part of the Orchestration
contract itself.

**D6 — Model capability is caller-selected, not classifier-selected.** Automatic
model-selection (an AIDE classifier deciding required capability) is parked, not
designed. The caller states required capability directly using a small logical
vocabulary (`basic/standard/high/maximum`), with an `exact` escape hatch for a specific
provider model. `level` and `exact` are normally mutually exclusive.

**D7 — Model-capability mapping content belongs to Core (Framework Resources), not
Orchestration.** The Framework/Framework-Resources split (durable behaviour vs volatile
current knowledge) is a cross-cutting AIDE pattern, confirmed in this session's review as
Core's to own and design. Orchestration is a consumer of Resources, not its owner. Not
deciding the Resources mechanism itself here — recorded as a dependency for Core's
design pass.

**D8 — Availability is discovered, not configured, wherever discovery can represent the
fact.** Machine-specific settings are only introduced where detection genuinely cannot
substitute. Effective available targets = supported-by-Resources ∩ detected-on-endpoint
∩ not-explicitly-disabled.

**D9 — Capability availability and execution-endpoint availability are different
things.** An AI session having the Orchestration capability does not imply a local
execution endpoint is present. The endpoint exposes its own effective target list; a
session queries it rather than inferring the environment (hostname, desktop-vs-web,
installed executables) directly.

**D10 — Implementation home is a local MCP server delivered as a marketplace plugin**,
not `aide dispatch` in the CLI (originally proposed), not a standalone script, not a
Code skill, not a Desktop Extension. The dispatch mechanism lives inside the MCP server;
Infrastructure owns the delivery model (packaging, distribution, update path, surface
coverage). Empirically tested 2026-09-16: all three surfaces (Code, Cowork, Chat) reach
the same server file — Code and Cowork via the plugin's `.mcp.json`, Chat via a one-time
`claude_desktop_config.json` bootstrap pointing at the same file in the marketplace
clone. Plugin updates propagate to all surfaces on restart. The CLI remains available
for terminal-only use but is not the primary delivery surface. Supersedes D10 as
originally drafted.

**D11 — First adapters: `claude-code` and `codex` only.** Gemini/Google support is
additive when a stable execution path exists (Gemini CLI's consumer auth path was found
discontinued as of June 2026; its successor, Antigravity CLI, is early). Not required to
block v1.

**D12 — Stateless first, unchanged from the original investigation position.** Each
dispatch is independently executable. Provider session IDs may be preserved as returned
metadata. No AIDE session-management abstraction is built until a demonstrated workflow
needs one.

**D13 — No semantic intermediate-progress protocol in v1.** Provider event streams may
be surfaced/logged opportunistically. The stable contract distinguishes only transport
completion from transport failure.

**D14 — FUP remains the validation scenario, using `aide fup` unchanged.** The
investigation's proposed `--batch` flag for non-interactive deployment is not adopted
pre-emptively — current `aide fup` behaviour already avoids interactive waiting without
a console. Test the orchestrated invocation first; change `aide fup` only if a real
failure demonstrates the need. Applies apparatus-avoidance directly.

**D15 — No second generic messaging envelope.** Messaging already owns structured
cross-boundary communication and correlation semantics. Where a dispatch payload needs
to travel as structured text, it travels inside Messaging's existing envelope.
Orchestration does not invent a parallel Markdown work-package doctype.

**D16 — Tier (autonomous vs heavyweight) is caller-owned.** Orchestration dispatches
without knowing or tracking whether the surrounding workflow is autonomous or
Dave-driven-interactive. Risk-flagged external review for heavyweight work is the
caller's workflow invoking Orchestration twice (plan review, build review), not a
distinct Orchestration mode. Settles an item left open in the original scoping.

**D17 — Routing (which tasks get delegated, and the threshold for it) is caller-owned.**
The original scoping proposed a crude size/complexity threshold living inside
Orchestration. Under the narrowed ownership (D2), the caller decides the target
explicitly per dispatch; Orchestration executes the routing decision rather than making
it. Settles an item left open in the original scoping.

**D18 — AIDE functionality delivered by plugins is Infrastructure's direction, not
Orchestration-specific.** The local MCP server delivery model (marketplace plugin for
Code/Cowork, `claude_desktop_config.json` bootstrap for Chat, one server codebase)
was tested and confirmed empirically on 2026-09-16 during Orchestration's
investigation. The same pattern applies to binder, FUP, and future AIDE tooling.
Infrastructure owns the delivery model; Orchestration and other components are
consumers. Raised to Infrastructure's design pass, not decided inside Orchestration.

**D19 — Assurance's D14 wording needs correcting.** D14 currently reads
"Infrastructure plumbing, Orchestration coordinates invocation" for learning-loop queue
writing. With the framework inbox and Assurance data logger scoped as remote-hosted MCP
services (always-on, cloud-hosted, reachable to any client), there is nothing for
Orchestration to coordinate — Assurance calls the hosted service directly. Drop the
Orchestration clause from D14 when Assurance's documents are next updated. The hosted
services themselves sit under Infrastructure's "hosted AIDE services" sub-scope
(also pending Infrastructure's design pass).

---

## Deferred (not decided, recorded so they aren't silently lost)

1. Final naming of capability levels.
2. Framework Resources schema and deployment cadence — Core's design pass.
3. Portable user/account settings mechanism.
4. Genuine machine-specific settings beyond environment discovery.
5. Remote execution endpoints for web-hosted sessions.
6. Stateful/multi-turn orchestration.
7. Semantic intermediate-progress protocol.
8. Broader Gemini/Google execution support.
9. Adapter-capability metadata beyond what the first two adapters demonstrate.
