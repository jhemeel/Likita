# Generated by Django 3.2.22 on 2023-10-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_alter_appointment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='message',
            field=models.TextField(default='optional..'),
        ),
    ]
