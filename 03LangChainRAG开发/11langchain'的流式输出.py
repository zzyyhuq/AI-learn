import os
import sys

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()


# deepseek‑chat 是通用对话模型；deepseek‑reasoner 是深度思考模型
model = ChatDeepSeek(model="deepseek-chat")

# invoke传参注意：ChatDeepSeek不使用input=xxx，直接传入字符串
res = model.stream("你是谁呀能做什么？")

# 输出要用 .content 获取文本内容
for chunk in res:
    print(chunk.content, end="", flush=True)
