from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 自动读取当前目录的 .env 文件

client = OpenAI()

response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role": "user", "content": "介绍一下你自己"}
    ]
)

print(response.choices[0].message.content)
