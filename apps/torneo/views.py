from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from braces.views import LoginRequiredMixin
from .models import Torneo
# Create your views here.
from .forms import TorneoForm

class MainTorneoView(TemplateView):
	template_name = 'torneo/torneo_main.html'

class FormTorneoView(LoginRequiredMixin ,CreateView): 
	form_class = TorneoForm
	template_name = 'torneo/torneo_form.html'
	success_url = '/torneo/' 
	field = ('nombre', 'deporte') 
	login_url = '/main/requerimientos'

	def form_valid(self, form):
		form.save()
		return super(FormTorneoView, self).form_valid(form)

class ListarView(ListView):
	model = Torneo
	template_name = 'torneo/torneo_list.html'
	context_object_name = "misTorneos"