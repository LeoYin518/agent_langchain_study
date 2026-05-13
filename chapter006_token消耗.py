from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
from dotenv import load_dotenv

load_dotenv()  # 自动读取当前目录的 .env 文件

llm = ChatOpenAI(model="qwen3.6-plus", temperature=0)

with get_openai_callback() as cb:
    response = llm.invoke("用三句话介绍一下量子力学")
    print(response.content)
    print("---")
    print(f"输入 Token：{cb.prompt_tokens}")
    print(f"输出 Token：{cb.completion_tokens}")
    print(f"总 Token：{cb.total_tokens}")
    print(f"费用：${cb.total_cost:.6f}")
