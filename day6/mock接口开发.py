import flask
import json
import tools
#mock接口开发
 #1、模拟接口的意思
 #2、给别人提供数据
 #3、flask是一个web开发框架


server = flask.Flask(__name__)#把这个python文件当做一个服务

#

@server.route('/api/login',methods=['post','get'])
def login():
    username = flask.request.values.get('username')#从请求里面获取到参数的
    password = flask.request.values.get('password')

    # flask.request.is_json#是否请求为json
    # flask.request.json.get('')#入参是json的话，用这个

    d = {'error_code':1,'msg':'登录成功','username':username,'password':password}
    return json.dumps(d,ensure_ascii=False)

@server.route('/api/pay',methods=['post','get'])
def pay():
    d = {'error_code':1,'msg':'支付成功'}
    return json.dumps(d,ensure_ascii=False)


@server.route('/api/get_bill')
def get_bill():
    table_list  = ['app_myuser','czm']
    table_name = flask.request.values.get('table_name')
    limit = flask.request.values.get('limit',50)
    if table_name and table_name in table_list:
        sql = 'select id,username,passwd from %s limit %s' % (table_name,limit)
        result = tools.op_mysql(sql)
        data = {'error_code':0,'msg':'成功','data':result}
    else:
        data = {'error_code':-1,'msg':'没有权限查询该表'}
    return json.dumps(data, ensure_ascii=False)


server.run(host='0.0.0.0',port=8000,debug=True)

#127.0.0.1:8000/api/login

#1、写一个程序，输入qq群号码，把每个群成员的头像下载下来，保存到本地，图片名字取群昵称，如果没有群昵称，取qq名字

#2、登录接口 login
    #username password
    #登陆成功，产生 seesionid,  1102a245b59af9c783bb8c18948ef96d# username+当前时间戳+salt
    #seesionid 存到redis里面，user_seesions: {
#               1102a245b59af9c783bb8c18948ef96d:{"user_name":"wyj","userid":1}
#               1102a245b59af9c783bb8c18948ef16d:{"user_name":"wqz","userid":1}
#               }，key的失效时间

#2、支付接口，支付需要登录
    #post请求，参数：seesionId，money
    #表字段
    #user  id username password balance
    #1、session不正确，提示请登录
    #2、校验money的类型
    #3、balance必须大于等于money才可以支付

    
    
