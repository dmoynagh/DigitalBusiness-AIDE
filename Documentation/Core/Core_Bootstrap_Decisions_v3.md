# Core Bootstrap — Decisions

> **Version 3** (2026-09-01). Preserves the v2 Bootstrap decision history and records effective
> Profile gating, no-Profile startup behaviour, non-executable `Why`, order-independent
> Contributions and the deliberately pre-Index role of `{bootstrap}`.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

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

## D15 — Effective Profile gates the Contribution startup set

**Decision.** The effective Bootstrap Profile defines the Profile-selected AIDE startup set.
Automatic startup processing considers only applicable Contributions whose owning material/
capability is brought into play by that set, unless a future explicit persistent primitive defines
an exception.

**Reason.** Physical deployment is availability, not startup intent. Without Profile gating, a host
with several deployed AIDE subsets would activate all available Contributions and cease to be
subset-neutral.

## D16 — No Profile does not activate every deployed Contribution

**Decision.** No Profile remains a valid state, but it means there is no Profile-selected AIDE
startup set and therefore no automatic processing of deployed AIDE Bootstrap Contributions merely
because they are physically available.

**Reason.** “No Profile” must not silently mean “all deployed AIDE”. That would invert the purpose
of Profile selection.

## D17 — Profile `Why` is rationale, not applicability syntax

**Decision.** `Why` is concise human/AI-readable rationale for including a Profile entry. It is not
an executable conditional expression and creates no second Scope/applicability language.

**Reason.** Bootstrap needs an explanation for startup selection, not a new rule engine. Conditional
behaviour remains with the substantive owner and normal applicability mechanisms.

## D18 — Bootstrap Contributions are order-independent

**Decision.** Peer Bootstrap Contributions must not require another Contribution to have executed
first or depend on peer startup side effects. Required material presence is expressed through the
normal Dependencies mechanism.

**Reason.** No demonstrated need justifies a startup orchestration/order engine, and platform file
order is not a stable semantic contract.

**Consequence.** If a future startup case genuinely requires ordered actions, design that mechanism
explicitly rather than extending current Contributions implicitly.

## D19 — `{bootstrap}` deliberately remains pre-Index

**Decision.** `{bootstrap}` is a primitive pre-capability/pre-Index discovery cue and does not depend
on Item Type recognition for its own initial discovery.

**Reason.** Bootstrap runs before richer AIDE Index/Item Type machinery can be assumed available.
Requiring that machinery to discover Bootstrap would create a circular startup dependency.

**Consequence.** `{bootstrap}` discovery and Item Type recognition remain intentionally separate.

## D20 — Issue Bootstrap v2

**Decision.** Publish the corrected runtime contract as `AIDE_Bootstrap@v2` with migration posture
`None`.

**Reason.** The startup selection semantics change, but no automatic transformation of existing
governed artefacts is required solely because the Bootstrap release changed.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Dependencies, Core_Bootstrap_Design_v3
References: Core_System_Decisions_v7
