> identity: Services_Decisions@v3 | doctype: decisions | updated: 2026-09-24

## D1 — Services is a methodological component, same pattern as Tools and Standards

Services defines how to create its type. Individual service instances live with their consuming component. This follows the common pattern established for Standards, Tools, and Infrastructure — methodological components own the methodology, not the instances. The document management service lives with Infrastructure; the dispatch service lives with Orchestration. The alternative — Services holding all services — was rejected for the same reason it was rejected for Tools: it violates the what-knows-most-about-it ownership principle.

## D2 — Two boundary tests, not one

A single boundary test would conflate two distinctions that need separating. The service-vs-tool boundary is about who executes (the AI or a separate process). The service-vs-utility boundary is about direction of service (serves sessions or serves the corpus). These are orthogonal. A thing that runs outside the session could be either a service or a utility; you need both tests to classify it.

The direction-of-service test is the heart of the component — it governs what belongs here. The execution-context boundary (in-session vs out-of-session) is a Capabilities taxonomy property that Services references but does not own.

## D3 — The AI-as-caller distinction is the governing difference from tools

The fundamental difference between a service and a tool is not persistence, configuration, or safety enforcement — those are consequences. The governing difference is that the AI is a caller, not the executor. For a tool, the AI performs the procedure. For a service, a separate process performs the work and the AI receives results.

This matters because it changes what the design concerns must cover. A tool author addresses the procedure the AI will follow. A service author addresses the interface the AI will call, the safety the process will enforce, and the state the process will manage — none of which the AI controls.

## D4 — Seven design concerns, derived from the two working examples

*Superseded by D12 — the seven concerns became informal design guidance. Retained for the derivation history.*

The seven concerns were derived by examining what the dispatch server and document management server each needed, then generalising. Both servers needed an interface and an error model. Document management additionally needed configuration, discovery, a safety model, state management, and lifecycle. Dispatch needed none of those four — it is stateless, configurationless, and its safety model is trivial (delegate to the target).

This asymmetry is expected and healthy. Not every concern will be substantial for every service. A simple service might have no discovery and no configuration; a complex one might need something this list does not name. The concerns are what to think about, not what to fill in. This is the same principle established for tool authoring concerns in Tools D3.

The seven are deliberately different from the seven tool concerns (inputs, preconditions, procedure, decision points, escalation, outputs/effects, failure behaviour). Tools' concerns describe a procedure the AI performs. Services' concerns describe a process the AI calls. The overlap is intentional where it exists (interface maps loosely to inputs/outputs; error model maps to failure behaviour) and the differences reflect the different execution context.

## D5 — Services always require a design

Tools allows authoring straight to a tool when the action is simple enough that a design would restate rather than elaborate. Services has no such exception. A service is a deployed process with configuration, lifecycle, and safety obligations — these are design concerns that need to be worked through before code is written, even for a simple service. The dispatch server is about as simple as a service gets, and its design still resolved non-trivial questions (what targets to support, how to handle timeout, what error model to use).

## D6 — The delivery separation is a design principle, not just an ownership statement

Stating that Infrastructure owns delivery is an ownership fact. The design principle is stronger: a service is designed independently of how it is delivered. The interface, configuration, discovery, safety, state, errors, and lifecycle are properties of the service. The MCP transport, stdio framing, marketplace packaging, and config-entry bootstrap are properties of the delivery mechanism.

This means the same service design could be delivered differently — as a local MCP server today, as a hosted service tomorrow, or as a different protocol entirely — without the service design changing. The separation is not aspirational; it is how the document management server was actually designed (the design says nothing about MCP, JSON-RPC, or stdio).

In practice, the service author must know enough about the delivery model to avoid designing something the delivery model cannot support (persistent cross-restart state on a local server, for example). The design acknowledges this with a proportionate statement rather than formalising a dependency.

## D7 — The sibling-outputs model extends naturally

A design already can produce standards and tools as sibling outputs (Tools D6). Extending to services adds no new mechanism — the same rule applies: all outputs derive from the design, not from each other, and must not disagree.

