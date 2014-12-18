# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20141218_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='photo',
            field=models.ImageField(default=b'meals/Images/no-img.jpg', upload_to=b'meals/Images'),
            preserve_default=True,
        ),
    ]
