# MCP Fetch Example - 项目概述

这是一个完整的 Python MCP SDK 示例项目，展示了如何构建一个 Model Context Protocol 服务器。

## 🎯 项目目标

这个示例项目展示了：
- 如何使用 Python MCP SDK 构建 MCP 服务器
- 如何定义和实现自定义工具
- 如何处理输入参数验证
- 如何配置和部署 MCP 服务器
- 如何进行开发和调试

## 📁 项目结构

```
example/
├── src/mcp_fetch/           # 核心源代码
│   ├── __init__.py         # 入口点和命令行处理
│   ├── __main__.py         # 模块执行入口
│   └── server.py           # MCP 服务器实现
├── demo.py                 # 演示脚本
├── claude_desktop_config.json  # Claude Desktop 配置示例
├── pyproject.toml          # 项目配置
├── README.md              # 详细文档
├── LICENSE                # MIT 许可证
└── .gitignore            # Git 忽略配置
```

## 🚀 快速开始

### 1. 环境设置
```bash
cd example
uv sync
```

### 2. 运行演示
```bash
uv run python demo.py
```

### 3. 测试服务器
```bash
uv run python -m mcp_fetch --help
```

### 4. 使用 MCP Inspector 调试
```bash
npx @modelcontextprotocol/inspector uv run python -m mcp_fetch
```

## 🛠️ 核心组件

### server.py
- 实现了 MCP 服务器的核心逻辑
- 定义了 `fetch` 工具
- 处理网页内容获取和转换
- 展示了错误处理和参数验证

### __init__.py
- 提供命令行接口
- 解析命令行参数
- 启动异步服务器

### pyproject.toml
- 项目元数据和依赖
- 构建配置
- 入口点定义

## 📚 学习要点

1. **MCP 服务器结构**：了解如何组织 MCP 服务器代码
2. **工具定义**：学习如何定义和实现自定义工具
3. **参数验证**：使用 Pydantic 模型进行输入验证
4. **错误处理**：实现适当的错误处理机制
5. **异步编程**：使用 asyncio 处理异步操作

## 🔧 扩展指南

基于这个示例，你可以：
- 添加更多工具
- 实现不同的数据处理逻辑
- 添加认证和授权
- 集成其他服务和 API
- 实现缓存和持久化

## 📖 相关资源

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Desktop 配置](https://docs.anthropic.com/claude/docs/mcp)

这个示例项目提供了一个完整的起点，帮助你理解和构建自己的 MCP 服务器。