# encoding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vulRetu$', views.vulRetu),
    url(r'^vulcheck_input$', views.vulcheck_input),
    url(r'^vulstart$', views.vulstart),
    url(r'^index$',views.index),


    ]
