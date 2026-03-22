import asyncio
import os
from pathlib import Path

from deepagents import create_deep_agent
from deepagents.backends import LocalShellBackend
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver

# 加载 .env 环境变量
load_dotenv()

# 配置模型需要的参数配置
URL = "http://api.siliconflow.cn/v1"
MODEL = "Pro/MiniMaxAI/MiniMax-M2.5"
API_KEY = os.getenv("API_KEY")

# https://docs.langchain.com/oss/python/integrations/chat 模型调用文档
# 初始化模型
model = ChatOpenAI(
    model=MODEL,
    api_key=API_KEY,
    base_url=URL
)


def get_work_dir():
    return Path(__file__).resolve().parent


SYSTEM_PROMPT = """你是一个运行在 Windows 系统上的 AI 助手。

重要约束：
1. 当执行 Python 脚本或命令时，必须使用完整的 Windows 绝对路径（如 `F:\\sun-liang\\langchain-chinese-tutorial\\...`），不能使用 Unix 风格路径（如 `/skills/...`）
2. 当前工作目录是 `F:\\sun-liang\\langchain-chinese-tutorial`
3. 执行后台任务时必须使用 `blocking: false` 使其不阻塞
"""


async def main():
    # 要用 deepagents，必须要设置 checkpointer
    checkpointer = MemorySaver()

    agent = create_deep_agent(
        model=model,
        skills=["/skills/background-timer/", "/skills/video-downloader/"],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
        backend=LocalShellBackend(
            root_dir=".",
            virtual_mode=True,
            inherit_env=True  # 可选：继承当前系统的环境变量，方便执行 npm/pip 等命令
        )
    )
    input_data = {
        "messages": [
            {
                "role": "user",
                "content": "下载B站视频，地址 https://www.bilibili.com/video/BV1oaULB4E2U/",
            }
        ]
    }

    async for chunk in agent.astream(
            input_data,  # type: ignore
            stream_mode="updates",  # type: ignore
            subgraphs=True,  # type: ignore
            version="v2",  # type: ignore
            config={"configurable": {"thread_id": "12345"}},  # type: ignore
    ):
        if chunk["type"] == "updates":
            if chunk["ns"]:
                # Subagent event - namespace identifies the source
                print(f"[subagent: {chunk['ns']}]")
            else:
                # Main agent event
                print("[main agent]")
            print(chunk["data"])
