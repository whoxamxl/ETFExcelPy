from excel.excel_reader import ExcelReader
from excel.excel_writer import ExcelWriter
from security_manager import SecurityManager

if __name__ == '__main__':
    sm = SecurityManager()
    file_path = "ETF.xlsx"
    er = ExcelReader(file_path, sm)
    er.read_and_update_securities()
    ew = ExcelWriter(file_path, sm)
    ew.update_excel()