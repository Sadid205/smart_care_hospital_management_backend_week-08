# Generated by Django 5.0.6 on 2024-07-03 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_availabletime_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availabletime',
            name='slug',
        ),
    ]
