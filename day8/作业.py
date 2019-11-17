from tools.my_request import MyRequest
from tools.wexcel import *
import os

class InterfaceTest():
    def __init__(self,file):
        self.res = get_data(file, "1")#从excel读取原始数据

#将exlce的类似'a=1,b=2,c=3'格式的，转为字典
    def dic(self,s):
        t=[]
        k=[]
        v=[]
        dic={}
        t=s.split(",")
        for i in t:
            k.append(i.split("=")[0])
            v.append(i.split("=")[1])
        dic=dict(zip(k,v))
        return dic

    def check(self,ck,res):
        fag = 1
        # for k,v in ck.items():
        #     if k in res.keys():
        #         if v==res[k]
        for i in ck.keys():

            if i in res.keys():
                if ck[i]!= str(res[i]):
                    fag=0
        if fag:
            res="校验成功"
        else:
            res="校验失败"
        return res




#将从excel读取的每行内容，提取出url，data，method，check等关键值，并生产字典返回
    def parameter(self):
        dic=[]
        for i in self.res[1:]:
            dic_={}
            dic_=dict(url=i[2],method=i[3],data=self.dic(i[4]),check=self.dic(i[5]))
            dic.append(dic_)
        return dic

#将 parameter类函数返回的字典传入，调用tools包下的MyRequest类，返回请求结果，返回响应和状态结果以list返回
    def my_request(self,data):
        par=data
        res=[]
        for i in par:
            res_=[]
            a=MyRequest(url=i.get("url"),method=i.get("method"),data=i.get("data"))

            res_.append(self.check(i.get("check"),a.response))
            res_.append(str(a.response))
            res.append(res_)
        return res

    def update_excl(self,f):
        req=f
        for i in range(len(req)):
            self.res[i+1][6]=req[i][0]
            self.res[i+1][7] = req[i][1]
        return self.res


#在原始excel目录下，生成结果文件
    def sava_excl(self):

        name1=os.path.basename(file)
        dir=os.path.dirname(file)
        name1_prefix=name1.split(".")[0]
        name=name1_prefix+"_reslut.xlsx"
        exfile=os.path.join(dir,name)
        wexcel(exfile,name1,self.res)


#整合相关请求，只需要调用该类函数即可
    def run(self):
        b = self.my_request(self.parameter())
        self.update_excl(b)
        self.sava_excl()


file = "D:\python_sted\day8\用例模板.xlsx"
cl=InterfaceTest(file)
cl.run()
# b=cl.run(cl.my_request())
# #print(b)
# cl.update_excl(b)
# #print(cl.res)

cl.sava_excl()

