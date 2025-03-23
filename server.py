from mcp.server.fastmcp import FastMCP
import mcp.types as types
from mcp.types import AnyUrl

mcp = FastMCP("server")

# ==================== Tool ===================
@mcp.tool()
def add(a: float, b: float) -> float:
    """adds two numbers together.
    
    Args:
        a: a number
        b: a number
    """
    return a+b


# ==================== Resources ===================
@mcp.resource("file://pi.txt")
async def read_resource() -> str:
    with open('pi.txt', 'r', encoding='utf-8') as file:
        pi_digits = file.read()
        print(pi_digits)
    return pi_digits


# ==================== Prompts ===================

@mcp.prompt()
def add_to_last(number:str) -> str:
    """Creates a prompt that will encourage the agent to use proper tooling
    to add a number to the final provided digit of Pi."""

    return f"read the pi resource and add {number} to the final digit using the add tool."
