> identity: Services_Development_Standard@v1 | doctype: standard | updated: 2026-09-23 | uses: Capabilities_Development_Standard@v1

# Services — Development Standard

How to design, build, and deploy an AIDE service.

## What a service is

Information. A service provides persistent operations to AI sessions. It runs as a separate process outside the session, accepts requests from the AI, and performs work the AI delegates to it. The AI is a caller, not the executor.

Information. A service reaches the AI platform as a server — a process the platform connects to and routes calls through. The service is what is designed; the server is how it is delivered. The delivery mechanism is Infrastructure's concern, not a property of the service type.

Information. A service earns its operational cost. The design must justify the out-of-session process — if the AI could perform the work in-session with equivalent safety and consistency, it should be a tool.

## Applicability

Information. This standard applies when designing, building, or deploying an AIDE service. It does not govern tools, utilities, or the infrastructure mechanisms that deliver services as servers.

## Boundary tests

### Service vs tool

If the AI performs the work in-session, it is a tool. If a separate process performs the work and the AI is a caller, it is a service. The test is about who executes, not about what is executed — the same operation could be a tool or a service depending on whether the AI or a separate process performs it.

Information. The execution-context property (in-session vs out-of-session) is a Capabilities taxonomy property. The invocability test that separates standards from tools is owned by Tools. Services references both when classifying.

### Service vs utility

If sessions connect to it for capabilities, it is a service. If it acts on the corpus rather than serving sessions, it is a utility. Both run outside the session; the direction of service distinguishes them. Services owns this test.

## Design concerns

Seven concerns a service developer must address. These are not a template — the developer decides how to meet them, in whatever structure the service demands. They describe what a complete service design covers, so a developer knows what to think about.

**Interface.** What operations the service exposes to callers. Each operation has a name, inputs, outputs, and failure modes. The interface is the contract — what callers can rely on and what the service promises. A service that exposes operations not described in its interface, or whose operations behave differently from their description, is defective.

**Configuration.** What the service needs to know about its environment before it can operate — where to find the things it works with, which are writable, any machine-level settings. The developer declares the configuration lifecycle: when configuration is loaded, when changes take effect, and what a change requires (restart, reload, or immediate effect). A service with no configuration is legitimate. A service that requires configuration should report clearly when configuration is missing or invalid, and should operate correctly with default or empty configuration rather than failing silently.

**Discovery.** How the service finds and registers the things it operates on. Not every service discovers — some take their targets as call-time arguments. But a service that manages a set of resources needs a defined discovery mechanism: what it scans, what qualifies, how naming collisions are handled, and what happens when discovery finds nothing.

**Safety model.** What the service prevents and enforces. Path containment, readonly enforcement, clean-state preconditions, input validation. The service enforces its own safety because the AI cannot — the AI is a caller, not the executor, and has no direct control over what the service does with a request. Safety in a service is not advisory; it is enforced by the process. Where the service delegates work downstream, the developer declares what the service validates before delegation and what enforcement the downstream target is trusted to provide.

**State management.** What state the service holds, how long it persists, and what resets it. Session-scoped state (tracked changes awaiting commit) is different from persistent state (configuration, discovery results held in memory). A service that holds session-scoped state must be clear about what a restart loses and what survives. If the service holds caller-specific state, the developer must declare how that state is partitioned across concurrent callers.

**Error model.** How the service reports problems to callers. Errors carry enough information for the caller to decide what to do — retry, change the request, escalate. Error types are named and consistent across operations so callers can handle them programmatically. A service that returns generic errors or swallows detail forces the caller to guess.

**Lifecycle.** How the service starts, shuts down, and behaves on restart. What it loads at startup, what it discards on shutdown, what requires a restart to take effect. A service developer declares the lifecycle so consumers know what to expect.

Recommended. Not every concern will be substantial for every service. A simple service might have no discovery and no configuration; a complex one might need something this list does not name. The concerns are what to think about, not what to fill in.

## Designing a service

**Design is always required.** A service always has a design. There is no exception for simple services — a service is a deployed process with configuration, lifecycle, and safety obligations that demand the design layer.

**Design fresh.** A service design is produced fresh, not by modifying a previous version. Same principle as tools and standards.

**No prescribed template.** Information. A service design has no fixed structure. The developer decides how to organise it, provided the design concerns are addressed.

**Delivery independence.** A service is designed independently of its delivery mechanism. The interface, configuration, discovery, safety, state, errors, and lifecycle are properties of the service, not of the process that hosts it. In practice, the developer must know enough about the delivery model to avoid designing something the delivery model cannot support — but the developer designs the service's behaviour, not the server's plumbing.

## The sibling-outputs model

Information. A single design can produce standards, tools, and services as sibling outputs. The design describes the behaviour; each output delivers the part appropriate to its type. All derive from the design, not from each other, and must not disagree.

## Build

The specification entering build is the design document — there is no intermediate authored document. Build creates the server from the design. The developer's responsibility at build handoff is a complete, accepted design that addresses the seven design concerns and points the builder at Infrastructure's delivery model and an existing service as a working example.

Cross-review of the design must be accepted before build.

## Deployment

Once built, the server is deployed through Infrastructure's delivery model. Currently this means a local MCP server delivered via a marketplace plugin. The developer does not own deployment mechanics — Infrastructure owns the delivery pipeline.

Information. The same service design could be delivered differently in future — as a hosted endpoint, a different protocol, or a different transport. The delivery-independence principle in the design section exists to keep that path open.

## Consumption

Every service has a user guide alongside its design documents. The user guide covers: what the service does, how to verify it is connected, how to configure it, the operation inventory, and any platform-specific setup. The user guide serves the human operating the service, not the AI consuming it.

Information. The AI consumes the service through its interface — the operations, inputs, outputs, and error model. A well-designed interface makes AI-side consumption self-evident from the tool descriptions the server exposes.

## Ownership

**Each service lives with its owning component.** Services is a methodological component — it defines how to build a service, not where services live. Each service is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v1 — initial standard. Authored fresh from Services_Design@v1. Seven design concerns, two boundary tests, delivery independence, user documentation as a deliverable. 2026-09-23.
