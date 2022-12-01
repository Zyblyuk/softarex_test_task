import pandas as pd

from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import VotingRegressor

from sklearn.model_selection import GridSearchCV

import pickle

if __name__ == '__main__':
    dataset = pd.read_csv('csv/train.csv').set_index('id')

    columns_len = dataset.columns.shape[0]

    X = dataset.iloc[:, 0:columns_len - 1]
    Y = dataset.iloc[:, columns_len - 1]

    params = {
        "max_depth": [4, 6, 8],
        "n_estimators": [100, 500, 1000]
    }

    modelRandForest = GridSearchCV(RandomForestRegressor(), params)

    modelExtraTrees = GridSearchCV(ExtraTreesRegressor(), params)

    modelXGBR = GridSearchCV(XGBRegressor(), params)

    DecisionTreeModel = GridSearchCV(DecisionTreeRegressor(), {"max_depth": [4, 6, 8]})

    estimators = [('ExtraTrees', modelExtraTrees),
                  ('RandomForest', modelRandForest),
                  ('XGB', modelXGBR),
                  ('DecisionTree', DecisionTreeModel)]

    ensemble = VotingRegressor(estimators)

    ensemble.fit(X, Y)

    with open('model/EnsembleTreeModel.pkl', 'wb') as f:
        pickle.dump(ensemble, f)
