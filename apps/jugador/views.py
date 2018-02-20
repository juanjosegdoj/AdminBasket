from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, UpdateView
from braces.views import LoginRequiredMixin

from .forms import JugadorForm
from .models import Jugador

class MainView(TemplateView):
	template_name = 'jugador/jugador_main.html'

class JugadorFormView(LoginRequiredMixin, FormView):
	template_name = 'jugador/jugador_form.html'
	form_class = JugadorForm
	success_url = '../'
	login_url = '/main/requerimientos'
	
	def form_valid(self, form):
		form.save()
		return super(JugadorFormView, self).form_valid(form)

	def form_invalid(self, form):
		print("inválido")
		return super(JugadorFormView, self).form_invalid(form)


def jugadorCreado(request):
	return HttpResponse('El jugador se ha creado en la base de datos con éxito')

def jugadorNOCreado(request):
	return HttpResponse('Algunos datos fueron ingresados incorrectamente')

class JugadorList():
	def sendRender(request):
		jugador = Jugador.objects.all()
		contexto = {'jugadores': jugador}
		return render(request, 'jugador/jugador_list.html', contexto)
