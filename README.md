# LangChain 中文教程

一个基于 LangChain 的中文教程项目，涵盖从基础概念到高级 Agent 开发的完整学习路径。

## 环境准备

### 1. 安装依赖

```bash
pip install langchain langchain-openai python-dotenv langchain-mcp-adapters deepagents
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env`，并填入你的 API Key：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
API_KEY=your_api_key_here
```

本项目使用 SiliconFlow API，你也可以根据需要修改 `00-overview.py` 等文件中的 `URL` 和 `MODEL` 配置。

## 教程内容

### [00-overview.py](00-overview.py) - LangChain 基础概述

介绍 LangChain 的基本概念和模型调用方式。

```bash
python 00-overview.py
```

### [01-agent.py](01-agent.py) - Agent 与工具

学习如何创建 Agent 并为其绑定工具，实现自定义功能。

```bash
python 01-agent.py
```

### [02-mcp.py](02-mcp.py) - MCP 集成

通过 Model Context Protocol (MCP) 集成外部服务，实现 12306 火车票查询功能。

```bash
python 02-mcp.py
```

### [03-deepAgents.py](03-deepAgents.py) - 深度 Agent 开发

使用 deepagents 框架创建具有文件系统访问能力的深度 Agent，支持多轮对话记忆。

```bash
python 03-deepAgents.py
```

## 项目结构

```
.
├── .env.example      # 环境变量模板
├── .gitignore        # Git 忽略配置
├── 00-overview.py    # LangChain 基础
├── 01-agent.py       # Agent 与工具
├── 02-mcp.py         # MCP 集成
├── 03-deepAgents.py  # 深度 Agent
└── rules.md          # Agent 规则配置
```

## 依赖说明

| 依赖包 | 说明 |
|--------|------|
| `langchain` | LangChain 核心库 |
| `langchain-openai` | OpenAI 兼容模型集成 |
| `python-dotenv` | 环境变量管理 |
| `langchain-mcp-adapters` | MCP 协议适配器 |
| `deepagents` | 深度 Agent 框架 |

## 注意事项

- 请勿在代码中硬编码 API Key，使用环境变量管理
- `rules.md` 定义了 Agent 的行为规则，03-deepAgents.py 会读取该文件
