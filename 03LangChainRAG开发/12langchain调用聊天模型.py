import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_deepseek import ChatDeepSeek

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()

# 创建聊天模型（会自动读取 .env 里的 DEEPSEEK_API_KEY）
model = ChatDeepSeek(model="deepseek-chat")

messages = [
    SystemMessage(content="你是一个唐代诗人"),
    HumanMessage(content="为我写一首诗"),
    AIMessage(content="床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    HumanMessage(content="你刚才的回答是什么，就是上一句的回答"),
]

res = model.stream(messages)


for chunk in res:
    print(chunk.content,end="",flush=True)