import mysql.connector
from nltk.corpus import stopwords
import re
from math import log

conn1=mysql.connector.connect(user='root', password='1234',database='hospitalHome')
conn2=mysql.connector.connect(user='root', password='1234',database='hospitalHome')

stop = stopwords.words('english')

def term_freq(disease_id, symptoms):
    global conn2
    global stop
    
    termfreq_map={}
    symptoms=re.sub('[.\(\)|,!:-]',' ', symptoms)
    terms=symptoms.lower().split(' ')    
    for i in range(len(terms)):
        terms[i]=terms[i].strip()
        if terms[i] not in stop:  
            if terms[i] in termfreq_map:
                termfreq_map[terms[i]]+=1
            else:
                termfreq_map[terms[i]]=1
    
    query = ("insert into symptoms_tfidf(disease_id, term, term_freq) values(%s, %s, %s)")
    cur=conn2.cursor()
    for term in termfreq_map.keys():
        if term !="":
            cur.execute(query,(disease_id,term,termfreq_map[term]))            
    
    cur.execute('commit')
    

def compute_termfreq():
    global conn1
    cur=conn1.cursor()
    query = ("select distinct DiseaseID, Symptoms from DiseaseSymptoms")
    cur.execute(query)
    for disease_id, symptoms in cur:
        term_freq(disease_id, symptoms)

    cur.close()

def getDocCount():
    global conn1    
    cur=conn1.cursor()
    query = ("select count(DiseaseID) from DiseaseSymptoms")
    cur.execute(query)
    N=cur.fetchone()
    cur.close()
    return N
    
def getTermDocFreq(termdocfreq_map):
    global conn1    
    cur=conn1.cursor()    
    query = ("select term, count(*) as cnt from symptoms_tfidf group by term")
    cur.execute(query)
    
    for term, cnt in cur:
        termdocfreq_map[term]=cnt
    cur.close()        



def compute_tfidf():    
    global conn1
    global conn2
    
    N=getDocCount()[0]
    print(N)
    termdocfreq_map={}  
    getTermDocFreq(termdocfreq_map)
    cur1=conn1.cursor()
    query = ("select disease_id, term, term_freq from symptoms_tfidf order by disease_id, term")
    cur1.execute(query)
    values=[]
    fp=open('tfidf.txt','w')
    for disease_id, term, term_freq in cur1:
        n=termdocfreq_map[term]
        idf=log(N/n)
        tf=1+log(term_freq)
        
        tfidf=tf*idf
        #print (tfidf)
        #text='update symptoms_tfidf set norm_tfidf='+str(tfidf)+' where disease_id='+str(disease_id)+' and term = '+ term + '\n' 
        #conn2.cursor().execute("update symptoms_tfidf set norm_tfidf = %s where disease_id = %s and term = %s",(tfidf,disease_id,term))	
	#cur2=conn2.cursor()
	#cur2.execute(query)
        values.append([tfidf,disease_id,term])    
        #fp.write(text)
    fp.flush()
  
    fp.close()
    cur1.close()
    cur2=conn1.cursor()
    """with open('tfidf.txt','r') as f:
        for line in f:
            query=line
            conn1.cursor().execute(query)
            print(query)
            break"""
    for item in values:
        #print(item)
        query="update symptoms_tfidf set norm_tfidf = %s where disease_id = %s and term = %s;",(item[0],item[1],item[2])
        #print(query)
        cur2.execute(*query)
        cur2.execute('commit')
    cur2.close()

def normalize_tfidf():    
    global conn1
    
    cur1=conn1.cursor()
    query = ("select disease_id, sqrt(sum(norm_tfidf*norm_tfidf)) from symptoms_tfidf group by disease_id")
    cur1.execute(query)
    
    docSS_map={}  
    for disease_id, ss_tfidf in cur1:
        docSS_map[disease_id]=ss_tfidf
    cur1.close()
    
    fp=open('norm_tfidf.csv','w')
    cur1=conn1.cursor()
    query = ("select disease_id, term, norm_tfidf, term_freq from symptoms_tfidf order by disease_id")
    cur1.execute(query)
    
    for disease_id, term, tfidf, term_freq in cur1:
        norm_tfidf=tfidf/docSS_map[disease_id]
        text=str(disease_id)+','+term+','+str(norm_tfidf)+','+str(term_freq)+'\n'
        fp.write(text)
        fp.flush()

    fp.close()
    cur1.close()
    


#compute_termfreq()
compute_tfidf()
normalize_tfidf()
conn1.close()
conn2.close()

