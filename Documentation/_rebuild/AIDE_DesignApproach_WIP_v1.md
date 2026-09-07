# AIDE — Design Approach WIP

Version 1. 2026-09-08.

Status: unmanaged working document. Holds the design approach agreed on 8 September 2026,
and where each part of it goes when the AIDE documents are authored. Persists until that
content has been written into the masters, then retires.

Why it is separate from the AIDE Rebuild WIP: the rebuild WIP holds the component-by-component
design work. This holds a cross-component change to how design itself is done, plus a
placement plan that touches four topics. Mixing them would bury it.

---

## 1. What this is

On 8 September Dave raised that the rebuild was going slowly and the working relationship was
not gelling — work becoming complex and cluttered quickly, unfamiliar terms and framings
requiring translation, agreed models not being carried through, and rework as a result. The
session diagnosed the causes and arrived at a design approach that addresses them.

The approach is Dave's. Most of it was already implicit in how he works; this session made it
explicit and testable.

---

## 2. The approach

### 2.1 The value of the top layers

The top two levels of design — purpose, and the model and approach — have close to a
one-to-one relationship with the success of the project. Everything built, delivered,
deployed and maintained traces back to their quality.

The overview is therefore the highest-value work, not the preamble to it. This matters as a
belief and not only a rule: it redirects the pull toward actionable work rather than fighting
it. Time at the overview level is the highest-return time available.

### 2.2 Design is layers

Purpose, then objectives and requirements and considerations, then the model and approach —
how it is architected, its base principles and framework — then implementation.

Each layer is the one above at greater depth.

### 2.3 The context rule

Every element's place in the model must be visible.

The model is part tree, part web, part horizontal. An element may relate to two or three
things above it, or span everything as a cross-cutting concern. It is not about tying an
element to a position in a tree.

Context is carried in the element's own description, not in separate wiring, references or
notation. It is stated explicitly only where it cannot be implied or inferred.

Connecting an element up is a design-time act before it is a documentation act: it is done so
the designer can see where the element fits, which is what makes anomalies, deviations and
branches visible.

### 2.4 The overview as the map

Read the overview once and it builds the whole picture of the design's structure and
framework. Then any element can be placed against it quickly — which part does this relate
to, where does it sit in the model.

An element that cannot be placed is either a branch, or evidence the overview is missing
something. Both are findings.

This gives the overview structural work to do, not decorative work, and it is why the
overview must be genuinely complete at the top.

### 2.5 The connection runs both ways

When something is becoming too hard, difficult or expensive to implement, that is often an
indication the model or design needs review — not that the implementation needs more
cleverness.

At each implementation decision, ask whether a change in the model would make this better,
easier, more robust or more comprehensive.

Identifying a possible improvement does not mean making it. It is assessed, on a cost-benefit
judgement. A single small improvement is usually absorbed. **The same accommodation recurring
across several elements is the strongest indicator it should be escalated**, however small
each instance looks. Recurrence is visible from across the work in a way it is not from any
single element.

### 2.6 Simple and well-conceived is a goal

A simple, well-conceived model produces simpler and clearer code, easier maintenance, and
easier uptake by someone new. Over-complication is not merely untidy — it defeats the
objective.

Output markedly more elaborate than the intent above it is a warning: either the intent was
more complex than it looked, or it has been over-built.

### 2.7 Design and build

Design produces a good definition and specification. Build creates from it, thinking rather
than transcribing, and owns how the code is structured. The design tree does not dictate the
build's structure.

### 2.8 No apparatus

A clear principle is applied, not implemented through stages, phases, buckets or machinery.
Adding a mechanism a principle did not ask for is the failure, not the delivery — the
mechanism masks the intent it was meant to serve.

Worked example: the rebuild refresh principle was simple — confirm the new design, then check
old material against it and carry only what earns a place. Six stages, a two-part sweep and
three buckets were built on top of it. The scaffolding was dropped on 7 September because
tracking it displaced deciding.

---

## 3. The working method

### 3.1 Two counterforces

Dave ranges around and brain-dumps; that is how he generates, and capture-and-place exists to
serve it. Claude gravitates hard toward actionable and executable work because the overview
feels abstract, and Dave has had to work to hold Claude at the overview level.

The method resolves both the same way.

### 3.2 Stay at the overview until it is complete enough

Complete enough means the layer below could be executed excellently from it, by someone who
was not part of the conversation. Do not descend before that.

### 3.3 Probe, do not dive

Claude's energy goes into completing the overview: ordering Dave's brain dump into it,
reading it back for cohesion, prompting on gaps, and probing — taking something the overview
treats as a boundary and asking what lies beyond it. That reliably surfaces gaps neither
party knew were there.

### 3.4 Understand the model before designing against it

Know what the model is, why it is shaped that way, and what it implies. Then the detail
largely falls out of it. Deriving a solution from a single requirement, without that
understanding, produces work broader than needed or inconsistent with everything around it.

### 3.5 Commit within the model

Where purpose, model and approach settle a question, decide it and move on. Only surface a
fork the model genuinely does not settle and that would materially shape the design.

Passing everything up is the same failure as branching, just noisier.

### 3.6 Language

Plain English wherever it will do. Use the terms already in use on the project; flag a new
term rather than introducing it silently. Say what an element is in ordinary words before
defining it. Meaning first, code second.

---

## 4. The four weaknesses, worked through

Claude raised four weaknesses of strict layered design. Dave worked each. Three were already
answered by principles he had settled.

