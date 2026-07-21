# EU AI Act Compliance Check

`v0.5.2` · updated 2026-07-15

Checks a Kiteworks folder for AI-related documents that are shared externally or contain personal/biometric data, under the EU AI Act. Most of the EU AI Act is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/eu-ai-act-compliance-check)** — live examples, screenshots, and full detail.

## Before you install — the short version

Kiteworks agents are provided **as is**. They are helpful, but they can be wrong. You are responsible for checking what an agent produces before you rely on it, and Kiteworks is not liable for outcomes from using them.

[Read the full install disclaimer](https://marketplace.kiteworkslabs.com/legal/install-disclaimer) · Version `1.0` · Effective 2026-07-16

## What's new

Refined the EU AI Act checks and PII term matching; refreshed the branded report and safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install eu-ai-act-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `eu-ai-act-compliance-check.plugin` (or the identical `eu-ai-act-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for the EU AI Act exposure risks”
- “Summarize this folder's the EU AI Act exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
