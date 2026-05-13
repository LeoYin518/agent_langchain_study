from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # 自动读取当前目录的 .env 文件

llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)
response = llm.invoke("介绍一下你自己")

print(response.content)
