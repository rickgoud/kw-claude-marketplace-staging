# Retention Sweeper

`v1.0.3` · updated 2026-07-15

Finds files in a Kiteworks folder that are past a retention deadline you set, and can save a report of what it found.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/retention-sweeper)** — live examples, screenshots, and full detail.

## What's new

Refreshed the branded report and the safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install retention-sweeper@kiteworks-lite
```

**Claude Desktop:** download `retention-sweeper.plugin` (or the identical `retention-sweeper.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Find files in Archive older than the 7-year retention deadline”
- “Summarize what's overdue and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
