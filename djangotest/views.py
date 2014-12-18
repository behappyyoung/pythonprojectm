__author__ = 'young'

from django.shortcuts import render_to_response
from django.template import RequestContext


from meals.models import Meal, Dish


def IndexView(request):
    context_object_name = 'meal_list'
    model = Meal
    return render_to_response('home/index.html', context_instance=RequestContext(request))