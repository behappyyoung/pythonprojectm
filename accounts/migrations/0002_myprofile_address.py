# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='address',
            field=models.CharField(default=b'', help_text='Address', max_length=15, verbose_name='address'),
            preserve_default=True,
        ),
    ]
