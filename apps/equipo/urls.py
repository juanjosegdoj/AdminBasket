from django.conf.urls import url
from .views import EquipoView, ListarView

urlpatterns = [
    url(r'^$', EquipoView.as_view()),
    url(r'^nuevo$', EquipoView.as_view()),
    url(r'^listado$', ListarView.as_view()),
]