# Generated by Django 3.1.7 on 2021-03-24 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spelling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='due_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 24, 9, 25, 31, 435990, tzinfo=utc)),
        ),
    ]
