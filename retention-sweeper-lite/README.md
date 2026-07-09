# 🗂️ Retention Sweeper Lite

**Version 0.3.0**

Best-effort direct-MCP scan of Kiteworks metadata for files past a retention threshold. Productivity-grade and host-instruction-driven - NOT the audited compliance runtime, not audit-defensible, and not a basis for deletion decisions.

> **Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.**

## Workflows

Each workflow is a bundled skill that fires automatically when your request matches it. Just ask in natural language. Where the surface supports invoking a skill by name, you can also run `/kiteworks-retention-sweeper-lite:<workflow>`:

- **preview** (`/kiteworks-retention-sweeper-lite:preview`) — Show me what's past retention in Marketing Drafts at 18 months.
- **export** (`/kiteworks-retention-sweeper-lite:export`) — Export a retention report for Marketing Drafts (18 months) to my Kiteworks.

## Setup

This plugin calls Kiteworks through a remote MCP connector named `Kiteworks`. See `skills/SETUP.md` to connect your tenant. No connector URL is bundled — your Kiteworks admin provides the tenant-specific link.

See `SECURITY.md` for this package's full security profile (allowed tools, enforcement status).

> **Legal hold is NOT evaluated. This workflow reads metadata only and cannot see legal-hold or tenant retention-policy state, so its results are review candidates only and must never be used to drive deletion or disposition decisions.**
