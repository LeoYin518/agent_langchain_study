from langchain_core.prompts import PromptTemplate

# 方式一：from_template（推荐，简洁）
prompt = PromptTemplate.from_template(
    "你是一个{role}，请用{style}的风格回答：{question}"
)

print(prompt.format(
    role="Python 专家",
    style="简洁",
    question="什么是装饰器？"
))
# 你是一个Python 专家，请用简洁的风格回答：什么是装饰器？

# 方式二：构造函数（需要显式声明变量）
prompt = PromptTemplate(
    input_variables=["role", "style", "question"],
    template="你是一个{role}，请用{style}的风格回答：{question}"
)

print(prompt.format(
    role="情感专家",
    style="共情",
    question="与男朋友分手很难过"
))
# 你是一个情感专家，请用共情的风格回答：与男朋友分手很难过
