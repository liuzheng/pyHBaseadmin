#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#
__author__ = 'liuzheng'
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render_to_response('api_guide.html')

def list(request):
    Rjson = json.dumps({'list':'llll'})
    return HttpResponse(Rjson)