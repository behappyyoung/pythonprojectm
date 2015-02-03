# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myprofile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='zipcode',
            field=models.CharField(default=b'', help_text='Zipcode', max_length=10, verbose_name='zipcode'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='address',
            field=models.CharField(default=b'', help_text='Address', max_length=150, verbose_name='address'),
            preserve_default=True,
        ),
    ]
