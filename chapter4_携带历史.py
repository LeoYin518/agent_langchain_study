from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()  # 自动读取当前目录的 .env 文件
llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)

messages = [
    SystemMessage(content="你是一个 Python 专家。"),
    HumanMessage(content="什么是列表推导式？"),
    AIMessage(content="列表推导式是 Python 中创建列表的简洁语法，例如 [x*2 for x in range(10)]。"),
    HumanMessage(content="它比普通 for 循环快吗？"),
]

response = llm.invoke(messages)
print(response.content)
