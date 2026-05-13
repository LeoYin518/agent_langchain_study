from langchain_core.prompts import PromptTemplate

# 第一层：角色设定
character_template = PromptTemplate.from_template(
    "你是{company}的客服助手，名字叫{name}，{personality}。"
)

# 第二层：行为规范
behavior_template = PromptTemplate.from_template(
    """你需要遵守以下行为规范：
{behavior_rules}
"""
)

# 第三层：禁止事项
restriction_template = PromptTemplate.from_template(
    """你不能做以下事情：
{restrictions}
"""
)

# 最终模板
final_template = PromptTemplate.from_template(
    """
{character}

{behavior}

{restriction}
"""
)

# 第一步：先生成子 Prompt
character = character_template.format(
    company="航趣信息",
    name="小航",
    personality="专业、友善、耐心",
)

behavior = behavior_template.format(
    behavior_rules="""1. 先理解用户问题再回答
2. 回答不超过 200 字
3. 遇到投诉先致歉
"""
)

restriction = restriction_template.format(
    restrictions="""1. 不能承诺具体的赔偿金额
2. 不能评价竞争对手产品
3. 不能泄露公司内部信息
"""
)

# 第二步：组装最终 Prompt
final_prompt = final_template.format(
    character=character,
    behavior=behavior,
    restriction=restriction,
)

print(final_prompt)
