#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, ListView, TemplateView, DetailView
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .forms import EquipoForm
from .models import Equipo

def detailView(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk = equipo_id)
    context = { 'equipo': equipo }
    template = loader.get_template('equipo/detalle_equipo.html')
    return HttpResponse(template.render(context, request))

def opcionarEquipos(request):
    equipos_list = Equipo.objects.order_by('nombre')
    template = loader.get_template('equipo/seleccionar_equipo.html')
    context = {
        'equipo_list': equipos_list,
    }
    return HttpResponse(template.render(context, request))

def equiposEnTexto(request):
    equipos_list = Equipo.objects.order_by('nombre')
    output = ', '.join([q.nombre for q in equipos_list])
    output = "Estos son los equipos del torneo: " + output
    return HttpResponse(output)

class EquipoView(FormView):
    template_name = 'equipo/equipo_form.html'
    form_class = EquipoForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(EquipoView, self).form_valid(form)

    def form_invalid(self, form):
        return super(EquipoView, self).form_invalid(form)

class ListarView(ListView):
    variablePub = 'Hola Soy Juanjo'
    model = Equipo
    template_name = 'equipo/list_equipo.html'
	#contexto_object_name = 'equipos'
