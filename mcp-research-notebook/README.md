# MCP Research Notebook

An end-to-end agentic research notebook built with **Streamlit**, **LangGraph**, **Ollama**, and multiple **MCP servers**.

The app lets a user enter a research topic, then uses an LLM-planned LangGraph workflow to search for relevant arXiv papers, build a Markdown research brief, save the output locally, and log the workflow steps.

---

## Project Goal

The goal of this project is to demonstrate how an agentic application can compose multiple MCP servers in one workflow.

The user enters a research topic such as:

```text
LoRA fine-tuning sentiment analysis
```

The system then:

1. Uses an LLM planner to decide the next workflow action.
2. Searches arXiv through a third-party MCP server.
3. Uses caching to avoid repeated arXiv API calls.
4. Builds a Markdown research brief.
5. Saves the final brief through a filesystem MCP server.
6. Logs planner decisions and tool calls to a JSONL log file.
7. Displays the result in a Streamlit UI.

---

## Architecture

```text
User
  ↓
Streamlit UI
  ↓
LangGraph Agent Orchestrator
  ↓
Ollama LLM Planner
  ↓
MCP Tool Layer
  ├── arXiv MCP Server
  ├── Filesystem MCP Server
  └── Custom Research Utils MCP Server
  ↓
Local outputs
  ├── outputs/final_research_brief.md
  └── logs/tool_calls.jsonl
```

---

## MCP Servers Used

This project uses three MCP servers.

### 1. arXiv MCP Server

Third-party MCP server.

Used to search arXiv for research papers.

Tool used:

```text
search_papers
```

The workflow calls this server only when no cached result exists for the topic.

---

### 2. Filesystem MCP Server

Third-party MCP server.

Used to save the generated Markdown brief locally.

Tool used:

```text
write_file
```

The filesystem server is restricted to the local project directory.

---

### 3. Custom Research Utils MCP Server

Custom MCP server written for this project.

File:

```text
servers/research_utils_server.py
```

Tools exposed:

```text
format_citation
build_markdown_brief
```

These tools demonstrate how a project can expose its own local Python functions through MCP.

---

## Orchestration Library

This project uses **LangGraph** for orchestration.

The graph uses a shared state object and routes between workflow nodes.

Main workflow nodes:

```text
planner_node
search_arxiv_node
build_brief_node
save_brief_node
finish_node
```

The planner node asks the local LLM which high-level action should happen next.

Allowed planner actions:

```text
search_arxiv
build_brief
save_brief
finish
```

The LLM does not directly execute arbitrary tools. Instead, it chooses from a constrained set of actions, and LangGraph routes to the corresponding node.

This keeps the workflow agentic while avoiding uncontrolled tool use.

---

## LLM Backend

The project uses **Ollama** with the local model:

```text
llama3.1:8b
```

Environment variables are defined in `.env`:

```env
LLM_BACKEND=ollama
OLLAMA_MODEL=llama3.1:8b
OLLAMA_BASE_URL=http://localhost:11434
```

The model is used as a planner. It decides which step should happen next based on the current workflow state.

---

## Error Handling

The workflow handles arXiv failures gracefully.

If the arXiv MCP server returns an error, such as an HTTP 429 rate-limit error, the workflow does not crash.

Instead, it:

1. Stores the error in graph state.
2. Builds an honest fallback Markdown report.
3. Saves the report through the filesystem MCP server.
4. Logs the error event in `logs/tool_calls.jsonl`.

This satisfies the project requirement for error handling and fallback behavior.

---

## Caching

The workflow uses a local cache to avoid repeatedly calling arXiv.

Cache files are stored in:

```text
cache/
```

For example:

```text
cache/lora_fine_tuning_sentiment_analysis.txt
```

If a cached result exists for the topic, the workflow uses it instead of calling arXiv again.

This is important because arXiv may rate-limit repeated API requests.

The `cache/` folder is ignored by Git.

---

## Observability

The workflow logs planner decisions and tool calls to:

```text
logs/tool_calls.jsonl
```

Each line is a JSON object.

Example event types:

```text
planner_decision
tool_call
workflow_finished
```

The log records summarized inputs and outputs, without secrets.

