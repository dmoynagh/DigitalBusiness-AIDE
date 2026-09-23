> identity: Utilities_Development_Standard@v2 | doctype: standard | updated: 2026-09-24 | uses: Capabilities_Development_Standard@v2

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

A utility has a design. The design describes what the utility does, what it needs, what it produces, and what it enforces. The Capabilities lifecycle applies — design, review, build, deploy, and consumption. There is no authoring phase: the design is the specification, and once reviewed it goes directly to build.

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

**Self-check first.** Before cross-review, check the design against its definition of done and confirm the boundary tests place it as a utility, not a service. Keep it proportionate — a read-through, not a checklist.

**Review the design.** The design is the build specification. Cross-review it with a separate AI directed to find defects against the design's definition of done; triage, remediate, and record in the decisions. Keep it proportionate to the utility's size.

**Test the built utility.** Run it against representative input and confirm its output and effects match the design. For a utility that changes or removes content, exercise its partial-failure behaviour. If the design declares it safe to run again, run it twice and confirm the second run changes nothing. Confirm it is invocable through its deployment form, not just from its source.

## Build

The design document is the build specification. Build creates the utility from the design — typically a script, a small program, or a module within a larger codebase. Build follows Build's generic mechanism. The utility's code is the deliverable.

## Deployment

A utility is deployed when it can be invoked, not just when its code is present. The minimum:

- **Code** placed per the Infrastructure CLI design — a module in the `utilities/` subpackage of the `aide` package (deploy repo, `aide-cli/src/aide/utilities/`) exposing `name`, `description` and `run`.
- **Invocation** as an `aide` CLI command (`aide <name>`) or through a script entry point.
- **Settings file and README** together in the utility's folder with its design.
- **Runtime state** — per-project settings and the log — under `_aide/utilities/<name>/` at the documentation root.

Information. References: `Infrastructure_CLI_Design@v1` for registration, settings layers and the `_aide` folder; the binder builder (`Infrastructure/binder-builder/`, `_aide/utilities/binder-builder/`) as a working example. Implementation choices beyond this contract stay open. Infrastructure owns the deployment path and any packaging.

Information. A utility may also be exposed through a service that wraps its implementation; the session-facing operation is then a service.

## Consumption

A utility is consumed through its README: what it does, how to invoke it, its settings file, and where its output and log go. Follow the existing utilities' READMEs as the model. A utility without a README is not deployed.

## Ownership

**Each utility lives with its owning component.** Utilities is a methodological component — it defines how to build a utility, not where utilities live. Each utility is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v1 — initial standard. Produced from Utilities_Design@v2, including review and testing. 2026-09-23.

Version note: v2 — lifecycle corrected to design, review, build, deploy, consumption. Self-check added before cross-review. Deployment states the minimum contract. Consumption section added — the README. Produced from Utilities_Design@v3. 2026-09-24. Replaces v1.
