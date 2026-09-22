> identity: Assurance_Cases_Working@v1 | doctype: working | updated: 2026-09-16

# AIDE Assurance — Cases Working v1

Status: informal working document, not a designed artefact. Assurance's learning loop
is designed but not built — it depends on a hosted queue service that doesn't exist
yet (see Infrastructure's "hosted AIDE services" sub-scope,
`AIDE_Infrastructure_MCPDeliveryModel_v1.md`). This document is a stand-in place to
park candidate learning-loop entries as they come up, so they aren't lost between now
and whenever that service exists and the real schema is designed.

Nothing here is a finished entry in Assurance's eventual format — that format hasn't
been designed yet. Each case below is written at whatever level of detail made sense
when it was captured, for a human (or Improvement, later) to review and decide whether
it's worth carrying forward.

---

## Case 1 — Search before building, when documentation and reality diverge

**Captured:** 2026-09-16, during Orchestration's MCP-delivery investigation.

**Pattern observed.** Twice in one investigation session, a documented Anthropic
feature (marketplace-plugin MCP servers, Desktop Extensions) didn't behave as
documented on first build. Both times, the response was another round of
build-and-debug — real, useful learning (stdio framing, path variables, executable
resolution) — rather than a web search for prior reports of the same divergence. The
actual breakthrough on the hardest sub-problem (Chat not receiving plugin-delivered
MCP tools) came from a deep search turning up multiple independent GitHub issue
reproductions confirming it as a known platform bug — not from further local
debugging.

**Why it recurred.** The trigger — "documentation says X, live test shows not-X" —
was present both times and wasn't treated as a search cue either time. It took an
explicit, separate request to get the search done.

**Candidate recommendation.** When a documented feature repeatedly fails to behave as
documented, treat that specifically as a search-first trigger, before further
build-and-test iteration. This is different from general "search when unsure" advice —
it's a specific, recognisable pattern (docs say X, reality says not-X, more than once)
with a specific fix (check for known issues before debugging further).

**Related observation, same session.** A tendency to offer multiple competing
hypotheses in parallel when a test result was ambiguous, rather than picking the
cheapest one to test and running it down first. Slowed convergence — needed one test
per hypothesis instead of one test settling it. Also: a numbered design decision (D10,
Orchestration's implementation home) was committed before any testing occurred, then
had to be substantially rewritten once real evidence came in. Worth distinguishing
"leading candidate, untested" from a committed decision with more care, given this
project's own stated discipline is test-before-commit.

**Status.** Unreviewed. Parked here pending Improvement's design pass and the hosted
queue existing.

---

## Case 2 — A theory tested before acted on, and the total cost across the session

**Captured:** 2026-09-16, tail end of the same investigation (orchestration-probe's
Chat surface debugging).

**Pattern observed, positive this time.** Chat calls were failing. The first theory —
MSIX filesystem virtualization silently shadowing config edits — was plausible,
well-reasoned, and wrong. Unlike Case 1's pattern, the theory was checked against real
evidence (`SignatureKind: Developer`, not Store; comparing file sizes/timestamps across
the supposed real and shadow paths) before being acted on. It was ruled out cheaply, and
the actual root cause — a `claude_desktop_config.json` with no `mcpServers` key at all
— was found immediately after. This is the correction Case 1 asked for, working.

**Candidate recommendation.** Worth confirming this wasn't a one-off — watch for
whether "test the theory before building around it" holds on the next few debugging
instances, or whether it regresses once the specific memory of Case 1 fades.

**Total session cost, named plainly.** The full MCP-delivery investigation, across
several probes and this final Chat-surface debugging session, took roughly five hours
to go from "we think this should work" to "confirmed working on all three surfaces for
both dispatch and Python invocation." Some of that was genuine first-time-discovery
cost in a space where Anthropic's own documentation is actively misleading in places —
not avoidable by working faster. Real avoidable cost within it: the search-before-
building miss (Case 1), and a wrong conclusion ("Chat requires hosted MCP") stated with
more confidence than the evidence supported, which sent part of the investigation
toward a more complex fallback (`.mcpb`) before the simpler working path
(`claude_desktop_config.json`) was tried. The offsetting factor: this produced a
reusable delivery methodology for all future AIDE tooling, not a one-off result — the
cost was paid once, not per-tool.

**Status.** Unreviewed. Parked here pending Improvement's design pass and the hosted
queue existing.

---

## Adding a case

Each entry: what happened, why it recurred (if it did), a candidate recommendation if
one's obvious, and status (unreviewed / reviewed-kept / reviewed-dropped). Don't force
a schema beyond that — the real schema is Improvement and the hosted-service design's
job, not this document's.
