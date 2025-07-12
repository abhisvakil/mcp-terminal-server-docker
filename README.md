# MCP Terminal Server 🚀

My first Model Context Protocol (MCP) server that enables Claude AI to manage local files and directories through terminal commands. This project demonstrates how to create a secure bridge between AI assistants and your local development environment.

## 🌟 What is MCP?

Model Context Protocol (MCP) is a protocol that allows AI assistants like Claude to communicate with external tools and services on your local machine. It's like a secure bridge between the AI and your system, enabling powerful local development workflows.

## 🎯 Project Overview

This MCP server provides Claude with the ability to:
- Execute terminal commands in a controlled workspace
- Manage files and directories
- Run development tools and scripts
- Install packages and dependencies
- All while maintaining security through isolated execution

## 🏗️ Architecture

```
┌─────────────────┐    MCP Protocol    ┌──────────────────┐    Shell Commands    ┌─────────────┐
│                 │◄──────────────────►│                  │◄────────────────────►│             │
│   Claude AI     │                    │  Terminal Server │                      │   Terminal  │
│                 │                    │  (Python Script) │                      │             │
└─────────────────┘                    └──────────────────┘                      └─────────────┘
                                              │
                                              ▼
                                       ┌─────────────┐
                                       │ ~/mcp/      │
                                       │ workspace/  │
                                       └─────────────┘
```

## 🚀 Features

- **Secure Command Execution**: All commands run in an isolated workspace directory
- **Error Handling**: Comprehensive error capture and reporting
- **MCP Protocol Compliance**: Full compatibility with Claude Desktop
- **Easy Configuration**: Simple setup with clear documentation

## 📦 Installation

### Prerequisites

- Python 3.9+
- Claude Desktop application
- MCP library (`pip install mcp>=1.0.0`)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mcp-terminal-server.git
   cd mcp-terminal-server
   ```

2. **Install dependencies**:
   ```bash
   cd servers/terminal_server
   pip install -e .
   ```

3. **Configure Claude Desktop**:
   
   Open your Claude Desktop config file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

   Add the following configuration:
   ```json
   {
       "mcpServers": {
           "terminal": {
               "command": "/path/to/your/python",
               "args": [
                   "/path/to/mcp-terminal-server/servers/terminal_server/terminal_server.py"
               ]
           }
       }
   }
   ```

4. **Restart Claude Desktop** to load the new configuration.

## 🛠️ Usage

Once configured, you can ask Claude to perform terminal operations:

- "Create a new Python project in the workspace"
- "List all files in the workspace"
- "Install the requests package"
- "Run the test suite"
- "Create a backup of the current project"

## 🔧 Development

### Project Structure

```
mcp-terminal-server/
├── servers/
│   └── terminal_server/
│       ├── terminal_server.py    # Main MCP server implementation
│       ├── pyproject.toml        # Python project configuration
│       └── README.md            # Server-specific documentation
├── workspace/                   # Default working directory for commands
├── .vscode/                    # VS Code configuration
└── README.md                   # This file
```

### Key Components

#### `terminal_server.py`
The main MCP server that:
- Defines the `run_command` tool for Claude
- Handles command execution in the workspace
- Provides error handling and output capture

#### `pyproject.toml`
Python project configuration with:
- MCP dependency specification
- Build system configuration
- Project metadata

## 🔒 Security Features

1. **Isolated Workspace**: All commands run in `~/mcp/workspace`
2. **Controlled Access**: Only specific tools are exposed to Claude
3. **Error Handling**: Safe error capture and reporting
4. **No System Access**: Commands cannot access your entire filesystem

## 🧪 Testing

Test your MCP server:

```bash
cd servers/terminal_server
python -c "import terminal_server; print('Server imports successfully')"
```

## 📝 Configuration Examples

### Different Python Interpreters

**Anaconda/Miniconda**:
```json
{
    "command": "/opt/anaconda3/bin/python",
    "args": ["/path/to/terminal_server.py"]
}
```

**System Python**:
```json
{
    "command": "/usr/bin/python3",
    "args": ["/path/to/terminal_server.py"]
}
```

**Virtual Environment**:
```json
{
    "command": "/path/to/venv/bin/python",
    "args": ["/path/to/terminal_server.py"]
}
```

## 🤝 Contributing

This is my first MCP project! Feel free to:
- Report issues
- Suggest improvements
- Share your own MCP server creations

## 📚 Learning Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Claude Desktop MCP Guide](https://docs.anthropic.com/claude/docs/model-context-protocol-mcp)
- [FastMCP Library](https://github.com/jlowin/fastmcp)

## 🎉 My MCP Journey

This project marks the beginning of my exploration into Model Context Protocol. MCP opens up incredible possibilities for AI-assisted development, allowing Claude to become a true development partner that can interact with your local environment safely and effectively.

**Key Learnings**:
- Understanding the MCP protocol and its capabilities
- Building secure bridges between AI and local systems
- Creating tools that enhance AI assistant functionality
- The power of controlled, isolated command execution

## 📄 License

MIT License - feel free to use this project as a starting point for your own MCP servers!

---

**Built with ❤️ and MCP** | **My first step into the future of AI-assisted development** 