**1. Cross-cutting concerns.** Some concerns span every branch and a pure tree has nowhere to
put them. Answered by the context rule: it is not about position in a tree, it is about
context being clear. A cross-cutting concern is described as such.

**2. Top-down can harden a wrong model before implementation tests it.** Elaborate lower
layers can make a wrong upper layer look more settled rather than less. Answered by the
two-way connection — difficulty is evidence about the model, and the question is asked at
every implementation decision rather than only when something visibly breaks.

**3. Rigidity and ceremony.** "Connect every element upward" could harden into mandatory
citation and become apparatus. Collapsed into the context rule, which already limits explicit
statement to where it cannot be inferred.

**4. The design tree is not the build structure.** Answered by the existing design-build
separation: design produces the specification, build creates from it and owns its own
structure.

Note: only weakness 2 needed genuinely new material, and even that turned out to be the
existing build-side cost-and-complexity flag pointed in a new direction. A coherent principle
absorbing its own weaknesses is a good sign about the principle.

---

## 5. Deployment

Settled 8 September and already in place.

**One skill, `aide-design-check`**, holding the value, the layering model, the working method
and two checks. Installed at account level, so it reaches every project including new ones,
with nothing to add or maintain per project.

**A bootstrap line in account-level instructions** ("Instructions for Claude", Settings >
General): for any work involving design, architecture or specification, read the skill before
starting and apply it. The trigger condition is "am I doing design work", which fires more
reliably than "do I need design discipline".

**Project instructions hold no design material.** They were used briefly and cleared.

Two checks in the skill:

- **Check 1 — is the overview complete enough?** Could the layer below be executed excellently
  from it by someone not in the conversation. If no, do not descend; probe instead.
- **Check 2 — does the design hold against the overview?** Per element: can it be placed; is
  its context clear in its own description; is it proportionate to the intent above it; was it
  derived from the model or from a single requirement. Plus a one-time coverage check when the
  design is called done.

Stated limit: the bootstrap raises the odds of the skill firing, it does not guarantee it. No
account instruction does. What makes it hold is Dave noticing when check 2 was not run.

This is also the first live test of AIDE's bootstrap-and-skill deployment model on real work.

---

## 6. Placement plan

Where this content goes when the AIDE masters are authored. None of these documents exist
yet — Project Design's masters are not output and Standards is not defined — so this is a plan,
not a set of edits.

### Principles

| Document | Content |
|---|---|
| Principles design | The value claim as a premise: the top two levels of design carry close to a one-to-one relationship with project outcome. Passes the portability test — true of any design work, not only AIDE's |
| Principles decisions | Reasoning for admitting it; the check that it does not duplicate the existing premise about stating the model before building machinery on it |
| Principles standard | The premise in lean form |

No new content for apparatus-avoidance — that premise already exists. At most it is
strengthened, which is a decisions entry against the existing premise, not a new one.

### Project Design

| Document | Content |
|---|---|
| Project Design design | The layering model; the context rule; the overview as the map elements are read against; understand-the-model-before-designing; derive from the model not a single requirement |
| Project Design design — doctype definitions | The context rule as a property of a design element; the overview's role sharpened in the overview doctype |
| Project Design design — commitment and return | Difficulty as evidence, as the design-time face of the existing build-side cost-and-complexity flag; escalation on recurrence |
| Project Design decisions | The four weaknesses and how each resolved, including the three already answered by settled material |
| Project Design standard | Application-time parts: the implied-versus-explicit test, the overview-complete-enough test, the four element questions. Discriminating guidance, which by the settled Standards principle belongs in the standard and not only the design |

### Documentation Methodology

| Document | Content |
|---|---|
| Doc Methodology design and standard | The language rules — plain English, use terms already in use, flag new terms, say what a thing is before defining it, meaning first. Writing grammar applies across all doctypes |

### Not a document

The skill is a deployment output, produced from the standards above. It is not authored
separately as a master.

---

## 7. Open items

**7.1 Home for the overview-first working behaviour.** Stay at the overview until it could
drive execution, probe don't dive, commit within the model, only surface real forks. Part is
design-specific and belongs to Project Design; part is generic human-AI working behaviour that
applies to build too, which points at Working Practices. A genuine ownership call, and the kind
that made Working Practices a dumping ground before. Decide deliberately, not by default.

**7.2 Difficulty-as-evidence — one home or two.** It now exists on both sides: the build return
cost-and-complexity flag, and the design-time question at each implementation decision. Likely
wants a single generic statement with both sides consuming it, rather than two statements that
drift apart. Reconcile when Project Design masters are authored.

**7.3 The skill's permanent placement.** Interim by design. Most of it is Project Design; a new
topic for it would itself be the apparatus failure. Confirm when the placement plan above is
executed, and update the skill's frontmatter note.

**7.4 The language profile.** `AIDE_Language_Profile_v1.md` was drafted on 8 September and
partly superseded by this work — Dave's comment was that several of its substitutions replaced
wording he had no problem with. The language rules that survive are in section 3.6 and the Doc
Methodology row above. Decide whether the profile document has a role beyond that, or retires.

**7.5 Model choice.** Dave finds Opus 4.6 more closely aligned than Opus 5 for this work — 5
tends to bend things toward a particular way of working, 4.6 adapts and applies correction
more, and more rework has been observed with 5. Claude backed running the next design pass on
4.6 and judging it on rework.

---

## 8. Next

Standards is the next component. Check 1 applies to its overview before any of it is written —
the first real run of this approach.
