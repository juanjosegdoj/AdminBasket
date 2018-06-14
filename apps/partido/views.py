from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Partido

def detail(request, partido_id):
    partido = get_object_or_404(Partido, pk = partido_id)
    context = { 'partido': partido , 'partido_id':partido_id}
    template = loader.get_template('partido/detalle_partido.html')
    return HttpResponse(template.render(context, request))

def index_partido(request):
	return HttpResponse("Estoy en views de la app PARTIDO")

def ingresoResultados(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk = equipo_id)
    context = { 'equipo': equipo ,
				'error_message' : 'Algo pasó papá' }
    template = loader.get_template('partido/ingresoResultadoPartido.html')
    return HttpResponse(template.render(context, request))
