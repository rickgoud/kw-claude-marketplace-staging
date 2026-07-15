---
name: dora-compliance-check
description: >
  Use when the user asks to check Kiteworks content against DORA --
  trigger phrases include `DORA` `digital operational resilience` `ICT risk management` `Register of Information`. Scans and, on confirmation,
  writes a CSV + txt/pdf report. Single-phase: no separate "apply" step
  to ask for. Fit tier: Light -- see below for what this can and can't
  actually check.
metadata:
  version: "0.4.2"
---

Delegate to the `dora-compliance-check` subagent on surfaces that support it (Claude Code, Cowork). If it reports no tools or fabricates results without tool calls, discard and check the `Kiteworks` connector. On other surfaces, follow this skill directly.

# DORA Compliance Check -- fit tier: Light

Read `../compliance-mapping/SKILL.md` first for the shared mechanism (signals A/B/C/D, report shape, honesty framing) -- this skill only supplies framework-specific content, never its own scanning logic.

## What DORA actually is

The EU's Digital Operational Resilience Act for financial entities, covering ICT risk management, incident reporting, and third-party risk.

## Signals this agent runs

Signals: **B**.

## Control citations

Fully confirmed this pass. Drawn from Regulation (EU) 2022/2554 (DORA) -- official text at EUR-Lex, OJ L 333, 27.12.2022, p. 1-79.

- **Signal B** (external sharing): Art. 28 (Register of Information) requires financial entities to maintain and report a register of all ICT third-party arrangements, including documentation and yearly reporting obligations; a file documenting such an arrangement being shared externally is squarely within its scope.
- **Art. 9 ("Protection and prevention"), Chapter II Section II (ICT risk management)** is now confirmed as the general ICT-risk-management article this skill's Signal B logic reflects -- closing the gap the prior research pass left open. Art. 9 requires financial entities to continuously monitor and control the security of ICT systems, and to design and implement ICT security policies that maintain "high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit," including a documented information security policy, access-control policies, strong authentication mechanisms, a documented ICT change-management process, and patch/update policies. A file containing such at-risk data being shared externally sits squarely within Art. 9's protection objective.

## What this doesn't check

ICT incident classification, the Register of Information's actual completeness, TLPT programmes, and third-party contract review are entirely outside file-scan visibility -- this speaks only to whether ICT-related documentation is externally shared.

## Recommended next steps

- Complete or update the Register of Information (Art. 28) to reflect any ICT third-party arrangement this scan's findings relate to.
- Verify ICT security policies required under Art. 9 (information security policy