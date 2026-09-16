> identity: Deployment_Plugin_Working@v1 | doctype: working | updated: 2026-09-16

# AIDE Plugin Deployment — Working

Decisions and plan from the Build design session 2026-09-16. Pending content for Infrastructure and Deployment when those components have their design passes.

---

## Marketplace

- **Marketplace name:** `digitalbusiness-aide`
- **Marketplace repo:** `DigitalBusiness-AIDE-Deploy` — all live/final plugins
- **Test marketplace repo:** `DigitalBusiness-AIDE-Marketplace` — experiments and probes only, never graduates

## Plugin structure

Four plugins, split by consumer need:

| Plugin | Purpose | Installed by |
|---|---|---|
| `aide` | Operational framework — everything a consumer uses | Any AIDE user |
| `aide-dev` | Framework development — authoring and extending standards, tools, schemas, utilities | Framework developers |
| `db-aide-info` | Machine-consumed resources — platform info, settings, model capability mapping | Machine (rarely human-invoked) |
| `db-aide-temp` | Testing and probes | Developers during testing |

**Dividing test:** "Am I using the framework or extending it?" Using → `aide`. Extending → `aide-dev`.

**`db-` prefix** on info and temp: keeps rarely-invoked plugins out of the way of the daily-use `aide` and `aide-dev` plugins.

**`db-aide-info` deferred** — no content exists yet (Core Resources not authored, platform profiles not built). Create when content arrives.

**`db-aide-temp` deferred** — probes stay in the test marketplace repo for now.

## Skill-to-plugin allocation

### `aide` plugin

| Skill | Source | Status |
|---|---|---|
| `messaging` | Messaging Standard v4 + Tool v4 | Phase 1 — migrate existing skill |
| `design-check` | PD Standard v4 deployment output | Phase 1 — migrate existing skill |
| `principles` | Principles Standard v2 | Phase 2 — author from master |
| `docmeth` | DocumentationMethodology Standard v1 | Phase 2 — author from master |
| `docmeth-schema-definitions` | DocumentationMethodology SchemaDefinitions Standard v1 | Phase 2 — author from master |
| `standards-consumption` | Standards Consumption Standard v3 | Phase 2 — author from master |
| `pd-standard` | ProjectDesign Standard v4 | Phase 2 — author from master |
| `wp` | WP Standard (not yet authored) | Phase 3 |
| `assurance` | Assurance Standard (not yet authored) | Phase 3 |
| `build` | Build Standard (deferred by D32) | Phase 3 |

MCP server: Orchestration dispatch — Phase 1.

### `aide-dev` plugin

| Skill | Source | Status |
|---|---|---|
| `standards-authoring` | Standards Authoring Standard v8 | Phase 2 — author from master |
| `tools-authoring` | Tools Authoring Standard v8 | Phase 2 — author from master |
| `docmeth-schema-authoring` | DocumentationMethodology SchemaAuthoring Standard v1 | Phase 2 — author from master |

No MCP server.

## Phased rollout

### Phase 1 — prove the model with real content

- Create `aide` and `aide-dev` plugin structures in `DigitalBusiness-AIDE-Deploy`
- Migrate `messaging` and `design-check` skills → `aide`
- Add Orchestration dispatch MCP server → `aide`
- Write Chat bootstrap (`claude_desktop_config.json` entry)
- Test all three surfaces, update propagation
- `aide-dev` created as structure only (no skills yet)

### Phase 2 — deploy completed standards as skills

Author skills from all cross-reviewed, accepted standards. Each skill names its plugin in the skill's own metadata. Batch deployment and test.

### Phase 3 — remaining

- WP, Assurance, Build standards as they are authored and cross-reviewed
- Resources plugin (`db-aide-info`) when Core Resources content exists
- CLI tools migrated to MCP servers if/when warranted

## Component output declaration

Each standard and tool should declare its target plugin in its deployment information — in the design or brief under the linked-build-outcome section, or in the standard's applicability section. This is a property of the output, not a separate registry. The pattern establishes itself with the Phase 2 skill authoring.

## Delivery model

The MCP delivery model documented in `Infrastructure/AIDE_Infrastructure_MCPDeliveryModel_v1.md` is the governing methodology. Key points:

- Raw Node.js CommonJS, newline-delimited JSON over stdio, no SDK dependency
- `.mcp.json` uses `${CLAUDE_PLUGIN_ROOT}` for paths
- Chat requires a `claude_desktop_config.json` bootstrap entry (platform bug workaround)
- Update path: merge PR → refresh clone → restart

---

Version note: v1 — decisions from the Build design-pass session 2026-09-16. Pending content for Infrastructure and Deployment design passes.
