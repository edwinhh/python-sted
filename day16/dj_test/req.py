import requests

url = 'http://127.0.0.1:8000/testcase/case_set_new'

result = requests.put(url,data={'id':1,'name':'requests模块测试'})

print(result.json())