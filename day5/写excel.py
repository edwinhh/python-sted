import xlwt

# sheet.write(0,0,'名字')
# sheet.write(1,0,'王庆柱')
# sheet.write(2,0,'王宇建')
#
# sheet.write(0,1,'手机号')
# sheet.write(1,1,'119')
# sheet.write(2,1,'110')


stus = [
    ['id', 'name', 'sex', 'age', 'addr', 'grade', 'phone', 'gold'],
    [314, '矿泉水', '男', 18, '北京市昌平区', '摩羯座', '18317155663', 14405],
    [315, '矿泉水', '女', 27, '上海', '摩羯座', '18317155664', 100],
    [5985, '矿泉水', '男', 18, '北京市昌平区', '班级', '18513867663', 100]
]

# row = 0#行号
# for stu in stus:#控制行
#     col = 0#列号
#     for field in stu:#控制列的
#         sheet.write(row,col,field)
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
# print(json.dumps(l,ensure_ascii=False,indent=2))