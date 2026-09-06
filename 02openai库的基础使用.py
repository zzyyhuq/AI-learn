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
        {"role":"system","content":"你是一个Python编程专家，并且不说废话"},
        {"role":"assistant","content":"你好，我是Python编程专家，并且不说废话，你要问什么"},
        {"role":"user","content":"为我输出1-10，使用Python代码"}
    ]
)

#3处理结果
print(response.choices[0].message.content)




