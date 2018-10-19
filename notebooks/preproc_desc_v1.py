

import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#matplotlib inline

path = '/Users/jean-sebastienprovost/Desktop/coursera/kaggle/energy_forecasting'
os.chdir(path)

# ["series_id", "surface", "base_temperature", "weekly"] on="series_id"


class Data:

    def __init__(self):
        self.dict_series = {}
        self.df = pd.DataFrame()

    def _convertTimestamp(self, col=None):
        self.df[col] = pd.to_datetime(self.df[col])

    def loadAllData(self, df1, df2, df2_features, mergingFeature):
        df1 = pd.read_csv(df1, index_col=0)
        df2 = pd.read_csv(df2, index_col=0)
        tmp = pd.merge(df1, df2[df2_features], on=mergingFeature)

        # Not good coding, need to incorporate _convertTimestamp
        tmp["timestamp"] = pd.to_datetime(tmp["timestamp"])

        # Creating a dictionary with the series_id as keys
        unique_seriesID = tmp.series_id.unique()
        for i in unique_seriesID:
            self.dict_series[i] = tmp[tmp.series_id == i]
        return self.dict_series

    def show_alldata(self):
        print(self.dict_series)

    def extractSeries(self, series_id=None, drop=None):
        self.df = pd.DataFrame(self.dict_series[series_id])
        return self.df

    def extractMultSeries(self, array_series):
        lst = []
        for i in arr_series:
            lst.append(self.dict_series[i])
        self.df = pd.concat(lst)
        return self.df

    def show_current(self):
        print(self.df)

    def desc_stats(self, col=None):
        if col is None:
            return self.df.describe()
        else:
            return self.df[col].describe()

    def getMin(self, col):
        return self.df[col].min()

    def getMax(self, col):
        return self.df[col].max()

    def colname(self):
        return self.df.columns

    def linePlot(self, series_id, x, y, figsize=None, title=None, xaxis_rot=None):
        plt.figure(figsize=figsize)
        plt.title(title)
        sns.lineplot(x=x, y=y, data=self.dict_series[series_id])
        plt.xticks(rotation=xaxis_rot)
        plt.show()

    def getBoxplot(self, x, y, hue=None, figsize=None, title=None):
        plt.figure(figsize=figsize)
        plt.title(title)
        sns.boxplot(x=x, y=y, data=self.df, hue=None)
        plt.show()

    def plotSeriesACF(self, y, lags=None, alpha=None):
        plot_acf(self.df[y], lags=lags, alpha=alpha)

    def plotSeriesPACF(self, y, lags=None, alpha=None):
        plot_pacf(self.df[y], lags=lags, alpha=alpha)

    def subsetCurrentTS(self, time_col=None, arg=None, starttime=None, stoptime=None):
        if arg == "between":
            return self.df[(self.df[time_col] > starttime) & (self.df[time_col] < stoptime)]
        elif arg == "less":
            return self.df[(self.df[time_col] < starttime)]
        elif arg == "greater":
            return self.df[(self.df[time_col] > starttime)]
        else:
            return self.df

    def subsetFromFeature(self, feature, attr):
        lst = []
        for i in list(self.dict_series.keys()):
            if self.dict_series[i][feature].iloc[0] == attr:
                lst.append(self.dict_series[i])
        new_df = pd.concat(lst)
        return new_df

    ### If you do not want to display the current series, 
    ### you can use this method and enter the TS you want to see
    def plotACF(self, series_id, y, lags=None, alpha=None):
        plot_acf(self.dict_series[series_id][y], lags=lags, alpha=alpha)

    def plotPACF(self, series_id, y, lags=None, alpha=None):
        plot_pacf(self.dict_series[series_id][y], lags=lags, alpha=alpha)

    def dataTypes(self):
        print(type(self.df), self.df.dtypes)


data = Data()   
