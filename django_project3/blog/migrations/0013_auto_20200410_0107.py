# Generated by Django 2.2.7 on 2020-04-09 20:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200128_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 20, 7, 23, 519946, tzinfo=utc)),
        ),
    ]