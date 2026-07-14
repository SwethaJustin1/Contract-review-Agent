CLAUSE_EXTRACTION_PROMPT = """You are a contract analysis assistant. Read the contract text below and \
identify the distinct clauses it contains (e.g. Termination, Indemnification, Payment Terms, \
Confidentiality, Liability, Governing Law, Renewal, IP Ownership, Force Majeure).

For each clause found, return a JSON array of objects with exactly these keys:
- "clause_type": short label for the clause
- "text": the verbatim or lightly condensed clause text
- "location_hint": a short reference like "Section 3" or "para 2" if identifiable, else "unspecified"

Return ONLY the JSON array, no commentary, no markdown fences.

CONTRACT TEXT:
{contract_text}
"""

RISK_ASSESSMENT_PROMPT = """You are a contract risk reviewer supporting a non-lawyer business user \
(a delivery manager). For each clause below, assess risk from the perspective of the party \
receiving/signing the contract (assume our organization is the vendor/service provider unless \
the clause clearly indicates otherwise).

For each clause, return a JSON array of objects with exactly these keys:
- "clause_type": matches the input clause_type
- "severity": one of "low", "medium", "high"
- "reason": one sentence on why this severity was assigned
- "recommendation": one sentence of practical next-step guidance (e.g. "escalate to legal", \
"acceptable as-is", "negotiate cap on liability")

Return ONLY the JSON array, no commentary, no markdown fences.

CLAUSES:
{clauses_json}
"""

SUMMARY_PROMPT = """Write a plain-language summary (120-180 words) of this contract for a delivery \
manager who is not a lawyer. Cover: what the contract is for, the key obligations on each side, \
and the two or three points that most need attention before signing. Avoid legal jargon.

CLAUSES:
{clauses_json}

RISK FLAGS:
{risk_flags_json}
"""
