__author__ = 'young'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views import generic
from meals.models import Meal, Dish


class HomeView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'meal_list'

    def get_queryset(self):
        """Return the last five published questions."""
        ##return Question.objects.order_by('-pub_date')[:5]
        return Meal.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]