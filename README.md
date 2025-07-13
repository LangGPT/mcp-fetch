# MCP Fetch

A Model Context Protocol server that provides web content fetching capabilities **with robots.txt checking removed**. This server enables LLMs to retrieve and process content from web pages, converting HTML to markdown for easier consumption.

This is a modified version of the original mcp-server-fetch that removes all robots.txt checking, allowing unrestricted access to web content.

> [!CAUTION]
> This server can access local/internal IP addresses and may represent a security risk. Exercise caution when using this MCP server to ensure this does not expose any sensitive data. Additionally, this version ignores robots.txt restrictions which may violate some websites' access policies.

The fetch tool will truncate the response, but by using the `start_index` argument, you can specify where to start the content extraction. This lets models read a webpage in chunks, until they find the information they need.

## Available Tools

- `fetch` - Fetches a URL from the internet and extracts its contents as markdown.
    - `url` (string, required): URL to fetch
    - `max_length` (integer, optional): Maximum number of characters to return (default: 5000)
    - `start_index` (integer, optional): Start content from this character index (default: 0)
    - `raw` (boolean, optional): Get raw content without markdown conversion (default: false)

## Available Prompts

- **fetch**
  - Fetch a URL and extract its contents as markdown
  - Arguments:
    - `url` (string, required): URL to fetch

## Installation and Usage

### Local Development Setup

1. **Clone or download the source code:**
   ```bash
   git clone <repository-url>
   cd mcp-web-fetch
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Test the server:**
   ```bash
   uv run python -m mcp_server_fetch --help
   ```

### Using with Claude Desktop (Local Source)

1. **Create Claude Desktop configuration:**
   ```json
   {
     "mcpServers": {
       "mcp-fetch": {
         "command": "uv",
         "args": [
           "run",
           "--directory",
           "/path/to/your/mcp-web-fetch",
           "python",
           "-m",
           "mcp_server_fetch"
         ]
       }
     }
   }
   ```

2. **Add configuration to Claude Desktop:**
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

3. **Restart Claude Desktop** to load the new server.

### Using with VS Code (Local Source)

Add to your VS Code settings or `.vscode/mcp.json`:

```json
{
  "mcp": {
    "servers": {
      "mcp-fetch": {
        "command": "uv",
        "args": [
          "run",
          "--directory",
          "/path/to/your/mcp-web-fetch",
          "python",
          "-m",
          "mcp_server_fetch"
        ]
      }
    }
  }
}
```

### Installation via Package Manager

#### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-fetch*:

```bash
uvx mcp-fetch
```

#### Using pip

```bash
pip install mcp-fetch
```

After installation, run it as:
```bash
python -m mcp_server_fetch
```

### Package Manager Configuration

#### Claude Desktop with uvx

```json
{
  "mcpServers": {
    "mcp-fetch": {
      "command": "uvx",
      "args": ["mcp-web-fetch"]
    }
  }
}
```

#### VS Code with uvx

```json
{
  "mcp": {
    "servers": {
      "mcp-fetch": {
        "command": "uvx",
        "args": ["mcp-fetch"]
      }
    }
  }
}
```

## Development

### Setting up Development Environment

1. **Install development dependencies:**
   ```bash
   uv sync --dev
   ```

2. **Run linting and type checking:**
   ```bash
   uv run ruff check
   uv run pyright
   ```

3. **Build the package:**
   ```bash
   uv build
   ```

### Testing

Test the server locally:
```bash
uv run python -m mcp_server_fetch
```

Use the MCP inspector for debugging:
```bash
npx @modelcontextprotocol/inspector uv run python -m mcp_server_fetch
```

### Making Changes

1. Edit the source code in `src/mcp_server_fetch/`
2. Test your changes with `uv run python -m mcp_server_fetch`
3. Update version in `pyproject.toml` if needed
4. Run tests and linting

## Publishing

### Publishing to PyPI

1. **Build the package:**
   ```bash
   uv build
   ```

2. **Publish to PyPI:**
   ```bash
   uv publish
   ```
   
   Or using twine:
   ```bash
   pip install twine
   twine upload dist/*
   ```

### Publishing to GitHub

1. **Initialize git repository (if not already done):**
   ```bash
   git init
   git branch -m main
   ```

2. **Add and commit files:**
   ```bash
   git add .
   git commit -m "Initial commit: MCP Web Fetch server without robots.txt checking"
   ```

3. **Create GitHub repository and push:**
   ```bash
   # Create repository on GitHub first, then:
   git remote add origin https://github.com/langgpt/mcp-web-fetch.git
   git push -u origin main
   ```

4. **Create a release on GitHub:**
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Tag version: `v0.6.3`
   - Release title: `v0.6.3 - MCP Web Fetch`
   - Describe your changes
   - Publish release

### Building Docker Image

```bash
docker build -t mcp-web-fetch .
docker tag mcp-web-fetch langgpt/mcp-web-fetch:latest
docker push langgpt/mcp-web-fetch:latest
```

## Customization

### robots.txt

**This version has robots.txt checking completely removed.** All web requests will proceed regardless of robots.txt restrictions.

### User-agent

By default, depending on if the request came from the model (via a tool), or was user initiated (via a prompt), the
server will use either the user-agent:
```
ModelContextProtocol/1.0 (Autonomous; +https://github.com/modelcontextprotocol/servers)
```
or:
```
ModelContextProtocol/1.0 (User-Specified; +https://github.com/modelcontextprotocol/servers)
```

This can be customized by adding the argument `--user-agent=YourUserAgent` to the `args` list in the configuration.

### Proxy

The server can be configured to use a proxy by using the `--proxy-url` argument.

## Debugging

You can use the MCP inspector to debug the server:

For local development:
```bash
npx @modelcontextprotocol/inspector uv run python -m mcp_server_fetch
```

For uvx installations:
```bash
npx @modelcontextprotocol/inspector uvx mcp-fetch
```

## Contributing

This is a modified version of the original mcp-server-fetch. For contributing to the original project, see:
https://github.com/modelcontextprotocol/servers

For this modified version, please submit issues and pull requests to this repository.

## License

mcp-fetch is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.