from kafka import KafkaProducer
from kafka import KafkaConsumer
import pandas as pd
import pickle
import json
import os

import logging

logging.basicConfig(level=logging.INFO)

filename = os.environ["MODEL_DIR"]
model = pickle.load(open(filename, 'rb'))

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

consumer = KafkaConsumer(
    'query_dict',
    bootstrap_servers='kafka:9092'
)


def predict_and_send(msg):
    msg = json.loads(msg.value.decode('utf-8'))
    params = msg['params']
    hash_id = msg['hash_id']

    data = pd.DataFrame(params, index=[0]).astype('float64')
    revenue = model.predict(data)[0]

    params['revenue'] = revenue
    logging.info(params)

    producer.send('revenue', {'revenue': revenue, 'hash_id': hash_id})
    producer.flush()


if __name__ == "__main__":
    for message in consumer:
        try:
            predict_and_send(message)
        except Exception as e:
            logging.error(e)
            continue
