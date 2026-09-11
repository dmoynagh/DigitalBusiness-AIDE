# Working Practices

Role: component design
Aliases: WP, workprac

Working Practices owns the conventions and behaviours for how an AI and user actually work together across surfaces. Cross-cutting operational conventions covering file handling, work management, content capture, content delivery, and how the human and AI collaborate.

## Parts

**File Operations** (prefix `WP_FileOps_`)
How files are physically managed — delivery, placement, versioning lifecycle, separation of design and output, git integration.

**Work Management** (prefix `WP_WorkManagement_`)
How work is tracked, progresses, and completes — work items, definition of done, pending content, development lifecycle, WIP conventions.

**Capture and Organisation** (prefix `WP_Capture_`)
How content is captured during work and allocated to its home — capture-and-place rules, session-end allocation, process document types.

**Content Delivery** (prefix `WP_ContentDelivery_`)
How content is assembled and delivered to the AI platform — binder concept, inclusion rules, context loading.

**Human-AI Collaboration** (prefix `WP_HumanAI_`)
How the AI works with the human — the human working model, tiering, confidence, drift detection, anomalies channel.
