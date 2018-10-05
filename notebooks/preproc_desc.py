

import pandas as pd
import os

path = '/Users/jean-sebastienprovost/Desktop/coursera/kaggle/energy_forecasting'
os.chdir(path)


class Data:

    def __init__(self):
        self.ind_col = 0

        # NEED TO FIX => df1 and df2 are coming from a previous pd.read_csv and not from a method from this class

    def getMerge(self, df1, df2, df2_features, ontarget):
        df1 = pd.merge(df1, df2[df2_features], on=ontarget)
        return df1

    def getBoxplot(self, x, y, hue=None):
        p = sns.boxplot(x=x, y=y, data=self.df, hue=None)
        return p

    def preview_data(self, nrow=None):
        return self.df.head(nrow)

    def extract_spec_val(self, col_id, series_id, extract_col):
        return self.df[self.df[col_id] == series_id][extract_col]

    def desc_stats(self, col=None):
        return self.df[col].describe()

    def get_min(self, col):
        return self.df[col].min()

    def get_max(self, col):
        return self.df[col].max()

    def show_data(self):
        print(self.df)

    def _load_data(self, file):
        self.df = pd.read_csv(file, index_col=0)


data = Data()
