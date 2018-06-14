from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, View
from django.views.generic.detail import SingleObjectMixin

from django.forms.formsets import formset_factory

from .forms import JugadorForm
from .models import Jugador

class MainView(TemplateView):
	template_name = 'jugador/jugador_main.html'

class JugadorFormView(FormView):
	template_name = 'jugador/jugador_form.html'
	form_class = JugadorForm
	success_url = '../'

	def form_valid(self, form):
		form.save()
		return super(JugadorFormView, self).form_valid(form)

	def form_invalid(self, form):
		return super(JugadorFormView, self).form_invalid(form)

class JugadorList():
	def sendRender(request):
		jugador = Jugador.objects.all()
		contexto = {'jugadores': jugador}
		return render(request, 'jugador/jugador_list.html', contexto)
