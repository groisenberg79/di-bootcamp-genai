import json
import re
from datetime import datetime, timezone
from typing import Any, Literal, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END

from agent_app.llm import get_llm
from agent_app.mcp_tool_runner import PROJECT_ROOT, call_mcp_tool


PlannerAction = Literal[
    "search_arxiv",
    "build_brief",
    "save_brief",
    "finish",
]


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
    next_action: str
    steps_taken: list[str]
    log_path: str

def log_event(event_type: str, payload: dict[str, Any]) -> None:
    """
    Append one structured event to logs/tool_calls.jsonl.

    This gives the workflow basic observability: planner decisions, tool calls,
    cache usage, errors, and file writes can be inspected after a run.
    """

    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(exist_ok=True)

    log_path = log_dir / "tool_calls.jsonl"

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        **payload,
    }

    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(event, ensure_ascii=False) + "\n")

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


def planner_node(state: ResearchState) -> ResearchState:
    """
    Ask the local Ollama model which high-level action should happen next.

    The LLM does not directly execute tools. It only chooses from a constrained
    list of allowed actions. LangGraph then routes to the corresponding node.
    """

    print("Starting planner_node...")

    llm = get_llm()

    system_prompt = """
You are the planner for a small MCP research notebook workflow.

You must choose exactly one next action from this list:

search_arxiv
build_brief
save_brief
finish

Rules:
- If there are no arXiv results and no arXiv error, choose search_arxiv.
- If there are arXiv results or an arXiv error, and there is no brief yet, choose build_brief.
- If there is a brief but no output_path yet, choose save_brief.
- If there is already an output_path, choose finish.
- Do not invent new action names.
- Return only the action name, with no explanation.
"""

    user_prompt = f"""
Current workflow state:

topic: {state["topic"]}
has_arxiv_results: {bool(state["arxiv_results"])}
has_arxiv_error: {bool(state["arxiv_error"])}
has_brief: {bool(state["brief"])}
has_output_path: {bool(state["output_path"])}
steps_taken: {state["steps_taken"]}

What is the next action?
"""

    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]
    )

    action = response.content.strip().lower()

    allowed_actions = {
        "search_arxiv",
        "build_brief",
        "save_brief",
        "finish",
    }

    if action not in allowed_actions:
        print(f"Planner returned invalid action: {action!r}. Falling back safely.")

        if not state["arxiv_results"] and not state["arxiv_error"]:
            action = "search_arxiv"
        elif not state["brief"]:
            action = "build_brief"
        elif not state["output_path"]:
            action = "save_brief"
        else:
            action = "finish"

    print(f"Planner chose next action: {action}")

    log_event(
        "planner_decision",
        {
            "action": action,
            "topic": state["topic"],
            "has_arxiv_results": bool(state["arxiv_results"]),
            "has_arxiv_error": bool(state["arxiv_error"]),
            "has_brief": bool(state["brief"]),
            "has_output_path": bool(state["output_path"]),
        },
    )

    state["next_action"] = action
    state["steps_taken"].append(f"planner:{action}")

    return state


