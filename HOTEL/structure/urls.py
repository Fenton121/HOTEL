# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

#from structure.views import *  # But I want to see all classes
from structure.views import HouseList

urlpatterns = [
    url(r'^houses/$', HouseList.as_view(), name='house_list'),
]
