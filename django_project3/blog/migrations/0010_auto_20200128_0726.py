# Generated by Django 2.2.6 on 2020-01-27 23:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200126_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 27, 23, 26, 3, 711740, tzinfo=utc)),
        ),
    ]