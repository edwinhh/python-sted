import xlwt,xlrd
import pymysql
ip = '118.24.3.40'
user = 'jxz'
password = '123456'
db = 'jxz'
port = 3306#默认端口号，可以不指定，需要改的话要传
charset = 'uft8'
conn= pymysql.connect(host = ip,user = user,password = password,db = db,port = port ,charset = charset,autocommit=True)#连接
cur= conn.cursor()#游标
sql = 'select *from app_myuser limit 10;'
cur.execute(sql)#执行sql语句
one = cur.fetchone()
many = cur.fetchmany()
all = cur.fetchall()
cur.close()#关游标
conn.close()#关连接
print(one)
# print(many)
# print(all)

import base64 #能加密，也能解密

s='https://www.cnblogs.com/zanjiahaoge666/p/7242642.html '
b = base64.b64encode( s.encode() ) #加密
result= b.decode()
print(result)

b = base64.b64decode( result ) #解密
print(b.decode())



stus = [
    ['id', 'name', 'sex', 'age', 'addr', 'grade', 'phone', 'gold'],
    [314, '矿泉水', '男', 18, '北京市昌平区', '摩羯座', '18317155663', 14405],
    [315, '矿泉水', '女', 27, '上海', '摩羯座', '18317155664', 100],
    [5985, '矿泉水', '男', 18, '北京市昌平区', '班级', '18513867663', 100]
]

#row = 0#行号
# for stu in stus:#控制行
#     col = 0#列号
#     for field in stu:#控制列的
#         sheet.write(row,col,field,cell_overwrite_ok=True)
#         col+=1 #
#     row+=1

# book = xlwt.Workbook()
# sheet = book.add_sheet('sheet1')
# for row,stu in enumerate(stus):#控制行
#     for col,field in enumerate(stu):#控制列的
#         sheet.write(row,col,field)
# book.save("students.xls")


# l=[['id', 'name', 'sex', 'age', 'addr', 'grade', 'phone', 'gold'], [314, '矿泉水', '男', 18, '北京市昌平区', '摩羯座', '18317155663', 14405], [315, '矿泉水', '女', 27, '上海', '摩羯座', '18317155664', 100], [5985, '矿泉水', '男', 18, '北京市昌平区', '班级', '18513867663', 100]]
# import json
# print(l)
# print(json.dumps(l,ensure_ascii=False,indent=2))

b=xlrd.open_workbook('students.xls')
s=b.sheet_by_name('sheet1')

for rnum in range(1,s.nrows):
    for cnum in range(1,s.ncols):
        print(s.cell(rnum,cnum).value)