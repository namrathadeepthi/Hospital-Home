from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import DoctorForm
from django.views.generic import TemplateView
#from django.views.generic.edit import ProcessFormView
import logging
from nltk.corpus import stopwords
#from app.models import 
from django.db import connection,transaction
from collections import OrderedDict
from pygeocoder import Geocoder

# Create your views here.
def process(request):
    text="wrong"
    z="1"
    specialities=[]
    cur=connection.cursor()
    if request.method == 'POST':
        myform = DoctorForm(request.POST)
        if myform.is_valid():
            
            text=myform.cleaned_data['locality_text']
            selected_speciality=myform.cleaned_data['category']
            latlong=Geocoder.geocode(text+', Bangalore') 
            x=latlong[0].coordinates[0]
            y=latlong[0].coordinates[1]
            z=[x,y]
            query="SELECT ClinicName, Latitude, Lon, 111.045* DEGREES(ACOS(COS(RADIANS(latpoint)) * COS(RADIANS(Latitude))* COS(RADIANS(longpoint) - RADIANS(Lon))+ SIN(RADIANS(latpoint))* SIN(RADIANS(Latitude)))) AS distance_in_km FROM clinic_lat_long JOIN ((SELECT %s AS latpoint, %s AS longpoint) AS p) where ClinicName IN (SELECT distinct ClinicName from doc_clinic where DoctorName in (select DoctorName from doc_speciality where Speciality=%s)) ORDER BY distance_in_km LIMIT 15"
            data=([x,y,selected_speciality])
            print (selected_speciality)
            cur.execute(query,data)
            results=cur.fetchall()
            print(results)
            cur.close()
    return render(request, 'finddoctor/finddoctor.html', {'form':z})

'''
def display(request):
    cur=connection.cursor()
    query1="SELECT distinct Speciality from doc_speciality"
    cur.execute(query1)
    specialities=cur.fetchall()
    cur.close()
    return render(request, 'finddoctor/finddoctor.html', {'specialities':specialities})
'''
