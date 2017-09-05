from django.conf.urls import url,include
from django.contrib import admin
from Proyeccion.views import Logear
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Logear.as_view()),
    
    url(r'^Proyeccion/', include("Proyeccion.urls")),
]