from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from meals.models import Meal, Dish


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
