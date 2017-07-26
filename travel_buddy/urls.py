
from django.conf.urls import url, include

urlpatterns = [
    url(r'^main', include('apps.user_app.urls', namespace='user')),
    url(r'^', include('apps.trip_app.urls', namespace='trip')),
]
