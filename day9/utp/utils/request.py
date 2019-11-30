import requests
from config.setting import log
#反射
class MyRequest:
    def __init__(self,url,data=None,method='get',headers=None,is_json=True):
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
        #print(self.response)
        log.info(self.response)

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

