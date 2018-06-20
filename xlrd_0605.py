import xlrd
from datetime import date,datetime

def read_excel(path):
    # 打开文件
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_names()
    workbook = workbook.sheet_by_name(sheet[0])
    for i in range(0, workbook.nrows):
        row = workbook.row(i)
        for j in range(0, workbook.ncols):
            print(workbook.cell_value(i, j), '\t', end='' )
        print()


    workbook = xlrd.open_workbook(path)
    # 获取所有sheet
    print(workbook.sheet_names()) # ['sheet1','sheet2']
    # 获取指定的sheet
    sheet_name = workbook.sheet_names()[0] # sheet从0开始
    print(sheet_name)
    
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0) # sheet索引从0开始
    # sheet = workbook.sheet_by_name('空sheet')
    print(sheet.name, sheet.nrows, sheet.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet.row_values(3) # 获取第四行内容
    cols = sheet.col_values(2) # 获取第三列内容
    print(rows)
    print(cols)

    # 获取单元格内容
    print(sheet.cell(1,0).value)
    print(sheet.cell_value(2,1))
    print(sheet.row(3)[2].value)

    # 获取单元格内容的数据类型 ctype:0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    print(sheet.cell(1,0).ctype)

    
file = '/Users/apple/Desktop/Excel.xls'

if __name__ == '__main__':
    read_excel(file)
