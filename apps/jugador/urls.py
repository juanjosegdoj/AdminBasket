from django.conf.urls import url, include
from django.urls import path
from .views import MainView, JugadorFormView, JugadorList

urlpatterns = [
    path('', MainView.as_view(), name='index'),
 	path('nuevo', JugadorFormView.as_view(), name='jugador_crear'),
 	path('listado', JugadorList.sendRender, name="jugador_listar"),
]
