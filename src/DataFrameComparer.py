import pandas as pd

class DataFrameComparer:
    @staticmethod
    def compare_dataframes(df1, df2):
        for index, row in df1.iterrows():
            matching_rows = df2[(df2.iloc[:, 0] == row[0]) & (df2.iloc[:, 1] == row[1])]
            if len(matching_rows) > 1:
                raise Exception('More than one matching row found in second dataframe')
            elif len(matching_rows) == 1:
                if matching_rows.iloc[0, 3] != row[2]:
                    print(f'Row {index} in first dataframe does not match with the found row in second dataframe')
