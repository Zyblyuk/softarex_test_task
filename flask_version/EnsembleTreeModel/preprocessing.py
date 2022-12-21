import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from datetime import date
from datetime import datetime


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


def preproc_drop(df: pd.DataFrame) -> pd.DataFrame:
    df['City Group'] = (df['City Group'] == 'Big Cities').astype(int)
    df['Type'] = (df['Type'] == 'IL').astype(int)
    df.drop(['City', 'Id'], axis=1, inplace=True)

    df = transform_date(df)

    return df


def get_smallest_corr_columns(df: pd.DataFrame) -> set:
    drop_col = []
    corr_matrix = df.corr()

    for i in corr_matrix.columns.drop('revenue'):
        corr = corr_matrix[i].index
        for a in corr:
            if corr_matrix[i][a] > 0.9 and i != a:
                if corr_matrix['revenue'][i] > corr_matrix['revenue'][a]:
                    drop_col.append(a) if a not in drop_col else 0
                else:
                    drop_col.append(i) if i not in drop_col else 0

    smallest = corr_matrix['revenue'][np.abs(corr_matrix['revenue'] < 0.05)].index
    drop_col += smallest.values.tolist()
    return set(drop_col)


def preproc_scaler(df: pd.DataFrame) -> pd.DataFrame:
    columns = []

    if 'revenue' in df.columns:
        columns = df.columns.drop(['revenue'])
    else:
        columns = df.columns

    scale = MinMaxScaler()
    for col in columns:
        df[col] = scale.fit_transform(df[col].values.reshape(-1, 1))
    return df


if __name__ == '__main__':
    train_data = pd.read_csv('income-prediction/train.csv')
    test_data = pd.read_csv('income-prediction/test.csv')

    train_data = preproc_drop(train_data)
    test_data = preproc_drop(test_data)

    smallest = get_smallest_corr_columns(train_data)

    train_data.drop(smallest, axis=1, inplace=True)
    test_data.drop(smallest, axis=1, inplace=True)

    train_data = preproc_scaler(train_data)
    test_data = preproc_scaler(test_data)

    train_data['id'] = train_data.index
    test_data['id'] = test_data.index

    train_data.set_index('id', inplace=True)
    test_data.set_index('id', inplace=True)

    train_data.to_csv('csv/train.csv')
    test_data.to_csv('csv/test.csv')
