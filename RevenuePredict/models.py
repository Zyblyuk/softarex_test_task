from django.db import models
from django.contrib.auth.models import User

from kafka import KafkaProducer
from kafka import KafkaConsumer

import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

consumer = KafkaConsumer(
    'revenue',
    bootstrap_servers='kafka:9092'
)


class TestTaskDB(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    OpenDate = models.FloatField(null=True, blank=True)
    CityGroup = models.FloatField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P6 = models.FloatField(null=True, blank=True)
    P7 = models.FloatField(null=True, blank=True)
    P11 = models.FloatField(null=True, blank=True)
    P17 = models.FloatField(null=True, blank=True)
    P21 = models.FloatField(null=True, blank=True)
    P22 = models.FloatField(null=True, blank=True)
    P28 = models.FloatField(null=True, blank=True)

    revenue = models.FloatField(null=True, blank=True)

    def predict(self):
        """Get predict from EnsembleTreeModel"""

        query_dict = self.get_dict()

        hash_id = hash(frozenset(query_dict.items()))
        producer.send('query_dict', {'params': query_dict, 'hash_id': hash_id})
        producer.flush()

        for message in consumer:
            msg = json.loads(message.value.decode('utf-8'))

            if msg['hash_id'] == hash_id:
                return msg['revenue']

    def get_dict(self):
        return {
            'Open Date': self.OpenDate, 'City Group': self.CityGroup,
            'P1': self.P1, 'P2': self.P2, 'P6': self.P6,
            'P7': self.P7, 'P11': self.P11, 'P17': self.P17,
            'P21': self.P21, 'P22': self.P22, 'P28': self.P28
        }
