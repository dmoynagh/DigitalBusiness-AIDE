> identity: _index | doctype: index

# Infrastructure

Role: component design, project design
Aliases: none

Infrastructure defines how to build and deploy utilities, and owns the design of the delivery mechanism (the `aide` dispatcher). It is a methodological component — it does not hold all utility designs. Individual utility designs live with the component or area that knows the most about them, under the what-knows-most-about-it principle.

Infrastructure is machinery that acts on the corpus and environment from outside the AI session. It is never loaded into session context and does not shape in-session decisions.

## Key distinction

Infrastructure utilities are not capability Tools. Capabilities (Standards, Tools) are loaded into the AI session to shape behaviour. Utilities run outside the session, acting on files, folders, and the environment.

## Documents

| Prefix | Document | Type |
|---|---|---|
| Infrastructure_ | CLI Design v1 | design |
| Infrastructure_ | CLI Decisions v1 | decisions |
| Infrastructure_ | Working v1 | working |
| AIDE_Infrastructure_ | MCPDeliveryModel v2 | reference |

## Parts

**binder-builder** (prefix n/a)
The binder assembly utility — design, settings, and README.

**file-update-package** (prefix n/a)
The FUP deployer — design, settings, and README.

**version-cleanup** (prefix n/a)
The version cleanup utility — design, settings, and README.
