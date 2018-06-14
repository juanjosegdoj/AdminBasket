from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, View, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm, LoginForm

class NuestraMisionView(DetailView):

	template_name = 'main/nuestra_mision.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class LogOut(TemplateView):
	template_name = 'base/fueradeservicio.html'

class RequirLoginView(TemplateView):
	template_name = 'main/required_log.html'

class LoginView(FormView):

	form_class = LoginForm
	template_name = 'main/logout.html'
	success_url = '/'

	def form_valid(self, form):
		user =  authenticate(username= form.cleaned_data['username'],
			password = form.cleaned_data['password'])
		if user is not None:
			if user.is_active:
				login(self.request, user)

		return super(LoginView, self).form_valid(form)


class RegisterUser(FormView):
	form_class = UserForm
	template_name = 'main/registroUsuario.html'
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		user.email = form.cleaned_data['email']
		user.save()
		return super(RegisterUser, self).form_valid(form)

class HomeView(TemplateView):
	template_name = 'main/home.html'

class AboutView(TemplateView):
	template_name = 'main/about.html'
