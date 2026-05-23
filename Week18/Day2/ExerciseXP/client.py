import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None
)


def extract_content(payload):
    """Best-effort to pull text from MCP responses."""
    if hasattr(payload, "contents"):
        contents = payload.contents
        if contents:
            first = contents[0]
            if hasattr(first, "text"):
                return first.text
            if isinstance(first, dict) and "text" in first:
                return first["text"]
            return str(first)

    if hasattr(payload, "content"):
        return payload.content

    return str(payload)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            resources = await session.list_resources()
            print("Resources:")
            for resource in resources.resources:
                print("-", resource.uri)

            tools = await session.list_tools()
            print("\nTools:")
            for tool in tools.tools:
                print("-", tool.name)

            greeting = await session.read_resource("greeting://hello")
            print("\nGreeting:")
            print(extract_content(greeting))

            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print("\nAdd result:")
            print(extract_content(result))


if __name__ == "__main__":
    asyncio.run(run())