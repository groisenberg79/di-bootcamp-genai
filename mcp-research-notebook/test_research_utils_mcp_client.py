import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    """
    Start the custom research utils MCP server, list its tools,
    and call one tool to verify that MCP communication works.
    """

    # Get the absolute path to this project folder.
    project_root = Path(__file__).parent.resolve()

    # Build the absolute path to our custom MCP server file.
    server_path = project_root / "servers" / "research_utils_server.py"

    # Define how the MCP client should start the server.
    # We use sys.executable so the server runs with the same Python interpreter
    # from the current virtual environment.
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)],
    )

    # Start the server as a subprocess and open stdio communication with it.
    async with stdio_client(server_params) as (read, write):

        # Create an MCP client session using the read/write streams.
        async with ClientSession(read, write) as session:

            # Initialize the MCP connection.
            await session.initialize()

            # Ask the server which tools it exposes.
            tools_response = await session.list_tools()

            print("\nAvailable tools:")
            for tool in tools_response.tools:
                print(f"- {tool.name}: {tool.description}")

            # Call our format_citation tool.
            result = await session.call_tool(
                "format_citation",
                arguments={
                    "title": "LoRA: Low-Rank Adaptation of Large Language Models",
                    "authors": [
                        "Edward J. Hu",
                        "Yelong Shen",
                        "Phillip Wallis",
                    ],
                    "year": "2021",
                    "url": "https://arxiv.org/abs/2106.09685",
                },
            )

            print("\nTool result:")
            for item in result.content:
                print(item.text)


if __name__ == "__main__":
    asyncio.run(main())