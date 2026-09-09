# AIDE Component Purpose Lines

Version 2. 2026-09-08. Rewritten against the rebuild overview per finding F2. Supersedes the item 7 table in the WIP.

---

## Active components

| # | Component | Purpose line | Key boundaries |
|---|---|---|---|
| 1 | Principles | Give any AI the durable, portable reasoning and premises to think and act well — independent of platform or methodology. | Portability is the defining test. Includes verification as a premise and the base human-side behavioural premises. |
| 2 | Working Practices | Own the conventions and behaviours for how an AI and user actually work together across surfaces. | Includes the human working model as its own standard. May grow into a container with sub-components. |
| 3 | Documentation Methodology | Define how documents are structured and created — the generic mechanics. | Owns the grammar. Not a registry of types belonging to other components. Specific types live with whoever knows the most. |
| 4 | Project Design | Produce the design specification. | One scalable architecture. Owns both ends of the design-build loop: handoff, return, reconciliation, and the work register. |
| 5 | Build | Take the design specification and execute it — produce the outcome, report what was done. | Creates from the spec, thinking not transcribing. Owns how code is structured. Likely an umbrella with different build paths. |
| 6 | Standards | Make sure standards are applied, honoured and kept current across the environment. | As a capability, owns the definition of a standard and the authoring guidance including leanness. |
| 7 | Tools | Encapsulate a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. | Owns the definition of a tool. Individual tools are owned by their consuming component. |
| 8 | Migration | Keep things current when something they depend on changes — collate, distribute and execute change actions. | Detection varies by consumer; the mechanism is generic. Documents against standards is the primary consumer. |
| 9 | Messaging | Carry a message across any boundary reliably, with a known envelope and delivery convention. | General-purpose transport. Any component or logic can use it. External AI and Code handoffs are consumers, not owners. |
| 10 | External AI | Bring another AI into your work — review, research, parallel solutioning, or consultation. | Modes, not separate components. Consumes Messaging. Mode is the contract; interaction pattern is a separate axis. |
| 11 | Deployment | Get the publishable capabilities live in a session, on whatever surface is in use. | Simple pipeline: build into a plugin, push to marketplace, account reloads. Includes the deployable-length weight gate. |
| 12 | Core | Hold whatever shared requirements have no natural home elsewhere. | Deferred by design, resolved last. Carries the settled Index, Domain and Bootstrap work forward. |

## Held — resolved by demonstrated need

| Candidate | Original rationale | Resolution trigger |
|---|---|---|
| Tags | Removed duplication of labelling behaviour across components. | Reappears if the new design shows the same duplication. |
| Scope | Removed duplication of applicability-decision logic. | Reappears if runtime applicability needs a shared definition. |
| Dependencies | Removed duplication of dependency-declaration behaviour. | Reappears if multiple components need a shared dependency methodology. |

## Deferred

| Concern | Reason | Trigger |
|---|---|---|
| Environment and platform concerns | Single platform, no current need. | Multi-platform deployment or a need to track deployed state. |
