# Generated by Django 4.2.4 on 2023-08-27 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='code',
        ),
    ]
