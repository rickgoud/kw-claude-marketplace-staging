---
description: Connect this plugin to your Kiteworks tenant before running any workflow.
---

# Setup — connect Kiteworks

Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.

This plugin's workflows call Kiteworks through a remote MCP connector named `Kiteworks`. Before running a workflow:

1. Ask your Kiteworks administrator for the tenant-specific "Connect to Claude" link for the `Kiteworks` connector.
2. Install/enable that connector in your Claude organization.
3. Confirm the `Kiteworks` connector is visible, then run a workflow.

No connector URL or credential is shipped in this package — the endpoint is configured per tenant by your admin.

**Name the connector exactly `Kiteworks`.** This plugin ships a per-workflow subagent whose tool list names connector tools by fully-qualified name (`mcp__Kiteworks__...`). A differently-named connector will not match: the subagent itself then runs with NO tools — it never inherits broader access — and is instructed to stop, report that it has no Kiteworks tools, and fall back to running this plugin's skill directly in the main conversation. Rename the connector and retry. (Troubleshooting: docs/CLAUDE-SUBAGENT-TOOL-NAMING.md in the platform repository.)

A subagent's tool list constrains which tools a workflow may call — it does not verify which server provides them. Connector identity, endpoint, and permissions remain managed by your Kiteworks admin and your Claude org admin.

These tool restrictions are host-instruction guidance, not runtime-enforced; the agent relies on the host honoring them.
