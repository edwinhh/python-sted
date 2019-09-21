# d =  {"name":"abc"}
import json
import pprint
# json_str = json.dumps(d) #就是把字典/list转成字符串（json）

# json_str2 = ' {"xiaohei":"123456","age":18}  '
# dic = json.loads(json_str2) #把字符串（json）转成 字典
# pprint.pprint(dic)

# pprint.pprint( json_str )
#json串就是字符串

d =  {
      "id": 314,
      "name": "矿泉水",
      "sex": "男",
      "age": 18,
      "addr": "北京市昌平区",
      "grade": "摩羯座",
      "phone": "18317155663",
      "gold": 405
    }

f = open('wjq.json','w',encoding='utf-8')
json.dump(d,f,ensure_ascii=False,indent=4)

f = open('wqz.json',encoding='utf-8')
dic = json.load(f)
print(dic)

# print(json.dumps(d,ensure_ascii=False))
# with open('users.json','w',encoding='utf-8') as f:
#     json_d = json.dumps(d,ensure_ascii=False,indent=8)
#     f.write(json_d)
#
#
# with open('users','r',encoding='utf-8') as f:
#     result = f.read()
#     d = json.loads(result)


