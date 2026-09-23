> identity: Services_Design@v1-draft1 | doctype: design | updated: 2026-09-23

## Brief

**Purpose.** Define what a service is and how one is developed within AIDE, including the boundary tests that distinguish a service from a tool and from a utility. Services is a methodological component — it owns the methodology for building services, not the services themselves. Each service is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The service definition and the boundaries that distinguish a service from a tool and a utility; the design concerns specific to services; the relationship between a service and its delivery as an MCP server; and the development rules. Individual services, the MCP delivery model, packaging, the cross-review process, and document structure are out of scope.

**Target outcome.** A deployed Services Development Standard that any component author uses when developing a service, and hands off for deployment.

**Definition of done.**

1. A clear definition of what a service is, distinct from tools and utilities.
2. Boundary tests that settle whether a given thing is a service, a tool, or a utility.
3. Design concerns that a service developer must address.
4. The relationship to Infrastructure's delivery model is stated without restating it.
5. The sibling-outputs model extends to cover services alongside standards and tools.

## What a service is and does

A service provides persistent operations to AI sessions. It runs as a separate process outside the session, accepts requests from the AI, and performs work the AI delegates to it — filesystem access, git operations, external process invocation. The AI is a caller, not the executor.

This is the fundamental distinction from a tool. A tool encapsulates a procedure the AI performs in-session. A service encapsulates operations a separate process performs, which the AI calls. The service has its own lifecycle, its own configuration, and its own safety enforcement — none of which depend on the session that calls it.

A service reaches the AI platform as a server — a process the platform connects to and routes calls through. Currently, this means an MCP server; the delivery mechanism is Infrastructure's concern, not a property of the service type. The service is what is designed; the server is how it is delivered.

## Two boundary tests

### Service vs tool

If the AI performs the work in-session, it is a tool. If a separate process performs the work and the AI is a caller, it is a service.

The test is about who executes, not about what is executed. File operations could be a tool (the AI writes to disk using platform-native capabilities) or a service (a server writes to disk on the AI's behalf with safety guarantees the platform doesn't provide). The question is whether the AI performs the steps or calls something that does.

### Service vs utility

If sessions connect to it for capabilities, it is a service. If it acts on the corpus rather than serving sessions, it is a utility.

A utility runs on its own terms — triggered by a human, a script, or a scheduled task. It does not accept requests from sessions. A service exists to be called by sessions. Both run outside the session, but the direction of service is different: a utility serves the corpus, a service serves the session.

A thing may start as a utility and become a service when sessions need to call it directly rather than consuming its output after the fact. The binder builder started as a utility and became a service operation (within the document management server) when sessions needed to trigger builds and receive the result within a conversation.

## What Services owns

### The service definition

What a service is, what it does, and what distinguishes it from a tool and a utility. The definitions are stated above. Services owns the service definition and the service-vs-utility boundary test. The execution-context property (in-session vs out-of-session) is a Capabilities taxonomy property; the invocability test that separates Standards from Tools is owned by Tools. Services references both when classifying.

### The design concerns

Seven concerns a service developer must address. These are not a template — the developer decides how to meet them, in whatever structure the service demands. They describe what a complete service design covers, so a developer knows what to think about.

**Interface.** What operations the service exposes to callers. Each operation has a name, inputs, outputs, and failure modes. The interface is the contract — what callers can rely on and what the service promises. A service that exposes operations not described in its interface, or whose operations behave differently from their description, is defective.

**Configuration.** What the service needs to know about its environment before it can operate — where to find the things it works with, which are writable, any machine-level settings. The developer declares the configuration lifecycle: when configuration is loaded, when changes take effect, and what a change requires (restart, reload, or immediate effect). A service with no configuration is legitimate (the dispatch server has none). A service that requires configuration should report clearly when configuration is missing or invalid, and should operate correctly with default or empty configuration rather than failing silently.

**Discovery.** How the service finds and registers the things it operates on. Not every service discovers — dispatch takes its targets as call-time arguments. But a service that manages a set of resources (document sources, connection targets, queues) needs a defined discovery mechanism: what it scans, what qualifies, how naming collisions are handled, and what happens when discovery finds nothing.

**Safety model.** What the service prevents and enforces. Path containment, readonly enforcement, clean-state preconditions, input validation. The service enforces its own safety because the AI cannot — the AI is a caller, not the executor, and has no direct control over what the service does with a request. Safety in a service is not advisory; it is enforced by the process. Where the service delegates work downstream, the developer declares what the service validates before delegation and what enforcement the downstream target is trusted to provide.

**State management.** What state the service holds, how long it persists, and what resets it. Session-scoped state (tracked changes awaiting commit) is different from persistent state (configuration, discovery results held in memory). A service that holds session-scoped state must be clear about what a restart loses and what survives. If the service holds caller-specific state, the developer must declare how that state is partitioned across concurrent callers.

