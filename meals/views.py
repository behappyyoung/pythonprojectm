from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from userena.decorators import secure_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import logout as Signout
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import render_to_response
from guardian.decorators import permission_required_or_403


from meals.models import Meal, Dish
from meals.forms import AddMealForm, AddDishForm

from userena.utils import (get_profile_model, get_user_model, get_user_profile)
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME


import logging
import sys
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

##if len(sys.argv) > 1:
##    level_name = sys.argv[1]
##    level = LEVELS.get(level_name, logging.NOTSET)
##    logging.basicConfig(level=level)


class IndexView(generic.ListView):
    template_name = 'meals/index.html'
    context_object_name = 'latest_meal_list'


    if False:       ### auth test
        from django.contrib.auth import authenticate
        user = authenticate(username='john', password='secret')
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")


    def get_queryset(self):
        """Return the last five published questions."""
        ##return Question.objects.order_by('-pub_date')[:5]
        return Meal.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    ##model = Dish
    ##model = get_object_or_404(Question)
    template_name = 'meals/detail.html'

    def get_queryset(self):
        """Return the last five published questions."""
        ##return Question.objects.order_by('-pub_date')[:5]
        return Meal.objects.filter()
        ##return Dish.objects.filter(pub_date__lte=timezone.now())
        ##return render_to_response(template_name, {'object': object})

class DishView(generic.DetailView):
    template_name = 'meals/dish.html'

    def get_queryset(self):
        return Dish.objects.filter()


class DishListView(generic.ListView):
    template_name = 'meals/dish_list.html'
    context_object_name = 'latest_dish_list'
    def get_queryset(self):
        return Dish.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class MyMeals(generic.ListView):
    template_name = 'meals/mymeals.html'
    context_object_name = 'my_meal_list'

    def get_queryset(self):

        user = get_object_or_404(get_user_model(), username__iexact=self.kwargs['username'])
        return Meal.objects.filter(owner=user.id).order_by('-pub_date')

class ExtraContextTemplateView(TemplateView):
    """ Add extra context to a simple template view """
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context

    # this view is used in POST requests, e.g. signup when the form is not valid
    post = TemplateView.get


def addmeal(request, addmeal_form=AddMealForm,
           template_name='meals/addmeal_form.html', success_url=None,
           extra_context=None):

    current_user = request.user
##    logging.debug(current_user)
    if hasattr(current_user, 'my_profile'):
        usertype = current_user.my_profile.usertype
        if usertype != 'chef':
            return HttpResponseRedirect('/Meals/')
    else:
         return HttpResponseRedirect('/Meals/')

    context = RequestContext(request)
    if request.method == 'POST':
        form = addmeal_form(request.POST, request.FILES)
        mealid = ''
        if form.is_valid():
            meal= form.save()
            mealid=meal.id
        return HttpResponseRedirect('/Meals/'+mealid)

    return render_to_response('meals/addmeal_form.html', {'form': addmeal_form}, context)


def AddDish(request, adddish_form=AddDishForm):
    # Get the context from the request.

    current_user = request.user
    logging.error(current_user)
    if hasattr(current_user, 'my_profile'):
        logging.error(current_user.my_profile.__dict__)
        usertype = current_user.my_profile.usertype
        if usertype != 'chef':
            return HttpResponseRedirect('/Meals/')
    else:
         return HttpResponseRedirect('/Meals/')

    context = RequestContext(request)
    if request.method == 'POST':
        form = adddish_form(request.POST, request.FILES)

        if form.is_valid():
            new_meal= form.save()
            new_meal.owner = current_user.id
            new_meal.save()
            return HttpResponseRedirect('/Meals/'+new_meal.id)
        return render_to_response('meals/adddish_form.html', {'form': form}, context)       ## with error

    return render_to_response('meals/adddish_form.html', {'form': adddish_form}, context)

