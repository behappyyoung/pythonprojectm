# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
now = timezone.now()
MEALTYPE=(
    (1, ('Public')),
    (2, ('Member')),
    (3, ('Private'))
)
DISHTYPE=(
    (1, ('Fully Cooked')),
    (2, ('Row / Ready to Cook ')),
    (3, ('Ingredients Only'))
)
class Dish(models.Model):

    dish_name = models.CharField(max_length=200)   ## dish name
    dish_desc = models.CharField(max_length=200)
    ##meal = models.ManyToManyField(Meal)
    owner = models.ForeignKey(User, default=1)
    dish_type=models.IntegerField(choices=DISHTYPE, default=1)
    pub_date = models.DateTimeField('date published', default=now)
    photo = models.ImageField(upload_to='meals', default = '/meals/no-img.jpg')
    votes = models.IntegerField(default=0)
    votes_name = models.CharField(max_length=200,  blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return  u'%s' % (self.dish_name)


class Meal(models.Model):
    meal_name = models.CharField(max_length=200)   ## meal name
    meal_desc = models.CharField(max_length=200)
    dishes = models.ManyToManyField(Dish, through='MealDish')
    owner = models.ForeignKey(User, default=1)
    ## meal type : public, private,
    meal_type=models.IntegerField(choices=MEALTYPE, default=1)
    featured=models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', default=now)
    photo = models.ImageField(upload_to='meals', default = 'meals/no-img.jpg')
    def __unicode__(self):              # __unicode__ on Python 2
        return  u'%s' % (self.meal_name)
    def was_published_recently(self):
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        ##return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class MealDish(models.Model):
    dish = models.ForeignKey(Dish)
    meal = models.ForeignKey(Meal)
    quantity = models.IntegerField(max_length=30, default=1)
