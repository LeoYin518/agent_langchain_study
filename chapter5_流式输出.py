from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # 自动读取当前目录的 .env 文件
llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)

prompt = ChatPromptTemplate.from_template("用 500 字介绍{topic}")
chain = prompt | llm | StrOutputParser()

for chunk in chain.stream({"topic": "量子计算"}):
    print(chunk, end="", flush=True)
