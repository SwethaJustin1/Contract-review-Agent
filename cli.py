#!/usr/bin/env python3
"""Run the contract review agent on a text file and print/save the report.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python cli.py examples/sample_contract.txt
"""

import argparse
import sys
from pathlib import Path

from src.agent import review_contract


def main():
    parser = argparse.ArgumentParser(description="Run the LangGraph contract review agent.")
    parser.add_argument("contract_file", help="Path to a .txt file containing the contract")
    parser.add_argument(
        "-o", "--output", default=None, help="Optional path to save the report (markdown)"
    )
    args = parser.parse_args()

    path = Path(args.contract_file)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    raw_text = path.read_text(encoding="utf-8")
    result = review_contract(raw_text, file_name=path.name)

    if result.get("error"):
        print(f"Completed with errors: {result['error']}", file=sys.stderr)

    report = result.get("final_report", "No report generated.")

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report saved to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
