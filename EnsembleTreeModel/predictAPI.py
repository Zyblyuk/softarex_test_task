import pickle
import pandas as pd

from flask import Flask
from flask import request
from flask import json
import os

app = Flask(__name__)


columns = ['Open Date', 'City Group',
           'P1', 'P2', 'P6', 'P7','P11',
           'P17', 'P21', 'P22', 'P28']

filename = 'model/EnsembleTreeModel.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route('/predict')
def user():
    x_data = [request.args.get(i.replace(' ', '')) for i in columns]
    data = pd.DataFrame([x_data], columns=columns).astype('float64')

    revenue = model.predict(data)[0]
    response = app.response_class(
        response=json.dumps({'revenue': revenue}),
        status=200,
        mimetype='application/json'
    )
    return response



if __name__ == "__main__":
    app.run(host=os.environ["FLASK_RUN_HOST"],
            port=int(os.environ["FLASK_PORT"]))