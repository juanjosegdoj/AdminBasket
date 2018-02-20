from django.contrib import admin
from apps.equipo.models import Equipo

# Register your models here.
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
	list_display = ('torneo','nombre','puntos','posicion','partJug',
	'partGan','partPerd','partW','cestAfa','cestCon', 'cestDif')
	
	list_filter = ('torneo',)