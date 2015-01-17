__author__ = 'young'

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from meals.models import Dish, Meal


from userena import settings as userena_settings

from userena.models import UserenaSignup
from userena.utils import get_profile_model, get_user_model

attrs_dict = {'class': 'required'}
NAME_RE = r'^[\. \w]+$'

class AddMealForm(forms.ModelForm):
    """
    """
    meal_name = forms.RegexField(regex=NAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Name"),
                                error_messages={'invalid': _('Meal Name must contain only letters, numbers, dots and underscores.')})
    meal_desc = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Desc"))

    class Meta:
        model = Meal
"""
    def save(self):
        meal_name, meal_desc = (self.cleaned_data['meal_name'], self.cleaned_data['meal_desc'])

        new_meal = Meal.objects.create_user(meal_name,
                                                     meal_desc
                                                   )
        return new_meal

"""

class AddDishForm(forms.ModelForm):
    """
    """
    dish_name = forms.RegexField(regex=NAME_RE,
                                max_length=40,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Name"),
                                error_messages={'invalid': _('Dish Name must contain only letters, numbers, dots and underscores.')})
    dish_desc = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Desc"))



    class Meta:
        model = Dish
        fields=['dish_name',  'dish_desc', 'dish_type', 'photo']
