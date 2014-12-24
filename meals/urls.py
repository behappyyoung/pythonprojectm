from django.conf.urls import patterns, url

from meals import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^dish/(?P<pk>\d+)/$', views.DishView.as_view(), name='dish'),
##    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
##    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)