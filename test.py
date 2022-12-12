import requests
import json

query_dict = {'OpenDate': 1,
           'CityGroup': 1,
           'P1': 1,
           'P2': 1,
           'P6': 0.5,
           'P7': 0.5,
           'P11': 1,
           'P17': 0.5,
           'P21': 1,
           'P22': 0,
           'P28': 0
}

a = requests.get('http://localhost:9876/predict', query_dict)
print(a.json()['revenue'])
