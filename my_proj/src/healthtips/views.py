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
import time
from datetime import datetime
from threading import Timer
from bs4 import BeautifulSoup
import urllib3

import requests
import re

# Create your views here.
def display(request):
    x=datetime.today()
    y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
    delta_t=y-x

    secs=delta_t.seconds+1
    t = Timer(secs,scrape)
    t.start()
    '''
    cur=connection.cursor()
    final=[]
    url='http://www.eatright.org/search?themes=hh&categories=dac'
    

    page=requests.get(url)

    bs=BeautifulSoup(page.text)

    data=[]
    div_items= bs.find_all('div',attrs={'class':'content'})
    for div in div_items:
        health_text=""
        a_name=div.find('a') 
        health_topic=a_name.text
        print(health_topic)
        url1=a_name['href']
        try:
            bs1=BeautifulSoup((requests.get(url1)).text)
        except:
            continue
        p_items= bs1.find_all('p')
        p_items= p_items[:-3]
        for p in p_items:
            health=p.text
            health= health.replace('\n', ' ').replace('\r', '')
            health_text=health_text+" "+health
        insert_query="insert into healthNews values(%s,%s)",(health_topic,health_text)
        data=([health_topic,health_text])
        cur.execute(*insert_query)
        cur.execute('commit')
    '''
    return render(request, 'healthtips/healthtips.html')

def scrape():
    cur=connection.cursor()
    final=[]
    url='http://www.eatright.org/search?themes=hh&categories=dac'
    

    page=requests.get(url)

    bs=BeautifulSoup(page.text)

    data=[]
    div_items= bs.find_all('div',attrs={'class':'content'})
    for div in div_items:
        health_text=""
        a_name=div.find('a') 
        health_topic=a_name.text
        print(health_topic)
        url1=a_name['href']
        try:
            bs1=BeautifulSoup((requests.get(url1)).text)
        except:
            continue
        p_items= bs1.find_all('p')
        p_items= p_items[:-3]
        for p in p_items:
            health=p.text
            health= health.replace('\n', ' ').replace('\r', '')
            health_text=health_text+" "+health
        insert_query="insert into healthNews values(%s,%s)",(health_topic,health_text)
        data=([health_topic,health_text])
        cur.execute(*insert_query)
        cur.execute('commit')