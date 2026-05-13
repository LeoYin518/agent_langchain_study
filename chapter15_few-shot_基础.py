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

# Few-shot 模板
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="对以下句子进行情感分析，输出\"正面\"、\"负面\"或\"中性\"：",
    suffix="输入：{sentence}\n情感：",
    input_variables=["sentence"],
)

print(few_shot_prompt.format(sentence="客服态度很好，但是物流太慢了"))