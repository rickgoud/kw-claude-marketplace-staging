---
name: surface-gate
description: >
  Shared internal reference skill, not invoked by users directly.
  folder-scan, report-export, and content-extract all read this file
  for the standard way to detect which Claude surface this conversation
  is running on (Cowork/Claude Code with subagents, vs. standard Chat
  without them) and what to tell the user when a capability this skill
  needs isn't available here. Read this before writing or modifying any
  of those three skills, or any new skill that delegates to a subagent
  or needs local file access.
metadata:
  version: "0.1.0"
---

# surface-gate — detect the surface, disclose or refuse honestly

Confirmed (Anthropic documentation): skills in a plugin run on every Claude surface — chat, Cowork, and Claude Code. **Hooks and subagents run only in Cowork and Claude Code; in standard Chat they don't exist at all, not degraded, just absent.** The Kiteworks MCP connector itself works on every surface (connectors work across claude.ai, desktop, Cowork, and mobile) — so the data and tool calls this plugin makes are fine anywhere; what changes per-surface is only the safety scaffolding around them.

## Step 1 — detect what's actually available, don't assume

Check the actual tool/agent list visible right now, the same way you'd check for anything else — don't guess from which product you think you're in.

- **Subagent isolation**: is a named subagent for this skill (e.g. `retention-sweeper-preview`) listed as an available agent to delegate to? If yes, you're on Cowork or Claude Code — delegate as the skill instructs. If no such subagent-delegation capability is listed at all, you're on a surface without it (standard Chat, most likely).
- **Local file access**: are native local file tools (Read/Write/Bash operating on real file paths) present *without* being namespaced under a separate connector like `Filesystem:...`? If yes, native local access exists (Cowork). If the only path to a local file is a distinct, separately-connected `Filesystem:` tool, or no local file tool exists at all, native local access is not available.

## Step 2 — pick the right response, per what THIS skill actually needs

Every skill that reads this file states which tier applies to it. There are three:

**Tier A — full support.** Both subagent isolation and (if needed) local file access are present. Proceed exactly as the skill's own instructions say, no extra disclosure needed.

**Tier B — degrade with disclosure.** Subagent isolation is missing, but this skill doesn't need local file access and doesn't do anything beyond its own documented, narrow write scope (this covers most preview and apply skills in this plugin — none of them are ever granted a delete tool in the first place, so the practical risk of running "directly" is modest). Proceed directly in the main conversation, but say once, plainly, before acting: *"Running this directly in the conversation rather than through an isolated subagent, since that isolation is a Cowork/Claude Code feature not available here. I'll still follow this skill's restrictions, but on this surface that's enforced by instruction, not by the platform."* Then continue.

**Tier C — refuse and redirect.** This skill needs a capability that is genuinely absent, not just less-enforced — right now that means: local file access for the binary-file path in `content-extract` (downloading and parsing PDFs/DOCX/etc. has nowhere to go without it). When this is the case, do not attempt a workaround or guess a path. Say plainly: *"This part of \[agent name\] isn't available here — it needs local file access to download and read \[file type\], which this surface doesn't have. Connect the Filesystem extension to enable it here, or run this from Claude Cowork or Claude Code, where it works natively."* If a `Filesystem:` connector tool exists but isn't actually connected/configured (as opposed to not existing at all), say that specifically — "installed but not connected" needs a different fix than "not installed," and collapsing them into one vague error wastes the user's time.

## Don't over-apply Tier C

Most of this plugin's skills are Tier B, not Tier C — losing subagent isolation is a real reduction in enforcement, but it isn't the same as the skill being unable to function. Reserve the hard refusal for cases where the actual mechanism (like local file access) doesn't exist, not just where the safety wall around it is thinner.
