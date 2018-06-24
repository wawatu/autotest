import xlwt

def write_excel(path):
    # 创建workbook和sheet对象
    wb = xlwt.Workbook(encoding='utf-8') # 注意Workbook的开头W要大写
    sheet = wb.add_sheet('test')
    value = [['name','bookid','lange'],
             ['ali','A001','chaness'],
             ['baidu','A002','jp'],
             ['wangyi','A003','gs']]
    for i in range(0, 3):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    wb.save(path)
    print("写入数据成功！")

file = '/Users/apple/Desktop/test.xls'

if __name__ == '__main__':
    write_excel(file)
