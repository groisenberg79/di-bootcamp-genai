import streamlit as st

from agent_app.agent import run_research_workflow


st.set_page_config(
    page_title="MCP Research Notebook",
    page_icon="📚",
    layout="wide",
)


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

        st.subheader("Final message")
        st.text(final_state["final_message"])

        st.subheader("Generated brief")
        st.markdown(final_state["brief"])

        st.subheader("Output path")
        st.code(final_state["output_path"])