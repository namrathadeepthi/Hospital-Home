from django import forms

CATEGORIES = (  
    ('Cardiac Surgery', 'Cardiac Surgery'),
    ('Cardiology', 'Cardiology'),
    ('Physiotherapy', 'Physiotherapy'),
    ('Orthopedic Surgery', 'Orthopedic Surgery'),
    ('Neurology', 'Neurology'),
    ('Neuro Surgery', 'Neuro Surgery'),
    ('Psychiatry', 'Psychiatry'),
    ('Psychology', 'Psychology'),
    ('Gastroenterology', 'Gastroenterology'),
    ('Colon and Rectal Surgery', 'Colon and Rectal Surgery'),
    ('Otolaryngology (ENT)', 'Otolaryngology (ENT)'),
    ('Endocrinology', 'Endocrinology'),
    ('Ophthalmology (Eye Specialist)', 'Ophthalmology (Eye Specialist)'),
    ('General Surgery', 'General Surgery'),
    ('Urology', 'Urology'),
    ('Chest physician', 'Chest physician'),
    ('Dentistry', 'Dentistry'),
    ('Dermatology', 'Dermatology'),
    ('Cosmetology', 'Cosmetology'),
    ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'),
    ('Sexology', 'Sexology'),
    
)
class DoctorForm(forms.Form):
    locality_text = forms.CharField(max_length=1000, required=False)
    category = forms.ChoiceField(choices=CATEGORIES, required=True )