from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^person$', views.formSubmit),
    url(r'^people$', views.people),
    url(r'^show/(?P<id>\d+)$', views.show),
]
