from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"], 
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            
            # Initialize the connection
            await session.initialize()

            # List available tools
            response = await session.list_tools()
            print('\n\ntools:')
            print(response.tools)

            # List available resources
            response = await session.list_resources()
            print('\n\nresources:')
            print(response.resources)

            # List available prompts
            response = await session.list_prompts()
            print('\n\nprompts:')
            print(response.prompts)

            

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())