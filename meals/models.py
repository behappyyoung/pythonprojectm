# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Meal(models.Model):
    meal_title = models.CharField(max_length=200)
    meal_desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.meal_title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        ##return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Dish(models.Model):
    meal = models.ForeignKey(Meal)
    dish_title = models.CharField(max_length=200)
    dish_desc = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    votes_name = models.CharField(max_length=200,  blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_title

