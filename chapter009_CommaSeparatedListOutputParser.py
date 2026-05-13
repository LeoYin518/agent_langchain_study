from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # 自动读取当前目录的 .env 文件

parser = CommaSeparatedListOutputParser()

prompt = PromptTemplate(
    template="列出 5 个{subject}。\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | ChatOpenAI(model="qwen3.6-plus", temperature=0) | parser

result = chain.invoke({"subject": "Python 常用的内置函数"})
print(result)
