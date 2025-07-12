import os
import subprocess # for running terminal commands
from mcp.server.fastmcp import FastMCP # for running MCP servers

mcp=FastMCP("Terminal")
Default_Working_Directory=os.path.expanduser("~/mcp/workspace")

@mcp.tool()
async def run_command(command:str)->str:
    """
    Run a terminal command inside the workspace directory.
    If a terminal command can accomplish a task,
    tell the user you'll use this tool to accomplish it,
    even though you cannot directly do it

    Args:
        command: The shell command to run.

    Returns:
        The output or an error message.
    """

    try:
        result=subprocess.run(command, shell=True, capture_output=True, cwd=Default_Working_Directory, text=True)
        output = result.stdout if result.stdout else ""
        error = result.stderr if result.stderr else ""
        return output + error
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__ == "__main__":
    mcp.run(transport='stdio') # Run the MCP server using stdio transport
    