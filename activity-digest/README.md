# Activity Digest

`v1.0.2` · updated 2026-07-14

Summarizes what's new or changed in a Kiteworks folder over a time window, and can save a report.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/activity-digest)** — live examples, screenshots, and full detail.

## What's new

Refreshed the saved activity report (branded PDF + export) and tightened change detection.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install activity-digest@kiteworks-lite
```

**Claude Desktop:** download `activity-digest.plugin` (or the identical `activity-digest.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “What changed in the Q3 Launch folder in the last 7 days?”
- “Summarize this month's activity in Contracts and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
