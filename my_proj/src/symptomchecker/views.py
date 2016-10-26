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
import mysql.connector
#from app.models import 
from django.db import connection,transaction
# Create your views here.


#conn1=mysql.connector.connect(user='root', password='1234',database='hospitalHome')   
    #form_class = forms.SymptomForm
def process(request):
    text="wrong"
    row=[]
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
            cur=connection.cursor()
            query="select distinct D.Disease as disease, D.BodyLocation as body_location, X.rank as rank from DiseaseSymptoms D join ( select T.disease_id, sum(T.norm_tfidf) as rank from (select disease_id, norm_tfidf from symptoms_tfidf where term in %s )T group by T.disease_id order by sum(T.norm_tfidf) desc) X on X.disease_id=D.DiseaseID order by X.rank desc limit 10" % repr(important_words).replace('[','(').replace(']',')') 
            cur.execute(query)
            #transaction.commit_unless_managed()
            row = cur.fetchall()
            print (row)
            cur.close()
    return render(request, 'symptomchecker/symptomchecker.html', {'form':text}, {'results': row })
