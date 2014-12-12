#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#
__author__ = 'liuzheng'

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import forms
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

# Create your views here.
def index(request):
     return render_to_response('index.html')

