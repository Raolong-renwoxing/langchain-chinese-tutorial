import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

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


# 定义工具
@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气"""
    weather_data = {
        "北京": "晴，25°C",
        "上海": "多云，28°C",
        "广州": "雨，26°C",
        "深圳": "晴，29°C",
    }
    return weather_data.get(city, "抱歉，暂未收录该城市天气信息")


# 创建一个 agent
# system_prompt 系统提示词
# tools 实用工具
graph = create_agent(
    model,
    system_prompt="你是一个天气助手，只回复天气查询相关问题，如果不是，直接告诉用户'无可奉告'",
    tools=[get_weather]
)
