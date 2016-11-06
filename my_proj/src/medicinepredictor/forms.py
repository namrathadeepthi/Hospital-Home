from django import forms 
from django.forms import ModelForm, CharField, TextInput , ChoiceField


GENDER=[('1','male'),
         ('0','female')]

CHEST = [
    ('1', 'typicalAngina'),
    ('2', 'atypicalAngina'),
    ('3', 'nonAnginalPain'),
    ('4', 'asymptomatic')]

RESTECG = [
    ('0', 'normal'),
    ('1', 'having ST-T wave abnormality'),
    ('2', 'non-showing probable or definite left ventricular hypertrophy ')]

SLOPE = [
    ('1', 'upsloping'),
    ('2', 'flat'),
    ('3', 'downsloping')
    ]
    

EXANG=[('1','yes'),
         ('0','no')]  
   
class HeartForm(forms.Form):
    age = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    
    gender= forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    chestpaintype = forms.ChoiceField(choices=CHEST, widget=forms.RadioSelect())
    bp = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    chol = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    bsugar= forms.CharField( widget=TextInput(attrs={'type':'number'}))
    thalach = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    #exang= forms.CharField( widget=TextInput(attrs={'type':'number'}))
    exang=forms.ChoiceField(choices=EXANG, widget=forms.RadioSelect())
    oldpeak = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    ca = forms.CharField( widget=TextInput(attrs={'type':'number'}))
    restecg= forms.ChoiceField(choices=RESTECG, widget=forms.RadioSelect())
    slope= forms.ChoiceField(choices=SLOPE, widget=forms.RadioSelect())
    