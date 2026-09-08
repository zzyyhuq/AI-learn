import os
import sys
import json

from dotenv import load_dotenv
from openai import OpenAI
from pyexpat.errors import messages

# 解决 Windows 控制台 GBK 编码打印 emoji/中文报错
sys.stdout.reconfigure(encoding="utf-8")

# 从 .env 加载密钥和接口地址
load_dotenv()

# 创建 OpenAI client（从 .env 读取密钥）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)

examples_data = {
    "是": [
        ("公司ABC发布了季度财报，显示盈利增长。", "财报披露，公司ABC利润上升。"),
        ("公司ITCAST发布了年度财报，显示盈利大幅度增长。", "财报披露，公司ITCAST更赚钱了。")
    ],
    "不是": [
        ("黄金价格下跌，投资者抛售。", "外汇市场交易额创下新高。"),
        ("央行降息，刺激经济增长。", "新能源技术的创新。")
    ]
}

questions = [
    ("利率上升，影响房地产市场。", "高利率对房地产有一定的冲击。"),
    ("油价大幅度下跌，能源公司面临挑战。", "未来智能城市的建设趋势越加明显。"),
    ("股票市场今日大涨，投资者乐观。", "持续上涨的市场让投资者感到满意。")
]

messages = [
    {"role":"system","content":f"你帮我完成文本匹配，我给你两个句子，按[]包围，你判断他们是否匹配，回答是或不是，以下是案例"}
]

for key,value in examples_data.items():
    for t in value:
        messages.append({"role":"user","content":f"句子1[{t[0]}],句子2[{t[1]}]"})
        messages.append({"role": "assistant", "content": key})

for q in questions:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages+[{"role":"user","content":f"句子1[{q[0]}],句子2[{q[1]}]"}]
    )
    print(response.choices[0].message.content)