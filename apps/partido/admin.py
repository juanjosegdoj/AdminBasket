from django.contrib import admin
from apps.partido.models import Partido

# Register your models here.
@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
	list_display = ('equipoLoc', 'equipoVis', 'fecha', 'ronda', 'cestasLocal', 'cestasVisit', 'faltasLocal', 'faltasVisit')
	list_filter = ('equipoLoc', 'equipoVis',)