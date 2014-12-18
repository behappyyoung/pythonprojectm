# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='photo',
            field=models.ImageField(default=b'meals/None/no-img.jpg', upload_to=b'meals'),
            preserve_default=True,
        ),
    ]
