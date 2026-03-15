# 🤖 Enterprise Multi-Agent Orchestrator

[![Python](https://img.shields.io/badge/Language-Python%203.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Framework-LangGraph-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 🌟 Overview
**Enterprise Multi-Agent Orchestrator** is a robust framework designed to automate complex, multi-step enterprise workflows using specialized Large Language Model (LLM) agents. Built specifically for software testing and validation lifecycles, it leverages a stateful, graph-based architecture to ensure deterministic outputs from non-deterministic models.

## 🏗️ Architectural Design
This system moves beyond linear prompt chaining by implementing a **Directed Acyclic Graph (DAG)** using `LangGraph`.

1.  **Router Agent:** Analyzes incoming unstructured requirements and routes tasks to specialized sub-agents.
2.  **Test Generation Agent:** Converts natural language requirements into executable test scenarios (e.g., PyTest, Selenium).
3.  **Code Review Agent:** Audits the generated test code for syntax, coverage, and security vulnerabilities.
4.  **State Management:** Maintains a persistent memory context across the entire workflow graph.

## 📂 Repository Structure
```text
├── api/                  # FastAPI endpoints for workflow triggering
├── core/                 # Graph definitions and state management
├── agents/               # Individual specialized LLM agents
├── models/               # Pydantic schemas for data validation
├── tests/                # Unit and integration tests
├── .github/workflows/    # CI/CD and automated evaluation pipelines
└── requirements.txt      # Project dependencies
```

## 🚀 Quick Start
### Prerequisites
- Python 3.10+
- OpenAI API Key (or Azure OpenAI endpoints)

### Installation
```bash
git clone https://github.com/MohamedBenzaghtaa/Enterprise-Multi-Agent-Orchestrator.git
cd Enterprise-Multi-Agent-Orchestrator
pip install -r requirements.txt
```

### Running the API
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🧪 Testing
```bash
pytest tests/ -v --cov=core
```

---
**Architected by [Mohamed Benzaghta](https://github.com/MohamedBenzaghtaa)**  
*Senior AI Engineer | Bridging AI Research & Enterprise Products*