**Error model.** How the service reports problems to callers. Errors carry enough information for the caller to decide what to do — retry, change the request, escalate. Error types are named and consistent across operations so callers can handle them programmatically. A service that returns generic errors or swallows detail forces the caller to guess.

**Lifecycle.** How the service starts, shuts down, and behaves on restart. What it loads at startup, what it discards on shutdown, what requires a restart to take effect. A service author declares the lifecycle so consumers know what to expect — a restart after configuration change is a design choice, not a surprise.

### The relationship to delivery

A service is designed independently of its delivery mechanism. The MCP server — the process, the transport protocol, the marketplace plugin packaging — is Infrastructure's concern. The service author designs the service; Infrastructure delivers it.

This separation means the same service design could be delivered as a local MCP server today and as a hosted service tomorrow without the service design changing. The interface, configuration, discovery, safety, state, errors, and lifecycle are properties of the service, not of the process that hosts it.

In practice, the service author must know enough about the delivery model to make sound design choices — a service that requires persistent state across Desktop restarts is making a claim the local delivery model doesn't support. But the author designs the service's behaviour, not the server's plumbing.

### The relationship to Build

The design document is the build specification for a service — there is no intermediate authored document. Build creates the server from the design. Build standards for the service build domain — the type-specific conventions for building services — belong in the Services Development Standard. Build owns the generic mechanism; Services owns the domain knowledge of how to build a service.

## The sibling-outputs model extends to services

A single design can produce standards, tools, and services as sibling outputs. The design describes the behaviour; each output delivers the part appropriate to its type — guidance into a standard, invokable actions into tools, persistent operations into services. All derive from the design, not from each other, and must not disagree.

This is already happening. The document management design produces a service (the MCP server) and will produce a governing skill (a tool, not yet built). Both derive from the same design. The service provides the primitives; the tool orchestrates them with document intelligence.

## Developing a service

**Design is the default.** A service always has a design. There is no equivalent of the tool exception ("simple enough that a design would restate rather than elaborate") because a service is a deployed process with configuration, lifecycle, and safety obligations — these demand the design layer.

**Design fresh.** A service design is produced fresh, not by modifying a previous version. Same principle as tools and standards.

**No prescribed template.** A service design has no fixed structure. The author decides how to organise it, provided the design concerns are addressed.

**Build references.** The service design should point the builder at Infrastructure's MCP delivery model and at an existing service as a working example. These are reference documents for the builder, not standards dependencies.

**User documentation.** Every service has a user guide alongside its design documents — what the service does, how to verify it is connected, how to configure it, the operation inventory, and any platform-specific setup. The user guide serves the human operating the service, not the AI consuming it.

## Boundaries

Services does **not** own:

- **The MCP delivery model** — how a service becomes an MCP server, how it is packaged as a marketplace plugin, how it reaches each surface. Infrastructure owns delivery.
- **The development rules** — the capability-wide development rules in the Capabilities Development Standard apply to services the same way they apply to tools. Services consumes them.
- **The cross-review process** — a Working Practices convention consumed by all components.
- **Document structure** — Documentation Methodology.
- **Any individual service** — each lives with its owning component.
- **Hosted services** — cloud-hosted, always-on services (framework inbox, assurance data logger) follow the same design concerns but have a different delivery model. The delivery distinction is Infrastructure's; the service design methodology is the same.

## Carries to other components

**To Infrastructure:** Infrastructure's `_index.md` currently says it "defines how to build and deploy utilities." This needs updating to include services — Infrastructure defines how to build and deploy utilities and how to deliver services (the MCP delivery model). The key distinction already there describes utilities as infrastructure that acts on the corpus from outside the session. Services need a parallel statement: services provide capabilities to sessions from outside the session. Infrastructure owns delivery of both.

**To Core:** the component map and purpose lines need a Services entry. The AIDE taxonomy expands from three capability types (standards, tools, utilities) to four (standards, tools, services, utilities) — or, more precisely, two in-session capabilities (standards, tools) and two out-of-session types (services, utilities), distinguished by direction of service.

---

Version note: v1-draft1 — initial design. Two boundary tests, seven authoring concerns, delivery separation, sibling-outputs extension. Derived from the two working examples (dispatch server, document management server). 2026-09-23.

Version note: v1 — cross-review remediation. F2: definition changed from "cannot do" to delegation. F3: boundary ownership corrected. F4: authoring concerns → design concerns, Author fresh → Design fresh. F5: Build relationship added. F8: delivery made platform-neutral. F9: "and exits" removed from utility boundary. F10: configuration lifecycle declared not mandated. F11: user documentation added as deliverable. F12: caller isolation added to state management. F13: safety delegation model added. 2026-09-23. Replaces v1-draft1.
