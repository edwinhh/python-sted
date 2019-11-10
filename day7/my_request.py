import requests
#反射
class MyRequest:
    def __init__(self,url,method='get',data=None,headers=None,is_json=False):
        method = method.lower()
        self.url = url
        self.data = data
        self.headers = headers
        self.is_json = is_json
        if hasattr(self,method):
            getattr(self,method)()

    def get(self):
        try:
            req = requests.get(self.url,self.data,headers=self.headers).json()
        except Exception as e:
            self.response = {"error":"接口请求出错%s"%e}
        else:
            self.response = req

    def post(self):
        try:
            if self.is_json:
                req = requests.post(self.url, json=self.data, headers=self.headers).json()
            else:
                req = requests.post(self.url, self.data, headers=self.headers).json()
        except Exception as e:
            self.response  = {"error":"接口请求出错%s"%e}
        else:
            self.response = req


if __name__ == '__main__':
    import jsonpath
    login = MyRequest('http://127.0.0.1:5000/login1',data={'username':'chenjie','password':'123456'})
    # sessionid = login.response.get('session_id')
    result = jsonpath.jsonpath(login.response,'$..session_id')
    if result:
        print('登录成功')
    else:
        print('登录失败')
    print(login.response)



    # data = {'sessionid':sessionid,'money':10000}
    # m = MyRequest('http://127.0.0.1:5000/pay',data=data)
    # print(m.response)
