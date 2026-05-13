import inspect
from langchain_core.prompts import StringPromptTemplate

TEMPLATE = """你是一个资深程序员，请分析以下函数并给出说明：

函数名：{function_name}
源代码：
{source_code}

请说明：
1. 这个函数的功能
2. 参数的含义
3. 潜在的问题或改进点"""


class FunctionAnalysisPrompt(StringPromptTemplate):
    """自动读取函数源码并注入 Prompt 的模板"""

    def format(self, **kwargs) -> str:
        func = kwargs["function"]
        # 自动获取函数源码
        source_code = inspect.getsource(func)
        return TEMPLATE.format(
            function_name=func.__name__,
            source_code=source_code,
        )


# 使用示例
def calculate_discount(price: float, discount_rate: float) -> float:
    if discount_rate > 1:
        discount_rate = discount_rate / 100
    return price * (1 - discount_rate)


prompt = FunctionAnalysisPrompt(input_variables=["function"])
print(prompt.format(function=calculate_discount))
