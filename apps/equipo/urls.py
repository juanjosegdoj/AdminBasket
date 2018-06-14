from django.conf.urls import url
from django.urls import path
from .views import EquipoView, ListarView, detailView, equiposEnTexto, opcionarEquipos

app_name = 'equipo' # Para crear 'espacio de nombres', # https://docs.djangoproject.com/es/2.0/intro/tutorial03/
# sin esta variable no funciona la parte del sistema de plantillas {% url %}

urlpatterns = [
    path('', EquipoView.as_view()),
    path('nuevo', EquipoView.as_view(), name="nuevoEq"),
    path('listado', ListarView.as_view(), name= "listadoEq"),
    path('<int:equipo_id>', detailView, name='detail'),
    path('equiposText', equiposEnTexto, name='equiposEnTexto'),
    path('opcionarEquipos', opcionarEquipos, name='opcionarEquipos')
]
