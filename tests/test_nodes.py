"""Lightweight tests that don't require an Anthropic API key.

Only compile_report is pure/deterministic given a state dict, so it's the
one node tested without mocking the LLM call. Run with: pytest tests/
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.nodes import compile_report


def test_compile_report_includes_escalation_banner_when_high_risk():
    state = {
        "file_name": "test.txt",
        "requires_escalation": True,
        "summary": "A short summary.",
        "risk_flags": [
            {
                "clause_type": "Indemnification",
                "severity": "high",
                "reason": "Uncapped indemnification obligation.",
                "recommendation": "Escalate to legal for a liability cap.",
            }
        ],
        "clauses": [
            {
                "clause_type": "Indemnification",
                "text": "Client shall indemnify Vendor without limitation...",
                "location_hint": "Section 4",
            }
        ],
    }

    result = compile_report(state)

    assert "ESCALATION RECOMMENDED" in result["final_report"]
    assert "Indemnification" in result["final_report"]


def test_compile_report_handles_no_risk_flags():
    state = {
        "file_name": "clean.txt",
        "requires_escalation": False,
        "summary": "All clear.",
        "risk_flags": [],
        "clauses": [],
    }

    result = compile_report(state)

    assert "No risk flags identified." in result["final_report"]
    assert "ESCALATION RECOMMENDED" not in result["final_report"]
