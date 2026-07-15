# Folder Expiry Audit

`v0.2.0` · updated 2026-07-15

Reports which Kiteworks folders have an expiry/retention policy configured and which don't.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/folder-expiry-audit)** — live examples, screenshots, and full detail.

## What's new

Refreshed the safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install folder-expiry-audit@kiteworks-lite
```

**Claude Desktop:** download `folder-expiry-audit.plugin` (or the identical `folder-expiry-audit.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Which folders under Client Files have a retention policy set?”
- “Show me folders with no expiry configured”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
