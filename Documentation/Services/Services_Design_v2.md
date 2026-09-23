> identity: Services_Design@v2 | doctype: design | updated: 2026-09-23

## Brief

**Purpose.** Define what a service is and how one is designed, reviewed, built, tested, and deployed within AIDE — and record what has been learned about building services, so each new service is easier than the last. Services is a methodological component — it owns the methodology for building services, not the services themselves. Each service is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The service definition and boundary tests; design guidance; review and testing; building and deploying services, locally now and remotely in future; consumption; and ownership. Broad scope, few constraints — the methodology guides service creation and records knowledge, practice, and solutions to known issues; it does not prescribe structure for every possible service.

**Target outcome.** A deployed Services Development Standard that any component author uses when developing a service.

**Definition of done.**

1. A developer can tell whether something should be a service — the definition and the boundaries with tools and utilities.
2. A developer can design a service — what the design should address, without a prescribed structure.
3. A developer can review and test a service — cross-review of the design, and testing the built server against its design on each surface it targets.
4. A developer can build a service against the current delivery model, using the practical knowledge recorded from the services built so far.
5. A developer can deploy a service — the delivery path, surfaces, update path, and known platform workarounds.
6. A human can operate a deployed service — the user guide is a required deliverable.
7. The Services Development Standard can be produced entirely from this design.

**Linked build outcome.** Services Development Standard, deployed as a skill in the `aide-dev` plugin.

## What a service is and does

A service provides persistent operations to AI sessions. It runs as a separate process outside the session, accepts requests from the AI, and performs work the AI delegates to it — filesystem access, git operations, external process invocation. The AI is a caller, not the executor.

This is the fundamental distinction from a tool. A tool encapsulates a procedure the AI performs in-session. A service encapsulates operations a separate process performs, which the AI calls. The service has its own lifecycle, its own configuration, and its own safety enforcement — none of which depend on the session that calls it.

A service reaches the AI platform as a server — a process the platform connects to and routes calls through. Currently this means a local MCP server; in future it may mean a remote endpoint. The delivery mechanism is Infrastructure's concern, not a property of the service type. The service is what is designed; the server is how it is delivered.

## Applicability of the development standard

The Services Development Standard applies when designing, reviewing, building, testing, or deploying an AIDE service. It does not govern tools, utilities, or Infrastructure's delivery mechanisms — but it records the practical knowledge a developer needs to build against those mechanisms.

## Two boundary tests

### Service vs tool

If the AI performs the work in-session, it is a tool. If a separate process performs the work and the AI is a caller, it is a service.

The test is about who executes, not about what is executed. File operations could be a tool (the AI writes to disk using platform-native capabilities) or a service (a server writes to disk on the AI's behalf with safety guarantees the platform doesn't provide). The question is whether the AI performs the steps or calls something that does.

### Service vs utility

If sessions connect to it for capabilities, it is a service. If it acts on the corpus rather than serving sessions, it is a utility.

A utility runs on its own terms — triggered by a human, a script, or a schedule. It does not accept requests from sessions. A service exists to be called by sessions. Both run outside the session; the direction of service differs.

A thing may start as a utility and become a service when sessions need to call it directly. The binder builder started as a standalone utility and became an operation within the document management service when sessions needed to trigger builds and receive the result in a conversation. The two forms can coexist from the same implementation. Classification follows the exposed entry point: the standalone invocation is a utility, the session-facing operation is a service.

### Ownership of the tests

Services owns the service definition and the service-vs-utility test. The execution-context property (in-session vs out-of-session) is a Capabilities taxonomy property; the invocability test that separates standards from tools is owned by Tools. Services references both.

## Designing a service

A service always has a design. There is no equivalent of the tool exception ("simple enough that a design would restate rather than elaborate") because a service is a deployed process with configuration, lifecycle, and safety obligations — even the simplest resolves questions that need working through before build.

The design addresses whatever the service needs to be built correctly. For most services, that means:

- What operations it exposes and what callers can rely on.
- How it is configured — settings, defaults, what happens when configuration is missing.
- What it prevents and enforces — safety is the service's responsibility, enforced in its process rather than advisory, because the AI is a caller with no direct control over what the service does.
- How it reports problems — enough detail for the caller to decide what to do.
- How it starts, shuts down, and behaves on restart.

Not every service needs all of these. A stateless dispatch service has no configuration and a trivial lifecycle; a document management service needs all of them and more. The list is what a designer naturally thinks about — not a compliance checklist. It is deliberately informal: the first two services were used to identify what to think about, not to fix a structure future services must follow. Where something on the list does not apply, the design says so, so the builder can tell intentional omission from oversight.

**Design fresh.** A service design is produced fresh, not by modifying a previous version.

**No prescribed template.** A service design has no fixed structure.

**Delivery independence.** The developer designs the service's behaviour, not the server's plumbing. The same design should work under a different delivery model — local today, remote later — without changing. In practice the developer must know enough about the delivery model to avoid designing something it cannot support: a service that needs persistent state across Desktop restarts makes a claim the local model doesn't support.

**Build references.** The design points the builder at Infrastructure's MCP delivery model and at an existing service as a working example. These are reference documents in prose, not `uses` dependencies — `uses` declares standards only.

## Reviewing and testing a service

**Reviewing the design.** The design is the build specification, so it is what gets reviewed. Cross-review by a separate AI, directed to find defects — contradictions, gaps, claims the delivery model can't support, operations without defined failure behaviour — and given the definition of done to test against. Findings are triaged as defects, partly valid, or misreadings, remediated, and recorded in the decisions. A further round is needed when remediation introduces material the reviewer hasn't seen.

