> identity: Utilities_Brief@v1 | doctype: brief | updated: 2026-09-23

# Utilities — Brief

## Purpose

Define what a utility is and how one is developed within AIDE. Utilities is the fourth type component in the Capabilities model — it owns the methodology for out-of-session, corpus-serving capabilities.

## Objectives

1. A definition of what a utility is, distinct from services and tools.
2. Design concerns specific to utilities, derived from the three working examples (binder builder, version cleanup, file update package).
3. The relationship to Infrastructure stated clearly — Infrastructure currently holds utility instances and delivery, but Utilities owns the methodology.
4. A development standard that any utility developer uses.

## Definition of done

1. A clear definition of what a utility is, distinct from services and tools.
2. Design concerns that a utility developer must address.
3. The relationship to Infrastructure is stated without restating it — ownership of instances vs ownership of methodology is clear.
4. The development standard can be authored from the design.

## Target outcome

A deployed Utilities Development Standard that any component author uses when developing a utility.

## Scope

The utility definition, design concerns, development rules, and the relationship to Infrastructure. Individual utilities, the build mechanism, Infrastructure's delivery concerns, and the service-vs-utility boundary test (owned by Services) are out of scope.

## Boundaries

- **The service-vs-utility boundary test** — owned by Services. Utilities references it.
- **The execution-context property** — owned by Capabilities. Utilities references it.
- **Build's generic mechanism** — consumed, not restated.
- **Infrastructure's delivery and operational concerns** — Infrastructure owns delivery and currently holds utility instances. Utilities owns methodology.
- **Individual utilities** — each lives with its owning component.

## Linked build outcome

Utilities Development Standard, deployed as a skill in the `aide-dev` plugin.

---

Version note: v1 — initial brief. 2026-09-23.
