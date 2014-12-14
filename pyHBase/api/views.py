#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#
__author__ = 'liuzheng'
from django.shortcuts import render
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render_to_response('api_guide.html')


def list(request):
    Rjson = json.dumps({'list': 'llll'})
    return HttpResponse(Rjson)

@csrf_exempt
def Login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/DJadmin/')
        else:
            return HttpResponseRedirect('/admin/')
    except:
        return HttpResponseRedirect('/admin/')

def Logout(request):
    logout(request)

