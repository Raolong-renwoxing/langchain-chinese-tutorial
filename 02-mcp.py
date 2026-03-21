# pip install langchain-mcp-adapters
import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

# 加载 .env 环境变量
load_dotenv()

# 配置模型需要的参数配置
URL = "http://api.siliconflow.cn/v1"
MODEL = "deepseek-ai/DeepSeek-V3.2"
API_KEY = os.getenv("API_KEY")


async def main():
    # https://docs.langchain.com/oss/python/integrations/chat 模型调用文档
    # 初始化模型
    model = ChatOpenAI(
        model=MODEL,
        api_key=API_KEY,
        base_url=URL
    )

    # 加载 mcp
    client = MultiServerMCPClient(
        {
            "12306-mcp": {
                "transport": "http",
                "url": "https://mcp.api-inference.modelscope.net/dcbef67d48d44b/mcp"
            }
        }
    )

    tools = await client.get_tools()

    # 创建一个 agent
    # system_prompt 系统提示词
    agent = create_agent(
        model,
        system_prompt="基于 Model Context Protocol (MCP) 的12306购票搜索服务器。提供了简单的API接口，允许大模型利用接口搜索12306购票信息。",
        tools=tools
    )

    input_data = {"messages": [{"role": "user", "content": "武汉到上海火车票，今天的"}]}

    result = await agent.ainvoke(
        input_data  # type:ignore
    )

    print(result["messages"])


if __name__ == "__main__":
    asyncio.run(main())
