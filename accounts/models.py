from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

USER_CHOICES = (
        ('member', _('Member')),
        ('chef', _('Chef')),
        ('mighty', _('Both')),
)


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5),
    usertype = models.CharField(_('usertype'),
                                max_length=15,
                               choices=USER_CHOICES,
                               default='member',
                               help_text=_('Choose User Type.'))

    address = models.CharField(_('address'), max_length=150, default='', help_text=_('Address'))
    phone = models.CharField(_('phone'), max_length=12, default='', help_text=_('Phone Number'))
    zipcode = models.CharField(_('zipcode'), max_length=10, default='', help_text=_('Zipcode'))
##    lastname = models.CharField(_('lastname'), max_length=15, default='', help_text=_('last name'))

    def get_chef_profiles(self, user=None):
        """
        Returns all the visible profiles available to this user.

        For now keeps it simple by just applying the cases when a user is not
        active, a user has it's profile closed to everyone or a user only
        allows registered users to view their profile.

        :param user:
            A Django :class:`User` instance.

        :return:
            All profiles that are visible to this user.

        """
        profiles = self.all()

        filter_kwargs = {'usertype': 'chef'}

        profiles = profiles.filter(**filter_kwargs)
        return profiles