Example log entry:

```json
{
  "timestamp": "2026-05-29T14:28:44.104819+00:00",
  "event_type": "tool_call",
  "server": "filesystem",
  "tool": "write_file",
  "status": "started",
  "path": "outputs/final_research_brief.md",
  "input_summary": "Writing Markdown brief with 5519 characters."
}
```

The `logs/` folder is ignored by Git.

---

## Project Structure

```text
mcp-research-notebook/
├── app.py
├── README.md
├── requirements.txt
├── test_ollama.py
├── test_langgraph_workflow.py
│
├── agent_app/
│   ├── __init__.py
│   ├── agent.py
│   ├── llm.py
│   ├── mcp_client.py
│   └── mcp_tool_runner.py
│
├── servers/
│   └── research_utils_server.py
│
├── notes/
├── outputs/
├── cache/
├── logs/
└── papers/
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:groisenberg79/di-bootcamp-genai.git
cd di-bootcamp-genai/mcp-research-notebook
```

---

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install and run Ollama

Install Ollama if needed:

```text
https://ollama.com
```

Pull the model:

```bash
ollama pull llama3.1:8b
```

Make sure Ollama is running:

```bash
ollama serve
```

If Ollama is already running in the background, this command may not be necessary.

---

### 5. Install the arXiv MCP server

This project uses the `arxiv-mcp-server` command.

Install with `uv`:

```bash
uv tool install arxiv-mcp-server
```

Check that it works:

```bash
arxiv-mcp-server --help
```

---

### 6. Check Node.js and npm

The filesystem MCP server is launched with `npx`.

Check:

```bash
node -v
npm -v
```

The workflow uses:

```bash
npx -y @modelcontextprotocol/server-filesystem
```

---

## Running the Project

### Run the Streamlit app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

Enter a research topic and click:

```text
Generate research brief
```

---

## Running Tests

### Test Ollama

```bash
python test_ollama.py
```

---

### Test the LangGraph workflow

```bash
python test_langgraph_workflow.py
```

This runs the workflow from the terminal and prints:

```text
planner/tool steps
final message
brief preview
```

---

## Generated Files

The app generates:

```text
outputs/final_research_brief.md
logs/tool_calls.jsonl
cache/<topic>.txt
```

These are ignored by Git because they are runtime artifacts.

---

## Notes on arXiv Rate Limiting

arXiv may temporarily rate-limit repeated API requests.

If this happens, the workflow may show an error such as:

```text
Error: arXiv is rate limiting this IP. Please wait 60 seconds before retrying.
```

This is expected external API behavior.

The workflow handles this by generating an error-status Markdown report instead of crashing.

If a cached result already exists for the topic, the workflow uses the cached result and does not call arXiv again.

---

## Requirement Mapping

| Requirement | Implementation |
|---|---|
| ≥ 2 third-party MCP servers | arXiv MCP server + filesystem MCP server |
| Custom MCP server | `servers/research_utils_server.py` |
| Runs locally | Streamlit, LangGraph, MCP servers, and Ollama run locally |
| LLM backend | Ollama with `llama3.1:8b` |
| Planning | `planner_node` uses the LLM to choose the next action |
| Tool orchestration | LangGraph routes planner actions to MCP/tool nodes |
| Error handling | arXiv errors are stored in state and reported gracefully |
| Observability | `logs/tool_calls.jsonl` records planner and tool events |
| Config | `.env` controls Ollama model and base URL |
| Reproducibility | README provides setup and run commands |
| UI | Streamlit app in `app.py` |

---

## Current Limitations

- The arXiv results are displayed from the MCP search response rather than from full paper text.
- The app does not yet deeply synthesize the papers into a polished literature review.
- The custom research-utils server exposes formatting tools, but the current LangGraph workflow mainly uses local brief-building logic.
- arXiv rate limits may affect live searches.

---

## Future Improvements

- Parse arXiv results into structured paper objects.
- Use the custom `format_citation` tool in the final graph.
- Add citation formatting to the final Markdown brief.
- Add a download button for the generated brief.
- Add retry logic for temporary network errors, while avoiding retries on HTTP 429 rate limits.
- Add a user option to force refresh the arXiv cache.