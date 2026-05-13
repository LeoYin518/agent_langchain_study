from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # 自动读取当前目录的 .env 文件

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

selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,
    # DashScope / OpenAI 兼容接口不支持 LangChain 默认的 token 数组输入，
    # 关闭上下文长度检查后会直接发送 str/list[str]，避免 input.contents 参数错误。
    embeddings=OpenAIEmbeddings(model="text-embedding-v3", check_embedding_ctx_length=False),
    vectorstore_cls=Chroma,
    k=2,  # 选最相似的 2 个例子
)

# 测试：输入一个情绪相关的句子
selected = selector.select_examples({"input": "这次购物体验糟透了"})
print(selected)
# 会选出负面情感相关的例子
