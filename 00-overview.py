import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

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

# 调用模型
response = model.invoke("什么是langchian?")
# 打印模型的响应
print(response.content)