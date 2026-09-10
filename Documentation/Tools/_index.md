# Tools

Role: component design
Aliases: none

Tools defines the methodology for building tools — repeatable, named, invokable actions performed by the AI in-session. It owns the tool definition, the invocability test that draws the boundary between a tool and a standard, and the authoring methodology used to design and author tools.

Tools is a methodological component. It defines how to create its type; individual tools live with their owning component under the what-knows-most-about-it principle.

## Parts

**Tools_Design** — the design document establishing what a tool is, the boundaries, authoring concerns, and the designing/authoring rules.

**Tools_Authoring_Standard** — the deployed standard a tool author consumes when designing, authoring, and deploying a tool.

**Tools_Decisions** — the reasoning behind each design decision.
