from django import forms

class SymptomForm(forms.Form):
    symptom_text = forms.CharField(max_length=100)