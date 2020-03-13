# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Patient(models.Model):
    fname = models.CharField(max_length=25)
    mname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    sex = models.CharField(max_length=10)
    dob = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phonenumber = models.IntegerField()

class PatientHistory(models.Model):
    diabetes = models.CharField(max_length=25)
    diabetes_long = models.CharField(max_length=25)
    hba1c = models.FloatField()
    fasting = models.FloatField()
    pp = models.FloatField()
    familyhistory = models.CharField(max_length=25)
    hypertension = models.CharField(max_length=25)
    hypertension_long = models.CharField(max_length=25)
    obesity = models.CharField(max_length=25)
    obesity_long = models.CharField(max_length=25)
    pcod = models.CharField(max_length=25)
    pcod_long = models.CharField(max_length=25)
    thyroid = models.CharField(max_length=25)
    thyroid_long = models.CharField(max_length=25)
    heartdiease = models.CharField(max_length=25)
    heartdisease_long = models.CharField(max_length=25)
    liverdisease = models.CharField(max_length=25)
    liverdisease_long = models.CharField(max_length=25)
    kidney = models.CharField(max_length=25)
    kidney_long = models.CharField(max_length=25)
    currentmed = models.CharField(max_length=25)
    foodhabit = models.CharField(max_length=25)



