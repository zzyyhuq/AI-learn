import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()

#1获取client对象，openai对象
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),

)

#2调用模型
response = client.chat.completions.create(
    model = "deepseek-chat",
    messages=[
        {"role":"system","content":"你是一个Python编程专家，并且话非常多"},
        {"role":"assistant","content":"你好，我是Python编程专家，并且话非常多，你要问什么"},
        {"role":"user","content":"为我输出1-10，使用Python代码"}
    ],
    stream=True #开启了流式输出的功能
)

#3处理结果
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",
        flush=True #立刻刷新缓冲区
    )
