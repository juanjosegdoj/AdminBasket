from django.conf.urls import url, include

from apps.jugador.views import *

urlpatterns = [
    url(r'^$', MainView.as_view(), name='index'),
 	url(r'^nuevo$', JugadorFormView.as_view(), name='jugador_crear'),
 	url(r'^creado$', jugadorCreado, name="creado"),
 	url(r'^NOcreado$', jugadorNOCreado, name="NOcreado"),
 	url(r'^listar$', JugadorList.sendRender, name="jugador_listar"),
]