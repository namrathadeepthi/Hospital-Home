from bs4 import BeautifulSoup
import urllib3
import urllib2
import requests
import re
import csv

url='http://www.nlm.nih.gov/medlineplus/healthtopics.html'
out_file=open('hh.csv','w')
file=csv.writer(out_file)

#page=urllib2.urlopen(url)
page=requests.get(url)

bs=BeautifulSoup(page.text)
list_items = bs.find_all('li',{'type':'bodymaps'})
uid=1;
dlist=[]
for item in list_items:
    body_loc=item.a.text
    url1 = item.a['href']
    try:
        bs1=BeautifulSoup((requests.get(url1)).text)
    except:
        continue
    #for elem in bs1(text=re.compile(r'^Blood, Heart and Circulation Topics$')):
    #	print 1
    slist = bs1.find('h2',text=body_loc+" Topics")
    #print slist.parent
    atags=slist.parent.find_all('a')
    
    for atag in atags:
        disease=atag.text
        url2 = atag['href']
        try:    
            bs2=BeautifulSoup((requests.get(url2)).text)
        except:
            continue
        divs = bs2.find_all('div')
	desc='"'        
	for div in divs:
            if div.has_attr('id'):
                if div['id']=='topic-summary':
                    desc=div.get_text().replace('"','').replace('\n','|')
                    break
        
        out_str='"'+str(uid)+'","' + body_loc+'","' + disease+'","' + desc+'"\n'
        uid+=1
        print out_str
        disease=[str(uid),body_loc,disease,desc]
        dlist.append(disease)
      # file.writerow(disease.encode('utf-8'))
        #out_file.write(out_str)
	
for row in dlist:
	file.writerow([item.encode('utf-8') for item in row])       
out_file.close()
