# Generated by Django 3.2.22 on 2023-10-27 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 9, 14, 10, 917959)),
        ),
        migrations.AlterField(
            model_name='replycontact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 9, 14, 10, 917959)),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 9, 14, 10, 918956)),
        ),
    ]
