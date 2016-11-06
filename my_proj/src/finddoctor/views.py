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
import subprocess

import json


# Create your views here.
def process(request):
    text="wrong"
    z="1"
    specialities=[]
    doctordata=[]

    cur=connection.cursor()
    final=[]
    latlong=[]
    if request.method == 'POST':
        myform = DoctorForm(request.POST)
        #print ("****RR*****")
        #output=subprocess.check_call(['Rscript', '/home/admin-pc/Hospital-Home/sample.R'], shell=False)
        #print("****R***")
        if myform.is_valid():
            
            text=myform.cleaned_data['locality_text']
            selected_speciality=myform.cleaned_data['category']
            latlong=Geocoder.geocode(text+', Bangalore') 
            x=latlong[0].coordinates[0]
            y=latlong[0].coordinates[1]
            z=[x,y]

            #query="SELECT distinct dc.DoctorName,cll.ClinicName,Latitude,Lon,Address, 111.045* DEGREES(ACOS(COS(RADIANS(%s)) * COS(RADIANS(Latitude))* COS(RADIANS(%s) - RADIANS(Lon))+ SIN(RADIANS(%s))* SIN(RADIANS(Latitude)))) AS distance_in_km FROM clinic_lat_long as cll,doc_clinic as dc,clinic_add as ca where cll.ClinicName IN (SELECT dc.ClinicName from doc_clinic where DoctorName in (select DoctorName from doc_speciality where Speciality=%s)) and cll.ClinicName=dc.ClinicName and cll.ClinicName=ca.ClinicName ORDER BY distance_in_km LIMIT 15"
            """if(text):
                print("Hello")
                query2="select distinct dc.DoctorName,ds.Speciality,dc.ClinicName,ca.Address,cll.Latitude,cll.Lon from doc_speciality as ds,doc_clinic as dc,clinic_add as ca,clinic_lat_long as cll where (ds.DoctorName=dc.DoctorName AND dc.ClinicName=ca.ClinicName AND cll.ClinicName=dc.ClinicName AND ds.Speciality IN %s) LIMIT 15 "
                data=([selected_speciality])
                cur.execute(query2,data)
                results=cur.fetchall()
                print(results)
                for result in results:
                    final.append(str(result[4])+","+str(result[5]))
                    doctordata.append([result[0],result[2],result[3]])
                print(doctordata)
                cur.close()
                latlong=json.dumps(final)"""
                #return render(request, 'finddoctor/finddoctor.html', {'form':latlong,'doctordata':doctordata})


            if(text):
                query="SELECT D.DoctorName,D.ClinicName,Latitude,Lon,D.Address,111.045* DEGREES(ACOS(COS(RADIANS(latpoint)) * COS(RADIANS(Latitude))* COS(RADIANS(longpoint) - RADIANS(Lon))+ SIN(RADIANS(latpoint))* SIN(RADIANS(Latitude)))) AS distance_in_km FROM Doctors as D JOIN ((SELECT %s AS latpoint, %s AS longpoint) AS p) where D.ClinicName IN (SELECT ClinicName from doc_clinic where DoctorName in (select DoctorName from doc_speciality where Speciality=%s)) ORDER BY distance_in_km LIMIT 15"
                data=([x,y,selected_speciality])
                print (selected_speciality)
                cur.execute(query,data)
                results=cur.fetchall()
            #final=[]
                for result in results:
                    final.append(str(result[2])+","+str(result[3]))
                    doctordata.append([result[0],result[1],result[4]])
                print(final)
                print(doctordata)
            
                cur.close()
                latlong=json.dumps(final)

            else:
                print("Hello")
                query2="select distinct dc.DoctorName,ds.Speciality,dc.ClinicName,ca.Address,cll.Latitude,cll.Lon from doc_speciality as ds,doc_clinic as dc,clinic_add as ca,clinic_lat_long as cll where (ds.DoctorName=dc.DoctorName AND dc.ClinicName=ca.ClinicName AND cll.ClinicName=dc.ClinicName AND ds.Speciality=%s) LIMIT 15 "
        #query2="SELECT D.DoctorName,D.ClinicName,Latitude,Lon,D.Address FROM Doctors as D where D.ClinicName IN (SELECT ClinicName from doc_clinic where DoctorName in (select DoctorName from doc_speciality where Speciality=%s)) LIMIT 15"
                data=([selected_speciality])
                cur.execute(query2,data)
                results=cur.fetchall()
                print(results)
                for result in results:
                    final.append(str(result[4])+","+str(result[5]))
                    doctordata.append([result[0],result[2],result[3]])
                print(doctordata)
                cur.close()
                latlong=json.dumps(final)

    return render(request, 'finddoctor/finddoctor.html', {'form':latlong,'doctordata':doctordata})
    #del doctordata[:]
    

'''
def display(request):
    cur=connection.cursor()
    query1="SELECT distinct Speciality from doc_speciality"
    cur.execute(query1)
    specialities=cur.fetchall()
    cur.close()
    return render(request, 'finddoctor/finddoctor.html', {'specialities':specialities})
'''