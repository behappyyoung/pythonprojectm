# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_auto_20150106_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(default=b'/meals/no-img.jpg', upload_to=b'meals'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dish',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 6, 23, 5, 23, 351624, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='photo',
            field=models.ImageField(default=b'meals/no-img.jpg', upload_to=b'meals'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 6, 23, 5, 23, 351624, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
