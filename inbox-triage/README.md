# Inbox Triage

`v0.5.1` · updated 2026-07-15

Sorts files sitting in a Kiteworks inbox or uploads folder into the right project folders, and moves them once you approve the matches.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/inbox-triage)** — live examples, screenshots, and full detail.

## What's new

Refreshed the branded report and the safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install inbox-triage@kiteworks-lite
```

**Claude Desktop:** download `inbox-triage.plugin` (or the identical `inbox-triage.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Sort the files in my Uploads inbox into the right project folders”
- “Move the confirmed matches”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
