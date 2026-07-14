# Contract Review Agent (LangGraph)

A multi-step AI agent that reviews a contract, extracts its clauses, flags risk areas, and
produces a plain-language summary report for a non-lawyer business reader (e.g. a delivery
manager deciding whether to escalate a contract to legal).

Built with [LangGraph](https://langchain-ai.github.io/langgraph/) as a personal project to get
hands-on with agentic workflow design — state graphs, multi-step reasoning, and structured
outputs from an LLM — rather than a single-prompt wrapper.

## Why this project

I work on AI adoption and use-case enablement in an enterprise managed-services environment,
where I evaluate GenAI use cases (including a LangGraph-based contract review agent built by our
dev team) rather than building them myself. I built this project independently to get real,
hands-on experience with LangGraph's graph-based agent architecture — designing state, wiring
nodes, and handling conditional logic — rather than just reviewing others' output.

## Architecture

```
raw contract text
       │
       ▼
┌─────────────────┐
│ extract_clauses │   → pulls structured clauses (type, text, location) from raw text
└─────────────────┘
       │
       ▼
┌─────────────────┐
│  assess_risk     │   → scores each clause low/medium/high, sets escalation flag
└─────────────────┘
       │
       ▼
┌─────────────────┐
│   summarize      │   → plain-language summary for a non-lawyer reader
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ compile_report   │   → assembles the final markdown report
└─────────────────┘
       │
       ▼
  final report (with escalation banner if high risk found)
```

Each step is a LangGraph node operating on a shared `ContractReviewState` (see `src/state.py`),
so the graph is easy to extend — for example, adding a conditional branch that routes
high-risk contracts to a separate "legal escalation" node instead of straight to the report.

## Setup

```bash
git clone https://github.com/<your-username>/contract-review-agent.git
cd contract-review-agent
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
```

## Usage

```bash
python cli.py examples/sample_contract.txt
```

Or save the report to a file:

```bash
python cli.py examples/sample_contract.txt -o report.md
```

The included `examples/sample_contract.txt` is a synthetic Master Services Agreement (not a
real client contract) with a deliberately uncapped indemnification clause, so the demo run
triggers the high-risk escalation path.

## Project structure

```
contract-review-agent/
├── cli.py                  # entry point
├── src/
│   ├── state.py            # shared state schema (TypedDict)
│   ├── prompts.py          # prompt templates for each node
│   ├── nodes.py            # node functions (extract, assess, summarize, compile)
│   └── agent.py            # StateGraph wiring
├── examples/
│   └── sample_contract.txt # synthetic demo contract
├── tests/
│   └── test_nodes.py       # deterministic tests (no API key required)
└── requirements.txt
```

## Running tests

```bash
pip install -r requirements.txt
pytest tests/
```

(Tests cover the deterministic `compile_report` node only — the LLM-calling nodes are
integration-tested manually via the CLI, since mocking the Anthropic API is out of scope for
this demo.)

## Limitations / next steps

- No conditional routing yet — a natural extension is branching high-risk contracts to a
  dedicated "flag for legal" node instead of just annotating the report.
- No PDF ingestion yet — currently takes plain text input.
- Prompts are tuned for general commercial contracts (MSAs, vendor agreements), not
  specialized domains (employment, IP licensing).

## Disclaimer

This is a generic personal learning project built with synthetic data, for demonstrating
LangGraph agent design and building my own hands-on skills. It is not affiliated with, and does
not use any code, data, or confidential information from, any employer. It is not legal advice
and should not be used to make real contract decisions without qualified legal review.
