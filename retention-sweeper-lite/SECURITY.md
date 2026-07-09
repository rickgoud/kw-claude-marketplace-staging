# Security profile — Retention Sweeper Lite

> Generated from the package's KACS spec — do not edit by hand; changes will be overwritten on the next build.

- **Plugin:** `kiteworks-retention-sweeper-lite` — package version 0.3.0
- **Grade:** productivity (Lite)

> **Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.**

## Scope

This package exposes exactly 2 workflow(s), listed below, and nothing else. No connector URL, credential, or server is bundled in this package; Kiteworks is reached only through the tenant-configured `Kiteworks` connector.

### Workflow: preview — read-only, metadata-only

Example ask: Show me what's past retention in Marketing Drafts at 18 months.

**Allowed tools (read-only):** get_folder_children, get_top_folders, search_files, search_folders.
**Never call:** delete_file, delete_folder, download_file_to_path, move_file, move_folder, read_file_contents, upload_file_from_path.
Requires an explicit folder or path before scanning.
Bounded walk — do not exceed max_depth=4, max_pages=20, max_items=500.

> Legal hold is NOT evaluated. This workflow reads metadata only and cannot see legal-hold or tenant retention-policy state, so its results are review candidates only and must never be used to drive deletion or disposition decisions.

### Workflow: export — WRITE (gated)

Example ask: Export a retention report for Marketing Drafts (18 months) to my Kiteworks.

**Tools it may call:** create_file_from_content, create_folder.
**Never call:** upload_file_from_path.
Writes agent-output artifacts only, with explicit user confirmation before writing; it never reads or downloads existing file contents.
Write path enabled only after live-tenant validation gates cleared: gate_d, gate_e (required: gate_d, gate_e).

> Legal hold is NOT evaluated. This workflow reads metadata only and cannot see legal-hold or tenant retention-policy state, so its results are review candidates only and must never be used to drive deletion or disposition decisions.

## Enforcement status

| Surface | Enforcement |
| --- | --- |
| claude.ai web chat | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |
| Claude Desktop chat | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |
| Claude Cowork | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |
| Claude Code | Guidance only — tool restrictions are host instructions the agent asks the host to honor; they are not runtime-enforced on this surface. |

These tool restrictions are host-instruction guidance, not runtime-enforced; the agent relies on the host honoring them.

## Security contact

To disclose a security issue in this package or the Kiteworks connector, contact Kiteworks via https://kiteworks.com.
