# Project Handoff — AI Deployment → Build

> Transfer/reconciliation artefact. Not an authoritative corpus master.

## Reason for the Handoff

AI Deployment has reconciled the Build/Deployment seam so that semantic production remains upstream in Build and Deployment-time composition is limited to mechanical target assembly of already built material.

No new Build mechanism is being prescribed from AI Deployment. One interface point should be checked against the current Build masters.

## Build-owned interface point

AI Deployment needs the Build/package handoff to make clear, directly or through the applicable representation/package contract:

1. the authoritative/canonical source identity/version provenance for the built material;
2. the package/build identity/integrity needed to identify the concrete Build output; and
3. whether the supplied output is:
   - a target-compatible member/contribution that downstream Deployment may mechanically assemble with other built members; or
   - an assembled consumption artefact that is itself the authorised Build output and therefore must be replaced by another Build output when its semantic/member composition changes.

This distinction prevents Deployment from treating an opaque assembled Build artefact as permission to semantically rebuild it, while still allowing set-aware deterministic mechanical assembly where that is part of target reconciliation.

## Requested Build reconciliation

Check whether the current Build Design/Standard/Tool/package-manifest contract already makes this distinction and provenance sufficiently explicit.

If yes, no Build change is required.

If not, tighten the Build-owned handoff/output contract in the next appropriate Build pass. Do not move Deployment Set ownership, target reconciliation, target mutation policy or runtime verification into Build.
