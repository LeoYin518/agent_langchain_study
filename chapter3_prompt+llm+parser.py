from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import BaseOutputParser

load_dotenv()  # 自动读取当前目录的 .env 文件


class NameListParser(BaseOutputParser):
    """把逗号分隔的名字字符串解析成列表"""

    def parse(self, text: str) -> list:
        return [name.strip() for name in text.strip().split("，")]


prompt = PromptTemplate.from_template(
    "你是一个起名大师，请模仿示例为{country}的{gender}孩子起3个名字。"
    "示例男孩名：{boy_example}，示例女孩名：{girl_example}。"
    "只返回名字，用逗号分隔。"
)

llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)
parser = NameListParser()

# 用 | 把三个组件串起来
chain = prompt | llm | parser

# 一行调用
result = chain.invoke({
    "country": "日本",
    "gender": "女",
    "boy_example": "太郎",
    "girl_example": "花子"
})

print(result)
