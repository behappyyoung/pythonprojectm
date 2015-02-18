__author__ = 'young'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views import generic
from meals.models import Meal, Dish
from userena.utils import (signin_redirect, get_profile_model, get_user_model,
                           get_user_profile)

import logging

class HomeView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'meal_list'



    def get_queryset(self):


        if self.request.session.get('usertype', None) != None:
            user_profile = get_user_profile(self.request.user)
            logging.error(user_profile.__dict__)
            self.request.session['usertype'] = user_profile.usertype


        logging.error(self.request.session.__dict__)
        """Return the last five published questions."""
        ##return Question.objects.order_by('-pub_date')[:5]
        meallist = Meal.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        ##logging.error(meallist.__dict__)

        return meallist