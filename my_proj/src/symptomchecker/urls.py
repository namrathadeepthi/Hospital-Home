from django.conf.urls import url
from django.views.generic import TemplateView
#from django.views.generic.edit import ProcessFormView
from . import views

urlpatterns = [
    url(r'^process/',views.process,name="process"),
    url(r'^', TemplateView.as_view(template_name= "symptomchecker/symptomchecker.html"), name="symptomchecker"),
    ]