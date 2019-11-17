import flask
from flask import request
import json,requests,jsonpath
import tools,time,os



#第一道题
def qq_check(qq):
    url="https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
    data = {'gc':qq,'bkn':808606003,'st':0,'end':20,'sort':0}
    headers = {'cookie':'pgv_info=ssid=s7322537788; pgv_si=s495309824; _qpsvr_localtk=0.22363272675046208; uin=o0923465313; skey=@Hx3xqwQv4; ptisp=ctc; pgv_pvid=144784798; ptcz=8edafc8d58972a178b269974b565ca131f9e3f08a0a955f4e883d4acd9b41c7e; pgv_pvi=4414191616; RK=yBIZ4LfMP3; p_uin=o0923465313; pt4_token=ykT1xtwrJhqPztQz42xC42DSQFn8l9WihEU9AmJAcus_; p_skey=UMUW7fUtaCTP-t2hszHyx7h4x1NbBfGnhUXob61b3-8_; traceid=f193e581ea; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin; ts_uid=3175526692; ts_last=qun.qq.com/member.html'}
    r = requests.post(url,data=data,verify=False,headers=headers )
    result=jsonpath.jsonpath(r.json(),'$.mems')
    return result[0]



def img_down(qq):
    qqs=qq_check(qq)
    url='https://q4.qlogo.cn/g'
    current_dir=os.path.abspath('.')
    img = os.path.join(current_dir, 'qq_img')
    if not os.path.exists(img):
        os.mkdir(img)
    for i in qqs:
        data={'b':'qq',
              'nk':i.get('uin'),
               's':140}
        r=requests.get(url,params=data,verify=False)
        if i.get('nick'):
            name=i.get('nick')
        else:
            name=str(i.get('uin'))
        with open(os.path.join(img,name+'.png'),'wb') as f:
            f.write(r.content)


qq='26930605'
#img_down(qq)


#第2,3题
server = flask.Flask(__name__)

@server.route('/api/login',methods=['post','get'])
def login():
    username = flask.request.values.get('username')#从请求里面获取到参数的
    password = flask.request.values.get('password')
    tick=time.time()
    t=username+str(tick)
    sessionid=tools.md5(t)
    #tools.rc.hset("user_seesions",sessionid,{"username":username,"userid":1})
    tools.rc.set(sessionid,username)
    tools.rc.expire(sessionid,60*60)

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

        return json.dumps({'error_code': 1, 'msg': '非用户登录，登录不成功！'}, ensure_ascii=False)

server.run(host='0.0.0.0',port=8000,debug=True)