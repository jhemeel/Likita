# Generated by Django 3.2.22 on 2023-11-01 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20231101_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 0, 36, 6, 943008)),
        ),
        migrations.AlterField(
            model_name='replycontact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 0, 36, 6, 944036)),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 0, 36, 6, 944036)),
        ),
    ]
