"""Assembles the contract review nodes into a LangGraph StateGraph."""

from langgraph.graph import StateGraph, END

from .state import ContractReviewState
from .nodes import extract_clauses, assess_risk, summarize, compile_report


def build_graph():
    graph = StateGraph(ContractReviewState)

    graph.add_node("extract_clauses", extract_clauses)
    graph.add_node("assess_risk", assess_risk)
    graph.add_node("summarize", summarize)
    graph.add_node("compile_report", compile_report)

    graph.set_entry_point("extract_clauses")
    graph.add_edge("extract_clauses", "assess_risk")
    graph.add_edge("assess_risk", "summarize")
    graph.add_edge("summarize", "compile_report")
    graph.add_edge("compile_report", END)

    return graph.compile()


def review_contract(raw_text: str, file_name: str = "contract.txt") -> ContractReviewState:
    """Convenience entry point: run the full graph on a piece of contract text."""
    app = build_graph()
    result = app.invoke({"raw_text": raw_text, "file_name": file_name})
    return result
