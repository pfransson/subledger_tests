import pandas as pd

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        # Load the CSV file as a pandas DataFrame
        df = pd.read_csv(self.file_path)
        return df