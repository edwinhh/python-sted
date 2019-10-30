import xlrd

book = xlrd.open_workbook(r'/Users/nhy/Desktop/中奖名单.xlsx')
sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name('sheet1')
result = sheet.cell(0,0).value #某个单元格的内容
print('某个单元格的内容',result)

row = sheet.row_values(0) #整行的内容
print('某一行的内容',row)

col = sheet.col_values(0) #整行的内容
print('某一列的内容',col)

print(sheet.nrows) #总共多少行
print(sheet.ncols) #总共多少列

for row_num in range(1,sheet.nrows):
    print(sheet.row_values(row_num))