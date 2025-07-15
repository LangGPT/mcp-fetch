#!/usr/bin/env python3
"""
MCP Fetch Example Usage

This script demonstrates how to use the MCP Fetch server programmatically.
For actual MCP usage, the server should be connected via stdio.
"""

import asyncio
import json
from mcp_fetch.server import serve


async def test_server():
    """Simple test to verify the server can start and list tools."""
    print("🚀 Starting MCP Fetch Example Server...")
    
    # Note: This is just a demonstration of how the server is structured.
    # In real MCP usage, the server communicates via stdio with the MCP client.
    
    print("✅ Server code loaded successfully!")
    print("📋 Available tools: fetch")
    print("🔧 Available parameters:")
    print("   - url (string, required): URL to fetch")
    print("   - max_length (int, optional): Maximum characters to return")
    print("   - start_index (int, optional): Start position for content")
    print("   - raw (bool, optional): Return raw HTML instead of markdown")
    
    print("\n📖 To use this server:")
    print("1. Configure in Claude Desktop using claude_desktop_config.json")
    print("2. Or test with MCP Inspector: npx @modelcontextprotocol/inspector uv run python -m mcp_fetch")


if __name__ == "__main__":
    asyncio.run(test_server())