import sys

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek


# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()

prompt_template = PromptTemplate.from_template(
    "我的邻居性{lastname}，生了一个性别为{gender},请你帮他们取一个名字，简单回答"
)

model = ChatDeepSeek(model="deepseek-chat")

#调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张",gender="女")
# model = ChatDeepSeek(model="deepseek-chat")
# res = model.invoke(prompt_text)

chain = prompt_template | model
res = chain.invoke(input = {"lastname": "张", "gender": "女儿"})
print(res.content)