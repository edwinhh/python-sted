import openpyxl

book = openpyxl.Workbook()
sheet = book.active #默认的sheet
#sheet2 = book.get_sheet_by_name('sheet1')
# sheet.append( ['id','username','password','error_count'])
# sheet.append( [1,'wyj','123456',0])
# sheet.append( [2,'wyj','123456'])
sheet['a1'] = 'id'
sheet['b1'] = 'username'
sheet.cell(3,1,'1')
book.save('user.xlsx')
