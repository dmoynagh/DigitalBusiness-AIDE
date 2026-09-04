# Core Bootstrap — Decisions

> **Version 2** (2026-08-31). Reissued against current Core/Documentation Methodology and records
> the confirmed Bootstrap/Profile architecture.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## D1 — Bootstrap remains a Core system primitive

**Decision.** Bootstrap belongs to Core.

**Reason.** It operates before individual AIDE components can assume detailed operating material is
in context and is consumed across participating environments.

## D2 — Persistent platform bootstrap is tiny and stable

**Decision.** The machine/platform-level instruction contains only stable Profile discovery and
activation behaviour and changes rarely.

**Rejected alternative.** Hard-code the current AIDE operating set in each platform's permanent
instructions. Rejected because every release/environment change would require machine-level
maintenance.

## D3 — Environment-specific startup posture is a Bootstrap Profile

**Decision.** A Profile identifies only `what`, `why` and `where`.

**Reason.** The Profile is an early-context map, not a second copy of capability behaviour.

## D4 — Bootstrap Contributions are thin and separate

**Decision.** Component early-session contributions are separately deployable from the full
Standard/Tool/guidance.

**Reason.** Startup discovery should not require eager loading of large operating contracts.

## D5 — Lazy context is a first-class goal

**Decision.** Bootstrap establishes awareness, locators and genuinely early checks; detailed
material loads only when relevant.

## D6 — One effective Profile by default

**Decision.** At most one effective Bootstrap Profile applies by default.

**Reason.** No demonstrated need currently justifies merge/precedence machinery.

**Consequence.** Competing Profiles fail visibly until an explicit composition model is designed.
No Profile remains valid.

## D7 — Startup-required presence reuses Dependencies

**Decision.** Bootstrap does not introduce its own dependency grammar.

**Reason.** Dependencies already owns requirement identity and presence/version semantics.

**Consequence.** Bootstrap supplies the startup opportunity and surfaces unresolved requirements;
it does not redefine dependency semantics or trigger blanket startup migration.

## D8 — Bootstrap does not deploy

**Decision.** Missing required material is surfaced at runtime, not silently installed by
Bootstrap.

**Reason.** Requirement, environment state, authority to change the host and deployment action are
separate concerns.

## D9 — Core does not create a new deployment-authority role

**Decision.** Bootstrap refers to the host administrator/controlling deployment process rather than
defining a new formal Core role.

**Reason.** If a formal authority/permission role is needed, its semantics belong with the
environment/deployment process that owns installation and reconciliation.

## D10 — Deployment Set does not erase semantic requirement

**Decision.** A capability/Profile may require an item even if the current Deployment Set omitted
it.

**Reason.** Otherwise a deployment misconfiguration would erase the requirement runtime checking
exists to detect.

## D11 — Bootstrap may be deployed but does not govern Deployment

**Decision.** Bootstrap/Profile/Contribution artefacts may be deployment inputs while AI Deployment
retains deployment semantics.

## D12 — Future trusted acquisition remains possible

**Decision.** Do not block future trusted-source/catalog resolution and authorised automatic
acquisition.

**Boundary.** Source resolution/acquisition is deferred and a Profile locator never grants
installation authority.

## D13 — Generic startup-task orchestration is deferred

**Decision.** Do not create a generic startup task framework.

**Reason.** Profile activation, thin Contributions and startup-required presence checks cover the
demonstrated needs.

## D14 — Bootstrap is subset-neutral

**Decision.** The same stable bootstrap primitive must support full AIDE, Principles/Working
Practices only, another future subset or no Profile.

**Reason.** The activation layer should not force the software-development system into unrelated AI
sessions.

---
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies, Core_Bootstrap_Design_v2
References: Core_System_Decisions_v5
