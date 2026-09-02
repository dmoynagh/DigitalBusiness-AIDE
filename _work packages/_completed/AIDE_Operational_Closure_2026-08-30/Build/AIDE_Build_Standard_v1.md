# AIDE Build — Standard

> **Identity:** `AIDE_Build@v1`
> **Common name:** Build
> **Version 1** (2026-08-30). Initial platform-independent execution, validation and return contract.
>
> **Default weight:** Requirement

---

## Purpose

Execute defined work through a WorkPackage, produce the required artefacts/state, validate the actual result, and return evidence without silently taking design authority.

## Applicability

Apply when an AI/environment is acting as the executor of a governed WorkPackage or equivalent explicitly defined Build task.

Build is behavioural. Coding agents, document/work agents and future execution environments may all implement this contract.

## Accept the handoff

Before consequential state change:

- resolve the WorkPackage and authoritative work-specific inputs;
- confirm Objective, Authorised Scope, Required Outputs and Acceptance are materially clear;
- load applicable Standards/Tools needed for the work; and
- return `NotReady`/Blocked if a substantive design gap prevents safe execution.

Do not use design-history material as permission to invent a result that the current handoff does not determine.

## Plan proportionately

Establish a coherent execution sequence proportionate to the work. Trivial work need not generate ceremonial plan artefacts.

Apply configured/governing Review before execution where required or recommended.

## Execute within authority

Resolve ordinary implementation detail autonomously where it remains within scope and does not alter objective, acceptance, major architecture/policy or reserved decisions.

If execution exposes a design-level problem, stop/contain affected work and return the issue rather than adding compensating machinery without authority.

## Validate the result

Test actual outputs/state against the WorkPackage Acceptance and applicable Standards. Validation evidence should be sufficient to support the returned status.

Apply result Review where required/recommended.

## Return outcome

Return an `AIDE_WorkPackage@v1` Outcome with truthful status, work performed, outputs, validation, deviations, remaining work, out-of-scope findings and design feedback.

`Complete` means the defined acceptance is satisfied, not merely that execution ended.

## Failure and resumption

Use `Partial`, `Blocked` or `Failed` distinctly. Preserve safe successful work where appropriate and state the actual resulting state. Re-running should resume or reproduce intentionally and avoid duplicate side effects where practicable.

## Platform boundary

Target-platform commands, plugin/skill structures, repositories, toolchains and environment mechanics belong in platform Build Standards/Tools/configuration. They may vary without changing this contract.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v1, AIDE_Review@v1
References: AIDE_WorkPackage@v1
