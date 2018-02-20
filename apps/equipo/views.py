from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, ListView
from braces.views import LoginRequiredMixin

from .forms import EquipoForm
from .models import Equipo

class EquipoView(LoginRequiredMixin ,FormView):
	template_name = 'equipo/equipo_form.html'
	form_class = EquipoForm
	success_url = '/'
	login_url = '/main/requerimientos'

	def form_valid(self, form):
		
		form.save()
		return super(EquipoView, self).form_valid(form)

	def form_invalid(self, form):
		print("inválido")
		return super(EquipoView, self).form_invalid(form)

class ListarView(ListView):
	model = Equipo
	template_name = 'equipo/list_equipo.html'
	contexto_object_name = 'equipos'
	