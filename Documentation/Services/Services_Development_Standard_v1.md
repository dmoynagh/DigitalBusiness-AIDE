> identity: Services_Development_Standard@v1 | doctype: standard | updated: 2026-09-23 | uses: Capabilities_Development_Standard@v1

# Services — Development Standard

How to design, build, and deploy an AIDE service — the practical guide to creating services that run outside AI sessions.

## What a service is

Information. A service provides persistent operations to AI sessions. It runs as a separate process outside the session, accepts requests from the AI, and performs work the AI delegates to it. The AI is a caller, not the executor. The service has its own lifecycle, its own configuration, and its own safety enforcement — none of which depend on the session that calls it.

Information. A service reaches the AI platform as a server. Currently this means a local MCP server; in future it may mean a remote endpoint. The service is what is designed; the server is how it is delivered.

## Applicability

Information. This standard applies when designing, building, or deploying an AIDE service. It does not govern tools, utilities, or Infrastructure's delivery mechanisms — but it records the practical knowledge of building against those mechanisms.

## Boundary

### Service vs tool

If the AI performs the work in-session, it is a tool. If a separate process performs the work and the AI calls it, it is a service. The test is about who executes, not about what is executed.

### Service vs utility

If sessions connect to it for capabilities, it is a service. If it acts on the corpus rather than serving sessions, it is a utility. Services owns this test.

A service and a utility can coexist from the same implementation. Classification follows the exposed entry point.

## Designing a service

A service always has a design — there is no exception for simple services. A service is a deployed process, and even a simple one resolves questions that need working through before build.

The design should address whatever the service needs to be built correctly. For most services, that means:

- What operations it exposes and what callers can rely on.
- How it is configured — settings, defaults, what happens when configuration is missing.
- What it prevents and enforces — safety is the service's responsibility because the AI has no direct control.
- How it reports problems — enough detail for the caller to act.
- How it starts, shuts down, and behaves on restart.

Recommended. Not every service will need all of these. A stateless dispatch service has no configuration and trivial lifecycle. A complex service may need more than this list names. These are what a designer naturally addresses — not a compliance checklist. Where something doesn't apply, the design says so, so the builder can distinguish intentional omission from oversight.

**Design fresh.** A service design is produced fresh, not by modifying a previous version.

**Delivery independence.** Design the service's behaviour, not the server's plumbing. The same design should work under a different delivery model without changing.

## Building a service

The design document is the build specification — there is no intermediate authored document. Build creates the server from the design.

### Current approach — local MCP servers

Services are currently built as local MCP servers using raw JSON-RPC over stdio, with no MCP SDK dependency. Two patterns are proven:

- **Node.js** — CommonJS, newline-delimited JSON over stdio. Used by the dispatch server.
- **Python** — raw JSON-RPC, stdlib only. Used by the document management server.

Key things learned from building the first two services:

- **Newline-delimited JSON framing is required.** Claude Desktop's stdio transport expects `\n`-delimited JSON. Using Content-Length headers causes a silent 120-second timeout on every connection attempt.
- **Windows encoding.** Python servers must set `sys.stdin.reconfigure(encoding="utf-8")` at startup. Without it, stdin defaults to the Windows system codepage, which corrupts non-ASCII content in requests.
- **Configuration reporting.** A service reports operational status to callers (what it can do, how many resources it found) — not filesystem paths or config file locations. The human sees setup detail in the user guide; the AI sees operational status.
- **Safety is enforced, not advisory.** The AI cannot verify what the service does with a request. Path containment, readonly enforcement, input validation — these are the service's responsibility, enforced in its process.

### Future approach — remote services

Cloud-hosted, always-on services (the framework inbox, assurance data logger) follow the same design methodology but have a different delivery model. The design guidance above applies regardless of where the service runs. What changes is Infrastructure's delivery concern — local process vs hosted endpoint, with the authentication and networking that implies.

## Deployment

### Local MCP servers

A local service is delivered as part of a marketplace plugin. The server code lives in the plugin alongside skills and plugin metadata. Infrastructure's MCP delivery model (`Infrastructure_MCPDeliveryModel@v2`) documents the full packaging methodology, known platform issues, and workarounds.

Key deployment facts for service developers:

- **Surfaces.** Code and Cowork get server tools via desktop app plugin registration. Chat currently needs a separate `claude_desktop_config.json` entry (platform bug workaround — the plugin's `.mcp.json` tools don't reliably reach Chat).
- **Update path.** Merge PR to the deploy repo → refresh marketplace clone (`claude plugin marketplace update`) → restart Desktop. Direct commits to `main` do not trigger updates.
- **Plugin structure.** `.mcp.json` declares servers (using `${CLAUDE_PLUGIN_ROOT}`), `plugin.json` has metadata, server code in `server/`.

### Remote services

Not yet built. When the first remote service is built, the deployment guidance will be added here from that experience — the same way local deployment guidance was derived from building the dispatch and document management servers.

## Consumption

Every service has a user guide alongside its design documents — what the service does, how to verify it is connected, how to configure it, the operation inventory, and any platform-specific setup. The user guide serves the human operating the service, not the AI consuming it.

Information. The AI consumes the service through its interface — the operations, inputs, outputs, and error model. A well-designed interface makes AI-side consumption self-evident from the tool descriptions the server exposes.

## The sibling-outputs model

Information. A single design can produce standards, tools, and services as sibling outputs. All derive from the design, not from each other, and must not disagree.

## Ownership

**Each service lives with its owning component.** Services is a methodological component — it defines how to build a service, not where services live. Each service is designed and owned by the component or area it serves.

---

Version note: v1 — revised. Design concerns softened from seven formal obligations to informal guidance. Practical building knowledge added from the two working services. Deployment guidance covers local MCP servers with key platform facts; remote services acknowledged for future. 2026-09-23.
