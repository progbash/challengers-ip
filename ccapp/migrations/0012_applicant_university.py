# Generated by Django 2.2.6 on 2019-12-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0011_auto_20191207_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='university',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
