# Generated by Django 4.2.1 on 2023-06-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_replycontact_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycontact',
            name='subject',
            field=models.CharField(default='Reply', max_length=200),
        ),
    ]