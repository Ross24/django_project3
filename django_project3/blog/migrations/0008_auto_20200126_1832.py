# Generated by Django 2.2.6 on 2020-01-26 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200126_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 26, 10, 32, 44, 843443, tzinfo=utc)),
        ),
    ]
