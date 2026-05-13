from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # 自动读取当前目录的 .env 文件


# 先定义数据结构
class CodeReview(BaseModel):
    issues: List[str] = Field(description="代码中发现的问题列表")
    suggestions: List[str] = Field(description="改进建议列表")
    score: int = Field(description="代码质量评分，1-10 分")


# 然后用 PydanticOutputParser 把它变成 Parser：
parser = PydanticOutputParser(pydantic_object=CodeReview)

prompt = PromptTemplate(
    template=(
        "你是一个代码审查专家，请审查以下代码并给出结构化反馈。\n"
        "{format_instructions}\n"
        "代码：\n{code}"
    ),
    input_variables=["code"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)
chain = prompt | llm | parser

result = chain.invoke({
    "code": "for i in range(len(lst)): print(lst[i])"
})

print(type(result))  # <class 'CodeReview'>
print(result.score)  # 6
# ['使用 range(len(lst)) 遍历列表不符合 Python 最佳实践，应直接迭代元素', '未处理 lst 可能为 None 或非可迭代对象的情况']
print(result.issues)
# ['改用 for item in lst: print(item)'...]
print(result.suggestions)
