from django.conf.urls import url
from . import views
app_name = 'trip'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^log_out$', views.log_out, name='log_out'),
    url(r'^add_page$', views.add_page, name='add_page'),
    url(r'^add_trip$', views.add_trip, name='add_trip'),
    url(r'^join_trip/(?P<trip_id>\d+)$', views.join_trip, name='join_trip'),
    url(r'^view_trip/(?P<trip_id>\d+)$', views.view_trip, name='view_trip'),
]
