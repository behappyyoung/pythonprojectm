from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView

from djangotest import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ##url(r'^$', include('polls.urls')),
    ##url(r'^$', RedirectView.as_view(url='/accounts/')),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^static/(.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)polls/', include('polls.urls', namespace="polls")),
    url(r'^(?i)meals/', include('meals.urls', namespace="meals")),
    url(r'^(?i)accounts/', include('accounts.urls')),

    ## Added  for mugshots url
     url(r'^(?i)images/(mugshots/.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
     url(r'^(?i)images/(meals/.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
##    url(r'^(?i)accounts/[\.\w-]+/(mugshots/.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
##    url(r'^(?i)accounts/(mugshots/.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    ## messages
    url(r'^(?i)messages/', include('django_messages.urls')),
)
