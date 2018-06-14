from django.conf.urls import url
from django.urls import path
from apps.partido.views import index_partido, detail

urlpatterns = [
    path('', index_partido),
    path('<int:partido_id>', detail, name = 'detailPartido')
    #path('<int:partido_id>', detail, name = 'detailPartido')
]
