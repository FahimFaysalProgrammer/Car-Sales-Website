# Generated by Django 5.0 on 2024-01-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_car_description_alter_car_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Contact Email (Optional)'),
        ),
    ]
