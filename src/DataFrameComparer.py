import pandas as pd

class DataFrameComparer:
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2

    def compare_dataframes(self):
        for index, row in self.df1.iterrows():
            matching_rows = self.df2[(self.df2.iloc[:, 0] == row[0]) & (self.df2.iloc[:, 1] == row[1])]
            if len(matching_rows) > 1:
                raise Exception('More than one matching row found in second dataframe')
            elif len(matching_rows) == 1:
                if matching_rows.iloc[0, 3] != row[2]:
                    print(f'Row {index} in first dataframe does not match with the found row in second dataframe')