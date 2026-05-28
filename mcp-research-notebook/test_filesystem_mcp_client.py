import asyncio
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    """
    Start the third-party filesystem MCP server, list its tools,
    and write a small test file into the local notes/ folder.
    """

    # Get the absolute path to the project root.
    project_root = Path(__file__).parent.resolve()

    # The filesystem MCP server will only be allowed to access this folder.
    allowed_directory = str(project_root)

    # Define how to start the filesystem MCP server.
    # We use npx so we do not need to manually clone the server repo.
    server_params = StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            allowed_directory,
        ],
    )

    # Start the server and connect through stdio.
    async with stdio_client(server_params) as (read, write):

        # Create an MCP session.
        async with ClientSession(read, write) as session:

            # Initialize the MCP handshake.
            await session.initialize()

            # Ask the server which tools it exposes.
            tools_response = await session.list_tools()

            print("\nAvailable filesystem tools:")
            for tool in tools_response.tools:
                print(f"- {tool.name}")

            # Write a small test file inside the notes folder.
            result = await session.call_tool(
                "write_file",
                arguments={
                    "path": str(project_root / "notes" / "filesystem_test.md"),
                    "content": "# Filesystem MCP Test\n\nThis file was written through the filesystem MCP server.\n",
                },
            )

            print("\nwrite_file result:")
            for item in result.content:
                print(item.text)

            # Read the file back to prove it was created correctly.
            result = await session.call_tool(
                "read_text_file",
                arguments={
                    "path": str(project_root / "notes" / "filesystem_test.md"),
                },
            )

            print("\nread_text_file result:")
            for item in result.content:
                print(item.text)


if __name__ == "__main__":
    asyncio.run(main())