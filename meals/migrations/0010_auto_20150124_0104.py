# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0009_auto_20150124_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 1, 4, 32, 756292, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 1, 4, 32, 756292, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
