# Generated by Django 4.1.3 on 2022-12-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevenuePredict', '0006_remove_testtaskdb_revenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtaskdb',
            name='revenue',
            field=models.FloatField(blank=True, null=True),
        ),
    ]