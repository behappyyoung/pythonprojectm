from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

USER_CHOICES = (
        ('member', _('Member')),
        ('chef', _('Chef')),
        ('Mighty', _('Both')),
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

##    firstname = models.CharField(_('firstname'), max_length=15, default='', help_text=_('first name'))
##    lastname = models.CharField(_('lastname'), max_length=15, default='', help_text=_('last name'))
