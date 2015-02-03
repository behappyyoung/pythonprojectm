# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_myprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='usertype',
            field=models.CharField(default=b'member', help_text='Choose User Type.', max_length=15, verbose_name='usertype', choices=[(b'member', 'Member'), (b'chef', 'Chef'), (b'mighty', 'Both')]),
            preserve_default=True,
        ),
    ]
