# Generated by Django 4.2.1 on 2023-10-20 00:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 20, 1, 10, 3, 121229))),
            ],
            options={
                'verbose_name_plural': 'ContactUs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SendNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.TextField()),
                ('attachment', models.FileField(default='empty-profile.png', upload_to='newsletter-file')),
                ('sender', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'SendNewsletter',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 20, 1, 10, 3, 123221))),
            ],
            options={
                'verbose_name_plural': 'Subscribe',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ReplyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replier', models.CharField(max_length=100)),
                ('subject', models.CharField(default='Reply Contacts', max_length=200)),
                ('message', models.TextField()),
                ('attachment', models.FileField(default='empty-profile.png', upload_to='contact-attchments')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 20, 1, 10, 3, 122225))),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.contactus')),
            ],
            options={
                'verbose_name_plural': 'ReplyContact',
                'ordering': ['-created_at'],
            },
        ),
    ]
