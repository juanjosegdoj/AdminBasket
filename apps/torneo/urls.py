from django.conf.urls import url, include
from django.urls import path
from apps.torneo.views import MainTorneoView, FormTorneoView, ListarView

urlpatterns = [
   path('', MainTorneoView.as_view()),
   path('nuevo', FormTorneoView.as_view()),
   path('listado', ListarView.as_view())
]
