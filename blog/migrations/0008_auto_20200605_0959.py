# Generated by Django 2.2.6 on 2020-06-05 09:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200605_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 5, 9, 59, 54, 158473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 5, 9, 59, 54, 158473, tzinfo=utc)),
        ),
    ]
