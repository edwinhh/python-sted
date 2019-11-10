import requests,os
def get_qq_img(qq_number):
    url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
    data = {"gc": qq_number, "st": 0, "end": 20, "bkn": 130497566}
    header = {
        "cookie": "pgv_pvi=7249094656; RK=kixRx4+4MA; ptcz=a6f42fd1cdde6551c7d77580b5b1a4bebc43f775e1c67619f90e86bbcb7d795a; pgv_pvid=9135559620; pac_uid=0_5dad537cd2c5a; pgv_si=s3034066944; _qpsvr_localtk=1573092681724; uin=o1146668071; ptisp=ctc; p_uin=o1146668071; traceid=95d450c234; pgv_info=ssid=s4130806408; ts_uid=8666553536; ts_last=qun.qq.com/member.html; skey=@nY5s1SQFV; pt4_token=uI-P*0RFcI0m0TENWIROuXpPYKEoYXeusjXvl1JckB8_; p_skey=rZhp86j2C5LwGevsSis2q9q4XgcBl1YbuENoOaVwmVc_; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin"}
    mems = requests.post(url, data, verify=False, headers=header).json().get('mems')

    img_url = 'https://q4.qlogo.cn/g?b=qq&nk=%s&s=140'
    if not os.path.exists(str(qq_number)):
        os.mkdir(str(qq_number))

    for mem in mems:
        qq = mem.get('uin') #qq
        nick = mem.get('nick') if not mem.get('card') else mem.get('card')
        req = requests.get(img_url % qq)
        f = open(nick+'.jpg','wb')
        f.write(req.content)
        f.close()



