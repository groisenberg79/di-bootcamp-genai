import re
from typing import TypedDict

from langgraph.graph import StateGraph, END

from agent_app.mcp_tool_runner import PROJECT_ROOT, call_mcp_tool


class ResearchState(TypedDict):
    """
    The state object that moves through the LangGraph workflow.

    Each node receives this state, reads some fields, adds or updates fields,
    and returns the updated state.
    """

    topic: str
    arxiv_results: str
    arxiv_error: str
    brief: str
    output_path: str
    final_message: str


def slugify_topic(topic: str) -> str:
    """
    Convert a research topic into a safe filename.

    Example:
    'LoRA fine-tuning sentiment analysis'
    becomes:
    'lora_fine_tuning_sentiment_analysis'
    """

    slug = topic.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = slug.strip("_")

    return slug or "research_topic"


def search_arxiv_node(state: ResearchState) -> ResearchState:
    """
    Search arXiv for papers related to the user's topic.

    To avoid repeatedly hitting the arXiv API, this node first checks a local
    cache. If cached results exist, it uses them. Otherwise, it makes one live
    arXiv request and stores the result if successful.

    If arXiv returns an error, the error is stored in the graph state so that
    the next node can build an honest error-status brief.
    """

    print("Starting search_arxiv_node...")

    topic = state["topic"]
    print(f"Research topic: {topic}")

    cache_dir = PROJECT_ROOT / "cache"
    cache_dir.mkdir(exist_ok=True)

    cache_path = cache_dir / f"{slugify_topic(topic)}.txt"

    if cache_path.exists():
        print(f"Using cached arXiv results from: {cache_path}")

        state["arxiv_results"] = cache_path.read_text(encoding="utf-8")
        state["arxiv_error"] = ""

        return state

    print("No cached result found. Calling live arXiv MCP server...")

    arxiv_results = call_mcp_tool(
        server_name="arxiv",
        tool_name="search_papers",
        arguments={
            "query": topic,
            "max_results": 3,
            "sort_by": "relevance",
        },
    )

    if arxiv_results.strip().lower().startswith("error:"):
        print("arXiv search failed.")

        state["arxiv_results"] = ""
        state["arxiv_error"] = arxiv_results

        return state

    print("Finished live arXiv search. Saving result to cache.")

    cache_path.write_text(arxiv_results, encoding="utf-8")

    state["arxiv_results"] = arxiv_results
    state["arxiv_error"] = ""

    return state


def build_brief_node(state: ResearchState) -> ResearchState:
    """
    Build a Markdown research brief.

    If the arXiv search succeeded, the brief includes the retrieved results.
    If the arXiv search failed, the brief explains the failure instead of
    pretending that papers were retrieved.
    """

    print("Starting build_brief_node...")

    topic = state["topic"]
    arxiv_results = state["arxiv_results"]
    arxiv_error = state["arxiv_error"]

    if arxiv_error:
        brief = f"""# Research Brief: {topic}

## Research Goal

This workflow attempted to retrieve arXiv papers related to **{topic}**.

## Search Status

The arXiv search did not complete successfully.

## Error Message

{arxiv_error}

## What Happened

The LangGraph workflow continued instead of crashing. It stored the arXiv error
in the graph state, generated this fallback Markdown report, and saved it using
the filesystem MCP server.

## Next Step

Retry the workflow later, or use a cached result if one has already been created
for this topic.
"""

    else:
        brief = f"""# Research Brief: {topic}

## Research Goal

This brief summarizes papers related to **{topic}**.

## Raw arXiv Search Results

{arxiv_results}

## Preliminary Notes

These results were retrieved through the arXiv MCP server and saved through the
filesystem MCP server. In a later version, the agent can parse these results,
format citations, and produce a cleaner synthesis.
"""

    state["brief"] = brief

    print("Finished building brief.")

    return state


def save_brief_node(state: ResearchState) -> ResearchState:
    """
    Save the generated Markdown brief using the filesystem MCP server.
    """

    print("Starting save_brief_node...")

    output_path = PROJECT_ROOT / "outputs" / "final_research_brief.md"

    result = call_mcp_tool(
        server_name="filesystem",
        tool_name="write_file",
        arguments={
            "path": str(output_path),
            "content": state["brief"],
        },
    )

    state["output_path"] = str(output_path)
    state["final_message"] = (
        f"Research brief created and saved to:\n{output_path}\n\n"
        f"Filesystem server response:\n{result}"
    )

    print("Finished saving brief.")

    return state


def build_research_graph():
    """
    Build and compile the LangGraph workflow.

    Current deterministic graph:

    search_arxiv -> build_brief -> save_brief -> END

    Later, this can be extended with an LLM planner node.
    """

    graph = StateGraph(ResearchState)

    graph.add_node("search_arxiv", search_arxiv_node)
    graph.add_node("build_brief", build_brief_node)
    graph.add_node("save_brief", save_brief_node)

    graph.set_entry_point("search_arxiv")

    graph.add_edge("search_arxiv", "build_brief")
    graph.add_edge("build_brief", "save_brief")
    graph.add_edge("save_brief", END)

    return graph.compile()


def run_research_workflow(topic: str) -> ResearchState:
    """
    Public function we can call from a test file or from Streamlit later.
    """

    graph = build_research_graph()

    initial_state: ResearchState = {
        "topic": topic,
        "arxiv_results": "",
        "arxiv_error": "",
        "brief": "",
        "output_path": "",
        "final_message": "",
    }

    final_state = graph.invoke(initial_state)

    return final_state