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
from .forms import SymptomForm
from django.views.generic import TemplateView
#from django.views.generic.edit import ProcessFormView
import logging
from nltk.corpus import stopwords
#from app.models import 
from django.db import connection,transaction
from collections import OrderedDict
# Create your views here.


#conn1=mysql.connector.connect(user='root', password='1234',database='hospitalHome')   
    #form_class = forms.SymptomForm

cur=connection.cursor()

def fillDoctors(key_bodyloc,proportion):
    bodyloc_specialty_query="select distinct Speciality from body_speciality where body_location in (%s) "
    #cur.execute(bodyloc_specialty_query)
    data1=([key_bodyloc])
    #print(bodyloc_specialty_query,data)
    cur.execute(bodyloc_specialty_query,data1)
    results=cur.fetchall()
    specialities=[x[0] for x in results]
    #condition=""
    #for speciality in specialities:
     #   print(str(speciality))
      #  y=speciality.strip()
       # condition=condition+"'%"+y+"%'"+" or Speciality like "
    #print(speciality)
    #print(condition)
    #like = "Speciality LIKE %%%s%%"
    #condition = like + (" OR {}".format(like)) * len(specialities-1)
    #specialty_doctors_query="select DoctorName,Speciality,ClinicName from Doctors where Speciality like %s limit %s"
    #query = "select DoctorName,Speciality,ClinicName from Doctors where %s LIMIT %s ",(condition,proportion)
    #query2="select DoctorName,Speciality,ClinicName from Doctors where Speciality IN %s LIMIT %s "
    query2="select dc.DoctorName,ds.Speciality,dc.ClinicName,ca.Address from doc_speciality as ds,doc_clinic as dc,clinic_add as ca where (ds.DoctorName=dc.DoctorName AND dc.ClinicName=ca.ClinicName AND ds.Speciality IN %s) LIMIT %s "
    #data2=([condition,proportion])
    #print(specialty_doctors_query)
    #cur.execute(specialty_doctors_query,data2)
    #cur.execute(query,specialities)
    data3=([specialities,proportion])
    #print(data3)
    cur.execute(query2,data3)
    final=cur.fetchall()
    #print(final)
    #print(results)
    print(final)
    return final

def process(request):
    text="wrong"
    rows=[]
    diseasetable=[]
    doctors=[]
    if request.method == 'POST':
        myform = SymptomForm(request.POST)
        if myform.is_valid():
            text=myform.cleaned_data['symptom_text']
            stop = set(stopwords.words('english'))
            important_words=[]
            for i in text.lower().split():
              if i not in stop:
                important_words.append(i)

            for i in range(0,len(important_words)):
                print (important_words[i])

            #cur=conn.cursor()
           
            query="select distinct D.Disease as disease, D.BodyLocation as body_location, X.rank as rank from DiseaseSymptoms D join ( select T.disease_id, sum(T.norm_tfidf) as rank from (select disease_id, norm_tfidf from norm_symptoms_tfidf where term in %s )T group by T.disease_id order by sum(T.norm_tfidf) desc) X on X.disease_id=D.DiseaseID order by X.rank desc limit 10" % repr(important_words).replace('[','(').replace(']',')') 
            cur.execute(query)
            #transaction.commit_unless_managed()
            rows = cur.fetchall()
            #print(type(row))
            #print (rows)
            for row in rows:
                diseasetable.append([row[0],row[1],row[2]])

            #print("disease table ")
            print(diseasetable)
            bodyloc={}
            total_body_locs=0
            for i in range(0,len(rows)):
                bl=diseasetable[i][1]
                print(bl)
                if bl==None:
                    break
                if bodyloc.get(bl):
                    bodyloc[bl]=bodyloc[bl]+1
                else:
                    bodyloc[bl]=1

                total_body_locs=total_body_locs+1

            proportion=0
            temp=sorted(bodyloc.items(), key=lambda x: (-x[1], x[0]))
            bodyloc = dict(temp)
            print(temp)
            #print(total_body_locs)
            #print(bodyloc)
            #for key in bodyloc:
             #   proportion=int(float(bodyloc[key])/total_body_locs*10)
                #print(proportion)
              #  doctors=fillDoctors(key,proportion)

            for item in temp:
                proportion=int(float(item[1])/total_body_locs*10)
                #print(proportion)
                doctors.append(fillDoctors(item[0],proportion))
            #cur.close()
    return render(request, 'symptomchecker/symptomchecker.html', {'rows':diseasetable,'form':text,'doctors':doctors})


   




