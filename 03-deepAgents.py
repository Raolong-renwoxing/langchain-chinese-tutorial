# pip install -qU deepagents
import os

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver

# 加载 .env 环境变量
load_dotenv()

# 配置模型需要的参数配置
URL = "http://api.siliconflow.cn/v1"
MODEL = "deepseek-ai/DeepSeek-V3.2"
API_KEY = os.getenv("API_KEY")

# https://docs.langchain.com/oss/python/integrations/chat 模型调用文档
# 初始化模型
model = ChatOpenAI(
    model=MODEL,
    api_key=API_KEY,
    base_url=URL
)

# 必须加这个 检查点
checkpointer = MemorySaver()

with open("rules.md", "r",encoding="utf8") as fp:
    content = fp.read()
    system_prompt = f"""你是一个桌面助手，遵循以下规则执行任务：{content}"""

agent = create_deep_agent(
    model=model,
    checkpointer=checkpointer,
    system_prompt=system_prompt,
    backend=FilesystemBackend(root_dir=".", virtual_mode=True)
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "`.env` 内容是什么？"}]},
    config={"configurable": {"thread_id": "main"}}
)

print(response)
