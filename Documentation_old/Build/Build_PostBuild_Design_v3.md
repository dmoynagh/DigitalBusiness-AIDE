
# Build Post-Build Actions — Design

> **Version 3** (2026-09-03). Keeps post-Build request/result as workflow state and clarifies owner-defined coordinated Release Batches.

## Model

Post-Build actions run only after successful output validation. The destination/mechanism owner owns
the Tool. The WorkPackage or equivalent producer-owned Build request supplies Tool identity, destination and action inputs. That request/intent is workflow state, not immutable package content. Outcome reports production and post-Build results separately; Registry receipt/result likewise remains outside immutable validated package bytes.

Build owns generic publication/copy of validated output to an ordinary nominated path/repository.
AI Deployment owns package registration/publication into its Deployment Registry through `AIDE_DeploymentRegistryTool@v2`.

Where several package registrations form one coordinated producer change, the producer/directing workflow owns that coordination decision and supplies one common Open Release Batch to every participating registration. Generic Build does not infer a batch merely because outputs were produced together.

## Failure and resumption

Do not erase or re-run a successful Build unnecessarily because publication failed. Preserve the
validated output identity/integrity, report the post-Build failure and resume idempotently where the
destination semantics allow.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Build@v9
References: AIDE_PublishBuildOutputTool@v1, AIDE_DeploymentRegistryTool@v2
