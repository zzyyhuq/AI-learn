import sys

from dashscope import model
from dotenv import load_dotenv
from xml.etree.ElementTree import tostring

from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain_core.runnables import history

from langchain_deepseek import ChatDeepSeek
from pydantic_core.core_schema import none_schema

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人，可以做诗"),
        MessagesPlaceholder("history"),
        ("human","再来一首唐诗"),
    ]
)


history_data=[
    ("human","你来写一个唐诗"),
    ("ai","床前明月光，疑是地上霜，举头望明月，低头思故乡")
]

prompt_text = chat_prompt_template.invoke({"history":history_data}).to_string()
print(prompt_text)

model = ChatDeepSeek(model="deepseek-chat")
res = model.invoke(prompt_text)
print(res.content)