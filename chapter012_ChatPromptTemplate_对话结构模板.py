from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的{domain}顾问，回答简洁准确。"),
    ("human", "你好，我有个问题想请教。"),
    ("ai", "你好！请说，我来帮你解答。"),
    ("human", "{question}"),
])

messages = chat_prompt.format_messages(
    domain="法律",
    question="合同违约需要赔偿哪些损失？"
)

for msg in messages:
    print(f"{msg.type}: {msg.content}")
