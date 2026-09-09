# Core — Design Documentation Working

Version 1. 2026-09-08. Working document — concept and principle, not placed.

---

## Status

Exploratory shaping session. Recording thoughts, knowledge, ideas and decisions as concept and principle. Residence of each piece not yet decided. When complete, consolidate and work out where each item belongs.

---

## The anchor — what AIDE is for

Core states AIDE's outcomes; components deliver them. The design use case is the lead outcome, delivered by the Project Design component.

AIDE is ambient until triggered by self-declaration. A document opts into AIDE's capabilities by carrying the information that maps it into scope. No declaration, no imposition — it is just a document. This is facilitate-not-constrain expressed as a mechanical principle.

---

## Forks abandoned

An earlier proposal split AIDE into two forks — Development (building the framework) and Framework (using it). Abandoned because it duplicates: every component would be described twice with most of the substance shared.

Instead, one project per component carries both concerns. The applied-behaviour lens — how the component operates once the framework is live — is included in each component's design where relevant, not as a fixed required element on every design.

---

## Structure — design projects and design areas

### Design project

A container grouping all design material for an area of work. "Project" is the term despite collision with Claude/chat projects — it is the natural word, and the collision is handled by context. "Design project" disambiguates when needed.

### Design area

A bounded part of the thing being designed. Areas are the groupings within a project — each is a section of the overall design. Terminology settled: **project** as the container, **area** as the grouping.

CMS is the reference example: areas include query, views, relationships, dependency system, keys, change log, localisation, pipeline, predicate engine, schema, tags, values — each a different part of the overall design.

### Folder structure

Folders are free organisation only. They carry no meaning the system depends on. A folder might hold one area, several areas, or areas might sit loose with no subfolders. Binders retire the old flatness constraint — a binder can carry a whole project or a segment, so subfolder hierarchies are now practical without paying a sync cost.

### Area identity and hierarchy

Areas are declared on the document, not by folder position. Expressed as a delimited **path** relative to a context-defined root. The path encodes the hierarchy — each segment is a level, shared prefixes show what is related.

Example: CMS / query / SQL — CMS is the project, query is the area, SQL is the sub-area.

Areas can be hierarchical. A sub-brief either opens a new area or sections an existing one — the brief itself declares which by carrying a different or the same area identity.

### Path — the general property

The property is **path**, not "design path." It is a general locating mechanism, not design-specific. Build documentation or anything else uses the same concept. The path is relative to a context-defined root; what the root represents depends on the domain. In a design project, the root is the project.

---

## Expand and collapse

The brief is always conceptually present. Big areas earn a separate brief and separate design documents. Small areas collapse the brief inline into the design document. Same methodology, scaled to the weight of the area.

A brief can branch to sub-briefs, to design documents, or both. The author decides per case and records it — flexible where it should be, explicit so the system knows.

---

## Document handling model

Three self-declared properties compose to give a document its behaviour:

1. **Path** — where it sits in the design structure, relative to a root.
2. **Doc type** — what it is. A known doc type inherits functionality and behaviour automatically. Declare the type and the behaviour comes with it.
3. **Blocks** — the granular unit of functionality. Known defined blocks bring their own logic whether or not the document has a doc type. Include a versioning block and versioning applies. Declare a dependency and the system knows what to do when that standard changes.

Path and doc type are independent and compose. Path is location, doc type is nature. Neither depends on the other.

### Partial application

Blocks work independently of doc type. A freeform document with no doc type can include known blocks, and each block gains its functionality — production guidance, navigation, extraction, and migration scope. Known parts get full support; the rest is carried inert. Functionality degrades gracefully, not all-or-nothing.

### The incentive model

"Define it and you get functionality; don't and it's inert." This is the design principle that lets AIDE be permissive without becoming chaos. You can extend freely — new doc types, modified structures — but you define what you create so the system knows how to handle it. Stay within known structures and you get support for free. Go your own way and you document your own information locally.

---

## Header and footer convention

### Header — triggers and identifies

The header holds what must be seen first because it switches on logic. A machine reading a document starts at the header, sees a doc type, and that fires the doc type skill, loads the rules and functionality, and loads the standard containing that type.

Header carries:
- Path
- Document identity
- Dependencies (change tracking / change management)
- Doc type
- Custom block types (delimited list, if the document includes blocks beyond what the doc type implies)

### Footer — elaborates

The footer holds structural detail needed only after the header has established what the document is. Accessed by jumping to the end, which is fast for both humans and machines.

Footer carries:
- Custom layout and block positioning within the document flow
- Document spec or structure definition for custom documents
- Custom doc type definition, if this document defines its own

### Principle

Header triggers, footer elaborates. Anything that must fire functionality goes up top and stays lean. Structural elaboration goes to the bottom, out of the way but findable. Metadata placement serves both machine navigation and human readability.

---

## AIDE activation model

AIDE is ambient until something triggers its behaviour. The presence of declarations in the header — the doc type above all — is what brings AIDE into play against a document. The header is not just describing the document, it is activating AIDE.

This is opt-in by self-description. No declaration, no imposition. The trigger model is the facilitate-not-constrain principle operating at the mechanical level.

---

## Stable triad

Most designs vary in their stages, but nearly all land on three document types: **brief** (the what — purpose, objectives, requirements, considerations, scope), **design** (the how — the confirmed model and approach), and **decisions** (the knowledge capital — how decisions were made, what was learned along the journey).

---

## Rapid evolution cycle

AIDE is a living, evolving system. Learn something while working, stop, design the component or standard or doc type needed, build it, deploy it — and use it almost immediately. This rapid application development cycle is why migration and change management are fundamental infrastructure, not bolted on.

---

## Open items

1. **Working document** — needs a proper definition as a concept. Flagged, not solved.
2. **Header/footer detail** — which exact properties at which end; the rule is clear but the full list needs pinning.
3. **Residence** — where each piece in this document eventually belongs across the AIDE components. To be consolidated when the shaping is complete.
4. **Path delimiter** — settled as a concept; the exact delimiter and any naming rules are design detail.
5. **Area boundary mechanism** — area boundaries are declared in documents, not by folders. The precise mechanism (property, marker block, doc type implication) is for the design.
6. **Core Brief v2** — drafted but needs rework to reflect this session. The fork structure is abandoned; Core's objectives now include stating AIDE's outcomes with components delivering them.
