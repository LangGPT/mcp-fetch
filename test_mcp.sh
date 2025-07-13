#!/bin/bash

# Test MCP server communication
echo "Testing MCP server..."

# Test 1: Initialize
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}}}' | uvx mcp-fetch

echo ""
echo "---"
echo ""

# Test 2: List tools (after initialization)
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}' | uvx mcp-fetch