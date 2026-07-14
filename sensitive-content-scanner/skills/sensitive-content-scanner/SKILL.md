---
name: sensitive-content-scanner
description: >
  Use when the user wants to sweep a Kiteworks folder for sensitive
  terms — trigger phrases include "scan for sensitive content in X,"
  "find files mentioning [term]," or "sensitive content scan." Scans
  and, on confirmation, writes a CSV + txt/pdf report. Single-phase: no
  separate "apply" step to ask for.
metadata:
  version: "1.1.3"
---

Delegate to the `sensitive-content-scanner` subagent. Read `../term-sweep/SKILL.md` first — it has the confirmed caveat about `content_contains` reliability; do not skip it.

# Sensitive Content Scanner

## Why this is one phase, not two

This agent never touches flagged files — its only write action is a CSV + txt/pdf report. A separate apply skill didn't protect against anything real, so scanning and (on confirmation) saving are now one flow, one agent.

## Collect from the user

A folder scope (required) and a term list (required — never assume a default list; sensitivity vocabulary is organization-specific, e.g. "confidential", "SSN", "ITAR", a client name).

## Sweep

Always run the name/path match per `term-sweep` — fast, one call, always on.

Content matching is a separate, opt-in "deep scan": ask the user whether they want it (it's real per-file work — a download and parse per candidate file, per `../content-extract/SKILL.md`), tell them roughly how many files are in scope, and only run it if they confirm. Respect `content-extract`'s per-run cap and disclose how many files were actually checked vs. in scope.

## Built-in PII/secret pattern presets — on by default whenever the deep scan runs

This is what makes this agent an actual *sensitive-content* scanner rather than just a keyword search the user has to fully configure themselves. Whenever the content deep-scan runs, also run `../term-sweep/SKILL.md`'s built-in pattern presets (`scripts/pii_patterns.py`: SSN-shaped numbers, Dutch BSN numbers via the real elfproef checksum, Luhn-valid credit card numbers, checksum-valid IBANs, AWS access key IDs) against the same extracted text, alongside whatever custom terms the user gave. Tell the user up front that this runs by default and let them turn it off if they only want their own term list — don't make them ask for it.

Each category also carries a `context_confirmed` count alongside its raw `valid` count — whether a relevant keyword (e.g. "BSN," "SSN," "IBAN," "card number") appeared within 60 characters of the match. A shape/checksum-valid match with no nearby keyword still counts as a hit (real PII is often unlabeled), but report both numbers so the user can see how many hits also have contextual support, not just checksum validity.

## Custom regex — for anything the built-in categories don't cover

If the user has their own pattern in mind (an internal ID shape, a partner account number, anything with a defined structure), ask for the regex, a label, and optionally context keywords, and run it through `term-sweep`'s custom regex mode (`scripts/pii_patterns.py`'s second, optional argument) alongside whatever else is running. A bad regex or a pathological one is reported as a per-pattern error, not a crash — surface that plainly if it happens rather than silently dropping the pattern.

## Present the result, then actively offer to save it

Summary card: summary, term list used, name-match hits, whether a content deep-scan ran and its hits if so (or "not run — ask to include a content scan" if the user didn't opt in), which built-in pattern categories ran with both their `valid` and `context_confirmed` counts (by category, never the matched value), coverage, warnings.

**Do not stop there and wait.** End by explicitly asking, e.g.: *"Want me to save this as a CSV + PDF report to `My Folder/Agents/Sensitive Content Scanner/`?"*

## If confirmed, write the report

Read `../report-export/SKILL.md`. Default agent name: "Sensitive Content Scanner". Never touches flagged files, never prints matched text or matched pattern values (per `term-sweep`), and the report must repeat the content-search reliability caveat.

Write CSV (name, path, term or pattern-category matched, match type name/custom-content/built-in-pattern, link) and txt/pdf narrative including the caveat verbatim. If built-in pattern presets ran, state which categories were checked with both their `valid` and `context_confirmed` counts, even for the ones with zero hits — a clean result on SSN/BSN/credit-card/IBAN/AWS-key patterns is itself useful information, not just noise to omit.
