import json

import flask
import tools


server = flask.Flask(__name__)

@server.route('/login')
def login():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')
    if not username or not password:
        data = {"code":-1,'msg':'不能为空'}
    else:
        # new_password = tools.md5(password)
        new_password =password
        sql = 'select id,username,passwd,error_count from app_myuser where username="%s";' % (username)
        result = tools.op_mysql(sql, False)
        if result:
            if result.get('error_count') > 5:
                data = {"code": -1, 'msg': '账号已经被锁定'}
            elif new_password == result.get('passwd'):
                up_sql = 'update app_myuser set error_count=0 where username="%s";' % username
                tools.op_mysql(up_sql)
                r = tools.get_redis()
                user_keys = r.keys('%s*'%username)
                if user_keys:
                    sessionid = user_keys[0].lstrip(username)
                else:
                    sessionid = tools.get_sessionid(username)
                    user_info = json.dumps({"user_id":result.get('id'),"username":username})
                    tools.my_redis(username+sessionid,user_info)
                data = {"code":0,"msg":"登录成功","session_id":sessionid}

            else:
                up_sql = 'update app_myuser set error_count=error_count+1 where username="%s";' % username
                tools.op_mysql(up_sql)
                data = {"code": -1, 'msg': '密码错误'}
        else:
            data = {"code": -1, 'msg': '用户不存在'}
    return json.dumps(data,ensure_ascii=False,indent=4)

@server.route('/pay')
def pay():
    sessionid = flask.request.values.get('sessionid')
    money = flask.request.values.get('money')
    if not sessionid or not money:
        data = {"code": -1, 'msg': '不能为空'}
    elif not tools.is_price(money):
        data = {"code": -1, 'msg': '不能为空'}
    else:
        r = tools.get_redis()
        sessionid_key = r.keys('*%s'%sessionid)
        if sessionid_key:
            sessionid = sessionid_key[0]
        else:
            return json.dumps({"code":-1,"msg":"请登录"})
        user_info = tools.my_redis(sessionid)
        if user_info:
            user_info = json.loads(user_info)
            user_id = user_info.get("user_id")
            sql='select balance from app_myuser where id=%s;'%user_id
            balance = tools.op_mysql(sql,False).get("balance")
            money = float(money)
            if balance>=money:
                # balance-=money
                update_sql = "update app_myuser set  balance = balance-%s where id = %s"%(money,user_id)
                print(update_sql)
                tools.op_mysql(update_sql)
                data = {"code":0,"msg":"支付成功"}
            else:
                data = {"code":0,"msg":"余额不足"}
        else:
            data = {"code":-1,"msg":"请登录"}
    return json.dumps(data,ensure_ascii=False,indent=4)


server.run(debug=True)