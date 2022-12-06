import pickle
import pandas as pd

columns = ['Open Date', 'City Group',
           'P1', 'P2', 'P6', 'P7','P11',
           'P17', 'P21', 'P22', 'P28']

def predict(x_data):
    data = pd.DataFrame([x_data], columns=columns)
    filename = 'EnsembleTreeModel/model/EnsembleTreeModel.pkl'
    model = pickle.load(open(filename, 'rb'))
    return model.predict(data)[0]
