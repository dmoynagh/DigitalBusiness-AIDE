# Core

Role: component design

Core is the root entry to AIDE — the framework's self-description, component model, framework-wide requirements, and the map to all components. A reader arriving at AIDE reads Core to understand what AIDE is, what a component is, what the framework expects, and where to find any specific component's design.

## Key definitions at this level

**Component.** A defined area of functionality with a declared purpose, scope, and ownership. It owns its own documents and decisions. It may produce capabilities but need not. It is the functional unit independent of where it lives.

**Capabilities.** A term covering output definitions — Standards, Tools, Utilities. Components that define things delivering and adding functionality.

## Parts

**Structure** (prefix `Core_Structure_`)
How AIDE documentation is physically and logically organised — folder conventions, container labels, the AIDE document concept, path authority, and naming.

**AIDEPrinciples** (prefix `Core_AIDEPrinciples_`)
The operating principles specific to AIDE as a framework — facilitate not constrain, opt-in behaviour, strength model, aliases. Produces a standard for deployment. Distinct from the Principles component, which owns universal, portable premises.
