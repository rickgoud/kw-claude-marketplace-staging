---
name: pci-dss-compliance-check
description: >
  Use when the user asks to check Kiteworks content against PCI DSS --
  trigger phrases include `PCI DSS` `cardholder data` `CDE` `SAQ` `PAN` `tokenisation`. Scans and, on confirmation,
  writes a CSV + txt/pdf report. Single-phase: no separate "apply" step
  to ask for. Fit tier: Good -- see below for what this can and can't
  actually check.
metadata:
  version: "0.3.2"
---

Delegate to the `pci-dss-compliance-check` subagent on surfaces that support it (Claude Code, Cowork). If it reports no tools or fabricates results without tool calls, discard and check the `Kiteworks` connector. On other surfaces, follow this skill directly.

# PCI DSS Compliance Check -- fit tier: Good

Read `../compliance-mapping/SKILL.md` first for the shared mechanism (signals A/B/C/D, report shape, honesty framing) -- this skill only supplies framework-specific content, never its own scanning logic.

## What PCI DSS actually is

The payment card industry's data security standard for any organization that stores, processes, or transmits cardholder data.

## Signals this agent runs

Signals: **A, B**. Signal A's default term list for this framework: "cardholder data", "primary account number", "PAN", "CVV", "card verification" (plus the built-in PII/secret presets, plus anything the user adds).

## Control citations

Drawn directly from PCI DSS v4.0 (PCI Security Standards Council, March 2022), not the third-party GRC skill library.

- **Signal A** (sensitive-content exposure): Requirement 3 ("Protect Stored Account Data") sub-requirements 3.3 (do not store sensitive authentication data after authorization) and 3.4 (restrict access to PAN wherever it is stored) govern any cardholder-data-shaped content this signal finds.
- **Signal B** (external sharing): Requirement 3.5 (PAN is secured wherever it is stored, including in files sent outside the cardholder data environment) is the closest direct match for an externally-shared file containing card data.

## What this doesn't check

Network segmentation, tokenization architecture, the SAQ/ROC process, and quarterly vulnerability scanning are outside file-scan visibility -- this only flags where card-data-shaped content (the built-in Luhn-validated credit-card pattern) appears to live or be shared.

## Recommended next steps

- Complete the applicable SAQ or engage a QSA for a full Report on Compliance (ROC) -- this scan is not a substitute.
- Verify network segmentation actually isolates the cardholder data environment from the rest of the network.
- Confirm quarterly ASV vulnerability scans are current for any system holding flagged card data.

## Source

Adapted from the PCI DSS skill in the Claude Skills for Governance, Risk & Compliance library (`Sushegaad/Claude-Skills-Governance-Risk-and-Compliance`) -- https://sushegaad.github.io/Claude-Skills-Governance-Risk-and-Compliance/ -- which offers much deeper advisory capability (policy/document drafting, licensing walkthroughs, breach-notification procedures) than a content-governance scan can ever provide.
