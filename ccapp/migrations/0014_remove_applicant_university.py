# Generated by Django 2.2.6 on 2019-12-10 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0013_auto_20191208_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='university',
        ),
    ]
