# coding=utf-8
from tools.my_request import MyRequest
data = {'title':"122",
        'desc':"desc",
        'method':0,
        'url':'http://127.0.0.1:8000/testcase/case',
        'params':"{'sessionid':sessionid,'money':10000}"
        }


m = MyRequest('http://127.0.0.1:8000/testcase/case',method='post',data=data)
print(m.response)
