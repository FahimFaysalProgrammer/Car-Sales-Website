# Generated by Django 5.0 on 2024-01-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
