from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_partido(request):
	return HttpResponse("Estoy en views de la app PARTIDO")