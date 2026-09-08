import math
import os
import sys

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

# text-embedding-v3 是阿里 DashScope(通义) 的向量模型
# 用阿里原生的 DashScopeEmbeddings（其底层走 dashscope SDK 原生接口，不是 OpenAI 兼容端点）
model = DashScopeEmbeddings(
    model="text-embedding-v3",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),   # 从 .env 读，绝不硬编码
)


print(model.embed_query("我喜欢你"))
print(model.embed_documents(["你好","你是谁","我是谁"]))
