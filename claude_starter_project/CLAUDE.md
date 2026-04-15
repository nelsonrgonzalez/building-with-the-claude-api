# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Set up environment
uv venv
source .venv/bin/activate
uv pip install -e .

# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This is an MCP (Model Context Protocol) server that exposes document processing tools to AI assistants.

**Entry point:** [main.py](main.py) — creates a `FastMCP` server instance and registers tools via `mcp.tool()(fn)`.

**Tools** live in [tools/](tools/) as plain Python functions. Each tool is registered individually in `main.py`. Currently:
- [tools/math.py](tools/math.py) — `add`: example numeric tool
- [tools/document.py](tools/document.py) — `document_path_to_markdown`: converts a `.pdf` or `.docx` file on disk to markdown using `markitdown`; `binary_document_to_markdown` is an internal helper (not registered)

**Adding a new tool:** implement a function in `tools/`, import it in `main.py`, and register it with `mcp.tool()(my_function)`. The function's name becomes the tool name exposed to AI assistants, so name it carefully.

**Tool definition conventions:**

Tool docstrings must follow this structure:
1. One-line summary
2. Detailed explanation of functionality
3. "When to use" (and when not to use) section
4. Examples with expected input/output

Use `pydantic.Field` for all parameter descriptions — these are surfaced to AI assistants as tool metadata:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """One-line summary.

    Detailed explanation of functionality.

    When to use:
    - Situation A
    - Situation B

    Examples:
    >>> my_tool("foo", 1)
    "expected output"
    """
    # Implementation
```

**Tests** are in [tests/](tests/) using pytest. Fixtures (sample `.docx`/`.pdf` files) live in [tests/fixtures/](tests/fixtures/).

## Code Style

Always annotate function arguments and return types.
