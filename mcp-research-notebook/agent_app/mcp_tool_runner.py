import asyncio
import sys
from pathlib import Path
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


PROJECT_ROOT = Path(__file__).parent.parent.resolve()


def get_server_params(server_name: str) -> StdioServerParameters:
    """
    Return the startup command for each MCP server used in the project.

    This keeps all server startup details in one place.
    """

    if server_name == "research_utils":
        server_path = PROJECT_ROOT / "servers" / "research_utils_server.py"

        return StdioServerParameters(
            command=sys.executable,
            args=[str(server_path)],
        )

    if server_name == "filesystem":
        return StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                str(PROJECT_ROOT),
            ],
        )

    if server_name == "arxiv":
        paper_storage_path = PROJECT_ROOT / "papers"
        paper_storage_path.mkdir(exist_ok=True)

        return StdioServerParameters(
            command="arxiv-mcp-server",
            args=[
                "--storage-path",
                str(paper_storage_path),
            ],
        )

    raise ValueError(f"Unknown server name: {server_name}")


async def call_mcp_tool_async(
    server_name: str,
    tool_name: str,
    arguments: dict[str, Any],
) -> str:
    """
    Start one MCP server, call one tool, return the text result.

    This is the low-level bridge between our Python app/LangGraph agent
    and the MCP servers.
    """

    server_params = get_server_params(server_name)

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments=arguments,
            )

            text_blocks = []

            for item in result.content:
                if hasattr(item, "text"):
                    text_blocks.append(item.text)
                else:
                    text_blocks.append(str(item))

            return "\n".join(text_blocks)


def call_mcp_tool(
    server_name: str,
    tool_name: str,
    arguments: dict[str, Any],
) -> str:
    """
    Synchronous wrapper around the async MCP tool call.

    LangGraph nodes can call this regular function without directly managing
    asyncio in every node.
    """

    return asyncio.run(
        call_mcp_tool_async(
            server_name=server_name,
            tool_name=tool_name,
            arguments=arguments,
        )
    )