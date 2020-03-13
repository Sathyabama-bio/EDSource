# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from Diet import Patientform


def Patient(request):
    form = Patientform.Patient()
    return render(request,'home1.html',{'form': form})

def PatientHistory(request):
    form = Patientform.Patient()
    return render(request,'home2.html',{'form': form})

def Dietplan(request):
    name = request.POST.get("food_hbt")
    if name == 'Veg':
        form = Patientform.PatientHistory()
        return render(request,'lowfatvegan1.html',{'form': form})
    else:
        form = Patientform.PatientHistory()
        return render(request,'lchf1.html',{'form': form})
   # context = {    }
   # return HttpResponse(template.render(context,request))


