# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_auto_20150116_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_type',
            field=models.IntegerField(default=1, choices=[(1, b'Fully Cooked'), (2, b'Row / Ready to Cook '), (3, b'Ingredients Only')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dish',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 16, 2, 51, 47, 730978, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 16, 2, 51, 47, 730978, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
