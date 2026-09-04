
# Build Post-Build Actions — Design

> **Version 2** (2026-09-02). Resolves AI Deployment Registry publication to the current Registry Tool.

## Model

Post-Build actions run only after successful output validation. The destination/mechanism owner owns
the Tool. A request supplies Tool identity, destination and action inputs; Outcome reports production
and post-Build results separately. Registry receipt/result remains external to immutable validated package bytes.

Build owns generic publication/copy of validated output to an ordinary nominated path/repository.
AI Deployment owns package registration/publication into its Deployment Registry through `AIDE_DeploymentRegistryTool@v1`.

## Failure and resumption

Do not erase or re-run a successful Build unnecessarily because publication failed. Preserve the
validated output identity/integrity, report the post-Build failure and resume idempotently where the
destination semantics allow.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Build@v6
References: AIDE_PublishBuildOutputTool@v1, AIDE_DeploymentRegistryTool@v1
