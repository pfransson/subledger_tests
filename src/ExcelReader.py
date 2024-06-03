import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_first_sheet_data(self):
        # Load the Excel file
        xls = pd.ExcelFile(self.file_path)
        # Get the names of all sheets in the Excel file
        sheet_names = xls.sheet_names
        # Load the first sheet as a pandas DataFrame
        df = xls.parse(sheet_names[0])
        return df