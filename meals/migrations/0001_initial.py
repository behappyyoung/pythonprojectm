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
                ('dish_name', models.CharField(max_length=200)),
                ('dish_desc', models.CharField(max_length=200)),
                ('dish_type', models.CharField(default=b'cooked', max_length=20)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 1, 9, 18, 27, 52, 777913, tzinfo=utc), verbose_name=b'date published')),
                ('photo', models.ImageField(default=b'/meals/no-img.jpg', upload_to=b'meals')),
                ('votes', models.IntegerField(default=0)),
                ('votes_name', models.CharField(max_length=200, blank=True)),
                ('owner', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_name', models.CharField(max_length=200)),
                ('meal_desc', models.CharField(max_length=200)),
                ('meal_type', models.CharField(default=b'public', max_length=20)),
                ('featured', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 1, 9, 18, 27, 52, 777913, tzinfo=utc), verbose_name=b'date published')),
                ('photo', models.ImageField(default=b'meals/no-img.jpg', upload_to=b'meals')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1, max_length=30)),
                ('dish', models.ForeignKey(to='meals.Dish')),
                ('meal', models.ForeignKey(to='meals.Meal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meal',
            name='dishes',
            field=models.ManyToManyField(to='meals.Dish', through='meals.MealDish'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meal',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
