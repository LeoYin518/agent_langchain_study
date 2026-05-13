from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # 自动读取当前目录的 .env 文件
llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)

prompt = ChatPromptTemplate.from_template("用 500 字介绍{topic}")
chain = prompt | llm | StrOutputParser()

questions = [
    {"topic": "机器学习"},
    {"topic": "深度学习"},
    {"topic": "强化学习"},
]

results = chain.batch(questions)
# results = chain.batch(questions, config={"max_concurrency": 3})
for r in results:
    print(r[:50])  # 只打印前 50 个字
