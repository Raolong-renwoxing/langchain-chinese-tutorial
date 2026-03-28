import os
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.structured_output import ProviderStrategy

load_dotenv()

URL = "http://api.siliconflow.cn/v1"
MODEL = "deepseek-ai/DeepSeek-V3.2"
API_KEY = os.getenv("API_KEY")

model = ChatOpenAI(
    model=MODEL,
    api_key=API_KEY,
    base_url=URL
)


class WeatherResponse(BaseModel):
    city: str = Field(description="城市名称")
    temperature: str = Field(description="温度")
    condition: str = Field(description="天气状况")
    humidity: str = Field(description="湿度")


class WeatherQueryResult(BaseModel):
    query: str = Field(description="原始查询内容")
    result: WeatherResponse = Field(description="天气查询结果")
    success: bool = Field(description="查询是否成功")


@tool
def query_weather(city: str) -> str:
    """查询指定城市的天气信息，返回结构化数据"""
    weather_data = {
        "北京": {"temperature": "25°C", "condition": "晴", "humidity": "45%"},
        "上海": {"temperature": "28°C", "condition": "多云", "humidity": "60%"},
        "广州": {"temperature": "26°C", "condition": "雨", "humidity": "80%"},
        "深圳": {"temperature": "29°C", "condition": "晴", "humidity": "50%"},
    }
    if city in weather_data:
        data = weather_data[city]
        return f"{city}|{data['temperature']}|{data['condition']}|{data['humidity']}"
    return f"{city}|未知|未知|未知"


agent = create_agent(
    model,
    system_prompt="你是一个天气助手。当用户询问天气时，使用 query_weather 工具查询，然后以 JSON 格式返回结果。",
    tools=[query_weather],
    response_format=ProviderStrategy(WeatherQueryResult)
)

user_input = {"messages": [{"role": "user", "content": "北京今天的天气怎么样？"}]}
result = agent.invoke(user_input)
res = result['structured_response'] # type: WeatherQueryResult
print(res.model_dump_json())