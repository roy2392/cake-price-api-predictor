import pandas as pd

from src.exceptions import NoInputException


class CollectData():
    def __init__(self, config):
        self.file_locaiton = config.data_file

    def _get_file_data(self):
        if self.file_locaiton:
            return pd.read_csv(self.file_locaiton)
        else:
            raise NoInputException("file_locaiton is not exist")

    def get_data(self):
        return self._get_file_data()