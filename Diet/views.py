# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('home.html')
    context = {    }
    return HttpResponse(template.render(context,request))

def Dietplan(request):
    name = request.POST.get("food_hbt")
    if name == 'Veg':
        template = loader.get_template('lowfatvegan.html')
    else:
        template = loader.get_template('lchf.html')
    context = {    }
    return HttpResponse(template.render(context,request))


