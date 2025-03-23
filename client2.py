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
            
            print('simulating asking the client to add 1 to the last digit in pi.txt...\n')
            

            print('\n======== Listing Resources =========')

            # Initialize the connection
            await session.initialize()

            # List all available things
            response = await session.list_tools()
            print('\ntools:')
            print(response.tools)
            response = await session.list_resources()
            print('\nresources:')
            print(response.resources)
            response = await session.list_prompts()
            print('\nprompts:')
            print(response.prompts)

            number_to_add = 1

            print('\n======== Getting Prompt =========')

            # Getting the add_to_last prompt
            prompt = await session.get_prompt(
                "add_to_last", arguments={"number": str(number_to_add)}
            )
            print(prompt.messages[0].content.text)

            print('\n======== Getting Resource =========')

            # Reading the pi.txt file
            _, mime_type = await session.read_resource("file://pi.txt/")
            pi_digits = mime_type[1][0].text
            print(pi_digits)

            print('\n======== Adding to last digit =========')
            #adding digits together
            last_digit = int(pi_digits[-1])
            result = await session.call_tool("add", arguments={"a": str(last_digit), "b": str(number_to_add)})
            print(result)


            

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())