import jsonpath

seqs = ['!=', '>=', '<=', '=', '>', '<', ]  # 支持的比较运算符


class ResponseCheck:

    def __init__(self, check: str, response: dict):
        self.check = check
        self.response = response
        self.process_check_str()
        self.check_res()

    def process_check_str(self):
        # 函数是处理检查点的，提取到检查点的key
        check_list_res = []  # 存放提取了key、vuale之后的list
        check_list = self.check.split(',')
        for check in check_list:
            check_list_res.append(self.get_kv(check))

        self.check_list_res = check_list_res

    def get_kv(self, check_str):
        for seq in seqs:  # 循环比较运算符
            if seq in check_str:  # 如果运算符在里面的话，就按照这个运算符分隔
                key, value = check_str.split(seq)  # 取到key和vlaue
                return [key, seq, value]  # 返回key，value和运算符

    def check_res(self):
        for check_list in self.check_list_res:
            if check_list:
                key, seq, value = check_list
                real_value = self.get_response_value(key, self.response)
                self.reason = '%s和预期结果不一致，预期结果【%s】，' \
                              '实际结果【%s】,运算符【%s】' % (key, value, real_value, seq)
                if real_value == '空':
                    self.status = 999
                    return '失败'
                seq = '==' if seq == '=' else seq  # 判断如果是=的话，改成==
                code = '%s %s %s' % (self.convert_type(real_value), seq, self.convert_type(value))  # 生成比较实际结果和语气结果的代码
                status = eval(code)  # 用eval来执行生成代码，获取到执行的结果
                if not status:
                    self.status = 999
                    return '失败'  # 如果有一个判断失败了，那么就返回失败
            else:
                self.status = 999
                self.reason = '校验点写法出错'
                return '校验点写法出错'

        self.status = 1
        self.reason = '验证通过'

    def convert_type(self, s):
        try:
            s = float(s)
        except:
            s = ' "%s" ' % s
        return s

    @staticmethod
    def get_response_value(key, response):
        '''根据传入的key从实际结果里面取到value'''
        jsonpath_str = '$..%s' % key
        value = jsonpath.jsonpath(response, jsonpath_str)
        if value:
            return value[0]  # 因为jsonopath返回的是一个list，所以取第一个元素
        return '空'
