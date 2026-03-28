# 结构化输出 (Structured Output)

在某些场景下，你可能希望 Agent 以特定的格式返回输出。LangChain 通过 `response_format` 参数提供结构化输出策略。

## ToolStrategy

`ToolStrategy` 使用人工工具调用来生成结构化输出。这适用于任何支持工具调用的模型。当 `ProviderStrategy`（提供商原生结构化输出）不可用或不可靠时，应使用 `ToolStrategy`。

```python
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


class ContactInfo(BaseModel):
    name: str
    email: str
    phone: str

agent = create_agent(
    model="gpt-4.1-mini",
    tools=[search_tool],
    response_format=ToolStrategy(ContactInfo)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

result["structured_response"]
# ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')
```

## ProviderStrategy

`ProviderStrategy` 使用模型提供商的原生结构化输出生成。这更可靠，但仅适用于支持原生结构化输出的提供商：

```python
from langchain.agents.structured_output import ProviderStrategy

agent = create_agent(
    model="gpt-4.1",
    response_format=ProviderStrategy(ContactInfo)
)
```