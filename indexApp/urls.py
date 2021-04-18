#coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^loginCheck$',views.loginCheck),
    url(r'^mainIndex$',views.mainIndex),
    url(r'^mainShow$',views.mainShow),
    url(r'^logout$',views.logout)
]