import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error

from datetime import date
from datetime import datetime

import seaborn as sn
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


if __name__ == '__main__':
    dataset = pd.read_csv('income-prediction/train.csv')

    dataset['City Group'] = (dataset['City Group'] == 'Big Cities').astype(int)
    dataset['Type'] = (dataset['Type'] == 'IL').astype(int)

    dataset.drop(['City', 'Id'], axis=1, inplace=True)

    dataset = transform_date(dataset)

    corr_matrix = dataset.corr()
    plt.figure(figsize=(20, 20))
    sn.heatmap(corr_matrix, annot=True)
    plt.show()

    drop = []
    for i in corr_matrix.columns.drop('revenue'):
        corr = corr_matrix[i].index
        for a in corr:
            if corr_matrix[i][a] > 0.9 and i != a:
                if corr_matrix['revenue'][i] > corr_matrix['revenue'][a]:
                    drop.append(a) if a not in drop else 0
                else:
                    drop.append(i) if i not in drop else 0

    dataset.drop(drop, axis=1, inplace=True)

    largest = corr_matrix['revenue'][np.abs(corr_matrix['revenue'] > 0.05)].index
    largest = [i for i in largest if i not in drop]
    dataset = dataset[largest]
    dataset.head()

    scale = MinMaxScaler()

    for col in dataset.columns.drop(['revenue']):
        dataset[col] = scale.fit_transform(dataset[col].values.reshape(-1, 1))

    columns_len = dataset.columns.shape[0]

    X = dataset.iloc[:, 0:columns_len - 1]
    Y = dataset.iloc[:, columns_len - 1]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=8)

    cls = ExtraTreesRegressor()
    cls.fit(X_train, y_train)

    y_predict_test = cls.predict(X_test)
    print(f'RMSE:\t{np.sqrt(mean_squared_error(y_test, y_predict_test))}')
