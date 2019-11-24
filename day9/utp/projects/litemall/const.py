import os
host = 'http://proxy.nnzhp.cn'

test_user = {
    'username':'user123',
    'password':'user123'
}#测试用户

test_admin_user = {
    'username':'admin123',
    'password':'admin123'
}#测试用户

base_path = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(base_path,'data') #存测试数据的目录
report_path = os.path.join(base_path,'report') #存报告的目录
case_path = os.path.join(base_path,'cases') #存测试用例的目录