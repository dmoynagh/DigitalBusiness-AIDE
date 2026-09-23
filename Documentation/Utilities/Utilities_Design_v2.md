> identity: Utilities_Design@v2 | doctype: design | updated: 2026-09-23

# Utilities — Design

## Brief

**Purpose.** Define what a utility is and how one is designed, reviewed, built, tested, deployed, and owned within AIDE.

**Scope.** The utility definition, design and build guidance, review and testing, deployment, and ownership. Broad scope, few constraints — utilities are the simplest capability type and the methodology reflects that.

**Definition of done.**

1. A developer can tell whether something should be a utility — the definition and the boundaries with tools and services.
2. A developer can design a utility without further methodology guidance.
3. A developer can review and test a utility — cross-review of the design, and testing the built utility against it.
4. A developer can build and deploy a utility so that it is invocable, and knows where it lives and who owns it.
5. The Utilities Development Standard can be produced entirely from this design.

**Linked build outcome.** Utilities Development Standard, deployed as a skill in the `aide-dev` plugin.

---

## What a utility is

A utility is an out-of-session tool — using "tool" in the plain-language sense, not as the formal capability type. It runs outside the AI environment, acts on the corpus, and operates independently of any session. Sessions do not call it; it does its work on its own terms — triggered by a human, a CLI command, a script, or a schedule.

A utility extends the development environment the same way a tool extends a session: by encapsulating a repeatable action so it does not have to be re-derived or re-performed manually each time. The difference is where it runs and what it serves. A tool runs in-session and serves the session. A utility runs out-of-session and serves the corpus.

Three working examples: the binder builder (assembles documentation into a single binder file), version cleanup (removes superseded document versions), and the file update package (applies batched file operations from a manifest).

## Boundary

A utility is classified by two properties from the Capabilities taxonomy: it runs out-of-session and it serves the corpus. The service-vs-utility boundary test is owned by Services — if sessions connect to it for capabilities, it is a service; if it acts on the corpus rather than serving sessions, it is a utility.

A thing may start as a utility and become a service when sessions need to call it directly. The binder builder started as a standalone utility and became an operation within the document management service when sessions needed to trigger builds and receive results within a conversation. The utility form and the service operation can coexist — the standalone utility for CLI and script use, the service operation for in-session use. Classification follows the exposed entry point: the standalone invocation is a utility, the session-facing operation is a service, even when both share an implementation.

## Designing a utility

A utility has a design. The design describes what the utility does, what it needs, what it produces, and what it enforces. The Capabilities lifecycle applies — design, then build, then deploy. There is no authored document; the design goes directly to build.

The design should address whatever the utility needs to be built correctly. For most utilities, that means:

- What it does and why it exists.
- What it reads, scans, or receives as input.
- What it produces, changes, or removes as output.
- How it is configured — settings, defaults, what happens when configuration is missing.
- What it enforces — path constraints, validation, anything it prevents. For utilities that change or remove content, how it behaves on partial failure.
- How it is invoked — CLI, script, schedule, or as a reusable implementation called by a service.
- Whether it is safe to run again (idempotency).

These are not formal concerns with compliance obligations. They are the things a designer naturally addresses when specifying an out-of-session tool. A simple utility may need only a few lines on each; a complex one may need more. Where a concern does not apply, the design says so — the builder needs to distinguish intentional omission from oversight.

**Design fresh.** A utility design is produced fresh, not by modifying a previous version. Same principle as all capability types.

## Applicability of the development standard

The Utilities Development Standard applies when designing, reviewing, building, testing, or deploying an AIDE utility. It does not govern tools, services, or Infrastructure's delivery mechanisms.

## Reviewing and testing a utility

**Reviewing the design.** The design is the build specification, so it is what gets reviewed: cross-review by a separate AI directed to find defects, against the definition of done, with findings triaged, remediated, and recorded in the decisions. For a small utility this is proportionately light — the point is an independent check, not ceremony.

**Testing the built utility.** Run it against representative input and confirm its output and effects match the design. For a utility that changes or removes content, exercise its failure behaviour — what it does when it fails partway — because that is where a utility can do lasting damage. If the design declares it safe to run again, run it twice and confirm the second run changes nothing. Confirm it is invocable through its deployment form, not just runnable from its source.

## Building a utility

The design document is the build specification. Build creates the utility from the design — typically a script, a small program, or a module within a larger codebase. Build follows Build's generic mechanism.

The utility's code is the deliverable. There is no intermediate document — the design specifies, build creates.

## Deployment

A utility is deployed where it can be invoked — deployment means the utility is callable, not just that its code is present. Currently this means the AIDE repository, with invocation through a registered CLI command, a script entry point, or a service that wraps the utility's implementation. Infrastructure owns the deployment path and any packaging.

A utility may also be delivered as part of an MCP server (as the binder builder is delivered within the document management server) or as a standalone CLI command. The deployment form depends on how the utility is invoked.

## Ownership

Each utility lives with the component that knows most about it. Utilities is a methodological component — it defines how to build a utility, not where utilities live.

Infrastructure currently holds the three working utility instances (binder builder, version cleanup, file update package). As utility methodology develops, individual utilities may move to the components they serve. Infrastructure's durable contribution is the delivery and operational machinery, not ownership of every utility.

---

Version note: v1 — initial design. Cross-review remediation: F1 (tool disambiguation), F2 (corpus alignment), F3 (classification-follows-entry-point), F5 (intentional-omission signal), F6 (failure behaviour for destructive utilities), F7 (deployment means invokable). 2026-09-23.

Version note: v2 — definition of done reframed around the development cycle. Applicability and reviewing-and-testing added so the development standard can be produced from the design. 2026-09-23. Replaces v1.
