from django.contrib import admin
from apps.jugador.models import Jugador

class EntryFilter(admin.SimpleListFilter):

	title = 'Mayores de Edad'
	parameter_name = 'Edad'

	def lookups(self, request, model_admin):
		return(
			('+18', ('Mayores de Edad')),
			('-18', ('Menores de Edad')),
			)

	def queryset(self, request, queryset):
		if self.value() == '+18':
			return queryset.filter(edad__gte = 18)
		elif self.value() == '-18':
			return queryset.filter(edad__lt = 18)

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
	list_display = ('equipo', 'cedula', 'nombres', 'apellidos', 'sexo', 'edad', 'telefono', 'email', 'esMayor')
	list_filter = ('equipo', EntryFilter,)
	list_editable = ('email',)