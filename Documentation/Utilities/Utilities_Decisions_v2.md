> identity: Utilities_Decisions@v2 | doctype: decisions | updated: 2026-09-24

# Utilities — Decisions

## D1 — Utilities is a methodological component

Utilities defines how to design, build, and deploy utilities; individual utilities live with the component that knows most about them. This is the same pattern as Standards, Tools, and Services. It completes the four type components under the Capabilities model (Capabilities D1, D6).

## D2 — Broad scope, few constraints

Direction from Dave (2026-09-23): Utilities should be broad in scope with few constraints. A utility is essentially a tool that runs outside the AI environment; the component defines what a utility is, how to design and build one, how to deploy it, and where it resides.

An initial approach — seven formal design concerns mirroring Services — was dropped before drafting as apparatus the type does not need. Utilities is the simplest capability type and its methodology is the lightest of the four. The same direction was later applied to Services (Services D12).

## D3 — "Out-of-session tool" as the plain-language definition

A utility is defined as an out-of-session tool, using "tool" in its plain-language sense. This makes the relationship to tools immediate: the same concept, a different execution context. Cross-review finding F1 noted that "tool" is also a formal capability type; the definition now states explicitly that the plain-language sense is meant.

## D4 — Utilities owns no boundary test

A utility is fully classified by the two Capabilities taxonomy properties — out-of-session and corpus-serving — and by the service-vs-utility test owned by Services. No further test is needed, so Utilities defines none. Adding one would create a second authority on a boundary Services already owns.

## D5 — Classification follows the exposed entry point

A utility and a service can share an implementation. The binder builder exists as a standalone utility (CLI and script use) and as an operation inside the document management service (in-session use). Classification follows the entry point exposed: the standalone invocation is a utility, the session-facing operation is a service. Added from cross-review finding F3, which showed the boundary was otherwise unusable for composed systems.

## D6 — Informal design guidance, with an intentional-omission signal

The design lists what a designer naturally addresses — what it does, input, output, configuration, what it enforces, invocation, idempotency — with no compliance obligations. Cross-review finding F5 pointed out that a builder cannot tell an intentional omission from an oversight. Rather than making the list binding, the design must say when something does not apply. This keeps the guidance light while giving the builder a clear specification.

## D7 — Failure behaviour for utilities that change or remove content

Cross-review finding F6: utilities such as the file update package and version cleanup change or delete content, and a partial failure can leave the corpus damaged. The enforcement item in the design guidance was extended to cover partial-failure behaviour for such utilities, and testing exercises it. This is a targeted addition, not a general failure-handling framework.

## D8 — Deployment means invokable

*Status: extended by D12 — the minimum deployment contract. That deployment means invokable stands.*

Cross-review finding F7: placing code in the repository does not make a utility usable. Deployment is defined as making the utility callable — a registered CLI command, a script entry point, or a service that wraps its implementation. Infrastructure owns the deployment path and any packaging.

## D9 — Cross-review findings not acted on

F2 (corpus or infrastructure) was resolved by aligning to "corpus" as the taxonomy uses it. F4 (binder builder identity and ownership) was not acted on as stated: the design is methodology, not a registry of instances. The example illustrates the transition pattern, and D5 resolves its classification.

## D10 — Review and testing, and the design produces the standard

Per Capabilities D9 and D10: the definition of done is framed around the development cycle, and review is an explicit phase. For utilities, review is proportionate cross-review of the design. Testing the built utility covers representative input, partial-failure behaviour for utilities that change content, a second run for utilities declared idempotent, and invocation through the deployment form. The design holds everything the standard carries, so the standard can be produced from it.

---

Version note: v1 — initial decisions, recorded retrospectively from the design session and cross-review. D1–D10. 2026-09-23.

## D11 — Base lifecycle, and consumption through the README

The design and standard said a utility follows "design, then build, then deploy" — out of step with the base lifecycle, which has review and consumption as phases (Capabilities D9). They now state the base lifecycle: design, review, build, deploy, consumption, with no authoring phase because the design is the specification.

Consumption had no section. A utility is run by a person, and what that person needs is its README: what it does, how to invoke it, its settings file, and where output and logs go. The three existing utilities already work this way and their READMEs are the model. The README is therefore a required deliverable — a utility without one is not deployed — and no consumption standard is needed. This mirrors the service user guide (Services D11) at the lighter weight utilities warrant.

## D12 — The minimum deployment contract

D8 said deployment means invokable but left a developer to work out what that takes. The minimum is now stated: code placed per the Infrastructure CLI design (a module in the `aide` package's `utilities/` subpackage exposing `name`, `description` and `run`); invocation as an `aide` CLI command or a script entry point; a settings file and README alongside, in the utility's folder with its design; runtime state (per-project settings, log) under `_aide/utilities/<name>/`. The Infrastructure CLI design and the binder builder are named as the references. The paths were checked against the repositories: the live `aide` package is in the deploy repo (`aide-cli/src/aide/`), and the binder builder's settings and log are under `_aide/utilities/binder-builder/`.

Implementation choices beyond the contract — language, internal structure, libraries — are left open, consistent with broad scope and few constraints (D2).

---

Version note: v2 — second cross-review remediation. D8 marked as extended by D12. D11 (base lifecycle; consumption through the README), D12 (minimum deployment contract). 2026-09-24. Replaces v1.
