import xlrd
class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = r"E:\Users\dongf\PycharmProjects\BaiDeom\config\casedata.xls"
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        #[[],[]]
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            #print(col)
            result.append(col)
            #print(cool)

        return result
if __name__ == "__main__":
    ex = ExcelUtil()
    print(ex.get_data())