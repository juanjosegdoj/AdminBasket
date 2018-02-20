from django.contrib import admin
from apps.torneo.models import Torneo

# Register your models here.
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'deporte', 'fecha', 'sexo')