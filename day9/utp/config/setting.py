import os
import nnlog
mysql_info  = {
    'host':'118.24.3.40',
    'port':3306,
    'user':'litemall',
    'password':'litemall123456',
    'db':'litemall',
    'charset':'utf8',
}

email_info = {
    'host':'smtp.163.com',
    'user':'uitestp4p@163.com',
    'password':'houyafan123'
}

email_to = ['niuhanyang@163.com','2273747892@qq.com','243551032@qq.com','511402865@qq.com']
email_cc = ['1064393357@qq.com','382706058@qq.com']

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(base_path,'logs','utp.log')

log = nnlog.Logger(log_path)

email_template = '''
各位好：
    本次接口测试结果如下：总共运行{all_count}条用例，通过{pass_count}条，失败【{fail_count}】条。
    详细信息请查看附件。
'''
