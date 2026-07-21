# ISO 42001 Compliance Check

`v0.6.2` · updated 2026-07-15

Checks a Kiteworks folder for AI-related documents that are shared externally or contain personal data, under ISO 42001. Most of ISO 42001 is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/iso42001-compliance-check)** — live examples, screenshots, and full detail.

## Before you install — the short version

Kiteworks agents are provided **as is**. They are helpful, but they can be wrong. You are responsible for checking what an agent produces before you rely on it, and Kiteworks is not liable for outcomes from using them.

[Read the full install disclaimer](https://marketplace.kiteworkslabs.com/legal/install-disclaimer) · Version `1.0` · Effective 2026-07-16

## What's new

Refined the ISO 42001 checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install iso42001-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `iso42001-compliance-check.plugin` (or the identical `iso42001-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for ISO 42001 exposure risks”
- “Summarize this folder's ISO 42001 exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
