# Invoice Organizer

`v0.5.1` · updated 2026-07-15

Finds invoices and receipts in a Kiteworks folder (including photos and scans), pulls out vendor, date, amount, and tax info, and -- once you approve -- renames them consistently and gives you a categorized spreadsheet for expenses or taxes.

**[View on the Kiteworks Agent Marketplace →](https://marketplace.kiteworkslabs.com/catalog/invoice-organizer)** — live examples, screenshots, and full detail.

## What's new

Refreshed the branded report and the safety pre-check.

## Install

Add the marketplace once, then install this agent:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install invoice-organizer@kiteworks-lite
```

**Claude Desktop:** download `invoice-organizer.plugin` (or the identical `invoice-organizer.zip` if the uploader rejects `.plugin`) and upload it via **Customize → Personal plugins → Upload plugin**.

## Requires

A remote MCP connector named `Kiteworks` in your Claude organization — your Kiteworks admin provides the tenant-specific link. Without it the workflows have nothing to call.

## Try it

- “Organize the invoices in my Receipts folder”
- “Rename them consistently and give me an expense spreadsheet”

---
*Generated from the marketplace source — do not edit by hand; changes are overwritten on publish.*
