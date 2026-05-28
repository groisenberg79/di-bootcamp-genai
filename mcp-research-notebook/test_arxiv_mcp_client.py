import asyncio
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    """
    Start the third-party arXiv MCP server, list its tools,
    and run a small paper search.
    """

    # Get the absolute path to the project root.
    project_root = Path(__file__).parent.resolve()

    # Store downloaded or cached arXiv papers inside this project.
    paper_storage_path = project_root / "papers"

    # Make sure the folder exists.
    paper_storage_path.mkdir(exist_ok=True)

    # Define how to start the arXiv MCP server.
    #
    # This is equivalent to running:
    # arxiv-mcp-server --storage-path /path/to/project/papers
    server_params = StdioServerParameters(
        command="arxiv-mcp-server",
        args=[
            "--storage-path",
            str(paper_storage_path),
        ],
    )

    # Start the server and connect through stdio.
    async with stdio_client(server_params) as (read, write):

        # Create an MCP client session over the server connection.
        async with ClientSession(read, write) as session:

            # Initialize the MCP connection.
            await session.initialize()

            # Ask the server what tools it exposes.
            tools_response = await session.list_tools()

            print("\nAvailable arXiv tools:")
            for tool in tools_response.tools:
                print(f"- {tool.name}")

            # Search arXiv for a small number of papers.
            result = await session.call_tool(
                "search_papers",
                arguments={
                    "query": "LoRA fine-tuning sentiment analysis",
                    "max_results": 3,
                    "sort_by": "relevance",
                },
            )

            print("\nsearch_papers result:")
            for item in result.content:
                print(item.text)


if __name__ == "__main__":
    asyncio.run(main())