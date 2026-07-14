"""State schema shared across all nodes in the contract review graph."""

from typing import TypedDict, List, Optional


class Clause(TypedDict):
    clause_type: str        # e.g. "Termination", "Indemnification", "Payment Terms"
    text: str                # the extracted clause text
    location_hint: str       # section/paragraph reference for traceability


class RiskFlag(TypedDict):
    clause_type: str
    severity: str             # "low" | "medium" | "high"
    reason: str
    recommendation: str


class ContractReviewState(TypedDict, total=False):
    # input
    raw_text: str
    file_name: str

    # working state populated by nodes
    clauses: List[Clause]
    risk_flags: List[RiskFlag]
    summary: str
    final_report: str

    # control flow
    requires_escalation: bool
    error: Optional[str]