def route_from_planner(state: ResearchState) -> str:
    """
    Route the graph based on the planner's selected action.
    """

    action = state["next_action"]

    if action == "search_arxiv":
        return "search_arxiv"

    if action == "build_brief":
        return "build_brief"

    if action == "save_brief":
        return "save_brief"

    return "finish"


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
        state["steps_taken"].append("tool:arxiv_cache")

        log_event(
            "tool_call",
            {
                "server": "local_cache",
                "tool": "read_cache",
                "status": "success",
                "topic": topic,
                "cache_path": str(cache_path),
                "output_summary": "Loaded cached arXiv results.",
            },
        )

        return state

    print("No cached result found. Calling live arXiv MCP server...")

    log_event(
    "tool_call",
    {
        "server": "arxiv",
        "tool": "search_papers",
        "status": "started",
        "topic": topic,
        "input_summary": {
            "query": topic,
            "max_results": 3,
            "sort_by": "relevance",
        },
    },
)

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
        state["steps_taken"].append("tool:arxiv_search_error")

        log_event(
            "tool_call",
            {
                "server": "arxiv",
                "tool": "search_papers",
                "status": "error",
                "topic": topic,
                "output_summary": arxiv_results[:500],
            },
        )

        return state

    print("Finished live arXiv search. Saving result to cache.")

    cache_path.write_text(arxiv_results, encoding="utf-8")

    log_event(
    "tool_call",
    {
        "server": "arxiv",
        "tool": "search_papers",
        "status": "success",
        "topic": topic,
        "cache_path": str(cache_path),
        "output_summary": arxiv_results[:500],
    },
)

    state["arxiv_results"] = arxiv_results
    state["arxiv_error"] = ""
    state["steps_taken"].append("tool:arxiv_search_success")

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
    state["steps_taken"].append("tool:build_brief")

    log_event(
        "tool_call",
        {
            "server": "local_function",
            "tool": "build_brief_node",
            "status": "success",
            "topic": topic,
            "input_summary": {
                "has_arxiv_results": bool(arxiv_results),
                "has_arxiv_error": bool(arxiv_error),
            },
            "output_summary": f"Generated Markdown brief with {len(brief)} characters.",
        },
    )

    print("Finished building brief.")

    return state


def save_brief_node(state: ResearchState) -> ResearchState:
    """
    Save the generated Markdown brief using the filesystem MCP server.
    """

    print("Starting save_brief_node...")

    output_path = PROJECT_ROOT / "outputs" / "final_research_brief.md"

    log_event(
        "tool_call",
        {
            "server": "filesystem",
            "tool": "write_file",
            "status": "started",
            "path": str(output_path),
            "input_summary": f"Writing Markdown brief with {len(state['brief'])} characters.",
        },
    )

    result = call_mcp_tool(
        server_name="filesystem",
        tool_name="write_file",
        arguments={
            "path": str(output_path),
            "content": state["brief"],
        },
    )

    state["output_path"] = str(output_path)
    state["log_path"] = str(PROJECT_ROOT / "logs" / "tool_calls.jsonl")
    state["final_message"] = (
        f"Research brief created and saved to:\n{output_path}\n\n"
        f"Filesystem server response:\n{result}"
    )
    state["steps_taken"].append("tool:filesystem_write")

    log_event(
        "tool_call",
        {
            "server": "filesystem",
            "tool": "write_file",
            "status": "success",
            "path": str(output_path),
            "output_summary": result[:500],
        },
    )

    print("Finished saving brief.")

    return state


def finish_node(state: ResearchState) -> ResearchState:
    """
    Finish the workflow.
    """

    print("Starting finish_node...")

    if not state["final_message"]:
        state["final_message"] = "Workflow finished."

    state["steps_taken"].append("finish")
    state["log_path"] = str(PROJECT_ROOT / "logs" / "tool_calls.jsonl")

    log_event(
        "workflow_finished",
        {
            "topic": state["topic"],
            "output_path": state["output_path"],
            "log_path": state["log_path"],
            "steps_taken": state["steps_taken"],
        },
    )

    return state


def build_research_graph():
    """
    Build and compile the LangGraph workflow.

    LLM-planned graph:

    planner -> selected action -> planner -> ... -> finish

    The LLM chooses the next high-level action, but the graph restricts actions
    to a safe fixed set.
    """

    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_node)
    graph.add_node("search_arxiv", search_arxiv_node)
    graph.add_node("build_brief", build_brief_node)
    graph.add_node("save_brief", save_brief_node)
    graph.add_node("finish", finish_node)

    graph.set_entry_point("planner")

    graph.add_conditional_edges(
        "planner",
        route_from_planner,
        {
            "search_arxiv": "search_arxiv",
            "build_brief": "build_brief",
            "save_brief": "save_brief",
            "finish": "finish",
        },
    )

    graph.add_edge("search_arxiv", "planner")
    graph.add_edge("build_brief", "planner")
    graph.add_edge("save_brief", "planner")
    graph.add_edge("finish", END)

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
        "next_action": "",
        "steps_taken": [],
        "log_path": str(PROJECT_ROOT / "logs" / "tool_calls.jsonl"),
    }

    final_state = graph.invoke(initial_state)

    return final_state