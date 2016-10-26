from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import symptomchecker.urls
import finddoctor.urls
import medicinepredictor.urls
import healthtips.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^symptomchecker/', include(symptomchecker.urls, namespace='symptomchecker')),
    url(r'^finddoctor/', include(finddoctor.urls, namespace='finddoctor')),
    url(r'^medicinepredictor/', include(medicinepredictor.urls, namespace='medicinepredictor')),
    url(r'^healthtips/', include(healthtips.urls, namespace='healthtips'))
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