**Testing the built server.** Every operation is exercised against what the design says it does, including its failure paths. The server is then confirmed working on each surface it targets — Code, Cowork, and Chat for a local server — because the surfaces register servers by different paths and a server can work on one and not another. After the first update, confirm the update propagates: the surfaces pick up the new code after the update path is followed. This is the approach that proved the delivery model: a small probe operation returning identifying data (origin, timestamp, a runtime ID) shows which build is actually running on which surface.

## Building a service

The design is the build specification — there is no intermediate authored document. Build creates the server from the design, following Build's generic mechanism. Build standards for the service build domain live in the Services Development Standard.

### Current approach — local MCP servers

Services are currently built as local MCP servers implementing raw JSON-RPC over stdio, with no MCP SDK dependency. Two patterns are proven:

- **Node.js** — CommonJS, newline-delimited JSON over stdio, no external dependencies. Used by the dispatch server.
- **Python** — raw JSON-RPC, standard library only. Used by the document management server. On Windows, the config entry must use the absolute path to a real Python interpreter; the Store stub does not work.

Knowledge from building the first two services:

- **Newline-delimited JSON framing is required.** Claude Desktop's stdio transport expects `\n`-delimited JSON. Content-Length headers cause a silent 120-second timeout on every connection attempt. This is not well documented and was found in testing.
- **Windows encoding.** Python servers set `sys.stdin.reconfigure(encoding="utf-8")` at startup. Without it, stdin uses the Windows system codepage and corrupts non-ASCII content in requests — file content, not just messages.
- **Report status, not paths.** A service reports operational status to callers — whether it is initialised, what resources it found. It does not report filesystem paths or config file locations to the AI; the AI has no use for them, and setup detail belongs in the user guide.
- **Safety is enforced in the process.** Path containment, readonly enforcement, clean-state preconditions, input validation. Where a service delegates work downstream, the design states what it validates before delegating and what it trusts the target to enforce.

### Future approach — remote services

Cloud-hosted, always-on services (the framework inbox, the assurance data logger) follow the same design methodology. What changes is Infrastructure's delivery concern — a hosted endpoint instead of a local process, with the authentication and networking that implies. No remote service has been built yet. When the first one is, its build and deployment knowledge is recorded here, the same way local knowledge was recorded from the first two services.

## Deploying a service

### Local MCP servers

A local service is delivered in a marketplace plugin. The plugin holds `.mcp.json` declaring each server using `${CLAUDE_PLUGIN_ROOT}`, `plugin.json` with metadata, and the server code under `server/`. The full packaging methodology and platform issues are in Infrastructure's MCP delivery model.

What a service developer needs to know:

- **Surfaces.** Code and Cowork get the server's tools through desktop app plugin registration. Chat currently needs a separate `claude_desktop_config.json` entry — the plugin's own server declaration doesn't reliably reach Chat (a platform bug). When the bug is fixed, the entry is removed; nothing else changes.
- **Update path.** Merge a PR to the deploy repo, refresh the marketplace clone with `claude plugin marketplace update`, then restart Desktop. Direct commits to `main` don't trigger updates. Quit Desktop before refreshing if a server from that marketplace is running — it holds a lock on the clone.

### Remote services

Not yet built. Deployment guidance is added from the first remote service's experience.

## Consuming a service

**The human operator** needs a user guide, delivered alongside the design documents: what the service does, how to verify it is connected, how to configure it, the operation inventory, and any platform-specific setup such as the Chat config entry. This was missing for the document management server and is now a required deliverable so the gap does not recur.

**The AI** consumes the service through its interface — the operations, their inputs and outputs, and the error reporting. A well-designed interface makes AI-side use self-evident from the operation descriptions the server exposes; no separate consumption standard is needed.

## The sibling-outputs model extends to services

A single design can produce standards, tools, and services as sibling outputs. The design describes the behaviour; each output delivers the part appropriate to its type — guidance into a standard, invokable actions into tools, persistent operations into services. All derive from the design, not from each other, and must not disagree.

The document management design produces a service (the MCP server) and will produce a governing skill (a tool, not yet built). The service provides the primitives; the tool will orchestrate them with document intelligence.

## Boundaries

Services does **not** own:

- **The delivery mechanism** — packaging, plugin structure, registration, and hosting. Infrastructure owns delivery; Services records what a developer needs to build against it.
- **The capability-wide lifecycle** — the Capabilities Development Standard. Services extends it.
- **The cross-review process** — a Working Practices convention. Services records what a developer needs to perform it.
- **Document structure** — Documentation Methodology.
- **Any individual service** — each lives with its owning component.

## Carries to other components

**To Infrastructure:** Infrastructure's `_index.md` should state that it owns delivery of services as well as utilities — services provide capabilities to sessions from outside the session, and Infrastructure delivers them.

**To Core:** the component map and purpose lines carry a Services entry, and the AIDE taxonomy has four capability types — two in-session (standards, tools) and two out-of-session (services, utilities), distinguished by direction of service.

---

Version note: v1 — initial design and cross-review remediation (F2–F13). 2026-09-23.

Version note: v2 — rescoped to broad guidance and knowledge capture: seven formal design concerns replaced with informal design guidance. Definition of done reframed around the development cycle. Added: applicability, classification by entry point, reviewing and testing a service (design cross-review, per-surface and update-propagation testing), the practical build knowledge from the first two services, local deployment facts, remote services, and AI-side consumption — so the development standard can be produced from this design. 2026-09-23. Replaces v1.
