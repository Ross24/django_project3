# Generated by Django 2.2.6 on 2019-12-13 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191214_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 16, 47, 34, 289549, tzinfo=utc)),
        ),
    ]
