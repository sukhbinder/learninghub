# Generated by Django 3.1.7 on 2021-03-30 07:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spelling', '0002_auto_20210324_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='isvoiceonly',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='due_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 30, 7, 36, 34, 63448, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='word',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spelling.subject'),
        ),
    ]