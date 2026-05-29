import json

import streamlit as st

from agent_app.agent import run_research_workflow


st.set_page_config(
    page_title="MCP Research Notebook",
    page_icon="📚",
    layout="wide",
)


def format_arxiv_results_as_markdown(arxiv_results: str) -> str:
    """
    Convert the raw JSON-like arXiv MCP result into readable Markdown for the UI.

    If parsing fails, return the raw text so the user can still inspect it.
    """

    try:
        data = json.loads(arxiv_results)
    except json.JSONDecodeError:
        return arxiv_results

    papers = data.get("papers", [])

    if not papers:
        return "No papers were returned by the arXiv search."

    markdown_parts = []

    for index, paper in enumerate(papers, start=1):
        title = paper.get("title", "Untitled paper")
        authors = paper.get("authors", [])
        published = paper.get("published", "Unknown publication date")
        url = paper.get("url", "No URL available")
        abstract = paper.get("abstract", "No abstract available")
        categories = paper.get("categories", [])

        authors_text = ", ".join(authors) if isinstance(authors, list) else str(authors)
        categories_text = ", ".join(categories) if isinstance(categories, list) else str(categories)

        markdown_parts.append(
            f"### {index}. {title}\n\n"
            f"**Authors:** {authors_text or 'Unknown author'}\n\n"
            f"**Published:** {published}\n\n"
            f"**Categories:** {categories_text or 'No categories listed'}\n\n"
            f"**Link:** {url}\n\n"
            f"**Abstract:**\n\n{abstract}\n"
        )

    return "\n---\n\n".join(markdown_parts)


def build_display_brief(final_state: dict) -> str:
    """
    Build a readable Markdown version of the brief for display in Streamlit.

    The saved brief may still contain raw MCP output, but the UI can present the
    arXiv results in a cleaner format.
    """

    topic = final_state.get("topic", "Research topic")
    arxiv_results = final_state.get("arxiv_results", "")
    arxiv_error = final_state.get("arxiv_error", "")

    if arxiv_error:
        return final_state.get("brief", "")

    if not arxiv_results:
        return final_state.get("brief", "")

    formatted_results = format_arxiv_results_as_markdown(arxiv_results)

    return f"""# Research Brief: {topic}

## Research Goal

This brief summarizes papers related to **{topic}**.

## Selected Papers

{formatted_results}

## Preliminary Notes

These results were retrieved through the arXiv MCP server and displayed in a
more readable Markdown format in the Streamlit UI.
"""


st.title("📚 MCP Research Notebook")

st.write(
    """
    This app uses a LangGraph workflow connected to MCP servers to search for
    research papers, build a Markdown brief, and save the result locally.
    """
)


topic = st.text_input(
    "Research topic",
    value="LoRA fine-tuning sentiment analysis",
)


if st.button("Generate research brief"):
    if not topic.strip():
        st.error("Please enter a research topic.")
    else:
        with st.spinner("Running LangGraph workflow..."):
            final_state = run_research_workflow(topic.strip())

        st.success("Workflow completed.")

        st.subheader("Planner / Tool Steps")
        for step in final_state.get("steps_taken", []):
            st.write(f"- {step}")

        st.subheader("Final message")
        st.text(final_state["final_message"])

        st.subheader("Generated brief")
        st.markdown(build_display_brief(final_state))

        st.subheader("Output path")
        st.code(final_state["output_path"])

        st.subheader("Log file")
        st.code(final_state.get("log_path", "No log path available"))