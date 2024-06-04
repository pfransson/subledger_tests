import pandas as pd

class ExcelReader:
    @staticmethod
    def get_first_sheet_data(file_path):
        # Load the Excel file
        xls = pd.ExcelFile(file_path)
        # Get the names of all sheets in the Excel file
        sheet_names = xls.sheet_names
        # Load the first sheet as a pandas DataFrame
        df = xls.parse(sheet_names[0])
        return df
