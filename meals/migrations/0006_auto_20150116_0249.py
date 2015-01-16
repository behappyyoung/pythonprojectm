# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_auto_20150110_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 16, 2, 49, 14, 177557, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.IntegerField(default=1, choices=[(1, b'Public'), (2, b'Member'), (3, b'Private')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 16, 2, 49, 14, 177557, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
