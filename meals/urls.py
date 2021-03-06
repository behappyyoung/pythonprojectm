from django.conf.urls import patterns, url

from meals import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?i)dishes$', views.DishListView.as_view(), name='dish_list'),
    url(r'^(?i)dish/(?P<pk>\d+)/$', views.DishView.as_view(), name='dish'),
    url(r'^(?P<username>[\@\.\w-]+)/$',views.MyMeals.as_view(), name='meals_mymeal'),
    url(r'^(?i)addmeal$',  views.addmeal, name='meal_addmeal'),
##    url(r'^(?i)adddish$',  views.adddish, name='meal_adddish'),
    url(r'^(?i)adddish$',  views.AddDish, name='adddish'),
##    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
##    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)