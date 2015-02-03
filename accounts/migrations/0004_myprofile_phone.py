# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150121_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='phone',
            field=models.CharField(default=b'', help_text='Phone Number', max_length=12, verbose_name='phone'),
            preserve_default=True,
        ),
    ]
