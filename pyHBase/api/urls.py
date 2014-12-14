#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#
__author__ = 'liuzheng'
from django.conf.urls import patterns, url
# from views import *

urlpatterns = patterns('api.views',
       url(r'^$', 'index'),
       url(r'^list$', 'list'),
       url(r'^login', 'Login'),
       url(r'^logout', 'Logout'),
)
