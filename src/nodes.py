"""LangGraph node functions for the contract review agent.

Each node takes the current ContractReviewState and returns a dict of the
fields it updates -- the standard LangGraph node contract.
"""

import json
import os
from anthropic import Anthropic

from .state import ContractReviewState
from .prompts import CLAUSE_EXTRACTION_PROMPT, RISK_ASSESSMENT_PROMPT, SUMMARY_PROMPT

_client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
_MODEL = "claude-sonnet-4-5"


def _call_claude(prompt: str) -> str:
    response = _client.messages.create(
        model=_MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def _parse_json_array(raw: str):
    """Best-effort parse of a JSON array from a model response, tolerating
    stray whitespace or accidental markdown fences."""
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.replace("json\n", "", 1)
    return json.loads(cleaned)


def extract_clauses(state: ContractReviewState) -> dict:
    """Node 1: pull structured clauses out of raw contract text."""
    prompt = CLAUSE_EXTRACTION_PROMPT.format(contract_text=state["raw_text"])
    try:
        raw = _call_claude(prompt)
        clauses = _parse_json_array(raw)
    except (json.JSONDecodeError, IndexError) as e:
        return {"error": f"clause extraction failed: {e}", "clauses": []}
    return {"clauses": clauses}


def assess_risk(state: ContractReviewState) -> dict:
    """Node 2: score each extracted clause for risk severity."""
    if not state.get("clauses"):
        return {"risk_flags": [], "requires_escalation": False}

    prompt = RISK_ASSESSMENT_PROMPT.format(clauses_json=json.dumps(state["clauses"]))
    try:
        raw = _call_claude(prompt)
        risk_flags = _parse_json_array(raw)
    except (json.JSONDecodeError, IndexError) as e:
        return {"error": f"risk assessment failed: {e}", "risk_flags": []}

    high_risk_present = any(flag.get("severity") == "high" for flag in risk_flags)
    return {"risk_flags": risk_flags, "requires_escalation": high_risk_present}


def summarize(state: ContractReviewState) -> dict:
    """Node 3: produce a plain-language summary for a non-lawyer reader."""
    prompt = SUMMARY_PROMPT.format(
        clauses_json=json.dumps(state.get("clauses", [])),
        risk_flags_json=json.dumps(state.get("risk_flags", [])),
    )
    summary_text = _call_claude(prompt)
    return {"summary": summary_text}


def compile_report(state: ContractReviewState) -> dict:
    """Node 4: assemble the final human-readable report."""
    lines = [f"# Contract Review Report: {state.get('file_name', 'contract')}", ""]

    if state.get("requires_escalation"):
        lines.append("**⚠ ESCALATION RECOMMENDED — one or more high-severity clauses found.**\n")

    lines.append("## Summary")
    lines.append(state.get("summary", "No summary generated."))
    lines.append("")

    lines.append("## Risk Flags")
    risk_flags = state.get("risk_flags", [])
    if not risk_flags:
        lines.append("No risk flags identified.")
    else:
        for flag in risk_flags:
            lines.append(
                f"- **{flag['clause_type']}** [{flag['severity'].upper()}] — "
                f"{flag['reason']} → *{flag['recommendation']}*"
            )
    lines.append("")

    lines.append("## Extracted Clauses")
    for clause in state.get("clauses", []):
        lines.append(f"### {clause['clause_type']} ({clause.get('location_hint', 'unspecified')})")
        lines.append(clause["text"])
        lines.append("")

    return {"final_report": "\n".join(lines)}
