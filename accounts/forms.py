__author__ = 'young'

from django import forms
from userena.forms import SignupForm



class SignupFormExtra(SignupForm):
    first_name = forms.CharField(label=(u'First name'),
                                 max_length=30,
                                 required=True)

    last_name = forms.CharField(label=(u'Last name'),
                                max_length=30,
                                required=True)

    address = forms.CharField(label=(u'Address'),
                                max_length=100,
                                required=True)
    zipcode = forms.CharField(label=(u'Zipcode'),
                                max_length=10,
                                required=True)
    phone = forms.CharField(label=(u'Phone Number'),
                                max_length=10,
                                required=True)


    USER_CHOICES = (('member', ('Member')),        ('chef', ('Chef')),        ('mighty', ('Both')),)

    usertype = forms.ChoiceField(label=(u'User Type'),
                                choices=USER_CHOICES,
                                required=True)
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
        ##user_profile = user.get_profile()
        user_profile = user.userprofile

        # Be sure that you have validated these fields with `clean_` methods.
        # Garbage in, garbage out.
        user_profile.firstname = self.cleaned_data['first_name']
        user_profile.lastname = self.cleaned_data['last_name']
        user_profile.usertype = self.cleaned_data['usertype']
        user_profile.address = self.cleaned_data['address']
        user_profile.zipcode = self.cleaned_data['zipcode']
        user_profile.phone = self.cleaned_data['phone']
        user_profile.save()

        # Return the user, not the profile!
        return user