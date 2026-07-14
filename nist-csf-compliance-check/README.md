# NIST CSF Compliance Check

`v0.5.1` · updated 2026-07-14

Checks a Kiteworks folder for external sharing exposure, the one sliver of NIST CSF's Protect function a file-sharing platform can see, and saves a report. Most of NIST CSF is outside what this can check; it says so.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/nist-csf-compliance-check)** — live examples, screenshots, and full detail.

## What's new

Checks a Kiteworks folder for the NIST CSF-relevant signals a file-sharing platform can actually see — sensitive content and external sharing — and saves a report, clearly flagging what falls outside its view.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install nist-csf-compliance-check@kiteworks-lite
```

**Claude Desktop:** download `nist-csf-compliance-check.plugin` (or the identical `nist-csf-compliance-check.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Check the Vendor Share folder for the NIST CSF exposure risks”
- “Summarize this folder's the NIST CSF exposure and save a report”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
