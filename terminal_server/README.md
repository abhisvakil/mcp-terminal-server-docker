# Terminal Server - MCP Component

This is the core MCP server component that enables Claude AI to execute terminal commands in a controlled environment.

## 🎯 Purpose

The Terminal Server provides a secure bridge between Claude AI and your local terminal, allowing the AI to:
- Execute shell commands in an isolated workspace
- Manage files and directories
- Run development tools and scripts
- Install packages and dependencies

## 🏗️ Architecture

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Terminal")

@mcp.tool()
async def run_command(command: str) -> str:
    # Executes terminal commands and returns output
```

## 🔧 Implementation Details

### Key Features

1. **Tool Definition**: Uses the `@mcp.tool()` decorator to expose the `run_command` function to Claude
2. **Isolated Execution**: All commands run in `~/mcp/workspace` directory
3. **Error Handling**: Comprehensive error capture and reporting
4. **Output Capture**: Captures both stdout and stderr from commands

### Security Considerations

- **Controlled Workspace**: Commands only execute in the designated workspace directory
- **No System Access**: Cannot access your entire filesystem
- **Error Isolation**: Errors are caught and returned safely without crashing the server

### Command Execution Flow

1. Claude sends a command request via MCP protocol
2. Server receives the command and validates it
3. Command is executed in the workspace directory using `subprocess.run()`
4. Output (stdout + stderr) is captured and returned to Claude
5. Any errors are caught and returned as error messages

## 🚀 Usage

### Basic Command Execution

```python
# Claude can call this function with any shell command
result = await run_command("ls -la")
result = await run_command("mkdir new_project")
result = await run_command("pip install requests")
```

### Error Handling

The server handles various error scenarios:
- Command not found
- Permission errors
- Invalid arguments
- System errors

All errors are captured and returned as informative error messages.

## 📦 Dependencies

- `mcp>=1.0.0` - Model Context Protocol library
- `fastmcp` - FastMCP framework for building MCP servers

## 🧪 Testing

Test the server:

```bash
# Test import
python -c "import terminal_server; print('Server imports successfully')"

# Test basic functionality
python -c "
import asyncio
import terminal_server

async def test():
    result = await terminal_server.run_command('echo \"Hello MCP!\"')
    print(result)

asyncio.run(test())
"
```

## 🔒 Security Notes

- All commands run in the isolated workspace directory
- No direct filesystem access outside the workspace
- Commands are executed with the same permissions as the user running the server
- Consider implementing additional command validation if needed

## 🚀 Future Enhancements

Potential improvements:
- Command whitelisting/blacklisting
- Resource usage limits
- Command history logging
- Additional tools for file operations
- Integration with version control systems

---

**Part of the MCP Terminal Server Project** | **Built with FastMCP**
