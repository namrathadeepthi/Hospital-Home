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

from django.views.generic import TemplateView
from django.contrib.sessions.models import Session
#from django.views.generic.edit import ProcessFormView
import logging
from nltk.corpus import stopwords
#from app.models import 
from django.db import connection,transaction
from collections import OrderedDict
from .forms import HeartForm
import csv
import subprocess
# Create your views here.


def process(request):
    text="wrong"
    z="1"
    output=0   
    final=[]
    if request.method == 'POST':
        
        myform = HeartForm(request.POST)
        print("hi")
        #print ("****RR*****")
        #output=subprocess.check_call(['Rscript', '/home/admin-pc/Hospital-Home/sample.R'], shell=False)
        #print("****R***")
        if myform.is_valid():
            
            print("hello")
            age=myform.cleaned_data['age']
            sex=myform.cleaned_data['gender']
            cp=myform.cleaned_data['chestpaintype']
            bp=myform.cleaned_data['bp']
            chol=myform.cleaned_data['chol']
            bsugar=myform.cleaned_data['bsugar']
            thalach=myform.cleaned_data['thalach']
            exang=myform.cleaned_data['exang']
            oldpeak=myform.cleaned_data['oldpeak']
            ca=myform.cleaned_data['ca']
            restecg=myform.cleaned_data['restecg']
            slope=myform.cleaned_data['slope']
            out_file=open('/home/admin-pc/Hospital-Home/testHeart.csv','w')
            file=csv.writer(out_file)

            final=[age,sex,cp,bp,chol,bsugar,restecg,thalach,exang,oldpeak,slope,ca]
            print(final)
            file.writerow(final)
            out_file.close()
            print ("****RR*****")
            output=subprocess.check_output(['Rscript', '/home/admin-pc/Hospital-Home/sample.R'], shell=False)
            print("****R***")

    return render(request, 'medicinepredictor/medicinepredictor.html', {'form':final,'output':output})
