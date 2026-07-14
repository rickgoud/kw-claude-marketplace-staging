# Kiteworks Agents (Lite)

Productivity-grade (Lite) Kiteworks agents for Claude — direct-MCP, best-effort. NOT the audited Kiteworks compliance runtime, not audit-defensible, and not a basis for deletion decisions.

## Browse the catalog

**→ https://marketplace.kiteworkslabs.com** — the full, always-current catalog with live examples, categories, and screenshots. This repository is the **install source**; the website is where you explore.

Recent additions and announcements: **https://marketplace.kiteworkslabs.com/whats-new**

## Prerequisite — the Kiteworks connector

Every agent calls Kiteworks through a remote MCP connector referenced by the logical name `Kiteworks` — no URL or credential is bundled. In your Claude organization, add the remote MCP connector and name it `Kiteworks` (your Kiteworks admin provides the tenant-specific link). Without it the workflows have nothing to call.

## Install

Add this marketplace by URL, then install any agent by name:

```
/plugin marketplace add rickgoud/kw-claude-marketplace-staging
/plugin install <agent>@kiteworks-lite
```

**Claude Desktop (single plugin):** download an `<agent>.plugin` bundle and upload it via **Customize → Personal plugins → Upload plugin** (or, org-wide, **Organization settings → Plugins → Add plugins → Upload a file**). If the uploader rejects `.plugin`, upload the identical `<agent>.zip`.

## Agents (41)

Explore and try each agent on the website — the list below links straight to each live page.

<details><summary>All 41 agents</summary>

