import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error

from datetime import date
from datetime import datetime

import matplotlib.pyplot as plt


def transform_date(dataframe):
    today = date.today()
    days = []
    for value in dataframe["Open Date"].values:
        casting_date = datetime.strptime(value, "%m/%d/%Y").date()
        delta = today - casting_date
        day = delta.days
        days.append(day)

    dataframe["Open Date"] = pd.Series(days, name="Open Days")
    return dataframe


dataset = pd.read_csv('income-prediction/train.csv')

dataset['City Group'] = (dataset['City Group'] == 'Big Cities').astype(int)
dataset['Type'] = (dataset['Type'] == 'IL').astype(int)

dataset.drop(['City', 'Id'], axis=1, inplace=True)

dataset = transform_date(dataset)
columns_len = dataset.columns.shape[0]

X = dataset.iloc[:, 0:columns_len - 1]
Y = dataset.iloc[:, columns_len - 1]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=8)

cls = ExtraTreesRegressor()
cls.fit(X_train, y_train)

print(cls.feature_importances_)
feat_importances = pd.Series(cls.feature_importances_, index=X.columns)
feat_importances.nlargest(8).plot(kind='barh')
plt.show()

y_predict_test = cls.predict(X_test)

print(f'\nRandomForestRegressor Test date:\n'
      f'RMSE:\t{np.sqrt(mean_squared_error(y_test, y_predict_test))}')

