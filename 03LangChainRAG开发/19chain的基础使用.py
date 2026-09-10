import sys

from dashscope import model
from dotenv import load_dotenv
from xml.etree.ElementTree import tostring

from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain_core.runnables import history, RunnableSerializable

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
    ("ai","床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human","好诗，再来一首"),
(   "ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦")
]
model = ChatDeepSeek(model="deepseek-chat")
chain: RunnableSerializable=chat_prompt_template | model
res = chain.invoke({"history":history_data})
print(res.content)

res2 = chain.stream({"history":history_data})
for chunk in res2:
    print(chunk.content,end="",flush=True)