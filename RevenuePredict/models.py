from django.db import models
from django.contrib.auth.models import User

from EnsembleTreeModel.predict import predict


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
        l = [self.OpenDate, self.CityGroup, self.P1,
             self.P2, self.P6, self.P7, self.P11,
             self.P17, self.P21, self.P22, self.P28]
        return predict(l)
