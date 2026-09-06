import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错的问题
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 文件加载配置（DEEPSEEK_API_KEY / DEEPSEEK_BASE_URL）
load_dotenv()

client = OpenAI(
    api_key = os.getenv("DEEPSEEK_API_KEY"),        # 在 DeepSeek 开放平台申请，存于 .env
    base_url = os.getenv("DEEPSEEK_BASE_URL")        # DeepSeek 接口地址
)

res = client.chat.completions.create(
    model = "deepseek-chat",   #对话模型；推理模型填 deepseek‑reasoner
    messages = [
        {"role":"user","content":"你现在具备推理能力吗，你用的是deepseek-v4-flash的模型吗"}
    ]
)
print(res.choices[0].message.content)