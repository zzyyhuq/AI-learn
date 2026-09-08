import json

d = {
    "name":"周杰伦",
    "age":18,
    "gender":"男"
}
s = json.dumps(d,ensure_ascii=False)
print(s)



json_str = '{"name":"周杰伦","age":18,"gender":"男"}'
print(json.loads(json_str))