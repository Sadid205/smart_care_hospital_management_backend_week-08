# Generated by Django 5.0.6 on 2024-07-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabletime',
            name='slug',
            field=models.SlugField(default='default_value', max_length=100),
            preserve_default=False,
        ),
    ]
