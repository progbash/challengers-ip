# Generated by Django 2.2.6 on 2019-12-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0006_auto_20191207_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='birth_date',
            field=models.DateField(),
        ),
    ]
