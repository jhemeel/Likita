# Generated by Django 3.2.22 on 2023-11-02 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20231102_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 16, 28, 55, 97062)),
        ),
        migrations.AlterField(
            model_name='replycontact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 16, 28, 55, 98064)),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 16, 28, 55, 98064)),
        ),
    ]
