import os
from urllib.parse import urljoin
from projects.litemall.const import host,test_user,data_path
from projects.litemall import tools
from utils.request import MyRequest
from utils.mysql_util import mysql
from utils.utils import GetTestData
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor,wait,as_completed
import time

class geo():
	def __init__(self,file):
		self.url_geo='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'
		self.geo_path=os.path.join(data_path,file)
		self.par=GetTestData.data_for_txt(self.geo_path)
	def test_geo(self,par):
		'''测试geo地址返回'''
		address=par[0]
		city=par[1]
		data = {'address' :address, \
				'opt': '', \
				'city': city, \
				'ak' :"70231a4fa9c047d381cc55c8ff75e0bf"}
		res= MyRequest(self.url_geo, data)
		return {"address":address,"res":res}
		
	
geo=geo("geo.txt")
#geo.test_geo()

def parse_page(res):
    res = res.result()
    print('<%s> is running [%s]'%(os.getpid(),res['address']))

		
def mp(fun,datas,num=os.cpu_count()):
	t1=time.time()
	with ThreadPoolExecutor(num) as ex:
		f_list=[ex.submit(fun,data) for data in datas]
		#f_list = [ex.submit(fun, data).add_done_callback(parse_page) for data in datas]
	t2 = time.time()
	wait(f_list)
	for f in f_list:
		if f.running():
			print('%s is running' % str(f))
	for f in as_completed(f_list):
		try:
			ret = f.done()
			if ret:
				print('%s is finished'%f.result()['address'])
		except Exception as e:
			f.cancel()
			print(str(e))
	print("主线程结束")
	print("耗时：%s" % (t2 - t1))

def mp1(fun,datas,num=os.cpu_count()):
	t1=time.time()
	with ThreadPoolExecutor(max_workers=num) as executor:
		future=list(executor.map(fun,datas))
	t2 = time.time()
	for f in future:
		print('%s is finished'%f.get('address'))
  
	print("主线程结束")
	print("耗时：%s"%(t2-t1))

# from concurrent.futures import ProcessPoolExecutor
# def pool_factorizer_go(nums, nprocs):
#    nprocs=xxx
#     with ProcessPoolExecutor(max_workers=nprocs) as executor:
#         return {num:factors for num, factors in
#                                 zip(nums,
#                                     executor.map(factorize_naive, nums))}



mp1(geo.test_geo,geo.par)