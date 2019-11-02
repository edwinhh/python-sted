import flask
from flask import request
import json,requests
import tools,time

#1
# def qq_check(qq):
#     url=""
#     data = {'gc':613536708,'bkn':240397961,'st':0,'end':40}
#     headers = {'cookie':'pgv_pvi=6636933120; RK=gRZhhBpNbS; ptcz=14bab564718e3e1048a09cc0e18a23f7c51f20d5b93da610cc1427f51f63a2f8; pgv_pvid=4990195883; ts_uid=5190463916; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin; uin=o0511402865; skey=@LUFPqSBxO; ptisp=cnc; pgv_info=ssid=s5139002932; ts_last=qun.qq.com/member.html; pgv_si=s4695831552; p_uin=o0511402865; pt4_token=m-08apoc2xJxW51Ahx*LKfuD4UyR2WEUd6PWyQ1PB8s_; p_skey=1whnzxqbI2kEJ7IEYgnr6wzrBRo8BY6dhPg57tD7ZBs_;'}
#     r = requests.post(url,data=data,verify=False,headers=headers )
#     print(r.json())


#2,3

server = flask.Flask(__name__)#把这个python文件当做一个服务

#

@server.route('/api/login',methods=['post','get'])
def login():
    username = flask.request.values.get('username')#从请求里面获取到参数的
    password = flask.request.values.get('password')
    tick=time.time()
    t=username+str(tick)
    sessionid=tools.md5(t)
    #tools.rc.hset("user_seesions",sessionid,{"username":username,"userid":1})
    tools.rc.set(sessionid,username)
    tools.rc.expire(sessionid,60*30)

    # flask.request.is_json#是否请求为json
    # flask.request.json.get('')#入参是json的话，用这个

    d = {'error_code':1,'msg':'登录成功','sessionid':sessionid,'username':username,'password':password}
    return json.dumps(d,ensure_ascii=False)

@server.route('/api/pay',methods=['post'])
def pay():
    sessionId=request.values.get('sessionId')
    money = request.values.get('money')

    if tools.iskey(sessionId):
        if tools.isdigit(money):
            username = tools.rc.get(sessionId)
            sql1 = 'SELECT balance FROM user WHERE username="%s"'%(username)
            balance=tools.op_mysql(sql1,many=0)
            if balance.get('balance') and float(balance.get('balance')-float(money))>=0:
                sql2 = 'update user set balance=%s-%s where username="%s";' %(float(balance.get("balance")), float(money), username)
                try:
                    tools.op_mysql(sql2, many=0)
                    return json.dumps({'error_code': 0, 'msg': '支付成功'}, ensure_ascii=False)
                except:
                    return json.dumps({'error_code': 1, 'msg': '扣款失败'}, ensure_ascii=False)
            else:
                return json.dumps({'error_code': 1, 'msg': '余额不足）'}, ensure_ascii=False)
        else:
            return json.dumps({'error_code': 1, 'msg': '请输入正确金额数值）'}, ensure_ascii=False)


    else:

        return json.dumps({'error_code': 1, 'msg': '非用户不成功'}, ensure_ascii=False)

server.run(host='0.0.0.0',port=8000,debug=True)