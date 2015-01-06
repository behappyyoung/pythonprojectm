# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150106_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='lastname',
        ),
    ]
