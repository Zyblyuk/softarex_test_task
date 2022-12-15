from django.db import models
from django.contrib.auth.models import User

import requests
from decouple import config


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

        query_dict = {
            'OpenDate': self.OpenDate, 'CityGroup': self.CityGroup,
            'P1': self.P1, 'P2': self.P2, 'P6': self.P6,
            'P7': self.P7, 'P11': self.P11, 'P17': self.P17,
            'P21': self.P21, 'P22': self.P22, 'P28': self.P28
        }

        host = config('PREDICT_API_HOST')
        port = config('PREDICT_API_PORT')
        response = requests.get(f"http://{host}:{port}/predict", query_dict)
        return response.json()['revenue']

    def check_empty(self):
        """Return True if some attribute empty"""
        l_art = [self.OpenDate, self.CityGroup, self.P1,
             self.P2, self.P6, self.P7, self.P11,
             self.P17, self.P21, self.P22, self.P28]
        for i in l_art:
            if not i:
                return True
        return False

    def get_dict(self):
        return {
            'OpenDate': self.OpenDate, 'CityGroup': self.CityGroup,
            'P1': self.P1, 'P2': self.P2, 'P6': self.P6,
            'P7': self.P7, 'P11': self.P11, 'P17': self.P17,
            'P21': self.P21, 'P22': self.P22, 'P28': self.P28
        }
