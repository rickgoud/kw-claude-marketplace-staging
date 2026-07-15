# Offboarding Content Finder

`v0.5.1` · updated 2026-07-15

Finds everything a departing or transferring employee owns across Kiteworks, and moves confirmed items to a holding folder for review.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/offboarding-content-finder)** — live examples, screenshots, and full detail.

## What's new

Refreshed the branded report and the safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install offboarding-content-finder@kiteworks-lite
```

**Claude Desktop:** download `offboarding-content-finder.plugin` (or the identical `offboarding-content-finder.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Find everything owned by jdoe@example.com across Kiteworks”
- “Move the confirmed items to the Offboarding Hold folder”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
