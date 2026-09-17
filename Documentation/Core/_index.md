# Core

Role: component design, project design
Aliases: none

Core is the root entry to AIDE — the framework's self-description, component model, framework-wide requirements, and the map to all components. A reader arriving at AIDE reads Core to understand what AIDE is, what a component is, what the framework expects, and where to find any specific component's design.

## Key definitions at this level

**Component.** A defined area of functionality with a declared purpose, scope, and ownership. It owns its own documents and decisions. It may produce capabilities but need not. It is the functional unit independent of where it lives.

**Capabilities.** An organisational grouping covering standards and tools — the output definitions that extend the development environment. Not a component.

**Utility.** A third kind of output alongside standards and tools. Infrastructure — a repeatable operational task serving the framework's own operation. Utilities are not capabilities.

## Documents

| Prefix | Document | Type |
|---|---|---|
| Core_ | Charter v1 | charter |
| Core_ | Brief v2 | brief |
| Core_ | Design v5 | design |
| Core_ | Decisions v1 | decisions |
| Core_ | Schema Standard v3 | standard |
| Core_ | AIDEMap v3 | reference |
| Core_ | Tags Working v1 | working |

## Parts

**Structure** (prefix `Core_Structure_`)
How AIDE documentation is physically and logically organised — folder conventions, container labels, the index doctype, path authority, and naming.

**AIDEPrinciples** (prefix `Core_AIDEPrinciples_`)
The operating principles specific to AIDE as a framework — facilitate not constrain, opt-in behaviour, strength model, aliases. Produces a standard for deployment. Distinct from the Principles component, which owns universal, portable premises.
