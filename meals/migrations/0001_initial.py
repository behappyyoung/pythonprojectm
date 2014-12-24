# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dish_title', models.CharField(max_length=200)),
                ('dish_desc', models.CharField(max_length=200)),
                ('dish_type', models.CharField(default=b'cooked', max_length=20)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2014, 12, 24, 1, 12, 24, 320893, tzinfo=utc), verbose_name=b'date published')),
                ('photo', models.ImageField(default=b'/var/www/pythonprojectm//images/meals/no-img.jpg', upload_to=b'/var/www/pythonprojectm/images/meals')),
                ('votes', models.IntegerField(default=0)),
                ('votes_name', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_title', models.CharField(max_length=200)),
                ('meal_desc', models.CharField(max_length=200)),
                ('meal_type', models.CharField(default=b'public', max_length=20)),
                ('featured', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2014, 12, 24, 1, 12, 24, 320893, tzinfo=utc), verbose_name=b'date published')),
                ('photo', models.ImageField(default=b'/var/www/pythonprojectm//images/meals/no-img.jpg', upload_to=b'/var/www/pythonprojectm/images/meals')),
                ('owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dish',
            name='meal',
            field=models.ManyToManyField(to='meals.Meal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dish',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
