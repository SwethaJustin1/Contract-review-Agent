# Contract Review Agent (LangGraph)

A multi-step AI agent that reviews a contract, extracts its clauses, flags risk areas, and
produces a plain-language summary report for user who can deciding whether to escalate a contract to legal team

Built with [LangGraph](https://langchain-ai.github.io/langgraph/) as a personal project to get

1.hands-on with agentic workflow design — 
state graphs,multi-step reasoning, and structured
outputs from an LLM .

## why choose this  project

I work on AI adoption and use-case enablement in an enterprise managed-services environment,
 I built this project independently to get real,hands-on experience with LangGraph's graph-based agent architecture , logic than just looking at others outputs

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

The included `examples/sample_contract.txt` is a mock up Services Agreement for the demo run.

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
integration-tested manually via the CLI .
## Limitations / next steps

No PDF ingestion yet — currently takes plain text input.
No conditional routing yet 
Prompts are tuned for general commercial contracts 

## Disclaimer

This is a generic personal learning project built with synthetic mockup data, for demonstrating
LangGraph agent design and building my own hands-on skills. It is not affiliated with, and does
not use any code, data, or confidential information from, any employer. 
