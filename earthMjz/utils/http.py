import requests


class MyRequest:
    def __init__(self, url, method, query_params=None, data=None, is_json=False, **kwargs):
        self.url = url
        self.data = data
        self.query_params = query_params
        self.kwargs = kwargs
        self.is_json = is_json
        getattr(self, method.lower())()

    def post(self):
        data_key = 'json' if self.is_json else 'data'
        post_dic = {'url': self.url, 'params': self.query_params, data_key: self.data}
        post_dic.update(self.kwargs)
        try:
            results = requests.post(**post_dic, verify=False).json()
        except Exception as e:
            print('请求接口出错，%s,%s' % (self.url, e))
            self.results = {'msg': '请求接口出错，%s,%s' % (self.url, e)}
        else:
            self.results = results

    def get(self):
        try:
            self.query_params = self.data
            results = requests.get(self.url, params=self.query_params, **self.kwargs, verify=False).json()
        except Exception as e:
            print('请求接口出错，%s,%s' % (self.url, e))
            self.results = {'msg': '请求接口出错，%s,%s' % (self.url, e)}
        else:
            self.results = results

    def put(self):
        try:
            self.query_params = self.data
            results = requests.put(self.url, data=self.data, params=self.query_params, **self.kwargs,
                                   verify=False).json()
        except Exception as e:
            print('请求接口出错，%s,%s' % (self.url, e))
            self.results = {'msg': '请求接口出错，%s,%s' % (self.url, e)}
        else:
            self.results = results

    def delete(self):
        try:
            self.query_params = self.data
            results = requests.delete(self.url, params=self.query_params, **self.kwargs, verify=False).json()
        except Exception as e:
            print('请求接口出错，%s,%s' % (self.url, e))
            self.results = {'msg': '请求接口出错，%s,%s' % (self.url, e)}
        else:
            self.results = results
