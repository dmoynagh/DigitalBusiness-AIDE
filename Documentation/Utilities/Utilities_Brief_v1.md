> identity: Utilities_Brief@v1 | doctype: brief | updated: 2026-09-23

# Utilities — Brief

## Purpose

Define what a utility is and how one is developed within AIDE. A utility is an out-of-session tool — it runs outside the AI environment, acts on the corpus or infrastructure, and exits or persists independently of any session. Utilities is the fourth type component in the Capabilities model.

## Objectives

1. A clear definition of what a utility is.
2. How to design and build a utility.
3. How to deploy a utility and where it resides.

## Definition of done

1. A developer can tell whether something should be a utility — the definition and the boundaries with tools and services.
2. A developer can design a utility without further methodology guidance.
3. A developer can review and test a utility — cross-review of the design, and testing the built utility against it.
4. A developer can build and deploy a utility so that it is invocable, and knows where it lives and who owns it.
5. The Utilities Development Standard can be produced entirely from the design.

## Target outcome

A deployed Utilities Development Standard.

## Scope

The utility definition, design and build guidance, deployment, and ownership. Broad scope, few constraints — utilities are the simplest capability type and the methodology should reflect that.

## Boundaries

- **The service-vs-utility boundary test** — owned by Services.
- **Build's generic mechanism** — consumed, not restated.
- **Infrastructure** — owns delivery. Currently holds utility instances; individual utilities may move to their owning components.
- **Individual utilities** — each lives with its owning component.

## Linked build outcome

Utilities Development Standard, deployed as a skill in the `aide-dev` plugin.

---

Version note: v1 — initial brief. Revised to reflect broad scope, few constraints. 2026-09-23.
