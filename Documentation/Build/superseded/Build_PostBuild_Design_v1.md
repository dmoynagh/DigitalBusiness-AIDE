
# Build Post-Build Actions — Design

> **Version 1** (2026-09-02). Defines explicit post-Build Tool invocation and ordinary output publication.

## Model

Post-Build actions run only after successful output validation. The destination/mechanism owner owns
the Tool. A request supplies Tool identity, destination and action inputs; Outcome reports production
and post-Build results separately.

Build owns generic publication/copy of validated output to an ordinary nominated path/repository.
AI Deployment owns future package registration/publication into its Deployment Registry.

## Failure and resumption

Do not erase or re-run a successful Build unnecessarily because publication failed. Preserve the
validated output identity/integrity, report the post-Build failure and resume idempotently where the
destination semantics allow.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v6
References: AIDE_PublishBuildOutputTool@v1
