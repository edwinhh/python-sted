import tools
#1、执行sql拿到结果
#2、写入excel
import xlwt
def export_excel(table_name):
    sql = 'select * from %s;'%table_name
    result = tools.op_mysql(sql)# = [{'id':1,'name':'xxx'},{'id':1,'name':'xxx'} ]
    if result:
        file_name = '%s.xls'%table_name
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        for col,k in enumerate(result[0]):#写表头
            sheet.write(0,col,k)
        for row,row_data in enumerate(result,1):
            for col,col_data in enumerate(row_data.values()):
                sheet.write(row,col,col_data)
        book.save(file_name)
    else:
        print('表里数据为空')
export_excel('app_myuser')

