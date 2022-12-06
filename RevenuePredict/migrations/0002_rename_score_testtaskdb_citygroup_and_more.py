# Generated by Django 4.1.3 on 2022-12-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevenuePredict', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testtaskdb',
            old_name='score',
            new_name='CityGroup',
        ),
        migrations.RemoveField(
            model_name='testtaskdb',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='testtaskdb',
            name='lastname',
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='OpenDate',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P1',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P11',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P17',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P2',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P21',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P22',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P28',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P6',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='P7',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='testtaskdb',
            name='revenue',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
