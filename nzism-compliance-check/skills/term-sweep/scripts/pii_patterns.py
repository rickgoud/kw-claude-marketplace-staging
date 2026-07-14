#!/usr/bin/env python3
"""Built-in sensitive-pattern presets for term-sweep's content deep-scan,
plus an optional deterministic custom-regex mode for user-supplied patterns.

Checks extracted file text against a small set of high-confidence PII/secret
shapes, using real checksum validation (Luhn for card numbers, mod-97 for
IBAN, the Dutch elfproef for BSN) rather than naive regex alone, to keep
false positives low on ordinary business documents full of unrelated
numbers (scores, IDs, weights, etc.).

Every built-in category also gets a second, independent signal: whether a
relevant keyword (e.g. "BSN", "IBAN", "social security") appears within a
small window of characters around the match. Checksum validation catches
numbers that are shaped right; context catches numbers that are shaped
right AND appear where you'd actually expect that kind of data. Neither
alone is proof -- together they're a much stronger signal than either.

Custom-regex mode (2026-07-13): a user can supply their own regex(es) --
e.g. an internal employee-ID shape like "EMP-\\d{6}" -- and have them
evaluated the same deterministic way, instead of the agent having to read
raw extracted text into its own reasoning to "look for" the pattern, which
would defeat the whole point of keeping sensitive content out of the
conversation. A bad regex is reported as an error per-pattern, never
crashes the run. Text is length-capped before evaluation and each pattern
gets a wall-clock timeout guard, since an arbitrary user-supplied regex can
pathologically backtrack (ReDoS) on adversarial input.

Usage:
  python3 pii_patterns.py <path-to-extracted-text-file>
  python3 pii_patterns.py <path-to-extracted-text-file> <path-to-custom-patterns.json>

  custom-patterns.json is a JSON array of objects:
    [{"label": "employee_id", "regex": "EMP-\\d{6}", "context_keywords": ["employee id"]}, ...]
  "context_keywords" is optional.

Prints ONLY a JSON object of counts per category/label, split into the raw
match count and the context-confirmed subset of it, e.g.
{"ssn_shaped": {"valid": 2, "context_confirmed": 1}, ...,
 "custom": {"employee_id": {"valid": 3, "context_confirmed": 3, "error": null}}}

Never prints the matched values themselves -- per this plugin's privacy rule
(term-sweep / content-extract), only counts and categories are safe to surface.
"""
import json
import re
import signal
import sys

SSN_SHAPED = re.compile(r"\b(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b")
BSN_SHAPED = re.compile(r"\b\d{9}\b")
CARD_CANDIDATE = re.compile(r"\b(?:\d[ -]?){13,19}\b")
IBAN_CANDIDATE = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")
AWS_ACCESS_KEY = re.compile(r"\bAKIA[0-9A-Z]{16}\b")

CATEGORIES = {
    "ssn_shaped": "US Social Security Number shape (area/group/serial validity rules applied, not government-verified)",
    "bsn_shaped": "Dutch BSN (Burgerservicenummer) shape, elfproef (11-test) checksum valid",
    "credit_card_luhn_valid": "13-19 digit number, Luhn checksum valid (real card-number validation, not just digit count)",
    "iban_checksum_valid": "IBAN shape, mod-97 checksum valid (real IBAN validation)",
    "aws_access_key": "AWS access key ID shape (AKIA prefix + 16 chars) -- a leaked-credential signal, not classic PII",
}

# Keywords checked within CONTEXT_WINDOW characters of a match, case-insensitive.
# A second, independent confirmation signal on top of checksum/shape validity --
# not required to count a hit at all, but raises confidence a lot when present.
CONTEXT_WINDOW = 60
CONTEXT_TRIGGERS = {
    "ssn_shaped": ["ssn", "social security"],
    "bsn_shaped": ["bsn", "burgerservicenummer", "sofinummer"],
    "credit_card_luhn_valid": ["credit card", "card number", "cvv", "visa", "mastercard", "amex", "discover"],
    "iban_checksum_valid": ["iban", "bank account", "rekeningnummer", "account number"],
    "aws_access_key": ["aws", "access key", "secret key"],
}

# Safety caps for custom user-supplied regexes -- built-in patterns above are
# fixed and already known-safe, these caps only apply to the custom mode.
CUSTOM_MAX_TEXT_CHARS = 2_000_000
CUSTOM_REGEX_TIMEOUT_SECONDS = 3


class _RegexTimeout(Exception):
    pass


def _alarm_handler(signum, frame):
    raise _RegexTimeout()


def _finditer_with_timeout(compiled, text, timeout_seconds):
    """Best-effort wall-clock guard against catastrophic backtracking in a
    user-supplied regex. SIGALRM is Unix-only and process-wide (not safe to
    nest), which is fine here since this script runs each pattern serially
    in its own process invocation. Falls back to no timeout if SIGALRM isn't
    available (e.g. non-Unix) rather than failing the whole run."""
    has_alarm = hasattr(signal, "SIGALRM")
    if has_alarm:
        old_handler = signal.signal(signal.SIGALRM, _alarm_handler)
        signal.alarm(timeout_seconds)
    try:
        return list(compiled.finditer(text))
    finally:
        if has_alarm:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)


def context_hit(text: str, start: int, end: int, keywords) -> bool:
    window = text[max(0, start - CONTEXT_WINDOW): end + CONTEXT_WINDOW].lower()
    return any(kw.lower() in window for kw in keywords)


def luhn_valid(number: str) -> bool:
    digits = [int(d) for d in number]
    checksum = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
    return checksum % 10 == 0


