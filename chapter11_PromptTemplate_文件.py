# from langchain_core.prompts import load_prompt
#
# prompt = load_prompt(path="prompts/code_review.yaml", encoding="utf-8")
# print(prompt.format(language="Python", code="x = 1; y = 2; print(x+y)"))

import yaml
from langchain_core.prompts import PromptTemplate

with open(
        "./prompts/code_review.yaml",
        "r",
        encoding="utf-8"
) as f:
    config = yaml.safe_load(f)

prompt = PromptTemplate(
    input_variables=config["input_variables"],
    template=config["template"]
)

print(prompt.format(
    language="Python",
    code="print('hello')"
))
