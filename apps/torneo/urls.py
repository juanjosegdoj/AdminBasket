from django.conf.urls import url, include

from apps.torneo.views import MainTorneoView, FormTorneoView, ListarView

urlpatterns = [
   url(r'^$', MainTorneoView.as_view()),
   url(r'^nuevo$', FormTorneoView.as_view()),
   url(r'^listado$', ListarView.as_view())
]