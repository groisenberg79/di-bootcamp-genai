from pathlib import Path

from agent_app.mcp_tool_runner import PROJECT_ROOT, call_mcp_tool


def main():
    """
    Test the reusable MCP tool runner with the custom research utils server
    and the filesystem server.
    """

    citation = call_mcp_tool(
        server_name="research_utils",
        tool_name="format_citation",
        arguments={
            "title": "LoRA: Low-Rank Adaptation of Large Language Models",
            "authors": ["Edward J. Hu", "Yelong Shen", "Phillip Wallis"],
            "year": "2021",
            "url": "https://arxiv.org/abs/2106.09685",
        },
    )

    print("\nCitation result:")
    print(citation)

    output_path = PROJECT_ROOT / "notes" / "runner_test.md"

    write_result = call_mcp_tool(
        server_name="filesystem",
        tool_name="write_file",
        arguments={
            "path": str(output_path),
            "content": f"# MCP Tool Runner Test\n\nCitation:\n\n{citation}\n",
        },
    )

    print("\nFilesystem write result:")
    print(write_result)

    read_result = call_mcp_tool(
        server_name="filesystem",
        tool_name="read_text_file",
        arguments={
            "path": str(output_path),
        },
    )

    print("\nFilesystem read result:")
    print(read_result)


if __name__ == "__main__":
    main()