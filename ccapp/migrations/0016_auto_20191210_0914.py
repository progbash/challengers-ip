# Generated by Django 2.2.6 on 2019-12-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0015_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender_email',
            field=models.EmailField(max_length=50),
        ),
    ]
