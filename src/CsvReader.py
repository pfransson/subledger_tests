import pandas as pd

class CSVReader:
    @staticmethod
    def get_data(file_path):
        # Load the CSV file as a pandas DataFrame
        df = pd.read_csv(file_path)
        return df
