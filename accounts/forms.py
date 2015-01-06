__author__ = 'young'

from django import forms
from userena.forms import SignupForm

class SignupFormExtra(SignupForm):
    firstname = forms.CharField(label=(u'First name'),
                                 max_length=30,
                                 required=False)

    lastname = forms.CharField(label=(u'Last name'),
                                max_length=30,
                                required=False)

    def save(self):
        """
        Override the save method to save the first and last name to the user
        field.

        """
        # Original save method returns the user
        user = super(SignupFormExtra, self).save()

        # Get the profile, the `save` method above creates a profile for each
        # user because it calls the manager method `create_user`.
        # See: https://github.com/bread-and-pepper/django-userena/blob/master/userena/managers.py#L65
        user_profile = user.get_profile()

        # Be sure that you have validated these fields with `clean_` methods.
        # Garbage in, garbage out.
        user_profile.firstname = self.cleaned_data['firstname']
        user_profile.lastname = self.cleaned_data['lastname']
        user_profile.save()

        # Return the user, not the profile!
        return user