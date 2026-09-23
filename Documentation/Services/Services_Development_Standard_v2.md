> identity: Services_Development_Standard@v2 | doctype: standard | updated: 2026-09-24 | uses: Capabilities_Development_Standard@v2

# Services — Development Standard

How to design, review, build, test, and deploy an AIDE service — and what has been learned building the services so far.

## What a service is

Information. A service provides out-of-session operations that sessions call. It runs as a separate process outside the session, accepts requests from the AI, and performs work the AI delegates to it. The AI is a caller, not the executor. The service has its own lifecycle, configuration, and safety enforcement, independent of the session that calls it. How long it runs is a lifecycle characteristic stated in its design, not what makes it a service.

Information. A service reaches the AI platform as a server. Currently this means a local MCP server; in future it may mean a remote endpoint. The service is what is designed; the server is how it is delivered.

## Applicability

Information. This standard applies when designing, reviewing, building, testing, or deploying an AIDE service. It does not govern tools, utilities, or Infrastructure's delivery mechanisms — but it records what a developer needs to build against them.

## Boundary

**Service vs tool.** If the AI performs the work in-session, it is a tool. If a separate process performs it and the AI calls it, it is a service. The test is who executes, not what is executed.

**Service vs utility.** If sessions connect to it for capabilities, it is a service. If it acts on the corpus rather than serving sessions, it is a utility.

A service and a utility can coexist from the same implementation. Classification follows the exposed entry point: the standalone invocation is a utility, the session-facing operation is a service.

## Designing a service

A service always has a design, however simple — it is a deployed process with configuration, lifecycle, and safety obligations.

The design addresses whatever the service needs to be built correctly. For most services:

- What operations it exposes and what callers can rely on.
- How it is configured — settings, defaults, what happens when configuration is missing.
- What it prevents and enforces — safety is enforced in the process, because the AI has no direct control over what the service does.
- How it reports problems — enough detail for the caller to act.
- How it starts, shuts down, and behaves on restart.

Recommended. Not every service needs all of these, and a complex one may need more. This is what to think about, not a checklist. Where something doesn't apply, say so in the design, so the builder can tell intentional omission from oversight.

**Design fresh.** Produce a service design fresh, not by modifying a previous version.

**Delivery independence.** Design the service's behaviour, not the server's plumbing — the same design should work under a different delivery model. Know enough about the delivery model not to design something it can't support, such as persistent state across Desktop restarts on a local server.

**Build references.** Point the builder at Infrastructure's MCP delivery model and at an existing service as a working example. These are prose references, not `uses` dependencies.

## Reviewing and testing a service

**Self-check first.** Before cross-review, check the design against its definition of done and confirm the boundary tests place it as a service, not a tool or a utility. Keep it proportionate — a read-through, not a checklist.

**Review the design.** The design is the build specification. Cross-review it with a separate AI directed to find defects — contradictions, gaps, claims the delivery model can't support, operations without defined failure behaviour — against the design's definition of done. Triage findings as defects, partly valid, or misreadings; remediate and record in the decisions. Run a further round only when remediation introduces material the reviewer hasn't seen.

**Test the built server.** Exercise every operation against what the design says it does, including failure paths. Confirm the server works on each surface it targets — for a local server, Code, Cowork, and Chat, which register servers by different paths. After the first update, confirm the update propagates to each surface.

Recommended. A small probe operation returning identifying data — origin, timestamp, a runtime ID — shows which build is actually running on which surface.

## Building a service

The design is the build specification — there is no authored document. Build creates the server from the design.

### Local MCP servers

Build as a local MCP server over stdio.

- **Use newline-delimited message framing.** Content-Length headers cause a silent 120-second timeout on every connection.
- **Use UTF-8.** Python servers on Windows call `sys.stdin.reconfigure(encoding="utf-8")` at startup; otherwise non-ASCII request content is corrupted.

Information. Proven approach, not required: raw JSON-RPC with no MCP SDK dependency — Node.js in CommonJS with no external dependencies (the dispatch server), or Python with the standard library only (the document management server). A service may choose differently where that serves it better.

Known issues and their solutions:

- **Python on Windows.** The config entry uses the absolute path to a real Python interpreter; the Store stub does not work.
- **Report status, not paths.** Report operational status to callers — initialised, resources found. Don't expose filesystem paths or config locations to the AI; put setup detail in the user guide.
- **Enforce safety in the process.** Path containment, readonly enforcement, clean-state preconditions, input validation. Where the service delegates downstream, state what it validates first and what it trusts the target to enforce.

### Remote services

Information. Hosted services follow the same design guidance; what changes is the delivery — a hosted endpoint, with its authentication and networking. None has been built yet. Build knowledge is added here from the first one.

## Deploying a service

### Local MCP servers

Deliver the server in a marketplace plugin: `.mcp.json` declaring each server using `${CLAUDE_PLUGIN_ROOT}`, `plugin.json` with metadata, and server code under `server/`.

- **Surfaces.** Code and Cowork get the tools through desktop app plugin registration. Chat needs a separate `claude_desktop_config.json` entry — a workaround for a platform bug; remove it when the bug is fixed.
- **Update path.** Merge a PR to the deploy repo, run `claude plugin marketplace update`, restart Desktop. Direct commits to `main` don't trigger updates. Quit Desktop first if a server from that marketplace is running — it locks the clone.

Information. Platform support: Claude — Chat, Code, and Cowork — is supported; the two paths above give coverage of all three Claude surfaces. ChatGPT and Codex are pending. The ChatGPT route recorded so far is curated standards binders, a future consideration that carries standards, not services. No adapters for other platforms are built.

Information. The full methodology and platform issues are in Infrastructure's MCP delivery model.

### Remote services

Information. Not yet built. Deployment guidance is added from the first remote service.

## Consuming a service

Every service has a user guide alongside its design documents: what it does, how to verify it is connected, how to configure it, the operation inventory, and platform-specific setup such as the Chat config entry. The guide serves the human operator.

Information. The AI consumes the service through its interface. A well-designed interface is self-evident from the operation descriptions the server exposes.

## The sibling-outputs model

Information. A single design can produce standards, tools, and services as sibling outputs. All derive from the design, not from each other, and must not disagree.

## Ownership

**Each service lives with its owning component.** Services defines how to build a service, not where services live.

---

Version note: v1 — initial standard. Produced from Services_Design@v2: informal design guidance, review and testing, practical build knowledge from the first two services, local deployment, remote placeholder, user guide as a deliverable. 2026-09-23.

Version note: v2 — a service is defined by out-of-session operations that sessions call, not persistence. Self-check added before cross-review. Build: only newline-delimited framing and UTF-8 are required; the rest is information on the proven approach. Platform-support statement added. Produced from Services_Design@v3. 2026-09-24. Replaces v1.
