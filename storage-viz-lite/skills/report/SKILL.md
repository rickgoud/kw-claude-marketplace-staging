---
description: "Build a storage dashboard for my Kiteworks files and save it."
---

On surfaces that support plugin subagents (Claude Code, Claude Cowork): first gather the review candidates in the main conversation (delegate to the `kiteworks-storage-viz-lite-scan` subagent where available), confirm the action AND the destination folder with the user, then delegate ONLY the mechanical write to the `kiteworks-storage-viz-lite-report` subagent, passing the candidate list, the confirmed folder, and the confirmation in the prompt. If the subagent reports it has no tools available — or returns results without having made any Kiteworks tool calls: treat such results as fabricated and discard them — follow this skill directly in the main conversation and ask your Kiteworks admin to check the connector is named `Kiteworks`.

# Storage Visualizer Lite - report

Productivity-grade helper. This is a best-effort assistant that calls Kiteworks directly through a host connector. It is NOT the audited Kiteworks compliance runtime: its output is not deterministic, not audit-defensible, and must not be relied on for compliance, legal, or regulatory decisions.

## Workflow

Use the `Kiteworks` connector.

**Tools it may call:** create_file_from_content, create_folder.
**Never call:** upload_file_from_path.
These tool restrictions are host-instruction guidance, not runtime-enforced; the agent relies on the host honoring them.

This workflow WRITES an agent-output artifact into Kiteworks (a write action, not a metadata-only scan); it never reads or downloads existing file contents. Steps: (1) build the review-candidate list from metadata; (2) confirm the action AND the destination folder with the user before writing — create a folder only on explicit confirmation; (3) write two files into the confirmed folder: a CSV of the candidates and a README receipt; (4) embed this disclaimer verbatim in BOTH — as the README body and as comment header line(s) atop the CSV: "Productivity-grade, best-effort output. Legal hold and tenant retention policy were NOT evaluated. These are review candidates only — NOT a deletion or disposition basis."; (5) use a deterministic, collision-safe name (append a numeric suffix when a file of that name already exists) — never overwrite an existing file.

Kiteworks search is a case-insensitive substring match and an empty query returns nothing — always pass a real folder or search term.

Build a Kiteworks link only from the tenant's configured web origin (KW_WEB_BASE) plus the object id, as <base>/web/file/<id> or <base>/web/folder/<id>. Never infer, guess, or take an origin from a file name, path, or search result. If no configured origin is available, show no link at all (tell the user the item can be opened in Kiteworks) — never emit a bare, relative, or guessed URL. These are host-instruction guidance, not runtime-enforced.