The document management component is the first concrete case: its design produces a service (the MCP server, built and deployed) and will produce a governing skill (a tool orchestrating document intelligence using the server's primitives, not yet built). Both are specified in the same design. The service provides format-agnostic file operations; the tool will add AIDE document vocabulary on top.

## D8 — The naming: "service" is the designed thing, "server" is the delivered thing

This parallels the existing taxonomy. A standard is delivered as a skill. A tool is delivered as a skill. A service is delivered as a server. The designed thing and the delivered thing have different names because they have different owners and different concerns.

"Service" was chosen over "server" because the design methodology is about what is built and why — the service's interface, safety model, and lifecycle — not about the process mechanics. "Server" stays as the delivery term in Infrastructure's MCP delivery model, where the process mechanics are the subject.

## D9 — Hosted services follow the same design methodology

*Status: revised by D12 — the seven design concerns it lists are now informal design guidance. That hosted services follow the same methodology stands.*

The design scope note says hosted services (cloud-hosted, always-on — the framework inbox and assurance data logger discussed in the orchestration and assurance designs) follow the same design concerns but have a different delivery model. The design methodology — interface, configuration, discovery, safety, state, errors, lifecycle — applies regardless of where the process runs. What changes is Infrastructure's delivery concern: local MCP server vs cloud-hosted endpoint.

This means Services does not need a "local vs hosted" split in its methodology. It provides one set of design concerns. Infrastructure provides different delivery models for each hosting context.

## D10 — Configuration reporting without exposing filesystem paths to the AI

A service that requires configuration should report its status to callers — whether it is initialised, how many resources it discovered, what their names are. It should not report filesystem paths, config file locations, or other machine-level detail to the AI. The AI does not need to know where the config file lives; the human does, and that belongs in the user guide.

This was raised during the document management server testing (2026-09-23) when discussing a status/initialise tool. The principle: the service reports operational status (what it can do); the user guide explains setup (how to configure it). The boundary is clean and avoids the AI surfacing machine-specific paths it has no use for.

## D11 — User documentation is a service deliverable

Every service should have a user guide alongside its design documents. The user guide covers: what the service does, how to verify it is connected, how to configure it (the config format and location), the tool/operation inventory, and any platform-specific setup (such as the chat config entry for the MCP platform bug workaround). The user guide is for the human operating the service, not the AI consuming it.

This was identified as missing during the document management server testing — the design documents exist but no user-facing guide does. Adding user documentation as a named deliverable prevents the same gap recurring for future services.

---

Version note: v1-draft1 — initial decisions. D1–D11 from the design session. 2026-09-23.

Version note: v1 — cross-review remediation. F3: D2 boundary ownership corrected. F4: D4 heading updated (authoring → design concerns). D3/D4/D9 terminology aligned (authoring → design concerns). 2026-09-23. Replaces v1-draft1.

## D12 — Broad scope, few constraints: design concerns become informal guidance

The seven formal design concerns (D4) were derived from two services and presented as if universal. Several — configuration, discovery, safety model, state management — were specific to the services built so far and could be irrelevant or obstructive for future ones. Direction from Dave (2026-09-23): the component should be broad in scope with few constraints, like Utilities. Its primary purpose is to guide service creation and record what has been learned — issues, solutions, best practice, approach — so services get easier to build.

The concerns were replaced with an informal list of what a designer naturally addresses, with explicit permission to omit or extend, and a requirement to say when something doesn't apply. The practical knowledge (framing, encoding, status reporting, safety enforcement, deployment facts) is kept as recorded learning rather than prescription.

## D13 — Build and deployment knowledge lives in the design

The v2 draft said practical building knowledge was "delegated to the development standard". That contradicts the rule that the standard is produced from the design (Standards D24, Capabilities D10). All build and deployment knowledge — the proven server patterns, the JSON-RPC framing and Windows encoding fixes, status-not-paths reporting, plugin structure, surfaces, the Chat workaround, and the update path — is now in the design, with the reasoning. The standard carries the lean operational version.

## D14 — Review and testing for services

Services previously had only "cross-review accepted" as a build precondition. Per Capabilities D9, review is now an explicit phase. For services it has two parts: cross-review of the design (the build specification) before build, and testing the built server during build — every operation against the design including failure paths, working on each surface it targets, and update propagation after the first update. Per-surface testing is required because the surfaces register servers by different paths: the delivery model testing found servers working on some surfaces and not others. The probe technique (an operation returning origin, timestamp, and runtime ID) is recommended because it was how the delivery model was proven.

## D15 — Remote services recorded as a placeholder, not designed

Remote (hosted) services follow the same design guidance (D9). No remote service has been built, so the design and standard record a placeholder: build and deployment knowledge is added from the first remote service's experience, the same way local knowledge came from the first two local services. Designing remote delivery in advance would be apparatus without a demonstrated consumer.

---

Version note: v2 — D12 (broad scope; design concerns become informal guidance; D4 superseded), D13 (build and deployment knowledge lives in the design), D14 (review and testing for services), D15 (remote services as placeholder). 2026-09-23. Replaces v1.

## D16 — Build patterns are information; only framing and encoding are required

The standard presented raw JSON-RPC, no MCP SDK, CommonJS and Python-standard-library-only as the way to build a service. Those are what the first two services chose and they work, but nothing in the platform requires them — a future service may be better served by an SDK or a library. They are now recorded as Information, a proven approach. Two things stay Required because they are interoperability facts, not choices: newline-delimited message framing (Content-Length framing times out silently on Claude Desktop) and UTF-8 (the Windows default codepage corrupts non-ASCII content). This keeps the component broad in scope with few constraints (D12).

## D17 — Persistence is not what defines a service

The definition said a service "provides persistent operations". Persistence is a lifecycle characteristic — a service may stay up with its host, start per request, or be hosted always-on — and making it part of the definition would misclassify a short-lived service and suggest a long-running utility is a service. The defining property is the one D3 already names: sessions call it and a separate process does the work. A service is now defined as providing out-of-session operations that sessions call. The same wording replaces "persistent operations" in the sibling-outputs model in Tools and Services.

---

Version note: v3 — second cross-review remediation. D9 marked as revised by D12. D16 (build patterns become information; framing and UTF-8 stay required), D17 (persistence is not service-defining). 2026-09-24. Replaces v2.
