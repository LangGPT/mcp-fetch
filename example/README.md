# MCP Fetch - Python SDK Example

这是一个使用 Python MCP SDK 构建的 Model Context Protocol 服务器示例，提供无 robots.txt 限制的网页内容获取功能。

## 项目结构

```
example/
├── src/
│   └── mcp_fetch/
│       ├── __init__.py      # 主入口点和命令行处理
│       ├── __main__.py      # 模块执行入口
│       └── server.py        # MCP 服务器核心逻辑
├── pyproject.toml           # 项目配置和依赖
├── README.md               # 本文档
├── LICENSE                 # MIT 许可证
└── .gitignore             # Git 忽略规则
```

## 功能特性

- ✅ 使用 Python MCP SDK 构建
- ✅ 提供 `fetch` 工具，支持网页内容获取
- ✅ HTML 到 Markdown 自动转换
- ✅ 移除了 robots.txt 检查限制
- ✅ 支持分块读取大型页面
- ✅ 支持自定义 User-Agent
- ✅ 支持代理配置

## 开发和测试

### 本地开发

1. **安装依赖**：
   ```bash
   cd example
   uv sync
   ```

2. **运行服务器**：
   ```bash
   uv run python -m mcp_fetch --help
   ```

3. **使用 MCP Inspector 调试**：
   ```bash
   npx @modelcontextprotocol/inspector uv run python -m mcp_fetch
   ```

### 代码结构说明

#### `src/mcp_fetch/__init__.py`
- 定义主入口函数 `main()`
- 处理命令行参数解析
- 启动异步服务器

#### `src/mcp_fetch/server.py`
- 实现 MCP 服务器核心逻辑
- 定义 `fetch` 工具和相关参数
- 处理网页获取和内容转换

#### `pyproject.toml`
- 项目元数据和依赖配置
- 构建系统配置
- 入口点定义

## Claude Desktop 配置

### 使用发布版本
```json
{
  "mcpServers": {
    "mcp-fetch": {
      "command": "uvx",
      "args": ["mcp-fetch"]
    }
  }
}
```

### 使用本地开发版本
```json
{
  "mcpServers": {
    "mcp-fetch-local": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/your/example",
        "python",
        "-m",
        "mcp_fetch"
      ]
    }
  }
}
```

## 工具使用示例

### fetch 工具

获取网页内容并转换为 Markdown：

```json
{
  "name": "fetch",
  "arguments": {
    "url": "https://example.com",
    "max_length": 5000,
    "start_index": 0,
    "raw": false
  }
}
```

参数说明：
- `url` (string, 必需): 要获取的 URL
- `max_length` (integer, 可选): 返回的最大字符数，默认 5000
- `start_index` (integer, 可选): 开始位置，默认 0
- `raw` (boolean, 可选): 是否返回原始 HTML，默认 false

## 构建和发布

### 构建包
```bash
uv build
```

### 发布到 PyPI
```bash
uv publish
```

## 扩展开发

基于此示例，你可以：

1. **添加新工具**：在 `server.py` 中添加新的工具定义
2. **修改参数**：调整 `Fetch` 模型的参数配置
3. **添加认证**：实现 API 密钥或其他认证机制
4. **错误处理**：增强错误处理和日志记录
5. **缓存功能**：添加内容缓存机制

## 关键学习点

### MCP SDK 使用模式

1. **服务器初始化**：
   ```python
   server = Server("server-name")
   ```

2. **工具注册**：
   ```python
   @server.list_tools()
   async def list_tools() -> list[Tool]:
       return [Tool(...)]
   ```

3. **工具调用处理**：
   ```python
   @server.call_tool()
   async def call_tool(name, arguments: dict) -> list[TextContent]:
       # 处理工具调用
   ```

4. **服务器运行**：
   ```python
   async with stdio_server() as (read_stream, write_stream):
       await server.run(read_stream, write_stream, options)
   ```

### 最佳实践

- 使用 Pydantic 模型验证输入参数
- 实现适当的错误处理和用户友好的错误消息
- 提供清晰的工具描述和参数说明
- 支持异步操作和适当的超时处理

## 许可证

MIT License - 详见 LICENSE 文件