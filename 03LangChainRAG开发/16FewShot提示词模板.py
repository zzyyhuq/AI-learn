import sys
from sys import prefix

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_deepseek import ChatDeepSeek
from pydantic_core.core_schema import none_schema

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()

#示例模板
example_template = PromptTemplate.from_template("单词：{word}，反义词：{antonym}")

#示例的动态数据注入
example_data = [
    {"word":"大","antonym":"小"},
    {"word":"上","antonym":"下"}
]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,    #示例模板
    examples=example_data,              #示例数据(list里面套字典)
    prefix="告知我单词的反义词，我提供如下示例",      #示例之前的提示词
    suffix="基于前面的示例，告诉我{input_word}的反义词是什么",    #示例之后的提示词
    input_variables=["inout_word"]         #表明在前缀或后缀中需要注入的变量名
)

few_text = few_shot_template.invoke(input = {"input_word":"左"}).to_string()
print(few_text)
model = ChatDeepSeek(model="deepseek-chat")
res = model.invoke(few_text)
print(res.content)