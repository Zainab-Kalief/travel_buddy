from django.conf.urls import url
from . import views
app_name = 'user'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^log_in$', views.log_in, name='log_in'),
]
