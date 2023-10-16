# Generated by Django 4.2.1 on 2023-10-16 17:45

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='overview',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='PB', max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='Categories',
            field=models.ManyToManyField(related_name='post_categories', to='base.categories'),
        ),
    ]
