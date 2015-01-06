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
            name='firstname',
            field=models.CharField(default=b'', help_text='first name', max_length=15, verbose_name='firstname'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myprofile',
            name='lastname',
            field=models.CharField(default=b'', help_text='last name', max_length=15, verbose_name='lastname'),
            preserve_default=True,
        ),
    ]
