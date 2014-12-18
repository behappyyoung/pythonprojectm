# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='photo',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'meals'),
            preserve_default=True,
        ),
    ]
