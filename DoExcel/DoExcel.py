import xlrd
#=================
#读取Excel
#=================
# workbook = xlrd.open_workbook("Demo.xlsx")
# print(workbook.nsheets)
# table = workbook.sheet_by_index(0)
# rows_count = table.nrows #获取行数
# print(rows_count)
# cols_count = table.ncols #获取列数
# print(cols_count)

 #获取某一单元格的内容，方式1
# cell_value = table.cell(1,1).value
# print(cell_value)
 #获取某一单元格的内容，方式2
# row_data = table.row_values(2)
# cell_data = row_data[1]
# print(cell_data)

#将Excel中的数据全部取出来
# for rownumber in range(0,rows_count,1):
#     for colnumber in range(0,cols_count,1):
#         cell_value = table.cell(rownumber,colnumber)
#         print(cell_value)

#*******************
#将读取Excel的操作，封装在类中
#*******************
class ReadExcel():
    def __init__(self,fileName,sheetName):
        self.workbook = xlrd.open_workbook(fileName)
        self.table = self.workbook.sheet_by_name(sheetName)

    def read_excel(self,rowNum,colNum):
        value = self.table.cell(rowNum,colNum).value
        return value

Data = ReadExcel("Demo.xlsx","Sheet1").read_excel(1,1)
print(Data)
