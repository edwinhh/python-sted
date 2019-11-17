import requests
import tools


# r = requests.get('url',params={'key':'value'})
#r.json()
# r.content
#r.text

# r = requests.get('http://www.nnzhp.cn/archives/855?username=abc',params={'key':'value'},data={'username':'xxxx'})
# print(r.json())
# print(r.text)

# r = requests.post('url',json={'':''})
url='https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'

#data = {'gc':613536708,'bkn':240397961,'st':0,'end':40}
# headers = {'cookie':'pgv_pvi=6636933120; RK=gRZhhBpNbS; ptcz=14bab564718e3e1048a09cc0e18a23f7c51f20d5b93da610cc1427f51f63a2f8; pgv_pvid=4990195883; ts_uid=5190463916; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin; uin=o0511402865; skey=@LUFPqSBxO; ptisp=cnc; pgv_info=ssid=s5139002932; ts_last=qun.qq.com/member.html; pgv_si=s4695831552; p_uin=o0511402865; pt4_token=m-08apoc2xJxW51Ahx*LKfuD4UyR2WEUd6PWyQ1PB8s_; p_skey=1whnzxqbI2kEJ7IEYgnr6wzrBRo8BY6dhPg57tD7ZBs_;'}
# r = requests.post(url,data=data,verify=False,headers=headers )
# print(r.json())

url1="http://127.0.0.1:8000/api/pay"
data={"sessionId":"2d2f69334817e10defab73fbd9161f7b","money":0.5}
#requests.post('url',files = {'file':open('a.py','rb')})
a=MyRequest(url1,method="post",data=data)
print(a.text)
# tools.put("abc","1")
# tools.rc.expire("abc",5)
