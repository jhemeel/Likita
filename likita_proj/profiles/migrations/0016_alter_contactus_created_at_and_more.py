# Generated by Django 4.2.1 on 2023-06-26 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_contactus_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 10, 26, 17, 577992)),
        ),
        migrations.AlterField(
            model_name='replycontact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 10, 26, 17, 578991)),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 10, 26, 17, 579988)),
        ),
    ]