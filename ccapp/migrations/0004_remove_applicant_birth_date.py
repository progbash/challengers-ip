# Generated by Django 2.2.6 on 2019-12-07 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0003_applicant_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='birth_date',
        ),
    ]
