# Generated by Django 3.2 on 2022-01-27 02:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='apellido',
            field=models.CharField(default='jose', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='flores', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 2, 9, 38, 792233, tzinfo=utc)),
        ),
    ]
