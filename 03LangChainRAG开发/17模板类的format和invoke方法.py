from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate


template = PromptTemplate.from_template("我的邻居是{lastname}，他的爱好是{hobby}")
res = template.format(lastname="张三",hobby="打篮球")
print(res,type(res))


res2 = template.invoke({"lastname":"张三","hobby":"打篮球"})
print(res2,type(res2))