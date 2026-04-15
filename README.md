# Building with the Claude API

> A hands-on learning repository based on the **[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)** course by Anthropic.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude%20API-orange?logo=anthropic)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-purple)
![uv](https://img.shields.io/badge/uv-package%20manager-black)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## Overview

This repository contains all the work completed throughout the Anthropic course. It is organized into **three distinct sections**:

| Section | Description |
|---|---|
| [Course Notebooks](#course-notebooks) | 21 Jupyter notebooks covering the full Claude API curriculum |
| [Document Tools — MCP Server](#document-tools--mcp-server) | Standalone project: an MCP server exposing document-processing tools |
| [MCP Chat — CLI Application](#mcp-chat--cli-application) | Standalone project: a feature-rich command-line chat client with MCP integration |

---

## Course Notebooks

Located in the **root directory**, these notebooks follow the course curriculum from first API call to advanced techniques.

### Module 0 — Core API Fundamentals

| Notebook | Topic |
|---|---|
| [`001_requests.ipynb`](001_requests.ipynb) | First API requests, multi-turn conversations, message structure |
| [`001_requests_exercise.ipynb`](001_requests_exercise.ipynb) | Hands-on exercises for core API patterns |
| [`002_system_prompt.ipynb`](002_system_prompt.ipynb) | System prompts and role-setting |
| [`003_temperature.ipynb`](003_temperature.ipynb) | Temperature and sampling parameters |
| [`004_streaming.ipynb`](004_streaming.ipynb) | Streaming responses |
| [`005_controlling_output.ipynb`](005_controlling_output.ipynb) | Output formatting and control |

### Module 1 — Prompt Evaluation

| Notebook | Topic |
|---|---|
| [`101_prompt_evals.ipynb`](101_prompt_evals.ipynb) | Building automated prompt evaluation pipelines |
| [`101_prompt_evals_complete.ipynb`](101_prompt_evals_complete.ipynb) | Complete reference implementation of prompt evals |

### Module 2 — Prompting Techniques

| Notebook | Topic |
|---|---|
| [`201_prompting.ipynb`](201_prompting.ipynb) | Advanced prompting, `PromptEvaluator` class, concurrent test generation |
| [`201_prompting_exercise.ipynb`](201_prompting_exercise.ipynb) | Prompting exercises |

### Module 3 — Tool Use

| Notebook | Topic |
|---|---|
| [`301_tools.ipynb`](301_tools.ipynb) | Tool use fundamentals, function calling |
| [`301_tool_streaming.ipynb`](301_tool_streaming.ipynb) | Streaming with tool use |
| [`302_text_editor_tool.ipynb`](302_text_editor_tool.ipynb) | Built-in text editor tool |
| [`303_web_search_complete.ipynb`](303_web_search_complete.ipynb) | Web search tool integration |

### Module 4 — Retrieval-Augmented Generation (RAG)

| Notebook | Topic |
|---|---|
| [`401_chunking.ipynb`](401_chunking.ipynb) | Document chunking strategies |
| [`402_embeddings.ipynb`](402_embeddings.ipynb) | Generating and working with embeddings |
| [`403_vectordb.ipynb`](403_vectordb.ipynb) | Vector database integration |
| [`404_bm25.ipynb`](404_bm25.ipynb) | BM25 lexical search |
| [`405_hybrid.ipynb`](405_hybrid.ipynb) | Hybrid search (dense + sparse retrieval) |

### Module 5 — Advanced Claude Features

| Notebook | Topic |
|---|---|
| [`501_thinking.ipynb`](501_thinking.ipynb) | Extended thinking / chain-of-thought |
| [`502_images_and_pdf.ipynb`](502_images_and_pdf.ipynb) | Vision — images and PDF processing |
| [`503_citations.ipynb`](503_citations.ipynb) | Citations and source attribution |
| [`504_caching.ipynb`](504_caching.ipynb) | Prompt caching for cost and latency optimization |
| [`505_code_execution.ipynb`](505_code_execution.ipynb) | Code execution tool |

### Prerequisites — Course Notebooks

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com/)
- A [Voyage AI API key](https://www.voyageai.com/) (for embedding notebooks)
- Jupyter or VS Code with the Jupyter extension

```bash
pip install anthropic python-dotenv voyageai
```

Create a `.env` file in the root directory:

```
ANTHROPIC_API_KEY="your-key-here"
VOYAGE_API_KEY="your-key-here"
```

---

## Standalone Projects

The two projects below were built as part of the course and live in their own subdirectories. Each is a self-contained Python package with its own dependencies and setup.

---

## Document Tools — MCP Server

📁 [`claude_starter_project/`](claude_starter_project/)

A Python package that implements document-processing tools and exposes them via an **MCP (Model Context Protocol)** server. AI assistants connect to this server to gain document-handling capabilities.

### Features

- Converts `.pdf` and `.docx` files to Markdown via [`markitdown`](https://github.com/microsoft/markitdown)
- Exposes tools through a `FastMCP` server interface
- Extensible architecture — add a new tool by implementing a function and registering it in one line
- Full pytest test suite with fixture files

### Architecture

```
claude_starter_project/
├── main.py          # FastMCP server entry point — tool registration
└── tools/
    ├── math.py      # Example: add()
    └── document.py  # document_path_to_markdown()
```

### Setup

```bash
cd claude_starter_project

# Create and activate a virtual environment
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install in development mode
uv pip install -e .

# Start the MCP server
uv run main.py

# Run tests
uv run pytest
```

### Adding a New Tool

```python
# 1. Implement the function in tools/
from pydantic import Field

def my_tool(
    param: str = Field(description="What this parameter does")
) -> str:
    """One-line summary.

    Detailed explanation of functionality.

    When to use:
    - Situation A

    Examples:
    >>> my_tool("foo")
    "expected output"
    """
    return param.upper()

# 2. Register it in main.py
mcp.tool()(my_tool)
```

---

## MCP Chat — CLI Application

📁 [`cli_project/`](cli_project/)

A feature-rich **command-line chat interface** that connects to Claude via the Anthropic API. It integrates an MCP server for document retrieval and command-based interactions, with a polished terminal UI powered by `prompt-toolkit`.

### Features

- Interactive multi-turn chat with Claude
- **Document retrieval** — reference documents inline with `@document-id`
- **Slash commands** — execute MCP server prompts with `/command`, with Tab auto-completion
- MCP client + server architecture
- Configurable via `.env`

### Usage

```
> What is the summary of @deposition.md
> /summarize deposition.md
> Tell me about quantum computing
```

### Architecture

```
cli_project/
├── main.py          # Entry point
├── mcp_server.py    # MCP server (documents, commands)
├── mcp_client.py    # MCP client connector
└── core/
    ├── chat.py      # Chat session management
    ├── claude.py    # Anthropic API wrapper
    ├── cli.py       # CLI UI (prompt-toolkit)
    ├── cli_chat.py  # CLI chat loop
    └── tools.py     # Tool definitions
```

### Setup

```bash
cd cli_project

# Configure environment
echo 'ANTHROPIC_API_KEY="your-key-here"' > .env

# Option A — with uv (recommended)
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uv pip install -e .
uv run main.py

# Option B — with pip
python -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv prompt-toolkit "mcp[cli]==1.8.0"
python main.py
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI / LLM | Anthropic Claude API (`claude-sonnet-4-x`, `claude-haiku-4-x`) |
| Protocol | Model Context Protocol (MCP) via `FastMCP` |
| Embeddings | Voyage AI |
| Document parsing | `markitdown` (PDF, DOCX → Markdown) |
| CLI UI | `prompt-toolkit` |
| Package management | [`uv`](https://github.com/astral-sh/uv) |
| Testing | `pytest` |
| Notebooks | Jupyter |

---

## Course Reference

This repository is based on the official Anthropic course:

> **[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)**
> Available on Anthropic SkillJar — covers everything from first API call to production-ready patterns including tool use, RAG, caching, and MCP.

---

## License

[MIT](LICENSE) — free to use, modify, and distribute.
Course curriculum and materials are the property of Anthropic.
