from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# 定义示例
examples = [
    {"input": "今天天气真好", "output": "正面"},
    {"input": "这个产品太差了", "output": "负面"},
    {"input": "还行吧，一般般", "output": "中性"},
]

# 单个示例的格式
example_prompt = PromptTemplate.from_template(
    "输入：{input}\n情感：{output}"
)

for example in examples:
    formatted = example_prompt.format(**example)

    print(formatted)
    print("格式化后长度：", len(formatted))
    print("------")

selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50,  # 格式化后的最大字符数
)

dynamic_prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=example_prompt,
    prefix="对以下句子进行情感分析，输出\"正面\"、\"负面\"或\"中性\"：",
    suffix="输入：{sentence}\n情感：",
    input_variables=["sentence"],
)
print("*" * 25)
print(dynamic_prompt.format(sentence="客服态度很好，但是产品太贵了"))
