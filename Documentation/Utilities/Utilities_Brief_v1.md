> identity: Utilities_Brief@v1 | doctype: brief | updated: 2026-09-23

# Utilities — Brief

## Purpose

Define what a utility is and how one is developed within AIDE. A utility is an out-of-session tool — it runs outside the AI environment, acts on the corpus or infrastructure, and exits or persists independently of any session. Utilities is the fourth type component in the Capabilities model.

## Objectives

1. A clear definition of what a utility is.
2. How to design and build a utility.
3. How to deploy a utility and where it resides.

## Definition of done

1. What a utility is — distinct from tools and services — is stated.
2. The design and build path is clear enough that someone can create a utility without further methodology guidance.
3. Deployment and ownership are stated — where the code lives, how it's made available, which component owns each instance.

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
