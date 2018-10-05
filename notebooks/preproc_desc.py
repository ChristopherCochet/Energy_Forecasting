

import pandas as pd
import os

path = '/Users/jean-sebastienprovost/Desktop/coursera/kaggle/energy_forecasting'
os.chdir(path)



class Data:

    def __init__(self):
        self.ind_col = 0

    def preview_data(self, data, nrow=None):
        df = self._load_data(data).head(nrow)
        print(df)

    def extract_spec_val(self, data, col_id, series_id, extract_col):
        df = self._load_data(data)
        return df[df[col_id] == series_id][extract_col]

    def desc_stats(self, data, col=None):
        return self._load_data(data)[col].describe()

    def min_data(self, data, col):
        return self._load_data(data)[col].min()

    def max_data(self, data, col):
        return self._load_data(data)[col].max()

    def show_data(self, data):
        df = self._load_data(data)
        return df

    def _load_data(self, file):
        return pd.read_csv(file, index_col=self.ind_col)


data = Data()

data.preview_data("consumption_train.csv",10)
