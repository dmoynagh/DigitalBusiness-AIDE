> identity: Utilities_Development_Standard@v1 | doctype: standard | updated: 2026-09-23 | uses: Capabilities_Development_Standard@v1

# Utilities — Development Standard

How to design, review, build, test, and deploy an AIDE utility.

## What a utility is

Information. A utility is an out-of-session tool — using "tool" in the plain-language sense, not as the formal capability type. It runs outside the AI environment, acts on the corpus, and operates independently of any session. It encapsulates a repeatable action so it does not have to be re-derived or re-performed manually each time.

Information. The difference from a tool: a tool runs in-session and serves the session. A utility runs out-of-session and serves the corpus. The difference from a service: sessions connect to a service for capabilities. A utility does its work on its own terms — triggered by a human, a CLI command, a script, or a schedule.

## Applicability

Information. This standard applies when designing, reviewing, building, testing, or deploying an AIDE utility. It does not govern tools, services, or Infrastructure's delivery mechanisms.

## Boundary

A utility is classified by two properties from the Capabilities taxonomy: it runs out-of-session and it serves the corpus. The service-vs-utility boundary test is owned by Services.

A utility and a service can coexist from the same implementation. Classification follows the exposed entry point: the standalone invocation is a utility, the session-facing operation is a service.

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

Recommended. These are not formal concerns with compliance obligations. They are the things a designer naturally addresses when specifying an out-of-session tool. A simple utility may need only a few lines on each; a complex one may need more. Where a concern does not apply, the design says so — the builder needs to distinguish intentional omission from oversight.

**Design fresh.** A utility design is produced fresh, not by modifying a previous version.

## Reviewing and testing a utility

**Review the design.** The design is the build specification. Cross-review it with a separate AI directed to find defects against the design's definition of done; triage, remediate, and record in the decisions. Keep it proportionate to the utility's size.

**Test the built utility.** Run it against representative input and confirm its output and effects match the design. For a utility that changes or removes content, exercise its partial-failure behaviour. If the design declares it safe to run again, run it twice and confirm the second run changes nothing. Confirm it is invocable through its deployment form, not just from its source.

## Build

The design document is the build specification. Build creates the utility from the design — typically a script, a small program, or a module within a larger codebase. Build follows Build's generic mechanism. The utility's code is the deliverable.

## Deployment

A utility is deployed where it can be invoked — deployment means the utility is callable, not just that its code is present. Currently this means the AIDE repository, with invocation through a registered CLI command, a script entry point, or a service that wraps the utility's implementation. Infrastructure owns the deployment path and any packaging.

A utility may also be delivered as part of an MCP server or as a standalone CLI command. The deployment form depends on how the utility is invoked.

## Ownership

**Each utility lives with its owning component.** Utilities is a methodological component — it defines how to build a utility, not where utilities live. Each utility is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v1 — initial standard. Produced from Utilities_Design@v2, including review and testing. 2026-09-23.
