# Generated by Django 2.2.6 on 2020-04-20 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200410_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 13, 34, 51, 980840, tzinfo=utc)),
        ),
    ]
