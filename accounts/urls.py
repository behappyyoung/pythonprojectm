__author__ = 'young'

from django.conf.urls import patterns, include, url
from accounts import views
from django.contrib.auth.decorators import login_required
from accounts.forms import SignupFormExtra

urlpatterns = patterns('',

    url(r'^$', login_required(views.ProfileListView.as_view()), name='profile_list'),
    url(r'^(?i)signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
    url(r'^(?i)providers/$', views.ProviderListView.as_view(), name='provider_list'),
    url(r'^', include('userena.urls')),
)