| Agent | Version | Links |
|---|---|---|
| Activity Digest | `1.0.2` | [`./activity-digest/`](./activity-digest/) · [live](https://marketplace.kiteworkslabs.com/catalog/activity-digest) |
| Ccpa Compliance Check | `0.5.1` | [`./ccpa-compliance-check/`](./ccpa-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/ccpa-compliance-check) |
| Cis Controls Compliance Check | `0.5.1` | [`./cis-controls-compliance-check/`](./cis-controls-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/cis-controls-compliance-check) |
| Cmmc Compliance Check | `0.5.1` | [`./cmmc-compliance-check/`](./cmmc-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/cmmc-compliance-check) |
| Contract Radar | `1.0.3` | [`./contract-radar/`](./contract-radar/) · [live](https://marketplace.kiteworkslabs.com/catalog/contract-radar) |
| Document Summarizer | `0.5.0` | [`./document-summarizer/`](./document-summarizer/) · [live](https://marketplace.kiteworkslabs.com/catalog/document-summarizer) |
| Dora Compliance Check | `0.6.1` | [`./dora-compliance-check/`](./dora-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/dora-compliance-check) |
| Dpdpa Compliance Check | `0.5.1` | [`./dpdpa-compliance-check/`](./dpdpa-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/dpdpa-compliance-check) |
| Duplicate Finder | `0.5.0` | [`./duplicate-finder/`](./duplicate-finder/) · [live](https://marketplace.kiteworkslabs.com/catalog/duplicate-finder) |
| Ear Compliance Check | `0.5.1` | [`./ear-compliance-check/`](./ear-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/ear-compliance-check) |
| Eu Ai Act Compliance Check | `0.5.1` | [`./eu-ai-act-compliance-check/`](./eu-ai-act-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/eu-ai-act-compliance-check) |
| Fedramp Compliance Check | `0.5.1` | [`./fedramp-compliance-check/`](./fedramp-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/fedramp-compliance-check) |
| Folder Expiry Audit | `0.1.1` | [`./folder-expiry-audit/`](./folder-expiry-audit/) · [live](https://marketplace.kiteworkslabs.com/catalog/folder-expiry-audit) |
| Gdpr Compliance Check | `0.5.1` | [`./gdpr-compliance-check/`](./gdpr-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/gdpr-compliance-check) |
| Hipaa Compliance Check | `0.5.1` | [`./hipaa-compliance-check/`](./hipaa-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/hipaa-compliance-check) |
| Inbox Triage | `0.5.0` | [`./inbox-triage/`](./inbox-triage/) · [live](https://marketplace.kiteworkslabs.com/catalog/inbox-triage) |
| Intake Form Builder | `0.1.0` | [`./intake-form-builder/`](./intake-form-builder/) · [live](https://marketplace.kiteworkslabs.com/catalog/intake-form-builder) |
| Invoice Organizer | `0.5.0` | [`./invoice-organizer/`](./invoice-organizer/) · [live](https://marketplace.kiteworkslabs.com/catalog/invoice-organizer) |
| Ism Au Compliance Check | `0.6.1` | [`./ism-au-compliance-check/`](./ism-au-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/ism-au-compliance-check) |
| Iso27001 Compliance Check | `0.5.1` | [`./iso27001-compliance-check/`](./iso27001-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/iso27001-compliance-check) |
| Iso27701 Compliance Check | `0.5.1` | [`./iso27701-compliance-check/`](./iso27701-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/iso27701-compliance-check) |
| Iso42001 Compliance Check | `0.6.1` | [`./iso42001-compliance-check/`](./iso42001-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/iso42001-compliance-check) |
| Itar Compliance Check | `0.5.1` | [`./itar-compliance-check/`](./itar-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/itar-compliance-check) |
| Lgpd Compliance Check | `0.5.1` | [`./lgpd-compliance-check/`](./lgpd-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/lgpd-compliance-check) |
| Naming Cleanup | `0.5.0` | [`./naming-cleanup/`](./naming-cleanup/) · [live](https://marketplace.kiteworkslabs.com/catalog/naming-cleanup) |
| Nis2 Compliance Check | `0.5.1` | [`./nis2-compliance-check/`](./nis2-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/nis2-compliance-check) |
| Nist 800 53 Compliance Check | `0.5.1` | [`./nist-800-53-compliance-check/`](./nist-800-53-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/nist-800-53-compliance-check) |
| Nist Ai Rmf Compliance Check | `0.6.1` | [`./nist-ai-rmf-compliance-check/`](./nist-ai-rmf-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/nist-ai-rmf-compliance-check) |
| Nist Csf Compliance Check | `0.5.1` | [`./nist-csf-compliance-check/`](./nist-csf-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/nist-csf-compliance-check) |
| Nzism Compliance Check | `0.6.1` | [`./nzism-compliance-check/`](./nzism-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/nzism-compliance-check) |
| Offboarding Content Finder | `0.5.0` | [`./offboarding-content-finder/`](./offboarding-content-finder/) · [live](https://marketplace.kiteworkslabs.com/catalog/offboarding-content-finder) |
| Pci Dss Compliance Check | `0.5.1` | [`./pci-dss-compliance-check/`](./pci-dss-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/pci-dss-compliance-check) |
| Redactor | `0.5.0` | [`./redactor/`](./redactor/) · [live](https://marketplace.kiteworkslabs.com/catalog/redactor) |
| Retention Sweeper | `1.0.2` | [`./retention-sweeper/`](./retention-sweeper/) · [live](https://marketplace.kiteworkslabs.com/catalog/retention-sweeper) |
| Section 508 Compliance Check | `0.6.1` | [`./section-508-compliance-check/`](./section-508-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/section-508-compliance-check) |
| Sensitive Content Scanner | `1.1.3` | [`./sensitive-content-scanner/`](./sensitive-content-scanner/) · [live](https://marketplace.kiteworkslabs.com/catalog/sensitive-content-scanner) |
| Sharing Auditor | `1.0.2` | [`./sharing-auditor/`](./sharing-auditor/) · [live](https://marketplace.kiteworkslabs.com/catalog/sharing-auditor) |
| Soc2 Compliance Check | `0.5.1` | [`./soc2-compliance-check/`](./soc2-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/soc2-compliance-check) |
| Storage Visualizer | `1.0.2` | [`./storage-visualizer/`](./storage-visualizer/) · [live](https://marketplace.kiteworkslabs.com/catalog/storage-visualizer) |
| Vn Pdpl Compliance Check | `0.6.1` | [`./vn-pdpl-compliance-check/`](./vn-pdpl-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/vn-pdpl-compliance-check) |
| Wcag Compliance Check | `0.6.1` | [`./wcag-compliance-check/`](./wcag-compliance-check/) · [live](https://marketplace.kiteworkslabs.com/catalog/wcag-compliance-check) |

</details>

## What's in this repo

- `.claude-plugin/marketplace.json` — the marketplace catalog (`kiteworks-lite`).
- `<agent>/` — the plugin directory (skills, agents, connector setup, per-agent README).
- `<agent>.plugin` and `<agent>.zip` — single-plugin bundles (identical bytes; `.zip` works around a Claude Desktop uploader that rejects `.plugin`).

## Notes

- Bundles are **unsigned** in this interim; install-source integrity rests on repository controls (branch protection on the published repo) until signed bundles land.

---
*Generated from the `kiteworks-agent-marketplace-lite` source — do not edit by hand; changes are overwritten on publish.*
