# Storage Visualizer

`v1.0.3` · updated 2026-07-15

Shows what's taking up space in a Kiteworks folder -- totals, the largest files and folders, and how much is shared -- and can save a report.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/storage-visualizer)** — live examples, screenshots, and full detail.

## What's new

Refreshed the branded report and the safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install storage-visualizer@kiteworks-lite
```

**Claude Desktop:** download `storage-visualizer.plugin` (or the identical `storage-visualizer.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “What's using the most space in the Projects folder?”
- “Show the largest files and how much is shared”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
