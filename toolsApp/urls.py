#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^portRetu$',views.portRetu),
    url(r'^portReady$',views.portReady),
    url(r'^portStart$',views.portStart),
    url(r'^dirRetu$',views.dirRetu),
    url(r'^dirReady$',views.dirReady),
    url(r'^dirStart$',views.dirStart)
]