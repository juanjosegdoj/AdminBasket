from django.conf.urls import url

from apps.partido.views import index_partido

urlpatterns = [
    url(r'^', index_partido),
]