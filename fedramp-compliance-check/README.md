# Fedramp Compliance Check

`v0.5.1` · updated 2026-07-14

Checks a Kiteworks folder for the narrow slice of FedRAMP a file-sharing platform can actually see -- sensitive content and external sharing -- and saves a report. Most of FedRAMP is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/fedramp-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Checks a Kiteworks folder for the FedRAMP-relevant signals a file-sharing platform can actually see — sensitive content and external sharing — and saves a report, clearly flagging what falls outside its view.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install fedramp-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `fedramp-compliance-check.plugin` (or the identical `fedramp-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for FedRAMP exposure risks”
- “Summarize this folder's FedRAMP exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