def iban_valid(candidate: str) -> bool:
    c = candidate.replace(" ", "").upper()
    if not re.fullmatch(r"[A-Z]{2}\d{2}[A-Z0-9]{11,30}", c):
        return False
    rearranged = c[4:] + c[:4]
    numeric = "".join(str(int(ch, 36)) if ch.isalpha() else ch for ch in rearranged)
    try:
        return int(numeric) % 97 == 1
    except ValueError:
        return False


def bsn_valid(candidate: str) -> bool:
    """Dutch elfproef: weights 9,8,7,6,5,4,3,2,-1 over the 9 digits, sum % 11 == 0.
    All-zero excluded explicitly -- it passes the arithmetic but was never issued."""
    if len(candidate) != 9 or not candidate.isdigit():
        return False
    if candidate == "000000000":
        return False
    weights = [9, 8, 7, 6, 5, 4, 3, 2, -1]
    total = sum(int(d) * w for d, w in zip(candidate, weights))
    return total % 11 == 0


def scan(text: str) -> dict:
    result = {}

    ssn_valid = ssn_context = 0
    for m in SSN_SHAPED.finditer(text):
        ssn_valid += 1
        if context_hit(text, m.start(), m.end(), CONTEXT_TRIGGERS["ssn_shaped"]):
            ssn_context += 1
    result["ssn_shaped"] = {"valid": ssn_valid, "context_confirmed": ssn_context}

    bsn_valid_n = bsn_context = 0
    for m in BSN_SHAPED.finditer(text):
        if bsn_valid(m.group()):
            bsn_valid_n += 1
            if context_hit(text, m.start(), m.end(), CONTEXT_TRIGGERS["bsn_shaped"]):
                bsn_context += 1
    result["bsn_shaped"] = {"valid": bsn_valid_n, "context_confirmed": bsn_context}

    cc_valid = cc_context = 0
    for m in CARD_CANDIDATE.finditer(text):
        digits = re.sub(r"[ -]", "", m.group())
        if 13 <= len(digits) <= 19 and luhn_valid(digits):
            cc_valid += 1
            if context_hit(text, m.start(), m.end(), CONTEXT_TRIGGERS["credit_card_luhn_valid"]):
                cc_context += 1
    result["credit_card_luhn_valid"] = {"valid": cc_valid, "context_confirmed": cc_context}

    iban_valid_n = iban_context = 0
    for m in IBAN_CANDIDATE.finditer(text):
        if iban_valid(m.group()):
            iban_valid_n += 1
            if context_hit(text, m.start(), m.end(), CONTEXT_TRIGGERS["iban_checksum_valid"]):
                iban_context += 1
    result["iban_checksum_valid"] = {"valid": iban_valid_n, "context_confirmed": iban_context}

    aws_valid = aws_context = 0
    for m in AWS_ACCESS_KEY.finditer(text):
        aws_valid += 1
        if context_hit(text, m.start(), m.end(), CONTEXT_TRIGGERS["aws_access_key"]):
            aws_context += 1
    result["aws_access_key"] = {"valid": aws_valid, "context_confirmed": aws_context}

    return result


def scan_custom(text: str, patterns: list) -> dict:
    """patterns: list of {"label": str, "regex": str, "context_keywords": [str, ...]?}.
    Returns {label: {"valid": int, "context_confirmed": int, "error": str|None}}.
    A pattern that fails to compile, times out, or is otherwise invalid gets
    valid=0, context_confirmed=0, and a plain-language error -- it never
    crashes the rest of the run."""
    result = {}
    truncated = len(text) > CUSTOM_MAX_TEXT_CHARS
    scan_text = text[:CUSTOM_MAX_TEXT_CHARS] if truncated else text

    for p in patterns:
        label = p.get("label", "unnamed_pattern")
        pattern_str = p.get("regex", "")
        keywords = p.get("context_keywords") or []

        try:
            compiled = re.compile(pattern_str)
        except re.error as e:
            result[label] = {"valid": 0, "context_confirmed": 0, "error": "invalid regex: " + str(e)}
            continue

        try:
            matches = _finditer_with_timeout(compiled, scan_text, CUSTOM_REGEX_TIMEOUT_SECONDS)
        except _RegexTimeout:
            result[label] = {
                "valid": 0,
                "context_confirmed": 0,
                "error": "regex timed out after " + str(CUSTOM_REGEX_TIMEOUT_SECONDS) + "s -- likely catastrophic backtracking, simplify the pattern",
            }
            continue

        valid = len(matches)
        context_confirmed = 0
        if keywords:
            for m in matches:
                if context_hit(scan_text, m.start(), m.end(), keywords):
                    context_confirmed += 1

        entry = {"valid": valid, "context_confirmed": context_confirmed, "error": None}
        if truncated:
            entry["note"] = "input text truncated to " + str(CUSTOM_MAX_TEXT_CHARS) + " chars before evaluation"
        result[label] = entry

    return result


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("usage: pii_patterns.py <path-to-extracted-text-file> [path-to-custom-patterns.json]", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r", errors="ignore") as f:
        content = f.read()

    output = scan(content)

    if len(sys.argv) == 3:
        with open(sys.argv[2], "r", errors="ignore") as f:
            custom_patterns = json.load(f)
        if not isinstance(custom_patterns, list):
            print("custom-patterns.json must be a JSON array", file=sys.stderr)
            sys.exit(1)
        output["custom"] = scan_custom(content, custom_patterns)

    print(json.dumps(output))
